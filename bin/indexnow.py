#!/usr/bin/env python3
"""Tell IndexNow about URLs that changed in a deploy.

The script is site-agnostic: it reads site.config.json and never contacts
IndexNow when noindex is true, or when the site is amazon-high-ticket.
API and network failures are logged and do not fail the process, so a
deploy workflow can run this after the VPS step without blocking the release.

The key file is public/<indexnow_key>.txt and contains only the key.
IndexNow keys are public by design.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
import traceback
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"
KEY_RE = re.compile(r"\A[A-Za-z0-9-]{8,128}\Z")
ASIN_RE = re.compile(r"\A[A-Z0-9]{10}\Z")
WAIT_SECONDS = 180
POLL_SECONDS = 5
BATCH_SIZE = 10000
DENIED_SLUGS = {"amazon-high-ticket"}
DENIED_DOMAINS = {"amazon-high-ticket.dealsatr.com"}


class Skip(Exception):
    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


def load_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise Skip(f"{path} is not a JSON object")
    return data


def is_noindex(config: dict) -> bool:
    value = config.get("noindex", False)
    return value is True or value == 1 or value == "1" or value == "true"


def denial_reason(config: dict) -> str | None:
    if is_noindex(config):
        return "noindex=true"
    slug = str(config.get("site_slug") or "").strip().lower()
    if slug in DENIED_SLUGS:
        return f"site_slug={slug}"
    domain = str(config.get("domain") or "").strip().lower()
    if domain in DENIED_DOMAINS or domain.startswith("amazon-high-ticket."):
        return f"domain={domain}"
    return None


def indexnow_key(config: dict) -> str:
    key = str(config.get("indexnow_key") or "").strip()
    if not KEY_RE.fullmatch(key):
        raise Skip("indexnow_key missing or not 8-128 letters, digits or dashes")
    return key


def normalize_path(path: str) -> str:
    path = path.strip()
    if path == "":
        return "/"
    path = "/" + path.lstrip("/")
    if path != "/":
        path = path.rstrip("/")
    return path or "/"


def view_public_path(relative: str) -> str | None:
    rel = relative.replace("\\", "/")
    if rel == "app/Views/home.php":
        return "/"
    if rel == "app/Views/sobre-nosotros.php":
        return "/sobre-nosotros"
    prefix = "app/Views/pages/"
    if not rel.startswith(prefix) or not rel.endswith(".php"):
        return None
    slug = rel[len(prefix):-4]
    if slug == "" or slug.endswith("/"):
        return None
    return "/" + slug


def parse_name_status(text: str) -> list[str]:
    """Paths added, modified or renamed. Deletions are left out."""
    paths: list[str] = []
    for line in text.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        status = parts[0]
        if status.startswith(("R", "C")) and len(parts) >= 3:
            paths.append(parts[2])
            continue
        if status[:1] in {"A", "M", "T"} and len(parts) >= 2:
            paths.append(parts[1])
    return paths


def git_name_status(site: Path, before: str, after: str) -> str:
    if before.strip() == "" or set(before) <= {"0"}:
        raise Skip("no previous deploy commit; nothing to submit")
    exists = subprocess.run(
        ["git", "cat-file", "-e", f"{before}^{{commit}}"],
        cwd=site,
        capture_output=True,
        text=True,
        check=False,
    )
    if exists.returncode != 0:
        raise Skip(f"previous commit {before} is not in this checkout")
    diff = subprocess.run(
        ["git", "diff", "--name-status", "--find-renames", before, after],
        cwd=site,
        capture_output=True,
        text=True,
        check=False,
    )
    if diff.returncode != 0:
        raise Skip(diff.stderr.strip() or "git diff failed")
    return diff.stdout


def changed_public_paths(site: Path, name_status: str) -> list[str]:
    paths = parse_name_status(name_status)
    publics: list[str] = []
    asins: list[str] = []
    for relative in paths:
        rel = relative.replace("\\", "/")
        public = view_public_path(rel)
        if public is not None:
            publics.append(public)
            continue
        marker = "content/products/"
        if rel.startswith(marker) and rel.endswith(".json"):
            stem = Path(rel).stem
            if ASIN_RE.fullmatch(stem):
                asins.append(stem)

    if asins:
        views = site / "app" / "Views"
        if views.is_dir():
            for php in sorted(views.rglob("*.php")):
                rel = php.relative_to(site).as_posix()
                try:
                    text = php.read_text(encoding="utf-8")
                except OSError:
                    continue
                if any(asin in text for asin in asins):
                    public = view_public_path(rel)
                    if public is not None:
                        publics.append(public)
    return publics


def absolute_urls(config: dict, publics: list[str]) -> list[str]:
    base = str(config.get("base_url") or "").rstrip("/")
    domain = str(config.get("domain") or "").strip().lower()
    if base == "" or domain == "":
        raise Skip("site.config.json needs base_url and domain")
    exclude = set()
    listed = config.get("sitemap_exclude") or []
    if isinstance(listed, list):
        for item in listed:
            if isinstance(item, str):
                exclude.add(normalize_path(item))

    urls: list[str] = []
    seen: set[str] = set()
    for public in publics:
        path = normalize_path(public)
        if path in exclude or path in seen:
            continue
        seen.add(path)
        url = base + "/" if path == "/" else base + path
        host = (urlparse(url).hostname or "").lower()
        if host != domain:
            continue
        urls.append(url)
    return urls


def key_location(config: dict, key: str) -> str:
    base = str(config.get("base_url") or "").rstrip("/")
    return f"{base}/{key}.txt"


def write_key_file(site: Path, config: dict) -> None:
    reason = denial_reason(config)
    if reason is not None:
        print(f"indexnow: skipped write-key ({reason})")
        return
    key = indexnow_key(config)
    path = site / "public" / f"{key}.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(key.encode("ascii"))
    print(f"indexnow: wrote {path}")


def fetch(url: str, timeout: int = 20) -> tuple[int, str]:
    request = urllib.request.Request(url, headers={"User-Agent": "indexnow-deploy"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            status = getattr(response, "status", 200)
            body = response.read().decode("utf-8", "replace")
            return int(status), body
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        return int(exc.code), body


def wait_for(label: str, ready, timeout: int = WAIT_SECONDS) -> bool:
    deadline = time.time() + timeout
    while True:
        ok, detail = ready()
        if ok:
            print(f"indexnow: {label} ready ({detail})")
            return True
        remaining = deadline - time.time()
        if remaining <= 0:
            print(f"indexnow: {label} not ready ({detail})", file=sys.stderr)
            return False
        print(f"indexnow: waiting for {label} ({detail})")
        time.sleep(min(POLL_SECONDS, remaining))


def key_is_live(location: str, key: str) -> tuple[bool, str]:
    try:
        status, body = fetch(location)
    except Exception as exc:
        return False, str(exc)
    if status == 200 and body.strip() == key:
        return True, location
    return False, f"status={status}"


def url_is_live(url: str) -> tuple[bool, str]:
    try:
        status, _body = fetch(url)
    except Exception as exc:
        return False, str(exc)
    if status == 200:
        return True, url
    return False, f"{url} status={status}"


def post_indexnow(host: str, key: str, location: str, urls: list[str]) -> int:
    payload = {
        "host": host,
        "key": key,
        "keyLocation": location,
        "urlList": urls,
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        INDEXNOW_ENDPOINT,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            status = int(getattr(response, "status", 200))
            body = response.read().decode("utf-8", "replace").strip()
            print(f"indexnow: POST {status} {body}")
            return status
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace").strip()
        print(f"indexnow: POST failed {exc.code} {body}", file=sys.stderr)
        return int(exc.code)
    except OSError as exc:
        print(f"indexnow: POST failed ({exc})", file=sys.stderr)
        return 0


def submit(site: Path, config: dict, before: str, after: str, dry_run: bool) -> None:
    reason = denial_reason(config)
    if reason is not None:
        print(f"indexnow: skipped ({reason}); not submitting")
        return
    key = indexnow_key(config)
    name_status = git_name_status(site, before, after)
    urls = absolute_urls(config, changed_public_paths(site, name_status))
    if not urls:
        print("indexnow: no changed urls")
        return
    host = str(config.get("domain") or "").strip().lower()
    location = key_location(config, key)
    print("indexnow: changed urls:")
    for url in urls:
        print(f"indexnow: - {url}")
    if dry_run:
        print("indexnow: dry-run; not posting")
        return
    if not wait_for("key file", lambda: key_is_live(location, key)):
        print("indexnow: key file was not live; not posting", file=sys.stderr)
        return
    pending = list(urls)

    def pages_ready() -> tuple[bool, str]:
        for url in pending:
            ok, detail = url_is_live(url)
            if not ok:
                return False, detail
        return True, f"{len(pending)} urls"

    if not wait_for("changed pages", pages_ready):
        print("indexnow: a changed page was not live; not posting", file=sys.stderr)
        return
    for start in range(0, len(urls), BATCH_SIZE):
        batch = urls[start:start + BATCH_SIZE]
        try:
            status = post_indexnow(host, key, location, batch)
        except Exception as exc:
            print(f"indexnow: POST failed ({exc})", file=sys.stderr)
            return
        if status not in (200, 202):
            print(f"indexnow: unexpected status {status}", file=sys.stderr)
            return
        print(f"indexnow: accepted {len(batch)} urls with status {status}")


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", required=True, type=Path)
    parser.add_argument("--write-key", action="store_true")
    parser.add_argument("--before", default="")
    parser.add_argument("--after", default="HEAD")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    site = args.site.resolve()
    try:
        config = load_json(site / "site.config.json")
        if args.write_key:
            write_key_file(site, config)
        # --write-key alone prepares the file. A before/after range also submits.
        if args.before.strip() == "" and not args.dry_run:
            if args.write_key:
                return 0
            print("indexnow: skipped (pass --before from the previous deploy)")
            return 0
        submit(site, config, args.before, args.after, args.dry_run)
    except Skip as exc:
        print(f"indexnow: skipped ({exc.reason})")
    return 0


def main(argv: list[str] | None = None) -> int:
    try:
        return run(argv)
    except SystemExit as exc:
        code = exc.code
        if code in (None, 0):
            return 0
        return int(code) if isinstance(code, int) else 1
    except Exception:
        traceback.print_exc()
        print("indexnow: failed; deploy continues", file=sys.stderr)
        return 0


if __name__ == "__main__":
    sys.exit(main())
