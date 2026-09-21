---
source_url: https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-CN
fetched_at: 2026-09-21T05:47:54.930041+00:00
title: "Gemini API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-cn)

# Gemini API

借助 Gemini API，您可以快速将提示词转化为实际应用，并利用 Gemini、Veo、Nano Banana 等工具实现更多功能。借助该 SDK，您可以将这些生成式模型集成到应用中，以生成文本和图片、分析多模态输入内容，以及构建对话式代理。

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3.8-flash",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3.8-flash", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

[开始构建](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)

---

## 认识这些模型

[查看全部](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn)

[auto\_awesome
Gemini 3.1 Pro
新

Google 最智能的模型，也是全球领先的多模态理解能力模型，建立在前沿推理技术基础上。](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-cn)
[spark
Gemini 3.6 Flash
新

Google 推出的最新模型，在速度和智能性之间实现了平衡，可在智能体和多模态任务中提供出色的性能。](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=zh-cn)
[spark
Gemini 3.5 Flash

以远低于大型模型的成本，实现可与 Frontier 级模型相媲美的性能。](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=zh-cn)
[spark
Gemini 3.5 Flash-Lite
新

经济高效的模型，专为大体量、成本敏感的子智能体任务而设计，并针对低延迟高吞吐量进行了优化。](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=zh-cn)
[spark
Gemini 3.1 Flash-Lite

这款模型具有 Gemini 3 系列的性能和质量，可处理大体量的成本敏感型流量。](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-cn)
[spark
Gemini 3 Flash

以远低于大型模型的成本，实现可与 Frontier 级模型相媲美的性能。](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-cn)
[🍌
Nano Banana 2 和 Nano Banana Pro

前沿的图片生成和编辑模型。](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)
[video\_library
Veo 3.1

我们前沿的视频生成模型，支持原生音频。](https://ai.google.dev/gemini-api/docs/video?hl=zh-cn)
[spark
Gemini Robotics

一种视觉-语言模型 (VLM)，可将 Gemini 的智能体功能引入机器人技术，并支持在物理世界中进行高级推理。](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=zh-cn)

## 探索功能

[imagesmode

原生图片生成 (Nano Banana)

使用 Gemini 2.5 Flash Image 原生生成和编辑高度情境化的图片。](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)
[article

长上下文

向 Gemini 模型输入数百万个 token，并从非结构化的图片、视频和文档中获取理解。](https://ai.google.dev/gemini-api/docs/long-context?hl=zh-cn)
[code

结构化输出

限制 Gemini 以 JSON（一种适合自动处理的结构化数据格式）进行回答。](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)
[functions

函数调用

通过将 Gemini 连接到外部 API 和工具来构建智能体工作流。](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)
[videocam

使用 Veo 3.1 生成视频

借助我们前沿的模型，根据文本或图片提示创作高品质视频内容。](https://ai.google.dev/gemini-api/docs/video?hl=zh-cn)
[android\_recorder

使用 Live API 的语音智能体

使用 Live API 构建实时语音应用和代理。](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-cn)
[build

工具

通过 Google 搜索、网址上下文、Google 地图、代码执行和计算机使用等内置工具，将 Gemini 与世界相连。](https://ai.google.dev/gemini-api/docs/tools?hl=zh-cn)
[stacks

文档理解

处理最多 1,000 页的 PDF 文件（支持完整的多模态理解能力）或其他基于文本的文件类型。](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-cn)
[cognition\_2

思考

了解思维能力如何改进复杂任务和代理的推理能力。](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)

[Google AI Studio

测试提示、管理 API 密钥、监控用量和构建原型。](https://aistudio.google.com?hl=zh-cn)
[group

开发者社区

向其他开发者和 Google 工程师提问并寻求解决方案。](https://discuss.ai.google.dev/c/gemini-api/4?hl=zh-cn)
[menu\_book

API 参考文档

如需详细了解 Gemini API，请参阅官方参考文档。](https://ai.google.dev/api?hl=zh-cn)
[sensors

状态

查看 Gemini API、Google AI Studio 和我们的模型服务的状态。](https://aistudio.google.com/status?hl=zh-cn)

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-14。

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-14。"],[],[]]
