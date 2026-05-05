---
name: 多模态输入指南
type: synthesis
created: 2026-05-05
sources:
  - 01_Raw/platform.claude.com/docs/en/build-with-claude/vision.md
  - 01_Raw/platform.claude.com/docs/en/build-with-claude/files.md
  - 01_Raw/platform.claude.com/docs/en/build-with-claude/pdf-support.md
  - 01_Raw/docs.openai.com/docs/guides/vision.md
  - 02_Wiki/Summaries/vision--bwc.md
  - 02_Wiki/Summaries/vision--openai-docs.md
  - 02_Wiki/Summaries/image-understanding--gemini-docs.md
  - 02_Wiki/Summaries/audio--gemini-docs.md
  - 02_Wiki/Summaries/video-understanding--gemini-docs.md
  - 02_Wiki/Summaries/files--gemini-docs.md
  - 02_Wiki/Summaries/document-processing--gemini-docs.md
---

# 多模态输入指南

跨 Claude / OpenAI / Gemini 三家厂商的图像、PDF、音频、视频、文件上传能力综合对比。

---

## 1. 图像输入

### Claude

- **支持格式**：JPEG、PNG、GIF（仅首帧，不支持动画）、WebP
- **单图大小限制**：API 每张最大 **5 MB**；claude.ai 每张最大 **10 MB**
- **每次请求图片数量上限**：
  - API（200k context window 模型）：最多 **100** 张
  - API（其他模型，含 1M window）：最多 **600** 张
  - claude.ai：每条消息最多 **20** 张
- **尺寸限制**：单张最大 **8000×8000 px**；若单次请求超过 20 张，降为 **2000×2000 px**
- **原生最大分辨率**：
  - Claude Opus 4.7：最多 4784 tokens / 张，长边 ≤ 2576 px（高分辨率首发）
  - 其他模型：最多 1568 tokens / 张，长边 ≤ 1568 px
  - 超出尺寸的图像会自动等比缩放，再在右下角补零到 28px 整数倍
- **输入方式**：
  1. **base64**：`source: {type: "base64", media_type: "image/jpeg", data: "..."}`
  2. **URL**：`source: {type: "url", url: "https://..."}`
  3. **Files API**（beta）：`source: {type: "file", file_id: "file_xxx"}`
- **最佳实践**：图像放在文本前（image-then-text 结构）效果更好

### OpenAI

- **支持格式**：PNG、JPEG、WEBP、非动态 GIF
- **大小限制**：单次请求 payload 最大 **512 MB**，最多 **1500 张**图片
- **输入方式**：
  1. URL
  2. Base64 data URL
  3. Files API 的 File ID
- **`detail` 参数**（控制分辨率与成本）：

  | 参数值 | 说明 |
  |--------|------|
  | `low` | 快速低成本，缩至 512×512 |
  | `high` | 标准高保真 |
  | `original` | 最高精度，适合 computer-use；需 gpt-5.4+ |
  | `auto` | 默认，gpt-5.5 上等价于 `original` |

- **Token 计算**：
  - Patch-based（gpt-5.4-mini/nano、o4-mini）：32×32px patch，各有 patch budget
  - Tile-based（GPT-4o、GPT-4.1 等）：`low` 固定基础成本；`high` 缩至 2048×2048 后按 512px tile 计算

### Gemini

- **支持格式**：JPEG、PNG、WEBP、HEIC、HEIF、GIF、BMP（比 Claude/OpenAI 多 HEIC/HEIF/BMP）
- **输入方式**：
  1. **Inline bytes**：总请求 < 20 MB 时可直接内嵌，用 `types.Part.from_bytes(data=..., mime_type=...)`
  2. **Files API**：上传后引用 URI，适合大文件或多次复用
- **Token 计算**：根据分辨率浮动，可用 `count_tokens` 预估；无公开的固定公式（not documented in detail）

---

## 2. PDF 支持

### Claude

- **支持模型**：Claude 3.5+ 全系列，平台支持直连 API 和 Google Vertex AI，Amazon Bedrock 也支持（有特殊注意事项）
- **不支持**：加密 / 带密码的 PDF
- **限制**：

  | 限制项 | 数值 |
  |--------|------|
  | 最大请求大小 | 32 MB（含所有内容） |
  | 最大页数 / 请求 | 600 页（200k window 模型 100 页） |
  | 格式 | 标准 PDF，无加密 |

- **处理机制**：每页转为图像 + 提取文本，Claude 同时看图和文字（视觉 PDF）
- **Token 成本**：文本约 1,500–3,000 tokens / 页，图像成本额外按 vision 计算
- **输入方式**：
  1. URL：`source: {type: "url", url: "..."}`
  2. Base64：`source: {type: "base64", media_type: "application/pdf", data: "..."}`
  3. Files API：`source: {type: "file", file_id: "..."}`（推荐用于大/重复使用的 PDF）
