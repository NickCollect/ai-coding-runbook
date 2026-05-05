---
name: Gemini Files API
type: entity
vendor: Gemini
aliases: ["Files API", "client.files", "Gemini file upload"]
created: 2026-05-05
---

# Gemini Files API

Gemini 的文件上传管理接口，用于将多媒体文件（音频、图像、视频、文档）上传后在 `generateContent` 中引用；文件保留 48 小时后自动删除，每个项目最大存储 20GB（*待确认*）。

## 关键属性

| 属性 | 值 |
|---|---|
| Vendor | Google / Gemini |
| SDK 方法 | `client.files.upload()` |
| 文件保留时间 | **48 小时**（自动删除） |
| 存储上限 | *待确认*：20GB/项目 |
| 文件可见性 | 私有（仅上传者的 API key / project 可见） |

## 核心功能

### 何时需要使用 Files API

- 总请求大小（文件 + 文本 prompt + system instruction）**超过 100 MB** 时必须使用
- **PDF 超过 50 MB** 时必须使用
- 较小内容可直接以 inline bytes 传入，无需上传

### 支持文件类型

| 类型 | 格式 |
|---|---|
| 音频 | MP3、WAV、AIFF、AAC、OGG、FLAC |
| 图像 | PNG、JPEG、WEBP、HEIC、HEIF |
| 视频 | MP4、MPEG、MOV、AVI、FLV、MPG、WEBM、WMV、3GPP |
| 文档 | PDF、纯文本、HTML、CSS、Markdown、CSV、XML、RTF 等 |
| 代码文件 | 多种代码扩展名 |

### 文件状态

| 状态 | 说明 |
|---|---|
| `PROCESSING` | 已收到上传，处理中（视频需轮询至完成） |
| `ACTIVE` | 就绪，可用于 generateContent |
| `FAILED` | 处理失败 |

### 文件操作

| 操作 | SDK 方法 |
|---|---|
| 上传 | `client.files.upload(file=path)` |
| 获取元数据 | `client.files.get(name=file_name)` |
| 列出文件 | `client.files.list()` |
| 删除 | `client.files.delete(name=file_name)` |

## API 示例

```python
from google import genai
client = genai.Client()

# 上传文件
myfile = client.files.upload(file="path/to/sample.mp3")

# 在 generateContent 中引用
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=["Describe this audio clip", myfile]
)
print(response.text)

# 视频：轮询等待处理完成
import time
while video_file.state.name == 'PROCESSING':
    time.sleep(2.5)
    video_file = client.files.get(name=video_file.name)
```

```javascript
// JavaScript 上传
await ai.files.upload({ file: "path", config: { mimeType: "audio/mpeg" } });
```

## 与 Claude 对应物

[[Files-API]] — Anthropic 的 Files API，定位相同：上传文件后在 Messages API 中引用；Claude Files API 同样有 TTL（*待确认*：具体时限）。

## 出现来源

- [[files--gemini-docs]]

## 相关

- [[Gemini-API]] — generateContent 中通过 file URI 引用上传的文件
- [[Gemini-Context-Caching]] — Context Caching 也使用 File URI
- [[Files-API]] — Claude 对应物
