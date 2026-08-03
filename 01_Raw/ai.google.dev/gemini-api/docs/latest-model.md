---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=zh-CN
fetched_at: 2026-08-03T04:34:36.843499+00:00
title: "\u4f7f\u7528\u6700\u65b0\u7684 Gemini \u6a21\u578b \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 使用最新的 Gemini 模型

[此页面](#)
[3.5 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=zh-cn)

Gemini 3.6 Flash (`gemini-3.6-flash`) 和 Gemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`) 现已正式发布 (GA)，可用于生产环境。

- **Gemini 3.6 Flash**：在复杂的智能体任务和多模态任务中表现更出色，同时减少了 token 使用量，价格也比 3.5 Flash 更低。
- **Gemini 3.5 Flash-Lite**：3.5 系列中速度最快、成本最低的模型。在高吞吐量执行方面优于之前的 Flash-Lite 版本。

本指南介绍了每个模型中的新功能、影响代码的 API 变更以及迁移方法。

### Gemini 3.6 Flash

1. 安装技能：

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. 应用技能：

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. 安装技能：

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. 应用技能：

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

## 新模型

| 模型 | 模型 ID | 默认思考等级 | 价格 | 说明 |
| --- | --- | --- | --- | --- |
| Gemini 3.6 Flash | `gemini-3.6-flash` | `medium` | 1.50 美元/100 万个输入 token 和 7.50 美元/100 万个输出 token | 在速度和智能之间取得平衡，可用于智能体任务和多模态任务。 |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | `minimal` | 0.30 美元/100 万个输入 token 和 2.50 美元/100 万个输出 token | 速度最快、成本最低的 3.5 模型，可实现高吞吐量执行。 |

这两种模型均支持 100 万个 token 的上下文窗口、最多 64,000 个输出 token、思考功能以及包括[使用电脑](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn)在内的全套解决方案。

如需查看完整规格，请参阅相应型号的页面：

- [Gemini 3.6 Flash 模型页面](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=zh-cn)
- [Gemini 3.5 Flash-Lite 模型页面](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=zh-cn)

如需详细了解价格，请参阅[价格页面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)。

## 快速入门

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Write a three.js script that renders an interactive 3D robot."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Write a three.js script that renders an interactive 3D robot.",
  });
  console.log(interaction.outputText);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.6-flash",
    "input": {
      "parts": [{"text": "Write a three.js script that renders an interactive 3D robot."}]
    }
  }'
```

## Gemini 3.6 Flash 新功能

- **减少了 token 和对话轮次**：与 Gemini 3.5 相比，完成多步工作流程所需的推理步骤、对话轮次和工具调用次数更少。它还可以减少执行循环螺旋式上升。
- **改进了代码生成功能**：可生成更高质量的可用于生产用途代码，减少了不必要的编辑和调试循环。
- **更好地遵循指令**：减少诊断任务期间不必要的文件更改。
- **强大的多模态和空间推理能力**：在图表解读、视觉蓝图转换和多元素网页布局生成方面的性能有所提升。
- **预先进行程序化检查**：与 Gemini 3.5 Flash 相比，更倾向于在进行更改之前运行诊断代码脚本。这有助于提高复杂任务的准确性，但可能会在简单的前端工作中增加额外的探索步骤。
- **计算机使用支持**：作为代理型界面自动化的原生工具提供支持。
- **界面样式偏好**：更擅长创建功能性代码，但人类评估者更喜欢早期模型提供的图文并茂和样式。您可以通过提供明确的设计指南来缓解此问题。
- **默认思考程度（中等）**：使用与 Gemini 3.5 Flash 相同的`medium`默认思考程度。
- **价格更低**：输出 token 费用更低（每 100 万个 token 7.50 美元，而 3.5 Flash 为每 100 万个 token 9.00 美元）。输入 token 仍为 1.50 美元/100 万个。

## Gemini 3.5 Flash-Lite 的新功能

- **缩短了任务执行延迟时间**：在 3.5 系列中，该模型具有最高吞吐量，可用于高容量数据解析和文档提取。
- **增强的推理和多模态性能**：从 Gemini 2.5 Flash 迁移的理想选择，在 HLE（18.0% 对比 11.0%）等推理任务和 CharXIV（74.5% 对比 63.7%）等多模态基准测试中取得了更高的分数。
- **子代理编排和工具可靠性**：提高了代码执行、搜索和 MCP 工作流的工具执行可靠性。提高自主规划和复杂子代理任务的思考水平。
- **提升了文档理解能力**：提高了文档解析和结构化数据提取的准确性。根据文档的复杂程度，尝试使用最低和最高思维水平。
- **交互式 Web 编码和表格数据处理**：通过轻量级代码执行进行规划，在前端 JavaScript 和表格数据处理方面表现出色。
- **聊天机器人和角色持久性**：与 Gemini 3.1 Flash-Lite 相比，在多轮对话中能更好地遵循指令，并保持角色一致性。
- **计算机使用支持**：作为代理型界面自动化的原生工具提供支持。

## 选择合适的 Flash 或 Flash-Lite 模型

使用下表为您的工作负载选择合适的模型和迁移路径。

这两种模型都需要移除已弃用的抽样参数（`temperature`、`top_p`、`top_k`）和预填充的模型对话轮次。如需了解详情，请参阅 [API 变更](#api-changes-and-parameter-updates)。

| 模型 | 主要应用场景 | 建议的迁移目标 |
| --- | --- | --- |
| **Gemini 3.6 Flash** `gemini-3.6-flash` | 代码生成、空间/多模态推理、多步骤智能体工作流 | **Gemini 3.5 Flash**、**Gemini 3 Flash（预览版）**或 **Gemini 3.1 Pro** |
| **Gemini 3.5 Flash-Lite** `gemini-3.5-flash-lite` | 自主子代理执行、海量数据分析和文档提取、结构化 JSON 解析 | **Gemini 3.1 Flash-Lite** 或 **Gemini 2.5 Flash** |

## 更新了 Antigravity 智能体

由于性能有所提升，Gemini 3.6 Flash 现在是 Gemini 托管式智能体 中 [Antigravity 智能体](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-cn)的新默认模型。您可以通过在 API 上设置新字段来更改此设置。

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
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## API 变更和参数更新

自 Gemini 3.6 Flash 和 Gemini 3.5 Flash-Lite 起，以下 API 变更将适用于这些模型以及未来发布的所有 Gemini 模型。

- **抽样参数废弃**：`temperature`、`top_p` 和 `top_k` 已废弃。该 API 会忽略这些参数，并在未来的模型生成中返回错误。
- **预填充模型对话轮次验证**：不再支持预填充模型对话轮次。如果请求中的最后一个非空对话轮次是 `model` 轮次，则 API 会返回 `400` 错误。

下面详细介绍了每项 API 变更，并提供了相应的代码示例。

### 1. 抽样参数弃用（`temperature`、`top_p`、`top_k`）

`temperature`、`top_p` 和 `top_k` 已被弃用并会被忽略。在未来的模型代系中，提供这些参数会返回 HTTP 400 错误。**从所有请求中移除这些参数。**

```
# ⚠️ Remove these parameters (deprecated)
generation_config = {
     "temperature": 0.7,
     "top_p": 0.9,
     "top_k": 40,
}
```

为了提高确定性，请针对您的特定用例定义包含明确规则的系统指令。

### 2. 预填充模型回合验证

不允许 API 请求以非空模型角色回合结束，并且会返回 **HTTP 400 错误**。

#### ⚠️ 避免

在旧版 `generateContent` 或原始 REST 载荷中，现在不允许以模型角色回合结束：

```
/* ❌ DO NOT: End payload contents with a 'model' role turn */
{
  "contents": [
    {"role": "user", "parts": [{"text": "Translate 'Hello world' to Spanish."}]},
    {"role": "model", "parts": [{"text": "Translation:"}]}  /* ❌ Returns error */
  ]
}
```

#### ✅ 推荐的迁移（Interactions API）

在 Interactions API 中，模型回合不会手动预填充。如果您的应用之前预填充了模型对话轮次以抑制序言或强制 JSON 格式，请改用 system\_instruction 或[结构化输出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)。

```
# ✅ RECOMMENDED: Use system_instruction in the Interactions API to specify output format
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Translate 'Hello world' to Spanish.",
    system_instruction="Output only the translation without introductory text.",
)
```

## 迁移核对清单

### Gemini 3.6 Flash

1. 安装技能：

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. 应用技能：

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. 安装技能：

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. 应用技能：

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

### 迁移到 gemini-3.6-flash

- **更新模型 ID**：将目标模型字符串更改为 `gemini-3.6-flash`。
- **移除了已废弃的抽样参数**：
  - 从生成配置中剥离了 `temperature`、`top_p` 和 `top_k`。
  - 将 `thinking_budget` 替换为设置为 `"medium"` 或 `"high"` 的字符串枚举 `thinking_level`。
  - 移除 `candidate_count`（在 Gemini 3.x 中不受支持）。
- **强制执行回合验证规则**：
  - 在服务器端 `previous_interaction_id` 上标准化多轮对话。
  - 移除预填充的模型对话轮次。
- **审核函数调用**：
  - 将多模态资源放置在响应载荷中。
  - 使用 `\n\n` 格式设置内嵌说明。
  - 如果您看到与工具前文本相关的 `Malformed_Function_Call` 错误，请参阅[工具前文本要求的解决方法](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn#workarounds-for-pre-tool-text-requirements)。
  - 仅在使用 generateContent API 时：确保所有 `FunctionResponse` 对象都包含 `call_id` 和 `name`。
- **Gemini 3.x 基准要求**：如需了解 SDK 更新和思考签名保留，请参阅 [Gemini 3.5 迁移核对清单](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=zh-cn#migration)。

### 迁移到 gemini-3.5-flash-lite

- **更新模型 ID**：将目标模型字符串更改为 `gemini-3.5-flash-lite`。
- **配置思考努力程度**：
  - 对于大批量提取、路由或分类：将 `thinking_level` 保留为 `"minimal"`（默认值），以实现最大吞吐量。
  - 对于具有工具调用、代码执行或多步推理的自主子代理：请将 `thinking_level` 设置为 `"medium"` 或 `"high"`，以防止工具过早终止。
- **移除已弃用的参数并验证函数调用**：应用与 3.6 Flash [相同的规则](#migrate-to-gemini-3-6-flash)。
- **Gemini 3.x 基准要求**：请参阅 [Gemini 3.5 迁移核对清单](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=zh-cn#migration)。

## 后续步骤

- 查看[模型概览](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn)中的 API 规范。
- 在 [Interactions API 指南](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-cn)中探索多代理编排。
- 在 [Google AI Studio](https://aistudio.google.com/?hl=zh-cn) 中测试和优化提示。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-30。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-30。"],[],[]]