- **Amazon Bedrock 注意**：通过 Converse API 时，须开启 citations 才能触发完整视觉 PDF 理解；否则退化为纯文字提取（~1,000 tokens for 3 pages vs 完整模式 ~7,000 tokens for 3 pages）

### OpenAI

raw 文件 `01_Raw/docs.openai.com/docs/guides/` 未包含独立 PDF 指南，**not documented** in available raw files。OpenAI 文件上传支持 `.pdf` 格式（通过 Files API），但详细 PDF 原生解析能力未在已采集文档中说明。

### Gemini

- **支持**：原生视觉 PDF 理解，可分析文本、图像、图表、表格、布局
- **页数上限**：最多 **1,000 页**
- **输入方式**：
  - 小文档（< 20 MB 请求）：直接 inline bytes
  - 大文档（> 50 MB）：须使用 Files API 上传
- **非 PDF 文件**：可传入但仅作纯文本处理，丧失图表/格式等视觉上下文

---

## 3. 音频输入

### Claude

Claude **不支持**音频输入（not documented）。当前仅支持文本、图像、PDF。

### OpenAI

`01_Raw/docs.openai.com/docs/guides/` 中未采集到独立 audio guide（git status 显示有 `realtime.md` 但不含音频输入指南）。Realtime API 支持音频流，但作为文本模型的音频输入能力 **not fully documented** in available raw files。

### Gemini

- **首个原生理解音频的 LLM 系列**（无需独立 speech-to-text 步骤）
- **支持格式**：MP3、WAV、AIFF、AAC、OGG、FLAC 等
- **计费**：**25 tokens / 秒**音频内容
- **输入方式**：
  - **Inline**（< 20 MB 总请求）：`types.Part.from_bytes(data=audio_bytes, mime_type="audio/mpeg")`
  - **Files API**：上传后引用，适合长音频
- **用途**：转录翻译、播客 Q&A、会议纪要、语音助手、音频分类

---

## 4. 视频输入

### Claude

Claude **不支持**视频输入（not documented）。

### OpenAI

raw files 中 **not documented**。

### Gemini

- **支持**：MP4、MPEG、MOV、AVI、FLV、MPG、WEBM、WMV、3GPP
- **Token 计算**：按帧采样（默认约 1 fps），长视频 = 大量 tokens
- **输入方式**：

  | 方式 | 最大大小 | 适用场景 |
  |------|----------|----------|
  | Files API | 20 GB（付费）/ 2 GB（免费） | 大文件、长视频（>10 min）、可复用 |
  | Cloud Storage 注册 | 每文件 2 GB，无存储上限 | 大文件、持久复用 |
  | Inline data | < 100 MB | 小文件、短视频（<1 min）、一次性 |
  | YouTube URL | 无大小限制 | 公开 YouTube 视频 |

- **能力**：视频描述/摘要、场景分割、时间戳 Q&A（"2:30 发生了什么？"）、多视频比较、字幕生成、内容审核

---

## 5. Files API 对比

三家厂商均提供 "upload once, reference many times" 的文件管理 API：

| 特性 | Claude Files API | OpenAI Files API | Gemini Files API |
|------|-----------------|------------------|------------------|
| 端点 | `POST /v1/files`（beta header 必须） | `POST /v1/files` | `POST /upload/v1beta/files` |
| Beta 标记 | 需要 `anthropic-beta: files-api-2025-04-14` | GA | GA |
| 单文件上限 | 500 MB | not documented in raw | 20 GB（视频付费账号） |
| 存储总量 | 500 GB / 组织 | not documented in raw | N/A（有 48h TTL） |
| 文件保留期 | **永久**（直到主动删除） | not documented in raw | **48 小时**后自动删除 |
| 支持文件类型 | PDF、文本、图像（JPEG/PNG/GIF/WebP）、数据集（code execution） | not documented in raw | 图像、音频、视频、文档（PDF/文本等） |
| 平台限制 | 不支持 Amazon Bedrock 和 Google Vertex AI | — | — |
| ZDR 资格 | **不符合** ZDR（数据按标准策略保留） | not documented | — |
| 文件 API 调用费 | **免费**（上传/列表/删除/元数据不计费） | not documented | — |
| 内容计费 | 内容用于消息时按 input tokens 计费 | not documented | 同样按 tokens 计费 |

### Claude Files API 使用模式

```python
# 上传
file = client.beta.files.upload(
    file=("document.pdf", open("doc.pdf", "rb"), "application/pdf")
)

# 引用（PDF/文本 用 document block）
{
  "type": "document",
  "source": {"type": "file", "file_id": file.id}
}

# 引用（图像 用 image block）
{
  "type": "image",
  "source": {"type": "file", "file_id": file.id}
}
```

