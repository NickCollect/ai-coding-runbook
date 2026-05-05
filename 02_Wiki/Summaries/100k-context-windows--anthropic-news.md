---
type: summary
source: 01_Raw/anthropic.com/news/100k-context-windows.md
source_url: https://www.anthropic.com/news/100k-context-windows
title: "Introducing 100K Context Windows"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Context-window]
---

May 11, 2023 — Claude's context window expanded from 9K → 100K tokens (~75,000 words / hundreds of pages). Conversations can now span hours or days. Demonstration: loaded *The Great Gatsby* (72K tokens) into Claude-Instant with one line modified ("Mr. Carraway was a software engineer that works on machine learning tooling at Anthropic"); Claude found the difference in 22 seconds.

**Use cases unlocked**: dense-document digest (financial statements, research papers); strategic risk/opportunity from annual reports; legislation pros/cons; legal-doc theme/argument analysis; full developer-doc Q&A; codebase prototyping by dropping the whole repo into context.

100K is positioned as substantially better than vector-search RAG for complex synthesis questions. AssemblyAI demoed transcribing a podcast to 58K words and using Claude for summarization/Q&A (~6 hours of audio at 100K). Available immediately on the API.
