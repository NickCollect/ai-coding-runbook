---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026.md
source_url: https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026
title: "Gemini API Model Spec — deep-research-preview-04-2026"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Model: deep-research-preview-04-2026

Source is in Japanese (crawler localization).

## Overview

Powerful agentic researcher designed for autonomous multi-step research. Synthesizes complex information into comprehensive, cited reports. Supports collaborative planning, visualization, MCP servers, and file search. Two variants: Deep Research (speed + efficiency) and Deep Research Max (comprehensiveness).

## Spec Sheet

| Property | Value |
|---|---|
| Agent ID | `deep-research-preview-04-2026` |
| API | Interactions API |
| Data types | **Input**: Text, image, PDF, audio, video · **Output**: Text (cited reports), images |
| Input context window | 1,048,576 (1M) |
| Output token limit | 65,536 |
| Related model | `deep-research-max-preview-04-2026` |
| Versions | Preview: `deep-research-preview-04-2026` |
| Last updated | April 2026 |

## Notes

- Used via Interactions API (not `generate_content`)
- See `deep-research.md` for full documentation
