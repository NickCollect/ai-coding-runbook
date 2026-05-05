# AI Coding Runbook · 项目手册（Master Guide）

> **写给任何 LLM 和未来失忆的人**——下次任何 LLM 或人打开这个项目却不知它怎么工作时，**先读这一份**。
> 项目所有规则、踩过的坑、维护方法都在这里。`CLAUDE.md` / `AGENTS.md` / `system_instructions.md` 都是这份的子集 / 引用。

---

## 一、这个项目是干啥的

**一句话**：把 Anthropic、OpenAI、Google、Cursor 等主流 AI 工具的官方文档自动抓回来，由 LLM 加工成一个**可查询 + 自带 cheatsheet**的多厂商知识库。

**覆盖来源**：
- **Anthropic / Claude**：docs.claude.com、anthropic.com blog/research、anthropics + modelcontextprotocol GitHub repos
- **OpenAI / Codex**：docs.openai.com、openai/codex GitHub repo、openai/model_spec
- **Google Gemini**：ai.google.dev Gemini API 文档
- **Cursor IDE**：cursor.com/docs（llms.txt 全量）

**核心 use case**：
1. 问"Claude Code / Cursor / Codex 怎么选 / hooks 怎么配置 / extended thinking 怎么用" → LLM 直接读 enriched entity 答（不用现场 google）
2. 哪家这周改了什么 → 看 `03_Output/Changelog/<latest>.md`（GHA 自动生成）
3. 想看常用配置速查 → `03_Output/Cheatsheets/` 直接拿
4. 加新 raw（GHA cron 每周一自动跑）→ session 开始时看到 "📋 待 ingest: N 个文件" → 用户授权后 LLM 处理

**目标用户**：任何接手这个 KB 的 LLM（Claude Code / Codex / Cursor / 其他）或人类维护者。

---

## 二、三层架构

```
┌────────────────────────────────────────────────────────────────┐
│  互联网（Anthropic / OpenAI / Google / Cursor 官方文档 + GitHub）│
│       ↓ GHA cron 每周一 09:00 HKT 自动抓                        │
│       ↓ crawler: scripts/refresh_raw.py                         │
└────────────────────────────────────────────────────────────────┘
                          ↓
┌────────────────────────────────────────────────────────────────┐
│  ai-coding-runbook/                 ← 这个项目                  │
│  ├── 01_Raw/                ← 真理之源（read-only）             │
│  │   ├── docs.claude.com/   Anthropic 官方文档                  │
│  │   ├── anthropic.com/{news,research,engineering}              │
│  │   ├── docs.openai.com/   OpenAI 平台文档                     │
│  │   ├── docs.cursor.com/   Cursor IDE 文档（llms.txt 全量）    │
│  │   ├── ai.google.dev/     Gemini API 文档                     │
│  │   ├── github/anthropics/<repo>/    （shallow clone）         │
│  │   ├── github/modelcontextprotocol/<repo>/                    │
│  │   ├── github/openai/{codex,model_spec}/                      │
│  │   └── _meta/last_crawl.json                                  │
│  │                                                               │
│  ├── 02_Wiki/               ← LLM 加工区                        │
│  │   ├── Entities/          具体 feature/tool 档案              │
│  │   │   （Skills, Hooks, MCP-server, Subagents, ...）          │
│  │   ├── Concepts/          抽象概念                            │
│  │   │   （context-window, agentic-loop, prompt-caching, ...） │
│  │   ├── Summaries/         每份 raw 的 1:1 摘要               │
│  │   ├── Synthesis/         跨多 entity 的综述                  │
│  │   ├── Comparison/        decision matrix                     │
│  │   ├── QA/                问答沉淀                            │
│  │   ├── _canonical-names.md  错别字 / 多名同实勘误             │
│  │   ├── _audit_report--YYYYMMDD.md  最新 audit 结果            │
│  │   └── _progress.log      历次 ingest 操作日志                │
│  │                                                               │
│  ├── 03_Output/             ← 对外 + 监控                       │
│  │   ├── Cheatsheets/       日常速查（手维护，模板生成）        │
│  │   ├── Changelog/         GHA 每次 refresh 自动写             │
│  │   ├── My-Setup/          维护者的 plugin/skill 配置笔记      │
│  │   └── templates/         （将来加）cheatsheet 模板           │
│  │                                                               │
│  ├── scripts/               ← 自动化                            │
│  │   ├── sources.yaml       源清单（用户/LLM 改这里加减源）     │
│  │   ├── refresh_raw.py     crawler                             │
│  │   ├── check_pending.py   找未 summary 的 raw                 │
│  │   ├── audit.py           结构性 audit                        │
│  │   └── requirements.txt                                       │
│  │                                                               │
│  ├── .github/workflows/                                          │
│  │   └── refresh-raw.yml    GHA cron（每周一 01:00 UTC）        │
│  │                                                               │
│  ├── docs/specs/            升级设计文档                        │
│  ├── CLAUDE.md              Claude Code session 启动钩子        │
│  ├── AGENTS.md → CLAUDE.md  symlink，给 Codex 等                │
│  ├── system_instructions.md 深度契约                            │
│  └── README.md              本文件                              │
└────────────────────────────────────────────────────────────────┘
```

