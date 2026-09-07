---
source_url: https://ai.google.dev/gemini-api/docs/deep-research?hl=ko
fetched_at: 2026-09-07T05:33:11.408947+00:00
title: "Gemini Deep Research \uc5d0\uc774\uc804\ud2b8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini Deep Research 에이전트

Gemini Deep Research Agent는 여러 단계로 이루어진 연구 작업을 자율적으로 계획, 실행, 합성합니다. Gemini를 기반으로 복잡한 정보 환경을 탐색하여 인용된 상세 보고서를 생성합니다. 새로운 기능을 사용하면 에이전트와 공동으로 계획하고, MCP 서버를 사용하여 외부 도구에 연결하고, 시각화 (예: 차트 및 그래프)를 포함하고, 문서를 직접 입력으로 제공할 수 있습니다.

조사 작업에는 반복적인 검색과 읽기가 포함되며 완료하는 데 몇 분이 걸릴 수 있습니다. [백그라운드 실행](https://ai.google.dev/gemini-api/docs/background-execution?hl=ko) (`background=true` 설정)을 사용하여 에이전트를 비동기적으로 실행하고 결과를 폴링하거나 업데이트를 스트리밍해야 합니다. 자세한 내용은 [장기 실행 작업 처리](#long-running-tasks)를 참고하세요.

다음 예에서는 백그라운드에서 연구 작업을 시작하고 결과를 폴링하는 방법을 보여줍니다.

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

### 자바스크립트

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

## 지원되는 버전

Deep Research 에이전트는 두 가지 버전으로 제공됩니다.

- **Deep Research** (`deep-research-preview-04-2026`): 속도와 효율성을 위해 설계되었으며 클라이언트 UI로 다시 스트리밍하는 데 적합합니다.
- **Deep Research Max** (`deep-research-max-preview-04-2026`): 자동 컨텍스트 수집 및 합성의 최대 포괄성입니다.

## 공동 계획

협업 계획을 사용하면 에이전트가 작업을 시작하기 전에 조사 계획을 검토하고 수정하여 조사 방향을 제어할 수 있습니다. 사용 설정하면 에이전트가 즉시 실행하는 대신 제안된 조사 계획을 반환합니다. 그런 다음 여러 차례의 상호작용을 통해 계획을 검토, 수정 또는 승인할 수 있습니다.

### 1단계: 요금제 요청

첫 번째 상호작용에서 `collaborative_planning=True`를 설정합니다. 에이전트가 전체 보고서 대신 조사 계획을 반환합니다.

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

### 자바스크립트

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

### 2단계: 계획 수정 (선택사항)

`previous_interaction_id`을 사용하여 대화를 계속하고 계획을 반복합니다. 계획 모드를 유지하려면 `collaborative_planning=True`을 유지합니다.

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

### 자바스크립트

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

### 3단계: 승인 및 실행

계획을 승인하고 조사를 시작하려면 `collaborative_planning=False`를 설정하거나 생략합니다.

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

### 자바스크립트

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

## 시각화

`visualization`이 `"auto"`로 설정되면 에이전트가 연구 결과를 뒷받침하는 차트, 그래프, 기타 시각적 요소를 생성할 수 있습니다.
생성된 이미지는 대답 단계에 포함되며 `image` 델타로 스트리밍됩니다. 최상의 결과를 얻으려면 질문에 시각적 요소를 명시적으로 요청하세요. 예를 들어 '시간에 따른 추세를 보여주는 차트를 포함해' 또는 '시장 점유율을 비교하는 그래픽을 생성해'와 같이 요청할 수 있습니다. `visualization`을 `"auto"`로 설정하면 기능이 사용 설정되지만, 에이전트는 프롬프트에서 시각적 요소를 요청하는 경우에만 시각적 요소를 생성합니다.

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

### 자바스크립트

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

## 지원되는 도구

Deep Research는 여러 기본 제공 도구와 외부 도구를 지원합니다. 기본적으로(`tools` 매개변수가 제공되지 않은 경우) 에이전트는 Google 검색, URL 컨텍스트, 코드 실행에 액세스할 수 있습니다. 에이전트의 기능을 제한하거나 확장할 도구를 명시적으로 지정할 수 있습니다.

| 도구 | 유형 값 | 설명 |
| --- | --- | --- |
| Google 검색 | `google_search` | 공개 웹을 검색합니다. 기본적으로 사용 설정됩니다. |
| URL 컨텍스트 | `url_context` | 웹페이지 콘텐츠를 읽고 요약합니다. 기본적으로 사용 설정됩니다. |
| 코드 실행 | `code_execution` | 코드를 실행하여 계산 및 데이터 분석을 수행합니다. 기본적으로 사용 설정됩니다. |
| MCP 서버 | `mcp_server` | 외부 도구 액세스를 위해 원격 MCP 서버에 연결 |
| 파일 검색 | `file_search` | 업로드된 문서 코퍼스를 검색합니다. |

### Google 검색

Google 검색을 유일한 도구로 명시적으로 사용 설정합니다.

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="What are the latest developments in quantum computing?",
    tools=[{"type": "google_search"}],
    background=True,
)
```

### 자바스크립트

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

### URL 컨텍스트

에이전트가 특정 웹페이지를 읽고 요약할 수 있도록 합니다.

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Summarize the content of https://www.wikipedia.org/.",
    tools=[{"type": "url_context"}],
    background=True,
)
```

