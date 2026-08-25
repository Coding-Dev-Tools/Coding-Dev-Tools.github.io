Portfolio Link-Integrity Audit - 2026-08-25T00:53:36Z

Read-only, offline. Verifies every `coding-dev-tools.github.io/...` and `revenueholdings.dev` link in product READMEs/AGENTS/site HTML against the local published repos. **BROKEN** = file absent from the Pages repo (404 on the live site). **LIVECHECK** = needs a live HTTP check (local repo absent).

OK (resolves locally): **401**
BROKEN (404 on live site): **97 unique targets** (1486 total references)
LIVECHECK (verify live): 6 unique targets

## BROKEN link clusters (fix these -- highest ROI rung-1)

| Broken target (404 on live site) | Refs | Files | Example sources |
|-----------------------------|------|-------|-----------------|
| `coding-dev-tools.github.io/devforge/og-image.svg` | 208 | 102 | `devforge-fix\about.html`, `devforge-fix\alternatives.html`, `devforge-fix\blog.html`, +99 more |
| `coding-dev-tools.github.io/pypi-index/simple/index.html` _(known Needs-W gap: self-hosted PyPI index not published)_ | 54 | 30 | `LEARNING\outreach-queue.md`, `Obsidian-Vault-Local-check\02-Revenue\Active-Streams.md`, `Obsidian-Vault-Local-check\40-Marketing\owned-site-page-publish-runbook.md`, +27 more |
| `coding-dev-tools.github.io/devforge/pricing.html` | 36 | 13 | `.github\README.md`, `Coding-Dev-Tools.github.io\blog\datamorph-schema-validation-in-ci.html`, `_cowork_ops\digests\mkt-domain-dead-refs-2026-08-22.md`, +10 more |
| `coding-dev-tools.github.io/devforge/blog.html` | 22 | 9 | `.github\README.md`, `devforge-fix\README.md`, `devforge-fix\blog.html`, +6 more |
| `coding-dev-tools.github.io/devforge/about.html` | 22 | 9 | `.github\profile\README.md`, `devforge-fix\README.md`, `devforge-fix\about.html`, +6 more |
| `coding-dev-tools.github.io/devforge/blog/apighost-advanced-mock-patterns.html` | 20 | 6 | `devforge-fix\blog\apighost-advanced-mock-patterns.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/click-to-mcp-og.svg` | 20 | 10 | `devforge-fix\blog\click-to-mcp-intro.html`, `devforge-fix\blog\click-to-mcp-three-distribution-channels.html`, `devforge-fix\blog\click-to-mcp-three-transport-modes.html`, +7 more |
| `coding-dev-tools.github.io/devforge/docs.html` | 18 | 9 | `.github\README.md`, `devforge-fix\README.md`, `devforge-fix\blog\license-key-rate-limiting-cli-tools.html`, +6 more |
| `coding-dev-tools.github.io/devforge/blog/mcp-server-directories-where-to-list-your-server.html` | 18 | 8 | `devforge-fix\blog\get-your-cli-tool-listed-awesome-directories.html`, `devforge-fix\blog\mcp-server-directories-where-to-list-your-server.html`, `devforge-fix\feed.xml`, +5 more |
| `coding-dev-tools.github.io/devforge/blog/five-productivity-workflows-cli-suite.html` | 18 | 6 | `devforge-fix\blog\five-productivity-workflows-cli-suite.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/python-cli-to-mcp-server.html` | 18 | 6 | `devforge-fix\blog\python-cli-to-mcp-server.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/autonomous-ai-experiment.html` | 18 | 6 | `devforge-fix\blog\autonomous-ai-experiment.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/start-here.html` | 18 | 8 | `devforge-fix\blog\license-key-rate-limiting-cli-tools.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +5 more |
| `coding-dev-tools.github.io/devforge/blog/preview-infra-cost-before-deploy.html` | 18 | 8 | `devforge-fix\blog\preview-infra-cost-before-deploy.html`, `devforge-fix\blog\revenue-hits-680-developers.html`, `devforge-fix\feed.xml`, +5 more |
| `coding-dev-tools.github.io/devforge/blog/json-to-sql-one-command.html` | 18 | 6 | `devforge-fix\blog\json-to-sql-one-command.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/before-you-deploy-config-drift-and-cost.html` | 17 | 5 | `devforge-fix\blog\before-you-deploy-config-drift-and-cost.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +2 more |
| `coding-dev-tools.github.io/devforge/blog/new-cli-features-may-18-2026.html` | 16 | 6 | `devforge-fix\blog\new-cli-features-may-18-2026.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/api-key-management-from-terminal.html` | 16 | 6 | `devforge-fix\blog\api-key-management-from-terminal.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/schemaforge-v0-5-0-sqlalchemy.html` | 16 | 6 | `devforge-fix\blog\schemaforge-v0-5-0-sqlalchemy.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/sync-env-variables-across-environments.html` | 16 | 6 | `devforge-fix\blog\sync-env-variables-across-environments.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/api-mock-server-from-openapi-spec.html` | 16 | 6 | `devforge-fix\blog\api-mock-server-from-openapi-spec.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/catch-config-drift-before-production.html` | 16 | 6 | `devforge-fix\blog\catch-config-drift-before-production.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/clean-up-react-dead-code.html` | 16 | 6 | `devforge-fix\blog\clean-up-react-dead-code.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/python-cli-type-safe-pep561.html` | 16 | 6 | `devforge-fix\blog\python-cli-type-safe-pep561.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/envault-serve-http-api-secrets.html` | 16 | 6 | `devforge-fix\blog\envault-serve-http-api-secrets.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/monetize-mcp-servers-x402-mpp.html` | 16 | 6 | `devforge-fix\blog\monetize-mcp-servers-x402-mpp.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/cli-tools-as-mcp-servers.html` | 16 | 6 | `devforge-fix\blog\cli-tools-as-mcp-servers.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/quickstart.html` | 16 | 8 | `devforge-fix\README.md`, `devforge-fix\blog\license-key-rate-limiting-cli-tools.html`, `devforge-fix\quickstart.html`, +5 more |
| `coding-dev-tools.github.io/devforge/blog/revenue-hits-680-developers.html` | 15 | 5 | `devforge-fix\blog\revenue-hits-680-developers.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +2 more |
| `coding-dev-tools.github.io/devforge/alternatives.html` | 14 | 6 | `devforge-fix\README.md`, `devforge-fix\alternatives.html`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/schemaforge-vs-prisma-migrate-vs-alembic-vs-atlas.html` | 14 | 6 | `devforge-fix\blog\schemaforge-vs-prisma-migrate-vs-alembic-vs-atlas.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/apicontractguardian-vs-oasdiff-vs-optic-vs-openapi-diff.html` | 14 | 6 | `devforge-fix\blog\apicontractguardian-vs-oasdiff-vs-optic-vs-openapi-diff.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/apicontractguardian-ci-cd-gating-breaking-api-changes.html` | 14 | 6 | `devforge-fix\blog\apicontractguardian-ci-cd-gating-breaking-api-changes.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/mcp-everywhere-why-your-cli-tools-need-it.html` | 14 | 6 | `devforge-fix\blog\mcp-everywhere-why-your-cli-tools-need-it.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/click-to-mcp-usage-guide.html` | 14 | 6 | `devforge-fix\blog\click-to-mcp-usage-guide.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/white-label-ai-agent-deployment.html` | 14 | 6 | `devforge-fix\blog\white-label-ai-agent-deployment.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/get-your-cli-tool-listed-awesome-directories.html` | 14 | 6 | `devforge-fix\blog\get-your-cli-tool-listed-awesome-directories.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/10-open-source-cli-tools-ai-development.html` | 14 | 6 | `devforge-fix\blog\10-open-source-cli-tools-ai-development.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/ai-built-cli-tools-zero-humans.html` | 14 | 6 | `devforge-fix\blog\ai-built-cli-tools-zero-humans.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/license-key-rate-limiting-cli-tools.html` | 14 | 6 | `devforge-fix\blog\license-key-rate-limiting-cli-tools.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/datamorph-batch-data-conversion.html` | 14 | 6 | `devforge-fix\blog\datamorph-batch-data-conversion.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/envault-secret-rotation-guide.html` | 14 | 6 | `devforge-fix\blog\envault-secret-rotation-guide.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/deadcode-technical-deep-dive.html` | 14 | 6 | `devforge-fix\blog\deadcode-technical-deep-dive.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/click-to-mcp-intro.html` | 14 | 6 | `devforge-fix\blog\click-to-mcp-intro.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/openapi-diff-tools-comparison.html` | 14 | 6 | `devforge-fix\blog\openapi-diff-tools-comparison.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/zero-to-ci-safety-net.html` | 14 | 6 | `devforge-fix\blog\zero-to-ci-safety-net.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/stop-breaking-production.html` | 14 | 6 | `devforge-fix\blog\stop-breaking-production.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/schemaforge-v0-2-0-drizzle.html` | 14 | 6 | `devforge-fix\blog\schemaforge-v0-2-0-drizzle.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/welcome-devforge.html` | 14 | 6 | `devforge-fix\blog\welcome-devforge.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/envault-vs-doppler-vs-infisical-vs-dotenv-vault.html` | 14 | 6 | `devforge-fix\blog\envault-vs-doppler-vs-infisical-vs-dotenv-vault.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/envault-apiauth-rotate-keys-across-environments.html` | 14 | 6 | `devforge-fix\blog\envault-apiauth-rotate-keys-across-environments.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/configdrift-ci-cd-gating-before-deploy.html` | 14 | 6 | `devforge-fix\blog\configdrift-ci-cd-gating-before-deploy.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/configdrift-vs-driftctl-vs-terraform-plan-vs-checkov.html` | 14 | 6 | `devforge-fix\blog\configdrift-vs-driftctl-vs-terraform-plan-vs-checkov.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/deadcode-fail-ci-on-dead-code.html` | 14 | 6 | `devforge-fix\blog\deadcode-fail-ci-on-dead-code.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/deadcode-vs-knip-vs-ts-prune-vs-eslint.html` | 14 | 6 | `devforge-fix\blog\deadcode-vs-knip-vs-ts-prune-vs-eslint.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/deploydiff-preview-infrastructure-changes-before-apply.html` | 14 | 6 | `devforge-fix\blog\deploydiff-preview-infrastructure-changes-before-apply.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/deploydiff-rollback-commands-terraform-cloudformation.html` | 14 | 6 | `devforge-fix\blog\deploydiff-rollback-commands-terraform-cloudformation.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/datamorph-data-conversion-batch-processing.html` | 14 | 6 | `devforge-fix\blog\datamorph-data-conversion-batch-processing.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/datamorph-validate-data-schema-ci-pipeline.html` | 14 | 6 | `devforge-fix\blog\datamorph-validate-data-schema-ci-pipeline.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/apiauth-zero-downtime-key-rotation-cicd.html` | 14 | 6 | `devforge-fix\blog\apiauth-zero-downtime-key-rotation-cicd.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/apiauth-audit-api-credentials-catch-expired-revoked-keys.html` | 14 | 6 | `devforge-fix\blog\apiauth-audit-api-credentials-catch-expired-revoked-keys.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/apiauth-verify-api-keys-runtime-import-revocation.html` | 14 | 6 | `devforge-fix\blog\apiauth-verify-api-keys-runtime-import-revocation.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/apiauth-vs-dotenv-vs-aws-secrets-manager-vs-vault.html` | 14 | 6 | `devforge-fix\blog\apiauth-vs-dotenv-vs-aws-secrets-manager-vs-vault.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/apicontractguardian-generate-api-migration-guides.html` | 14 | 6 | `devforge-fix\blog\apicontractguardian-generate-api-migration-guides.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/apighost-openapi-mock-server-60-seconds.html` | 14 | 6 | `devforge-fix\blog\apighost-openapi-mock-server-60-seconds.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/apighost-vs-prism-vs-wiremock-vs-mockoon.html` | 14 | 6 | `devforge-fix\blog\apighost-vs-prism-vs-wiremock-vs-mockoon.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/json2sql-generate-create-table-from-json-schema-first.html` | 14 | 6 | `devforge-fix\blog\json2sql-generate-create-table-from-json-schema-first.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/json2sql-nested-json-relational-tables.html` | 14 | 6 | `devforge-fix\blog\json2sql-nested-json-relational-tables.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/json2sql-vs-papa-parse-vs-aws-dms-vs-airbyte.html` | 14 | 6 | `devforge-fix\blog\json2sql-vs-papa-parse-vs-aws-dms-vs-airbyte.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/revenueholdings.dev/index.html` | 14 | 1 | `_cowork_ops\digests\mkt-domain-dead-refs-2026-08-22.md` |
| `coding-dev-tools.github.io/devforge/blog/configdrift-scan-multi-environment-configs-one-command.html` | 13 | 5 | `devforge-fix\blog\configdrift-scan-multi-environment-configs-one-command.html`, `devforge-fix\feed.xml`, `devforge\blog\configdrift-scan-multi-environment-configs-one-command.html`, +2 more |
| `coding-dev-tools.github.io/devforge/blog/click-to-mcp-three-transport-modes.html` | 13 | 5 | `devforge-fix\blog\click-to-mcp-three-transport-modes.html`, `devforge-fix\feed.xml`, `devforge\blog\click-to-mcp-three-transport-modes.html`, +2 more |
| `coding-dev-tools.github.io/devforge/blog/saas-churn-predictor-launch.html` | 13 | 3 | `devforge-fix\blog\saas-churn-predictor-launch.html`, `devforge\blog\saas-churn-predictor-launch.html`, `devforge\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/deploydiff-vs-terraform-plan-vs-pulumi-preview-vs-infracost.html` | 12 | 6 | `devforge-fix\blog\deploydiff-vs-terraform-plan-vs-pulumi-preview-vs-infracost.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/datamorph-vs-pandas-vs-nifi-vs-aws-glue.html` | 12 | 6 | `devforge-fix\blog\datamorph-vs-pandas-vs-nifi-vs-aws-glue.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +3 more |
| `coding-dev-tools.github.io/devforge/blog/schemaforge-v1-7-0-vscode-extension.html` | 11 | 5 | `devforge-fix\blog\schemaforge-v1-7-0-vscode-extension.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +2 more |
| `coding-dev-tools.github.io/devforge/blog/ci-cd-python-cli-tools-guide.html` | 11 | 5 | `devforge-fix\blog\ci-cd-python-cli-tools-guide.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +2 more |
| `coding-dev-tools.github.io/devforge/blog/click-vs-typer-vs-argparse-python-cli.html` | 11 | 5 | `devforge-fix\blog\click-vs-typer-vs-argparse-python-cli.html`, `devforge-fix\feed.xml`, `devforge-fix\sitemap.xml`, +2 more |
| `coding-dev-tools.github.io/devforge/blog/catch-breaking-api-changes-in-ci.html` | 10 | 4 | `devforge-fix\blog\catch-breaking-api-changes-in-ci.html`, `devforge-fix\sitemap.xml`, `devforge\blog\catch-breaking-api-changes-in-ci.html`, +1 more |
| `coding-dev-tools.github.io/devforge/releases.html` | 8 | 4 | `devforge-fix\releases.html`, `devforge-fix\sitemap.xml`, `devforge\releases.html`, +1 more |
| `coding-dev-tools.github.io/devforge/blog/click-to-mcp-three-distribution-channels.html` | 7 | 3 | `devforge-fix\blog\click-to-mcp-three-distribution-channels.html`, `devforge\blog\click-to-mcp-three-distribution-channels.html`, `devforge\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/blog/deploydiff-cost-governance-before-you-deploy.html` | 7 | 3 | `devforge-fix\blog\deploydiff-cost-governance-before-you-deploy.html`, `devforge\blog\deploydiff-cost-governance-before-you-deploy.html`, `devforge\sitemap.xml` |
| `coding-dev-tools.github.io/devforge/404.html` | 4 | 2 | `devforge-fix\404.html`, `devforge\404.html` |
| `coding-dev-tools.github.io/devforge/feed.xml` | 4 | 2 | `devforge-fix\feed.xml`, `devforge\feed.xml` |
| `coding-dev-tools.github.io/devforge/blog/deadcode-remove-dead-code-nextjs-app-router.html` | 4 | 1 | `devforge-fix\blog\deadcode-remove-dead-code-nextjs-app-router.html` |
| `coding-dev-tools.github.io/devforge/blog/schemaforge-convert-prisma-to-drizzle-migration-guide.html` | 4 | 1 | `devforge-fix\blog\schemaforge-convert-prisma-to-drizzle-migration-guide.html` |
| `coding-dev-tools.github.io/devforge/blog/apicontractguardian-git-branch-openapi-diff-pr-review.html` | 3 | 1 | `devforge-fix\blog\apicontractguardian-git-branch-openapi-diff-pr-review.html` |
| `coding-dev-tools.github.io/devforge/blog/json2sql-cicd-automated-database-seeding.html` | 3 | 1 | `devforge-fix\blog\json2sql-cicd-automated-database-seeding.html` |
| `coding-dev-tools.github.io/devforge/sitemap.xml` | 2 | 2 | `devforge-fix\robots.txt`, `devforge\robots.txt` |
| `coding-dev-tools.github.io/devf` | 2 | 2 | `Obsidian-Vault-Local-check\06-Learnings\cross-agent-learnings.md`, `Obsidian-Vault-Local\06-Learnings\cross-agent-learnings.md` |
| `coding-dev-tools.github.io/deploydiff-preview-infra-changes.html` | 2 | 1 | `Obsidian-Vault-Local\40-Marketing\content-calendar.md` |
| `coding-dev-tools.github.io/devforge/blog/traction-hits-680-developers.html` | 1 | 1 | `devforge-fix\sitemap.xml` |
| `coding-dev-tools.github.io/revenueholdings.dev/blog/openapi-diff-tools-comparison.html` | 1 | 1 | `_cowork_ops\digests\mkt-domain-dead-refs-2026-08-22.md` |
| `coding-dev-tools.github.io/revenueholdings.dev/alternatives.html` | 1 | 1 | `_cowork_ops\digests\mkt-domain-dead-refs-2026-08-22.md` |
| `coding-dev-tools.github.io/revenueholdings.dev/quickstart.html` | 1 | 1 | `_cowork_ops\digests\mkt-domain-dead-refs-2026-08-22.md` |
| `coding-dev-tools.github.io/revenueholdings.dev/blog/clean-up-react-dead-code.html` | 1 | 1 | `_cowork_ops\digests\mkt-domain-dead-refs-2026-08-22.md` |
| `coding-dev-tools.github.io/revenueholdings.dev (malformed path form)` | 1 | 1 | `_cowork_ops\digests\mkt-domain-dead-refs-2026-08-22.md` |

## LIVECHECK (needs a live HTTP check; local repo absent)

- `revenueholdings.dev/alternatives.html` -- referenced by 2 file(s): `_cowork_ops\digests\mkt-domain-dead-refs-2026-08-22.md`, `devforge-fix\sitemap.xml`
- `revenueholdings.dev/blog/clean-up-react-dead-code.html` -- referenced by 2 file(s): `_cowork_ops\digests\mkt-domain-dead-refs-2026-08-22.md`, `devforge-fix\sitemap.xml`
- `revenueholdings.dev/blog/openapi-diff-tools-comparison.html` -- referenced by 2 file(s): `_cowork_ops\digests\mkt-domain-dead-refs-2026-08-22.md`, `devforge-fix\sitemap.xml`
- `revenueholdings.dev/index.html` -- referenced by 2 file(s): `_cowork_ops\digests\mkt-domain-dead-refs-2026-08-22.md`, `json2sql\README.md`
- `revenueholdings.dev/pricing` -- referenced by 1 file(s): `_cowork_ops\digests\mkt-domain-dead-refs-2026-08-22.md`
- `revenueholdings.dev/quickstart.html` -- referenced by 2 file(s): `_cowork_ops\digests\mkt-domain-dead-refs-2026-08-22.md`, `devforge-fix\sitemap.xml`

## Suggested fixes (honest, one-click next run)

- **DevForge suite hub sub-pages 404 (84 targets):** the `devforge-fix` repo contains the real built pages (pricing/alternatives/blog/docs/quickstart/about.html) but the live `Coding-Dev-Tools.github.io/devforge/` folder only has `index.html`. Decision for W: (a) deploy `devforge-fix` to the `/devforge/` Pages path, or (b) copy those built pages into `Coding-Dev-Tools.github.io/devforge/`. Until then every README link to those sub-pages 404s.

- **Malformed `revenueholdings.dev` *path* links:** these point at `coding-dev-tools.github.io/revenueholdings.dev/...` (a path, not the domain). No such directory exists on the Pages repo. Repoint to the real `https://revenueholdings.dev/...` domain. Found in json2sql + apiauth + SaaS-Churn-Predictor READMEs and devforge-fix sitemap.

