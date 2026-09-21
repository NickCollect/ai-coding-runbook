---
source_url: https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-CN
fetched_at: 2026-09-21T05:47:14.664890+00:00
title: "Gemini Deep Research \u667a\u80fd\u4f53 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Gemini Deep Research 智能体

Gemini Deep Research 智能体可自主规划、执行和整合多步骤研究任务。在 Gemini 的支持下，它能够驾驭复杂的信息环境，生成详细且包含引用的报告。借助新功能，您可以与智能体协作规划，使用 MCP 服务器连接到外部工具，添加可视化内容（例如图表和图形），以及直接提供文档作为输入内容。

研究任务涉及迭代搜索和阅读，可能需要几分钟才能完成。您必须使用[后台执行](https://ai.google.dev/gemini-api/docs/background-execution?hl=zh-cn)（设置 `background=true`）来异步运行代理并轮询结果或流式传输更新。如需了解详情，请参阅[处理长时间运行的任务](#long-running-tasks)。

以下示例展示了如何在后台启动研究任务并轮询结果。

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.steps[-1].content[0].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.steps.at(-1).content[0].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import java.util.Collections;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Research the history of Google TPUs."))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Research started: " + interaction.id().orElse(""));

while (true) {
  interaction =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(interaction.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(interaction.status().orElse(null))) {
    System.out.println(interaction.outputText().orElse(""));
    break;
  } else if (InteractionStatus.FAILED.equals(interaction.status().orElse(null))) {
    System.out.println("Research failed: " + interaction.errors().orElse(Collections.emptyList()));
    break;
  }
  Thread.sleep(10000);
}
```

### REST

```
# 1. Start the research task
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

## 支持的版本

Deep Research 智能体分为两个版本：

- **深度研究** (`deep-research-preview-04-2026`)：旨在提高速度和效率，非常适合流式传输回客户端界面。
- **Deep Research Max** (`deep-research-max-preview-04-2026`)：自动收集和整合上下文信息，实现最全面的研究。

## 协作规划

通过协作式规划，您可以在代理开始工作之前控制研究方向，方法是在执行之前查看和完善研究计划。启用后，代理会返回建议的研究计划，而不是立即执行。然后，您可以通过多轮对话查看、修改或批准该计划。

### 第 1 步：申请方案

在第一次互动中设置 `collaborative_planning=True`。智能体返回的是研究计划，而不是完整报告。

### Python

```
from google import genai

client = genai.Client()

# First interaction: request a research plan
plan_interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Do some research on Google TPUs.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    background=True,
)

# Wait for and retrieve the plan
while (result := client.interactions.get(id=plan_interaction.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const planInteraction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Do some research on Google TPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    background: true
});

let result;
while ((result = await client.interactions.get(planInteraction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();

// First interaction: request a research plan
CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Do some research on Google TPUs."))
        .agentConfig(
            DeepResearchAgentConfig.builder()
                .thinkingSummaries(ThinkingSummaries.AUTO)
                .collaborativePlanning(true)
                .build())
        .background(true)
        .build();

Interaction planInteraction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// Wait for and retrieve the plan
Interaction result;
while (true) {
  result =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(planInteraction.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(result.status().orElse(null))) {
    break;
  }
  Thread.sleep(5000);
}
System.out.println(result.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Do some research on Google TPUs.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "background": true
}'
```

### 第 2 步：优化方案（可选）

使用 `previous_interaction_id` 继续对话并迭代计划。按住 `collaborative_planning=True` 可保持在规划模式下。

### Python