### 자바스크립트

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

### 코드 실행

에이전트가 계산 및 데이터 분석을 위해 코드를 실행하도록 허용합니다.

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Calculate the 50th Fibonacci number.",
    tools=[{"type": "code_execution"}],
    background=True,
)
```

### 자바스크립트

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
    "input": "Calculate the 50th Fibonacci number.",
    "agent": "deep-research-preview-04-2026",
    "tools": [{"type": "code_execution"}],
    "background": true
}'
```

### MCP 서버

원격 MCP 서버에 연결하여 에이전트가 외부 도구 및 서비스에 액세스할 수 있도록 합니다.

도구 구성에서 서버 `name` 및 `url`을 제공합니다. 인증 사용자 인증 정보를 전달하고 에이전트가 호출할 수 있는 도구를 제한할 수도 있습니다.

| 필드 | 유형 | 필수 | 설명 |
| --- | --- | --- | --- |
| `type` | `string` | 예 | `"mcp_server"`이어야 합니다. |
| `name` | `string` | 아니요 | MCP 서버의 표시 이름입니다. |
| `url` | `string` | 아니요 | MCP 서버 엔드포인트의 전체 URL입니다. |
| `headers` | `object` | 아니요 | 서버에 대한 모든 요청과 함께 HTTP 헤더로 전송되는 키-값 쌍 (예: 인증 토큰)입니다. |
| `allowed_tools` | `array` | 아니요 | 에이전트가 호출할 수 있는 서버의 도구를 제한합니다. |

#### 기본 사용법

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

### 자바스크립트

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

### 파일 검색

[파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko) 도구를 사용하여 에이전트가 자체 데이터에 액세스할 수 있도록 합니다.

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

### 자바스크립트

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

## 조향성 및 서식

프롬프트에 구체적인 서식 지정 안내를 제공하여 에이전트의 출력을 유도할 수 있습니다. 이를 통해 보고서를 특정 섹션과 하위 섹션으로 구성하고, 데이터 표를 포함하거나, 다양한 잠재고객 (예: '기술', '임원', '일반')에 맞게 어조를 조정할 수 있습니다.

입력 텍스트에 원하는 출력 형식을 명시적으로 정의합니다.

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

### 자바스크립트

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

## 멀티모달 입력

Deep Research는 이미지와 문서 (PDF)를 비롯한 멀티모달 입력을 지원하므로 에이전트가 시각적 콘텐츠를 분석하고 제공된 입력에 따라 컨텍스트화된 웹 기반 조사를 수행할 수 있습니다.

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

### 자바스크립트

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

### 문서 이해

문서 이해를 사용하면 문서를 멀티모달 입력으로 직접 전달할 수 있습니다.
에이전트는 제공된 문서를 분석하고 콘텐츠에 기반한 조사를 수행합니다.

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

### 자바스크립트

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

## 장기 실행 작업 처리

Deep Research는 계획, 검색, 읽기, 쓰기와 관련된 다단계 프로세스입니다. 이 주기는 일반적으로 동기 API 호출의 표준 제한 시간을 초과합니다.

