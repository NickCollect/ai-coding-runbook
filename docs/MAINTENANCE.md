# Maintenance

> 给维护者（self-host 这份 wiki 的人 / fork 改造的人）看的手册。包括踩过的坑、长期维护节奏、术语表。

---

## 一、🚨 踩过的坑 / Lessons Learned

### #1 · 永远不改 `01_Raw/`

raw 是 GHA bot 的输出。手动改 raw 会：

- 下次 cron 跑发现 diff 又改回去（拉锯）
- 污染 git diff 信号
- 误导 enrichment（以为 Anthropic 改了什么）

要"修正"的内容（比如 Anthropic 文档错别字、过时引用）→ 写到 `02_Wiki/_canonical-names.md` 走勘误机制。

### #2 · 模型权重 vs raw 文档冲突时以 raw 为准

Anthropic 改 API / 加 feature 频繁，Claude 模型权重训练截止日期之后的所有变化只在 raw 里。LLM 答问题时如果 raw 有，必须以 raw 为准；raw 没的才能用模型知识（并明确标注"基于训练知识，未在最新 docs 验证"）。

### #3 · "记得 Claude Code 有这个 feature" 不算证据

任何 entity / concept 的事实必须能 trace 回某份 raw 文件。写 `Hooks 支持 X` 之前要 grep `01_Raw/` 找到原文。找不到的写 `（待验证）` 或不写。

### #4 · 同一概念的多个名字

Anthropic 文档自己就不统一：`Sub-agent` / `Subagent` / `subagent`、`Tool use` / `Function calling`、`Slash commands` / `slash-commands`。统一靠 `_canonical-names.md`。Vault 内部用 canonical 名，aliases 写在 entity frontmatter 里。

### #5 · Wikilink 必须先 ls

`[[Hooks]]` 之前 `ls 02_Wiki/Entities/Hooks.md`。不存在的别写，会变死链。Audit 会抓但写时就该避免。

### #6 · Subagent finding 不直接 trust

调用 subagent 调研某 topic 后，master 阶段必须 sample re-verify（≥3 + 全部 MAJOR claim）。Subagent 容易幻觉，尤其在调研当前还没 enrich 的领域。

### #7 · GHA 推 main 没问题，但要小心 `sources.yaml` 改坏

GHA workflow 没有 PR review，改 `sources.yaml` 加坏 prefix 会导致下次 cron 抓回 0 个文件 / 错的文件。改前最好本地 `python3 scripts/refresh_raw.py --dry-run --source <name>` 验一遍。

### #8 · 多机器同步

通过 git 同步，不依赖 iCloud。**不要在脚本里 hardcode 绝对路径**——用 `~`、`$HOME` 或 project-relative path（`Path(__file__).resolve().parent.parent`），确保在不同机器上都能运行。

---

## 二、长期维护节奏

### 用户做的

- 每周一 GHA 跑完后 `git pull`
- 看 `03_Output/Changelog/<latest>.md` 决定要不要 ingest
- 想 ingest → 在你的 agent session（Claude Code / Cursor / Codex 等）里说 "ingest"

### GHA 自动做的

- 每周一 09:00 HKT 抓 raw（matrix 9 个源并行）
- diff 检测 + commit + push（每个 source 独立 commit）
- 写 `03_Output/Changelog/<date>.md`（aggregator job）
- 失败时 GitHub 发邮件告警

### 想加 / 改 source

1. 编辑 `scripts/sources.yaml`
2. 本地 `python3 scripts/refresh_raw.py --dry-run --source <name>` 验证
3. 如果是新 source 要在 `.github/workflows/refresh-raw.yml` 的 matrix 里同步加
4. commit + push
5. 等下次 cron，或手动 `gh workflow run refresh-raw.yml`

### 想改 crawler 行为

1. 改 `scripts/refresh_raw.py`
2. 本地 `python3 scripts/refresh_raw.py --dry-run` 验证
3. commit + push
4. 下次 cron 用新版

---

## 三、术语表

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

## 相关文档

- [`../README.md`](../README.md) — 项目 landing page
- [`./ARCHITECTURE.md`](./ARCHITECTURE.md) — 架构 + 5 个核心机制
- [`./INGEST_WORKFLOW.md`](./INGEST_WORKFLOW.md) — LLM ingest Phase A→E SOP
- [`../CLAUDE.md`](../CLAUDE.md) — agent session 启动钩子（精简规则速查）
- [`../system_instructions.md`](../system_instructions.md) — frontmatter 规范、深度契约
