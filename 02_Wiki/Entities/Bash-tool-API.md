---
type: entity
name: Bash-tool-API
aliases: [bash tool (API) / bash_20250124 / shell tool API]
category: api-tool
status: ga
created: 2026-05-05
---

## 一句话定义

Anthropic API 的 client-side bash 工具 —— 让 Claude 在你应用维护的持久 shell session 里跑 shell 命令（**与 Claude Code 内置 Bash 工具不同**：API tool schema 由模型预定义，执行由你的 app 负责）。

## 关键属性

- **Tool definition**：schema-less，`{type: "bash_20250124", name: "bash"}`，schema 内置模型 [[bash-tool--at]]
- **Client-side**：API 只回 `tool_use` block，**你的 app 负责执行 + 维护 session state**（API 本身 stateless） [[bash-tool--at]]
- **Tool params**：`command` (required unless restart) / `restart: true` 重启 session [[bash-tool--at]]
- **典型实现**：`subprocess.Popen(["/bin/bash"], ...)` + 异步 stdin/stdout/stderr 管道 [[bash-tool--at]]
- **Capabilities**：persistent session（env vars / cwd 跨命令）、命令链、scripting [[bash-tool--at]]
- **Use cases**：dev workflow（build/test）、system automation、data processing、env setup [[bash-tool--at]]
- **Safety**：用 **allowlist**（不是 blocklist）；reject `&&` / `||` / `|` / `;` / `&` / `>` / `<` / `>>` / `$` / 反引号；强隔离用 `shell=False` + `shlex.split()` [[bash-tool--at]]
- **Error handling**：`tool_result` + `is_error: true`；常见 timeout / not found / permission denied；`subprocess.run(..., timeout=30)` 防挂 [[bash-tool--at]]
- **Best practices**：保持 session state、>100 行 output 截断防 context 爆、log 全命令、regex 删 secrets（`aws_access_key_id` 等） [[bash-tool--at]]
- **Security**：纵深防御 —— Docker/VM 隔离 + allowlist + ulimit + 过滤危险（`sudo` / `rm -rf`）+ 最小权限 + log [[bash-tool--at]]
- **Pricing**：tool definition 加 **245 input tokens**；命令 output 另计 [[bash-tool--at]]
- **Limitations**：无交互（vim / less / 密码 prompt）、无 GUI、session 在 client、output 完成才返回（无 streaming） [[bash-tool--at]]
- **配对**：与 [[Text-editor-tool]] 最佳（inspect → edit → test loop）；与 [[Code-execution-tool]] 同时启用 → 两个独立 sandbox，state 不共享，需 system prompt 区分 [[bash-tool--at]]
- **Git checkpointing 模式**：长 agent workflow 推荐 baseline commit + 每 feature commit + git log 重建 state + 失败 git checkout [[bash-tool--at]]
- **ZDR-eligible** [[bash-tool--at]]

## 出现来源

_14 summaries reference this entity_ ——
- [[bash-tool--at]] / [[tool-use-overview--at]] / [[tool-reference--at]] / [[tool-combinations--at]]
- [[text-editor-tool--at]] / [[code-execution-tool--at]] / [[computer-use-tool--at]]
- [[server-tools--at]] / [[memory-tool--at]] / [[manage-tool-context--at]]

## 相关

- [[Text-editor-tool]] —— canonical 配对
- [[Code-execution-tool]] —— Anthropic-managed 等价物（state 隔离）
- [[Hooks]]（Claude Code 的 Bash 是另一回事，与 API tool 区分）
- [[Tool-use]] / [[Messages-API]]