---

## 三、快速上手

> 三种最常见用法，按"配置成本"从低到高排。

### 用法 1：当查阅文档（0 配置）

```bash
git clone https://github.com/NickCollect/ai-coding-runbook
cd ai-coding-runbook
```

然后用 Obsidian / VSCode / 任何 markdown 编辑器打开：

- **看速查表** → `03_Output/Cheatsheets/*.md`（hook recipes、API 速查、模型定价等）
- **看横向对比** → `02_Wiki/Comparison/*.md`（Claude / Cursor / Codex 决策表等）
- **查具体 feature** → `02_Wiki/Entities/<feature>.md`
- **看每周变化** → `03_Output/Changelog/<latest>.md`

`.obsidianignore` 已经排除大目录，Obsidian 打开不卡。

### 用法 2：给 AI agent 当 long-term context（最推荐，0 配置）

clone 后用 **Claude Code / Cursor / Codex CLI** 打开这个文件夹：

- session 启动自动加载 `CLAUDE.md` / `AGENTS.md`，agent 知道项目结构和工作规则
- 直接问问题，agent 读 `02_Wiki/` 答。例子：
  - "Hooks 怎么配？给个 PreToolUse recipe"
  - "Skill vs MCP vs Subagent 该用哪个？"
  - "Anthropic / OpenAI 这周改了啥？"
  - "Codex CLI 和 Claude Code 怎么对比"

不需要额外 API key —— agent 用你自己的订阅 / token。

### 用法 3：fork 后跟自己的源（要 fork）

如果要：

- 加公司内部 / 团队文档源、删不需要的源
- 跑自己的 GHA cron（每周一自动刷 raw）
- 改 enrichment 流程

→ fork 这个 repo 到你的 GitHub 账号。GHA workflow 用默认 `GITHUB_TOKEN` 权限够用，不需要额外 secret。改源清单：编辑 `scripts/sources.yaml`，下次 cron 自动覆盖。

```bash
# 本地手动刷新一次（调试用）
pip install -r scripts/requirements.txt
python3 scripts/refresh_raw.py --all      # ~10 分钟
```

---

## 四、核心机制

### 机制 1 · GHA cron 自动抓 raw（matrix 并行）

`.github/workflows/refresh-raw.yml` 每周一 01:00 UTC（= 09:00 HKT）自动跑。**6 个 source 并行**（GHA matrix），每个 source 独立 commit + push（`git pull --rebase` + 重试 5 次防并发冲突）。

```
matrix sources (parallel):
  - code.claude.com           → 124 docs   (~2 min with concurrency=5)
  - platform.claude.com       → 1275 docs  (~7 min)
  - anthropic.com             → 345 docs   (~2 min, no .md probe)
  - support.claude.com        → 347 docs   (~2 min)
  - github.anthropics         → 12 repos   (~3 min)
  - github.modelcontextprotocol → 6 repos  (~2 min)
```

