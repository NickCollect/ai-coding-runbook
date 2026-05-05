---
type: summary
source: 01_Raw/anthropic.com/engineering/contextual-retrieval.md
source_url: https://www.anthropic.com/engineering/contextual-retrieval
title: "Introducing Contextual Retrieval"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Prompt-caching, Context-window]
---

Anthropic post (Sep 19, 2024) introducing **Contextual Retrieval**, a preprocessing technique that improves RAG retrieval accuracy by attaching chunk-specific context before embedding and BM25 indexing.

**The context-conundrum in traditional RAG.** Standard RAG splits documents into chunks (a few hundred tokens), embeds them, stores in a vector DB, retrieves by semantic similarity at query time. Sometimes BM25 is added for exact-match queries (technical terms, error codes, IDs). But chunking destroys context: "The company's revenue grew by 3% over the previous quarter" is useless if you don't know which company or which quarter.

**Contextual Retrieval** prepends chunk-specific explanatory context to each chunk before both embedding (Contextual Embeddings) and BM25 indexing (Contextual BM25). Example transformation:

> *Original:* "The company's revenue grew by 3% over the previous quarter."
> *Contextualized:* "This chunk is from an SEC filing on ACME corp's performance in Q2 2023; the previous quarter's revenue was $314 million. The company's revenue grew by 3% over the previous quarter."

**Generation is automated with Claude.** A Claude 3 Haiku prompt receives the whole document plus a chunk and outputs 50-100 tokens of situating context. Cost is made viable by **prompt caching**: the document is loaded once into the cache, then referenced for every chunk. Quoted cost: $1.02 per million document tokens (assuming 800-token chunks, 8K-token documents, 50-token context instructions, 100-token output per chunk).

**Results.** Reduces failed retrievals by **49%**; combined with reranking, by **67%**.

**When you don't need RAG.** If your knowledge base is <200K tokens (~500 pages), just put it all in the prompt — prompt caching makes this fast and cheap (>2x latency reduction, up to 90% cost reduction on cached prompts).

**Comparison to prior approaches.** Generic document summaries appended to chunks gave Anthropic limited gains in their experiments. Hypothetical document embedding (HyDE) and summary-based indexing were evaluated and showed low performance. Contextual Retrieval differs: per-chunk situating context, not document-level or query-level transformation.

**Implementation.** Cookbook published at platform.claude.com/cookbook/capabilities-contextual-embeddings-guide. The approach is now considered a standard baseline for RAG over chunked corpora when prompt caching is available.
