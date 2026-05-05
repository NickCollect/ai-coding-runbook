---
type: summary
source: 01_Raw/anthropic.com/engineering/effective-context-engineering-for-ai-agents.md
source_url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
title: "Effective context engineering for AI agents"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Memory, Memory-tool]
concepts_referenced: [Context-window, Agentic-loop, Compaction, Prompt-caching]
---

Anthropic post (Sep 29, 2025) framing **context engineering** as the natural successor to prompt engineering — the discipline of curating and maintaining the optimal token set across all sources (system prompt, tools, MCP, external data, message history) during multi-turn agent inference.

**Why context is finite.** "Context rot": as token count grows, the model's recall accuracy decreases (varying per model, but universal). LLMs have an attention budget; every token depletes it. Architectural cause: transformer attention is n² over n tokens, training-data distribution favors shorter sequences, position-encoding interpolation handles longer contexts but with degradation. Performance is a gradient, not a cliff.

**Anatomy of effective context.**
- *System prompts at the right altitude* — between brittle if-else hardcoded logic and overly vague guidance. Use clear sections (`<background_information>`, `## Tool guidance`, `## Output description`) with XML or Markdown delimiters. Minimal does not mean short — minimal means the *smallest set fully outlining expected behavior*.
- *Tools matter* — they define the agent-environment contract. Self-contained, robust to error, clear intent, descriptive parameters, minimal overlap. The most common failure mode: bloated tool sets where even a human engineer can't say which tool to use. (See [writing-tools-for-agents](https://www.anthropic.com/engineering/writing-tools-for-agents).)
- *Examples (few-shot) yes, edge-case dumps no* — curate diverse canonical examples, not exhaustive rule lists.

**Just-in-time context vs. pre-inference retrieval.** Field shifting from pre-loading embeddings to maintaining lightweight identifiers (file paths, queries, URLs) and dynamically loading via tools. Mirrors human cognition (we use file systems and bookmarks, not memorized corpora). Claude Code uses this: `glob` and `grep` allow just-in-time file retrieval, bypassing stale indexes. Metadata of references (folder structure, naming, timestamps) provides interpretive signals. Trade-off: runtime exploration is slower than retrieval; needs careful tool/heuristic design or agent wastes context. Hybrid strategies often best (CLAUDE.md upfront + glob/grep on demand).

**Long-horizon techniques** for tasks exceeding context window:
- *Compaction* — summarize current context into a smaller representation, restart with summary plus most recent items (Claude Code passes message history to model for summarization, keeps architectural decisions / unresolved bugs / implementation details, drops redundant tool outputs, plus 5 most recently accessed files). Tune for high recall first, then iterate to improve precision. Lightest-touch form: tool-result clearing (now a Developer Platform feature).
- *Structured note-taking / agentic memory* — agent writes notes outside context window, pulls them back later. Examples: Claude Code to-do lists, custom NOTES.md files. **Claude Plays Pokémon** demonstrates this: agent maintains tallies ("for the last 1,234 steps I've trained Pikachu in Route 1, gained 8 levels toward 10"), maps explored regions, remembers achievements, persists combat strategies. After context resets, reads its notes and continues multi-hour sequences. Sonnet 4.5 launch shipped a Memory tool (file-based system) on the Developer Platform.
- *Multi-agent architectures* — split work across subagents with isolated context windows; orchestrator coordinates summaries.

**Mental model.** Context engineering is iterative: "what configuration of context is most likely to generate desired behavior?" Curation phase happens *every time* you decide what to send the model — not once like a written prompt. As models improve, design will trend toward less human curation; "do the simplest thing that works" remains the guidance. Foundational reference, paired with [building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents).