每个 source 内：`ThreadPoolExecutor(5)` 并发 HTTP fetch + 自动 retry（429/5xx backoff）。Wall time ≈ max(单 source) ≈ **~10 分钟**。

**aggregator job**（matrix 全跑完后跑一次）：扫最近 2h 内 bot commits → 写 `03_Output/Changelog/YYYY-MM-DD.md`。

**`fail-fast: false`** —— 一个 source 挂了，其他继续，已抓的内容已 commit 不丢。

**人工触发**：GitHub repo Actions 页面点 "Run workflow"，或本地 `gh workflow run refresh-raw`。

**本地刷新**（调试）：
```bash
python3 scripts/refresh_raw.py --list                       # 列所有 source 名
python3 scripts/refresh_raw.py --source code.claude.com     # 单 source
python3 scripts/refresh_raw.py --source github.anthropics
python3 scripts/refresh_raw.py --all                        # 全部 sequential
python3 scripts/refresh_raw.py --source X --dry-run
```

GitHub repos 抓回来后会**剥离 `.git/`**（避免被父 repo 当成 submodule）。代价：失去原 repo 的 git history；好处：repo 内文件正常被 wiki repo 跟踪。每周完整 re-clone（小，3 分钟）。

### 机制 2 · Enrichment 飞轮（"煮过的菜"独立存在）

02_Wiki 里的 entity / concept / summary 是 LLM 从 raw 提炼后**写到这些文件里**的，**已经独立存在**。

**飞轮的核心意义**：LLM 答问题时**不需要每次重读 raw**——直接读 enriched entity 就够。这是查询速度快 + 准确度高的根本原因。

**为啥不自动 enrich**：抓到 raw diff 后，GHA **不自动调 LLM** 写 summary，只生成 changelog 通知。原因：
1. LLM enrich 容易幻觉，需要 self-review
2. 加什么 entity / concept 是设计决定，不是流水线
3. 用户在 Claude Code session 里看到 changelog，决定哪些 diff 值得 enrich、哪些 skip

### 机制 3 · 模板驱动的活文件（将来）

将来：定期 prep / report 类的活模板生成。当前 03_Output/templates 是空的，等 cheatsheet 数量够多后再加自动模板。

### 机制 4 · 结构性 audit

`scripts/audit.py` 检查 02_Wiki 的内部一致性：

- Summary 是否有 frontmatter `source:` 指向真 raw
- Entity / Concept 是否有 frontmatter + 至少一个 section
- Wikilink `[[X]]` 是否指向真文件
- Entity / Concept 名字是否重复

跑完写 `02_Wiki/_audit_report--YYYYMMDD.md`。

### 机制 5 · canonical-names 错别字 / 多名同实治理

`02_Wiki/_canonical-names.md` 是**单一事实源** —— 记录所有 raw 里出现但 vault 用 canonical 名的映射。

例：
- `Sub-agent` / `Subagent` / `Sub agent` → canonical: `Subagent`
- `Tool use` / `Function calling` → canonical: `Tool use`
- `Slash commands` / `Slash Commands` / `slash-commands` → canonical: `Slash commands`

**LLM 必读规则**：
1. enrich 前 `cat 02_Wiki/_canonical-names.md`
2. 引用未知名字前在 `02_Wiki/Entities/*.md` 的 frontmatter `aliases` 里 grep 一遍
3. 不要凭脑补造 entity 名

---

## 五、日常工作流

### 用户做的（不用 LLM）

| 场景 | 做啥 |
|---|---|
| 想知道 Anthropic 这周改了啥 | 打开 `03_Output/Changelog/<最新日期>.md` |
| 查某个 feature 速查 | `03_Output/Cheatsheets/<topic>.md` |
| 拉远程更新（GHA cron 跑完后）| `cd <repo目录> && git pull` |
| 加新源 | 编辑 `scripts/sources.yaml`，commit push，下次 cron 自动覆盖 |

