#!/usr/bin/env python3
"""Orphan-guide checker for the owned site (read-only, idempotent).

Flags any guide page under blog/ that has ZERO inbound links from the site's
crawl/authority surfaces: blog/index.html, the homepage (index.html), and
devforge-tools/blog.html. Orphaned pages get no crawl equity and no human path,
so their keyword surfaces are invisible no matter how good the content is
(4 such orphans found and fixed 2026-08-23, Run 241).

USAGE:
  python3 tools/orphan_page_check.py [--site-root DIR] [--strict]
  python3 tools/orphan_page_check.py --live [--base-url URL] [--strict]

--live mode (added 2026-08-25, Run 254) additionally fetches the PUBLISHED
versions of the three index surfaces and reports:
  * DEAD LIVE LINKS  - blog pages linked from a published index but returning
                       non-200 on the live site (the Run-252 false-claim class:
                       local commits are NOT proof a page is live);
  * PUSH-GAP PAGES   - guide pages committed locally with NO card on any
                       published index surface (shipped-but-invisible until W
                       pushes Pages).
Local-only checks are always run too. Requires network access only in --live.

EXIT: 0 normally; 1 with --strict if any orphan/dead-link/push-gap is found.

Marketing value: run after every new page ship AND during hold-pattern sweeps -
a finished page without an index card is half-shipped (playbook Run-231 rule),
and a finished page without a live card is worth zero (Run-253 lesson). Pair
with tools/linkcheck_portfolio.py.
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

DEFAULT_BASE_URL = "https://coding-dev-tools.github.io"


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


def guide_pages(root: Path) -> list[str]:
    blog_dir = root / "blog"
    return sorted(p.name for p in blog_dir.glob("*.html") if p.name != "index.html")


def links_from(html: str, surface: str) -> set[str]:
    """Return the set of blog/<name>.html guide names linked from one HTML doc."""
    surface_dir = posixpath.dirname(surface)
    out: set[str] = set()
    for href in HREF_RE.findall(html):
        target = normalize(href, surface_dir)
        if target.startswith("blog/") and target.endswith(".html"):
            out.add(target.split("/", 1)[1])
    return out


def fetch(url: str, timeout: int = 20) -> str:
    import urllib.request

    req = urllib.request.Request(
        url, headers={"User-Agent": "orphan-page-check/live-mode"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", "replace")


def check_local(root: Path):
    """Local orphan/dead-link scan. Returns (pages, linked, dead)."""
    pages = guide_pages(root)
    linked: set[str] = set()
    for surface in INDEX_SURFACES:
        f = root / surface
        if not f.exists():
            print(f"WARN: missing index surface {surface}", file=sys.stderr)
            continue
        linked |= links_from(f.read_text(encoding="utf-8", errors="replace"), surface)
    dead = sorted(linked - set(pages))
    return pages, linked, dead


def check_live(base: str, pages: list[str]):
    """Live-site scan. Returns (live_linked_union, dead_live, push_gap)."""
    per_surface: dict[str, set[str]] = {}
    for surface in INDEX_SURFACES:
        url = f"{base.rstrip('/')}/{surface}"
        try:
            html = fetch(url)
        except Exception as e:  # noqa: BLE001 - report and continue
            print(f"WARN: could not fetch live {surface}: {e}", file=sys.stderr)
            per_surface[surface] = set()
            continue
        per_surface[surface] = links_from(html, surface)

    union: set[str] = set()
    for names in per_surface.values():
        union |= names

    dead_live: list[str] = []
    for name in sorted(union):
        url = f"{base.rstrip('/')}/blog/{name}"
        try:
            fetch(url)
        except Exception:  # noqa: BLE001 - any HTTPError/non-2xx counts
            dead_live.append(name)

    push_gap = [p for p in pages if p not in union]
    return union, dead_live, push_gap


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site-root", default=".", help="repo root of Coding-Dev-Tools.github.io")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--live", action="store_true",
                    help="also audit the PUBLISHED site (dead live links + push gaps)")
    ap.add_argument("--base-url", default=DEFAULT_BASE_URL,
                    help=f"published site base URL (default {DEFAULT_BASE_URL})")
    args = ap.parse_args()

    root = Path(args.site_root)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")

    pages, linked, dead = check_local(root)
    problems = False
    print(f"orphan_page_check {stamp}: guides={len(pages)} linked={len(linked)}"
          + (" [live]" if args.live else ""))
    if dead:
        problems = True
        print("DEAD LINKS in local index surfaces (point at missing blog pages):")
        for d in dead:
            print(f"  blog/{d}")
    orphans = [p for p in pages if p not in linked]
    if orphans:
        problems = True
        print("ORPHANS (no inbound link from any local index surface):")
        for o in orphans:
            print(f"  blog/{o}")
    if not dead and not orphans:
        print("missing NONE / dead-links NONE")

    if args.live:
        base = args.base_url
        live_linked, dead_live, push_gap = check_live(base, pages)
        print(f"live audit vs {base}: live-indexed-guides={len(live_linked)}")
        if dead_live:
            problems = True
            print("DEAD LIVE LINKS (linked from a published index, non-200 live):")
            for d in dead_live:
                print(f"  {base}/blog/{d}")
        if push_gap:
            problems = True
            print("PUSH-GAP PAGES (committed locally, absent from every published index):")
            for p in push_gap:
                print(f"  blog/{p}")
        if not dead_live and not push_gap:
            print("live dead-links NONE / push-gap NONE")

    if args.strict and problems:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
