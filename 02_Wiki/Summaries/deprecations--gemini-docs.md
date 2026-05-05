---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/deprecations.md
source_url: https://ai.google.dev/gemini-api/docs/deprecations
title: "Gemini API — Deprecations"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Deprecations

Source is in Korean (crawler localization). "Deprecated" = announced end-of-support, soon to be "shut down". "Shut down" = completely disabled, endpoint unavailable.

## Gemini 3 Models

| Model | Release | Shutdown | Replacement |
|---|---|---|---|
| `gemini-3.1-flash-lite-preview` | 2026-03-03 | Not announced | — |
| `gemini-3.1-flash-image-preview` | 2026-02-26 | Not announced | — |
| `gemini-3.1-pro-preview` | 2026-02-19 | Not announced | — |
| `gemini-3-pro-image-preview` | 2025-11-20 | Not announced | — |
| `gemini-3-flash-preview` | 2025-12-17 | Not announced | — |
| `gemini-3-pro-preview` | 2025-11-18 | 2026-03-09 | `gemini-3.1-pro-preview` |

## Gemini 2.5 Pro

| Model | Shutdown | Replacement |
|---|---|---|
| `gemini-2.5-pro` (stable) | 2026-06-17 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-03-25` | 2025-12-02 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-05-06` | 2025-12-02 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-06-05` | 2025-12-02 | `gemini-3.1-pro-preview` |

## Gemini 2.5 Flash

| Model | Shutdown | Replacement |
|---|---|---|
| `gemini-2.5-flash` (stable) | 2026-06-17 | `gemini-3-flash-preview` |
| `gemini-2.5-flash-image` | 2026-10-02 | `gemini-3.1-flash-image-preview` |
| `gemini-2.5-flash-lite` | 2026-07-22 | `gemini-3.1-flash-lite-preview` |
| `gemini-2.5-flash-lite-preview-09-2025` | 2026-03-31 | `gemini-3.1-flash-lite-preview` |

## Gemini 2.0 Models

| Model | Shutdown | Replacement |
|---|---|---|
| `gemini-2.0-flash` | 2026-06-01 | `gemini-2.5-flash` |
| `gemini-2.0-flash-001` | 2026-06-01 | `gemini-2.5-flash` |
| `gemini-2.0-flash-lite` | 2026-06-01 | `gemini-2.5-flash-lite` |
| `gemini-2.0-flash-lite-001` | 2026-06-01 | `gemini-2.5-flash-lite` |

## Live API Models

| Model | Shutdown | Replacement |
|---|---|---|
| `gemini-2.0-flash-live-001` | 2025-12-09 | `gemini-3.1-flash-live-preview` |
| `gemini-3.1-flash-live-preview` | Not announced | — |
| `gemini-2.5-flash-native-audio-preview-12-2025` | Not announced | `gemini-3.1-flash-live-preview` |
| `gemini-live-2.5-flash-preview` | 2025-12-09 | `gemini-3.1-flash-live-preview` |

## Policy

- Deprecation notices posted on Release Notes page.
- Preview models deprecated with ≥2 weeks notice.
- Stable models deprecated with ≥1 year notice.
- Shut down models shown with grey background in the table.
