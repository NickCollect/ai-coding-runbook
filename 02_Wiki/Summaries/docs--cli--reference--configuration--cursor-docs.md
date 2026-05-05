---
type: summary
source: 01_Raw/docs.cursor.com/docs--cli--reference--configuration.md
source_url: https://cursor.com/docs/cli/reference/configuration
title: "CLI 配置文件参考"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cursor CLI 通过 `~/.cursor/cli-config.json`（全局）或 `<project>/.cursor/cli.json`（项目级，仅权限）进行配置。

**必填字段**：`version`（当前为 1）、`editor.vimMode`（Vim 键位）、`permissions.allow`/`permissions.deny`（权限列表）。

**可选字段**：`model`（模型选择）、`network.useHttp1ForAgent`（HTTP/1.1 回退，适合 Zscaler 等企业代理）、`attribution.attributeCommitsToAgent`（Commit 中添加 "Made with Cursor" 标注，默认 true）。

**代理配置**：设置 `HTTP_PROXY`/`HTTPS_PROXY`/`NODE_USE_ENV_PROXY=1` 环境变量；SSL 拦截（中间人）还需 `NODE_EXTRA_CA_CERTS=/path/to/ca.pem`；企业代理需在 config 中设 `network.useHttp1ForAgent: true`（HTTP/2 改 SSE）。

**模型选择**：通过 `/model <id>` slash 命令选择（如 `/model auto`、`/model gpt-5.2`），设置后保存在 config 文件。

**注意**：纯 JSON（无注释）；字段缺失时自动修复；损坏的 config 备份为 `.bad` 后重建；部分字段由 CLI 自动管理（可能被覆盖）。
