---
source_url: https://ai.google.dev/gemini-api/docs/interactions/media-resolution?hl=zh-TW
fetched_at: 2026-06-22T06:32:25.219434+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research) is now available in preview with collaborative planning, visualization, MCP support, and more.

- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview)
- [Docs](https://ai.google.dev/gemini-api/docs)

Send feedback

# Media resolution

The `media_resolution` parameter controls how the Gemini API processes media inputs like images, videos, and PDF documents by determining the **maximum number of tokens** allocated for media inputs, allowing you to balance response quality against latency and cost. For different settings, default values and how they correspond to tokens, see the [Token counts](#token-counts) section.

You can configure media resolution for individual media objects (content items) within your request (Gemini 3 only).

## Per-content-item media resolution (Gemini 3 only)

Gemini 3 allows you to set media resolution for individual media objects within your request, offering fine-grained optimisation of token usage. You can mix resolution levels in a single request. For example, using high resolution for a complex diagram and low resolution for a simple contextual image.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## Available resolution values

The Gemini API defines the following levels for media resolution:

- `unspecified`: The default setting. The token count for this level varies significantly between Gemini 3 and earlier Gemini models.
- `low`: Lower token count, resulting in faster processing and lower cost, but with less detail.
- `medium`: A balance between detail, cost, and latency.
- `high`: Higher token count, providing more detail for the model to work with, at the expense of increased latency and cost.
- `ultra_high` (Per content item only): Highest token count, required for specific use cases such as [computer use](https://ai.google.dev/gemini-api/docs/interactions/computer-use).

Note that `high` provides the optimal performance for most use cases.

The exact number of tokens generated for each of these levels depends on both the **media type** (Image, Video, PDF) and the **model version**.

## Token counts

The tables below summarize the approximate token counts for each `media_resolution` value and media type per model family.

**Gemini 3 models**

| MediaResolution | Image | Video | PDF |
| --- | --- | --- | --- |
| `unspecified` (Default) | 1120 | 70 | 560 |
| `low` | 280 | 70 | 280 + Native Text |
| `medium` | 560 | 70 | 560 + Native Text |
| `high` | 1120 | 280 | 1120 + Native Text |
| `ultra_high` | 2240 | N/A | N/A |

## Choosing the right resolution

- **Default (`unspecified`):** Start with the default. It's tuned for a good balance of quality, latency, and cost for most common use cases.
- **`low`:** Use for scenarios where cost and latency are paramount, and fine-grained detail is less critical.
- **`medium` / `high`:** Increase the resolution when the task requires understanding intricate details within the media. This is often needed for complex visual analysis, chart reading, or dense document comprehension.
- **`ultra_high`** - Only available for per content item setting. Recommended for specific use cases such as computer use or where testing shows a clear enhancement over `high`.
- **Per-content-item control (Gemini 3):** Optimizes token usage. For example, in a prompt with multiple images, use `high` for a complex diagram and `low` or `medium` for simpler contextual images.

**Recommended settings**

The following lists the recommended media resolution settings for each supported media type.

| Media Type | Recommended Setting | Max Tokens | Usage Guidance |
| --- | --- | --- | --- |
| **Images** | `high` | 1120 | Recommended for most image analysis tasks to ensure maximum quality. |
| **PDFs** | `medium` | 560 | Optimal for document understanding; quality typically saturates at `medium`. Increasing to `high` rarely improves OCR results for standard documents. |
| **Video** (General) | `low` (or `medium`) | 70 (per frame) | **Note:** For video, `low` and `medium` settings are treated identically (70 tokens) to optimize context usage. This is sufficient for most action recognition and description tasks. |
| **Video** (Text-heavy) | `high` | 280 (per frame) | Required only when the use case involves reading dense text (OCR) or small details within video frames. |

Always test and evaluate the impact of different resolution settings on your application to find the best trade-off between quality, latency, and cost.

## Version compatibility summary

- Setting the `resolution` on individual content items is **exclusive to Gemini 3 models**.

## Next steps

- Learn more about the multimodal capabilities of Gemini API in the [image understanding](https://ai.google.dev/gemini-api/docs/interactions/image-understanding), [video understanding](https://ai.google.dev/gemini-api/docs/interactions/video-understanding) and [document understanding](https://ai.google.dev/gemini-api/docs/interactions/document-processing) guides.

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]]
