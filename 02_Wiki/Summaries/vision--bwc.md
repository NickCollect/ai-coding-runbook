---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/vision.md
source_url: https://platform.claude.com/docs/en/build-with-claude/vision
title: "Vision"
summarized_at: 2026-05-05
entities_referenced: [Vision, Messages-API, Files-API, Computer-use-tool-API]
concepts_referenced: [Context-window]
---

Claude's vision capabilities let it understand and analyze images. Multiple images per request are jointly analyzed.

## Limits

- **Per claude.ai message:** 20 images.
- **Per API request:** 100 images for 200k-window models, **600 images for other models** (1M-window).
- **Max dimensions:** 8000×8000 px. If >20 images in one request → reduced to 2000×2000 px.
- **Request size:** 32 MB standard endpoint cap may bite first → use Files API for many large images.

## Token cost approximation

`tokens ≈ (width × height) / 750` (in pixels).

## Native max resolution

| Model | Max tokens / image | Max long edge |
|---|---|---|
| Opus 4.7 | 4784 tokens | 2576 px |
| Other models | 1568 tokens | 1568 px |

Larger images are resized preserving aspect ratio, then padded to multiples of 28 px on bottom/right.

**Coordinates in output** (points, bboxes) are in resized/padded image space → must be rescaled client-side using original-vs-resized dimensions.

### Opus 4.7 high-resolution support

First Claude model with high-res images (up to 2576 px long edge). Auto-applied — no beta header. Can use ~3× more tokens (4784 vs 1600 prior). Useful for computer use, screenshot understanding, document analysis. Downsample if you don't need the fidelity.

## Cost examples (Sonnet 4.6 @ $3/MTok input)

| Image | Tokens | $/image | $/1k images |
|---|---|---|---|
| 200×200 | ~54 | ~$0.00016 | ~$0.16 |
| 1000×1000 | ~1334 | ~$0.004 | ~$4.00 |
| 1092×1092+ | ~1568 | ~$0.0047 | ~$4.70 |

## Cost examples (Opus 4.7 @ $5/MTok input)

| Image | Tokens | $/image | $/1k images |
|---|---|---|---|
| 200×200 | ~54 | ~$0.00027 | ~$0.27 |
| 1000×1000 | ~1334 | ~$0.0067 | ~$6.70 |
| 1092×1092 | ~1590 | ~$0.0080 | ~$8.00 |
| 1920×1080 | ~2765 | ~$0.014 | ~$14.00 |
| 2000×1500 | ~4000 | ~$0.020 | ~$20.00 |

## Quality best practices

- **Formats:** JPEG, PNG, GIF, WebP. Animations not supported (only first frame).
- **Image clarity:** avoid blur/pixelation.
- **Text in image:** keep legible; don't crop key visual context to enlarge.
- **Resizing:** images may be resized — pre-resize/crop yourself for predictable text legibility and coordinate work.
- **Compression:** lossy (JPEG / WebP-lossy) reduces request size + latency, but heavy compression introduces artifacts that degrade model performance — verify settings on actual images.

## Three input methods

1. Base64-encoded in `image` content blocks (`source: {type: "base64", media_type, data}`)
2. URL reference (`source: {type: "url", url}`)
3. Files API `file_id` (`source: {type: "file", file_id}`)

## Tip

Place images **before** text for best results (image-then-text structure).
