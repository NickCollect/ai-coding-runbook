---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=zh-CN
fetched_at: 2026-09-14T05:36:27.081426+00:00
title: "\u53d7\u7ba1\u4ee3\u7406\u5feb\u901f\u5165\u95e8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 受管代理快速入门

本指南将引导您使用 [Antigravity 智能体](https://ai.google.dev/gemini-api/docs/agents/antigravity-agent?hl=zh-cn)，在 Gemini API 上创建和使用托管式智能体。您将进行首次代理调用、继续多轮对话、流式传输响应、从沙盒下载文件，以及使用 Antigravity 托管代理。

## 运行您的首次智能体互动

只需对 [Interactions API](https://ai.google.dev/gemini-api/docs?hl=zh-cn) 进行一次调用，即可预配 Linux 沙盒、运行智能体循环并返回结果。您将定义三个参数：

- 传入 `agent` 作为 `"antigravity-preview-05-2026",`，这是我们预定义的一般用途的受管代理的当前版本。
- 定义 `environment="remote"`，以预配新的沙盒环境。
- 创建输入，定义您希望代理执行的操作。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)

# Print the agent's final output
print(f"Interaction ID: {interaction.id}")
print(f"Environment ID: {interaction.environment_id}")
print(f"Output: {interaction.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment: "remote",
});

console.log(`Interaction ID: ${interaction.id}`);
console.log(`Environment ID: ${interaction.environment_id}`);

console.log(`Output: ${interaction.output_text}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."}],
    "environment": {"type": "remote"}
}'
```

响应会返回一个 `Interaction` 对象。存储 `interaction.id` 和 `interaction.environment_id`，以便在同一沙盒中继续对话。使用 `interaction.output_text` 访问代理的最终回答。`interaction.steps` 列出了智能体采取的每个步骤（推理、工具调用、代码执行）。

## 继续对话（多回合）

该 API 会跟踪两个独立的状态维度：

- **对话上下文**：聊天记录、推理轨迹、工具使用情况、使用 `previous_interaction_id`。
- [**环境状态**：](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-cn)使用 `environment` 的文件、已安装的软件包和沙盒状态。

在各自的位置传递这两个实参以恢复：

### Python

```
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    input="Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
)

print(interaction_2.output_text)
```

### JavaScript

```
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    input: "Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
}, { timeout: 300_000 });

console.log(interaction2.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "previous_interaction_id": "interaction_id_from_step_1",
    "environment": "environment_id_from_step_1",
    "input": [{"type": "text", "text": "Now plot the Fibonacci sequence as a line chart and save it as chart.png."}]
}'
```

回合 1 (`fibonacci.txt`) 中的文件会保留到回合 2。智能体还会保留对话上下文。

您可以独立混搭使用这些功能：

- **清除对话，保留文件**：省略 `previous_interaction_id`，仅使用 `environment` 传递环境 ID，以便在同一工作区中开始新的对话。
- **保留对话，新工作区**：传递 `previous_interaction_id`，为全新沙盒设置 `environment="remote"`。

### 自动压缩上下文

在长时间的多轮对话中，推理步骤、工具调用和大型文件内容的原始历史记录可能会快速增长，并占用大量上下文空间。为防止出现令牌限制错误并保持托管式智能体的专注度（防止出现“上下文腐烂”），Managed Agents API 在大约 13.5 万个令牌时会执行原生上下文压缩步骤。这个过程是自动进行的。

## 以流式传输回答

对于长时间运行的任务，您可以流式传输响应，以实时查看代理的工作情况：

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment="remote",
    stream=True,
)

for event in stream:
    print(event)
    if event.event_type == "step.stop" and event.usage:
        print(event.usage)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment: "remote",
    stream: true,
});

for await (const event of stream) {
    console.log(event);
    if (event.event_type === "step.stop" && event.usage) {
        console.log(event.usage);
    }
}
```

### REST

```
curl -N -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    "environment": "remote",
    "stream": true
}'
```

流式传输会返回步数增量，并进行增量更新。当某个步骤完成时，`step.stop` 事件会包含累积的使用情况统计信息。如需了解详情，请参阅[流式传输指南](https://ai.google.dev/gemini-api/docs/streaming?hl=zh-cn)。

## 从环境中下载文件

当代理在沙盒内创建文件时。使用 Files API 通过直接 HTTP 请求（尚无 SDK 方法）下载这些文件：

### Python

```
import os
import requests
import tarfile

