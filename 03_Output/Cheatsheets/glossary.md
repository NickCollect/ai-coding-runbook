---
type: cheatsheet
topic: glossary
last_updated: 2026-05-05
based_on:
  - 02_Wiki/_canonical-names.md
  - 02_Wiki/Summaries/glossary.md
  - 02_Wiki/Entities/*.md
---

# Claude Code 术语速查

> Anthropic 自己对同一概念有时多种写法。这是 vault 内 canonical 名 + 一句话定义 + 链接。
> 完整 entity registry [[_canonical-names]]。

---

## 核心扩展机制

| Canonical | 一句话 | 链接 |
|---|---|---|
| **Skill** | 可加载的"专项流程"文件，按 SKILL.md 触发 | [[Skill]] |
| **Plugin** | 可分发的容器，能打包 skills/hooks/MCP/subagents/commands 等 | [[Plugin]] |
| **MCP-server** | 通过 MCP 协议接入的外部 tool 服务器 | [[MCP-server]] |
| **Subagent** | 隔离 context 的子 agent | [[Subagent]] |
| **Hooks** | session lifecycle 各点 deterministic 触发的命令 | [[Hooks]] |
| **Slash-command** | `/foo` 命令（user-invocable） | [[Slash-command]] |
| **Output-style** | Claude 输出格式风格 | [[Output-style]] |
| **Status-line** | 终端底部可定制状态栏 | [[Status-line]] |
| **Memory** | 跨 session 的持久 memory（CLAUDE.md / auto-memory） | [[Memory]] |
| **Checkpointing** | 文件变更快照（可回滚） | [[Checkpointing]] |
| **Plugin-marketplace** | Plugin 的发现 / 分发渠道 | [[Plugin-marketplace]] |
| **Settings** | 多层 cascading 配置（managed > user > project > local） | [[Settings]] |

---

## 执行模式 / Config

| Canonical | 一句话 | 链接 |
|---|---|---|
| **Permission-mode** | tool 调用授权策略 (`default` / `acceptEdits` / `bypassPermissions` / `auto` / `plan`) | [[Permission-mode]] |
| **Sandboxing** | 命令执行的沙箱隔离（filesystem / network） | [[Sandboxing]] |
| **Auto-mode** | `auto` permission mode 的精细规则配置 | [[Auto-mode]] |
| **Fast-mode** | 用 Opus 4.6 的低延迟交互模式 | [[Fast-mode]] |
| **Headless-mode** | 非交互式（脚本 / CI / SDK）调用模式 | [[Headless-mode]] |
| **Computer-use** | Claude 控制鼠标/键盘/屏幕的 tool | [[Computer-use]] |

---

## 接口 / Integration

| Canonical | 含义 | 链接 |
|---|---|---|
| **Agent-SDK** | Anthropic Python SDK，构建 Claude Code-同款 agent app | [[Agent-SDK]] |
| **IDE-integration** | VS Code / JetBrains / Chrome 扩展 | [[IDE-integration]] |
| **Native-interface** | CLI / Desktop / Web / Slack 等接入方式 | [[Native-interface]] |
| **CI-integration** | GitHub Actions / GitLab CI/CD | [[CI-integration]] |
| **Enterprise-gateway** | Bedrock / Vertex AI / Foundry / 自建 LLM gateway | [[Enterprise-gateway]] |

---

## Scheduled / Background

| Canonical | 含义 | 链接 |
|---|---|---|
| **Routine** | 云端按 cron 跑的 scheduled agent | [[Routine]] |
| **Scheduled-task** | 桌面端的本地定时任务 | [[Scheduled-task]] |

---

## 概念 (Concepts)

| Canonical | 一句话 | 链接 |
|---|---|---|
| **Agentic-loop** | 思考→调工具→看结果→再思考 的循环 | [[Agentic-loop]] |
| **Context-window** | input + output token 上限（Opus 4.7 = 1M） | [[Context-window]] |
| **Channel** | Claude Code 的通信通道抽象（push 模型 + 双向） | [[Channel]] |
| **Agent-team** | 多 subagent 协作组成的 team | [[Agent-team]] |
| **Tool-use** | Claude 通过结构化输出调用外部工具的协议 | [[Tool-use]] |

---

## 跨产品（API 层概念，P1 起 stub，P2 完整）

| Canonical | 一句话 | 链接 |
|---|---|---|
| **Extended-thinking** | Claude 输出 reasoning trace 的模式 | [[Extended-thinking]] |
| **Prompt-caching** | 跨请求复用 prompt prefix | [[Prompt-caching]] |

---

## Anthropic 同概念多写法（注意！）

raw 文档自己就不统一，**vault 内一律用左列**（canonical）：

| Canonical | Raw 出现的变体 |
|---|---|
| `Subagent` | sub-agent / sub agent / subagents / Sub-agent |
| `Slash-command` | slash command / slash-command / /command |
| `MCP-server` | MCP / Model Context Protocol server |
| `Skill` | skills / Anthropic Skill / agent skill |
| `Hooks` | hook / hook system / session hooks |
| `Tool-use` | function calling / tool calling |
| `Computer-use` | computer use / computer-use tool |
| `Agent-SDK` | claude-agent-sdk / agent-sdk |
| `Status-line` | statusline / status line |
| `Plugin-marketplace` | plugin marketplace / marketplace |

---

## Model 速查

| Canonical | model ID（写在 settings / SDK 用） |
|---|---|
| Opus 4.7 | `claude-opus-4-7` |
| Opus 4.6 | `claude-opus-4-6`（Fast mode 用此 model） |
| Sonnet 4.6 | `claude-sonnet-4-6` |
| Haiku 4.5 | `claude-haiku-4-5-20251001` |

---

## 引用规则

vault 内写 wikilink 永远用 canonical 名（左列）。**raw 里看到右列变体不要照抄进 vault** —— 在对应 entity 的 frontmatter `aliases:` 字段加变体即可。

新发现 raw 里出现新写法 / 新概念 → 先在 [[_canonical-names]] 登记 → 再 enrich entity。
