---
type: entity
name: Checkpointing
aliases: [checkpoint, file checkpoints]
category: feature
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 文件变更的快照机制，可回滚

## 关键属性

- 每个 user prompt 自动创建一个 checkpoint，跨 session 持久（`--resume` 后仍可访问），与 session 一起 30 天清理（可配置）[[checkpointing]]
- `Esc Esc` 或 `/rewind` 打开菜单，列出 prompts 可选 4 种动作：restore code+conversation / restore conversation only / restore code only / summarize from here [[checkpointing]] [[interactive-mode]]
- "Summarize from here" 是定向压缩单点（替换选定 message + 之后内容为简短 AI summary），与 `/compact` 整轮压缩不同；不动文件，原始 message 保留在 transcript [[checkpointing]]
- restore conversation / summarize 后，原 prompt 自动回填输入框，方便编辑重发 [[checkpointing]]
- **关键限制**：只追踪 Write / Edit / NotebookEdit 等 file-edit tool 的改动；**Bash tool 的 `rm` / `mv` / `cp` / `echo >` / `sed -i` 全部不追踪**，无法 undo [[checkpointing]] [[file-checkpointing]]
- 不追踪外部修改（Claude Code 之外 + 并行 session 的编辑），除非碰到同一文件 [[checkpointing]]
- 不是 Git 替代品：checkpoint = local undo，git = permanent history [[checkpointing]] [[how-claude-code-works]]
- Agent SDK 启用要同时设 `enableFileCheckpointing: true` + `extraArgs: { "replay-user-messages": null }`（缺后者拿不到 UUID）[[file-checkpointing]]
- Capture pattern：iterate stream，从首个 `UserMessage.uuid` 拿 checkpoint id，从 `ResultMessage.session_id` 拿 session id；rewind 走 `rewindFiles(uuid)` / `rewind_files(uuid)`，**只回滚文件，不回滚对话历史** [[file-checkpointing]]
- CLI 等价命令：`claude -p --resume <session-id> --rewind-files <checkpoint-uuid>` [[file-checkpointing]]
- 常见错误：缺 `replay-user-messages` flag → "User messages don't have UUIDs"；resume 后没先发空 prompt → "ProcessTransport is not ready for writing" [[file-checkpointing]]
- 适用场景：探索另一种实现 / 撤销错误 / 释放 context 空间；想"保留原 session + 试新方向"则用 `--fork-session` 而非 rewind [[checkpointing]] [[best-practices]]
- "Tool use or thinking block mismatch" 等 corrupted history 错误的标准恢复手段就是 `/rewind` 或 Esc Esc 回退到出错前 [[errors]]
- 关闭 checkpoint：`CLAUDE_CODE_DISABLE_FILE_CHECKPOINTING` env [[env-vars]]

## 出现来源

_15 summaries reference this entity_:

- [[best-practices]]
- [[changelog--claude-code-repo]]
- [[checkpointing]]
- [[commands]]
- [[communications-kit]]
- [[desktop]]
- [[env-vars]]
- [[errors]]
- [[file-checkpointing]]
- [[glossary]]
- [[hooks]]
- [[how-claude-code-works]]
- [[interactive-mode]]
- [[sessions--agent-sdk]]
- [[vs-code]]

## 相关

- [[Agent-SDK]] — SDK 通过 `enableFileCheckpointing` + `replay-user-messages` 启用
- [[Permission-mode]] — 通常配合 `acceptEdits` 使用，避免 file edit 反复弹 prompt
- [[Memory]] — checkpoint 与 session 一起持久化在 `~/.claude/projects/`
- [[Hooks]] — `UserMessage` 携带 checkpoint UUID，hook 流可观察
- [[Agentic-loop]] — loop 中每个 file-edit tool 触发自动 snapshot
