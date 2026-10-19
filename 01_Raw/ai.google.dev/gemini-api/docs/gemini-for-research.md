---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=zh-CN
fetched_at: 2026-10-19T05:54:50.965096+00:00
title: "\u4f7f\u7528 Gemini for Research \u52a0\u901f\u53d1\u73b0 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 现已上架。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)

# 使用 Gemini for Research 加速发现

[获取 Gemini API 密钥](https://aistudio.google.com/apikey?hl=zh-cn)

Gemini 模型可用于推进各个学科的基础研究。
以下是一些探索 Gemini 在研究方面的用途的方法：

- **分析和控制模型输出**：如需进一步分析，您可以使用 `CitationMetadata` 等工具检查模型生成的候选回答。您还可以配置模型生成和输出选项，例如 `responseSchema`、`topP` 和 `topK`。[了解详情](https://ai.google.dev/api/generate-content?hl=zh-cn)。
- **多模态输入**：Gemini 可以处理图片、音频和视频，从而实现众多令人兴奋的研究方向。[了解详情](https://ai.google.dev/gemini-api/docs/vision?hl=zh-cn)。
- **长上下文功能**：Gemini 3.0 Flash 和 Pro 均配备 100 万个词元的上下文窗口。[了解详情](https://ai.google.dev/gemini-api/docs/long-context?hl=zh-cn)。
- **Grow with Google 谷歌成长计划**：通过 API 和 Google AI Studio 快速访问 Gemini 模型，以用于生产用例。如果您正在寻找基于 Google Cloud 的平台，Gemini Enterprise Agent Platform 可以提供额外的支持基础设施。

为了支持学术研究并推动前沿研究，Google 通过 [Gemini 学术计划](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=zh-cn#gemini-academic-program)为科学家和学术研究人员提供 Gemini API 赠金。

## 开始使用 Gemini

借助 Gemini API 和 Google AI Studio，您可以开始使用 Google 的最新模型，并将您的想法转化为可扩缩的应用。

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="How large is the universe?",
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
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;

Client client = new Client();
CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.8-flash"))
    .input(InteractionsInput.of("How large is the universe?"))
    .build();
var interaction = client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("How large is the universe?"),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
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
  "contents": [{
    "parts":[{"text": "How large is the universe?"}]
    }]
   }'
```

## 精选学术研究人员

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=zh-cn)

“我们的研究从稳健性和安全性的角度，探讨了 Gemini 作为视觉语言模型 (VLM) 在各种环境中的智能体行为。到目前为止，我们已经评估了 VLM 代理在执行计算机任务时，Gemini 针对弹出式窗口等干扰的鲁棒性，并利用 Gemini 分析了基于视频输入的社交互动、时间事件以及风险因素。”

[Diyi Yang 的网站](https://cs.stanford.edu/~diyiy/)

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=zh-cn)

“Gemini Pro 和 Flash 具有长上下文窗口，一直在帮助我们开展 OK-Robot 项目，这是一个开放词汇移动操作项目。Gemini 支持对机器人的“记忆”（在本例中是指机器人在长时间运行期间的先前观测结果）进行复杂的自然语言查询和命令。Mahi Shafiullah 和我还在使用 Gemini 将任务分解为机器人可以在现实世界中执行的代码。”

[Lerrel Pinto 的网站](https://www.lerrelpinto.com/)

## Gemini 学术计划

[支持的国家/地区](https://ai.google.dev/gemini-api/docs/available-regions?hl=zh-cn)中符合条件的学术研究人员（例如教职员工和博士生）可以申请获得 Gemini API 赠金和更高的速率限制，以用于研究项目。此支持可提高科学实验的吞吐量，并推进研究。

我们对以下部分的研究领域特别感兴趣，但也欢迎来自不同科学学科的申请：

- **评估和基准**：社区认可的评估方法，可在事实性、安全性、指令遵循、推理和规划等领域提供强有力的性能信号。
- **加速科学发现，造福人类**：AI 在跨学科科学研究中的潜在应用，包括罕见病和被忽视的疾病、实验生物学、材料科学和可持续性等领域。
- **具身和互动**：利用大语言模型来探索具身 AI、环境互动、机器人技术和人机交互领域的新型互动。
- **新兴功能**：探索增强推理和规划能力所需的新智能体功能，以及如何在推理过程中扩展功能（例如，通过利用 Gemini Flash）。
- **多模态交互和理解**：确定多模态基础模型在各种任务中进行分析、推理和规划时的差距和机遇。

资格要求：只有与有效学术机构或学术研究组织相关联的个人（教职人员、研究人员或同等人员）才能申请。请注意，Google 会自行决定授予和移除 API 访问权限及积分。我们会每月审核申请。

### 开始使用 Gemini API 进行研究

[立即申请](https://forms.gle/HMviQstU8PxC5iCt5)

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-24。

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-24。"],[],[]]
