---
type: summary
source: 01_Raw/docs.cursor.com/docs--cli--reference--permissions.md
source_url: https://cursor.com/docs/cli/reference/permissions
title: "CLI 权限配置"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

CLI 权限系统控制 Agent 可执行的操作范围，配置在 `~/.cursor/cli-config.json`（全局）或 `<project>/.cursor/cli.json`（项目级，仅限权限）。

**四种权限类型**：
- `Shell(commandBase)`：Shell 命令访问（如 `Shell(git)`、`Shell(rm)`）；支持 `command:args` 语法精细控制
- `Read(pathOrGlob)`：文件读取（如 `Read(src/**/*.ts)`、`Read(.env*)`）
- `Write(pathOrGlob)`：文件写入（如 `Write(src/**)`, `Write(**/*.key)` deny）；print 模式需加 `--force` 才能写文件
- `WebFetch(domainOrPattern)`：Agent Web fetch 允许域名（如 `WebFetch(docs.github.com)`、`WebFetch(*.example.com)`）
- `Mcp(server:tool)`：MCP 工具调用（如 `Mcp(datadog:*)`、`Mcp(*:*)` 谨慎使用）

**配置结构**：
```json
{ "permissions": { "allow": [...], "deny": [...] } }
```

**规则**：Deny 优先于 Allow；支持 glob 通配符（`**`/`*`/`?`）；相对路径限定在当前工作区；绝对路径可指向工作区外。
