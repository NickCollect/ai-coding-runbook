---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ko
fetched_at: 2026-06-01T06:02:41.654952+00:00
title: "Antigravity Agent \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Antigravity Agent

Antigravity 에이전트는 Gemini API의 범용 관리형 에이전트입니다. 단일 API 호출을 통해 Google에서 호스팅하는 자체 보안 Linux 샌드박스 내에서 추론하고, 코드를 실행하고, 파일을 관리하고, 웹을 탐색하는 에이전트를 얻을 수 있습니다.

Gemini 3.5 Flash로 구동되며 Antigravity IDE와 동일한 하네스를 사용합니다. [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ko) 및 [Google AI Studio](https://aistudio.google.com?hl=ko)를 통해 사용할 수 있습니다.

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
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## 기능

각 호출은 Linux 샌드박스를 프로비저닝하고 도구 사용 루프를 시작할 수 있습니다. 에이전트는 태스크가 완료될 때까지 계획하고, 행동하고, 결과를 관찰하고, 반복합니다.

- **코드 실행:** Bash, Python, Node.js 명령어를 실행합니다. 패키지를 설치하고, 테스트를 실행하고, 앱을 빌드합니다.
- **파일 관리:** 샌드박스에서 파일을 읽고, 쓰고, 수정하고, 검색하고, 나열합니다. 파일은 상호작용 전반에 걸쳐 유지됩니다.
- **웹 액세스:** 데이터용 Google 검색 및 URL 가져오기.
- **컨텍스트 압축:** 컨텍스트를 잃거나 토큰 한도에 도달하지 않고 장기 실행 다중 턴 세션을 지원하기 위한 자동 컨텍스트 압축 (~135, 000개 토큰에서 트리거됨).

다중 턴 사용 및 스트리밍에 관한 [빠른 시작](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ko)을 참고하세요.

## 지원되는 도구

기본적으로 에이전트는 `code_execution`, `google_search`, `url_context`에 액세스할 수 있습니다. `environment` 매개변수를 지정하면 파일 시스템 도구가 자동으로 사용 설정됩니다. 기본 집합을 맞춤설정하거나 제한할 때만 `tools` 매개변수를 지정하면 됩니다.

| 도구 | 유형 값 | 설명 |
| --- | --- | --- |
| 코드 실행 | `code_execution` | stdout/stderr 캡처를 사용하여 셸 명령어 (bash, Python, Node)를 실행합니다. |
| Google 검색 | `google_search` | 공개 웹을 검색합니다. |
| URL 컨텍스트 | `url_context` | 웹페이지를 가져오고 읽습니다. |
| 파일 시스템 | *(`environment`를 통해 사용 설정됨)* | 샌드박스에서 파일을 읽고, 쓰고, 수정하고, 검색하고, 나열합니다. 별도의 도구 유형이 없으며 `environment`가 설정되면 자동으로 사용 설정됩니다. |

에이전트를 특정 도구로 제한하려면 필요한 도구만 전달하세요.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Search for the latest AI research papers on reasoning and summarize them.",
    environment="remote",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"},
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Search for the latest AI research papers on reasoning and summarize them.",
    environment: "remote",
    tools: [
        { type: "google_search" },
        { type: "url_context" },
    ],
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Search for the latest AI research papers on reasoning and summarize them.",
    "environment": "remote",
    "tools": [
        {"type": "google_search"},
        {"type": "url_context"}
    ]
}'
```

## 멀티모달 입력

Antigravity 에이전트는 멀티모달 입력을 지원합니다. 현재는 `text` 및 `image` 입력만 지원됩니다. 이미지는 인라인 base64 인코딩 문자열 (`data`)로 제공되어야 합니다.

### Python

```
import base64
from google import genai

client = genai.Client()

with open("path/to/chart.png", "rb") as f:
    image_bytes = f.read()

interaction_inline = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=[
        {"type": "text", "text": "Analyze this chart and summarize the trends."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png",
        },
    ],
    environment="remote",
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64Image = fs.readFileSync("path/to/chart.png", { encoding: "base64" });

