---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use
title: "Parallel tool use"
summarized_at: 2026-05-05
entities_referenced: [Tool-use, Tool-runner]
concepts_referenced: []
---

How to enable, format, and troubleshoot parallel tool calls—when Claude calls multiple tools in one turn. Single-call flow lives in the Handle tool calls page.

**Default behavior.** Claude *may* use multiple tools to answer one query. Disable via:
- `disable_parallel_tool_use: true` with `tool_choice.type: "auto"` → at most one tool.
- `disable_parallel_tool_use: true` with `tool_choice.type: "any"` or `"tool"` → exactly one tool.

The [[Tool-runner]] SDK abstraction handles parallel execution automatically; the manual examples on this page are for code that needs custom control.

**Worked example pattern.** Two tools (`get_weather` + `get_time`); user asks "What's the weather in SF and NYC, and what time is it there?"; Claude returns multiple `tool_use` blocks in a single response. Iterate over `response.content`, filter by `block.type == "tool_use"`, execute each, and collect ALL `tool_result` blocks into a SINGLE user message before sending the next request. Code example shown in Python, TypeScript, C#, Go, Java, PHP, Ruby.

**Maximizing parallel tool use.** Default Claude 4 behavior is already strong, but you can encourage parallelism with system-prompt nudges. Mild version: "For maximum efficiency, whenever you need to perform multiple independent operations, invoke all relevant tools simultaneously rather than sequentially." Stronger version (XML-tagged):

```
<use_parallel_tool_calls>
For maximum efficiency, whenever you perform multiple independent operations, invoke all relevant tools simultaneously rather than sequentially. Prioritize calling tools in parallel whenever possible. For example, when reading 3 files, run 3 tool calls in parallel to read all 3 files into context at the same time. When running multiple read-only commands like `ls` or `list_dir`, always run all of the commands in parallel. Err on the side of maximizing parallel tool calls rather than running too many tools sequentially.
</use_parallel_tool_calls>
```

User-message phrasing also matters: prefer "Check the weather in Paris and London simultaneously" or explicit "Please use parallel tool calls to get the weather for Paris, London, and Tokyo at the same time" over serial phrasing like "What's the weather in Paris? Also check London."

**Troubleshooting—if Claude isn't making parallel calls when expected:**

1. *Incorrect tool result formatting* (most common). Sending separate user messages for each tool result "teaches" Claude to avoid parallel calls. ALL tool results must be in a single user message:

❌ Wrong (reduces parallel use):
```json
[{"role": "assistant", "content": [tool_use_1, tool_use_2]},
 {"role": "user", "content": [tool_result_1]},
 {"role": "user", "content": [tool_result_2]}]
```

✅ Correct:
```json
[{"role": "assistant", "content": [tool_use_1, tool_use_2]},
 {"role": "user", "content": [tool_result_1, tool_result_2]}]
```

Other formatting rules (text-after-tool_results, immediate adjacency) live in Handle tool calls.

2. *Weak prompting*: use the stronger XML-tagged system prompt above.

3. *Measuring*: average tools per tool-calling message—`>1.0` indicates parallel calls are working.
