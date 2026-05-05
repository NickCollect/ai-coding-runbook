---
type: summary
source: 01_Raw/docs.cursor.com/docs--cli--github-actions.md
source_url: https://cursor.com/docs/cli/github-actions
title: "CLI 在 GitHub Actions 中的使用"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

在 GitHub Actions 和 CI/CD 系统中使用 Cursor CLI 自动化开发任务，以 CURSOR_API_KEY 环境变量认证。

**基础配置**：先安装 CLI，再设置 `CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}`，然后运行 `agent -p "prompt" --model gpt-5.2`。

**自主级别两种方式**：
- **完全自主**：Agent 完全控制 git、API 调用等所有操作，配置简单但需要更高信任
- **受限自主（推荐）**：限制 Agent 仅做文件修改，git 操作和 PR 评论由 CI 确定性步骤处理，可审计性强

**权限配置示例**（通过 permissions.json）：
```json
{
  "permissions": {
    "allow": ["Read(**/*.md)", "Write(docs/**/*)", "Shell(grep)"],
    "deny": ["Shell(git)", "Shell(gh)", "Write(.env*)"]
  }
}
```

**认证**：在 Cursor dashboard 生成 API Key，通过 `gh secret set CURSOR_API_KEY` 存入仓库或组织 Secret，在 workflow 的 `env` 中引用。
