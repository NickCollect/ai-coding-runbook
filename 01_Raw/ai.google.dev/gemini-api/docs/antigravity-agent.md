---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-CN
fetched_at: 2026-05-25T05:25:32.283963+00:00
title: "Antigravity Agent \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Antigravity Agent

Antigravity 智能体是 Gemini API 上的通用型托管智能体。只需一次 API 调用，您就可以获得一个智能体，该智能体可以在 Google 托管的您自己的安全 Linux 沙盒中进行推理、执行代码、管理文件和浏览网页。

它由 Gemini 3.5 Flash 提供支持，并使用与 Antigravity IDE 相同的 harness。可通过 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-cn) 和 [Google AI Studio](https://aistudio.google.com?hl=zh-cn) 使用。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## 功能

每次调用都可以预配 Linux 沙盒并启动工具使用循环。智能体会进行规划、执行操作、观察结果，并重复此过程，直到任务完成。

- **代码执行**： 运行 Bash、Python 和 Node.js 命令。安装软件包、运行测试、构建应用。
- **文件管理**： 在沙盒中读取、写入、修改、搜索和列出文件。文件在多次交互中保持不变。
- **网络访问**： Google 搜索和网址提取，用于获取数据。
- **上下文压缩**： 自动上下文压缩（在约 13.5 万个令牌时触发），以支持长时间运行的多轮会话，而不会丢失上下文或达到令牌限制。

如需了解多轮使用和流式传输，请参阅[快速入门](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=zh-cn)。

## 支持的工具

默认情况下，智能体可以访问 `code_execution`、`google_search` 和 `url_context`。当您指定 `environment` 参数时，文件系统工具会自动启用。只有在自定义或限制默认集时，您才需要指定 `tools` 参数。

| 工具 | 类型值 | 说明 |
| --- | --- | --- |
| 代码执行 | `code_execution` | 运行 shell 命令（bash、Python、Node），并捕获 stdout/stderr。 |
| Google 搜索 | `google_search` | 搜索公共网络。 |
| 网址上下文 | `url_context` | 提取和读取网页。 |
| 文件系统 | *（通过 `environment` 启用）* | 在沙盒中读取、写入、修改、搜索和列出文件。没有单独的工具类型；在设置 `environment` 时自动启用。 |

如需将智能体限制为特定工具，请仅传递所需的工具：

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Search for the latest AI research papers on reasoning and summarize them.",
    environment="remote",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"},
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Search for the latest AI research papers on reasoning and summarize them.",
    environment: "remote",
    tools: [
        { type: "google_search" },
        { type: "url_context" },
    ],
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Search for the latest AI research papers on reasoning and summarize them.",
    "environment": "remote",
    "tools": [
        {"type": "google_search"},
        {"type": "url_context"}
    ]
}'
```

## 多模态输入

Antigravity 智能体支持多模态输入。目前，仅支持 `text` 和 `image` 输入。图片必须以内嵌 base64 编码字符串 (`data`) 的形式提供。

### Python

```
import base64
from google import genai

client = genai.Client()

with open("path/to/chart.png", "rb") as f:
    image_bytes = f.read()

interaction_inline = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=[
        {"type": "text", "text": "Analyze this chart and summarize the trends."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png",
        },
    ],
    environment="remote",
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64Image = fs.readFileSync("path/to/chart.png", { encoding: "base64" });

