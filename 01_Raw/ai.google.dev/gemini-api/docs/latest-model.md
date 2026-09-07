---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=zh-CN
fetched_at: 2026-09-07T05:45:31.518526+00:00
title: "Gemini 3.8 Flash \u6709\u54ea\u4e9b\u65b0\u529f\u80fd \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Gemini 3.8 Flash 有哪些新功能

[查看所有模型](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn)

Gemini 3.8 Flash (`gemini-3.8-flash`) 已正式发布 (GA)，可用于生产环境。它是我们最智能的 Flash
模型，专为长期软件工程、自主智能体和复杂的企业工作流而设计。

本指南介绍了 Gemini 3.8 Flash 的新增功能、API 变更、代码示例和迁移指南。

## 新建模型

| 模型 | 模型 ID | 默认思考级别 | 价格 | 说明 |
| --- | --- | --- | --- | --- |
| Gemini 3.8 Flash | `gemini-3.8-flash` | `medium` | 3.8 Flash 将以初次体验价提供至今年年底，每百万输入 token 仅需 0.75 美元，每百万输出 token 仅需 3.75 美元；如需了解详情，请参阅[价格](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)。 | 我们最智能的 Flash 模型，专为长期软件工程、自主智能体和复杂的企业工作流而设计。 |

Gemini 3.8 Flash 支持 100 万个 token 的上下文窗口、最多 6.4 万个输出 token、可调的思考级别（`low`、`medium`、`high`）以及相同的全套内置工具。

如需了解完整规格，请参阅[Gemini 3.8 Flash 模型页面](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=zh-cn)。如需了解初次体验价详情，请参阅下方的[价格部分](#pricing)或[价格页面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn#gemini-3.8-flash)。

## 快速入门

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Write a three.js script that renders a realistic 3D black hole."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Write a three.js script that renders a realistic 3D black hole.",
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();
CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.8-flash"))
    .input(InteractionsInput.of("Hello world"))
    .build();
Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Write a three.js script that renders a realistic 3D black hole."
  }'
```

## Gemini 3.8 Flash 的新增功能

- **长期软件工程**： 在实际编码基准、复杂的多文件重构和确定性工具执行方面表现出色。如需了解详情，请参阅[评估方法](https://deepmind.google/models/evals-methodology/gemini-3-8-flash/?hl=zh-cn)。
- **自主智能体**： 可让您构建弹性多步骤规划和工具编排工作流，大幅减少失败循环和错误。
- **复杂的企业工作流**： 在要求严苛的领域任务和大规模数据流水线中，可提供卓越的准确性、深入的推理能力和高度的事实严谨性。
- **托管式智能体的默认模型**： 托管式智能体的默认智能体（[Antigravity 智能体](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-cn)）现在使用 Gemini 3.8 Flash。[Antigravity SDK](https://antigravity.google/docs/sdk/overview/?hl=zh-cn) 也默认使用 Gemini 3.8 Flash。
- **初次体验价**： Gemini 3.8 Flash 将以初次体验价提供至 2026 年 12 月 31 日，每百万输入 token 仅需 0.75 美元，每百万输出 token 仅需 3.75 美元。标准价格（每百万输入 token 1.50 美元，每百万输出 token 7.50 美元）将于 2027 年 1 月 1 日生效。

Gemini 3.8 Flash 经过精心设计，可在长时间运行的复杂任务中使用更多 token。为了在困难的多步骤目标上提供更高质量的结果，该模型会采取较小的推理步骤，迭代调用工具，并在此过程中验证其工作。并非每个工作流都需要这种级别的验证。对于日常任务，您可以降低[推理](#understanding-reasoning-levels)工作量，以减少 token 消耗。或者，您也可以继续使用 Gemini 3.7 Flash，它仍然完全受支持。

## 了解推理级别

Gemini 3.8 Flash 可让您通过调整模型的思考级别，灵活控制延迟时间和智能程度：

- **低思考力度**：缩短延迟时间敏感型任务的回答时间，例如突发事件响应流水线、实时聊天、撰写草稿和快速数据分析。
- **中等（默认）**： 适用于大多数任务的最佳质量。建议用于复杂的代码和智能体用例，可提供更高的首次准确率。
- **思考力度**：最大限度地提高模型的推理和工具编排能力。最适合深度推理、数学和困难的多步骤任务。

以下示例将复杂代码分析请求的 `thinking_level` 设置为 `medium`：

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    generation_config={
        "thinking_level": "medium"  # Balanced reasoning effort for complex tasks
    }
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
  generation_config: {
    thinking_level: "medium"
  }
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();
CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.8-flash"))
    .input(InteractionsInput.of("Hello world"))
    .build();
Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    "generation_config": {
      "thinking_level": "medium"
    }
  }'
```

## 更新后的 Antigravity 智能体

由于性能和推理能力有所提升，Gemini Managed Agents 中的 [Antigravity 智能体](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-cn)现在默认使用 Gemini 3.8 Flash 构建。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=(
        "Audit https://web.dev for performance, Core Web Vitals, and SEO. "
        "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. "
        "Check search indexing with Google Search for site:web.dev. "
        "Format the output as a side-by-side scorecard table with prioritized fixes."
    ),
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
  input: "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
  environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();
CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.8-flash"))
    .input(InteractionsInput.of("Hello world"))
    .build();
Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google'\''s PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
    "environment": "remote"
}'
```

可以使用 `agent_config` 配置底层 Gemini 模型 [can be configured](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-cn#model-selection)。

## 迁移核对清单

```
  `/gemini-api-dev migrate my app to Gemini 3.8 Flash`
```

### 迁移到 gemini-3.8-flash

- **更新模型 ID**： 将目标模型字符串更改为 `gemini-3.8-flash`。
- **移除已废弃的采样参数**：
  - 从生成配置中移除 `temperature`、`top_p` 和 `top_k`。
  - 将 `thinking_budget` 替换为字符串枚举 `thinking_level`。请注意，3.8 Flash 不支持 `minimal`。
  - 移除 `candidate_count`（Gemini 3 及更高版本不支持）。
- **强制执行轮次验证规则**：
  - 在服务器端 `previous_interaction_id` 上标准化多轮对话。
  - 移除预填充的模型轮次。
- **审核函数调用**：
  - 将多模态素材资源放置在响应载荷内。
  - 使用 `\n\n` 设置内嵌说明的格式。
  - 如果您看到与工具前文本相关的 `Malformed_Function_Call` 错误，请参阅 [工具前文本要求的变通方法](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn#workarounds-for-pre-tool-text-requirements)。
  - 仅在使用 generateContent API 时：确保所有 `FunctionResponse` 对象都包含 `call_id` 和 `name`。
- **Gemini 3 基准要求**： 如需了解 SDK 更新和思考签名保留，请参阅[Gemini 3.5 迁移核对清单](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=zh-cn#migration)。

## 价格

在 2026 年 12 月 31 日之前，您可以在 Google AI Studio 和 Gemini Enterprise Agent Platform 中享受 Gemini 3.8 Flash、Gemini 3.7 Flash 和 Gemini 3.6 Flash 的初次体验价。标准价格将于 2027 年 1 月 1 日生效。如需了解完整价格层级，请参阅[价格页面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn#gemini-3.8-flash)。

## 后续步骤

- 在[模型概览](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn)中查看 API 规范。
- 在 [Interactions API 概览](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 中探索多智能体编排。
- 在 [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn) 中测试和优化提示。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-03。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-03。"],[],[]]
