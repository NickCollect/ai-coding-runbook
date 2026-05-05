---
type: summary
source: 01_Raw/docs.cursor.com/docs--cloud-agent--self-hosted-pool.md
source_url: https://cursor.com/docs/cloud-agent/self-hosted-pool
title: "Self-Hosted Pool（企业自托管 Worker 池）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Self-Hosted Pool 让团队在公司自有基础设施中运行 Cloud Agent，管理员统一维护 Worker 池，支持 Kubernetes、自动扩缩容和标签路由。

**工作原理**：Worker 向 Cursor 云端建立出站 HTTPS 长连接，Agent 推理/规划在 Cursor 云端，工具调用（终端/文件编辑/浏览器）在本地 Worker 执行，Artifacts 上传至 Cursor 管理的存储。无需入站端口。上限：每用户 10 个 Worker，每团队 50 个；更大规模需联系销售。

**启动命令**：`agent worker start --pool`（池模式）；`--idle-release-timeout 600`（会话结束后保持 10 分钟等待追加消息再退出）；`--pool-name gpu`（命名池，路由特定 Worker 子集）。

**认证**：必须用 Service Account API Key，个人 API Key 不可用。

**触发池 Worker**：Slack 用 `self_hosted=true`/`pool=<name>`；GitHub 评论加 `@cursoragent self_hosted=true`；Linear 在 issue body 加 `pool=<name>` 或用 parent-child 标签。

**标签**：通过 `--label key=value`、`--labels-file labels.json`（JSON/TOML）或环境变量配置，用于路由。`repo` 和 `pool` 是保留标签。

**监控**：`--management-addr ":8080"` 暴露 `/healthz`、`/readyz`、`/metrics`，提供连接状态、会话状态等 Gauge/Counter 指标。**舰队 API**：`/v0/private-workers` 和 `/v0/private-workers/summary` 支持自动扩缩容（利用率 ≥90% 时触发扩容）。

**Kubernetes**：提供 Helm chart 和 Kubernetes operator。