- **Self-hosted PyPI index (`pypi-index/simple/`) 404s:** already tracked as a 'Needs W' gap (the index was never published). Not a new finding; W must publish the index or accept `git+` as canonical.

---
Generated by `tools/linkcheck_portfolio.py` at 2026-08-25T00:53:36Z. Re-run each tick; commit the report so the backlog stays fresh.

## 2026-08-25 addendum — LIVE verification of newest owned-site surfaces (curl, this run)

| URL | Live status |
|---|---|
| /blog/configdrift-gate-deploys-on-config-drift-ci.html | **404** |
| /blog/deploydiff-cost-estimation-before-apply.html | **404** |
| /blog/deploydiff-preview-infra-changes.html | 200 |
| /blog/json2sql-nested-json-to-relational-sql.html | 200 |
| /sitemap.xml (hub root, commit 1da01d8) | **404** |

CORRECTION to Run-252 activity-log: its "both new cards verified live HTTP 200"
claim was WRONG — those two pages exist only on LOCAL main (16 commits ahead of
origin b83f055, zero pushes since Run 238). No live leak yet (the rotated
homepage cards are in the same unpushed commit), but every guide, the homepage
rotation, and the hub-root sitemap remain INVISIBLE until W pushes local main.
Push command: git push origin main:b83f055..main (fast-forward) from this repo.
