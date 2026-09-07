---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tool-combination?hl=ko
fetched_at: 2026-09-07T05:41:18.420200+00:00
title: "\uae30\ubcf8 \uc81c\uacf5 \ub3c4\uad6c\uc640 \ud568\uc218 \ud638\ucd9c \uacb0\ud569 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 기본 제공 도구와 함수 호출 결합

[모델에서만 지원됩니다.](https://ai.google.dev/gemini-api/docs/models?hl=ko#gemini-3)

Gemini를 사용하면 도구 호출의 컨텍스트 기록을 보존하고 노출하여 단일 생성에서 [기본 제공 도구](https://ai.google.dev/gemini-api/docs/tools?hl=ko)(예: `google_search`)와 [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)(*커스텀 도구*라고도 함)을 결합할 수 있습니다. 기본 제공 도구와 커스텀 도구 조합을 사용하면 모델이 특정 비즈니스 로직을 호출하기 전에 실시간 웹 데이터를 기반으로 할 수 있는 복잡한 에이전트 워크플로가 가능합니다.

`google_search` 및 커스텀 함수 `getWeather`를 사용하여 기본 제공 도구와 커스텀 도구 조합을 사용 설정하는 예는 다음과 같습니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
response = client.models.generate_content(
    model="gemini-3.7-flash",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),  # Built-in tool
                function_declarations=[getWeather],  # Custom tool
            ),
        ],
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)
function_call_id = None
for part in response.candidates[0].content.parts:
    if part.function_call:
        print(f"Function call: {part.function_call.name} (ID: {part.function_call.id})")
        function_call_id = part.function_call.id

# Turn 2: Manually build history to circulate both tool and function context
history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    # Response from Turn 1 includes tool_call, tool_response, and thought_signatures
    response.candidates[0].content,
    # Return the function_response
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=function_call_id # Match the ID from the function_call
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3.7-flash",
    contents=history,
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),
                function_declarations=[getWeather]
            ),
        ],
        # This flag needs to be enabled for built-in tool context circulation and tool combination
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)

for part in response_2.candidates[0].content.parts:
    if part.text:
        print(part.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: Type.OBJECT,
        properties: {
            location: {
                type: Type.STRING,
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    // This flag needs to be enabled for built-in tool context circulation and tool combination
    const toolConfig = { includeServerSideToolInvocations: true };

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    const response1 = await client.models.generateContent({
        model: "gemini-3.7-flash",
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });

    for (const part of response1.candidates[0].content.parts) {
        if (part.functionCall) {
            console.log(`Function call: ${part.functionCall.name} (ID: ${part.functionCall.id})`);
        }
    }

   const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    // Turn 2: Manually build history to circulate both tool and function context
    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        // Response from Turn 1 includes tool_call, tool_response, and thought_signatures
        response1.candidates[0].content,
        // Return the function_response
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId // Match the ID from the function_call
                }
            }]
        }
    ];

    const response2 = await client.models.generateContent({
        model: "gemini-3.7-flash",
        contents: history,
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });

    for (const part of response2.candidates[0].content.parts) {
        if (part.text) {
            console.log(part.text);
        }
    }
}

