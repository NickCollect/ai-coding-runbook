---
type: summary
source: 01_Raw/docs.cursor.com/docs--agent--agent-review.md
source_url: https://cursor.com/docs/agent/agent-review
title: "Agent Review（本地代码审查）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Agent Review 对 Cursor 内的本地变更运行专项代码审查，可读取 `BUGBOT.md` 仓库规则文件。

**触发方式**：自动模式（每次 commit 后自动运行，需在设置中启用）、Slash 命令（chat 输入 `/agent-review`）、Source Control 标签页（审查所有本地改动与 main 分支的完整差异）。

**审查深度**：
- **Quick（快速）**：速度快、成本低，适合小 diff、格式变更或快速健全检查
- **Deep（深度）**：速度慢、成本高，适合复杂逻辑、安全敏感代码或大规模重构

**配置**：Cursor Settings > Agents > Agent Review。
