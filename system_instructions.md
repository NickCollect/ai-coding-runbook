# AI Coding Runbook — System Instructions（深度契约）

> 这是机器规则，比 `CLAUDE.md` 更细。CLAUDE.md 是 hook，本文件是 contract。
> 所有 LLM 在 ingest / enrichment / output 生成时必须遵守。
>
> **知识库范围**：Anthropic（Claude / Claude Code / MCP）· OpenAI（API / Codex CLI）· Google（Gemini API）· Cursor IDE。
> **GitHub**：`NickCollect/ai-coding-runbook`（本地文件夹名可能改变，以 remote URL 为准）。

---

## §0 · 顶层原则

1. **Raw 是唯一真理之源**：02_Wiki / 03_Output 里的任何事实必须能 trace 回 01_Raw 某个文件。
2. **加工产物可独立使用**：02_Wiki/Entities 里的档案应自洽（不需要每次重读 raw 就能答问题），但每条事实都附 `[[Summary-X]]` 指向支撑 summary。
3. **没有"我记得"**：模型权重里关于任何工具（Claude / Codex / Cursor / Gemini）的知识 vs raw 文档冲突时，以 raw 为准（各厂商改产品快，权重过期）。
4. **Hallucination 是最大罪**：宁愿写 "（本份 raw 无相关信息）" 也不要编。

---

## §1 · Frontmatter 规范

### Summary（02_Wiki/Summaries/*.md）

```yaml
---
type: summary
source: 01_Raw/docs.claude.com/en/docs/claude-code/hooks.md  # 必填，相对路径
source_url: https://docs.claude.com/en/docs/claude-code/hooks  # 选填，原 URL
title: "Claude Code Hooks"
crawled_at: 2026-05-04T...                                    # 从 raw frontmatter 拷
summarized_at: 2026-05-04                                     # ingest 当天
entities_referenced: [Hooks, SessionStart, PreToolUse]        # 提到的 entity name
concepts_referenced: [agentic-loop]
---
```

### Entity（02_Wiki/Entities/*.md）

```yaml
---
type: entity
name: Hooks
aliases: [hook, hook system, session hooks]
category: feature                  # feature / tool / sdk / model / concept-adjacent
first_introduced: 2024-XX-XX       # 选填
status: ga | beta | deprecated
---
```

Entity body 必须有这些 section（缺哪个 audit 报警）：
- `## 一句话定义`
- `## 关键属性`（事实集合，每条配 wikilink 到支撑 summary）
- `## 出现来源`（list of `[[Summary-X]]`）
- `## 相关`（其他 entity / concept 的 wikilink）

### Concept（02_Wiki/Concepts/*.md）

跟 Entity 同 schema，区别：Entity 是"具体的命名实体"（Hooks、Skills、Opus 4.7 model），Concept 是"抽象概念"（agentic loop、prompt caching、context window）。

### Cheatsheet（03_Output/Cheatsheets/*.md）

```yaml
---
type: cheatsheet
topic: claude-code-keybindings
last_updated: 2026-05-04
based_on:                                # list of source raw paths
  - 01_Raw/docs.claude.com/en/docs/claude-code/keybindings.md
  - 01_Raw/github/anthropics/claude-code/README.md
---
```

---

## §2 · Sub-directory 入库规则

### 2.1 Summaries

- 文件名 = raw 文件 stem（保持映射关系，audit 用得上）
- 一份 raw → 一份 summary（1:1，不要合并多 raw 进一个 summary）
- 长度：raw 短（< 500 字）摘要 100–200 字；raw 长（> 5000 字）摘要 400–800 字 + 结构化要点
- **不要照抄 raw**：抽要点 + 名词 + 关键代码片段。原文细节去读 raw。

### 2.2 Entities / Concepts

- **Entity 是聚合 view**：跨多份 raw 的同一概念合并到一个文件
- 例：`Hooks.md` 聚合 `docs.claude.com/.../hooks.md` + `github/anthropics/claude-code/README.md` 提到 hooks 的部分 + `anthropic-cookbook` 里 hooks 例子
- 新事实进入 Entity 必须：
  1. 在某 summary 里能找到原文
  2. 在 Entity 的 `## 关键属性` 加一行 + `[[Summary-X]]`
  3. 在 Entity 的 `## 出现来源` 加 `[[Summary-X]]`（如果还没列）
- **不要合并不同实体**：Skills 和 Subagents 是两个 entity，不要因为都"扩展 Claude Code"就合并

### 2.3 Synthesis / Comparison

- Synthesis：跨多 entity 的综述（比如 "Claude Code 的扩展性全景：Plugins / Skills / MCP / Subagents / Hooks"）
- Comparison：横向对比 / decision matrix（比如 "Skills vs MCP vs Subagents：什么时候用哪个"）
- 这两类**不必 1:1 对应 raw**，但每个 claim 还是要能 trace 回 entity / summary

