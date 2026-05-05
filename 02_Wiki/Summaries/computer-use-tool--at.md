---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool
title: "Computer use tool"
summarized_at: 2026-05-05
entities_referenced: [Computer-use-tool-API, Tool-use, Bash-tool-API, Text-editor-tool, Vision]
concepts_referenced: [Extended-thinking, Agentic-loop]
---

The [[Computer-use-tool-API]] enables Claude to interact with desktop environments via screenshot capture, mouse control, keyboard input, and window automation. On WebArena (autonomous web navigation across real websites), Claude achieves state-of-the-art results among single-agent systems. Beta header: `computer-use-2025-11-24` for Opus 4.7/4.6, Sonnet 4.6, Opus 4.5; `computer-use-2025-01-24` for older models. **Eligible for ZDR.**

This is a *client-side* tool: Claude does NOT directly connect to the environment. Your application receives `tool_use` requests, executes them in your virtualized environment, captures screenshots/outputs, and returns them as `tool_result` blocks. Reference implementation lives at `anthropics/anthropic-quickstarts/computer-use-demo` (Docker-based with web UI).

**Capabilities.** Screenshot capture, mouse (click/drag/move), keyboard (type/shortcuts), desktop automation across any GUI app. Often paired with the [[Bash-tool-API]] and [[Text-editor-tool]] for full automation workflows.

**Computing environment.** Sandboxed VM/container with: virtual X11 display (Xvfb), lightweight UI (Mutter window manager + Tint2 panel) on Linux, pre-installed apps (Firefox, LibreOffice, etc.), tool implementation code, and an [[Agentic-loop]] driver. Claude doesn't connect directly—your app translates requests into actions and returns results.

**Security.** Distinct beta-feature risks; heightened with internet access. Recommended precautions: dedicated VM/container with minimal privileges; no sensitive data; allowlist domains; human-in-the-loop confirmation for actions with real-world consequences (cookies, transactions, ToS). **Prompt injection defense:** Anthropic auto-runs classifiers on screenshots; potential injections trigger automatic user-confirmation prompts. Opt-out available via support contact for headless workflows.

**Tool definition.** `type: "computer_20251124"` (or `_20250124`), `name: "computer"`, `display_width_px`, `display_height_px`, optional `display_number`, optional `enable_zoom: true` (only for `_20251124`).

**Available actions.**
- *Basic (all versions):* `screenshot`, `left_click [x,y]`, `type`, `key` (e.g., `"ctrl+s"`), `mouse_move`.
- *Enhanced (`computer_20250124`, on Claude 4 + Sonnet 3.7):* `scroll` (with direction + amount), `left_click_drag`, `right_click`, `middle_click`, `double_click`, `triple_click`, `left_mouse_down`/`up` (fine-grained click), `hold_key` (duration in seconds), `wait`.
- *Enhanced (`computer_20251124`, on Opus 4.7/4.6, Sonnet 4.6, Opus 4.5):* All of the above plus `zoom` (view a region `[x1,y1,x2,y2]` at full resolution; requires `enable_zoom: true`).

**Modifier keys with click/scroll.** Use the `text` parameter on click or scroll actions: `"shift"`, `"ctrl"`, `"alt"`, `"super"` (Cmd/Win key). Different from `hold_key` (which holds without performing other actions).

**Coordinate scaling.** *Note:* Claude Opus 4.7 supports up to 2576 px on long edge, 1:1 with image pixels. Earlier models: API constrains images to ≤1568 px on the longest edge and ~1.15 megapixels total. So a 1512x982 screen gets downsampled to ~1330x864; Claude returns coordinates in the downsampled space, but your tool clicks the original screen. Resize screenshots yourself and scale Claude's coordinates back up using `scale = min(1.0, 1568/long_edge, sqrt(1_150_000/total_pixels))`.

**Agent loop pattern.** Iteration-capped `while True` loop: call `client.beta.messages.create(...)`; append assistant content; collect `tool_use` blocks; execute each via your action handlers; append `tool_result` user message; repeat until no tools used. Iteration cap prevents runaway costs.

**Best practices.** Specify simple well-defined tasks; instruct "After each step, take a screenshot and carefully evaluate if you achieved the right outcome" to prevent assumed outcomes; use keyboard shortcuts for tricky UI (dropdowns, scrollbars); include example screenshots for repeatable tasks; pass credentials inside `<robot_credentials>` XML tags (see jailbreak mitigation guide first). For multi-session agents, run end-to-end verification at the start of each session, not just after implementation.

**Combining.** Add bash and text-editor tools in the same `tools` array. Pair with [[Extended-thinking]] for visible reasoning. Custom tools work normally.

**Limitations.** Latency unsuitable for fast human-AI interaction—use for background gathering, automated testing. Computer-vision accuracy: Claude may hallucinate coordinates; thinking helps debug. Tool selection less reliable on niche/multi-app workflows. Spreadsheet interaction improved with `left_mouse_down`/`up` and modifier keys. Account creation and content generation on social platforms is limited. Vulnerabilities (jailbreaking, prompt injection) persist; never grant computer use access to sensitive accounts without strict oversight.

**Pricing.** Computer-use beta adds **466–499 system prompt tokens**. Tool definition: **735 input tokens** (Claude 4.x and Sonnet 3.7). Plus screenshot tokens (see [[Vision]] pricing) and tool result tokens. Bash and text editor tools have separate token costs.

**Data retention.** ZDR-eligible because all screenshots/inputs/files are stored client-side; Anthropic processes them in real time per request and does not retain after response.
