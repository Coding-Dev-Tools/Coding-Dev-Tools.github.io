#!/usr/bin/env python3
"""Portfolio link-integrity checker (read-only, idempotent).

Scans product READMEs / AGENTS.md / owned-site HTML / email-sequence docs under the
GitHub working tree for links into OUR owned surfaces -- coding-dev-tools.github.io and
revenueholdings.dev -- and verifies they resolve against the LOCAL published repos (no
network).

Why local-only:
  * The published Pages site == the local Coding-Dev-Tools.github.io repo.
  * revenueholdings.dev == the local revenueholdings.dev repo (when present).
  Checking on-disk files is authoritative for what is live, and it is safe/offline.

Marketing value: dead links on motivated-visitor paths are silent conversion leaks
(rung 1). Run it each tick; the aggregated report makes the backlog one-click-fresh.

USAGE:
  python3 tools/linkcheck_portfolio.py [--github-root DIR] [--out FILE] [--strict]

EXIT: 0 normally; 1 with --strict if any BROKEN link is found.
"""
from __future__ import annotations
import argparse
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_ROOT = r"C:\Users\jomie\Documents\Github"

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HREF = re.compile(r"""(?:href|src)=["']([^"']+)["']""")
# Stop at whitespace/quotes/angle-brackets/parens so we never swallow an HTML
# attribute tail like  https://x/y.html">text  or a JSON blob.
BARE = re.compile(r"https?://[^\s\"'<>()]+")

SKIP_DIRS = {".git", "node_modules", "__pycache__", "_archive", ".hermes",
             "drafts", ".pytest_cache", ".ruff_cache", ".venv", "venv",
             "claude-local-agent-sessions"}
# Only scan real conversion-surface file types (skip .json tool dumps / state files).
SCAN_SUFFIXES = {".md", ".html", ".xml", ".txt"}

PAGES_HOST = "coding-dev-tools.github.io"
TEMPLATE_CHARS = set("<>{}%&`")


def iter_files(root: Path):
    """Walk the tree but PRUNE skipped dirs (so .git/node_modules are never
    descended into) -- far faster than rglob over a huge working tree."""
    root = str(root)
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            p = Path(dirpath) / fn
            if p.suffix.lower() not in SCAN_SUFFIXES:
                continue
            if fn.startswith("link-audit-") or fn == "linkcheck_portfolio.py":
                continue
            try:
                if p.stat().st_size > 500_000:
                    continue
            except OSError:
                continue
            yield p


def extract_uris(text: str):
    out = []
    for m in MD_LINK.finditer(text):
        out.append(m.group(1).strip())
    for m in HREF.finditer(text):
        out.append(m.group(1).strip())
    for m in BARE.finditer(text):
        out.append(m.group(0))
    cleaned = []
    for u in out:
        if PAGES_HOST not in u and "revenueholdings.dev" not in u:
            continue
        if any(c in u for c in TEMPLATE_CHARS):  # template/placeholder, e.g. <slug>.html
            continue
        cleaned.append(u)
    return cleaned


def cand_rel(rh_root: Path, path: str) -> str:
    return str((rh_root / path.lstrip("/")).relative_to(rh_root))