---

## §3 · 多机器兼容

此 repo（`NickCollect/ai-coding-runbook`）通过 git 同步：
- `git pull` 拿改动
- **本地文件夹名可能改变**，以 remote URL 为准：`https://github.com/NickCollect/ai-coding-runbook`
- 任何脚本 / 配置不要 hardcode 绝对路径或用户名，用 `~`、`$HOME`、project-relative path
- 用 `~`、`$HOME`、project-relative path（`Path(__file__).resolve().parent.parent`）
- Symlink 用相对路径（如果将来需要）

---

## §4 · Ingest 标准流程（详细版）

### Phase A · Summary 创建

```
1. for each raw file in pending list:
2.     读 raw 头几百行 + 末几百行
3.     提取 frontmatter 里的 source_url / title / fetched_at
4.     写 summary 到 02_Wiki/Summaries/<raw_stem>.md
5.     summary frontmatter 的 source 字段填 01_Raw/<relative_path_to_raw>
6. self-review:
   - ls 02_Wiki/Summaries/ 看是否有同名碰撞
   - cat 几个 random summary 验证 frontmatter 合规
   - grep "source:" 02_Wiki/Summaries/*.md | wc -l == pending count
```

### Phase B · 已有 entity / concept 更新

```
1. for each new summary:
2.     提取 entities_referenced / concepts_referenced
3.     for each referenced entity name:
4.         如果 02_Wiki/Entities/<name>.md 已存在:
5.             在 ## 出现来源 追加 [[summary stem]]
6.             如果 summary 提到该 entity 的新事实 → 在 ## 关键属性 加一行
7.         如果不存在 → 加入 "C 阶段候选名单"（不在本阶段创建）
8. self-review:
   - 跑 grep '\[\[' 02_Wiki/Entities/*.md 看 wikilink 都指向真文件
   - 抽查 5 条新加事实，确认能在对应 summary 里找到原文
```

### Phase C · 新名字处理（必须问用户）

```
1. 列出本次新出现的 entity / concept 候选（B 阶段攒的）
2. 给用户清单：
   "本次发现 N 个新名字候选：
    1. Skill marketplace (新 entity?)
    2. agentic context engineering (新 concept?)
    ...
    选择处理：'create all' / 'create 1,3' / 'skip all' / 'rename 2 to X'"
3. 用户授权后，建 stub：
   - frontmatter 完整
   - body 只有: <!-- stub: awaiting enrichment -->
   - ## 出现来源 列已知的 summary
4. self-review: ls 新建的 stub 都在对的目录
```

### Phase D · Audit

```
python3 scripts/audit.py
```

输出列出问题 + 修复建议。**不自动修**——告诉用户哪里有问题，等用户决定。

### Phase E · 日志

```
echo "[$(date +%Y-%m-%d\ %H:%M)] INGEST - <N> summaries, <M> entity updates, <K> new stubs" >> 02_Wiki/_progress.log
```

---

## §5 · 不该做的事

1. **不自动 enrich**：GHA 抓到 raw diff 后只生成 changelog 通知，绝不自动调 LLM 写 summary。Enrichment 永远 user-triggered。
2. **不改模板 / 脚本**：`scripts/*` 和 `03_Output/templates/*` 由用户演化，不主动改。
3. **不"清理"raw**：raw 是 ground truth，再难看也不动。要修改请走 canonical-names 走勘误。
4. **不夸大确定性**：写 entity 时 "Skills 支持 X" vs "Skills 文档说 X"，后者更诚实。raw 没明说的不要替它说。
5. **不批量删除 stub**：stub 是设计预期（`<!-- stub: awaiting enrichment -->`），等被 enrich，不是 bug。

---

## §6 · 紧急 / 异常

- **GHA crawler 挂了** → 看 GitHub Actions 页面 log → 修 `scripts/refresh_raw.py` 或 `scripts/sources.yaml`
- **某 doc URL 改了** → crawler 报 404 → 在 sources.yaml 加 redirect / 改 prefix
- **Audit 大批量 FAIL** → 优先看 wikilink 死链（最常见，通常 entity 改名导致）
- **Vault 自相矛盾**（不同 summary 描述同一 entity 的 X 属性不一致）→ 列到 `02_Wiki/_accuracy_suspects.md` 让用户决定哪个对

---

## §7 · 演化

本文件由用户编辑。LLM 想修改 → 在对话里提议 → 用户决定。

主要演化触发：
- 加新源类型（不是 docs / github / blog）
- 加新 02_Wiki 子目录类型
- 加新 03_Output 自动化模板
