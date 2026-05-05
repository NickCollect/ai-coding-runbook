---
type: summary
source: 01_Raw/docs.cursor.com/docs--agent--prompting.md
source_url: https://cursor.com/docs/agent/prompting
title: "Prompting Agents"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

通过 chat 输入框向 Agent 发送文字、图片或语音指令，可随时切换模型。

**@ 提及**：在输入框输入 `@` 可附加特定上下文：
- `@文件/文件夹`：直接引用代码文件
- `@Docs`：搜索已索引文档（支持添加自定义文档）
- `@Terminals`：将终端输出作为上下文
- `@Past Chats`：引用历史对话
- `@Commit (Diff of Working State)`：未提交变更的 diff
- `@Branch (Diff with Main)`：整个分支的 diff
- `@Browser`：附加浏览器当前页面上下文

**图片输入**：拖拽图片文件到输入框，或 Cmd+V 粘贴截图，适用于 UI 实现、视觉调试等场景。

**语音输入**：点击麦克风图标，口述指令，支持技术术语，发送前可审查转录文本。

**切换模型**：顶部模式选择器下拉框或 Cmd/（斜杠）循环切换；快速任务用轻量模型，复杂推理用高能力模型；可在对话中途切换。默认模型在 Cursor Settings > Models 设置。
