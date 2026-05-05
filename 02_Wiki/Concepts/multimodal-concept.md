---
name: Multimodal
type: concept
aliases: [Multimodal AI, Vision, Audio Input, Video Understanding, Cross-modal]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# Multimodal（多模态）

LLM 同时处理多种类型输入（文本、图像、音频、视频）的能力，使模型能理解和推理非文本信息，并将不同模态融合在同一对话上下文中。

## 核心机制

多模态模型通过专用编码器将不同模态的输入转换为统一的向量表示，再与文本 token 一起输入 transformer：

- **图像**：通过 Vision Encoder（如 ViT）将图像分割为 patch，每个 patch 映射为 token 序列
- **音频**：通过音频编码器（Whisper 架构等）转换为 token
- **视频**：按帧采样，每帧作为图像处理，辅以时间位置编码
- **文档/PDF**：转换为图像流逐页处理

**Token 计算**：不同模态的输入消耗不同数量的 token（通常远多于等量文字），直接影响成本和 context 利用率。

## 跨厂商实现

**Claude**：
- Vision 支持 JPEG、PNG、GIF、WebP；通过 `content` 数组中的 `image` 类型传入（base64 或 URL）
- PDF 支持（beta）：上传后按图像流处理
- 不原生支持音频/视频输入（截至 2026-05 主线 API）
- `vision` 参数控制图像处理质量（影响 token 消耗）

**OpenAI**：
- GPT-4o、GPT-4o mini 支持图像输入；`gpt-4o-audio-preview` 支持音频输入输出
- 图像：URL 或 base64，`detail: "low"/"high"/"auto"`；high detail 按 512×512 分块计算 token
- Whisper API：专用音频转文字
- GPT-Image-1：图像生成

**Gemini**：
- 原生多模态，支持文本、图像、视频、音频、PDF 混合输入
- Gemini 1.5 Pro：支持最长 2 小时视频 + 19 小时音频 + 1500 页文档
- `vision` / `audio` / `video` 统一通过 `parts` 数组传入
- `countTokens` API 可统计多模态输入的 token 数

## 关键参数 / API 表面

| 参数 | 说明 |
|---|---|
| `content[].type: "image_url"` (OpenAI) | 图像输入块 |
| `content[].type: "image"` (Claude) | 图像输入块（base64 或 URL） |
| `detail: "low"/"high"` (OpenAI) | 图像处理精度（影响 token 数） |
| `parts[].inline_data` (Gemini) | 多模态数据块 |
| `max_tokens` | 多模态输入通常消耗更多 token，需留足输出空间 |

## 使用场景

**适用**：
- 图表/截图解读（OCR + 语义理解）
- 文档/PDF 分析（发票、报告、表单）
- 视觉 QA（产品图片、界面截图）
- 音频转录和摘要（Gemini/OpenAI）
- 混合媒体内容生成

**注意**：
- 图像 token 成本高（尤其高分辨率），生产环境注意控制图像尺寸
- 隐私敏感图像避免传给云端 API
- 不同厂商支持的模态范围差异显著，选型时注意

## 相关

- [[Vision]] — Claude 视觉能力 entity 档案
- [[embeddings-concept]] — 多模态 embedding 扩展到图像向量空间
- [[Context-window]] — 图像占用大量 context token
- [[tokenization]] — 图像的 token 换算方式

## 出现来源

- [[Vision]] — Claude 视觉能力
- [[embeddings--bwc]] — embedding 多模态扩展
- [[vision--openai-docs]] — OpenAI GPT-4o/detail 参数
- [[models--openai-docs]] — GPT-4o audio preview / GPT-Image-1
- [[imagen--gemini-docs]] — Gemini 原生多模态 / parts 数组
- [[audio--gemini-docs]] — Gemini 音频支持
- [[image-generation--gemini-docs]] — Gemini 图像生成
