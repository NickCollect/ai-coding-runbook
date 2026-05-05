# AI Coding Runbook — Agent 操作规则（session 启动钩子）

> Claude Code / Cursor / Codex 等 agent 进 session 自动加载本文件（`AGENTS.md` 是 symlink，内容 100% 一致）。
>
> 这是**操作 hook + 关键规则**。完整工作手册见 `README.md`（master）。冲突时以 `README.md` 为准。
>
> **项目**：多厂商 AI 编程工具知识库（Anthropic · OpenAI · Google · Cursor）。GitHub: `NickCollect/ai-coding-runbook`。

---

## 一、对话开始时（必做）

1. 跑 `python3 scripts/check_pending.py` → 把输出**完整**展示给用户
2. 看 `03_Output/Changelog/` 里**最新一份**（按文件名日期排序），告诉用户"上次 GHA 刷新带来 N 个文件改动"。注意：GHA 现在是 matrix 并行，每个 source 单独 commit，changelog 是聚合视图
3. **有 pending**：等用户授权（"ingest" / "ingest 1,3" / "skip" / 自然语言）才开始处理
4. **无 pending + 无新 changelog**：简短确认，等其他指令

---

## 二、Wiki 三层架构（速记）

```
01_Raw/       ← 真理之源，read-only（GHA bot 写，人 / LLM 永远不能改）
  ├── docs.claude.com/      （Anthropic Claude 官方文档）
  ├── anthropic.com/        （news / research / engineering blog）
  ├── docs.openai.com/      （OpenAI 平台文档）
  ├── docs.cursor.com/      （Cursor IDE 文档，llms.txt 全量）
  ├── ai.google.dev/        （Gemini API 文档）
  └── github/               （anthropics/* + modelcontextprotocol/* + openai/* 的 git clone）

02_Wiki/      ← 加工层（神经元）
  ├── Entities/    （具体的工具 / feature 档案：Skills.md, Hooks.md, MCP-server.md, Subagents.md ...）
  ├── Concepts/    （抽象概念：context-window.md, agentic-loop.md, prompt-caching.md ...）
  ├── Summaries/   （每份 raw 的 1:1 摘要）
  ├── Synthesis/   （跨多 entity 的综述）
  ├── Comparison/  （横向对比 / decision matrix：skill-vs-mcp-vs-subagent.md ...）
  └── QA/          （问答沉淀）

03_Output/    ← 对外交付 + 监控
  ├── Cheatsheets/   （日常速查：keybindings、hook recipes、常用 slash commands）
  ├── Changelog/     （GHA 每次 refresh 自动生成 YYYY-MM-DD.md）
  ├── My-Setup/      （维护者的 plugin/skill/hook 配置笔记，手维护）
  └── templates/     （cheatsheet 模板，将来加）
```

详细架构 → `README.md` § 二。

---

## 三、Ingest 工作流（用户授权后）

按 Phase A→E 顺序，**每 Phase 完成后必须 self-review**：

| Phase | 做啥 | self-review checkpoint |
|---|---|---|
| **A · Summary 创建** | 对每个 pending raw 写 summary 到 `02_Wiki/Summaries/` | frontmatter 合规？source 字段指向 `01_Raw/` 真路径？是否同名碰撞？|
| **B · 已有 entity / concept 更新** | 在 `## 出现来源` 追加 source；如有新事实更新 `## 关键属性` | **不创建新文件**；wikilink 指向真存在；事实都能在新 summary 里找到原文支撑（**无幻觉**）|
| **C · 新名字处理（必须问用户）** | 列出新 entity / concept 候选，等用户选择是否建 stub | 用户授权后才建 stub |
| **D · Audit** | 跑 `python3 scripts/audit.py` | 列修复建议但不自动修 |
| **E · 日志** | 在 `02_Wiki/_progress.log` 追加：`[YYYY-MM-DD HH:MM] INGEST - <N> summaries / ...` | — |

**为什么每 Phase self-review**：防上一阶段幻觉污染下一阶段。详细见 `README.md` § 五。

---

## 四、🚨 关键踩坑（top 8，必须避免）

1. **绝对不改 `01_Raw/`** —— raw 是 ground truth，只有 GHA bot 写。手动改 raw 会污染 diff、误导 enrichment。要纠错走 `02_Wiki/_canonical-names.md` 走勘误表机制。
2. **建 Entity / Concept 前必查** —— `ls 02_Wiki/Entities/ 02_Wiki/Concepts/` + grep frontmatter `aliases`，避免造 ghost entity。Anthropic 同一概念有多名（Sub-agent / Subagent / Sub agent；MCP server / MCP；Tool use / Function calling），靠 canonical-names.md 统一。
3. **Verbatim quote 必须有 source** —— 引号 (「」/ "") 必须能在某 raw 文档里精确搜到。找不到原文的降级为 paraphrase 或 *italic*。
4. **Wikilink 必须指向真文件** —— `[[X]]` 引用前 `ls 02_Wiki/{Entities,Concepts}/` 确认。死链由 audit 抓，但写时就该避免。
5. **不能凭"我记得某工具有这个 feature"写 entity** —— 任何事实必须能 trace 回某份 raw 文件。模型权重里的训练知识 vs raw 里的当前文档以 raw 为准（各厂商改 API 频繁）。
6. **Subagent finding 不能直接 trust** —— 调用 subagent 调研后，master 阶段必须 sample re-verify（≥3 + 全部 MAJOR claim）。
7. **Frontmatter 规范严格** —— Summary 必须有 `source:` 指向 `01_Raw/...`；Entity / Concept 必须有 `name:` + `## 出现来源` section。
8. **多机器同步** —— 通过 git 同步，不依赖 iCloud。绝对路径都用 `~` 或 project-relative，不要 hardcode 用户名或本地路径。本地文件夹名可能改变，以 remote URL 为准：`https://github.com/NickCollect/ai-coding-runbook`。

---

## 五、写入边界

**✅ 可写**：
- `02_Wiki/**`（vault 内容）
- `03_Output/Cheatsheets/**`、`03_Output/My-Setup/**`
- `02_Wiki/_progress.log`、`02_Wiki/_canonical-names.md`
- `docs/**`（设计文档）

**❌ 禁写（人 / LLM 都不写）**：
- `01_Raw/**`（read-only，**只有 GHA bot 能写**）
- `03_Output/Changelog/**`（GHA 自动生成）
- `scripts/**`（除非用户明确要求改脚本）
- `.github/workflows/**`（同上）
- `system_instructions.md`（深度契约，人工编辑）
- `CLAUDE.md` / `AGENTS.md`（本文件，重大改动需用户同意）

---

## 六、审计

| 脚本 | 检查啥 | 何时跑 |
|---|---|---|
| `scripts/check_pending.py` | 哪些 raw 还没 summary | 每次 session 开始（§一 触发） |
| `scripts/audit.py` | 结构性：summary source resolve、entity 重名、wikilink 死链 | ingest 后、想确认 vault 健康时 |

---

## 七、规则索引

| 文件 | 内容 |
|---|---|
| **`README.md`** | **Master 手册**——架构、机制、工作流、踩坑详解 |
| `system_instructions.md` | 深度契约：frontmatter 规范、ingest 流程细节、edge case |
| `02_Wiki/_canonical-names.md` | 错别字 / 多名同实勘误表（enrich 前必读）|
| `docs/specs/` | 各升级的设计文档 |

---

> **元规则**：本文件 / `AGENTS.md` / `system_instructions.md` 都是 `README.md` 的子集。冲突时以 `README.md` 为准。
