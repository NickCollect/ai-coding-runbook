# Ingest Workflow

> 用户 / LLM 协同把 raw 加工成 wiki 的 SOP。从"raw 文件出现"到"entity 更新"的完整路径。

---

## 一、用户做的（不用 LLM）

| 场景 | 做啥 |
|---|---|
| 想知道 Anthropic 这周改了啥 | 打开 `03_Output/Changelog/<最新日期>.md` |
| 查某个 feature 速查 | `03_Output/Cheatsheets/<topic>.md` |
| 拉远程更新（GHA cron 跑完后）| `cd <repo目录> && git pull` |
| 加新源 | 编辑 `scripts/sources.yaml`，commit push，下次 cron 自动覆盖 |

---

## 二、用户请 LLM 做的

| 场景 | 用户说 | LLM 做啥 |
|---|---|---|
| 新 raw 想入库 | **不用开口**——session 开始 LLM 自动看到 "📋 待 ingest"。说 "ingest" / "ingest 1,3" / "skip" | Phase A→E（详见 § 三） |
| 查任何 Claude Code / API 问题 | 直接问 | 读 enriched entity 答，缺信息回 raw 找 |
| 写新 cheatsheet | "写一份 hooks 速查" / "做一份 Skill vs MCP 对比表" | 跨多 entity 综合 → 写到 `03_Output/Cheatsheets/` |
| 加新源 | "加上 modelcontextprotocol/inspector repo" | 改 sources.yaml + commit + 跑一次 refresh 测试 |
| 跑 audit | "跑一次 audit" | `python3 scripts/audit.py` |
| 修错别字 | "Anthropic 文档把 X 写成 Y，但 vault 应该用 Y" | 改 canonical-names + 批量替换 + 重跑 audit |

---

## 三、Phase A → E（ingest 流程）

按 user 授权后：

| Phase | 做啥 | self-review checkpoint |
|---|---|---|
| **A · Summary 创建** | 对每个 pending raw 写 summary 到 `02_Wiki/Summaries/` | frontmatter 合规、`source:` 指向 `01_Raw/` 真路径、无同名碰撞 |
| **B · 已有 entity / concept 更新** | 在 `## 出现来源` 追加；新事实进 `## 关键属性` | **不创建新文件**；wikilink `[[X]]` 都真存在；事实有 raw 原文支撑（无幻觉）|
| **C · 新名字处理** | 列候选给用户，用户选 → 建 stub | 用户授权后才建 |
| **D · Audit** | `python3 scripts/audit.py` | 列修复建议但不自动修 |
| **E · 日志** | append `02_Wiki/_progress.log`：`[YYYY-MM-DD HH:MM] INGEST - <N> summaries / ...` | — |

**为啥每 Phase self-review**：防上一阶段幻觉污染下一阶段。Phase A 写错的 source 字段，Phase B 引用就会传播错；Phase B 漏 wikilink 死链，Phase D audit 才发现已经晚了——所以 self-review 要在每 Phase 内自闭环。

---

## 四、辅助脚本

| 脚本 | 检查啥 | 何时跑 |
|---|---|---|
| `scripts/check_pending.py` | 哪些 raw 还没 summary | 每次 session 开始（`CLAUDE.md` § 一 触发）|
| `scripts/audit.py` | 结构性：summary `source:` 能 resolve、entity 重名、wikilink 死链 | ingest 后、想确认 vault 健康时 |

---

## 相关文档

- [`../README.md`](../README.md) — 项目 landing page
- [`./ARCHITECTURE.md`](./ARCHITECTURE.md) — 架构 + 5 个核心机制（含 enrichment 飞轮）
- [`./MAINTENANCE.md`](./MAINTENANCE.md) — 维护者手册（踩过的坑 + ops）
- [`../system_instructions.md`](../system_instructions.md) — frontmatter 规范、深度契约 §0-§7
- [`../02_Wiki/_canonical-names.md`](../02_Wiki/_canonical-names.md) — enrich 前必读的勘误表
