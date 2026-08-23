#!/usr/bin/env python3
"""Orphan-guide checker for the owned site (read-only, idempotent).

Flags any guide page under blog/ that has ZERO inbound links from the site's
crawl/authority surfaces: blog/index.html, the homepage (index.html), and
devforge-tools/blog.html. Orphaned pages get no crawl equity and no human path,
so their keyword surfaces are invisible no matter how good the content is
(4 such orphans found and fixed 2026-08-23, Run 241).

USAGE:
  python3 tools/orphan_page_check.py [--site-root DIR] [--strict]

EXIT: 0 normally; 1 with --strict if any orphan is found.

Marketing value: run after every new page ship — a finished page without an
index card is half-shipped (playbook Run-231 rule). Pair with
tools/linkcheck_portfolio.py.
"""
from __future__ import annotations

import argparse
import posixpath
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HREF_RE = re.compile(r"""href=["']([^"'#?]+)["']""", re.I)

INDEX_SURFACES = [
    "blog/index.html",        # primary crawl hub for guides
    "index.html",             # homepage = highest-authority page
    "devforge-tools/blog.html",
]


def normalize(href: str, surface_dir: str) -> str:
    """Resolve href against the surface page's own directory to a site-root path."""
    href = href.strip()
    if href.startswith(("http://", "https://")):
        m = re.match(r"https?://[^/]+/(.+)$", href)
        if not m:
            return ""
        href = m.group(1)
    elif not href.startswith("/"):
        # relative href: resolve against the linking page's directory
        href = posixpath.normpath(posixpath.join(surface_dir, href))
    return href.lstrip("./")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site-root", default=".", help="repo root of Coding-Dev-Tools.github.io")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    root = Path(args.site_root)
    blog_dir = root / "blog"
    pages = sorted(p.name for p in blog_dir.glob("*.html") if p.name != "index.html")

    linked: set[str] = set()
    for surface in INDEX_SURFACES:
        f = root / surface
        if not f.exists():
            print(f"WARN: missing index surface {surface}", file=sys.stderr)
            continue
        html = f.read_text(encoding="utf-8", errors="replace")
        surface_dir = posixpath.dirname(surface)
        for href in HREF_RE.findall(html):
            target = normalize(href, surface_dir)
            if target.startswith("blog/") and target.endswith(".html"):
                linked.add(target.split("/", 1)[1])

    orphans = [p for p in pages if p not in linked]
    dead = sorted(linked - set(pages))

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    print(f"orphan_page_check {stamp}: guides={len(pages)} linked={len(linked)}")
    if dead:
        print("DEAD LINKS in index surfaces (point at missing blog pages):")
        for d in dead:
            print(f"  blog/{d}")
    if orphans:
        print("ORPHANS (no inbound link from any index surface):")
        for o in orphans:
            print(f"  blog/{o}")
        return 1 if args.strict else 0
    print("missing NONE / dead-links " + ("FOUND" if dead else "NONE"))
    return 1 if (args.strict and dead) else 0


if __name__ == "__main__":
    sys.exit(main())
