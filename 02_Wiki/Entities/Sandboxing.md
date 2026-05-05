---
type: entity
name: Sandboxing
aliases: [sandbox, Claude Code sandbox]
category: feature
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 命令执行的沙箱隔离机制

## 关键属性

- OS-level filesystem + network 隔离仅作用于 Bash tool 及其子进程；built-in Read/Edit/Write 走 permission system 而**不**经 sandbox [[sandboxing]]
- OS primitives：macOS = Seatbelt，Linux/WSL2 = `bubblewrap`（需 `apt install bubblewrap socat`），WSL1 **不支持** [[sandboxing]]
- 默认 filesystem 边界：写权限 = cwd + 子目录，读权限 = 整机（除被 deny 的目录）；OS 级强制，对 kubectl/terraform/npm 子进程同样生效 [[sandboxing]] [[security]]
- Network 通过 sandbox 外部的 proxy server 强制 domain allowlist；新域名 prompt（除非 `allowManagedDomainsOnly`）；**不做 TLS 终止/检查**，存在 domain fronting 风险 [[sandboxing]] [[secure-deployment]]
- `/sandbox` 命令打开菜单，依赖缺失时显示安装步骤；默认无法启动时 warn-and-run-without-sandbox，managed `sandbox.failIfUnavailable: true` 改为硬失败 [[sandboxing]]
- 两种模式：**auto-allow**（沙箱内 bash 自动放行，不能沙箱化的回退到普通 permission flow）vs **regular permissions**（沙箱内仍走 prompt） [[sandboxing]]
- `rm`/`rmdir` 针对 `/`、`$HOME`、关键系统路径**始终** prompt（即便 bypass 模式）作为 circuit breaker [[sandboxing]] [[permission-modes]]
- `allowWrite`/`denyWrite`/`allowRead`/`denyRead` 数组**跨 settings scope 合并**（不替换）；`allowRead` 优先于 `denyRead` [[sandboxing]]
- 路径前缀语义和 Read/Edit permission 不同：`/` = 绝对，`~/` = home，`./` 或无前缀 = project root（项目设置）或 `~/.claude`（用户设置） [[sandboxing]]
- WSL2 沙箱命令**不能**调用 Windows binary（`cmd.exe`、`powershell.exe`、`/mnt/c/`）；通过 `excludedCommands` 让其在沙箱外执行 [[sandboxing]]
- 已知不兼容：`watchman`（用 `jest --no-watchman` 替代）、`docker`（加入 `excludedCommands`） [[sandboxing]]
- Escape hatch：`dangerouslyDisableSandbox` 参数让 Claude 请求出沙箱执行；`allowUnsandboxedCommands: false` 完全禁用此 escape [[sandboxing]] [[settings-bash-sandbox]]
- 严格模板（`settings-strict.json` / `settings-bash-sandbox.json`）组合：`allowManagedPermissionRulesOnly`、`autoAllowBashIfSandboxed: false`、`allowUnsandboxedCommands: false`、空 `allowedDomains`、`enableWeakerNestedSandbox: false` [[settings-bash-sandbox]] [[settings-strict]]
- `enableWeakerNestedSandbox` 让 Linux 在 Docker 内运行（不需要 privileged namespaces）但**显著削弱安全性** [[sandboxing]] [[secure-deployment]]
- 开源：`npx @anthropic-ai/sandbox-runtime <command>` 来自 `anthropic-experimental/sandbox-runtime`，可沙箱化任意命令包括 MCP server [[sandboxing]] [[secure-deployment]]
- 与 permissions 互补：permissions 管"哪些 tool / 哪些输入"（覆盖所有 tool）；sandbox 管"Bash + 子进程在 OS 层能访问什么" [[sandboxing]] [[permissions--claude-code]]
- Devcontainer / Docker / gVisor / Firecracker 是更强的隔离层，sandbox-runtime 是最低 overhead 的内置方案 [[secure-deployment]] [[devcontainer]]

## 出现来源

_23 summaries reference this entity_:

- [[2026-w16]]
- [[README--examples-settings]]
- [[admin-setup]]
- [[best-practices]]
- [[changelog]]
- [[changelog--claude-code-repo]]
- [[commands]]
- [[computer-use]]
- [[debug-your-config]]
- [[devcontainer]]
- [[env-vars]]
- [[glossary]]
- [[hosting]]
- [[permission-modes]]
- [[permissions--claude-code]]
- [[remote-control]]
- [[sandboxing]]
- [[secure-deployment]]
- [[security]]
- [[settings]]
- [[settings-bash-sandbox]]
- [[settings-strict]]
- [[setup]]

## 相关

- [[Permission-mode]] — sandbox 与 permission mode 正交但互补；auto-allow 模式与 mode 设置独立
- [[Settings]] — `sandbox.*` 配置块在 settings.json 中声明
- [[MCP-server]] — sandbox-runtime 可包裹 MCP server 进程
- [[Hooks]] — PreToolUse hook 可与 sandbox 配合做更细粒度过滤
- [[Computer-use]] — computer-use 工具不在 sandbox 范围内
