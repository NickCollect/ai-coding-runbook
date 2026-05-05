---
type: entity
name: Vision
aliases: [vision / image understanding / multimodal images / image input]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

Claude 的图像理解能力 —— 在 Messages API content 里以 `image` block 输入，多图联合分析。

## 关键属性

- **限制**：claude.ai message 20 图；API 单请求 100 图（200k window）/ 600 图（1M window）；max 8000×8000 px（>20 图自动 reduce 到 2000×2000）；request size 32 MB cap [[vision--bwc]]
- **Token 估算**：`tokens ≈ (width × height) / 750` [[vision--bwc]]
- **Native max resolution**：Opus 4.7 高 resolution 4784 tokens / 2576 px long edge（其他模型 1568 tokens / 1568 px）；超出按比例 resize + pad 到 28 px 倍数 [[vision--bwc]]
- **Coordinates 输出**：bounding box 在 resized + padded 空间，client 自己 rescale 回原图 [[vision--bwc]]
- **Format 支持**：JPEG / PNG / GIF / WebP；动图只用首帧 [[vision--bwc]]
- **三种输入方式**：base64 (`source: {type: "base64", media_type, data}`) / URL (`source: {type: "url", url}`) / Files API file_id (`source: {type: "file", file_id}`) [[vision--bwc]] [[Files-API]]
- **图前文后**：image-then-text 排列效果最好 [[vision--bwc]]
- **Cost**（Sonnet 4.6 @ $3/MTok input）：1000×1000 ≈ $0.004/image；Opus 4.7 1920×1080 ≈ $0.014/image [[vision--bwc]]
- **PDF support 基于 Vision**：document block 复用同样 capability + 限制 [[PDF-support]]
- **Compatibility**：Vision 工作于 batch processing、prompt caching、tool use [[batch-processing--bwc]]
- **Computer-use-tool**：基于 vision 看屏幕截图 [[Computer-use-tool-API]]
- **API model 支持**：所有 active Claude models（Opus 4.7 高分辨率独有；其他模型限 1568 token / image）

## 出现来源

_16 summaries reference this entity_ —— 主要：
- [[vision--bwc]] / [[create--msg-api]] / [[messages-create--beta-api]]
- [[pdf-support--bwc]] / [[batch-processing--bwc]] / [[working-with-messages--bwc]]
- [[Files-API]]-related: [[files--bwc]] / [[files-upload--beta-api]]
- [[computer-use-tool--at]] / [[tool-use-overview--at]]

## 相关

- [[Messages-API]] —— Vision 是 Messages content 的子类
- [[PDF-support]] —— PDF 用 Vision 视觉处理 charts/tables
- [[Files-API]] —— file_id 可作为 image source
- [[Computer-use-tool-API]] —— screenshot vision
