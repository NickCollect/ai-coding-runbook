---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/slash-commands.md
source_url: https://code.claude.com/docs/en/agent-sdk/slash-commands
title: "Claude Agent SDK — Slash Commands"
summarized_at: 2026-05-05
entities_referenced:
  - Agent-SDK.md
concepts_referenced:
  - Agentic-loop.md
---

Slash Commands 是以 `/` 开头的特殊命令，用于通过 SDK 控制 Claude Code 会话。只有不依赖交互式终端的命令才能通过 SDK 分发；可用命令列表在 `system/init` 消息中返回。

## 发现可用命令

在 `system` init 消息中读取 `slash_commands` 字段：

```typescript
for await (const message of query({ prompt: "Hello Claude", options: { maxTurns: 1 } })) {
  if (message.type === "system" && message.subtype === "init") {
    console.log("Available slash commands:", message.slash_commands);
    // 示例：["/compact", "/context", "/usage"]
  }
}
```

## 发送 Slash Commands

直接将命令作为 `prompt` 字符串传入：

```typescript
for await (const message of query({ prompt: "/compact", options: { maxTurns: 1 } })) {
  if (message.type === "result") console.log("Command executed:", message.result);
}
```

## 常用内置命令

### `/compact` — 压缩对话历史

将历史消息摘要化以释放 context 空间，同时保留重要上下文。响应包含 `compact_boundary` system 消息，含 `pre_tokens`（压缩前 token 数）和 `trigger` 字段。

### `/clear`（不可用）

交互式 `/clear` 在 SDK 中不可用。每次 `query()` 调用已创建新对话；若需清空上下文，结束当前 `query()` 并开新一个即可（旧对话仍保留在磁盘，可通过 session ID 的 `resume` 选项恢复）。

## 创建自定义 Slash Commands

自定义命令以 Markdown 文件形式定义在特定目录：

- **项目命令**：`.claude/commands/`（仅当前项目可用）
- **个人命令**：`~/.claude/commands/`（所有项目可用）

> **注**：`.claude/commands/` 是旧格式。推荐新格式为 `.claude/skills/<name>/SKILL.md`，支持同样的 `/name` 调用，同时支持 Claude 自主调用。

### 文件格式

- 文件名（去掉 `.md`）即命令名
- 文件正文定义命令行为
- 可选 YAML frontmatter 提供配置

**基础示例** `.claude/commands/refactor.md`：

```markdown
Refactor the selected code to improve readability and maintainability.
```

**带 frontmatter 示例**：

```markdown
---
allowed-tools: Read, Grep, Glob
description: Run security vulnerability scan
model: claude-opus-4-7
---
Analyze the codebase for security vulnerabilities...
```

### 高级特性

**动态参数**（用 `$1`、`$2` 或 `$ARGUMENTS` 占位符）：

```markdown
---
argument-hint: [issue-number] [priority]
---
Fix issue #$1 with priority $2.
```

**内联 Bash 输出**（`!` 前缀）：

```markdown
## Context
- Current status: !`git status`
- Current diff: !`git diff HEAD`
```

**文件引用**（`@` 前缀）：

```markdown
Review the following: @package.json @tsconfig.json
```

**命名空间**（子目录组织）：

```
.claude/commands/
├── frontend/
│   └── component.md    # 创建 /component
├── backend/
│   └── api-test.md     # 创建 /api-test
└── review.md           # 创建 /review
```

子目录名显示在命令描述中，但不影响命令名称本身。

### SDK 中使用自定义命令

自定义命令与内置命令一样出现在 `slash_commands` 列表中，使用方式相同：

```typescript
for await (const message of query({ prompt: "/refactor src/auth/login.ts", options: { maxTurns: 3 } })) {
  if (message.type === "assistant") console.log("Suggestions:", message.message);
}
```
