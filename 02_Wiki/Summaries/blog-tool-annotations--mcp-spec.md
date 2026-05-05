---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/blog/content/posts/2026-03-16-tool-annotations.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/2026-03-16-tool-annotations.md
title: "Blog post: Tool Annotations as Risk Vocabulary (2026-03-16)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Tool-use]
concepts_referenced: []
---

Co-authored by Ola Hungerford (Maintainer), Sam Morrow (GitHub), Luca Chang (AWS). Recaps the state of MCP **tool annotations** and offers a framework for evaluating new annotation proposals.

**Current annotations** (shipped in 2025-03-26 spec): `title`, `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`. All are **hints** — clients **must** treat them as untrusted unless they come from a trusted server. Defaults are pessimistic: a tool with no annotations is assumed non-read-only, potentially destructive, non-idempotent, open-world.

**History**: original PR #185 surfaced the still-relevant question — what value do hints provide if they can't be trusted? Spec landed on a compromise: hints + each client decides how much weight to give. Interface stayed deliberately small. `taskHint` was rejected as an annotation and landed as `Tool.execution` instead.

**Five open SEPs** proposing new annotations:
- #1913 Trust and Sensitivity Annotations (Draft, GitHub + OpenAI co-authored)
- #1984 Comprehensive Tool Annotations for Governance/UX (Draft)
- #1561 `unsafeOutputHint`
- #1560 `secretHint`
- #1487 `trustedHint`

A **Tool Annotations Interest Group** is forming.

**Lethal trifecta** (Simon Willison): private data + untrusted content + external communication = data theft conditions. Demonstrated with malicious Google Calendar event + MCP calendar server + local code execution tool. MCP makes assembling this trifecta easy because users mix-and-match servers in one session — the risk is a session property, not a server property. Several open SEPs aim to define metadata so a client can detect when a session has all three legs.

**What annotations CAN do**: drive confirmation prompts; enable graduated trust; improve UX (filtering, context in approval prompts — largely unexploited today); feed policy engines.

**What annotations CAN'T do**: make models resist prompt injection; prevent untrusted servers from lying; serve as enforcement (use network controls/sandboxing for hard guarantees); reason about a tool's risk in isolation (depends on what else is in the session).

**Five questions for evaluating proposals**: (1) What concrete client behavior does it enable? (2) Does it need trust to be useful? (3) Could `_meta` (namespaced custom keys) handle it instead? (4) Does it help reason about combinations? (5) Is it a hint or a contract? — contracts belong in the auth layer or runtime, not in `ToolAnnotations`.
