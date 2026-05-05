---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/vision.md
source_url: https://platform.openai.com/docs/guides/vision
title: "OpenAI — Images and Vision"
summarized_at: 2026-05-05
entities_referenced: [Vision]
concepts_referenced: []
---

## 核心要点

OpenAI 支持图像理解（vision）和图像生成，通过不同 API 端点访问。

### API 端点对应关系

| API | 支持用途 |
|---|---|
| Responses API | 图像作为输入分析 + 图像作为输出生成 |
| Images API | 图像生成（可选图像输入） |
| Chat Completions API | 图像输入 → 文本/音频输出 |

### 图像生成

使用 `gpt-image-2`（state-of-the-art），在 Responses API 中通过 `image_generation` tool 调用。

### 图像理解（Vision）示例

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

输入方式：URL / Base64 data URL / Files API 的 File ID

### 输入要求

- **格式**：PNG、JPEG、WEBP、非动态 GIF
- **大小限制**：单次请求最大 512 MB，最多 1500 张图片

### `detail` 参数

| 级别 | 适用场景 |
|---|---|
| `low` | 快速、低成本，给模型 512×512 版本 |
| `high` | 标准高保真理解 |
| `original` | 大图、密集、空间敏感、computer-use；需 gpt-5.4+ |
| `auto` | 自动选择（默认），gpt-5.5 上等价于 `original` |

### Token 计算

- **Patch-based**（gpt-5.4-mini/nano、o4-mini）：32×32px patch，有 patch budget
- **Tile-based**（GPT-4o、GPT-4.1、o-series 除 o4-mini）：低精度固定成本；高精度按 512px tile 计算

### 已知局限

- 医疗图像不适合医疗建议
- 非拉丁文字识别性能有限
- 精确空间推理、精确计数能力弱
- CAPTCHA 出于安全原因被阻止