```
# Second interaction: refine the plan
refined_plan = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    previous_interaction_id=plan_interaction.id,
    background=True,
)

while (result := client.interactions.get(id=refined_plan.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const refinedPlan = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Focus more on the differences between Google TPUs and competitor hardware, and less on the history.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    previous_interaction_id: planInteraction.id,
    background: true
});

let result;
while ((result = await client.interactions.get(refinedPlan.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();
String planInteractionId = "PLAN_INTERACTION_ID";

// Second interaction: refine the plan
CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(
            InteractionsInput.of(
                "Focus more on the differences between Google TPUs and competitor hardware, and less on the history."))
        .agentConfig(
            DeepResearchAgentConfig.builder()
                .thinkingSummaries(ThinkingSummaries.AUTO)
                .collaborativePlanning(true)
                .build())
        .previousInteractionId(planInteractionId)
        .background(true)
        .build();

Interaction refinedPlan =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

Interaction result;
while (true) {
  result =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(refinedPlan.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(result.status().orElse(null))) {
    break;
  }
  Thread.sleep(5000);
}
System.out.println(result.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

### 第 3 步：批准并执行

设置 `collaborative_planning=False`（或省略此参数）以批准计划并开始研究。

### Python

```
# Third interaction: approve the plan and kick off research
final_report = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Plan looks good!",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": False,
    },
    previous_interaction_id=refined_plan.id,
    background=True,
)

while (result := client.interactions.get(id=final_report.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const finalReport = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Plan looks good!',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: false
    },
    previous_interaction_id: refinedPlan.id,
    background: true
});