run();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/generative-ai-go/genai"
    "google.golang.org/api/option"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, option.WithAPIKey(os.Getenv("GEMINI_API_KEY")))
    if err != nil {
        log.Exit(err)
    }
    defer client.Close()

    getWeather := &genai.FunctionDeclaration{
        Name:        "getWeather",
        Description: "Get the weather in a given location",
        Parameters: &genai.Schema{
            Type: genai.Object,
            Properties: map[string]*genai.Schema{
                "location": {
                    Type:        genai.String,
                    Description: "The city and state, e.g. San Francisco, CA",
                },
            },
            Required: []string{"location"},
        },
    }

    model := client.GenerativeModel("gemini-3.7-flash")
    model.Tools = []*genai.Tool{
        {GoogleSearch: &genai.GoogleSearch{}}, // Built-in tool
        {FunctionDeclarations: []*genai.FunctionDeclaration{getWeather}}, // Custom tool
    }
    ist := true
    model.ToolConfig = &genai.ToolConfig{
        IncludeServerSideToolInvocations: &ist, // This flag needs to be enabled for built-in tool context circulation and tool combination
    }

    chat := model.StartChat()

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    prompt := genai.Text("What is the northernmost city in the United States? What's the weather like there today?")
    resp1, err := chat.SendMessage(ctx, prompt)
    if err != nil {
        log.Exitf("SendMessage failed: %v", err)
    }

    if resp1 == nil || len(resp1.Candidates) == 0 || resp1.Candidates[0].Content == nil {
        log.Exit("empty response from model")
    }

    var functionCallID string
    for _, part := range resp1.Candidates[0].Content.Parts {
        switch p := part.(type) {
        case genai.FunctionCall:
            fmt.Printf("Function call: %s (ID: %s)\n", p.Name, p.ID)
            if p.Name == "getWeather" {
                functionCallID = p.ID
            }
        }
    }

    if functionCallID == "" {
        log.Exit("no getWeather function call in response")
    }

    // Turn 2: Provide function result back to model.
    // Chat history automatically includes tool_call, tool_response, and thought_signatures from Turn 1.
    fr := genai.FunctionResponse{
        Name: "getWeather",
        ID:   functionCallID,
        Response: map[string]any{
            "response": "Very cold. 22 degrees Fahrenheit.",
        },
    }

    resp2, err := chat.SendMessage(ctx, fr)
    if err != nil {
        log.Exitf("SendMessage for turn 2 failed: %v", err)
    }

    if resp2 == nil || len(resp2.Candidates) == 0 || resp2.Candidates[0].Content == nil {
        log.Exit("empty response from model in turn 2")
    }

    for _, part := range resp2.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Println(string(txt))
        }
    }
}
```

### REST

```
# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.7-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What is the northernmost city in the United States? What'\''s the weather like there today?"
    }]
  }],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'

# Turn 2: Manually build history to circulate both tool and function context
# The following request assumes you have captured candidates[0].content from Turn 1 response,
# and extracted function_call.id for getWeather.
# Replace FUNCTION_CALL_ID and insert candidate content from turn 1.
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.7-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [
    {
      "role": "user",
      "parts": [{"text": "What is the northernmost city in the United States? What'\''s the weather like there today?"}]
    },
    YOUR_CANDIDATE_CONTENT_FROM_TURN_1_RESPONSE,
    {
      "role": "user",
      "parts": [{
        "functionResponse": {
          "name": "getWeather",
          "id": "FUNCTION_CALL_ID",
          "response": {"response": "Very cold. 22 degrees Fahrenheit."}
        }
      }]
    }
  ],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'
