---
type: summary
source: 01_Raw/docs.cursor.com/docs--cloud-agent--my-machines.md
source_url: https://cursor.com/docs/cloud-agent/my-machines
title: "My Machines（本机 Worker）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

My Machines 让 Cloud Agent 在用户自有机器（笔记本、devbox、远程 VM）上执行，Agent 循环在 Cursor 云端运行，终端命令/文件操作在本机执行，无需开放入站端口。

**快速启动**：安装 CLI → `agent login` → `agent worker start` → 在 cursor.com/agents 选择该机器发送任务。

**常用选项**：`--name "devbox"`（多机器区分）、`--worker-dir /path/to/repo`（指定 repo 目录）、`--api-key` 或 `--auth-token-file`（服务账号/共享 devbox 场景）。

**从 Chat 触发特定机器**：在 Slack/GitHub/Linear 消息中加 `worker=my-devbox`（或 `machine=my-devbox`）；匹配条件：机器所有者 = 触发者、机器名一致、机器注册 repo = 触发 repo（三者同时满足）。repo 来自 worker 启动目录的 git remote，服务多个 repo 需分别启动 worker。

**MCP**：stdio 传输的 MCP server 在本机执行（可访问私有网络）；HTTP/SSE 传输由 Cursor 后端处理。

**网络要求**：仅需对外 HTTPS 访问 `api2.cursor.sh` 和 S3 artifacts 存储（artifact 上传用），无需入站规则。

**适用场景**：使用已有 repo/工具的 devbox、访问内网服务、保留构建缓存和密钥在本机、快速体验自托管 Cloud Agent。
