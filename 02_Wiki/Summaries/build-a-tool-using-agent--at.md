---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent
title: "Tutorial: Build a tool-using agent"
summarized_at: 2026-05-05
entities_referenced: [Tool-use, Tool-runner, Messages-API, Anthropic-SDK-Python, Anthropic-SDK-TypeScript]
concepts_referenced: [Agentic-loop]
---

A guided five-ring tutorial that builds a calendar-management agent from a single tool call to a production-ready agentic loop and then collapses everything into the [[Tool-runner]] SDK abstraction. Each ring is a complete standalone runnable program that adds exactly one concept to the previous one. The example tool is `create_calendar_event` whose schema includes nested objects (recurrence), arrays (attendees), and optional fields—closer to real-world tools than a flat string argument.

**Ring 1: Single tool, single turn.** The smallest possible tool-using program. Send `tools` array with the user message via [[Messages-API]]. Response comes back with `stop_reason: "tool_use"` and a `tool_use` content block containing the tool's `name`, `id`, and `input`. Execute the tool externally; send back a `tool_result` block whose `tool_use_id` matches the call's `id`, plus the assistant's previous response content for full history. Second response has `stop_reason: "end_turn"` with the natural-language answer. Examples in cURL, ant CLI, [[Anthropic-SDK-Python]], [[Anthropic-SDK-TypeScript]].

**Ring 2: The agentic loop.** Real tasks may need several tool calls. The fix: a `while response.stop_reason == "tool_use":` loop that runs tools, appends the assistant content + tool_result, and re-calls the API until `stop_reason` is no longer `"tool_use"`. Conversation history accumulates instead of being rebuilt each request. The loop may run once or many times—your code no longer needs to know in advance. The example task ("Schedule a weekly team standup every Monday at 9am for the next 4 weeks. Invite alice/bob/carol@example.com.") may trigger one call (recurrence) or four calls (one per week) depending on how Claude breaks it down.

**Ring 3: Multiple tools, parallel calls.** Add a second tool `list_calendar_events` so Claude can check the existing schedule before creating new events. When Claude has multiple independent tool calls, it may return *several `tool_use` blocks in a single response*. Iterate over every `tool_use` block in `response.content`, collect all `tool_result` blocks, and send them back together in one user message. The example output: "I checked your calendar for next Monday and found an existing meeting from 2pm to 3pm. I've scheduled the planning session for 10am to 11am to avoid the conflict."

**Ring 4: Error handling.** Tools fail (e.g., a calendar API rejects an event with too many attendees). Wrap tool execution in try/except; on failure, send back a `tool_result` with the error text and `is_error: true`. Claude reads the flag and can retry with corrected input, ask the user for clarification, or explain the limitation. Example output for a 15-attendee request when the tool's max is 10: "I tried to schedule the all-hands but the calendar only allows 10 attendees per event. I can split this into two sessions, or you can let me know which 10 people to prioritize." The `is_error` flag is the only difference from a successful result.

**Ring 5: The Tool Runner SDK abstraction.** The hand-written loop from rings 2–4 is replaced by `client.beta.messages.tool_runner(...).until_done()` (Python) or `client.beta.messages.toolRunner({...})` (TypeScript). The Python SDK uses the `@beta_tool` decorator to infer the schema from type hints + docstring (an `attendees: list[str] | None = None` parameter, etc.). TypeScript uses `betaZodTool` with a Zod `z.object({...})` schema and an inline `run: async (input) => ...` callback. The loop, error wrapping, result formatting, and conversation management are all handled internally. Output is identical to Ring 3, but with roughly half the lines and the schema living next to the implementation. Tool Runner is available in Python, TypeScript, and Ruby SDKs only—the cURL and CLI tabs note this and recommend keeping the Ring 4 loop for those scripts.

**Common patterns reinforced across rings:**
- `tool_choice: {type: "auto", disable_parallel_tool_use: true}` is used in early rings; ring 3 omits it to allow parallel calls.
- The assistant's `response.content` (the entire array, including any text blocks before `tool_use`) must be appended verbatim to messages on every turn.
- A response may contain text blocks before the `tool_use` block; filter by `block.type == "tool_use"` rather than assuming position.
- `tool_use_id` matching is mandatory.

**What the reader has built.** Every piece of the tool-use protocol is touched: `tool_use` blocks, `tool_result` blocks, `tool_use_id` matching, `stop_reason` checking, `is_error` signaling—then collapsed into the Tool Runner. Suggested next reading: define-tools (schema specs), tool-runner (deep dive), troubleshooting-tool-use.