```

## 작동 방식

Gemini 3 모델은 *도구 컨텍스트 순환* 을 사용하여 기본 제공 도구와 커스텀 도구 조합을 사용 설정합니다. 도구 컨텍스트 순환을 사용하면 기본 제공 도구의 컨텍스트를 보존하고 노출하여 턴마다 동일한 호출에서 커스텀 도구와 공유할 수 있습니다.

### 도구 조합 사용 설정

- 도구 컨텍스트 순환을 사용 설정하려면 `include_server_side_tool_invocations` 플래그를 `true`로 설정해야 합니다.
- 사용하려는
  기본 제공 도구와 함께 [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko#function-declarations)를 포함하여 조합 동작을 트리거합니다.
  - `function_declarations`를 포함하지 않더라도 플래그가 설정되어 있는 한 도구 컨텍스트 순환은 포함된 기본 제공 도구에 계속 적용됩니다.

### API가 파트를 반환함

단일 응답에서 API는 기본 제공 도구 호출의 `toolCall` 및 `toolResponse` 파트를 반환합니다. 함수 (커스텀 도구) 호출의 경우 API는 `functionCall` 호출 파트를 반환하며, 사용자는 다음 턴에서 `functionResponse` 파트를 제공합니다.

- `toolCall` 및 `toolResponse`: API는 이러한 파트를 반환하여 다음 턴을 위해 서버 측에서 실행되는 도구의 컨텍스트와 실행 결과를 보존합니다.
- `functionCall` 및 `functionResponse`: API는 사용자가 작성할 함수 호출을 사용자에게 전송하고 사용자는 함수 응답에서 결과를 다시 전송합니다. 이러한 파트는 도구 조합 기능에 고유한 것이 아니라 Gemini API의 모든 [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)에 표준입니다.
- ([코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko) 도구만 해당)
  `executableCode` 및 `codeExecutionResult`:
  코드 실행 도구를 사용하는 경우 API는 `functionCall` 및
  `functionResponse` 대신 `executableCode` (실행되도록 모델에서 생성된 코드)와 `codeExecutionResult` (실행 가능한 코드의 결과)를 반환합니다.

컨텍스트를 유지하고 도구
조합을 사용 설정하려면 각 턴에서 포함된 모든 [필드](#critical-fields)를 포함한 모든 파트를 모델에 다시 반환해야 합니다.

### 반환된 파트의 중요 필드

API에서 반환된 특정 [파트](#api-returns-parts)에는 `id`,
`tool_type`, 및 `thought_signature` 필드가 포함됩니다. 이러한 필드는 도구 컨텍스트를 유지하는 데 중요하며 따라서 도구 조합에 중요합니다. 후속 요청에서 *응답에 제공된 대로* 모든 파트를 반환해야 합니다.

- `id`: 호출을 응답에 매핑하는 고유 식별자입니다. `id`는 도구 컨텍스트 순환과 관계없이 **모든 함수 호출 응답에 설정** 됩니다.
  API가 함수 호출에서 제공하는 것과 동일한 `id`를 함수 응답에서 제공*해야* 합니다. 기본 제공 도구는 도구 호출과 도구 응답 간에 `id`를 자동으로 공유합니다.
  - 모든 도구 관련 파트에서 찾을 수 있음: `toolCall`, `toolResponse`, `functionCall`, `functionResponse`, `executableCode`, `codeExecutionResult`
- `tool_type`: 사용 중인 특정 도구를 식별합니다. 리터럴 기본 제공 도구 또는 (예: `URL_CONTEXT`) 또는 함수 (예: `getWeather`) 이름입니다.
  - `toolCall` 및 `toolResponse` 파트에서 찾을 수 있습니다.
- `thought_signature`: **API에서 반환된 각 파트** 에 삽입된 실제 암호화된 컨텍스트입니다. 사고 서명 없이는 컨텍스트를 재구성할 수 없습니다. 모든 턴에서 모든 파트의 사고 서명을 반환하지 않으면 모델에서 오류가 발생합니다.
  - *모든* 파트에서 찾을 수 있습니다.

### 도구별 데이터

일부 기본 제공 도구는 도구 유형에 고유한 사용자에게 표시되는 데이터 인수를 반환합니다.

| 도구 | 사용자에게 표시되는 도구 호출 인수 (있는 경우) | 사용자에게 표시되는 도구 응답 (있는 경우) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` 탐색할 URL | `urls_metadata` `retrieved_url`: 탐색된 URL `url_retrieval_status`: 탐색 상태 |
| **FILE\_SEARCH** | 없음 | 없음 |

## 도구 조합 요청 구조 예

다음 요청 구조는 '미국에서 가장 북쪽에 있는 도시는 어디인가요? 오늘 날씨는 어떤가요?'라는 프롬프트의 요청 구조를 보여줍니다. 기본 제공 Gemini 도구 `google_search` 및 `code_execution`과 커스텀 함수 `get_weather`라는 세 가지 도구를 결합합니다.

