---
type: summary
source: 01_Raw/github/anthropics/claude-code-action/docs/setup.md
source_url: https://github.com/anthropics/claude-code-action/blob/main/docs/setup.md
title: "Claude Code Action — docs/setup"
summarized_at: 2026-05-05
entities_referenced: [CI-integration]
concepts_referenced: []
---

Setup guide for the Claude Code Action — both the standard install and a custom GitHub App alternative.

**Manual setup (Direct API).** Repo admin required.

1. Install the official Claude GitHub app: https://github.com/apps/claude.
2. Add authentication to repo secrets — either `ANTHROPIC_API_KEY` (API key auth) or `CLAUDE_CODE_OAUTH_TOKEN` (OAuth, Pro/Max users generate via `claude setup-token` locally).
3. Copy the workflow file from `examples/claude.yml` into `.github/workflows/`.

**Custom GitHub App.** When the official app isn't suitable: more restrictive permissions needed; org policy prevents third-party app install; using AWS Bedrock or Google Vertex AI (cloud-provider OIDC requires custom apps).

**Quick setup with App manifest** (recommended). The repo ships a `github-app-manifest.json` with all required permissions pre-configured.

1. Create the app — download `create-app.html`, open in browser, click "Create App for Personal Account" or enter org name and click "Create App for Organization". Tool auto-configures permissions and submits the manifest. Alternative: paste the manifest JSON into github.com/settings/apps/new (or the org's app settings) via the "Create from manifest" option.
2. Complete the creation flow — review the preview, optionally rename, click "Create GitHub App".
3. Generate and download a private key — Settings → Private keys → Generate a private key → download the `.pem`.
4. Continue with installation by following step 3 of the manual setup to install the app and configure the workflow.

The doc continues with: option 2 (manual app creation step-by-step with the explicit list of required permissions), wiring the custom app's App ID and private key into repo secrets, configuring the workflow to use the custom app via `app-id` / `private-key`, and security best practices for custom apps (rotation, restricted permissions, audit logging).
