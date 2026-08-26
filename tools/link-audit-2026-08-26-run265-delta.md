# Portfolio link-integrity delta audit - 2026-08-26 (Run 265)

Baseline: `tools/link-audit-2026-08-25.md` (Run 253) + run261 delta.
Method: `python tools/linkcheck_portfolio.py` full re-run at 2026-08-26T06:54Z + `hold-sweep.sh` (push-state x8 + live facts + site-health).

## Result: ZERO new broken clusters vs 08-25 baseline

| Metric | 08-25 | 08-26 | Delta |
|---|---|---|---|
| OK (resolves locally) | 401* | 396 | -5 |
| BROKEN unique targets | 97 | 97 | 0 |
| Total references | 1486 | 1486 | 0 |
| LIVECHECK targets | 6 | 6 | 0 |

*OK-count drift (-5) comes from guides/pages added locally since the 08-25 snapshot referencing existing targets differently; every newly-added link resolves locally (orphan checker same run: guides=31 linked=31, dead-links NONE).

## Broken-cluster composition unchanged
1. `devforge/*` sub-pages exist only in the unpushed `devforge-fix` repo (84 targets) - W deploy decision pending.
2. Malformed `coding-dev-tools.github.io/revenueholdings.dev/...` path links - fixes sit on unpushed branches (see push-manifest).
3. Dead `pypi-index/simple/` refs - W republish decision pending.

## Push-state sweep (same run)
HOLD on all 8 tracked origin defaults vs baseline - zero pushes since Run 238; all accumulated fix work remains invisible live.

## Live facts re-verified this run
- pypi-index/simple: HTTP 404 (do NOT advertise --index-url)
- hub root coding-dev-tools.github.io: HTTP 200
- revenueholdings.dev: NXDOMAIN

## Site health (Pages local main @ 2b43457)
guides=31 linked=31 / missing NONE / dead-links NONE.

Conclusion: no new conversion-surface leaks; the single highest-ROI action remains the W push (local Pages main now 27+ commits ahead) plus devforge-fix deploy decision.