에이전트는 `background=True`를 사용해야 합니다. API는 부분 `Interaction` 객체를 즉시 반환합니다. `id` 속성을 사용하여 폴링을 위한 상호작용을 가져올 수 있습니다. 상호작용 상태가 `in_progress`에서 `completed` 또는 `failed`로 전환됩니다. 백그라운드 작업 관리에 관한 자세한 가이드는 [백그라운드 실행](https://ai.google.dev/gemini-api/docs/background-execution?hl=ko)을 참고하세요.

### 스트리밍

Deep Research는 생각 요약, 텍스트 출력, 생성된 이미지 등 연구 진행 상황에 관한 실시간 업데이트를 수신하기 위한 스트리밍을 지원합니다.
`stream=True` 및 `background=True`를 설정해야 합니다.

중간 추론 단계 (생각)와 진행 상황 업데이트를 받으려면 `agent_config`에서 `thinking_summaries`를 `"auto"`로 설정하여 **생각 요약**을 사용 설정해야 합니다. 이 기능이 없으면 스트림에서 최종 결과만 제공할 수 있습니다.

#### 스트림 이벤트 유형

| 이벤트 유형 | 델타 유형 | 설명 |
| --- | --- | --- |
| `step.delta` | `thought` | 에이전트의 중간 추론 단계입니다. |
| `step.delta` | `text` | 최종 텍스트 출력의 일부입니다. |
| `step.delta` | `image` | 생성된 이미지 (base64 인코딩) |

다음 예에서는 연구 작업을 시작하고 자동 재연결로 스트림을 처리합니다. 연결이 끊어지면 (예: 600초 시간 제한 후) 중단된 위치에서 다시 시작할 수 있도록 `interaction_id` 및 `last_event_id`를 추적합니다.

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

### 자바스크립트

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

## 후속 질문 및 상호작용

에이전트가 최종 보고서를 반환한 후 `previous_interaction_id`를 사용하여 대화를 계속할 수 있습니다. 이렇게 하면 전체 작업을 다시 시작하지 않고도 연구의 특정 섹션에 대한 설명, 요약 또는 자세한 설명을 요청할 수 있습니다.

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

### 자바스크립트

```
const interaction = await client.interactions.create({
    input: 'Can you elaborate on the second point in the report?',
    model: 'gemini-3.1-pro-preview',
    previous_interaction_id: 'COMPLETED_INTERACTION_ID'
});
console.log(interaction.steps.at(-1).content[0].text);
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

## Gemini Deep Research Agent를 사용해야 하는 경우

Deep Research는 모델이 아닌 **에이전트**입니다. 지연 시간이 짧은 채팅보다는 '분석가-인-어-박스' 접근 방식이 필요한 워크로드에 가장 적합합니다.

| 기능 | 표준 Gemini 모델 | Gemini Deep Research 에이전트 |
| --- | --- | --- |
| **지연 시간** | 초 | 분 (비동기/백그라운드) |
| **절차** | 생성 -> 출력 | 계획 -> 검색 -> 읽기 -> 반복 -> 출력 |
| **출력** | 대화형 텍스트, 코드, 짧은 요약 | 자세한 보고서, 긴 형식의 분석, 비교 표 |
| **용도** | 챗봇, 추출, 창의적 글쓰기 | 시장 분석, 실사, 문헌 검토, 경쟁 환경 |

## 에이전트 구성

Deep Research는 `agent_config` 매개변수를 사용하여 동작을 제어합니다.
다음 필드가 포함된 사전으로 전달합니다.

| 필드 | 유형 | 기본값 | 설명 |
| --- | --- | --- | --- |
| `type` | `string` | 필수 | `"deep-research"`이어야 합니다. |
| `thinking_summaries` | `string` | `"none"` | 스트리밍 중에 중간 추론 단계를 수신하려면 `"auto"`로 설정합니다. 사용 중지하려면 `"none"`로 설정합니다. |
| `visualization` | `string` | `"auto"` | 에이전트 생성 차트 및 이미지를 사용 설정하려면 `"auto"`로 설정합니다. 사용 중지하려면 `"off"`로 설정합니다. |
| `collaborative_planning` | `boolean` | `false` | 조사가 시작되기 전에 다중 턴 계획 검토를 사용 설정하려면 `true`로 설정합니다. |

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

### 자바스크립트

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

## 사용 가능 여부 및 가격 책정

Google AI Studio 및 Gemini API의 Interactions API를 사용하여 Gemini Deep Research Agent에 액세스할 수 있습니다.

가격은 기본 Gemini 모델과 에이전트가 사용하는 특정 도구를 기반으로 [사용한 만큼만 지불 모델](https://ai.google.dev/gemini-api/docs/pricing?hl=ko#pricing-for-agents)을 따릅니다. 요청이 하나의 출력으로 이어지는 표준 채팅 요청과 달리 Deep Research 작업은 에이전트형 워크플로입니다. 단일 요청으로 계획, 검색, 읽기, 추론의 자율 루프가 트리거됩니다.

### 예상 비용

비용은 필요한 연구의 깊이에 따라 다릅니다. 에이전트는 프롬프트에 답변하는 데 필요한 읽기 및 검색의 양을 자율적으로 결정합니다.

- **Deep Research** (`deep-research-preview-04-2026`): 중간 수준의 분석이 필요한 일반적인 질문의 경우 에이전트가 검색어 약 80개, 입력 토큰 약 250,000개 (50~70% 캐시됨), 출력 토큰 약 60,000개를 사용할 수 있습니다.
  - **예상 총액:** 작업당$1.00~$3.00
- **Deep Research Max** (`deep-research-max-preview-04-2026`): 심층적인 경쟁 환경 분석 또는 광범위한 실사를 위해 에이전트는 최대 ~160개의 검색어, ~900,000개의 입력 토큰 (~50~70% 캐시됨), ~80,000개의 출력 토큰을 사용할 수 있습니다.
  - **예상 총액:** 작업당$3.00~$7.00

## 안전 고려사항

에이전트가 웹과 비공개 파일에 액세스하도록 허용하려면 안전 위험을 신중하게 고려해야 합니다.

- **파일을 사용한 프롬프트 삽입:** 에이전트가 제공된 파일의 콘텐츠를 읽습니다. 업로드된 문서 (PDF, 텍스트 파일)가 신뢰할 수 있는 출처에서 제공된 것인지 확인합니다. 악성 파일에는 에이전트의 출력을 조작하기 위해 설계된 숨겨진 텍스트가 포함될 수 있습니다.
- **웹 콘텐츠 위험:** 에이전트가 공개 웹을 검색합니다. 강력한 안전 필터를 구현하고 있지만 에이전트가 악성 웹페이지를 접하고 처리할 위험이 있습니다. 소스 확인을 위해 대답에 제공된 `citations`를 검토하는 것이 좋습니다.
- **무단 반출:** 웹 탐색을 허용하는 경우 에이전트에게 민감한 내부 데이터를 요약해 달라고 요청할 때 주의해야 합니다.

## 권장사항

- **알 수 없는 항목에 대한 프롬프트:** 누락된 데이터를 처리하는 방법을 상담사에게 안내합니다.
  예를 들어 프롬프트에 *'2025년의 구체적인 수치를 사용할 수 없는 경우 추정하지 말고 예측치이거나 사용할 수 없다고 명시하세요'*를 추가합니다.
- **컨텍스트 제공:** 입력 프롬프트에 배경 정보나 제약 조건을 직접 제공하여 에이전트의 조사를 그라운딩합니다.
- **공동 계획 사용:** 복잡한 질문의 경우 실행 전에 조사 계획을 검토하고 다듬을 수 있도록 공동 계획을 사용 설정합니다.
- **멀티모달 입력:** Deep Research Agent는 멀티모달 입력을 지원합니다.
  비용이 증가하고 컨텍스트 윈도우 오버플로 위험이 있으므로 신중하게 사용하세요.

## 제한사항

- **맞춤 도구:** 현재 맞춤 함수 호출 도구를 제공할 수는 없지만, Deep Research 에이전트와 함께 원격 MCP (모델 컨텍스트 프로토콜) 서버를 사용할 수 있습니다.
- **구조화된 출력:** 현재 Deep Research 에이전트는 구조화된 출력을 지원하지 않습니다.
- **최대 조사 시간:** Deep Research 에이전트의 최대 조사 시간은 60분입니다. 대부분의 작업은 20분 이내에 완료됩니다.
- **저장소 요구사항:** `background=True`를 사용하는 에이전트 실행에는 `store=True`가 필요합니다.
- **Google 검색:** [Google 검색](https://ai.google.dev/gemini-api/docs/google-search?hl=ko)은 기본적으로 사용 설정되어 있으며 그라운딩된 결과에는 [특정 제한사항](https://ai.google.dev/gemini-api/terms?hl=ko#use-restrictions2)이 적용됩니다.

## 다음 단계

- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)에 대해 자세히 알아보세요.
- [파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko) 도구를 사용하여 자체 데이터를 사용하는 방법을 알아보세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-14(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-14(UTC)"],[],[]]
