#!/usr/bin/env python3
"""Replace {{product:ASIN.figure}} tokens with a lazy-loaded <figure>.

Must run before ci4-base build-pages.py: that tool HTML-escapes ordinary
product fields and fails the build on any leftover {{ token. This script
writes the figure HTML into the views first, so build-pages only has to
resolve the remaining product, compare and site tokens.

Official packshots are stored as base64 in content/product-images/images.json
and decoded into public/img/products/ at the start of this script.
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import sys
from pathlib import Path

TOKEN_PREFIX = "{{product:"
TOKEN_SUFFIX = ".figure}}"


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



def load_image_payloads(site: Path) -> dict[str, bytes]:
    srcdir = site / "content" / "product-images"
    payloads: dict[str, bytes] = {}
    manifest = srcdir / "images.json"
    if manifest.is_file():
        raw = json.loads(manifest.read_text(encoding="utf-8"))
        for asin, encoded in raw.items():
            payloads[asin] = base64.b64decode(encoded)
    for path in srcdir.glob("*.webp.b64"):
        payloads[path.name.removesuffix(".webp.b64")] = base64.b64decode(
            path.read_text(encoding="ascii")
        )
    return payloads


def materialize_images(site: Path, products: dict[str, dict], errors: list[str]) -> int:
    """Decode official packshots into public/img/products from content/product-images."""
    payloads = load_image_payloads(site)
    written = 0
    for asin, product in products.items():
        src = product.get("image") or f"/img/products/{asin}.webp"
        dest = image_file(site, src)
        if asin in payloads:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(payloads[asin])
            written += 1
        elif not dest.is_file():
            errors.append(f"missing image for {asin}: no {dest} and no base64 source")
    print(f"product-figures: wrote {written} images from base64 sources")
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", default=".", help="Site repository root")
    args = parser.parse_args()
    site = Path(args.site).resolve()
    products = load_products(site)
    errors: list[str] = []
    materialize_images(site, products, errors)

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
        text = path.read_text(encoding="utf-8")
        leftover += text.count(TOKEN_SUFFIX)

    print(f"product-figures: replaced {replaced} figures in {files} views")
    if leftover:
        errors.append(f"{leftover} unresolved {TOKEN_SUFFIX} token(s)")
    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        return 1
    if replaced == 0:
        print("product-figures: no figure tokens found", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
