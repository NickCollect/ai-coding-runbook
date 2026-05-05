---
type: summary
source: 01_Raw/docs.cursor.com/docs--agent--tools--terminal.md
source_url: https://cursor.com/docs/agent/tools/terminal
title: "Terminal Tool（沙盒执行）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Agent 在受限沙盒环境中执行 Shell 命令，默认阻止未授权文件访问和网络活动，支持 macOS/Linux/Windows（需 WSL2）。

**平台要求**：macOS v2.0+ 开箱即用；Windows 需 WSL2；Linux 需内核 6.2+ 且启用 Landlock v3（部分发行版需安装 AppArmor 配置包）。

**沙盒权限**：文件系统只读（工作区目录可读写）；网络默认封锁，可通过 `sandbox.json` 配置；`/tmp/` 完全可访问；`.cursor` 配置目录受保护不受白名单影响。

**白名单**：沙盒限制失败时，可选择 Skip（跳过）、Run（无限制执行）或 Add to allowlist（无限制执行并永久自动审批）。默认网络白名单包含 npm、PyPI、GitHub、DockerHub 等常用包注册中心和云服务商。

**配置**：`~/.cursor/sandbox.json`（用户级）或 `<workspace>/.cursor/sandbox.json`（项目级）。

**Auto-run 三种模式**：Run in Sandbox（自动沙盒执行）、Ask Every Time（每次审批）、Run Everything（无限制自动执行）。

**保护设置**：命令白名单、MCP 白名单、浏览器保护、文件删除保护、dotfile 保护、外部文件保护。

**企业控制**：管理员可从 web dashboard 覆盖用户配置，控制沙盒模式、网络访问、删除保护等。
