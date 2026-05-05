---
type: summary
source: 01_Raw/code.claude.com/docs/en/platforms.md
source_url: https://code.claude.com/docs/en/platforms
title: "Platforms and integrations"
summarized_at: 2026-05-05
entities_referenced: [Native-interface, IDE-integration, Agent-SDK, Computer-use, MCP-server, CI-integration, Routine, Scheduled-task, Headless-mode]
concepts_referenced: [Channel]
---

Decision-map page for choosing where to run Claude Code and what to connect to it.

**Where to run Claude Code**:
| Platform | Best for | Distinguishing features |
|---|---|---|
| CLI | Terminal, scripting, remote servers | Most complete; **only surface** for Agent SDK, third-party providers, and full feature set; computer use (macOS, Pro/Max) |
| Desktop | Visual review, parallel sessions, managed setup | Diff viewer, app preview, computer use (Pro/Max), Dispatch (Pro/Max) |
| VS Code | Inside VS Code | Inline diffs, integrated terminal, file context |
| JetBrains | Inside IntelliJ/PyCharm/WebStorm/etc. | Diff viewer, selection sharing, terminal session |
| Web (`claude.ai/code`) | Long-running tasks, work that should continue offline | Anthropic-managed cloud; continues after disconnect |
| Mobile (iOS/Android Claude app) | Start/monitor from away | Cloud sessions, Remote Control for local sessions, Dispatch to Desktop (Pro/Max) |

CLI is most complete. Desktop/IDE trade some CLI-only features (scripting, third-party providers, Agent SDK) for visual review + editor integration. Web runs in Anthropic cloud (continues after disconnect). Mobile is a thin client into cloud sessions or local-via-Remote-Control or Dispatch.

Configuration, project memory, MCP servers shared across local surfaces.

**Integrations**:
| Integration | What |
|---|---|
| Chrome | Browser automation with logged-in sessions |
| GitHub Actions | `@claude` in PRs/issues; CI automation |
| GitLab CI/CD | Same for GitLab |
| Code Review | Auto-review every PR (managed service) |
| Slack | `@Claude` mentions in channels |

For anything not listed: MCP servers / connectors (Linear, Notion, GDrive, internal APIs).

**Working away from terminal** — five mechanisms differentiated by trigger / where Claude runs / setup:
| Mechanism | Trigger | Runs on | Best for |
|---|---|---|---|
| Dispatch | Mobile-app message | Your machine (Desktop) | Delegating from away, minimal setup |
| Remote Control | Drive from claude.ai/code or mobile app | Your machine (CLI/VS Code) | Steering in-progress work from another device |
| Channels | Push events from Telegram/Discord/own server | Your machine (CLI) | Reacting to CI failures or chat events |
| Slack | `@Claude` mention | Anthropic cloud | PRs/reviews from team chat |
| Scheduled tasks | Set schedule | CLI / Desktop / cloud (Routines) | Recurring automation |
