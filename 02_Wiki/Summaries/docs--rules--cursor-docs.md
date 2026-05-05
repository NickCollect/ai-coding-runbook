---
type: summary
source: 01_Raw/docs.cursor.com/docs--rules.md
source_url: https://cursor.com/docs/rules
title: "Rules（规则系统）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Rules 为 Agent 提供系统级持久化指令，解决 LLM 无法跨对话保留记忆的问题，内容在每次 model context 开头注入。

**四种规则类型**：
- **Project Rules**：存放在 `.cursor/rules/`，随代码库版本控制，支持路径模式/描述/手动触发
- **User Rules**：全局设置，跨所有项目生效，仅用于 Agent Chat
- **Team Rules**：Teams/Enterprise 专属，管理员从 dashboard 统一管理，可强制执行
- **AGENTS.md**：根目录或子目录的 markdown 文件，无需 frontmatter 的简单替代方案，支持嵌套

**规则触发方式**（通过 frontmatter 控制）：
- `alwaysApply: true` → 每次会话都包含
- `globs` 有值（`alwaysApply: false`）→ 匹配文件在上下文时自动附加
- `description` 有值、无 globs → Agent 根据相关性决定是否包含
- 无 description 无 globs → 仅 `@` 提及时手动引入

**创建方式**：chat 中输入 `/create-rule`，或 Cursor Settings > Rules > + Add Rule；也可从 GitHub 仓库导入远程规则。

**优先级**：Team Rules > Project Rules > User Rules（后者可被前者覆盖）。

**最佳实践**：规则保持 500 行内；具体可操作，避免泛泛而谈；重复提示才添加规则；引用文件而非复制内容；提交到 git 供团队共享。
