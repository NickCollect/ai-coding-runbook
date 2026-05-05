---
type: summary
source: 01_Raw/docs.cursor.com/docs--enterprise--deployment-patterns.md
source_url: https://cursor.com/docs/enterprise/deployment-patterns
title: "Enterprise 部署模式"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

企业 Cursor 部署涵盖编辑器（MDM）和 CLI（自动化/CI/CD）两种模式，支持 Windows/macOS/Linux。

**编辑器 MDM 部署**：IT 打包 Cursor 应用 → MDM（Jamf/Intune/Kandji）推送到用户机器 → 通过策略强制配置。

**MDM 策略（6 种）**：
- `AllowedTeamId`：限制登录账号
- `AllowedExtensions`：控制可安装扩展（JSON 格式，按发布者或完整 ID）
- `ExtensionGalleryServiceUrl`：自定义扩展市场 URL
- `NetworkDisableHttp2`：禁用 HTTP/2（改用 HTTP/1.1，兼容 Zscaler 等代理）
- `UpdateMode`：控制自动更新（`none` 禁用，`silentlyApplyOnQuit` 静默更新）
- `WorkspaceTrustEnabled`：工作区信任提示

**MDM 配置文件位置**：Windows: Group Policy（ADMX/ADML）；macOS: `.mobileconfig` 配置文件（Bundle ID: `com.todesktop.230313mzl4w4u92`），可通过 Jamf/Kandji/Intune 部署；Linux: `~/.cursor/policy.json`（2.0+ 版本）。

**permissions.json 部署**：`~/.cursor/permissions.json` 管理 terminal/MCP 自动运行白名单，可通过 MDM 推送，Cursor 实时监控变更无需重启。优先级：Dashboard > MDM 文件 > 编辑器设置。

**CLI 部署**：`curl https://cursor.com/install | bash` 安装，`CURSOR_API_KEY` 环境变量认证，支持 GitHub Actions 和 CI/CD 管道。安全控制（Privacy Mode/Hooks/模型限制）与编辑器版本完全相同。

**版本要求**：推荐用户保持在最新版本的一个版本内；落后 4 个以上版本将强制更新。
