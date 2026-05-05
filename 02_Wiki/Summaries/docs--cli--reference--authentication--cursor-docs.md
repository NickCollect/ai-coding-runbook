---
type: summary
source: 01_Raw/docs.cursor.com/docs--cli--reference--authentication.md
source_url: https://cursor.com/docs/cli/reference/authentication
title: "CLI 认证参考"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cursor CLI 支持两种认证方式：浏览器登录（推荐）和 API Key。

**浏览器认证**：`agent login`（打开浏览器认证，凭证本地安全存储）；`agent status`（查看认证状态）；`agent logout`（登出并清除凭证）。

**API Key 认证**（适合自动化/CI/CD）：从 Dashboard → Integrations → API Keys 生成；通过 `CURSOR_API_KEY` 环境变量或 `--api-key` flag 传入。

**常见问题**：未认证错误→运行 `agent login` 或设置 API Key；SSL 证书错误→开发环境用 `--insecure` flag；端点问题→用 `--endpoint` 指定自定义 API 端点。