let result;
while ((result = await client.interactions.get(finalReport.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();
String refinedPlanId = "REFINED_PLAN_ID";

// Third interaction: approve the plan and kick off research
CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Plan looks good!"))
        .agentConfig(
            DeepResearchAgentConfig.builder()
                .thinkingSummaries(ThinkingSummaries.AUTO)
                .collaborativePlanning(false)
                .build())
        .previousInteractionId(refinedPlanId)
        .background(true)
        .build();

Interaction finalReport =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

Interaction result;
while (true) {
  result =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(finalReport.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(result.status().orElse(null))) {
    break;
  }
  Thread.sleep(5000);
}
System.out.println(result.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Plan looks good!",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": false
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

## 可视化

当 `visualization` 设置为 `"auto"` 时，智能体可以生成图表、图形和其他视觉元素来支持其研究发现。
生成的图片包含在回答步骤中，并以 `image` delta 的形式进行流式传输。为获得最佳结果，请在查询中明确要求生成图文内容，例如“包含显示随时间变化的趋势的图表”或“生成比较市场份额的图表”。将 `visualization` 设置为 `"auto"` 可启用此功能，但智能体仅在提示要求时生成视觉效果。

### Python

```
import base64
import time

from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Analyze global semiconductor market trends. Include graphics showing market share changes.",
    agent_config={
        "type": "deep-research",
        "visualization": "auto",
    },
    background=True,
)

print(f"Research started: {interaction.id}")

while (result := client.interactions.get(id=interaction.id)).status != "completed":
    time.sleep(5)

for step in result.steps:
    if step.type == "model_output":
        for content_item in step.content:
            if content_item.type == "text":
                print(content_item.text)
            elif content_item.type == "image" and content_item.data:
                image_bytes = base64.b64decode(content_item.data)
                print(f"Received image: {len(image_bytes)} bytes")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Analyze global semiconductor market trends. Include graphics showing market share changes.',
    agent_config: {
        type: 'deep-research',
        visualization: 'auto'
    },
    background: true
});

console.log(`Research started: ${interaction.id}`);

let result;
while ((result = await client.interactions.get(interaction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}

for (const step of result.steps) {
    if (step.type === 'model_output') {
        for (const contentItem of step.content) {
            if (contentItem.type === 'text') {
                console.log(contentItem.text);
            } else if (contentItem.type === 'image' && contentItem.data) {
                console.log(`[Image Output: ${contentItem.data.substring(0, 20)}...]`);
            }
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.Visualization;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import java.util.Base64;
import java.util.Collections;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(
            InteractionsInput.of(
                "Analyze global semiconductor market trends. Include graphics showing market share changes."))
        .agentConfig(DeepResearchAgentConfig.builder().visualization(Visualization.AUTO).build())
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Research started: " + interaction.id().orElse(""));

Interaction result;
while (true) {
  result =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(interaction.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(result.status().orElse(null))) {
    break;
  }
  Thread.sleep(5000);
}

for (Step step : result.steps().orElse(Collections.emptyList())) {
  if (step instanceof ModelOutputStep) {
    for (Content contentItem : ((ModelOutputStep) step).content().orElse(Collections.emptyList())) {
      if (contentItem instanceof TextContent) {
        System.out.println(((TextContent) contentItem).text().orElse(""));
      } else if (contentItem instanceof ImageContent) {
        ImageContent img = (ImageContent) contentItem;
        if (img.data().isPresent()) {
          byte[] imageBytes = Base64.getDecoder().decode(img.data().get());
          System.out.println("Received image: " + imageBytes.length + " bytes");
        }
      }
    }
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Analyze global semiconductor market trends. Include graphics showing market share changes.",
    "agent_config": {
        "type": "deep-research",
        "visualization": "auto"
    },
    "background": true
}'
```

## 支持的工具

Deep Research 支持多种内置工具和外部工具。默认情况下（未提供 `tools` 参数时），代理可以访问 Google 搜索、网址上下文和代码执行功能。您可以明确指定工具来限制或扩展代理的功能。

| 工具 | 类型值 | 说明 |
| --- | --- | --- |
| Google 搜索 | `google_search` | 在公共网络中搜索。默认处于启用状态。 |
| 网址上下文 | `url_context` | 阅读和总结网页内容。默认处于启用状态。 |
| 代码执行 | `code_execution` | 执行代码以进行计算和数据分析。默认处于启用状态。 |
| MCP 服务器 | `mcp_server` | 连接到远程 MCP 服务器以访问外部工具。 |
| 文件搜索 | `file_search` | 搜索您上传的文档语料库。 |

### Google 搜索

明确启用 Google 搜索作为唯一工具：

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="What are the latest developments in quantum computing?",
    tools=[{"type": "google_search"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'What are the latest developments in quantum computing?',
    tools: [{ type: 'google_search' }],
    background: true
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("What are the latest developments in quantum computing?"))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "What are the latest developments in quantum computing?",
    "tools": [{"type": "google_search"}],
    "background": true
}'
```

### 网址上下文

让代理能够读取和总结特定网页的内容：

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Summarize the content of https://www.wikipedia.org/.",
    tools=[{"type": "url_context"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Summarize the content of https://www.wikipedia.org/.',
    tools: [{ type: 'url_context' }],
    background: true
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.URLContext;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Summarize the content of https://www.wikipedia.org/."))
        .tools(Arrays.asList(URLContext.builder().build()))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Summarize the content of https://www.wikipedia.org/.",
    "tools": [{"type": "url_context"}],
    "background": true
}'
```

### 代码执行

允许代理执行代码以进行计算和数据分析：

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Calculate the 50th Fibonacci number.",
    tools=[{"type": "code_execution"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Calculate the 50th Fibonacci number.',
    tools: [{ type: 'code_execution' }],
    background: true
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Calculate the 50th Fibonacci number."))
        .tools(Arrays.asList(CodeExecution.builder().build()))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Calculate the 50th Fibonacci number.",
    "agent": "deep-research-preview-04-2026",
    "tools": [{"type": "code_execution"}],
    "background": true
}'
```

### MCP 服务器

连接到远程 MCP 服务器，以便智能体访问外部工具和服务。

在工具配置中提供服务器 `name` 和 `url`。您还可以传递身份验证凭据，并限制代理可以调用的工具。

| 字段 | 类型 | 是否必需 | 说明 |
| --- | --- | --- | --- |
| `type` | `string` | 是 | 必须为 `"mcp_server"`。 |
| `name` | `string` | 否 | MCP 服务器的显示名称。 |
| `url` | `string` | 否 | MCP 服务器端点的完整网址。 |
| `headers` | `object` | 否 | 作为 HTTP 标头随每个请求一起发送到服务器的键值对（例如身份验证令牌）。 |
| `allowed_tools` | `array` | 否 | 限制智能体可调用的服务器工具。 |

#### 基本用法

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Check the status of my last server deployment.",
    tools=[
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"},
        }
    ],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Check the status of my last server deployment.',
    tools: [
        {
            type: 'mcp_server',
            name: 'Deployment Tracker',
            url: 'https://mcp.example.com/mcp',
            headers: { Authorization: 'Bearer my-token' }
        }
    ],
    background: true
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.MCPServer;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Check the status of my last server deployment."))
        .tools(
            Arrays.asList(
                MCPServer.builder()
                    .name("Deployment Tracker")
                    .url("https://mcp.example.com/mcp")
                    .headers(Collections.singletonMap("Authorization", "Bearer my-token"))
                    .build()))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Check the status of my last server deployment.",
    "tools": [
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"}
        }
    ],
    "background": true
}'
```

### 文件搜索

使用[文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn)工具授予智能体对您自有数据的访问权限。

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Compare our 2025 fiscal year report against current public web news.",
    agent="deep-research-preview-04-2026",
    background=True,
    tools=[
        {
            "type": "file_search",
            "file_search_store_names": ['fileSearchStores/my-store-name']
        }
    ]
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Compare our 2025 fiscal year report against current public web news.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    tools: [
        { type: 'file_search', file_search_store_names: ['fileSearchStores/my-store-name'] },
    ]
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(
            InteractionsInput.of(
                "Compare our 2025 fiscal year report against current public web news."))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList("fileSearchStores/my-store-name"))
                    .build()))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Compare our 2025 fiscal year report against current public web news.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "tools": [
        {"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]},
    ]
}'
```

## 可操纵性和格式设置

您可以在提示中提供具体的格式设置说明，从而引导代理的输出。这样，您就可以将报告划分为特定部分和子部分，添加数据表格，或针对不同受众群体调整语气（例如“技术”“高管”“随意”）。

在输入文本中明确定义所需的输出格式。

### Python

```
prompt = """
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
"""

interaction = client.interactions.create(
    input=prompt,
    agent="deep-research-preview-04-2026",
    background=True
)
```

### JavaScript

```
const prompt = `
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
`;

const interaction = await client.interactions.create({
    input: prompt,
    agent: 'deep-research-preview-04-2026',
    background: true,
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

String prompt =
    "Research the competitive landscape of EV batteries.\n\n"
        + "Format the output as a technical report with the following structure:\n"
        + "1. Executive Summary\n"
        + "2. Key Players (Must include a data table comparing capacity and chemistry)\n"
        + "3. Supply Chain Risks";

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of(prompt))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of EV batteries.\n\nFormat the output as a technical report with the following structure: \n1. Executive Summary\n2. Key Players (Must include a data table comparing capacity and chemistry)\n3. Supply Chain Risks",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'
```

## 多模态输入

Deep Research 支持多模态输入，包括图片和文档 (PDF)，让智能体能够分析视觉内容并根据提供的输入进行情境化网络研究。

### Python

```
import time
from google import genai

client = genai.Client()

prompt = """Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground."""

interaction = client.interactions.create(
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"
        }
    ],
    agent="deep-research-preview-04-2026",
    background=True
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.steps[-1].content[0].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const prompt = `Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground.`;

const interaction = await client.interactions.create({
    input: [
        { type: 'text', text: prompt },
        {
            type: 'image',
            mime_type: "image/jpeg",
            uri: 'https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg'
        }
    ],
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.steps.at(-1).content[0].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import java.util.Arrays;
import java.util.Collections;

Client client = new Client();

String prompt =
    "Analyze the interspecies dynamics and behavioral risks present "
        + "in the provided image of the African watering hole. Specifically, investigate "
        + "the symbiotic relationship between the avian species and the pachyderms "
        + "shown, and conduct a risk assessment for the reticulated giraffes based on "
        + "their drinking posture relative to the specific predator visible in the "
        + "foreground.";

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    TextContent.builder().text(prompt).build(),
                    ImageContent.builder()
                        .mimeType(ImageContentMimeType.IMAGE_JPEG)
                        .uri(
                            "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg")
                        .build())))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Research started: " + interaction.id().orElse(""));

while (true) {
  interaction =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(interaction.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(interaction.status().orElse(null))) {
    System.out.println(interaction.outputText().orElse(""));
    break;
  } else if (InteractionStatus.FAILED.equals(interaction.status().orElse(null))) {
    System.out.println("Research failed: " + interaction.errors().orElse(Collections.emptyList()));
    break;
  }
  Thread.sleep(10000);
}
```

### REST

```
# 1. Start the research task with image input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": [
        {"type": "text", "text": "Analyze the interspecies dynamics and behavioral risks present in the provided image of the African watering hole. Specifically, investigate the symbiotic relationship between the avian species and the pachyderms shown, and conduct a risk assessment for the reticulated giraffes based on their drinking posture relative to the specific predator visible in the foreground."},
        {"type": "image", "mime_type": "image/jpeg", "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"}
    ],
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

