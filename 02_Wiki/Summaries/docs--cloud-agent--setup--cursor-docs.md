---
type: summary
source: 01_Raw/docs.cursor.com/docs--cloud-agent--setup.md
source_url: https://cursor.com/docs/cloud-agent/setup
title: "Cloud Agent Setup（环境配置）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cloud Agent 运行在隔离的 Ubuntu VM 上，需要配置开发环境使 Agent 具备与人类开发者相同的工具访问能力。

**环境配置两种方式**：
1. **Agent 驱动（推荐）**：在 cursor.com/onboard 让 Agent 自动搭建环境，完成后可创建 VM 快照供后续重用
2. **手动 Dockerfile 配置（高级）**：通过 `.cursor/environment.json` 引用 Dockerfile，适合需要特定系统依赖、编译器版本或 OS 镜像的场景

**配置解析顺序**：`.cursor/environment.json`（仓库级）> 个人环境配置 > 团队环境配置。

**关键字段**（environment.json）：`build.dockerfile`、`install`（更新/安装依赖命令，幂等）、`start`（启动常驻进程）、`terminals`（tmux 会话中运行的应用进程）。

**密钥管理**：通过 cursor.com/dashboard/cloud-agents 的 Secrets tab 管理（KMS 加密，暴露为环境变量）；支持 redacted 模式（防止 Agent 意外提交密钥到 repo）；支持 AWS IAM Role assume。

**Docker/Tailscale**：支持，但 Docker 在容器内有边缘情况，需用 fuse-overlayfs + iptables-legacy；Tailscale 需使用 userspace networking 模式。

**AGENTS.md**：建议添加"Cursor Cloud specific instructions"专区，说明云端特定的构建/测试步骤。
