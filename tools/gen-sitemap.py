#!/usr/bin/env python
"""Generate hub-root sitemap.xml + robots.txt for coding-dev-tools.github.io.

Run 249 (2026-08-24). Reusable: re-run after any new pages go LIVE to refresh lastmod/URLs.
Safety properties:
  - Candidate URLs come from the LOCAL main tree (git ls-tree).
  - A URL enters sitemap.xml ONLY if it returns HTTP 200 on the LIVE site right now,
    so queued-but-unpushed pages are never submitted as crawl targets.
  - Output XML is validated by parsing before anything is written next to it.
Usage:  python tools/gen-sitemap.py          (from repo root)
"""
import subprocess, sys, os, datetime, xml.etree.ElementTree as ET
from urllib.request import urlopen

BASE = "https://coding-dev-tools.github.io/"
NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"

def tree_html_paths():
    out = subprocess.run(["git", "ls-tree", "-r", "main", "--name-only"],
                         capture_output=True, text=True, check=True).stdout
    return sorted(p for p in out.splitlines() if p.endswith(".html"))

def live_ok(url):
    try:
        with urlopen(url, timeout=15) as r:
            return r.status == 200
    except Exception:
        return False

def lastmod(path):
    d = subprocess.run(["git", "log", "-1", "--format=%cI", "main", "--", path],
                       capture_output=True, text=True, check=True).stdout.strip()
    return d[:10] or datetime.date.today().isoformat()

def tier(path):
    if path == "index.html":
        return "1.0", "weekly"
    if path.endswith("index.html"):
        return "0.8", "weekly"
    if path.startswith("blog/"):
        return "0.7", "monthly"
    return "0.6", "monthly"

def main():
    rows, skipped = [], []
    for p in tree_html_paths():
        if live_ok(BASE + p):
            pri, cf = tier(p)
            rows.append((p, lastmod(p), pri, cf))
        else:
            skipped.append(p)
    rows.sort(key=lambda r: (r[3], r[0]))
    today = datetime.date.today().isoformat()
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
             f'<!-- Generated {today} by tools/gen-sitemap.py. Lists ONLY pages verified HTTP 200',
             '     on the LIVE site at generation time; not-yet-live pages are excluded until they resolve. -->']
    for p, lm, pri, cf in rows:
        lines += ["  <url>", f"    <loc>{BASE}{p}</loc>", f"    <lastmod>{lm}</lastmod>",
                  f"    <changefreq>{cf}</changefreq>", f"    <priority>{pri}</priority>", "  </url>"]
    lines.append("</urlset>")
    xml = "\n".join(lines) + "\n"
    root = ET.fromstring(xml)  # validate BEFORE writing
    locs = [e.text for e in root.iter(NS + "loc")]
    assert len(locs) == len(rows) == len(set(locs)), "loc/count mismatch"
    with open("sitemap.xml", "w", encoding="utf-8", newline="\n") as f:
        f.write(xml)
    with open("robots.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write("User-agent: *\nAllow: /\n\n"
                f"Sitemap: {BASE}sitemap.xml\n")
    print(f"sitemap.xml: {len(locs)} URLs (parse OK); robots.txt written")
    print(f"excluded (not live yet): {len(skipped)} -> {', '.join(skipped)}")

if __name__ == "__main__":
    sys.exit(main())