---

## 6. 跨厂商能力对比表

| 能力 | Claude | OpenAI | Gemini |
|------|--------|--------|--------|
| **图像理解** | ✅ JPEG/PNG/GIF/WebP | ✅ PNG/JPEG/WEBP/GIF | ✅ JPEG/PNG/WEBP/HEIC/HEIF/GIF/BMP |
| **图像生成** | ❌ | ✅（gpt-image-2） | ✅（Imagen） |
| **PDF 原生理解** | ✅ Claude 3.5+（视觉+文本） | ❌ 未在 raw 中记录 | ✅ 最多 1000 页 |
| **音频输入** | ❌ | ❌ 未在 raw 中完整记录 | ✅ 多格式，25 tokens/秒 |
| **视频输入** | ❌ | ❌ 未在 raw 中记录 | ✅ 多格式，1 fps 采样 |
| **Files API** | ✅ beta，永久存储 | ✅（细节未在 raw 中记录） | ✅ GA，48h TTL |
| **URL 直接引用图像** | ✅ | ✅ | 不需要（inline bytes 或 Files API） |
| **高分辨率图像** | Opus 4.7 起 2576px 长边 | `detail: original`（gpt-5.4+） | 不同模型各异 |

---

## 7. 选型建议

**优先选 Gemini** 当：
- 需要处理音频（Gemini 是三者中唯一原生支持的）
- 需要处理视频（包括直接引用 YouTube URL）
- 需要处理超长 PDF（1000 页上限 > Claude 的 600 页）
- 图像格式含 HEIC/HEIF（iOS 照片默认格式）

**优先选 Claude** 当：
- 文档理解任务要求高，需要 citations 功能（搭配 PDF 支持）
- 需要在多轮长对话中反复引用同一批图像或文件（Files API 永久存储，base64 每轮都要重传）
- 高分辨率截图分析（Opus 4.7 的 2576px 高分辨率）

**优先选 OpenAI** 当：
- 任务需要图像生成与理解一体化（Responses API 同时支持）
- 需要 computer-use / 精确坐标定位（`detail: original` 模式）
- 生产系统已在 OpenAI 生态，文件管理 API 已 GA（Claude Files API 仍为 beta）

---

## 8. Vision Token 成本对比

**Claude（Sonnet 4.6 @ $3/MTok input）**：

| 图像尺寸 | Tokens | 成本/张 | 成本/千张 |
|----------|--------|---------|-----------|
| 200×200 | ~54 | ~$0.00016 | ~$0.16 |
| 1000×1000 | ~1334 | ~$0.004 | ~$4.00 |
| 1920×1080（自动缩放到 1568 px 上限） | ~1568 | ~$0.0047 | ~$4.70 |

**Claude Opus 4.7（@ $5/MTok input，高分辨率）**：

| 图像尺寸 | Tokens | 成本/张 | 成本/千张 |
|----------|--------|---------|-----------|
| 200×200 | ~54 | ~$0.00027 | ~$0.27 |
| 1920×1080 | ~2765 | ~$0.014 | ~$14.00 |
| 2000×1500 | ~4000 | ~$0.020 | ~$20.00 |

**OpenAI（tile-based，GPT-4o 系列）**：

| 精度 | Base tokens | Tile tokens（per 512px tile） |
|------|-------------|-------------------------------|
| `detail: low` | 85 | — |
| `detail: high` | 85 | 170/tile |

**Gemini**：图像 token 按分辨率浮动；音频固定 **25 tokens/秒**；视频按 1 fps 帧率折算图像 tokens。

> **成本控制建议**：
> - Claude：先压缩/缩放图像再上传；多轮对话用 Files API 避免重复传 base64
> - OpenAI：低精度任务选 `detail: low`；高精度时缩小图像减少 tile 数量
> - Gemini：PDF 大文件先用 Files API 上传，避免 inline 超过 20 MB 限制

---

## 出现来源

- `01_Raw/platform.claude.com/docs/en/build-with-claude/vision.md`
- `01_Raw/platform.claude.com/docs/en/build-with-claude/files.md`
- `01_Raw/platform.claude.com/docs/en/build-with-claude/pdf-support.md`
- `01_Raw/docs.openai.com/docs/guides/vision.md`
- `02_Wiki/Summaries/vision--bwc.md`
- `02_Wiki/Summaries/vision--openai-docs.md`
- `02_Wiki/Summaries/image-understanding--gemini-docs.md`
- `02_Wiki/Summaries/audio--gemini-docs.md`
- `02_Wiki/Summaries/video-understanding--gemini-docs.md`
- `02_Wiki/Summaries/files--gemini-docs.md`
- `02_Wiki/Summaries/document-processing--gemini-docs.md`
