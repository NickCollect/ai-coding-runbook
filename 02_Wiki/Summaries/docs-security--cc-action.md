---
type: summary
source: 01_Raw/github/anthropics/claude-code-action/docs/security.md
source_url: https://github.com/anthropics/claude-code-action/blob/main/docs/security.md
title: "Claude Code Action — docs/security"
summarized_at: 2026-05-05
entities_referenced: [CI-integration]
concepts_referenced: []
---

Security guidance for the Claude Code Action.

**Access control.**

- **Repository access.** Only users with **write** access can trigger the action.
- **Bot user control.** Bots can't trigger the action by default. Use `allowed_bots` to enable specific bots or all bots. Critical caveat: allowed bots are NOT checked for repository permissions — a bot matching an entry doesn't need to be installed or have write access. On a public repo, external parties (including GitHub Apps created by anyone) may trigger workflow events. If `allowed_bots: '*'` is set, any such App can invoke the action with a prompt it controls. Prefer an explicit list over `'*'`. Only list trusted App names. If `'*'` is needed, scope workflow `permissions:` to the minimum required.
- **Non-write user access (RISKY).** `allowed_non_write_users` bypasses the write-permission requirement. Significant security risk. Only for workflows with extremely limited permissions (e.g., issue-labeling workflows with only `issues: write`). Only works when `github_token` input is provided (not with GitHub App auth). Accepts comma-separated usernames or `'*'`. When set, Claude does best-effort scrubbing of Anthropic, cloud, and GitHub Actions secrets from subprocess environments. On Linux runners with bubblewrap, subprocesses run with PID-namespace isolation. Reduces but doesn't eliminate prompt-injection risk. Set `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB: 0` to opt out. Optionally set `CLAUDE_CODE_SCRIPT_CAPS` (JSON `{"script-name.sh": maxCalls}`) to cap how many times Claude can call specific scripts per run. Always pass `github_token: ${{ secrets.GITHUB_TOKEN }}` (auto-generated, scoped, expires when job completes) — **do not use a PAT** because static tokens don't rotate and could be partially recovered via prompt injection. Restrict allowed tools with `claude_args: '--allowedTools "Bash(gh issue view:*)"'`.
- **Token permissions.** GitHub App receives a short-lived token scoped to the operating repository. No cross-repository access. Limited scope.

**Using with `pull_request_target` or `workflow_run`.** These execute with the **base repository's secrets**. If the workflow checks out the PR head into `$GITHUB_WORKSPACE` before the action, the action and Claude run with that untrusted checkout as cwd. **Don't check out an untrusted ref into the workspace root before this action.** Two safe patterns: (1) check out the base ref only (default behavior of `actions/checkout@v6`); (2) check out base ref at workspace root, then check out PR head into a subdirectory (`path: pr-head`) and pass it via `claude_args: "--add-dir pr-head"`.

**`claude-code-action` vs `claude-code-base-action`.** Base-action is a lower-level building block — it does NOT perform actor permission checks or restore project config from the base ref. For those behaviors use `claude-code-action`.

**Pull request creation.** By default Claude does NOT create pull requests automatically when responding to `@claude`. Instead it commits to a new branch.

The file continues with full-output security warning (`show_full_output` may expose secrets, auto-enabled in GitHub Actions debug mode), commit signing, secret scrubbing, and additional hardening recommendations.
