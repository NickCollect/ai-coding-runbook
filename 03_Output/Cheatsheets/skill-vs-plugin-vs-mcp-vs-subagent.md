---
type: cheatsheet
topic: skill-vs-plugin-vs-mcp-vs-subagent
last_updated: 2026-05-05
based_on:
  - 02_Wiki/Entities/Skill.md
  - 02_Wiki/Entities/Plugin.md
  - 02_Wiki/Entities/MCP-server.md
  - 02_Wiki/Entities/Subagent.md
  - 02_Wiki/Entities/Hooks.md
---

# Skill vs Plugin vs MCP-server vs Subagent — 怎么选

> Claude Code 4 种最常被混淆的扩展机制。一句话区分：
> - **Skill** = 一份可加载的"专项知识 + 流程"（文件，本地）
> - **Plugin** = 多种东西的**打包分发**容器（可含 skills/hooks/MCP/subagents/commands）
> - **MCP-server** = 把**外部服务**接进来当 tool（进程，远程或本地）
> - **Subagent** = **隔离 context** 的子 agent（运行时，不是文件）

---

## 决策矩阵

| 你想 ... | 用 | 原因 |
|---|---|---|
| 把"PDF 处理"这样一个**专项流程**变成 Claude 自动调用的能力 | **Skill** | model-invoked、文件少、本地路径就能跑 |
| 给 IDE / 终端添加一个 **`/foo` 命令**，按下就跑特定逻辑 | **Slash-command**（不在本表，但属同一族）| 也可写成 user-invocable Skill，二者同名时 skill 胜 |
| 把"GitHub PR 工具集 + 配套 hook + 脚本"作为**一个包分发**给团队 | **Plugin** | 唯一支持 marketplace + 版本化分发的容器 |
| 让 Claude 能查公司内部 **数据库 / 私有 API** | **MCP-server** | MCP 是接外部服务的标准协议；写自定义 tool 是替代但麻烦 |
| 让 Claude **大批量做某类任务**（如"扫 50 个文件查 bug"），又不想污染主 context | **Subagent** | 隔离 context，最终只回主一条总结 |
| 在 commit 前**强制 lint**、把 prompt **强制改写**、调用前**审核 tool 参数** | **Hook** | 唯一在生命周期固定点 deterministic 触发的机制 |
| 做一个**复合产品**：CLI 命令 + 后台 hook + MCP server + 自定义 subagent + 输出风格 | **Plugin**（含 skills + hooks + MCP + subagents） | 因为 plugin 是唯一能打包多种 component 的容器 |

---

## 五维属性对比

|  | **Skill** | **Plugin** | **MCP-server** | **Subagent** |
|---|---|---|---|---|
| **本质** | 文件系统 artifact（`<n>/SKILL.md`） | 文件系统目录（`.claude-plugin/plugin.json`） | 进程（stdio / SSE / HTTP / WebSocket） | 运行时实例（隔离 context） |
| **触发** | model 自动 / `/skill-name` 显式 | install 后其内部组件按各自规则生效 | tool call（受 `allowedTools` 控制） | Agent tool 委派（自动 or `@"agent-name"`） |
| **隔离** | 共享主 context（SKILL.md 渲染入 session） | N/A（容器） | tool 调用边界（Claude 不见 server 内部） | **整个 context 隔离**（最强） |
| **跨 project 分发** | ⚠️ 手动 copy / git submodule | ✅ marketplace + semver | 配置文件 copy / OAuth | 文件 copy (`.claude/agents/*.md`) |
| **可包含别的扩展** | ❌（独立单元） | ✅ skills + commands + hooks + MCP + subagents + output-styles + LSP + monitors + themes | ❌ | 可在 frontmatter 引用 skills + memory |
| **版本** | 文件夹覆盖 | semver / git SHA | server 端自管 | 文件覆盖 |
| **存储路径优先级** | enterprise > personal `~/.claude/skills/` > project `.claude/skills/` > plugin | managed > user > project > local > plugin | `.mcp.json` 项目级、`mcpServers` 配置或 plugin 内置 | managed > `--agents` flag > project `.claude/agents/` > user `~/.claude/agents/` > plugin |

---

## 5 个常见组合 pattern

1. **Skill + Hook**：Skill 提供"PDF 处理"流程，Hook 在 `PostToolUse` 后自动验证输出 → 用户只装 skill 就行（hook 由 plugin 一并打包）
2. **MCP + Subagent**：MCP 提供数据库 tool，Subagent 用其完成大批量查询（隔离 context 防主对话被填满 row data）
3. **Plugin = Skills + Commands + Hooks**：典型 dev workflow plugin（如 `pr-review-toolkit`）
4. **Subagent 做重活，主 agent 看结论**：`Explore`（只读 codebase 搜索）/ `Plan`（生成实施计划）就是这个 pattern 的 built-in 版
5. **Skill 内嵌 Subagent**：SKILL.md 里 `agent: <subagent-name>` → 每次 invoke skill 自动 fork 一个 subagent 跑（适合长链路任务）

---

## 易踩的坑

- **Skill 同名时优先于 Slash-command**：老的 `.claude/commands/foo.md` 与新的 `.claude/skills/foo/SKILL.md` 都创建 `/foo`，但 skill 胜（[[Skill]]）
- **Plugin 内 subagent 的 `hooks`/`mcpServers`/`permissionMode` 字段被忽略**（安全）—— 改用 plugin 顶层配置（[[Plugin]] [[Subagent]]）
- **`bypassPermissions` 模式下，subagent 强制继承父模式**：等于把"自主全权访问"交给受约束更少的 subagent system prompt（[[Subagent]]）
- **MCP 的 SSE transport 已 deprecated** —— 新项目用 streamable HTTP（[[MCP-server]]）
- **Skill 在 SDK 里必须 `"Skill"` 在 `allowedTools`** 才生效；且 SDK 忽略 SKILL.md 的 `allowed-tools` 字段（CLI 才 honor）（[[Skill]]）
- **Hooks 只能 tighten 不能 loosen**：`PreToolUse` deny 在 `bypassPermissions` 也生效；`allow` 不能绕过 settings/managed 的 deny rule（[[Hooks]]）

---

## 详细引用

- [[Skill]] · [[Plugin]] · [[MCP-server]] · [[Subagent]] · [[Hooks]]
- [[Plugin-marketplace]] —— plugin 的发现 / 分发渠道
- [[Permission-mode]] —— `bypassPermissions` / `acceptEdits` / `default` / `auto` / `plan`
- [[Slash-command]] —— `/foo` 命令体系
