---
type: summary
source: 01_Raw/docs.cursor.com/docs--plugins.md
source_url: https://cursor.com/docs/plugins
title: "Plugins（插件系统）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Plugins 将 Rules、Skills、Agents、Commands、MCP Servers、Hooks 打包为可分发的捆绑包，可从 Cursor Marketplace（官方审核）或 cursor.directory（社区）获取，也可自行创建。

**插件可包含的组件**：Rules（AI 指引，.mdc 文件）、Skills（专项 Agent 能力）、Agents（自定义配置和提示）、Commands（可执行命令文件）、MCP Servers（外部工具集成）、Hooks（事件自动化脚本）。

**团队 Marketplace**：Teams 计划最多 1 个，Enterprise 无限制。管理员从 Dashboard → Settings → Plugins 导入 GitHub 仓库作为团队 Marketplace。可设置必须安装（Required，保存后自动为分组成员安装）或可选（Optional，成员自选安装）。

**创建插件**：目录包含 `.cursor-plugin/plugin.json` 清单文件，加上 rules/、skills/、agents/ 等目录；本地测试放 `~/.cursor/plugins/local/插件名`；就绪后提交至 cursor.com/marketplace/publish 等待审核。

**清单 plugin.json**：仅 `name` 字段必填，其余组件从默认目录自动发现；也可在清单中指定自定义路径。

**Extension API**：可用 `vscode.cursor.plugins.registerPath()` 以编程方式注册插件目录，适合 VS Code 扩展内捆绑分发或自动化部署。