### 文档理解

文档理解功能可让您直接将文档作为多模态输入传递。
智能体分析提供的文档，并根据文档内容进行研究。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input=[
        {"type": "text", "text": "What is this document about?"},
        {
            "type": "document",
            "uri": "https://arxiv.org/pdf/1706.03762",
            "mime_type": "application/pdf",
        },
    ],
    background=True,
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: [
        { type: 'text', text: 'What is this document about?' },
        {
            type: 'document',
            uri: 'https://arxiv.org/pdf/1706.03762',
            mime_type: 'application/pdf'
        }
    ],
    background: true
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    TextContent.builder().text("What is this document about?").build(),
                    DocumentContent.builder()
                        .uri("https://arxiv.org/pdf/1706.03762")
                        .mimeType(DocumentContentMimeType.APPLICATION_PDF)
                        .build())))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### REST

```
# 1. Start the research task with document input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": [
        {"type": "text", "text": "What is this document about?"},
        {"type": "document", "uri": "https://arxiv.org/pdf/1706.03762", "mime_type": "application/pdf"}
    ],
    "background": true
}'
```

## 处理长时间运行的任务

Deep Research 是一个多步骤流程，包括规划、搜索、阅读和撰写。此周期通常会超出同步 API 调用的标准超时限制。

必须使用代理才能使用 `background=True`。该 API 会立即返回部分 `Interaction` 对象。您可以使用 `id` 属性检索用于轮询的互动。互动状态将从 `in_progress` 转换为 `completed` 或 `failed`。如需查看有关管理后台任务的全面指南，请参阅[后台执行](https://ai.google.dev/gemini-api/docs/background-execution?hl=zh-cn)。

### 流式

Deep Research 支持流式传输，可实时接收研究进度更新，包括思路总结、文本输出和生成的图片。您必须设置 `stream=True` 和 `background=True`。

如需接收中间推理步骤（想法）和进度更新，您必须通过在 `agent_config` 中将 `thinking_summaries` 设置为 `"auto"` 来启用**思考总结**。如果不设置此值，流可能只会提供最终结果。

#### 数据流事件类型

| 事件类型 | 增量类型 | 说明 |
| --- | --- | --- |
| `step.delta` | `thought` | 智能体的中间推理步骤。 |
| `step.delta` | `text` | 最终文本输出的一部分。 |
| `step.delta` | `image` | 生成的图片（采用 base64 编码）。 |

以下示例启动了一项研究任务，并处理了具有自动重新连接功能的流。它会跟踪 `interaction_id` 和 `last_event_id`，以便在连接断开（例如，在 600 秒超时后）时，可以从中断处继续。

### Python

```
from google import genai

client = genai.Client()

interaction_id = None
last_event_id = None
is_complete = False

def process_stream(stream):
    global interaction_id, last_event_id, is_complete
    for event in stream:
        if event.event_type == "interaction.created":
            interaction_id = event.interaction.id
        if event.event_id:
            last_event_id = event.event_id
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                print(event.delta.text, end="", flush=True)
            elif event.delta.type == "thought":
                print(f"Thought: {event.delta.text}", flush=True)
        elif event.event_type in ("interaction.completed", "interaction.error"):
            is_complete = True

stream = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
    stream=True,
    agent_config={"type": "deep-research", "thinking_summaries": "auto"},
)
process_stream(stream)

# Reconnect if the connection drops
while not is_complete and interaction_id:
    status = client.interactions.get(interaction_id)
    if status.status != "in_progress":
        break
    stream = client.interactions.get(
        id=interaction_id, stream=True, last_event_id=last_event_id,
    )
    process_stream(stream)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interactionId;
let lastEventId;
let isComplete = false;

async function processStream(stream) {
    for await (const event of stream) {
        if (event.type === 'interaction.created') {
            interactionId = event.interaction.id;
        }
        if (event.event_id) lastEventId = event.event_id;
        if (event.type === 'step.delta') {
            if (event.delta.type === 'text') {
                process.stdout.write(event.delta.text);
            } else if (event.delta.type === 'thought') {
                console.log(`Thought: ${event.delta.text}`);
            }
        } else if (['interaction.completed', 'interaction.error'].includes(event.type)) {
            isComplete = true;
        }
    }
}

const stream = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    stream: true,
    agent_config: { type: 'deep-research', thinking_summaries: 'auto' },
});
await processStream(stream);

// Reconnect if the connection drops
while (!isComplete && interactionId) {
    const status = await client.interactions.get(interactionId);
    if (status.status !== 'in_progress') break;
    const resumeStream = await client.interactions.get(interactionId, {
        stream: true, last_event_id: lastEventId,
    });
    await processStream(resumeStream);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.ErrorEvent;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionCompletedEvent;
import com.google.genai.gaos.models.interactions.InteractionCreatedEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.StepDelta;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.TextDelta;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.ThoughtSummaryDelta;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.utils.EventStream;

class StreamProcessor {
  String interactionId = null;
  String lastEventId = null;
  boolean isComplete = false;

  void processStream(EventStream<InteractionSSEStreamEvent> stream) {
    for (InteractionSSEStreamEvent streamEvent : stream) {
      InteractionSSEEvent event = streamEvent.data().orElse(null);
      if (event instanceof InteractionCreatedEvent) {
        InteractionCreatedEvent created = (InteractionCreatedEvent) event;
        interactionId = created.interaction().flatMap(i -> i.id()).orElse(null);
        if (created.eventId().isPresent()) {
          lastEventId = created.eventId().get();
        }
      } else if (event instanceof StepDelta) {
        StepDelta stepDelta = (StepDelta) event;
        if (stepDelta.eventId().isPresent()) {
          lastEventId = stepDelta.eventId().get();
        }
        if (stepDelta.delta().isPresent()) {
          if (stepDelta.delta().get() instanceof TextDelta) {
            System.out.print(((TextDelta) stepDelta.delta().get()).text().orElse(""));
            System.out.flush();
          } else if (stepDelta.delta().get() instanceof ThoughtSummaryDelta) {
            ThoughtSummaryDelta thought = (ThoughtSummaryDelta) stepDelta.delta().get();
            Content content = thought.content().orElse(null);
            if (content instanceof TextContent) {
              System.out.println("Thought: " + ((TextContent) content).text().orElse(""));
            }
          }
        }
      } else if (event instanceof InteractionCompletedEvent || event instanceof ErrorEvent) {
        isComplete = true;
      }
    }
  }
}

Client client = new Client();
StreamProcessor processor = new StreamProcessor();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Research the history of Google TPUs."))
        .background(true)
        .stream(true)
        .agentConfig(
            DeepResearchAgentConfig.builder().thinkingSummaries(ThinkingSummaries.AUTO).build())
        .build();

try (EventStream<InteractionSSEStreamEvent> stream =
    client.interactions.create(CreateInteractionRequestBody.of(params)).events()) {
  processor.processStream(stream);
}

// Reconnect if the connection drops
while (!processor.isComplete && processor.interactionId != null) {
  Interaction status =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(processor.interactionId).build())
          .interaction()
          .get();
  if (!InteractionStatus.IN_PROGRESS.equals(status.status().orElse(null))) {
    break;
  }
  try (EventStream<InteractionSSEStreamEvent> stream =
      client.interactions
          .get(
              GetInteractionByIdRequest.builder()
                  .id(processor.interactionId)
                  .stream(true)
                  .lastEventId(processor.lastEventId)
                  .build())
          .events()) {
    processor.processStream(stream);
  }
}
```

### REST

```
# 1. Start the stream (save the INTERACTION_ID from the interaction.start event
#    and the last "event_id" you receive)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "stream": true,
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto"
    }
}'

# 2. If the connection drops, reconnect with your saved IDs
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID?stream=true&last_event_id=LAST_EVENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## 后续问题和互动

在代理返回最终报告后，您可以使用 `previous_interaction_id` 继续对话。这样，您就可以针对研究的特定部分请求澄清、总结或详细说明，而无需重新开始整个任务。

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Can you elaborate on the second point in the report?",
    model="gemini-3.1-pro-preview",
    previous_interaction_id="COMPLETED_INTERACTION_ID"
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Can you elaborate on the second point in the report?',
    model: 'gemini-3.1-pro-preview',
    previous_interaction_id: 'COMPLETED_INTERACTION_ID'
});
console.log(interaction.steps.at(-1).content[0].text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.1-pro-preview")
        .input(InteractionsInput.of("Can you elaborate on the second point in the report?"))
        .previousInteractionId("COMPLETED_INTERACTION_ID")
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Can you elaborate on the second point in the report?",
    "model": "gemini-3.1-pro-preview",
    "previous_interaction_id": "COMPLETED_INTERACTION_ID"
}'
```

## 何时使用 Gemini Deep Research 智能体

Deep Research 是一种**智能体**，而不仅仅是一种模型。它最适合需要“开箱即用的分析师”方法而非低延迟聊天的工作负载。

| 功能 | 标准 Gemini 模型 | Gemini Deep Research 智能体 |
| --- | --- | --- |
| **延迟时间** | 秒 | 分钟（异步/后台） |
| **流程** | 生成 -> 输出 | 规划 -> 搜索 -> 阅读 -> 迭代 -> 输出 |
| **输出** | 对话文本、代码、简短摘要 | 详细报告、长篇分析、比较表格 |
| **适用场景** | 聊天机器人、提取、创意写作 | 市场分析、尽职调查、文献综述、竞争格局 |

## 代理配置

Deep Research 使用 `agent_config` 参数来控制行为。
以字典形式传递，其中包含以下字段：

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `type` | `string` | 必填 | 必须为 `"deep-research"`。 |
| `thinking_summaries` | `string` | `"none"` | 设置为 `"auto"` 可在流式传输期间接收中间推理步骤。设置为 `"none"` 即可停用。 |
| `visualization` | `string` | `"auto"` | 设置为 `"auto"` 可启用智能体生成的图表和图片。设置为 `"off"` 即可停用。 |
| `collaborative_planning` | `boolean` | `false` | 设置为 `true` 可在研究开始前启用多轮计划审核。 |

### Python

```
agent_config = {
    "type": "deep-research",
    "thinking_summaries": "auto",
    "visualization": "auto",
    "collaborative_planning": False,
}

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Research the competitive landscape of cloud GPUs.",
    agent_config=agent_config,
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Research the competitive landscape of cloud GPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        visualization: 'auto',
        collaborative_planning: false,
    },
    background: true,
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.Visualization;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

DeepResearchAgentConfig agentConfig =
    DeepResearchAgentConfig.builder()
        .thinkingSummaries(ThinkingSummaries.AUTO)
        .visualization(Visualization.AUTO)
        .collaborativePlanning(false)
        .build();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Research the competitive landscape of cloud GPUs."))
        .agentConfig(agentConfig)
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of cloud GPUs.",
    "agent": "deep-research-preview-04-2026",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "visualization": "auto",
        "collaborative_planning": false
    },
    "background": true
}'
```

## 适用范围和定价

您可以使用 Google AI Studio 和 Gemini API 中的 Interactions API 访问 Gemini Deep Research 智能体。

价格遵循[随用随付模式](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn#pricing-for-agents)，具体取决于底层 Gemini 模型和智能体使用的特定工具。与标准聊天请求（一个请求对应一个输出）不同，深度研究任务是一种智能体工作流。只需一个请求，即可触发自主规划、搜索、阅读和推理循环。

### 估算费用

费用因所需研究的深度而异。智能体可自主确定需要阅读和搜索多少内容才能回答您的提示。

- **Deep Research** (`deep-research-preview-04-2026`)：对于需要中等程度分析的典型查询，该智能体可能会使用约 80 个搜索查询、约 25 万个输入 token（约 50-70% 为缓存 token）和约 6 万个输出 token。
  - **估计总价**：每项任务约 1.00 美元至 3.00 美元
- **Deep Research Max** (`deep-research-max-preview-04-2026`)：对于深入的竞争格局分析或广泛的尽职调查，智能体可能会使用多达约 160 次搜索查询、约 90 万个输入 token（约 50-70% 为缓存）和约 8 万个输出 token。
  - **估计总价**：每项任务约 3.00 美元 - 7.00 美元

## 安全注意事项

让智能体访问网络和您的私密文件需要仔细考虑安全风险。

- **使用文件进行提示注入**：代理会读取您提供的文件的内容。确保上传的文档（PDF、文本文件）来自可信来源。恶意文件可能包含旨在操纵代理输出的隐藏文字。
- **网络内容风险**：智能体会在公开网络中搜索内容。虽然我们实现了强大的安全过滤功能，但代理仍有可能遇到并处理恶意网页。建议您查看回答中提供的 `citations`，以验证来源。
- **数据渗出**：如果您还允许代理浏览网页，那么在要求代理总结敏感的内部数据时，请务必谨慎。

## 最佳做法

- **提示未知内容**：指示代理如何处理缺失的数据。
  例如，在提示中添加*“如果无法提供 2025 年的具体数据，请明确说明这些数据是预测数据或无法提供，而不是进行估计”*。
- **提供背景信息**：直接在输入提示中提供背景信息或限制条件，以便为代理的研究提供背景信息。
- **使用协作规划**：对于复杂查询，请启用协作规划，以便在执行之前查看和优化研究计划。
- **多模态输入**：Deep Research 智能体支持多模态输入。
  请谨慎使用，因为这会增加费用并导致上下文窗口溢出风险。

## 限制

- **自定义工具**：目前，您无法提供自定义的函数调用工具，但可以将远程 MCP（模型上下文协议）服务器与深度研究智能体搭配使用。
- **结构化输出**：Deep Research 智能体目前不支持结构化输出。
- **最长研究时间**：Deep Research 智能体的最长研究时间为 60 分钟。大多数任务应该会在 20 分钟内完成。
- **商店要求**：使用 `background=True` 执行代理需要 `store=True`。
- **Google 搜索**： [Google 搜索](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)默认处于启用状态，并且[特定限制](https://ai.google.dev/gemini-api/terms?hl=zh-cn#use-restrictions2)适用于接地结果。

## 后续步骤

- 详细了解 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn)。
- 了解如何使用[文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn)工具来使用您自己的数据。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-18。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-18。"],[],[]]
