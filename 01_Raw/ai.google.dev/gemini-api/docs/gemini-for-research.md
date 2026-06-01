---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=zh-CN
fetched_at: 2026-06-01T05:56:40.438894+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)

# 利用 Gemini for Research 加快发现速度

[获取 Gemini API 密钥](https://aistudio.google.com/apikey?hl=zh-cn)

Gemini 模型可用于推进各个学科的基础研究。
您可以通过以下方式探索 Gemini 在研究中的应用：

- **分析和控制模型输出**：如需进一步分析，您可以使用
  等工具检查模型生成的
  `CitationMetadata`。您还可以配置模型生成和输出的选项，例如 `responseSchema`、`topP` 和 `topK`。[了解详情](https://ai.google.dev/api/generate-content?hl=zh-cn)。
- **多模态输入**：Gemini 可以处理图片、音频和视频，从而实现
  众多令人兴奋的研究方向。[了解详情](https://ai.google.dev/gemini-api/docs/vision?hl=zh-cn)。
- **长上下文功能**：Gemini 3.0 Flash 和 Pro 配备了 100 万个 token 的
  上下文窗口。[了解详情](https://ai.google.dev/gemini-api/docs/long-context?hl=zh-cn)。
- **Grow with Google**：通过 API 和 Google AI
  Studio 快速访问 Gemini 模型，以用于生产用例。如果您正在寻找基于 Google Cloud 的平台，Gemini Enterprise Agent Platform 可以提供额外的支持基础架构。

为了支持学术研究并推动前沿研究，Google 通过
[Gemini Academic Program](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=zh-cn#gemini-academic-program)为科学家和学术研究人员提供
Gemini API 赠金。

## 开始使用 Gemini

借助 Gemini API 和 Google AI Studio，您可以开始使用 Google 的最新模型，并将您的想法转化为可扩缩的应用。

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

“我们的研究从稳健性和安全性角度出发，调查了 Gemini 作为视觉语言模型 (VLM) 及其在各种环境中的智能体行为。到目前为止，我们已经评估了 Gemini 在 VLM 智能体执行计算机任务时应对弹出式窗口等干扰的稳健性，并利用 Gemini 基于视频输入分析社交互动、时间事件以及风险因素。”

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=zh-cn)

“Gemini Pro 和 Flash 具有长上下文窗口，一直在帮助我们完成 OK-Robot（我们的开放词汇移动操作项目）。Gemini 支持对机器人的‘记忆’执行复杂的自然语言查询和命令：在本例中，是指机器人长时间运行期间的先前观察结果。我和 Mahi Shafiullah 也在使用 Gemini 将任务分解为机器人可以在现实世界中执行的代码。”

## Gemini Academic Program

符合条件的学术研究人员（例如教职员工和博士生）可以在 [支持的
国家/地区](https://ai.google.dev/gemini-api/docs/available-regions?hl=zh-cn)申请 Gemini API
赠金和更高的速率限制，以用于研究项目。此支持可提高科学实验的吞吐量并推进研究。

我们对以下部分的研究领域特别感兴趣，但也欢迎来自不同科学学科的申请：

- **评估和基准**：社区认可的评估方法，
  可在事实性、安全性、
  指令遵循、推理和规划等领域提供强大的性能信号。
- **加速科学发现，造福人类**：AI 在跨学科科学研究中的潜在
  应用，包括罕见病和被忽视的疾病、实验生物学、材料科学
  和可持续性等领域。
- **具身和互动**：利用大语言模型
  调查具身 AI、环境
  互动、机器人技术和人机交互领域的新型互动。
- **新兴功能**：探索增强推理和规划所需的新智能体功能，以及如何在推理期间扩展功能（例如，利用 Gemini Flash）。
- **多模态互动和理解**：确定多模态基础模型在各种任务中进行分析、推理
  和规划的差距和
  机会。

资格条件：只有隶属于有效学术机构或学术研究组织的个人（教职员工、研究人员或同等人员）可以申请。请注意，API 访问权限和赠金将由 Google 自行决定授予和移除。我们会每月审核申请。

### 开始使用 Gemini API 进行研究

[立即申请](https://forms.gle/HMviQstU8PxC5iCt5)

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-19。

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-19。"],[],[]]
