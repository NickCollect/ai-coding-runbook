# Images and vision

<!-- source: https://platform.openai.com/docs/guides/vision -->

Recent language models can process image inputs and analyze them (vision). GPT Image models can use text and image inputs to create new images or edit existing ones.

## API endpoints for images

| API | Supported use cases |
|---|---|
| Responses API | Analyze images as input and/or generate images as output |
| Images API | Generate images as output, optionally using images as input |
| Chat Completions API | Analyze images as input to generate text or audio |

## Image generation

Use `gpt-image-2` for state-of-the-art image generation. Supports strong instruction following and contextual awareness with world knowledge.

```python
response = client.responses.create(
    model="gpt-4.1-mini",
    input="Generate an image of gray tabby cat hugging an otter with an orange scarf",
    tools=[{"type": "image_generation"}],
)
```

## Analyze images (vision)

Provide images as input via:
- Fully qualified URL to an image file
- Base64-encoded data URL
- File ID (from Files API)

Multiple images can be provided in a single request (each image counts as tokens).

```python
response = client.responses.create(
    model="gpt-4.1-mini",
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": "what's in this image?"},
            {"type": "input_image", "image_url": "https://..."},
        ],
    }],
)
```

## Image input requirements

**Supported formats**: PNG, JPEG, WEBP, non-animated GIF

**Size limits**: Up to 512 MB total payload, up to 1500 individual images per request

## Detail level (`detail` parameter)

| Detail level | Best for |
|---|---|
| `low` | Fast, low-cost. Model receives 512×512 version. |
| `high` | Standard high-fidelity understanding. |
| `original` | Large, dense, spatially sensitive, or computer-use images. Available on gpt-5.4+. |
| `auto` | Automatic selection (default). On gpt-5.5, equivalent to `original`. |

For computer use, localization, click-accuracy: use `"detail": "original"` on gpt-5.4+.

## Token costs

Patch-based tokenization (gpt-5.4-mini, gpt-5.4-nano, o4-mini):
- Images covered with 32×32px patches
- Each model has a patch budget (e.g., 1,536 patches)
- Multipliers by model: gpt-5.4-mini=1.62, gpt-5.4-nano=2.46, o4-mini=1.72

Tile-based tokenization (GPT-4o, GPT-4.1, o-series except o4-mini):
- `detail: low` = fixed base token cost
- `detail: high` = scale to 2048×2048, tile into 512px squares

| Model | Base tokens | Tile tokens |
|---|---|---|
| gpt-5/gpt-5-chat-latest | 70 | 140 |
| 4o, 4.1, 4.5 | 85 | 170 |
| 4o-mini | 2833 | 5667 |

## Limitations

- Medical images (CT scans etc.): not suitable for medical advice
- Non-Latin text in images: may not perform optimally
- Small text: enlarge for better readability; use `"detail": "original"` when available
- Rotation: may misinterpret rotated/upside-down text
- Precise spatial reasoning: struggles with exact positioning
- Counting: approximate counts only
- CAPTCHAs: blocked for safety reasons
- Panoramic/fisheye images: struggles
