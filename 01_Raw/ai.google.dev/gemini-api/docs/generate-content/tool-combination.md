---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tool-combination?hl=ru
fetched_at: 2026-10-12T06:59:06.961949+00:00
title: "\u041a\u0430\u043a \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0432\u0441\u0442\u0440\u043e\u0435\u043d\u043d\u044b\u0435 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b \u0438 \u0444\u0443\u043d\u043a\u0446\u0438\u044e \u0432\u044b\u0437\u043e\u0432\u0430 \u0444\u0443\u043d\u043a\u0446\u0438\u0439 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Флэш-память Gemini 3.8 теперь доступна. [Попробуйте!](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ru)

![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Чтобы переводить контент на ваш предпочитаемый язык, Google использует технологии на основе искусственного интеллекта. Переводы от ИИ могут содержать ошибки.

- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs/generate-content?hl=ru)

Отправить отзыв

# Как использовать встроенные инструменты и функцию вызова функций

Gemini позволяет сочетать [встроенные инструменты](https://ai.google.dev/gemini-api/docs/tools?hl=ru), такие как `google_search`, и [вызов функций](https://ai.google.dev/gemini-api/docs/function-calling?hl=ru) (также известный как *персонализированные инструменты*) в одном ответе, сохраняя и предоставляя историю контекста вызовов инструментов. Встроенные и пользовательские комбинации инструментов позволяют создавать сложные рабочие процессы, в которых, например, модель может получать актуальные данные из интернета, прежде чем вызывать определенную бизнес-логику.

Вот пример, в котором сочетаются встроенные и специальные инструменты с использованием разметки `google_search` и специальной функции `getWeather`:

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
    model="gemini-3.8-flash",
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
    model="gemini-3.8-flash",
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
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
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
        model: "gemini-3.8-flash",
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
        model: "gemini-3.8-flash",
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

### Проложить маршрут

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

    model := client.GenerativeModel("gemini-3.8-flash")
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

## Принцип работы

Модели Gemini 3 используют *циркуляцию контекста инструмента*, чтобы обеспечить работу встроенных и пользовательских комбинаций инструментов. Передача контекста инструментов позволяет сохранять и предоставлять контекст встроенных инструментов, а также делиться им со специальными инструментами в рамках одного вызова от хода к ходу.

### Как включить комбинирование инструментов

- Чтобы включить передачу контекста инструмента, необходимо задать для флага `include_server_side_tool_invocations` значение `true`.
- Добавьте [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=ru#function-declarations) и встроенные инструменты, которые хотите использовать, чтобы активировать комбинированное поведение.
  - Если вы не добавите `function_declarations`, передача контекста инструмента будет работать с включенными встроенными инструментами, если установлен флаг.

### API возвращает части

В одном ответе API возвращает части `toolCall` и `toolResponse` для встроенного вызова инструмента. При вызове функции (специального инструмента) API возвращает часть `functionCall`, а пользователь в следующем запросе предоставляет часть `functionResponse`.

- `toolCall` и `toolResponse`. API возвращает эти части, чтобы сохранить контекст того, какие инструменты выполняются на стороне сервера, и результат их выполнения для следующего хода.
- `functionCall` и `functionResponse`. API отправляет пользователю вызов функции, чтобы он заполнил его, а пользователь отправляет результат обратно в ответе функции. Эти части являются стандартными для всех [вызовов функций](https://ai.google.dev/gemini-api/docs/function-calling?hl=ru) в Gemini API и не относятся к уникальным функциям сочетания инструментов.
- (только для [инструмента выполнения кода](https://ai.google.dev/gemini-api/docs/code-execution?hl=ru))
  `executableCode` и `codeExecutionResult`:
  При использовании инструмента выполнения кода вместо `functionCall` и `functionResponse` API возвращает `executableCode` (код, сгенерированный моделью и предназначенный для выполнения) и `codeExecutionResult` (результат выполнения кода).

На каждом шаге вы должны возвращать модели все части, включая все [поля](#critical-fields), которые они содержат, чтобы поддерживать контекст и использовать комбинации инструментов.

### Важные поля в возвращенных частях

Некоторые [части, возвращаемые API](#api-returns-parts), будут включать поля `id`, `tool_type` и `thought_signature`. Эти поля необходимы для сохранения контекста инструмента (а значит, и для сочетания инструментов), поэтому в последующих запросах вам нужно возвращать все части *в том виде, в котором они были указаны в ответе*.

- `id` – уникальный идентификатор, который сопоставляет вызов с ответом. `id` **устанавливается во всех ответах на вызовы функций** независимо от того, передается ли контекст инструмента.
  Вы *должны* указать в ответе функции тот же параметр `id`, который API предоставляет в вызове функции. Встроенные инструменты автоматически передают `id` между вызовом инструмента и ответом инструмента.
  - Встречается во всех разделах, связанных с инструментами: `toolCall`, `toolResponse`, `functionCall`, `functionResponse`, `executableCode`, `codeExecutionResult`.
- `tool_type` – определяет, какой инструмент используется. Это может быть встроенный инструмент (например, `URL_CONTEXT`) или функция (например, `getWeather`).
  - Найдено в частях `toolCall` и `toolResponse`.
- `thought_signature` – фактический зашифрованный контекст, встроенный в **каждую часть, возвращаемую API**. Без сигнатур мыслей контекст не может быть восстановлен. Если вы не будете возвращать сигнатуры мыслей для всех частей на каждом шаге, модель будет выдавать ошибки.
  - Встречается во *всех* частях.

### Данные, относящиеся к определенному инструменту

Некоторые встроенные инструменты возвращают видимые пользователю аргументы данных, относящиеся к определенному типу инструмента.

| Инструмент | Аргументы вызова инструмента, видимые пользователю (если есть) | Ответ инструмента, видимый пользователю (если есть) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` URL для просмотра | `url_metadata` `retrieved_url`: просмотренные URL `url_retrieval_status`: статус просмотра |
| **FILE\_SEARCH** | Нет | Нет |

## Пример структуры запроса на комбинацию инструментов

Ниже приведена структура запроса для следующего запроса: "Какой город в США расположен севернее всех?" Какая там сегодня погода?" Он сочетает три инструмента: встроенные инструменты Gemini `google_search`
и `code_execution`, а также пользовательскую функцию `get_weather`.

```
{
  "model": "models/gemini-3.8-flash",
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

## Токены и цены

Обратите внимание, что части `toolCall` и `toolResponse` в запросах учитываются в `prompt_token_count`. Поскольку промежуточные шаги теперь видны и возвращаются вам, они являются частью истории чата. Это относится только к *запросам*, но не к *ответам*.

Исключение составляет инструмент Google Поиска. В Google Поиске уже применяется собственная модель ценообразования на уровне запроса, поэтому токены не оплачиваются дважды (см. страницу [Цены](https://ai.google.dev/gemini-api/docs/pricing?hl=ru)).

Подробнее [о токенах](https://ai.google.dev/gemini-api/docs/tokens?hl=ru)…

## Ограничения

- Если включен флаг `include_server_side_tool_invocations`, по умолчанию используется режим `VALIDATED` (режим `AUTO` не поддерживается).
- Встроенные инструменты, такие как `google_search`, используют данные о местоположении и текущем времени. Если в `system_instruction` или `function_declaration.description` указаны несовпадающие сведения о местоположении и времени, функция комбинирования инструментов может работать некорректно.

## Поддерживаемые инструменты

Стандартная передача контекста инструмента применяется к встроенным инструментам на стороне сервера.
Выполнение кода – это также инструмент на стороне сервера, но у него есть собственное встроенное решение для передачи контекста. Использование компьютера и вызов функций – это клиентские инструменты, в которых также есть встроенные решения для передачи контекста.

| Инструмент | Сторона исполнения | Поддержка передачи контекста |
| --- | --- | --- |
| [Google Поиск](https://ai.google.dev/gemini-api/docs/google-search?hl=ru) | Сторона сервера | Поддерживается |
| [Google Карты](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ru) | Сторона сервера | Поддерживается |
| [Контекст URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ru) | Сторона сервера | Поддерживается |
| [Поиск файлов](https://ai.google.dev/gemini-api/docs/file-search?hl=ru) | Сторона сервера | Поддерживается |
| [Выполнение кода](https://ai.google.dev/gemini-api/docs/code-execution?hl=ru) | Сторона сервера | Поддерживается (встроенный, использует детали `executableCode` и `codeExecutionResult`) |
| [Использование компьютера](https://ai.google.dev/gemini-api/docs/computer-use?hl=ru) | Сторона клиента | Поддерживается (встроенный, использует детали `functionCall` и `functionResponse`) |
| [Пользовательские функции](https://ai.google.dev/gemini-api/docs/function-calling?hl=ru) | Сторона клиента | Поддерживается (встроенный, использует детали `functionCall` и `functionResponse`) |

## Дальнейшие действия

- Подробнее [о вызове функций](https://ai.google.dev/gemini-api/docs/function-calling?hl=ru) в Gemini API…
- Ознакомьтесь с поддерживаемыми инструментами:
  - [Google Поиск](https://ai.google.dev/gemini-api/docs/google-search?hl=ru)
  - [Google Карты](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ru)
  - [Контекст URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ru)
  - [Поиск файлов](https://ai.google.dev/gemini-api/docs/file-search?hl=ru)

Отправить отзыв

Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-10-05 UTC.

Хотите рассказать подробнее?

[[["Прост для понимания","easyToUnderstand","thumb-up"],["Помог мне решить мою проблему","solvedMyProblem","thumb-up"],["Другое","otherUp","thumb-up"]],[["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"],["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"],["Устарел","outOfDate","thumb-down"],["Проблема с переводом текста","translationIssue","thumb-down"],["Проблемы образцов/кода","samplesCodeIssue","thumb-down"],["Другое","otherDown","thumb-down"]],["Последнее обновление: 2026-10-05 UTC."],[],[]]
