---
type: summary
source: 01_Raw/github/anthropics/skills/skills/mcp-builder/reference/evaluation.md
title: "MCP Server Evaluation Guide (mcp-builder)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Reference doc on creating evaluations for MCP servers. The measure of MCP server quality is NOT comprehensiveness of tools — it's how well the input/output schemas + descriptions enable an LLM (with no other context, only the MCP server) to answer realistic complex questions.

**Output format**: 10 question/answer pairs in `<evaluation>` XML:
```xml
<evaluation>
  <qa_pair>
    <question>...</question>
    <answer>Single verifiable answer</answer>
  </qa_pair>
</evaluation>
```

**Question requirements** (13 rules):
1. **Independent** — no question depends on another's answer.
2. **READ-ONLY, NON-DESTRUCTIVE, IDEMPOTENT** — no state mutation needed.
3. **Realistic, clear, concise, complex** — multiple/dozens of tool calls or steps.
4. **Deep exploration** — multi-hop, sequential.
5. **Extensive paging** — may need querying old/niche data (1–2 years out-of-date).
6. **Deep understanding** — may use True/False with evidence, multi-hypothesis multiple-choice.
7. **NOT keyword-searchable** — use synonyms / paraphrases / related concepts; no surface keywords from target.
8. **Stress-test return values** — large JSON, multiple data modalities (IDs/names/timestamps/file IDs/extensions/mimetypes/URLs/GIDs).
9. **Reflect real human use cases**.
10. **May require dozens of tool calls** — challenges LLMs with limited context, encourages MCP servers to reduce per-call payload.
11. **Include ambiguous questions** — but each must still have a SINGLE VERIFIABLE answer.
12. **STABLE answers** — don't ask about counts/state that changes (reactions to a post, replies to a thread, channel members).
13. **Don't let the MCP server's surface limit your questions** — some may not be solvable with available tools, that's signal.

**Answer guidelines**: verifiable via direct string comparison. (Doc continues past read limit.)
