---
type: summary
source: 01_Raw/code.claude.com/docs/en/security.md
source_url: https://code.claude.com/docs/en/security
title: "Security"
summarized_at: 2026-05-05
entities_referenced: [Sandboxing, Permission-mode, Settings, Hooks, MCP-server, IDE-integration]
concepts_referenced: []
---

Overview of Claude Code's security model and best practices. Anthropic Trust Center has SOC 2 Type 2 / ISO 27001 details.

**Permission-based architecture**: read-only by default; explicit approval for edits/bash/network. Approve once or auto-allow per rule.

**Built-in protections**:
- Sandboxed bash tool with filesystem + network isolation (`/sandbox`).
- Write access **restricted to working directory + subfolders** — Claude can't write to parent dirs without permission. Reads can go outside (system libs/deps), but writes can't.
- Per-user/codebase/org allowlists for prompt fatigue.
- Accept Edits mode batches edits while still prompting for side-effecting commands.

**Prompt-injection safeguards**:
- Permission system gates sensitive ops.
- Context-aware analysis detects harmful instructions.
- Input sanitization against command injection.
- Default blocklist of risky web fetchers (`curl`, `wget`).
- Network requests need approval by default.
- Web fetch uses isolated context window.
- Trust verification on first run + new MCP servers (DISABLED in headless `-p` mode).
- Command injection detection: suspicious bash needs manual approval even if previously allowlisted.
- Fail-closed matching: unmatched commands → manual approval.
- Natural language descriptions on complex bash commands.
- Encrypted credential storage.

**Windows WebDAV warning**: do not enable WebDAV or grant Claude Code access to `\\*` paths — Microsoft has deprecated WebDAV due to security risks; can bypass permission system.

**Best practices for untrusted content**:
1. Review commands before approval.
2. Avoid piping untrusted content directly to Claude.
3. Verify proposed changes to critical files.
4. Use VMs for scripts/external web tool calls.
5. Report suspicious behavior with `/feedback`.

**MCP**: Claude Code does NOT manage/audit any MCP servers. Use trusted ones or write your own. Configure permissions per server.

**Cloud (Claude Code on the web)**: isolated VMs per session, network ACLs (default limited), credential proxy translates scoped sandbox creds to actual GitHub tokens, push restricted to current branch, audit logs, auto-cleanup.

**Remote Control** (vs cloud): connection is just a window into your local session — code execution + file access stay local. Multiple short-lived narrowly-scoped credentials limit blast radius if any one leaks.

**Team security**:
- Use managed settings to enforce org standards.
- Share approved permission configs via VCS.
- Monitor via OpenTelemetry metrics.
- Audit/block settings changes during sessions with `ConfigChange` hooks.

**Reporting vulns**: do not disclose publicly; submit via Anthropic HackerOne program with repro steps.
