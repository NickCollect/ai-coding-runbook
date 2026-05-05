---
type: summary
source: 01_Raw/code.claude.com/docs/en/chrome.md
source_url: https://code.claude.com/docs/en/chrome
title: "Use Claude Code with Chrome (beta)"
summarized_at: 2026-05-05
entities_referenced: [IDE-integration, MCP-server, Computer-use, Native-interface, Enterprise-gateway]
concepts_referenced: []
---

Chrome integration (beta) lets Claude Code drive a real Chrome / Edge browser via the **Claude in Chrome** extension. Different from `Computer-use` (computer use is for native macOS apps; Chrome is browser-only and DOM-aware). Implemented as a built-in MCP server (`claude-in-chrome`).

**Capabilities**: live debugging (read console/DOM, fix code), design verification (Figma → built UI compare), web app testing (form validation, regressions, user flows), authenticated apps without API connectors (Google Docs, Gmail, Notion etc.), data extraction → CSV, multi-site automation, session recording as GIF.

**Prerequisites**:
- Chrome OR Microsoft Edge (NOT Brave/Arc/other Chromium-based; NOT WSL)
- Extension v1.0.36+
- Claude Code v2.0.73+
- A direct Anthropic plan (Pro/Max/Team/Enterprise) — NOT available via Bedrock/Vertex/Foundry; need separate claude.ai account if using third-party provider

**Enable**: launch with `claude --chrome` OR run `/chrome` in-session. `/chrome` also exposes "Enabled by default" (warning: increases context usage as browser tools always loaded).

Site permissions inherited from Chrome extension settings. Login pages and CAPTCHAs cause Claude to pause and request manual handling. Browser actions run in a visible Chrome window in real time, sharing the user's logged-in state.

**Native messaging host config** is installed on first enable; Chrome reads it on startup, so a Chrome restart is needed if extension isn't detected first try. Locations:
- Chrome macOS: `~/Library/Application Support/Google/Chrome/NativeMessagingHosts/com.anthropic.claude_code_browser_extension.json`
- Chrome Linux: `~/.config/google-chrome/NativeMessagingHosts/...`
- Chrome Windows: `HKCU\Software\Google\Chrome\NativeMessagingHosts\`
- Edge: same paths but under `Microsoft Edge` / `microsoft-edge` / `Microsoft\Edge`.

**Common errors**: "Browser extension is not connected" (restart Chrome+Claude, run `/chrome`), "Extension not detected" (install/enable), "No tab available" (ask Claude to open new tab), "Receiving end does not exist" (service worker idle → "Reconnect extension"). Long sessions can drop connection due to MV3 service worker idling.

Cross-references: `Computer-use` for native apps, VS Code extension also exposes browser automation when Chrome extension installed (no `--chrome` flag needed).
