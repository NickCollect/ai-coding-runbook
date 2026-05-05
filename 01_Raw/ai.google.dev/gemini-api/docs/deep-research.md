---
source_url: https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-TW
fetched_at: 2026-05-05T20:02:57.756570+00:00
title: "Gemini Deep Research Agent \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Gemini Deep Research Agent

Gemini Deep Research 代理會自主規劃、執行及統整多步驟研究工作。這項功能採用 Gemini，可瀏覽複雜的資訊環境，生成詳細且附有引用的報告。新功能可讓您與代理共同規劃、使用 MCP 伺服器連結外部工具、加入視覺化內容 (例如圖表)，以及直接提供文件做為輸入內容。

研究工作需要反覆搜尋和閱讀，可能需要幾分鐘才能完成。您必須使用背景執行 (設定 `background=true`)，以非同步方式執行代理程式，並輪詢結果或串流更新。詳情請參閱「[處理長時間執行的工作](#long-running-tasks)」。

以下範例說明如何在背景啟動研究工作，並輪詢結果。

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
        print(interaction.outputs[-1].text)
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
        console.log(result.outputs[result.outputs.length - 1].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
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

## 支援版本

Deep Research 代理有兩種版本：

- **Deep Research** (`deep-research-preview-04-2026`)：專為速度和效率而設計，非常適合串流回用戶端 UI。
- **Deep Research Max** (`deep-research-max-preview-04-2026`)：自動收集及統整內容，提供最全面的資訊。

## 共同規劃

在代理開始工作前，您可透過協作規劃功能控管研究方向。啟用後，代理程式會傳回建議的研究計畫，而不是立即執行。然後透過多輪互動檢閱、修改或核准計畫。

### 步驟 1：申請方案

在第一次互動中設定 `collaborative_planning=True`。代理程式會傳回研究計畫，而不是完整報告。

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
print(result.outputs[-1].text)
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
console.log(result.outputs[result.outputs.length - 1].text);
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

### 步驟 2：修正計畫 (選用)

使用 `previous_interaction_id` 繼續對話，並反覆修正行程。按住 `collaborative_planning=True` 即可繼續規劃模式。

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
print(result.outputs[-1].text)
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
console.log(result.outputs[result.outputs.length - 1].text);
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

### 步驟 3：核准並執行

設定 `collaborative_planning=False` (或省略) 即可核准計畫並開始研究。

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
print(result.outputs[-1].text)
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
console.log(result.outputs[result.outputs.length - 1].text);
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

## 視覺化

將 `visualization` 設為 `"auto"` 後，代理程式就能生成圖表和其他視覺元素，輔助研究結果。生成圖像會納入回覆輸出內容，並以 `image` 增量串流傳輸。為獲得最佳結果，請在查詢中明確要求提供視覺化內容，例如「附上顯示一段時間內趨勢的圖表」或「生成比較市占率的圖形」。將 `visualization` 設為 `"auto"` 即可啟用這項功能，但只有在提示要求時，代理程式才會生成圖像。

### Python

```
import base64
from IPython.display import Image, display

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

for output in result.outputs:
    if output.type == "text":
        print(output.text)
    elif output.type == "image" and output.data:
        image_bytes = base64.b64decode(output.data)
        print(f"Received image: {len(image_bytes)} bytes")
        # To display in a Jupyter notebook:
        # from IPython.display import display, Image
        # display(Image(data=image_bytes))
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

for (const output of result.outputs) {
    if (output.type === 'text') {
        console.log(output.text);
    } else if (output.type === 'image' && output.data) {
        console.log(`[Image Output: ${output.data.substring(0, 20)}...]`);
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

## 支援的工具

Deep Research 支援多種內建和外部工具。根據預設 (未提供 `tools` 參數時)，代理程式可存取 Google 搜尋、網址內容和程式碼執行功能。您可以明確指定工具，限制或擴充代理程式的功能。

| 工具 | 輸入值 | 說明 |
| --- | --- | --- |
| Google 搜尋 | `google_search` | 搜尋公開網路。(預設為啟用)。 |
| 網址背景資訊 | `url_context` | 閱讀並摘要網頁內容。(預設為啟用)。 |
| 程式碼執行 | `code_execution` | 執行程式碼以進行計算和資料分析。(預設為啟用)。 |
| MCP 伺服器 | `mcp_server` | 連線至遠端 MCP 伺服器，存取外部工具。 |
| 檔案搜尋 | `file_search` | 搜尋上傳的文件語料庫。 |

### Google 搜尋

明確啟用 Google 搜尋做為唯一工具：

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

### 網址背景資訊

讓代理程式能夠讀取及摘要特定網頁內容：

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

### 程式碼執行

允許代理執行程式碼，進行計算和資料分析：

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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Calculate the 50th Fibonacci number.",
    "tools": [{"type": "code_execution"}],
    "background": true
}'
```

### MCP 伺服器

在工具設定中提供伺服器 `name` 和 `url`。您也可以傳遞驗證憑證，並限制代理程式可呼叫的工具。

| 欄位 | 類型 | 必要 | 說明 |
| --- | --- | --- | --- |
| `type` | `string` | 是 | 必須為 `"mcp_server"`。 |
| `name` | `string` | 否 | MCP 伺服器的顯示名稱。 |
| `url` | `string` | 否 | MCP 伺服器端點的完整網址。 |
| `headers` | `object` | 否 | 以 HTTP 標頭形式傳送至伺服器的鍵值組 (例如驗證權杖)。 |
| `allowed_tools` | `array` | 否 | 限制代理程式可呼叫伺服器的哪些工具。 |

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

### 檔案搜尋

使用「檔案搜尋」工具，授予代理程式存取您自有資料的權限。

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

## 可操控性和格式

您可以在提示中提供特定格式設定指令，引導代理程式輸出內容。您可以將報表劃分為特定章節和子章節、加入資料表，或針對不同目標對象調整語氣 (例如「技術」、「高階主管」、「輕鬆」)。

在輸入文字中明確定義所需的輸出格式。

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

## 多模態輸入內容

「Deep Research」支援多模態輸入內容，包括圖片和文件 (PDF)，讓代理程式分析視覺內容，並根據提供的輸入內容進行網路研究。

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
        print(interaction.outputs[-1].text)
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
        console.log(result.outputs[result.outputs.length - 1].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
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
        {"type": "image", "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"}
    ],
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

### 文件解讀

直接將文件做為多模態輸入內容傳送。代理程式會分析您提供的文件，並根據文件內容進行研究。

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

## 處理長時間執行的工作

Deep Research 包含規劃、搜尋、閱讀和撰寫等多個步驟。這個週期通常會超出同步 API 呼叫的標準逾時限制。

服務專員必須使用 `background=True`。API 會立即傳回部分 `Interaction` 物件。您可以使用 `id` 屬性擷取輪詢的互動。互動狀態會從 `in_progress` 轉換為 `completed` 或 `failed`。

### 串流

Deep Research 支援串流功能，可即時更新研究進度，包括想法摘要、文字輸出內容和生成的圖片。您必須設定 `stream=True` 和 `background=True`。

如要接收中介推論步驟 (想法) 和進度更新，請將 `agent_config` 中的 `thinking_summaries` 設為 `"auto"`，啟用**思考摘要**。否則串流可能只會提供最終結果。

#### 串流事件類型

| 事件類型 | Delta 類型 | 說明 |
| --- | --- | --- |
| `content.delta` | `thought_summary` | 代理程式的中間推論步驟。 |
| `content.delta` | `text` | 最終文字輸出內容的一部分。 |
| `content.delta` | `image` | 生成的圖片 (Base64 編碼)。 |

以下範例會啟動研究工作，並處理自動重新連線的串流。這項功能會追蹤 `interaction_id` 和 `last_event_id`，因此如果連線中斷 (例如在 600 秒逾時後)，可以從中斷處繼續。

### Python

```
from google import genai

client = genai.Client()

interaction_id = None
last_event_id = None
is_complete = False

def process_stream(stream):
    global interaction_id, last_event_id, is_complete
    for chunk in stream:
        if chunk.event_type == "interaction.start":
            interaction_id = chunk.interaction.id
        if chunk.event_id:
            last_event_id = chunk.event_id
        if chunk.event_type == "content.delta":
            if chunk.delta.type == "text":
                print(chunk.delta.text, end="", flush=True)
            elif chunk.delta.type == "thought_summary":
                print(f"Thought: {chunk.delta.content.text}", flush=True)
        elif chunk.event_type in ("interaction.complete", "error"):
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
    for await (const chunk of stream) {
        if (chunk.event_type === 'interaction.start') {
            interactionId = chunk.interaction.id;
        }
        if (chunk.event_id) lastEventId = chunk.event_id;
        if (chunk.event_type === 'content.delta') {
            if (chunk.delta.type === 'text') {
                process.stdout.write(chunk.delta.text);
            } else if (chunk.delta.type === 'thought_summary') {
                console.log(`Thought: ${chunk.delta.content.text}`);
            }
        } else if (['interaction.complete', 'error'].includes(chunk.event_type)) {
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

## 後續問題和互動

代理程式傳回最終報告後，你可以使用 `previous_interaction_id` 繼續對話。這樣一來，您不必重新啟動整個工作，就能要求澄清、摘要或詳細說明研究的特定部分。

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

print(interaction.outputs[-1].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Can you elaborate on the second point in the report?',
    model: 'gemini-3.1-pro-preview',
    previous_interaction_id: 'COMPLETED_INTERACTION_ID'
});
console.log(interaction.outputs[interaction.outputs.length - 1].text);
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

## 何時使用 Gemini Deep Research 代理

Deep Research 是**代理**，而不只是模型。最適合需要「分析師即時服務」方法的工作負載，而非低延遲的即時通訊。

| 功能 | 標準 Gemini 模型 | Gemini Deep Research 代理程式 |
| --- | --- | --- |
| **延遲** | 秒 | 分鐘 (非同步/背景) |
| **流程** | 生成 -> 輸出內容 | 規劃 -> 搜尋 -> 閱讀 -> 疊代 -> 輸出 |
| **輸出內容** | 對話文字、程式碼、簡短摘要 | 詳細報表、長篇分析、比較表 |
| **最佳用途** | 聊天機器人、擷取、創意寫作 | 市場分析、盡職調查、文獻回顧、競爭環境 |

## 代理程式設定

Deep Research 會使用 `agent_config` 參數控制行為。
以字典形式傳遞，並包含下列欄位：

| 欄位 | 類型 | 預設 | 說明 |
| --- | --- | --- | --- |
| `type` | `string` | 必填 | 必須為 `"deep-research"`。 |
| `thinking_summaries` | `string` | `"none"` | 設為 `"auto"` 即可在串流期間接收中間推論步驟。如要停用，請設為 `"none"`。 |
| `visualization` | `string` | `"auto"` | 設為 `"auto"`，即可啟用代理程式生成的圖表和圖片。如要停用，請設為 `"off"`。 |
| `collaborative_planning` | `boolean` | `false` | 設為 `true`，即可在開始研究前啟用多輪計畫審查。 |

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

## 適用情形與定價

您可以使用 Google AI Studio 和 Gemini API 中的 Interactions API，存取 Gemini Deep Research Agent。

價格採用[即付即用模式](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw#pricing-for-agents)，取決於基礎 Gemini 模型和代理程式使用的特定工具。標準的即時通訊要求會產生一個輸出內容，但 Deep Research 工作是代理式工作流程，只要提出要求，系統就會自動規劃、搜尋、閱讀和推論。

### 預估費用

費用會因所需研究的深度而異。代理會自主判斷回答提示詞需要多少閱讀和搜尋量。

- **Deep Research** (`deep-research-preview-04-2026`)：對於需要中等程度分析的典型查詢，代理程式可能會使用約 80 個搜尋查詢、約 25 萬個輸入權杖 (約 50% 至 70% 的權杖會快取)，以及約 6 萬個輸出權杖。
  - **預估總金額：**每項工作約$1.00 美元至 $3.00 美元
- **Deep Research Max** (`deep-research-max-preview-04-2026`)：如要深入分析競爭環境或進行廣泛的盡職調查，代理程式最多可能會使用約 160 個搜尋查詢、約 90 萬個輸入權杖 (約 50% 至 70% 的權杖會快取)，以及約 8 萬個輸出權杖。
  - **預估總金額：**每項工作約$3.00 美元至 $7.00 美元

## 安全考量

授予代理程式網路和私人檔案的存取權時，請務必仔細考量安全風險。

- **使用檔案進行提示詞注入：**代理程式會讀取您提供的檔案內容。請確認上傳的文件 (PDF、文字檔) 來自可信來源。惡意檔案可能含有隱藏的文字，用於操縱代理程式的輸出內容。
- **網路內容風險：**代理程式會搜尋公開網路，雖然我們導入了強大的安全篩選器，但代理程式仍可能遇到並處理惡意網頁。建議您查看回覆中`citations`提供的
  來源，確認資訊是否正確。
- **資料外洩：**如果允許代理程式瀏覽網頁，要求代理程式摘要說明機密內部資料時，請務必謹慎。

## 最佳做法

- **提示未知內容：**指示代理程式如何處理遺漏的資料。
  舉例來說，在提示中加入「如果沒有 2025 年的具體數據，請明確指出這些是預測或無法取得，而非估算」。
- **提供脈絡：**直接在輸入提示中提供背景資訊或限制，做為代理程式研究的基準。
- **使用協作規劃功能：**對於複雜查詢，請啟用協作規劃功能，以便在執行前查看及修正研究計畫。
- **多模態輸入內容：**Deep Research 代理程式支援多模態輸入內容。
  請謹慎使用，因為這會增加成本，並可能導致脈絡視窗溢位。

## 限制

- **Beta 版狀態**：Interactions API 目前為公開 Beta 版。功能和結構定義可能會有所異動。
- **自訂工具：**目前無法提供自訂函式呼叫工具，但您可以搭配 Deep Research 代理使用遠端 MCP (Model Context Protocol) 伺服器。
- **結構化輸出內容：**Deep Research Agent 目前不支援結構化輸出內容。
- **研究時間上限：**Deep Research 代理的研究時間上限為 60 分鐘。大多數工作應可在 20 分鐘內完成。
- **商店規定：**使用 `background=True` 執行代理程式時，需要
  `store=True`。
- **Google 搜尋：** [Google 搜尋](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)預設為啟用，且[特定限制](https://ai.google.dev/gemini-api/terms?hl=zh-tw#use-restrictions2)適用於以 Google 搜尋為基礎的結果。

## 後續步驟

- 進一步瞭解 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-tw)。
- 請參閱 [Gemini API 教戰手冊中的 Deep Research](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Deep_Research.ipynb?hl=zh-tw)。
- 瞭解如何使用[檔案搜尋](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw)工具，運用自己的資料。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-04-29 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-04-29 (世界標準時間)。"],[],[]]
