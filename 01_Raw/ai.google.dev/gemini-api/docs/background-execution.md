---
source_url: https://ai.google.dev/gemini-api/docs/background-execution?hl=ko
fetched_at: 2026-07-20T04:40:22.972120+00:00
title: "\ubc31\uadf8\ub77c\uc6b4\ub4dc \uc2e4\ud589 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 백그라운드 실행

심층 연구, 복잡한 추론 또는 다단계 에이전트 실행과 같은 장기 실행 작업의 경우 연결 시간 제한으로 인해 표준 HTTP 요청이 중단될 수 있습니다 (일반적으로 60초 후에 닫힘). [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)는 이러한 작업을 비동기식으로 실행하는 **백그라운드 실행**을 제공합니다.

상호작용이 서버에서 작업을 완료할 때까지 실행되도록 하려면 상호작용을 만들 때 `"background": true`를 설정합니다. API는 즉시 상호작용 ID를 반환하며, 클라이언트 애플리케이션은 이 ID를 사용하여 상태를 폴링하거나, 진행 상황을 스트리밍하거나, 연결이 끊어진 스트림에 다시 연결할 수 있습니다.

백그라운드 실행은 표준 Gemini 모델 (예: `gemini-3.5-flash`, `gemini-3.1-pro-preview`) 및 관리형 에이전트 (예: `antigravity-preview-05-2026`)에서 지원됩니다.

## 백그라운드 상호작용 만들기

