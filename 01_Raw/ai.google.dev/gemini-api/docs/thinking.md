---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=zh-CN
fetched_at: 2026-05-05T19:50:29.587290+00:00
title: "Gemini \u601d\u8003 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Gemini 思考

[Gemini 3 和 2.5 系列模型](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn)使用内部
“思考过程”，可显著提高其推理和多步
规划能力，使其能够高效处理编码、高等数学和数据分析等复杂任务。

本指南介绍了如何使用 Gemini API 来使用 Gemini 的思考功能。

## 使用思考功能生成内容

使用思考模型发起请求与任何其他内容生成请求类似。主要区别在于，在 `model` 字段中指定一个
[支持思考的模型](#supported-models)，如
以下 [文本生成](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-cn#text-input) 示例所示：

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3-flash-preview"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## 思考总结

思考总结是模型原始思考的总结版本，可帮助您了解模型的内部推理过程。请注意，思考等级和预算适用于模型的原始思考，而不适用于思考总结。

您可以在请求配置中将 `includeThoughts` 设置为 `true`，以启用思考总结。然后，您可以遍历 `response` 参数的 `parts` 并检查 `thought` 布尔值，以访问总结。

以下示例演示了如何在不进行流式传输的情况下启用和检索思考总结，该示例会返回包含回答的单个最终思考总结：

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3-flash-preview"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

以下示例展示了如何使用流式传输进行思考，该示例会在生成期间返回滚动式增量总结：

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3-flash-preview",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3-flash-preview",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
    }
  }
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
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3-flash-preview"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## 控制思考

Gemini 模型默认采用动态思考，会根据用户请求的复杂程度自动调整推理工作量。
但是，如果您有特定的延迟时间限制，或者需要模型进行比平时更深入的推理，您可以选择使用参数来控制思考行为。

### 思考等级 (Gemini 3)

`thinkingLevel` 参数（建议用于 Gemini 3 模型及更高版本）可让您控制推理行为。

下表详细介绍了每种模型类型的 `thinkingLevel` 设置：

| 思考等级 | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | 说明 |
| --- | --- | --- | --- | --- |
| **`minimal`** | 不支持 | 受支持（默认） | 受支持 | 与大多数查询的“不思考”设置匹配。对于复杂的编码任务，模型可能会进行非常少的思考。最大限度地减少聊天或高吞吐量应用的延迟时间。请注意，`minimal` 并不能保证思考功能处于关闭状态。 |
| **`low`** | 受支持 | 支持 | 受支持 | 最大限度地减少延迟时间和费用。最适合简单的指令遵循、聊天或高吞吐量应用。 |
| **`medium`** | 受支持 | 支持 | 受支持 | 针对大多数任务进行平衡思考。 |
| **`high`** | 受支持（默认、动态） | 受支持（动态） | 受支持（默认、动态） | 最大限度地提高推理深度。模型可能需要更长的时间才能 生成第一个（非思考）输出 token，但输出将经过更仔细的推理。 |

以下示例展示了如何设置思考等级。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3-flash-preview"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

您无法为 Gemini 3.1 Pro 停用思考功能。Gemini 3 Flash 和 Flash-Lite 也不支持完全关闭思考功能，但 `minimal` 设置意味着模型可能不会思考（尽管它仍然有可能思考）。
如果您未指定思考等级，Gemini 将使用 Gemini 3 模型的
默认动态思考等级 `"high"`。

Gemini 2.5 系列模型不支持 `thinkingLevel`；请改用 `thinkingBudget`。

### 思考预算

`thinkingBudget` 参数是 Gemini 2.5 系列中引入的参数，用于指导模型使用特定数量的思考 token 进行推理。

以下是每种模型类型的 `thinkingBudget` 配置详细信息。
您可以通过将 `thinkingBudget` 设置为 0 来停用思考功能。
将 `thinkingBudget` 设置为 -1 会启用 **动态思考** ，这意味着模型将根据请求的复杂程度调整预算。

| 模型 | 默认设置 (未设置思考预算) | 范围 | 停用思考功能 | 启用动态思考 |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | 动态思考 | `128` 到 `32768` | 不适用：无法停用思考功能 | `thinkingBudget = -1`（默认） |
| **2.5 Flash** | 动态思考 | `0` 到 `24576` | `thinkingBudget = 0` | `thinkingBudget = -1`（默认） |
| **2.5 Flash 预览版** | 动态思考 | `0` 到 `24576` | `thinkingBudget = 0` | `thinkingBudget = -1`（默认） |
| **2.5 Flash Lite** | 模型不思考 | `512` 到 `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite 预览版** | 模型不思考 | `512` 到 `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 预览版** | 动态思考 | `0` 到 `24576` | `thinkingBudget = 0` | `thinkingBudget = -1`（默认） |
| **2.5 Flash Live Native Audio 预览版 (09-2025)** | 动态思考 | `0` 到 `24576` | `thinkingBudget = 0` | `thinkingBudget = -1`（默认） |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