def resolve(uri: str, pages_root: Path, rh_root):
    """Return (status, target). status in {OK, BROKEN, LIVECHECK, SKIP}."""
    if PAGES_HOST not in uri and "revenueholdings.dev" not in uri:
        return ("SKIP", "")
    if PAGES_HOST in uri:
        idx = uri.find(PAGES_HOST) + len(PAGES_HOST)
        path = uri[idx:].split("#")[0].split("?")[0]
        if path == "" or path.endswith("/"):
            base = path.rstrip("/")
            path = base + "/index.html"
        cand = pages_root / path.lstrip("/")
        if cand.exists():
            return ("OK", "coding-dev-tools.github.io" + path)
        return ("BROKEN", "coding-dev-tools.github.io" + path)
    if uri.startswith("http://revenueholdings.dev") or uri.startswith("https://revenueholdings.dev"):
        idx = uri.find("revenueholdings.dev") + len("revenueholdings.dev")
        path = uri[idx:].split("#")[0].split("?")[0]
        if path == "" or path.endswith("/"):
            base = path.rstrip("/")
            path = base + "/index.html"
        if rh_root is not None and (rh_root / path.lstrip("/")).exists():
            return ("OK", "revenueholdings.dev" + path)
        return ("LIVECHECK", "revenueholdings.dev" + path)
    return ("BROKEN", "coding-dev-tools.github.io/revenueholdings.dev (malformed path form)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--github-root", default=DEFAULT_ROOT)
    ap.add_argument("--out", default=None, help="write markdown report to this file")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any BROKEN link")
    args = ap.parse_args()

    root = Path(args.github_root).resolve()
    pages_root = root / "Coding-Dev-Tools.github.io"
    rh_root = root / "revenueholdings.dev"
    if not pages_root.exists():
        print("ERROR: Pages repo not found at " + str(pages_root), file=sys.stderr)
        sys.exit(2)
    rh = rh_root if rh_root.exists() else None

    ok_count = 0
    broken_by_target = defaultdict(set)   # target -> set of source files
    broken_refs = defaultdict(int)        # target -> total reference count
    livecheck = defaultdict(set)
    for f in iter_files(root):
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        rel = str(f.relative_to(root))
        for uri in extract_uris(text):
            status, target = resolve(uri, pages_root, rh)
            if status == "SKIP":
                continue
            if status == "OK":
                ok_count += 1
                continue
            if status == "BROKEN":
                broken_by_target[target].add(rel)
                broken_refs[target] += 1
            elif status == "LIVECHECK":
                livecheck[target].add(rel)

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = []
    lines.append("Portfolio Link-Integrity Audit - " + ts)
    lines.append("")
    lines.append("Read-only, offline. Verifies every `coding-dev-tools.github.io/...` and "
                 "`revenueholdings.dev` link in product READMEs/AGENTS/site HTML against the "
                 "local published repos. **BROKEN** = file absent from the Pages repo (404 on the "
                 "live site). **LIVECHECK** = needs a live HTTP check (local repo absent).")
    lines.append("")
    lines.append("OK (resolves locally): **" + str(ok_count) + "**")
    lines.append("BROKEN (404 on live site): **" + str(len(broken_by_target)) + " unique targets** ("
                 + str(sum(broken_refs.values())) + " total references)")
    lines.append("LIVECHECK (verify live): " + str(len(livecheck)) + " unique targets")
    lines.append("")

    # Known, already-tracked gap cluster -> report but flag as not-new.
    KNOWN_GAP = "coding-dev-tools.github.io/pypi-index/simple/index.html"

    if broken_by_target:
        lines.append("## BROKEN link clusters (fix these -- highest ROI rung-1)")
        lines.append("")
        lines.append("| Broken target (404 on live site) | Refs | Files | Example sources |")
        lines.append("|-----------------------------|------|-------|-----------------|")
        for target in sorted(broken_by_target, key=lambda t: -broken_refs[t]):
            files = sorted(broken_by_target[target])
            examples = ", ".join("`" + x + "`" for x in files[:3])
            if len(files) > 3:
                examples += ", +" + str(len(files) - 3) + " more"
            note = " _(known Needs-W gap: self-hosted PyPI index not published)_" if target == KNOWN_GAP else ""
            lines.append("| `" + target + "`" + note + " | " + str(broken_refs[target]) + " | "
                         + str(len(files)) + " | " + examples + " |")
        lines.append("")

    if livecheck:
        lines.append("## LIVECHECK (needs a live HTTP check; local repo absent)")
        lines.append("")
        for target, files in sorted(livecheck.items()):
            lines.append("- `" + target + "` -- referenced by " + str(len(files)) + " file(s): "
                         + ", ".join("`" + x + "`" for x in sorted(files)[:3]) + "")
        lines.append("")

    lines.append("## Suggested fixes (honest, one-click next run)")
    lines.append("")
    devforge_broken = [t for t in broken_by_target if "/devforge/" in t and t.endswith(".html")]
    devforge_dev_broken = [t for t in broken_by_target if "devforge.dev" in t]
    rh_path_broken = [t for t in broken_by_target if "revenueholdings.dev (malformed path form)" in t
                      or (PAGES_HOST in t and "revenueholdings.dev" in t)]
    if devforge_broken:
        lines.append("- **DevForge suite hub sub-pages 404 (" + str(len(devforge_broken)) + " targets):** "
                     "the `devforge-fix` repo contains the real built pages (pricing/alternatives/blog/"
                     "docs/quickstart/about.html) but the live `Coding-Dev-Tools.github.io/devforge/` "
                     "folder only has `index.html`. Decision for W: (a) deploy `devforge-fix` to the "
                     "`/devforge/` Pages path, or (b) copy those built pages into "
                     "`Coding-Dev-Tools.github.io/devforge/`. Until then every README link to those "
                     "sub-pages 404s.")
        lines.append("")
    if devforge_dev_broken:
        lines.append("- **`devforge.dev` slug 404s (" + str(len(devforge_dev_broken)) + " targets):** "
                     "`.github/README.md` and `.github/profile/README.md` link to "
                     "`coding-dev-tools.github.io/devforge.dev/...` but the real slug is `devforge` "
                     "(no `.dev`). Repoint those links to `coding-dev-tools.github.io/devforge/`.")
        lines.append("")
    if rh_path_broken:
        lines.append("- **Malformed `revenueholdings.dev` *path* links:** these point at "
                     "`coding-dev-tools.github.io/revenueholdings.dev/...` (a path, not the domain). No "
                     "such directory exists on the Pages repo. Repoint to the real "
                     "`https://revenueholdings.dev/...` domain. Found in json2sql + apiauth + "
                     "SaaS-Churn-Predictor READMEs and devforge-fix sitemap.")
        lines.append("")
    if KNOWN_GAP in broken_by_target:
        lines.append("- **Self-hosted PyPI index (`pypi-index/simple/`) 404s:** already tracked as a "
                     "'Needs W' gap (the index was never published). Not a new finding; W must publish "
                     "the index or accept `git+` as canonical.")
        lines.append("")
    lines.append("---")
    lines.append("Generated by `tools/linkcheck_portfolio.py` at " + ts + ". Re-run each tick; commit the "
                 "report so the backlog stays fresh.")
    report = "\n".join(lines) + "\n"

    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
        print("report written to " + args.out)
    print(report)
    if args.strict and broken_by_target:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