env_id = interaction.environment_id
api_key = os.environ["GEMINI_API_KEY"]

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

with open("snapshot.tar", "wb") as f:
    f.write(response.content)

with tarfile.open("snapshot.tar") as tar:
    tar.extractall(path="extracted_snapshot")
```

### JavaScript

```
import fs from "fs";
import { execSync } from "child_process";

const envId = interaction.environment_id;
const apiKey = process.env.GEMINI_API_KEY || "";

const url = `https://generativelanguage.googleapis.com/v1beta/files/environment-${envId}:download?alt=media`;
const response = await fetch(url, {
    headers: {
        "x-goog-api-key": apiKey,
    },
});

if (!response.ok) {
    throw new Error(`Failed to download file: ${response.statusText}`);
}

const buffer = Buffer.from(await response.arrayBuffer());
fs.writeFileSync("snapshot.tar", buffer);

if (!fs.existsSync("extracted_snapshot")) {
    fs.mkdirSync("extracted_snapshot");
}
execSync("tar -xf snapshot.tar -C extracted_snapshot");

console.log(fs.readdirSync("extracted_snapshot"));
```

### REST

```
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-o snapshot.tar

tar -xf snapshot.tar -C extracted_snapshot
```

## 保存受管代理

在之前的步骤中，我们使用了默认的 Antigravity 智能体，并对其进行了内嵌自定义。对配置（指令、技能、模型选择和环境）进行迭代后，您可以将其保存为可重复使用的受管代理。这样一来，您就可以通过 ID 调用该配置，而无需重复配置。

保存代理时，请注意与内嵌互动之间的架构对称性：您可以指定 `base_agent: "antigravity-preview-05-2026"`，并传递包含所选 `model` 的 `agent_config`，就像在 `interactions.create` 上一样。您还可以定义 `base_environment`（通过来源或派生现有环境）。代理将针对每次新互动使用此环境和模型配置。

**来自来源**：内嵌定义来源，或从 GitHub 或 Cloud Storage 等其他来源定义来源。

### Python

```
agent = client.agents.create(
    id="fibonacci-analyst",
    base_agent="antigravity-preview-05-2026",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.6-flash",
    },
    system_instruction="You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports.",
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ],
    },
)

print(f"Saved agent: {agent.id}")
```

### JavaScript

```
const agent = await client.agents.create({
    id: "fibonacci-analyst",
    base_agent: "antigravity-preview-05-2026",
    agent_config: {
        type: "antigravity",
        model: "gemini-3.6-flash",
    },
    system_instruction: "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always include a chart and a summary table in your reports.",
            },
            {
                type: "repository",
                source: "https://github.com/your-org/skills",
                target: ".agents/skills"
            }
        ],
    },
});

console.log(`Saved agent: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "fibonacci-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "agent_config": {
        "type": "antigravity",
        "model": "gemini-3.6-flash"
    },
    "system_instruction": "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports."
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ]
    }
}'
```

## 调用受管理的代理

保存受管理的代理后，您可以通过 ID 调用它。每次调用都会派生出基本环境，因此每次运行都是从干净的状态开始的：

### Python

```
result = client.interactions.create(
    agent="fibonacci-analyst",
    input="Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "fibonacci-analyst",
    input: "Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment: "remote",
}, {
    timeout: 300_000,
});

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "fibonacci-analyst",
    "environment": "remote",
    "input": "Generate the first 50 prime numbers, plot their distribution, and save a PDF report."
}'
```

## 后续步骤

- [反重力智能体](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-cn)：功能、支持的工具、多模态输入、价格和限制。
- [构建托管式智能体](https://ai.google.dev/gemini-api/docs/custom-agents?hl=zh-cn)：使用您自己的指令、技能和数据来扩展 Antigravity。
- [环境](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-cn)：来源、网络、生命周期、资源限制。
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn)：模型和代理的基础 API。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-12。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-12。"],[],[]]
