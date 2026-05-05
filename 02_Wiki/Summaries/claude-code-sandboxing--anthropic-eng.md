---
type: summary
source: 01_Raw/anthropic.com/engineering/claude-code-sandboxing.md
source_url: https://www.anthropic.com/engineering/claude-code-sandboxing
title: "Beyond permission prompts: making Claude Code more secure and autonomous"
summarized_at: 2026-05-05
entities_referenced: [Sandboxing, Permission-mode, MCP-server]
concepts_referenced: []
---

Launch post (Oct 20, 2025) for two new sandboxing-based features in Claude Code: a sandboxed bash tool and Claude Code on the web. Internal usage shows sandboxing safely reduces permission prompts by **84%**.

**Why.** Claude Code is permission-based and read-only by default. Constant "approve" clicking causes approval fatigue, where users stop paying attention. Sandboxing creates pre-defined boundaries Claude can work freely within.

**Two boundaries (both required).** Filesystem isolation alone leaves exfiltration risk; network isolation alone allows local-file mischief. Effective sandboxing needs both:
1. **Filesystem isolation** — Claude can only access/modify specific directories. Prevents prompt-injected Claude from modifying sensitive system files.
2. **Network isolation** — Claude can only connect to approved servers. Prevents leaking data or downloading malware.

**Feature 1 — Sandboxed bash tool (beta research preview).** A new sandbox runtime defines exact allowed directories and network hosts without container overhead. Can sandbox arbitrary processes, agents, MCP servers. Built on OS primitives: **Linux bubblewrap** and **macOS seatbelt**. Coverage extends to subprocesses spawned by sandboxed commands. Filesystem: read/write to cwd, blocks modifications outside. Network: internet access only via a Unix domain socket connected to an out-of-sandbox proxy server that enforces domain restrictions and prompts for newly requested domains. Proxy customizable for arbitrary outgoing-traffic rules. If Claude tries to access something outside the sandbox, user is notified and can approve. Open-sourced as `anthropic-experimental/sandbox-runtime` for other agent builders. Activate via `/sandbox` slash command.

**Feature 2 — Claude Code on the web.** Each session runs in an isolated cloud sandbox with full server access — but sensitive credentials (git, signing keys) are never inside the sandbox. Custom proxy service transparently handles git: inside-sandbox git client authenticates to the proxy with a custom-built scoped credential; proxy verifies the credential and the git interaction (e.g. only pushing to configured branch) and attaches the right token before forwarding to GitHub. Even a fully compromised sandbox cannot push outside the configured branch or access user credentials.

**Threat model framing.** Sandboxing means even a successful prompt injection is fully isolated — compromised Claude Code can't steal SSH keys or phone home. Authors: David Dworken and Oliver Weller-Davies. The piece positions sandboxing as the path to letting Claude run more autonomously without trading off security.
