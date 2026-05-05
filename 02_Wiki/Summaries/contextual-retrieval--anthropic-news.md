---
type: summary
source: 01_Raw/anthropic.com/news/contextual-retrieval.md
source_url: https://www.anthropic.com/news/contextual-retrieval
title: "Introducing Contextual Retrieval"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Prompt-caching, Context-window]
---

Sep 19, 2024 — Announcement-page version of the engineering post **Introducing Contextual Retrieval**. Same content as the Engineering Blog version (`engineering/contextual-retrieval.md`): two preprocessing techniques — Contextual Embeddings + Contextual BM25 — that prepend chunk-specific situating context to each chunk before embedding/BM25 indexing.

**Headline result.** 49% reduction in failed retrievals; 67% with reranking. Implementation uses Claude 3 Haiku with prompt caching to keep cost low ($1.02 per M document tokens). For knowledge bases <200K tokens, Anthropic still recommends putting the whole base in the prompt with prompt caching.

See the engineering-version summary `contextual-retrieval--anthropic-eng.md` for the technical detail.