백그라운드 상호작용을 시작하려면 리소스를 만들 때 `background` 매개변수를 `true`로 설정합니다.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Write a guide on space exploration.",
    background=True,
)
print(f"Created background interaction ID: {interaction.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Write a guide on space exploration.",
    background: true,
});
console.log(`Created background interaction ID: ${interaction.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Write a guide on space exploration.",
    "background": true
  }'
```

## 백그라운드 실행 작동 방식

백그라운드 상호작용을 만들면 작업이 서버에서 비동기식으로 실행됩니다. 상호작용은 다양한 실행 상태를 거칩니다.

- `in_progress`: 서버가 상호작용을 적극적으로 실행하고 있습니다 (예: 코드 실행 또는 연구).
- `requires_action`: 상호작용이 일시중지되었으며 클라이언트 입력 (예: 도구 실행 확인 또는 질문 답변)을 기다리고 있습니다.
- `completed`: 상호작용이 성공적으로 완료되었으며 출력을 사용할 수 있습니다.
- `failed`: 실행 중에 오류가 발생했습니다 (예: 도구 실패 또는 비율 제한).
- `cancelled`: 클라이언트 요청으로 실행이 중지되었습니다.

### 사용 사례

백그라운드 실행은 다음 용도로 사용합니다.

- **에이전트 실행:** 코드 실행, 웹브라우징 또는 하위 에이전트 오케스트레이션이 필요한 작업 (예: `antigravity-preview-05-2026`).
- **심층 연구:** 몇 분이 걸리는 `deep-research-preview-04-2026` 또는 `deep-research-max-preview-04-2026`을 사용하여 실행합니다.
- **긴 추론:** 모델 사고 단계가 표준 HTTP 연결 한도를 초과하는 작업.

## 결과 검색

**폴링** 또는 **스트리밍** 을 사용하여 백그라운드 상호작용 결과를 가져옵니다.

### 폴링 패턴 (비차단)

폴링은 종료 상태에 도달할 때까지 비차단 GET 요청을 사용하여 상호작용 상태를 주기적으로 확인합니다.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.get(id="YOUR_INTERACTION_ID")

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

let interaction = await client.interactions.get("YOUR_INTERACTION_ID");

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

if (interaction.status === "completed") {
    console.log(interaction.output_text);
} else {
    console.log(`Finished with status: ${interaction.status}`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

### 스트리밍 패턴

네트워크 중단으로 인해 스트림 연결이 끊어지면 스트리밍이 마지막으로 수신된 이벤트부터 다시 시작될 수 있습니다. 각 델타에는 페이로드에 고유한 `event_id`가 포함되어 있습니다. 이 ID를 `last_event_id`로 전달하면 해당 이벤트부터 스트림이 다시 시작됩니다.

### Python

```
import time
from google import genai

client = genai.Client()
interaction_id = "YOUR_INTERACTION_ID"

def stream_with_reconnect(interaction_id: str):
    last_event_id = None
    while True:
        try:
            # Retrieve the stream. If resuming, pass last_event_id
            stream = client.interactions.get(
                id=interaction_id,
                stream=True,
                last_event_id=last_event_id
            )

            for event in stream:
                # Log event updates and capture event_id if present
                if event.event_id:
                    last_event_id = event.event_id

                if event.event_type == "step.delta" and event.delta.type == "text":
                    print(event.delta.text, end="", flush=True)

                if event.event_type == "interaction.completed":
                    return

        except Exception as e:
            print(f"\n[Connection lost: {e}. Reconnecting in 3s...]")
            time.sleep(3)

stream_with_reconnect(interaction_id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const interactionId = "YOUR_INTERACTION_ID";

async function streamWithReconnect(id) {
    let lastEventId = undefined;
    while (true) {
        try {
            // Retrieve the stream. If resuming, pass last_event_id in options
            const stream = await client.interactions.get(id, {
                stream: true,
                last_event_id: lastEventId
            });

            for await (const event of stream) {
                // Capture event_id if present
                const idVal = event.event_id || event.id;
                if (idVal) {
                    lastEventId = idVal;
                }

                if (event.event_type === "step.delta" && event.delta?.type === "text") {
                    process.stdout.write(event.delta.text);
                }

                if (event.event_type === "interaction.completed") {
                    return;
                }
            }
        } catch (error) {
            console.log(`\n[Connection lost: ${error.message}. Reconnecting in 3s...]`);
            await new Promise(resolve => setTimeout(resolve, 3000));
        }
    }
}

await streamWithReconnect(interactionId);
```

### REST

```
curl -N -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID?stream=true&last_event_id=YOUR_LAST_EVENT_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## 멀티턴 대화

후속 상호작용은 다음 제약 조건에 따라 `previous_interaction_id`를 사용하여 백그라운드 대화에 연결할 수 있습니다.

1. **활성 실행이 차단됨:** 후속 상호작용을 `in_progress` 상태의 상호작용에 연결하면 `400 Bad Request` 오류가 반환됩니다. 상호작용이 `completed` 상태에 도달할 때까지 기다린 후 다음 상호작용을 시작합니다.
2. **관리형 에이전트의 환경 매개변수:** 관리형 에이전트 (예: `antigravity-preview-05-2026`)의 상호작용을 연결할 때 요청에 `previous_interaction_id`와 `environment`가 모두 포함되어야 합니다.

다음 예에서는 상호작용을 연결하는 방법을 보여줍니다.

### Python

```
import time
from google import genai

client = genai.Client()
agent_model = "antigravity-preview-05-2026"

# First interaction: Provision sandbox environment and execute first instruction
interaction1 = client.interactions.create(
    model=agent_model,
    input="Create a folder named project/ and write hello.py inside.",
    environment="remote",
    background=True
)

# Wait for completion
while True:
    check = client.interactions.get(id=interaction1.id)
    if check.status != "in_progress":
        break
    time.sleep(2)

# Second interaction: Chain using previous_interaction_id and environment
interaction2 = client.interactions.create(
    model=agent_model,
    input="List all files in the project/ directory.",
    previous_interaction_id=interaction1.id,
    environment="remote",
    background=True
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const agentModel = "antigravity-preview-05-2026";

// First interaction: Provision sandbox environment and execute first instruction
const interaction1 = await client.interactions.create({
    model: agentModel,
    input: "Create a folder named project/ and write hello.py inside.",
    environment: "remote",
    background: true
});

// Wait for completion
while (true) {
    const check = await client.interactions.get(interaction1.id);
    if (check.status !== "in_progress") {
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 2000));
}

// Second interaction: Chain using previous_interaction_id and environment
const interaction2 = await client.interactions.create({
    model: agentModel,
    input: "List all files in the project/ directory.",
    previous_interaction_id: interaction1.id,
    environment: "remote",
    background: true
});
```

### REST

```
# Chain second interaction (Make sure FIRST_INTERACTION_ID has status 'completed')
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "antigravity-preview-05-2026",
    "input": "List all files in the project/ directory.",
    "previous_interaction_id": "FIRST_INTERACTION_ID",
    "environment": "remote",
    "background": true
  }'
```

## 취소 및 삭제

취소 및 삭제 요청을 사용하여 실행 중인 실행을 제어하고 스토리지를 관리합니다.

- **취소 (`POST /interactions/{id}/cancel`):** 실행 중인 작업을 중지합니다. 상태가 `cancelled`로 전환됩니다. 서버에서 정리 작업을 수행하면 GET 요청에서 상태가 업데이트되기 전에 약간의 지연이 발생할 수 있습니다.
- **삭제 (`DELETE /interactions/{id}`):** 서버에서 상호작용 레코드를 삭제합니다. 후속 GET 요청은 `404 Not Found` 오류를 반환합니다.

### Python

```
from google import genai

client = genai.Client()

# Cancel a running interaction
client.interactions.cancel(id="YOUR_INTERACTION_ID")

# Delete the interaction record entirely
client.interactions.delete(id="YOUR_INTERACTION_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Cancel a running interaction
await client.interactions.cancel("YOUR_INTERACTION_ID");

// Delete the interaction record entirely
await client.interactions.delete("YOUR_INTERACTION_ID");
```

### REST

```
# Cancel the interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID/cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"

# Delete the interaction
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## 다음 단계

- 세션 및 상태 관리를 이해하려면 [Interactions API 개요](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)를 읽어보세요.
- 실시간 이벤트 업데이트에 관한 자세한 내용은 [스트리밍 상호작용](https://ai.google.dev/gemini-api/docs/streaming?hl=ko) 가이드를 참고하세요.
- [관리형 에이전트 빠른 시작](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ko)을 살펴보고 상태 저장 멀티턴 에이전트를 빌드하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-06-26(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-06-26(UTC)"],[],[]]
