---
type: summary
source: 01_Raw/docs.cursor.com/docs--cli--reference--output-format.md
source_url: https://cursor.com/docs/cli/reference/output-format
title: "CLI 输出格式参考"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cursor CLI `--print` 模式支持三种输出格式，通过 `--output-format` 指定。

**text（默认）**：仅输出最终助手消息，无中间过程和工具调用信息，适合只需要最终答案的脚本。

**json**：运行完成后输出单个 JSON 对象，包含 `type`/`subtype`/`result`（完整助手文本）/`duration_ms`/`session_id` 等字段；运行失败则非零退出码写 stderr。

**stream-json**：换行分隔 JSON（NDJSON），每行一个事件。事件类型：
- `system`（init，含模型/会话 ID/权限模式）
- `user`（用户 prompt 回显）
- `assistant`（完整助手消息段）
- `tool_call`（started/completed，含参数和结果）
- `result`（成功时终结事件，含完整文本）

**实时流**：`--stream-partial-output` 配合 `stream-json` 输出字符级增量 delta；注意过滤重复的 assistant 事件（`timestamp_ms` 有值且 `model_call_id` 无值的才是新增量）。

每行事件以 `\n` 结尾；未知字段应忽略（向后兼容）；`thinking` 事件在 print 模式中不输出。
