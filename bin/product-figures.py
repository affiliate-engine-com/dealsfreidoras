#!/usr/bin/env python3
"""Build product figures and comparison-table thumbnails.

Must run once before ci4-base build-pages.py: that tool HTML-escapes ordinary
product fields and fails the build on any leftover {{ token. This script
writes figure HTML into the views first, so build-pages only has to resolve
the remaining product, compare and site tokens.

After build-pages, run again with --inject-table-thumbs to place a 120px
thumbnail in each comparison-table "Modelo" cell.

Official packshots live as base64 in content/product-images/images.json
(and thumbs.json). They are decoded into public/img/products/ at the start
of a normal run.
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import re
import sys
from pathlib import Path

TOKEN_PREFIX = "{{product:"
TOKEN_SUFFIX = ".figure}}"
ROW_RE = re.compile(
    r'(<(?:th|td)\b[^>]*scope="row"[^>]*>)\s*'
    r'(<a\b[^>]*href="#([^"]+)"[^>]*>)(.*?)(</a>)',
    re.IGNORECASE | re.DOTALL,
)


def load_products(site: Path) -> dict[str, dict]:
    products: dict[str, dict] = {}
    folder = site / "content" / "products"
    if not folder.is_dir():
        raise SystemExit(f"missing product folder: {folder}")
    for path in sorted(folder.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        asin = data.get("asin") or path.stem
        products[asin] = data
    return products


def image_file(site: Path, src: str) -> Path:
    relative = src[1:] if src.startswith("/") else src
    return site / "public" / relative if src.startswith("/") else site / relative


def thumb_src(product: dict) -> str:
    explicit = product.get("image_thumb")
    if explicit:
        return explicit
    src = product.get("image") or f"/img/products/{product['asin']}.webp"
    if src.endswith(".webp") and not src.endswith("-thumb.webp"):
        return src[:-5] + "-thumb.webp"
    return f"/img/products/{product['asin']}-thumb.webp"


def figure_html(product: dict) -> str:
    asin = product["asin"]
    src = product.get("image") or f"/img/products/{asin}.webp"
    alt = product.get("image_alt") or product.get("full_name") or asin
    width = int(product.get("image_width") or 1000)
    height = int(product.get("image_height") or 1000)
    credit = product.get("image_credit") or {}
    if isinstance(credit, str):
        brand = credit
        url = ""
    else:
        brand = credit.get("name") or product.get("brand") or ""
        url = (credit.get("url") or "").strip()
    note = (product.get("image_note") or "").strip()

    img = (
        f'<img src="{html.escape(src, quote=True)}" '
        f'alt="{html.escape(alt, quote=True)}" '
        f'width="{width}" height="{height}" loading="lazy" decoding="async">'
    )
    label = f"Imagen: {html.escape(brand)}" if brand else "Imagen"
    if url:
        caption = (
            f'<a href="{html.escape(url, quote=True)}" '
            f'rel="nofollow noopener">{label}</a>'
        )
    else:
        caption = label
    if note:
        caption += f" {html.escape(note)}"
    return (
        f'<figure class="product-figure">{img}'
        f"<figcaption>{caption}</figcaption></figure>"
    )


def load_b64_manifest(path: Path) -> dict[str, bytes]:
    if not path.is_file():
        return {}
    raw = json.loads(path.read_text(encoding="utf-8"))
    return {asin: base64.b64decode(encoded) for asin, encoded in raw.items()}


def load_image_payloads(site: Path) -> dict[str, bytes]:
    srcdir = site / "content" / "product-images"
    payloads = load_b64_manifest(srcdir / "images.json")
    for path in srcdir.glob("*.webp.b64"):
        payloads[path.name.removesuffix(".webp.b64")] = base64.b64decode(
            path.read_text(encoding="ascii")
        )
    return payloads


def write_webp(dest: Path, payload: bytes) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(payload)


def materialize_images(site: Path, products: dict[str, dict], errors: list[str]) -> int:
    """Decode packshots and thumbnails into public/img/products."""
    payloads = load_image_payloads(site)
    thumbs = load_b64_manifest(site / "content" / "product-images" / "thumbs.json")
    written = 0
    for asin, product in products.items():
        src = product.get("image") or f"/img/products/{asin}.webp"
        dest = image_file(site, src)
        if asin in payloads:
            write_webp(dest, payloads[asin])
            written += 1
        elif not dest.is_file():
            errors.append(f"missing image for {asin}: no {dest} and no base64 source")
        tdest = image_file(site, thumb_src(product))
        if asin in thumbs:
            write_webp(tdest, thumbs[asin])
            written += 1
        elif not tdest.is_file():
            errors.append(f"missing thumbnail for {asin}: no {tdest} and no thumbs.json entry")
    print(f"product-figures: wrote {written} image files from base64 sources")
    return written


def replace_tokens(text: str, products: dict, site: Path, origin: str, errors: list[str]) -> tuple[str, int]:
    count = 0
    out: list[str] = []
    i = 0
    while True:
        start = text.find(TOKEN_PREFIX, i)
        if start == -1:
            out.append(text[i:])
            break
        mid = start + len(TOKEN_PREFIX)
        end = text.find(TOKEN_SUFFIX, mid)
        if end == -1 or end - mid != 10 or not text[mid:end].isalnum() or not text[mid:end].isupper():
            out.append(text[i:mid])
            i = mid
            continue
        asin = text[mid:end]
        out.append(text[i:start])
        product = products.get(asin)
        if not product:
            errors.append(f"{origin}: no JSON for {asin}")
            out.append(text[start:end + len(TOKEN_SUFFIX)])
            i = end + len(TOKEN_SUFFIX)
            continue
        src = product.get("image") or f"/img/products/{asin}.webp"
        path = image_file(site, src)
        if not path.is_file():
            errors.append(f"{origin}: missing image for {asin} at {path}")
        out.append(figure_html(product))
        count += 1
        i = end + len(TOKEN_SUFFIX)
    return "".join(out), count


def replace_figure_tokens(site: Path, products: dict[str, dict], errors: list[str]) -> int:
    views = site / "app" / "Views"
    if not views.is_dir():
        raise SystemExit(f"missing views folder: {views}")

    replaced = 0
    files = 0
    for path in sorted(views.rglob("*.php")):
        original = path.read_text(encoding="utf-8")
        if TOKEN_PREFIX not in original or TOKEN_SUFFIX not in original:
            continue
        updated, count = replace_tokens(original, products, site, str(path), errors)
        if count:
            path.write_text(updated, encoding="utf-8")
            files += 1
            replaced += count

    leftover = 0
    for path in sorted(views.rglob("*.php")):
        leftover += path.read_text(encoding="utf-8").count(TOKEN_SUFFIX)

    print(f"product-figures: replaced {replaced} figures in {files} views")
    if leftover:
        errors.append(f"{leftover} unresolved {TOKEN_SUFFIX} token(s)")
    if replaced == 0:
        errors.append("no figure tokens found")
    return replaced


def thumb_html(product: dict) -> str:
    alt = product.get("image_alt") or product.get("full_name") or product["asin"]
    src = thumb_src(product)
    return (
        f'<img class="compare-thumb" src="{html.escape(src, quote=True)}" '
        f'alt="{html.escape(alt, quote=True)}" width="120" height="120" '
        f'loading="lazy" decoding="async">'
    )


def inject_table_thumbs(site: Path, products: dict[str, dict], errors: list[str]) -> int:
    by_anchor = {str(p.get("anchor") or ""): p for p in products.values() if p.get("anchor")}
    views = site / "app" / "Views"
    injected = 0
    files = 0
    unresolved = 0
    for path in sorted(views.rglob("*.php")):
        original = path.read_text(encoding="utf-8")
        if 'class="comparison-table"' not in original and "class='comparison-table'" not in original:
            continue

        def repl(match: re.Match[str]) -> str:
            nonlocal injected, unresolved
            prefix, open_a, anchor, inner, close_a = match.groups()
            if 'class="compare-thumb"' in inner:
                return match.group(0)
            product = by_anchor.get(anchor)
            if not product:
                unresolved += 1
                errors.append(f"{path}: no product for table anchor #{anchor}")
                return match.group(0)
            tdest = image_file(site, thumb_src(product))
            if not tdest.is_file():
                errors.append(f"{path}: missing thumb file for {product['asin']} at {tdest}")
            # Keep the existing name, wrap as a flex row: thumb + label
            label = inner.strip()
            if not label.startswith("<"):
                label = f"<span>{label}</span>"
            open_with_class = open_a
            if "compare-model" not in open_a:
                if 'class="' in open_a:
                    open_with_class = open_a.replace('class="', 'class="compare-model ', 1)
                elif "class='" in open_a:
                    open_with_class = open_a.replace("class='", "class='compare-model ", 1)
                else:
                    open_with_class = open_a.replace("<a ", '<a class="compare-model" ', 1)
            injected += 1
            return f"{prefix}{open_with_class}{thumb_html(product)}{label}{close_a}"

        updated = ROW_RE.sub(repl, original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            files += 1

    print(f"product-figures: injected {injected} table thumbnails in {files} views")
    if injected == 0:
        errors.append("no comparison-table model rows found to inject")
    return injected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", default=".", help="Site repository root")
    parser.add_argument(
        "--inject-table-thumbs",
        action="store_true",
        help="Post-process comparison tables after build-pages.py",
    )
    args = parser.parse_args()
    site = Path(args.site).resolve()
    products = load_products(site)
    errors: list[str] = []

    if args.inject_table_thumbs:
        inject_table_thumbs(site, products, errors)
    else:
        materialize_images(site, products, errors)
        replace_figure_tokens(site, products, errors)

    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
