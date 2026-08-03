---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ko
fetched_at: 2026-08-03T04:39:05.703615+00:00
title: "\uad00\ub9ac \uc5d0\uc774\uc804\ud2b8 \ube60\ub978 \uc2dc\uc791 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 관리 에이전트 빠른 시작

이 가이드에서는 [Antigravity 에이전트](https://ai.google.dev/gemini-api/docs/agents/antigravity-agent?hl=ko)를 사용하여 Gemini API에서 관리형 에이전트를 만들고 사용하는 방법을 안내합니다. 첫 번째 에이전트 호출을 하고, 멀티턴 대화를 계속하고, 응답을 스트리밍하고, 샌드박스에서 파일을 다운로드하고, Antigravity 관리형 에이전트를 사용합니다.

## 첫 번째 에이전트 상호작용 실행

[Interactions API](https://ai.google.dev/gemini-api/docs?hl=ko)를 한 번 호출하면 Linux 샌드박스가 프로비저닝되고, 에이전트 루프가 실행되고, 결과가 반환됩니다. 다음 세 가지 매개변수를 정의합니다.

- 미리 정의된 범용 관리형 에이전트의 현재 버전인 `agent`를 `"antigravity-preview-05-2026",`으로 전달합니다.
- 새 샌드박스 환경을 프로비저닝하려면 `environment="remote"`를 정의합니다.
- 에이전트가 수행할 작업을 정의하는 입력을 만듭니다.

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

응답은 `Interaction` 객체를 반환합니다. 동일한 샌드박스에서 대화를 계속하려면 `interaction.id` 및 `interaction.environment_id`를 저장합니다. `interaction.output_text`를 사용하여 에이전트의 최종 응답에 액세스합니다. `interaction.steps`는 에이전트가 수행한 각 단계 (추론, 도구 호출, 코드 실행)를 나열합니다.

## 대화 계속 (멀티턴)

API는 두 가지 독립적인 상태 측정기준을 추적합니다.

- **대화 컨텍스트:** 채팅 기록, 추론 추적, 도구 사용, `previous_interaction_id` 사용
- [**환경 상태:**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko) 파일, 설치된 패키지, 샌드박스 상태, `environment` 사용

각각의 위치에 전달하여 다시 시작합니다.

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

턴 1의 파일 (`fibonacci.txt`)은 턴 2에도 유지됩니다. 에이전트는 대화 컨텍스트도 유지합니다.

다음과 같이 독립적으로 혼합하고 일치시킬 수 있습니다.

- **대화 삭제, 파일 유지:** `previous_interaction_id`를 생략하고 동일한 작업공간에서 새 대화를 위해 `environment`를 사용하여 환경 ID만 전달합니다.
- **대화 유지, 새 작업공간:** `previous_interaction_id`를 전달하고 새 샌드박스에 `environment="remote"`를 설정합니다.

### 자동 컨텍스트 압축

장기 실행 멀티턴 대화에서 추론 단계, 도구 호출, 대용량 파일 콘텐츠의 원시 기록은 빠르게 증가하고 상당한 컨텍스트 공간을 사용할 수 있습니다. 토큰 한도 오류를 방지하고 에이전트의 집중을 유지하기 위해 (컨텍스트 손상 방지) 관리형 에이전트 API는 약 135,000개의 토큰에서 기본 컨텍스트 압축 단계를 제공합니다. 이 작업은 자동으로 진행되며

## 응답 스트리밍

장기 실행 작업의 경우 응답을 스트리밍하여 에이전트가 실시간으로 작동하는 것을 확인할 수 있습니다.

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

스트리밍은 증분 업데이트가 포함된 단계 델타를 반환합니다. 단계가 완료되면 `step.stop` 이벤트에 누적된 사용 통계가 포함됩니다. 자세한 내용은
[스트리밍 가이드](https://ai.google.dev/gemini-api/docs/streaming?hl=ko)를 참고하세요.

## 환경에서 파일 다운로드

에이전트가 샌드박스 내에서 파일을 만들 때. 직접 HTTP 요청으로 Files API를 사용하여 다운로드합니다 (아직 SDK 메서드 없음).

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

## 관리형 에이전트 저장

이전 단계에서는 기본 Antigravity 에이전트를 사용하고 인라인으로 맞춤설정했습니다. 구성 (안내, 기술, 모델 선택, 환경)을 반복한 후 재사용 가능한 관리형 에이전트로 저장할 수 있습니다. 이렇게 하면 구성을 반복하지 않고 ID로 호출할 수 있습니다.

에이전트를 저장할 때 인라인 상호작용과의 아키텍처 대칭에 유의하세요. `base_agent: "antigravity-preview-05-2026"`을 지정하고 `interactions.create`에서와 마찬가지로 선택한 `model`로 `agent_config`를 전달할 수 있습니다. 또한 소스에서 또는 기존 환경을 포크하여 `base_environment`를 정의합니다. 에이전트는 모든 새 상호작용에 이 환경 및 모델 구성을 사용합니다.

**소스에서:** 소스를 인라인으로 또는 GitHub나 Cloud Storage와 같은 다른 소스에서 정의합니다.

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

## 관리형 에이전트 호출

관리형 에이전트를 저장한 후 ID로 호출할 수 있습니다. 각 호출은 기본 환경을 포크하므로 모든 실행이 깨끗하게 시작됩니다.

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

## 다음 단계

- [Antigravity 에이전트](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ko): 기능, 지원되는 도구, 멀티모달 입력, 가격 책정, 제한사항
- [관리형 에이전트 빌드](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ko): 자체 안내, 기술, 데이터로 Antigravity 확장
- [환경](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko): 소스, 네트워킹, 수명 주기, 리소스 한도
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko): 모델 및 에이전트의 기본 API

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-30(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-30(UTC)"],[],[]]
