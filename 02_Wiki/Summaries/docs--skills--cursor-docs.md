---
type: summary
source: 01_Raw/docs.cursor.com/docs--skills.md
source_url: https://cursor.com/docs/skills
title: "Agent Skills"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Agent Skills 是可扩展 AI Agent 专项能力的开放标准，将领域知识和工作流打包为可版本控制、可复用的包，按需加载保持上下文高效。

**Skill 目录**（自动加载）：`.agents/skills/`、`.cursor/skills/`（项目级）；`~/.agents/skills/`、`~/.cursor/skills/`（用户全局）。兼容 Claude/Codex 的 `.claude/skills/`、`.codex/skills/` 目录。每个 Skill 是一个含 `SKILL.md` 的文件夹。

**SKILL.md frontmatter 字段**：
- `name`（必填）：小写字母+连字符的标识符，需与文件夹名一致
- `description`（必填）：Agent 据此判断何时调用
- `paths`（可选）：glob 模式，将 Skill 限定到匹配文件
- `disable-model-invocation`（可选）：`true` 时仅显式 `/skill-name` 才触发

**可选目录**：`scripts/`（可执行脚本）、`references/`（按需加载的详细文档）、`assets/`（模板/图片/数据文件）。

**触发方式**：Agent 根据上下文自动应用，或 chat 中输入 `/skill名称` 手动调用。

**安装**：可从 GitHub 仓库导入（Cursor Settings > Rules > Add Rule > Remote Rule (Github)）。

**迁移**：内置 `/migrate-to-skills` Skill（v2.4+）可将现有动态规则和 slash command 批量转换为 Skills。

兼容所有支持 Agent Skills 标准的 Agent（开放标准，详见 agentskills.io）。
