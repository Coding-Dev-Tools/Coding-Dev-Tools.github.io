Portfolio Link-Integrity Audit - 2026-07-18T00:36:28Z

Read-only, offline. Verifies every `coding-dev-tools.github.io/...` and `revenueholdings.dev` link in product READMEs/AGENTS/site HTML against the local published repos. **BROKEN** = file absent from the Pages repo (404 on the live site). **LIVECHECK** = needs a live HTTP check (local repo absent).

OK (resolves locally): **211**
BROKEN (404 on live site): **91 unique targets** (758 total references)
LIVECHECK (verify live): 6 unique targets

## BROKEN link clusters (fix these -- highest ROI rung-1)

| Broken target (404 on live site) | Refs | Files | Example sources |
|-----------------------------|------|-------|-----------------|
| `coding-dev-tools.github.io/devforge/og-image.svg` | 106 | 53 | `devforge-fix\about.html`, `devforge-fix\alternatives.html`, `devforge-fix\blog.html`, +50 more |
| `coding-dev-tools.github.io/pypi-index/simple/index.html` _(known Needs-W gap: self-hosted PyPI index not published)_ | 30 | 18 | `Coding-Dev-Tools.github.io\blog\envault-scan-prevent-env-leaks-in-git.html`, `Coding-Dev-Tools.github.io\blog\envault-secret-rotation-workflow.html`, `Coding-Dev-Tools.github.io\templates\seo-blog-page.template.html`, +15 more |
| `coding-dev-tools.github.io/devforge/pricing.html` | 16 | 7 | `.github\README.md`, `Coding-Dev-Tools.github.io\blog\datamorph-schema-validation-in-ci.html`, `datamorph\README.md`, +4 more |
| `coding-dev-tools.github.io/devforge/about.html` | 14 | 6 | `.github\profile\README.md`, `devforge-fix\README.md`, `devforge-fix\about.html`, +3 more |
| `coding-dev-tools.github.io/devforge/blog.html` | 12 | 5 | `.github\README.md`, `devforge-fix\README.md`, `devforge-fix\blog.html`, +2 more |
| `coding-dev-tools.github.io/devforge/docs.html` | 10 | 5 | `.github\README.md`, `devforge-fix\README.md`, `devforge-fix\blog\license-key-rate-limiting-cli-tools.html`, +2 more |
| `coding-dev-tools.github.io/devforge/blog/apighost-advanced-mock-patterns.html` | 10 | 3 | `devforge-fix\blog\apighost-advanced-mock-patterns.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/json-to-sql-one-command.html` | 10 | 3 | `devforge-fix\blog\json-to-sql-one-command.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/before-you-deploy-config-drift-and-cost.html` | 10 | 3 | `devforge-fix\blog\before-you-deploy-config-drift-and-cost.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/click-to-mcp-og.svg` | 10 | 5 | `devforge-fix\blog\click-to-mcp-intro.html`, `devforge-fix\blog\click-to-mcp-three-distribution-channels.html`, `devforge-fix\blog\click-to-mcp-three-transport-modes.html`, +2 more |
| `coding-dev-tools.github.io/devforge/blog/mcp-server-directories-where-to-list-your-server.html` | 9 | 4 | `devforge-fix\blog\get-your-cli-tool-listed-awesome-directories.html`, `devforge-fix\blog\mcp-server-directories-where-to-list-your-server.html`, `devforge-fix\feed.xml`, +1 more |
| `coding-dev-tools.github.io/devforge/blog/revenue-hits-680-developers.html` | 9 | 3 | `devforge-fix\blog\revenue-hits-680-developers.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/five-productivity-workflows-cli-suite.html` | 9 | 3 | `devforge-fix\blog\five-productivity-workflows-cli-suite.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/python-cli-to-mcp-server.html` | 9 | 3 | `devforge-fix\blog\python-cli-to-mcp-server.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/autonomous-ai-experiment.html` | 9 | 3 | `devforge-fix\blog\autonomous-ai-experiment.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/start-here.html` | 9 | 4 | `devforge-fix\blog\license-key-rate-limiting-cli-tools.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +1 more |
| `coding-dev-tools.github.io/devforge/blog/preview-infra-cost-before-deploy.html` | 9 | 4 | `devforge-fix\blog\preview-infra-cost-before-deploy.html`, `devforge-fix\blog\revenue-hits-680-developers.html`, `devforge-fix\feed.xml`, +1 more |
| `coding-dev-tools.github.io/devforge/blog/new-cli-features-may-18-2026.html` | 8 | 3 | `devforge-fix\blog\new-cli-features-may-18-2026.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/api-key-management-from-terminal.html` | 8 | 3 | `devforge-fix\blog\api-key-management-from-terminal.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/schemaforge-v0-5-0-sqlalchemy.html` | 8 | 3 | `devforge-fix\blog\schemaforge-v0-5-0-sqlalchemy.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/sync-env-variables-across-environments.html` | 8 | 3 | `devforge-fix\blog\sync-env-variables-across-environments.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/api-mock-server-from-openapi-spec.html` | 8 | 3 | `devforge-fix\blog\api-mock-server-from-openapi-spec.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/catch-config-drift-before-production.html` | 8 | 3 | `devforge-fix\blog\catch-config-drift-before-production.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/clean-up-react-dead-code.html` | 8 | 3 | `devforge-fix\blog\clean-up-react-dead-code.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/python-cli-type-safe-pep561.html` | 8 | 3 | `devforge-fix\blog\python-cli-type-safe-pep561.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/envault-serve-http-api-secrets.html` | 8 | 3 | `devforge-fix\blog\envault-serve-http-api-secrets.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/monetize-mcp-servers-x402-mpp.html` | 8 | 3 | `devforge-fix\blog\monetize-mcp-servers-x402-mpp.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/cli-tools-as-mcp-servers.html` | 8 | 3 | `devforge-fix\blog\cli-tools-as-mcp-servers.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/quickstart.html` | 8 | 4 | `devforge-fix\README.md`, `devforge-fix\blog\license-key-rate-limiting-cli-tools.html`, `devforge-fix\quickstart.html`, +1 more |
| `coding-dev-tools.github.io/devforge/alternatives.html` | 7 | 3 | `devforge-fix\README.md`, `devforge-fix\alternatives.html`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/schemaforge-vs-prisma-migrate-vs-alembic-vs-atlas.html` | 7 | 3 | `devforge-fix\blog\schemaforge-vs-prisma-migrate-vs-alembic-vs-atlas.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/apicontractguardian-vs-oasdiff-vs-optic-vs-openapi-diff.html` | 7 | 3 | `devforge-fix\blog\apicontractguardian-vs-oasdiff-vs-optic-vs-openapi-diff.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/apicontractguardian-ci-cd-gating-breaking-api-changes.html` | 7 | 3 | `devforge-fix\blog\apicontractguardian-ci-cd-gating-breaking-api-changes.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/mcp-everywhere-why-your-cli-tools-need-it.html` | 7 | 3 | `devforge-fix\blog\mcp-everywhere-why-your-cli-tools-need-it.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/click-to-mcp-usage-guide.html` | 7 | 3 | `devforge-fix\blog\click-to-mcp-usage-guide.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/white-label-ai-agent-deployment.html` | 7 | 3 | `devforge-fix\blog\white-label-ai-agent-deployment.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/get-your-cli-tool-listed-awesome-directories.html` | 7 | 3 | `devforge-fix\blog\get-your-cli-tool-listed-awesome-directories.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/click-vs-typer-vs-argparse-python-cli.html` | 7 | 3 | `devforge-fix\blog\click-vs-typer-vs-argparse-python-cli.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/ci-cd-python-cli-tools-guide.html` | 7 | 3 | `devforge-fix\blog\ci-cd-python-cli-tools-guide.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/10-open-source-cli-tools-ai-development.html` | 7 | 3 | `devforge-fix\blog\10-open-source-cli-tools-ai-development.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/ai-built-cli-tools-zero-humans.html` | 7 | 3 | `devforge-fix\blog\ai-built-cli-tools-zero-humans.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/license-key-rate-limiting-cli-tools.html` | 7 | 3 | `devforge-fix\blog\license-key-rate-limiting-cli-tools.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/datamorph-batch-data-conversion.html` | 7 | 3 | `devforge-fix\blog\datamorph-batch-data-conversion.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/envault-secret-rotation-guide.html` | 7 | 3 | `devforge-fix\blog\envault-secret-rotation-guide.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/deadcode-technical-deep-dive.html` | 7 | 3 | `devforge-fix\blog\deadcode-technical-deep-dive.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/click-to-mcp-intro.html` | 7 | 3 | `devforge-fix\blog\click-to-mcp-intro.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/openapi-diff-tools-comparison.html` | 7 | 3 | `devforge-fix\blog\openapi-diff-tools-comparison.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/zero-to-ci-safety-net.html` | 7 | 3 | `devforge-fix\blog\zero-to-ci-safety-net.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/stop-breaking-production.html` | 7 | 3 | `devforge-fix\blog\stop-breaking-production.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/schemaforge-v0-2-0-drizzle.html` | 7 | 3 | `devforge-fix\blog\schemaforge-v0-2-0-drizzle.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/welcome-devforge.html` | 7 | 3 | `devforge-fix\blog\welcome-devforge.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/envault-vs-doppler-vs-infisical-vs-dotenv-vault.html` | 7 | 3 | `devforge-fix\blog\envault-vs-doppler-vs-infisical-vs-dotenv-vault.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/envault-apiauth-rotate-keys-across-environments.html` | 7 | 3 | `devforge-fix\blog\envault-apiauth-rotate-keys-across-environments.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/configdrift-ci-cd-gating-before-deploy.html` | 7 | 3 | `devforge-fix\blog\configdrift-ci-cd-gating-before-deploy.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/configdrift-vs-driftctl-vs-terraform-plan-vs-checkov.html` | 7 | 3 | `devforge-fix\blog\configdrift-vs-driftctl-vs-terraform-plan-vs-checkov.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/deadcode-fail-ci-on-dead-code.html` | 7 | 3 | `devforge-fix\blog\deadcode-fail-ci-on-dead-code.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/deadcode-vs-knip-vs-ts-prune-vs-eslint.html` | 7 | 3 | `devforge-fix\blog\deadcode-vs-knip-vs-ts-prune-vs-eslint.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/deploydiff-preview-infrastructure-changes-before-apply.html` | 7 | 3 | `devforge-fix\blog\deploydiff-preview-infrastructure-changes-before-apply.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/deploydiff-rollback-commands-terraform-cloudformation.html` | 7 | 3 | `devforge-fix\blog\deploydiff-rollback-commands-terraform-cloudformation.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/datamorph-data-conversion-batch-processing.html` | 7 | 3 | `devforge-fix\blog\datamorph-data-conversion-batch-processing.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/datamorph-validate-data-schema-ci-pipeline.html` | 7 | 3 | `devforge-fix\blog\datamorph-validate-data-schema-ci-pipeline.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/apiauth-zero-downtime-key-rotation-cicd.html` | 7 | 3 | `devforge-fix\blog\apiauth-zero-downtime-key-rotation-cicd.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/apiauth-audit-api-credentials-catch-expired-revoked-keys.html` | 7 | 3 | `devforge-fix\blog\apiauth-audit-api-credentials-catch-expired-revoked-keys.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/apiauth-verify-api-keys-runtime-import-revocation.html` | 7 | 3 | `devforge-fix\blog\apiauth-verify-api-keys-runtime-import-revocation.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/apiauth-vs-dotenv-vs-aws-secrets-manager-vs-vault.html` | 7 | 3 | `devforge-fix\blog\apiauth-vs-dotenv-vs-aws-secrets-manager-vs-vault.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/apicontractguardian-generate-api-migration-guides.html` | 7 | 3 | `devforge-fix\blog\apicontractguardian-generate-api-migration-guides.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/apighost-openapi-mock-server-60-seconds.html` | 7 | 3 | `devforge-fix\blog\apighost-openapi-mock-server-60-seconds.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/apighost-vs-prism-vs-wiremock-vs-mockoon.html` | 7 | 3 | `devforge-fix\blog\apighost-vs-prism-vs-wiremock-vs-mockoon.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/json2sql-generate-create-table-from-json-schema-first.html` | 7 | 3 | `devforge-fix\blog\json2sql-generate-create-table-from-json-schema-first.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/json2sql-nested-json-relational-tables.html` | 7 | 3 | `devforge-fix\blog\json2sql-nested-json-relational-tables.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/json2sql-vs-papa-parse-vs-aws-dms-vs-airbyte.html` | 7 | 3 | `devforge-fix\blog\json2sql-vs-papa-parse-vs-aws-dms-vs-airbyte.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/schemaforge-v1-7-0-vscode-extension.html` | 7 | 3 | `devforge-fix\blog\schemaforge-v1-7-0-vscode-extension.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/configdrift-scan-multi-environment-configs-one-command.html` | 6 | 2 | `devforge-fix\blog\configdrift-scan-multi-environment-configs-one-command.html`, `devforge-fix\feed.xml` |
| `coding-dev-tools.github.io/devforge/blog/click-to-mcp-three-transport-modes.html` | 6 | 2 | `devforge-fix\blog\click-to-mcp-three-transport-modes.html`, `devforge-fix\feed.xml` |
| `coding-dev-tools.github.io/devforge/blog/deploydiff-vs-terraform-plan-vs-pulumi-preview-vs-infracost.html` | 6 | 3 | `devforge-fix\blog\deploydiff-vs-terraform-plan-vs-pulumi-preview-vs-infracost.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/datamorph-vs-pandas-vs-nifi-vs-aws-glue.html` | 6 | 3 | `devforge-fix\blog\datamorph-vs-pandas-vs-nifi-vs-aws-glue.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/saas-churn-predictor-launch.html` | 6 | 1 | `devforge-fix\blog\saas-churn-predictor-launch.html` |
| `coding-dev-tools.github.io/devforge/blog/catch-breaking-api-changes-in-ci.html` | 5 | 2 | `devforge-fix\blog\catch-breaking-api-changes-in-ci.html`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge.dev/og-image.svg` | 4 | 2 | `devforge-fix\docs.html`, `devforge-fix\index.html` |
| `coding-dev-tools.github.io/devforge/releases.html` | 4 | 2 | `devforge-fix\releases.html`, `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/deadcode-remove-dead-code-nextjs-app-router.html` | 4 | 1 | `devforge-fix\blog\deadcode-remove-dead-code-nextjs-app-router.html` |
| `coding-dev-tools.github.io/devforge/blog/schemaforge-convert-prisma-to-drizzle-migration-guide.html` | 4 | 1 | `devforge-fix\blog\schemaforge-convert-prisma-to-drizzle-migration-guide.html` |
| `coding-dev-tools.github.io/devforge/blog/apicontractguardian-git-branch-openapi-diff-pr-review.html` | 3 | 1 | `devforge-fix\blog\apicontractguardian-git-branch-openapi-diff-pr-review.html` |
| `coding-dev-tools.github.io/devforge/blog/click-to-mcp-three-distribution-channels.html` | 3 | 1 | `devforge-fix\blog\click-to-mcp-three-distribution-channels.html` |
| `coding-dev-tools.github.io/devforge/blog/deploydiff-cost-governance-before-you-deploy.html` | 3 | 1 | `devforge-fix\blog\deploydiff-cost-governance-before-you-deploy.html` |
| `coding-dev-tools.github.io/devforge/blog/json2sql-cicd-automated-database-seeding.html` | 3 | 1 | `devforge-fix\blog\json2sql-cicd-automated-database-seeding.html` |
| `coding-dev-tools.github.io/devforge/404.html` | 2 | 1 | `devforge-fix\404.html` |
| `coding-dev-tools.github.io/devforge/feed.xml` | 2 | 1 | `devforge-fix\feed.xml` |
| `coding-dev-tools.github.io/devforge/sitemap.xml` | 1 | 1 | `devforge-fix\robots.txt` |
| `coding-dev-tools.github.io/devforge/blog/traction-hits-680-developers.html` | 1 | 1 | `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/devf` | 1 | 1 | `Obsidian-Vault-Local\06-Learnings\cross-agent-learnings.md` |

## LIVECHECK (needs a live HTTP check; local repo absent)

- `revenueholdings.dev/alternatives.html` -- referenced by 1 file(s): `devforge-fix\sitemap.xml`
- `revenueholdings.dev/blog/clean-up-react-dead-code.html` -- referenced by 1 file(s): `devforge-fix\sitemap.xml`
- `revenueholdings.dev/blog/envault-team-env-file-sync.html` -- referenced by 1 file(s): `Coding-Dev-Tools.github.io\blog\envault-team-env-file-sync.html`
- `revenueholdings.dev/blog/openapi-diff-tools-comparison.html` -- referenced by 1 file(s): `devforge-fix\sitemap.xml`
- `revenueholdings.dev/index.html` -- referenced by 11 file(s): `Coding-Dev-Tools.github.io\blog\django-models-to-prisma-migration.html`, `Coding-Dev-Tools.github.io\blog\sqlalchemy-to-prisma-migration.html`, `Coding-Dev-Tools.github.io\configdrift.html`
- `revenueholdings.dev/quickstart.html` -- referenced by 1 file(s): `devforge-fix\sitemap.xml`

## Suggested fixes (honest, one-click next run)

- **DevForge suite hub sub-pages 404 (84 targets):** the `devforge-fix` repo contains the real built pages (pricing/alternatives/blog/docs/quickstart/about.html) but the live `Coding-Dev-Tools.github.io/devforge/` folder only has `index.html`. Decision for W: (a) deploy `devforge-fix` to the `/devforge/` Pages path, or (b) copy those built pages into `Coding-Dev-Tools.github.io/devforge/`. Until then every README link to those sub-pages 404s.

- **`devforge.dev` slug 404s (1 targets):** `.github/README.md` and `.github/profile/README.md` link to `coding-dev-tools.github.io/devforge.dev/...` but the real slug is `devforge` (no `.dev`). Repoint those links to `coding-dev-tools.github.io/devforge/`.

- **Self-hosted PyPI index (`pypi-index/simple/`) 404s:** already tracked as a 'Needs W' gap (the index was never published). Not a new finding; W must publish the index or accept `git+` as canonical.

---
Generated by `tools/linkcheck_portfolio.py` at 2026-07-18T00:36:28Z. Re-run each tick; commit the report so the backlog stays fresh.

