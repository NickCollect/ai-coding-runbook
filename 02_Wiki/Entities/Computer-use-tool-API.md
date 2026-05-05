---
type: entity
name: Computer-use-tool-API
aliases: [computer use (API) / computer_20251124 / computer_20250124]
category: api-tool
status: beta
created: 2026-05-05
---

## 一句话定义

Anthropic API 的 client-side computer use tool —— Claude 通过 screenshot + mouse + keyboard + window 控制操作桌面（**与 Claude Code 的 [[Computer-use]] 区分**：这里指 Anthropic API 的 server-defined tool schema）。

## 关键属性

- **Beta header**：`computer-use-2025-11-24`（Opus 4.7/4.6 / Sonnet 4.6 / Opus 4.5） / `computer-use-2025-01-24`（更早模型） [[computer-use-tool--at]]
- **Client-side**：API 不直连环境，回 `tool_use` 让你 app 在 VM/容器里执行 + 截图 + 回 `tool_result`；reference impl `anthropics/anthropic-quickstarts/computer-use-demo` [[computer-use-tool--at]] [[computer-use-demo-README--quickstart]]
- **Tool definition**：`{type: "computer_20251124", name: "computer", display_width_px, display_height_px, optional display_number, enable_zoom: true (only _20251124)}` [[computer-use-tool--at]]
- **Actions（基础版，所有版本）**：`screenshot` / `left_click [x,y]` / `type` / `key` (`"ctrl+s"`) / `mouse_move` [[computer-use-tool--at]]
- **Actions（`_20250124` 增强）**：`scroll` / `left_click_drag` / `right_click` / `middle_click` / `double_click` / `triple_click` / `left_mouse_down` / `left_mouse_up` / `hold_key` / `wait` [[computer-use-tool--at]]
- **Actions（`_20251124` 增强）**：以上 + `zoom`（view region 全分辨率，需 `enable_zoom: true`） [[computer-use-tool--at]]
- **Modifier keys**：click/scroll 用 `text` 参数 = `"shift"` / `"ctrl"` / `"alt"` / `"super"` [[computer-use-tool--at]]
- **Coordinate scaling**：Opus 4.7 支持 2576 px long edge 1:1 像素；更早模型 ≤1568 px + ~1.15 MP 总 → screenshot 自动 downsample，client 用 `scale = min(1.0, 1568/long_edge, sqrt(1_150_000/total_pixels))` 还原坐标 [[computer-use-tool--at]] [[Vision]]
- **Computing env**：sandbox VM/容器 + virtual X11 (Xvfb) + Mutter window manager + Tint2 panel + 预装 Firefox/LibreOffice 等 [[computer-use-tool--at]]
- **Security**：dedicated VM、minimal privileges、无 sensitive data、allowlist domains、human-in-the-loop confirm；Anthropic auto-runs prompt-injection 分类器 on screenshots → trigger user-confirm prompts；headless 用支持 opt-out [[computer-use-tool--at]]
- **Best practices**：simple well-defined task、"After each step, take a screenshot and carefully evaluate" 防假定结果、keyboard shortcuts、example screenshots、credentials 用 `<robot_credentials>` XML tag [[computer-use-tool--at]]
- **Combine**：与 [[Bash-tool-API]] + [[Text-editor-tool]] 同 array 用；配 [[Extended-thinking]] 看推理 [[computer-use-tool--at]]
- **Limitations**：latency 不适合实时人机交互、coord hallucination、niche multi-app workflow 不稳、social platforms 限制 [[computer-use-tool--at]]
- **Pricing**：beta system prompt +466-499 token；tool definition +**735 input tokens**；加 screenshot token (per [[Vision]] pricing) + tool result token [[computer-use-tool--at]]
- **ZDR-eligible**（screenshot/inputs/files 全 client-side） [[computer-use-tool--at]]

## 出现来源

_13 summaries reference this entity_ ——
- [[computer-use-tool--at]] / [[tool-use-overview--at]] / [[tool-reference--at]] / [[tool-combinations--at]]
- [[server-tools--at]] / [[manage-tool-context--at]]
- [[vision--bwc]] / [[adaptive-thinking--bwc]] / [[api-and-data-retention--bwc]]
- [[computer-use-demo-README--quickstart]] / [[browser-use-demo-README--quickstart]]

## 相关

- [[Computer-use]] —— Claude Code 的 computer use（不同 product）
- [[Bash-tool-API]] / [[Text-editor-tool]] —— canonical 三件套
- [[Vision]] —— screenshot 经过 Vision pipeline
- [[Extended-thinking]] —— debugging coord hallucination 用
- [[Tool-use]] / [[Messages-API]]