```
{
  "model": "models/gemini-3.7-flash",
  "contents": [{
    "parts": [{
      "text": "What is the northernmost city in the United States? What's the weather like there today?"
    }],
    "role": "user"
  }, {
    "parts": [{
      "thoughtSignature": "...",
      "toolCall": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "args": {
          "queries": ["northernmost city in the United States"]
        },
        "id": "a7b3k9p2"
      }
    }, {
      "thoughtSignature": "...",
      "toolResponse": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "response": {
          "search_suggestions": "..."
        },
        "id": "a7b3k9p2"
      }
    }, {
      "functionCall": {
        "name": "getWeather",
        "args": {
          "city": "Utqiaġvik, Alaska"
        },
        "id": "m4q8z1v6"
      },
      "thoughtSignature": "..."
    }],
    "role": "model"
  }, {
    "parts": [{
      "functionResponse": {
        "name": "getWeather",
        "response": {
          "response": "Very cold. 22 degrees Fahrenheit."
        },
        "id": "m4q8z1v6"
      }
    }],
    "role": "user"
  }],
  "tools": [{
    "functionDeclarations": [{
      "name": "getWeather"
    }]
  }, {
    "googleSearch": {
    }
  }, {
    "codeExecution": {
    }
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}
```

## 토큰 및 가격 책정

요청의 `toolCall` 및 `toolResponse` 파트는 `prompt_token_count`에 포함됩니다. 이러한 중간 도구 단계는 이제 표시되고 사용자에게 반환되므로 대화 기록의 일부입니다. 이는 *응답*이 아닌
*요청*에만 해당합니다.

Google 검색 도구는 이 규칙의 예외입니다. Google 검색은 이미
쿼리 수준에서 자체 가격 책정 모델을 적용하므로 토큰이
이중으로 청구되지 않습니다 ([가격 책정](https://ai.google.dev/gemini-api/docs/pricing?hl=ko) 페이지 참고).

자세한 내용은 [토큰](https://ai.google.dev/gemini-api/docs/tokens?hl=ko) 페이지를 참고하세요.

## 제한사항

- `include_server_side_tool_invocations` 플래그가 사용 설정된 경우 `VALIDATED` 모드를 기본값으로 설정합니다 (`AUTO` 모드는 지원되지 않음)
- `google_search`와 같은 기본 제공 도구는 위치 및 현재 시간 정보를 사용하므로 `system_instruction` 또는 `function_declaration.description`에 위치 및 시간 정보가 충돌하는 경우 도구 조합 기능이 제대로 작동하지 않을 수 있습니다.

## 지원되는 도구

표준 도구 컨텍스트 순환은 서버 측 (기본 제공) 도구에 적용됩니다.
코드 실행도 서버 측 도구이지만 컨텍스트 순환을 위한 자체 기본 제공 솔루션이 있습니다. 컴퓨터 사용 및 함수 호출은 클라이언트 측 도구이며 컨텍스트 순환을 위한 기본 제공 솔루션도 있습니다.

| 도구 | 실행 측 | 컨텍스트 순환 지원 |
| --- | --- | --- |
| [Google 검색](https://ai.google.dev/gemini-api/docs/google-search?hl=ko) | 서버 측 | 지원됨 |
| [Google 지도](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko) | 서버 측 | 지원됨 |
| [URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko) | 서버 측 | 지원됨 |
| [파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko) | 서버 측 | 지원됨 |
| [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko) | 서버 측 | 지원됨 (기본 제공, `executableCode` 및 `codeExecutionResult` 파트 사용) |
| [컴퓨터 사용](https://ai.google.dev/gemini-api/docs/computer-use?hl=ko) | 클라이언트 측 | 지원됨 (기본 제공, `functionCall` 및 `functionResponse` 파트 사용) |
| [커스텀 함수](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko) | 클라이언트 측 | 지원됨 (기본 제공, `functionCall` 및 `functionResponse` 파트 사용) |

## 다음 단계

- Gemini API의 [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)에 대해 자세히 알아보세요.
- 지원되는 도구를 살펴보세요.
  - [Google 검색](https://ai.google.dev/gemini-api/docs/google-search?hl=ko)
  - [Google 지도](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko)
  - [URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko)
  - [파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko)

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-08-26(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-08-26(UTC)"],[],[]]
