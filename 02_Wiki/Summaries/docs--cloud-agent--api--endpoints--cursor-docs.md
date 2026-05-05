---
type: summary
source: 01_Raw/docs.cursor.com/docs--cloud-agent--api--endpoints.md
source_url: https://cursor.com/docs/cloud-agent/api/endpoints
title: "Cloud Agents API v1"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cloud Agents REST API v1（公测版），通过 Basic Auth（用户 API Key 或 Service Account API Key）以编程方式创建和管理 Cloud Agent，端点基地址 `https://api.cursor.com`。

**核心资源模型**：Agent（持久容器，跨 Run 保持对话和工作区）+ Run（单次 prompt 执行，有独立状态）。

**Agent 端点**：
- `POST /v1/agents`：创建 Agent 并立即启动初始 Run（参数：prompt.text、model.id、repos[0].url、autoCreatePR 等）
- `GET /v1/agents`：分页列出 Agents（支持 prUrl 过滤）
- `GET /v1/agents/{id}`：获取单个 Agent 元数据

**Run 端点**：
- `POST /v1/agents/{id}/runs`：向已有 Agent 发送追加 prompt（一次只能有一个活跃 Run，冲突返回 409）
- `GET /v1/agents/{id}/runs`：列出所有 Run
- `GET /v1/agents/{id}/runs/{runId}`：获取 Run 状态
- `GET /v1/agents/{id}/runs/{runId}/stream`：SSE 流式读取（支持 Last-Event-ID 断点续传；超时返回 410 后改用 Get A Run）
- `POST /v1/agents/{id}/runs/{runId}/cancel`：取消 Run（终态，不可恢复）

**Artifacts**：`GET /v1/agents/{id}/artifacts`（列出）；`GET /v1/agents/{id}/artifacts/download?path=`（获取 15 分钟预签名 S3 URL）。

**Agent 生命周期**：archive（软删除，可恢复）、unarchive、DELETE（永久删除）。

**元数据端点**：`GET /v1/me`（API Key 信息）、`GET /v1/models`（可用模型）、`GET /v1/repositories`（GitHub 仓库，严格限速 1次/用户/分钟）。

**Worker Token**：`POST /v1/sub-tokens`（Service Account 为指定用户创建 1 小时 User-Scoped Token，用于 My Machines worker）。
