---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/embeddings.md
source_url: https://platform.claude.com/docs/en/build-with-claude/embeddings
title: "Embeddings"
summarized_at: 2026-05-05
entities_referenced: [Embeddings]
concepts_referenced: []
---

**Anthropic does not offer its own embedding model.** This guide is mainly about Voyage AI, recommended as one option among many embeddings vendors. Voyage offers state-of-the-art and domain-specific (finance, healthcare, legal, code) embedding models, including bespoke fine-tuned models for individual customers.

## Selecting an embeddings provider — factors

- Dataset size & domain specificity
- Inference performance (lookup speed + end-to-end latency)
- Customization (continued training on private data, domain specialization)

## Voyage models (recommended)

**Voyage 4 (latest):** all 32k context length; default embedding dim 1024 (also 256/512/2048 supported).

| Model | Notes |
|---|---|
| `voyage-4-large` | Best general-purpose / multilingual retrieval |
| `voyage-4` | Balanced quality/efficiency |
| `voyage-4-lite` | Latency / cost optimized |
| `voyage-4-nano` | Open-weight (Apache 2.0), on Hugging Face |

**Previous gen:** `voyage-3-large`, `voyage-3.5`, `voyage-3.5-lite`, `voyage-code-3` (code), `voyage-finance-2` (finance), `voyage-law-2` (legal, 16k context).

**Multimodal:** `voyage-multimodal-3.5` (text+image+video, 32k), `voyage-multimodal-3` (text+image, 32k).

## Getting started

1. Sign up at Voyage AI.
2. `export VOYAGE_API_KEY=...`
3. `pip install -U voyageai` then `voyageai.Client().embed(texts, model="voyage-4", input_type="document")`.
4. Or HTTP: `POST https://api.voyageai.com/v1/embeddings` with `Authorization: Bearer $VOYAGE_API_KEY`.

Available on AWS Marketplace.

## Usage tips

- For retrieval, **always set `input_type`** to `"query"` or `"document"` (not None). Voyage prepends task-specific prompts internally:
  - query: "Represent the query for retrieving supporting documents: "
  - document: "Represent the document for retrieval: "
- Voyage embeddings normalized to length 1 → cosine == dot product; cosine and Euclidean give identical rankings.
- **Quantization** via `output_dtype`: `float` (default), `int8`, `uint8`, `binary`, `ubinary` — saves 4× / 32× storage.
- **Matryoshka truncation:** keep leading subset of dimensions (e.g., truncate 1024 → 256).

## FAQ

- For general use: voyage-4-large (quality), voyage-4-lite (latency/cost), voyage-4 (balanced).
- Domain-specific: voyage-law-2 / voyage-code-3 / voyage-finance-2.