### 用户请 LLM 做的

| 场景 | 用户说 | LLM 做啥 |
|---|---|---|
| 新 raw 想入库 | **不用开口**——session 开始自动看到 "📋 待 ingest"。说 "ingest" / "ingest 1,3" / "skip" | Phase A→E（详见 § 五 ingest） |
| 查任何 Claude Code / API 问题 | 直接问 | 读 enriched entity 答，缺信息回 raw 找 |
| 写新 cheatsheet | "写一份 hooks 速查" / "做一份 Skill vs MCP 对比表" | 跨多 entity 综合 → 写到 `03_Output/Cheatsheets/` |
| 加新源 | "加上 modelcontextprotocol/inspector repo" | 改 sources.yaml + commit + 跑一次 refresh 测试 |
| 跑 audit | "跑一次 audit" | `python3 scripts/audit.py` |
| 修错别字 | "Anthropic 文档把 X 写成 Y，但 vault 应该用 Y" | 改 canonical-names + 批量替换 + 重跑 audit |

### LLM 工作时的 Phase A→E（ingest）

按 user 授权后：

| Phase | 做啥 | self-review |
|---|---|---|
| **A · Summary 创建** | 对每个 pending raw 写 summary 到 `02_Wiki/Summaries/` | frontmatter 合规、source 字段指向真 raw、无同名碰撞 |
| **B · 已有 entity / concept 更新** | 在 `## 出现来源` 追加；新事实进 `## 关键属性` | **不创建新文件**；wikilink 都真存在；事实有原文支撑 |
| **C · 新名字处理** | 列候选给用户，用户选 → 建 stub | 用户授权后才建 |
| **D · Audit** | `python3 scripts/audit.py` | 列修复建议但不自动修 |
| **E · 日志** | append `02_Wiki/_progress.log` | — |

每 Phase self-review **是为了防上一阶段幻觉污染下一阶段**。

---

## 六、🚨 踩过的坑 / Lessons Learned

### #1 · 永远不改 01_Raw

raw 是 GHA bot 的输出。手动改 raw 会：
- 下次 cron 跑发现 diff 又改回去（拉锯）
- 污染 git diff 信号
- 误导 enrichment（以为 Anthropic 改了什么）

要"修正"的内容（比如 Anthropic 文档错别字、过时引用）→ 写到 `02_Wiki/_canonical-names.md` 走勘误机制。

### #2 · 模型权重 vs Raw 文档冲突时以 Raw 为准

Anthropic 改 API / 加 feature 频繁，Claude 模型权重训练截止日期之后的所有变化只在 raw 里。LLM 答问题时如果 raw 有，必须以 raw 为准；raw 没的才能用模型知识（并明确标注"基于训练知识，未在最新 docs 验证"）。

### #3 · "记得 Claude Code 有这个 feature" 不算证据

任何 entity / concept 的事实必须能 trace 回某份 raw 文件。写 `Hooks 支持 X` 之前要 grep `01_Raw/` 找到原文。找不到的写 `（待验证）` 或不写。

### #4 · 同一概念的多个名字

Anthropic 文档自己就不统一：`Sub-agent` / `Subagent` / `subagent`、`Tool use` / `Function calling`、`Slash commands` / `slash-commands`。统一靠 `_canonical-names.md`。Vault 内部用 canonical 名，aliases 写在 entity frontmatter 里。

### #5 · Wikilink 必须先 ls

`[[Hooks]]` 之前 `ls 02_Wiki/Entities/Hooks.md`。不存在的别写，会变死链。Audit 会抓但写时就该避免。

### #6 · Subagent finding 不直接 trust

调用 subagent 调研某 topic 后，master 阶段必须 sample re-verify（≥3 + 全部 MAJOR claim）。Subagent 容易幻觉，尤其在调研当前还没 enrich 的领域。

### #7 · GHA 推 main 没问题，但要小心 sources.yaml 改坏

