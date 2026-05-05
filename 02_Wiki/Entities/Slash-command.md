---
type: entity
name: Slash-command
aliases: [slash command, slash-command, /command]
category: feature
status: ga
created: 2026-05-05
---

## 一句话定义

在 Claude Code 输入 `/<name>` 触发的命令，可由 plugin / user 定义

## 关键属性

- 在 prompt 开头输入 `/<name>` 触发；只有消息开头识别，session 内键入 `/` 列出所有 [[commands]]
- 三种来源：项目 `.claude/commands/` 标 `(project)`、个人 `~/.claude/commands/` 标 `(user)`、plugin `<plugin>/commands/` 标 `(plugin-name)`，子目录形成 namespace（如 `commands/ci/build.md` → `/build (project:ci)`）[[SKILL--command-development]] [[slash-commands--agent-sdk]]
- Markdown 文件，文件名（去 `.md`）即命令名；frontmatter 全部 optional，body 是发给 Claude 的指令而**不是给用户看的说明** [[SKILL--command-development]] [[simple-commands]]
- Frontmatter 字段：`description`（≤60 字符）、`allowed-tools`（如 `Read, Bash(git:*)`）、`model`（sonnet/opus/haiku）、`argument-hint`（自动补全提示）、`disable-model-invocation`（boolean，限用户手动） [[frontmatter-reference--plugin-dev]]
- Body 三种动态注入：`$1`/`$2`/`$ARGUMENTS` 位置参数、`` !`cmd` `` 内联 bash 输出、`@path/to/file` 引用文件内容 [[slash-commands--agent-sdk]] [[SKILL--command-development]]
- Plugin 命令必须用 `${CLAUDE_PLUGIN_ROOT}` 解析 plugin 内部路径，相对路径 `./` 会按 cwd 解析而非 plugin 根 [[SKILL--command-development]] [[plugin-commands-examples--plugin-dev]]
- Bash 内联执行需要 frontmatter `allowed-tools` 包含 `Bash`（建议加命令过滤如 `Bash(git:*)`）；不加会失败 [[plugin-commands-examples--plugin-dev]] [[frontmatter-reference--plugin-dev]]
- `disable-model-invocation: true` 时仅用户键入触发，Claude 不能通过 SlashCommand tool 程序化调用 — 用于生产部署批准等手动操作 [[frontmatter-reference--plugin-dev]]
- 复杂多选交互用 `AskUserQuestion` tool（≤4 questions/call，每题 2-4 options，header ≤12 字符），简单已知值用位置参数 [[interactive-commands]]
- SDK 内 `query({ prompt: "/compact" })` 直接发送；可用命令在 `system/init` 的 `slash_commands` 字段；`/clear` SDK 内不可用（每次 query 已是新会话） [[slash-commands--agent-sdk]]
- MCP server 提供的 prompts 自动暴露为 `/mcp__<server>__<prompt>`；命令支持 namespace 子目录但子目录名不改命令本身 [[commands]] [[slash-commands--agent-sdk]]
- 推荐替代：新增"Claude 可自主调用"的命令，写成 `.claude/skills/<name>/SKILL.md`；`/commands/` 是 legacy 格式但仍支持 [[slash-commands--agent-sdk]]
- 内置命令分类涵盖 session（`/clear`、`/compact`、`/resume`）、配置（`/model`、`/effort`、`/sandbox`、`/fast`）、skills/plugins/agents 管理、`/install-github-app`、bundled skills（`/loop`、`/simplify`、`/review`） [[commands]]

## 出现来源

_66 summaries reference this entity_:

- [[2026-w14]]
- [[README--commit-commands]]
- [[README--hookify]]
- [[README--plugin-dev]]
- [[SKILL--command-development]]
- [[advanced-plugin]]
- [[advanced-workflows]]
- [[agent-sdk-dev--readme]]
- [[cancel-ralph]]
- [[changelog]]
- [[claude-dedupe-issues]]
- [[claude-directory]]
- [[clean_gone--commit-commands]]
- [[code-review--plugin-command]]
- [[code-review--readme]]
- [[command-development--readme]]
- [[commands]]
- [[commit--plugin-command]]
- [[commit-push-pr]]
- [[component-patterns--plugin-dev]]
- [[configure--hookify]]
- [[context-window]]
- [[create-plugin]]
- [[create-settings-command]]
- [[debug-your-config]]
- [[desktop-quickstart]]
- [[documentation-patterns]]
- [[feature-dev-cmd--feature-dev]]
- [[feature-dev-readme--feature-dev]]
- [[frontmatter-reference--plugin-dev]]
- [[help--hookify]]
- [[help--ralph-wiggum]]
- [[hookify]]
- [[interactive-commands]]
- [[interactive-mode]]
- [[list--hookify]]
- [[manifest-reference--plugin-structure]]
- [[marketplace-considerations]]
- [[minimal-plugin]]
- [[new-sdk-app--agent-sdk-dev]]
- [[overview--agent-sdk]]
- [[overview--claude-code]]
- [[plugin-commands-examples--plugin-dev]]
- [[plugin-features-reference]]
- [[plugin-settings--skill]]
- [[plugin-structure-skill--plugin-dev]]
- [[plugins]]
- [[plugins--agent-sdk]]
- [[plugins-readme--claude-code-repo]]
- [[plugins-reference]]
- [[pr-review-toolkit-readme]]
- [[quickstart--claude-code]]
- [[ralph-loop]]
- [[ralph-wiggum-readme]]
- [[review-pr]]
- [[scheduled-tasks]]
- [[simple-commands]]
- [[skills]]
- [[skills--agent-sdk]]
- [[slash-commands--agent-sdk]]
- [[standard-plugin]]
- [[sub-agents]]
- [[testing-strategies--plugin-dev]]
- [[tool-usage--mcp-integration]]
- [[vs-code]]
- [[whats-new]]

## 相关

- [[Skill]] — 推荐替代 legacy `/commands/`；skill 同时支持 `/name` 触发和模型自主调用
- [[Plugin]] — plugin 可打包 commands，安装即扩展 `/`
- [[MCP-server]] — MCP prompts 暴露为 `/mcp__<server>__<prompt>`
- [[Subagent]] — 命令可在 body 里 "Launch the [agent] agent" 委派给 subagent
- [[Hooks]] — UserPromptSubmit / PreToolUse hooks 可拦截或扩展命令执行
- [[Settings]] — `allowed-tools` 与全局 permission rules 互动
