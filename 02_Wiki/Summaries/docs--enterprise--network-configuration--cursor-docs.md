---
type: summary
source: 01_Raw/docs.cursor.com/docs--enterprise--network-configuration.md
source_url: https://cursor.com/docs/enterprise/network-configuration
title: "Enterprise 网络配置"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

企业网络配置指南，涵盖代理、防火墙和加密要求，帮助 Cursor 在复杂企业网络中正常运行。

**代理配置**：Cursor 默认使用 HTTP/2 双向流；代理不支持 HTTP/2 时自动回退到 HTTP/1.1 SSE 模式（对 Zscaler 等有效）。SSL 拦截（中间人/DLP）是最常见的企业部署障碍，建议对 `.cursor.sh`/`cursor-cdn.com`/`marketplace.cursorapi.com` 等域名禁用 SSL 检查；若必须检查则代理需支持 HTTP/2 双向流或 SSE passthrough（不缓冲）。

**连通性测试**：`curl -v https://api2.cursor.sh |& grep -C1 issuer:` 检查 SSL 证书（应为 Amazon RSA，看到代理商则说明 SSL 检查激活）；另有 HTTP/1.1 流和 HTTP/2 双向流的 curl 测试命令。

**IP 白名单**：推荐用域名模式而非 IP（IP 可变）：`*.cursor.sh`/`*.cursor-cdn.com`/`*.cursorapi.com`。

**加密**：传输中 TLS 1.2+，静态 AES-256，向量数据库和 Cloud Agent 代码存储均加密；支持 CMEK（企业客户管理加密密钥）。

**LLM 网关**：不推荐自定义 LLM 网关（引入延迟和兼容问题），建议用 Hooks 实现安全控制；BYOK 模式下 ZDR 政策不适用。

**Cloud Agents 网络**：在 Cursor 基础设施上运行，可访问公开 GitHub/GitLab/npm/PyPI 等，无法访问企业防火墙后的内部资源。