根据提示，模型可能会超出或低于 token 预算。

## 思考特征

Gemini API 是无状态的，因此模型会独立处理每个 API 请求，并且无法访问多轮互动中先前轮次的思考上下文。

为了能够在多轮互动中保持思考上下文，Gemini 会返回思考特征，这些特征是模型内部思考过程的加密表示形式。

- **Gemini 2.5 模型** 会在启用思考功能且
  请求包含 [函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn#thinking)（具体来说是 [函数声明](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn#step-2)）时返回思考特征。
- **Gemini 3 模型** 可能会针对所有类型的 [部件](https://ai.google.dev/api/caching?hl=zh-cn#Part) 返回思考特征。
  我们建议您始终按收到的方式传递所有特征，但函数调用特征是必需的。 如需了解详情，请参阅
  [思考特征](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=zh-cn)页面。

使用函数调用时，还需考虑以下用量限制：

- 特征由模型在回答的其他部分（例如函数调用或文本部分）中返回。[在后续对话轮次中，将包含所有部分的完整回答](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn#step-4)
  返回给模型。
- 请勿将包含特征的部分串联在一起。
- 请勿将包含签名的部分与不包含签名的部分合并。

## 价格

启用思考功能后，回答价格是输出 token 和思考 token 的总和。您可以从 `thoughtsTokenCount` 字段获取生成的思考 token 总数。

### Python

```
# ...
print("Thoughts tokens:",response.usage_metadata.thoughts_token_count)
print("Output tokens:",response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println("Thoughts tokens:", string(usageMetadata.thoughts_token_count))
fmt.Println("Output tokens:", string(usageMetadata.candidates_token_count))
```

[思考模型会生成完整的思考内容，以提高最终回答的质量，然后输出总结，以帮助您了解思考过程。](#summaries)因此，价格取决于模型生成总结所需的完整思考 token，尽管 API 仅输出总结。

如需详细了解 token，请参阅 [token 计数](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn)
指南。

## 最佳做法

本部分提供了一些关于如何高效使用思考模型的指导。
与往常一样，遵循我们的[提示指南和最佳做法](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=zh-cn)将获得最佳结果。

### 调试和引导

- **查看推理**：如果您没有从
  思考模型中获得预期的回答，仔细分析 Gemini 的思考总结可能会有所帮助。
  您可以了解模型如何分解任务并得出结论，并使用该信息来纠正，以获得正确的结果。
- **在推理中提供指导**：如果您希望获得特别长的
  输出，不妨在提示中提供指导，以限制模型使用的
  [思考量](#set-budget)。这样，您就可以为回答预留更多 token 输出。

### 任务复杂性

- **简单任务（可以关闭思考功能）**： 对于不需要复杂推理的简单请求（例如事实检索或分类），不需要思考功能。例如：
  - “DeepMind 是在哪里成立的？”
  - 这封电子邮件是要求开会还是仅提供信息？
- **中等任务（默认/部分思考）**： 许多常见请求都受益于一定程度的逐步处理或更深入的理解。Gemini 可以灵活地使用思考功能来处理以下任务：
  - 将光合作用比作成长。
  - 比较和对比电动汽车和混合动力汽车。
- **困难任务（最大思考能力）**： 对于真正复杂的挑战（例如解决复杂的数学问题或编码任务），我们建议设置较高的思考预算。这些类型的任务需要模型充分发挥推理和规划能力，通常需要执行许多内部步骤才能提供答案。例如：
  - 解决 AIME 2025 中的问题 1：求所有整数基数 b > 9 的和，其中 17b 是 97b 的除数。
  - 为可视化实时股票市场数据的 Web 应用编写 Python 代码，包括用户身份验证。尽可能提高效率。

## 支持的模型、工具和功能

所有 3 和 2.5 系列模型都支持思考功能。
您可以在
[模型概览](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn)页面上找到所有模型功能。

思考模型适用于 Gemini 的所有工具和功能。这使得模型能够与外部系统互动、执行代码或访问实时信息，并将结果纳入其推理和最终回答中。

您可以在
[思考功能使用示例](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking.ipynb?hl=zh-cn)中尝试使用思考模型搭配工具的示例。

## 接下来怎么做？

- 您可以在我们的 [OpenAI 兼容性](https://ai.google.dev/gemini-api/docs/openai?hl=zh-cn#thinking) 指南中找到思考功能覆盖范围。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-04-29。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-04-29。"],[],[]]