GHA workflow 没有 PR review，改 sources.yaml 加坏 prefix 会导致下次 cron 抓回 0 个文件 / 错的文件。改前最好本地 `python3 scripts/refresh_raw.py --dry-run --only <kind>` 验一遍。

### #8 · 多机器同步

通过 git 同步，不依赖 iCloud。**不要在脚本里 hardcode 绝对路径**——用 `~`、`$HOME` 或 project-relative path（`Path(__file__).resolve().parent.parent`），确保在不同机器上都能运行。

---

## 七、源清单

详见 `scripts/sources.yaml`。当前 5 大类：

1. `docs.claude.com` 整站（按 section 抓）—— Claude Code、API、模型、prompt 工程、release notes、legal
2. `support.anthropic.com` —— Claude.ai 产品文档
3. `anthropic.com/{news,research,engineering}` —— blog
4. `anthropics/*` GitHub repos × 15 —— claude-code、agent SDK、cookbook、quickstarts、courses、skills、evals 等
5. `modelcontextprotocol/*` GitHub repos × 5 —— MCP spec、SDK、reference servers

加 / 减源：编辑 `scripts/sources.yaml`，commit。下次 cron 跑自动覆盖。

---

## 八、维护

### 长期日常（你做）
- 每周一 GHA 跑完后 `git pull`
- 看 `03_Output/Changelog/<latest>.md` 决定要不要 ingest
- 想 ingest → Claude Code session 里说 "ingest"

### 长期日常（GHA 自动做）
- 每周一 09:00 HKT 抓 raw
- diff 检测 + commit + push
- 写 changelog
- 失败时 GitHub 邮件告警

### 想加 / 改 source
1. 编辑 `scripts/sources.yaml`
2. 本地 `python3 scripts/refresh_raw.py --dry-run --only <kind>` 验证
3. commit + push
4. 等下次 cron，或手动 `gh workflow run refresh-raw`

### 想改 crawler 行为
1. 改 `scripts/refresh_raw.py`
2. 本地 `python3 scripts/refresh_raw.py --dry-run` 验证
3. commit + push
4. 下次 cron 用新版

---

## 九、术语

- **raw**：`01_Raw/` 下的文件，GHA bot 抓来的 markdown / git clone 的 repo
- **summary**：`02_Wiki/Summaries/` 下，每份 raw 的 1:1 摘要
- **entity**：`02_Wiki/Entities/` 下，具体的 feature / tool / model 档案（聚合多 raw）
- **concept**：`02_Wiki/Concepts/` 下，抽象概念
- **synthesis**：`02_Wiki/Synthesis/` 下，跨多 entity 的综述
- **comparison**：`02_Wiki/Comparison/` 下，decision matrix / 横向对比
- **cheatsheet**：`03_Output/Cheatsheets/` 下，对外日常速查
- **changelog**：`03_Output/Changelog/` 下，GHA 自动写的 raw 变化记录
- **canonical name**：vault 内部用的统一名字（vs raw 里出现的多个变体）
- **stub**：含 `<!-- stub: awaiting enrichment -->` 标记的占位 entity / concept

---

## 十、相关文档

| 文档 | 用途 |
|---|---|
| `CLAUDE.md` | Claude Code session 启动钩子 + 关键规则速查 |
| `AGENTS.md` | symlink → CLAUDE.md，给 Codex 等其他 agent |
| `system_instructions.md` | 深度契约 §0-§7：frontmatter 规范 / 入库规则 / ingest 流程 / edge case |
| `scripts/sources.yaml` | 源清单（YAML） |
| `02_Wiki/_canonical-names.md` | 错别字 / 多名同实勘误（enrich 前必读） |
| `docs/specs/` | 各升级 brainstorm 沉淀 |

---

> **元规则**：本文件是 master 综合手册。`CLAUDE.md` / `AGENTS.md` / `system_instructions.md` 都是这份的子集 / 引用。**冲突时以 README.md 为准**。
