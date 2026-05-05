---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/tool-combinations.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-combinations
title: "Tool combinations"
summarized_at: 2026-05-05
entities_referenced: [Tool-use, Web-search-tool, Web-fetch-tool, Code-execution-tool, Text-editor-tool, Bash-tool-API, Memory-tool, Computer-use-tool-API]
concepts_referenced: []
---

Common Anthropic-tool pairings for research agents, coding agents, and long-running agents. Each snippet shows only the `tools` array; the rest of the request shape lives in Handle tool calls.

**Research agent: web_search + code_execution.** [[Web-search-tool]] finds sources; [[Code-execution-tool]] analyzes and synthesizes. Claude searches for data, then writes Python to process, tabulate, or visualize it. Good fit for questions that need both up-to-date info and nontrivial computation—e.g., "compare this quarter's earnings across the top five cloud providers." Flow: search → execute → optionally search again to fill a gap. Code execution is server-side, so no client sandbox to manage.

```json
{"tools": [
  {"type": "web_search_20260209", "name": "web_search"},
  {"type": "code_execution_20250825", "name": "code_execution"}
]}
```

**Coding agent: text_editor + bash.** [[Text-editor-tool]] reads and modifies files; [[Bash-tool-API]] runs tests and build commands. The canonical software-development loop: inspect → edit → test → repeat. Both client-executed, so your application controls which files and commands are accessible. Pair with a constrained working directory and a command allowlist if the agent operates on untrusted code.

```json
{"tools": [
  {"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"},
  {"type": "bash_20250124", "name": "bash"}
]}
```

**Cite-then-fetch: web_search + web_fetch.** [[Web-search-tool]] surfaces candidate URLs; [[Web-fetch-tool]] retrieves full page content for the relevant ones. Avoids fetching everything upfront—Claude inspects search snippets, picks the two or three results that look truly relevant, and fetches only those. Useful when answers live in long-form content (docs, articles, specs) that snippets can't fully capture; fetch pulls the complete page so Claude can cite specific passages.

```json
{"tools": [
  {"type": "web_search_20260209", "name": "web_search"},
  {"type": "web_fetch_20260209", "name": "web_fetch"}
]}
```

**Long-running agent: memory + any toolset.** [[Memory-tool]] persists state across conversations; the other tools do the work. Add memory to any agent that needs to remember prior sessions—a support agent recalling a customer's earlier issues, a project assistant tracking decisions made last week. Memory is *orthogonal* to the rest of the toolset—it doesn't change how other tools behave; it gives Claude a place to write down and later retrieve facts that would otherwise be lost when the context window resets.

```json
{"tools": [{"type": "memory_20250818", "name": "memory"}]}
```

Add other tools alongside `memory` in the same array.

**All-in-one: computer_use.** The [[Computer-use-tool-API]] subsumes most others by operating a full desktop. Claude sees screenshots and issues mouse/keyboard actions—it can drive any application a human can. Use when the task requires arbitrary GUI interaction that more specific tools can't reach: legacy software without an API, visual verification steps, or workflows spanning multiple desktop apps.

```json
{"tools": [{
  "type": "computer_20250124", "name": "computer",
  "display_width_px": 1280, "display_height_px": 800
}]}
```

Computer use is the *most general* option but also the *slowest*—every action requires a screenshot round-trip. Prefer narrower tools when they cover your case; reach for computer use when nothing else fits.

These pairings are starting points, not prescriptions—mix to fit the task.
