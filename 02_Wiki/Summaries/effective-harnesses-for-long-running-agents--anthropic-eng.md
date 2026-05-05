---
type: summary
source: 01_Raw/anthropic.com/engineering/effective-harnesses-for-long-running-agents.md
source_url: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
title: "Effective harnesses for long-running agents"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, MCP-server]
concepts_referenced: [Agentic-loop, Compaction, Context-window]
---

Anthropic engineering post (Nov 26, 2025) on building harnesses that let Claude Agent SDK agents make consistent progress across many context windows on hours-or-days-long tasks. Out of the box, even Opus 4.5 in a loop with compaction fails to build a production-quality web app from a high-level prompt like "build a clone of claude.ai."

**Two failure modes observed.**
1. *Trying to one-shot the app* — agent runs out of context mid-implementation, leaves features half-built and undocumented, next session must guess what happened.
2. *Late-stage premature completion* — later instances see existing progress, declare the job done.

**Two-part solution.**
- **Initializer agent** — runs once at the start. Sets up `init.sh` (starts dev server, runs basic e2e check), a `claude-progress.txt` log, an initial git commit, and a comprehensive feature list (200+ items for the claude.ai clone, e.g., "user can open a new chat, type query, press enter, see AI response"), all initially marked `passes: false`. JSON format for the feature file (model less likely to overwrite JSON than Markdown). Strong wording: "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality."
- **Coding agent** — every subsequent session works on one feature at a time, commits to git with descriptive messages, updates the progress file. Git allows revert to working states.

**End-to-end testing via Puppeteer MCP.** Claude tends to mark features done after unit-test or curl-against-dev-server checks without verifying end-to-end. Explicit prompting + browser-automation tools (Puppeteer MCP) eliminates this. Limitations remain: Puppeteer can't see browser-native alert modals, so features depending on those tend to be buggier.

**Standard session opening.** Each coding agent prompts itself through:
1. `pwd` to confirm working directory.
2. Read git log + progress file for recent state.
3. Read feature list, pick highest-priority undone feature.
4. Run `init.sh`, do basic end-to-end test (start dev server, send a chat message, get response) before implementing anything new — catches broken state before introducing more changes.

A typical session starts with `pwd / read claude-progress.txt / read feature_list.json / git log --oneline -20 / start dev server / Puppeteer e2e check / verify fundamental functionality / pick next feature`.

**Inspiration.** Practices borrowed from what effective human software engineers do daily — write progress logs, structure handoffs, leave clean states. Code samples in the `anthropics/claude-quickstarts` repo under `autonomous-coding`. Paired conceptually with the [building-c-compiler](https://www.anthropic.com/engineering/building-c-compiler) post on agent teams and the [harness-design-long-running-apps](https://www.anthropic.com/engineering/harness-design-long-running-apps) follow-up.
