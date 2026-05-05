---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026.md
source_url: https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026
title: "Gemini API Model Spec — deep-research-max-preview-04-2026"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Model: deep-research-max-preview-04-2026

Source is in Korean (crawler localization).

## Overview

Maximum comprehensiveness for automated context collection and synthesis. Deep Research Max is optimized for long-running, accuracy-critical research that synthesizes complex information from hundreds of public web sources and private Workspace data (Gmail, Drive) into comprehensive, cited reports. Supports collaborative planning, visualization, MCP servers, file search.

## Spec Sheet

| Property | Value |
|---|---|
| Agent ID | `deep-research-max-preview-04-2026` |
| API | Interactions API |
| Data types | **Input**: Text, image, PDF, audio, video · **Output**: Text (cited reports), images |
| Input context window | 1,048,576 (1M) |
| Output token limit | 65,536 |
| Versions | Preview: `deep-research-max-preview-04-2026` |
| Last updated | April 2026 |

## Deep Research vs. Deep Research Max

| | Deep Research | Deep Research Max |
|---|---|---|
| Focus | Speed + efficiency | Maximum comprehensiveness |
| Sources | Public web | Public web + private Workspace |
| Speed | Faster | Slower (more thorough) |

- See `deep-research.md` for full documentation