const interactionInline = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: [
        { type: "text", text: "Analyze this chart and summarize the trends." },
        {
            type: "image",
            data: base64Image,
            mime_type: "image/png",
        },
    ],
    environment: "remote",
}, { timeout: 300000 });
```

### REST

```
BASE64_IMAGE=$(base64 -w0 /path/to/chart.png)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d "{
    \"agent\": \"antigravity-preview-05-2026\",
    \"input\": [
        {\"type\": \"text\", \"text\": \"Analyze this chart and summarize the trends.\"},
        {
            \"type\": \"image\",
            \"mime_type\": \"image/png\",
            \"data\": \"$BASE64_IMAGE\"
        }
    ],
    \"environment\": \"remote\"
}"
```

## 에이전트 맞춤설정

안내, 도구, 환경을 맞춤설정하여 Antigravity 에이전트를 확장할 수 있습니다. 에이전트는 파일 시스템 기본 맞춤설정 접근 방식을 지원합니다. 안내 및 기술을 위한 `AGENTS.md`와 같은 파일을 `.agents/skills/` 아래의 샌드박스에 직접 마운트하거나 상호작용 시 인라인으로 구성을 전달할 수 있습니다. 구성을 인라인으로 반복한 후 준비가 되면 관리형 에이전트로 저장할 수 있습니다.

커스텀 에이전트를 빌드하는 방법에 관한 자세한 내용은 [관리형 에이전트 빌드](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ko)를 참고하세요.

## 환경

각 호출은 Linux 샌드박스를 만들거나 재사용합니다. `environment` 매개변수는 세 가지 형식을 취합니다.

| 자세 | 설명 |
| --- | --- |
| `"remote"` | 기본 설정으로 새 샌드박스를 프로비저닝합니다. |
| `"env_abc123"` | 모든 파일과 상태를 보존하여 기존 환경을 ID별로 재사용합니다. |
| `{...}` | 커스텀 소스 및 네트워크 규칙이 포함된 전체 `EnvironmentConfig`입니다. |

소스 (Git, GCS, 인라인), 네트워킹, 수명 주기, 리소스 한도에 관한 자세한 내용은 [환경](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko)을 참고하세요.

## 사용 가능 여부 및 가격 책정

Antigravity 에이전트는 Google AI Studio 및 Gemini API의 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ko)를 통해 프리뷰로 제공됩니다.

가격은 기본 Gemini 모델 토큰과 에이전트가 사용하는 도구를 기반으로 [사용한 만큼만 지불 모델](https://ai.google.dev/gemini-api/docs/pricing?hl=ko#pricing-for-agents)을 따릅니다. 단일 출력을 생성하는 표준 채팅 요청과 달리 Antigravity 상호작용은 에이전트형 워크플로입니다. 단일 요청은 추론, 도구 실행, 코드 실행, 파일 관리의 자율 루프를 트리거합니다.

### 예상 비용

비용은 태스크 복잡성에 따라 다릅니다. 에이전트는 필요한 도구 호출, 코드 실행, 파일 작업 수를 자율적으로 결정합니다. 다음 예상치는 실행을 기반으로 합니다.

| 태스크 카테고리 | 입력 토큰 | 출력 토큰 | 일반적인 비용 |
| --- | --- | --- | --- |
| **연구 및 정보 합성** | 100,000~500,000 | 10,000~40,000 | $0.30~$1.00 |
| **문서 및 콘텐츠 생성** | 100,000~500,000 | 15,000~50,000 | $0.30~$1.30 |
| **프로세스 및 시스템 설계** | 100,000~400,000 | 10,000~30,000 | $0.25~$0.80 |
| **데이터 처리 및 분석** | 300,000~3,000,000 | 30,000~150,000 | $0.70~$3.25 |

일반적으로 입력 토큰의 50~70% 가 캐시됩니다. 도구 호출이 많은 복잡한 에이전트 워크플로는 단일 상호작용에서 300만~500만 개의 토큰을 누적할 수 있으며 비용은 최대 약$5입니다.

프리뷰 기간에는 **환경 컴퓨팅** (CPU, 메모리, 샌드박스 실행)에 **요금이 청구되지 않습니다**.

## 제한사항

- **프리뷰 상태:** Antigravity 에이전트와 Interactions API는 프리뷰로 제공됩니다. 기능과 스키마는 변경될 수 있습니다.
- **지원되지 않는 생성 구성:** 다음 매개변수는 지원되지 않으며 400 오류를 반환합니다. `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **구조화된 출력:** Antigravity 에이전트는 구조화된 출력을 지원하지 않습니다.
- **사용할 수 없는 도구:** `file_search`, `computer_use`, `google_maps`, `function_calling`, `mcp`는 아직 지원되지 않습니다.
- **파일 시스템 도구:** 현재 파일 시스템 도구가 없습니다. 이는 `environment`의 일부입니다.
- **백그라운드:** 에이전트는 `background=True` 사용을 지원하지 않으며 `store=True`가 필요합니다.
- **지원되지 않는 멀티모달 유형.** 현재 오디오, 동영상, 문서 입력은 지원되지 않습니다. 텍스트와 이미지만 허용됩니다.

## 다음 단계

- [빠른 시작](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ko): 다중 턴 대화 및 스트리밍.
- [커스텀 에이전트 빌드](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ko): 커스텀 안내, 기술, 에이전트 저장.
- [환경](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko): 샌드박스 구성, 소스, 네트워킹.
- [Deep Research Agent](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=ko): 장문 연구 태스크.
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ko): 기본 API.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-20(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-20(UTC)"],[],[]]