const interactionInline = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: [
        { type: "text", text: "Analyze this chart and summarize the trends." },
        {
            type: "image",
            data: base64Image,
            mime_type: "image/png",
        },
    ],
    environment: "remote",
}, { timeout: 300000 });
```

### REST

```
BASE64_IMAGE=$(base64 -w0 /path/to/chart.png)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d "{
    \"agent\": \"antigravity-preview-05-2026\",
    \"input\": [
        {\"type\": \"text\", \"text\": \"Analyze this chart and summarize the trends.\"},
        {
            \"type\": \"image\",
            \"mime_type\": \"image/png\",
            \"data\": \"$BASE64_IMAGE\"
        }
    ],
    \"environment\": \"remote\"
}"
```

## 自定义智能体

您可以通过自定义 Antigravity 智能体的说明、工具和环境来扩展它。智能体支持文件系统原生自定义方法：您可以将 `AGENTS.md` 等文件装载到 `.agents/skills/` 下，以获取说明和技能，也可以在交互时内嵌传递配置。您可以内嵌迭代配置，然后在准备就绪后将其保存为托管智能体。

如需详细了解如何构建自定义智能体，请参阅[构建托管智能体](https://ai.google.dev/gemini-api/docs/custom-agents?hl=zh-cn)。

## 环境

每次调用都会创建或重复使用 Linux 沙盒。`environment` 参数采用三种形式：

| 姿势 | 说明 |
| --- | --- |
| `"remote"` | 使用默认设置预配新的沙盒。 |
| `"env_abc123"` | 按 ID 重复使用现有环境，保留所有文件和状态。 |
| `{...}` | 包含自定义来源和网络规则的完整 `EnvironmentConfig`。 |

如需详细了解来源（Git、GCS、内嵌）、网络、生命周期和资源限制，请参阅[环境](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-cn)。

## 适用范围和定价

Antigravity 智能体可通过 Google AI Studio 和 Gemini API 中的 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-cn) 以预览版形式提供。

定价遵循[随用随付模式](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn#pricing-for-agents)，具体取决于底层 Gemini 模型令牌和智能体使用的工具。与生成单个输出的标准聊天请求不同，Antigravity 交互是一种智能体工作流。单个请求会触发推理、工具执行、代码运行和文件管理的自主循环。

### 估算费用

费用因任务复杂性而异。智能体会自主确定需要多少工具调用、代码执行和文件操作。以下估算基于运行情况。

| 任务类别 | 输入令牌 | 输出令牌 | 一般费用 |
| --- | --- | --- | --- |
| **研究和信息合成** | 10 万–50 万 | 1 万–4 万 | $0.30–$1.00 |
| **文档和内容生成** | 10 万–50 万 | 1.5 万–5 万 | $0.30–$1.30 |
| **流程和系统设计** | 10 万–40 万 | 1 万–3 万 | $0.25–$0.80 |
| **数据处理和分析** | 30 万–300 万 | 3 万–15 万 | $0.70–$3.25 |

通常会缓存 50%–70% 的输入令牌。包含许多工具调用的复杂智能体工作流在一次交互中可能会累积 300 万–500 万个令牌，费用高达约 5 美元。

在预览版期间，**环境计算** （CPU、内存、沙盒执行）**不会收费** 。

## 限制

- **预览版状态**： Antigravity 智能体和 Interactions API 均为预览版。功能和架构可能会发生变化。
- **不支持的生成配置**： 以下参数不受支持，并返回 400 错误：`temperature`、`top_p`、`top_k`、`stop_sequences`、`max_output_tokens`。
- **结构化输出**： Antigravity 智能体不支持结构化输出。
- **不可用的工具**： 尚不支持 `file_search`、`computer_use`、`google_maps`、`function_calling` 和 `mcp`。
- **文件系统工具**： 目前没有文件系统工具。它是 `environment` 的一部分。
- **背景**： 智能体不支持使用 `background=True`，并且需要 `store=True`。
- **不支持的多模态类型。**目前不支持音频、视频和文档输入。仅允许使用文本和图片。

## 后续步骤

- [快速入门](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=zh-cn)：多轮对话和流式传输。
- [构建自定义智能体](https://ai.google.dev/gemini-api/docs/custom-agents?hl=zh-cn)：自定义说明、技能和保存智能体。
- [环境](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-cn)：沙盒配置、来源、网络。
- [Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=zh-cn)：长篇研究任务。
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-cn)：底层 API。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-20。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-20。"],[],[]]
