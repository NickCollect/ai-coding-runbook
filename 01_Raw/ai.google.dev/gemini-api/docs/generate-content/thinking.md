---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=ru
fetched_at: 2026-10-26T05:53:55.576452+00:00
title: "Gemini \u0434\u0443\u043c\u0430\u0435\u0442 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Доступна новая модель Gemini 4 Argon. [Попробовать](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ru)

![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Чтобы переводить контент на ваш предпочитаемый язык, Google использует технологии на основе искусственного интеллекта. Переводы от ИИ могут содержать ошибки.

- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs/generate-content?hl=ru)

Отправить отзыв

# Gemini думает

[Модели Gemini](https://ai.google.dev/gemini-api/docs/models?hl=ru) используют внутренний "процесс мышления", который значительно улучшает их способность рассуждать и планировать многоэтапные действия. Это делает их очень эффективными для сложных задач, таких как программирование, высшая математика и анализ данных.

В этом руководстве рассказывается, как использовать возможности Gemini для размышлений с помощью Gemini API.

## Генерирование контента с помощью Thinking

Запрос к думающей модели отправляется так же, как и любой другой запрос на генерацию контента. Главное отличие заключается в том, что в поле `model` нужно указать одну из [моделей с поддержкой рассуждения](#tools), как показано в примере [генерации текста](https://ai.google.dev/gemini-api/docs/text-generation?hl=ru) ниже.

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### Проложить маршрут

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3.8-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## Краткие пересказы рассуждений

Краткие пересказы рассуждений – это обобщенные версии необработанных рассуждений модели, которые дают представление о ее внутреннем процессе мышления. Обратите внимание, что уровни и лимиты рассуждений применяются к необработанным рассуждениям модели, а не к их краткому пересказу.

Чтобы включить краткий пересказ мыслей, задайте для параметра `includeThoughts` значение `true` в конфигурации запроса. Затем вы можете получить доступ к сводке, перебирая `parts` параметра `response` и проверяя логическое значение `thought`.

Ниже приведен пример, демонстрирующий, как включить и получить сводку мыслей без потоковой передачи, которая возвращает одну окончательную сводку мыслей вместе с ответом.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.8-flash",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### Проложить маршрут

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3.8-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

А вот пример использования цепочки рассуждений с потоковой передачей, которая возвращает скользящие, инкрементные сводки во время генерации:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3.8-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.8-flash",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
    }
  }
}

await main();
```

### Проложить маршрут

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3.8-flash"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## Управление мышлением

Модели Gemini по умолчанию используют динамическое мышление, автоматически регулируя объем рассуждений в зависимости от сложности запроса пользователя.
Однако, если у вас есть особые требования к задержке или вам нужно, чтобы модель выполняла более глубокие рассуждения, чем обычно, вы можете использовать параметры для управления процессом мышления.

### Уровни мышления (Gemini 4 и Gemini 3)

Параметр `thinkingLevel`, который является обязательным для моделей Gemini 4 и рекомендованным для моделей Gemini 3, позволяет управлять логикой рассуждений. Gemini 4 (`gemini-4-argon`) поддерживает `low`, `medium` (по умолчанию) и `high`.

В таблице ниже приведены настройки `thinkingLevel` для каждого типа модели.

| Уровень рассуждений | Gemini 3.8 Flash | Gemini 3.6 Flash | Gemini 4 Argon | Gemini 3.5 и 3.1 Flash-Lite | Gemini 3.1 Flash-Lite Image | Gemini 3 Flash | Gemini Robotics ER 2 | Описание |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | Не поддерживается (ошибка) | Что пользователь может | Не поддерживается (ошибка) | Поддерживается (по умолчанию) | Поддерживается (по умолчанию) | Что пользователь может | Что пользователь может | Соответствует настройке "не думать" для большинства запросов. Обратите внимание, что `minimal` не гарантирует, что рассуждения будут отключены. Модель может рассуждать минимально при выполнении сложных задач. |
| **`low`** | Что пользователь может | Что пользователь может | Что пользователь может | Что пользователь может | Не поддерживается | Что пользователь может | Что пользователь может | Минимизирует задержку и стоимость. |
| **`medium`** | Поддерживается (по умолчанию) | Поддерживается (по умолчанию) | Поддерживается (по умолчанию) | Что пользователь может | Чего пользователь не может | Что пользователь может | Что пользователь может | Сбалансированное мышление для большинства задач. |
| **`high`** | Поддерживается (динамический) | Поддерживается (динамический) | Поддерживается (динамический) | Поддерживается (динамический) | Поддерживается (динамический) | Поддерживается (по умолчанию, динамический) | Поддерживается (по умолчанию, динамический) | Максимальная глубина рассуждений. Модели может потребоваться значительно больше времени, чтобы сгенерировать первый токен ответа (не относящийся к размышлениям), но ответ будет более тщательно продуман. |

В следующем примере показано, как задать уровень мышления.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Проложить маршрут

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3.8-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

Для Gemini 4 Argon отключить мышление нельзя. Модели Gemini 3 Flash и Flash-Lite также не поддерживают полное отключение мышления. Если вы не укажете уровень мышления, Gemini будет использовать уровень мышления по умолчанию для модели (например, `"medium"` для Gemini 4 Argon, Gemini 3.8 Flash и Gemini 3.6 Flash).

Модели серии Gemini 2.5 не поддерживают `thinkingLevel`. Вместо этого используйте `thinkingBudget`.

### Ограничения на количество токенов и `max_output_tokens`

Параметр генерации [`max_output_tokens`](https://ai.google.dev/api/generate-content?hl=ru#v1beta.GenerationConfig) задает максимальное количество токенов, которые может сгенерировать ответ, включая токены размышлений.

Если этот параметр задан, он действует как жесткое ограничение, применяемое инфраструктурой, без изменения того, как модель распределяет свой бюджет на рассуждения (`thinking_level`).

Если модель достигнет этого лимита во время рассуждения, она прекратит генерировать ответ с помощью `finish_reason: MAX_TOKENS` и вернет усеченный или пустой результат (при этом плата за сгенерированные токены мышления будет взиматься). Чтобы снизить стоимость или задержку, не усекая ответы, уменьшите значение `thinking_level` (`low` или `medium`), а не `max_output_tokens`.

Для моделей Gemini 4 (`gemini-4-argon`) действуют следующие ограничения на контекст и выходные данные:

- **Общее окно контекста на 1 миллион токенов.** Входные, выходные и токены рассуждения используют одно окно контекста на 1 миллион токенов (`1,048,576` токенов). Если сумма входных токенов и `max_output_tokens` превышает 1 048 576 токенов, API автоматически ограничивает выходные токены оставшимся местом в окне контекста (`1,048,576` минус входные токены).
- **Ограничения на количество выходных данных для каждого запроса (64 000 токенов для потоковой передачи и 32 000 токенов для других запросов) и длинное декодирование (до 1 000 000 токенов).** Один запрос для потоковой передачи (`streamGenerateContent`) возвращает до `65,536` токенов, а один запрос без потоковой передачи (`generateContent`) – до `32,768` токенов. Чтобы сгенерировать больше токенов, чем разрешено за один запрос (до `1,048,576` токенов за вычетом входных данных), задайте для параметра `max_output_tokens` значение выше ограничения. Последние версии Google GenAI SDK по умолчанию продолжают генерацию автоматически (`automatic_continuation=True`). Вы также можете запустить цикл клиента, используя `continuation_token`, возвращенный, когда генерация останавливается с `finish_reason: "CONTINUATION"`. Примеры кода приведены в разделе [Длинный код](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=ru).

### Бюджеты на рассуждения

Параметр `thinkingBudget`, представленный в серии Gemini 2.5, указывает модели, сколько токенов мышления нужно использовать для рассуждений.

Ниже приведены сведения о конфигурации для каждого типа модели.`thinkingBudget`
Чтобы отключить функцию, задайте для параметра `thinkingBudget` значение 0.
Если задать для параметра `thinkingBudget` значение -1, будет включено **динамическое мышление**, то есть модель будет корректировать бюджет в зависимости от сложности запроса.

| Модель | Настройка по умолчанию (бюджет на размышления не задан) | Диапазон | Отключить режим размышления | Как включить динамическое мышление |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | Динамическое мышление | `128` – `32768` | —: нельзя отключить режим размышления | `thinkingBudget = -1` (по умолчанию) |
| **2.5 Flash** | Динамическое мышление | `0` – `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (по умолчанию) |
| **2.5. Предварительный просмотр Flash** | Динамическое мышление | `0` – `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (по умолчанию) |
| **2.5 Flash Lite** | Модель не думает | `512` – `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite Preview** | Модель не думает | `512` – `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 Preview** | Динамическое мышление | `0` – `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (по умолчанию) |
| **2.5 Flash Live Native Audio Preview (09-2025)** | Динамическое мышление | `0` – `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (по умолчанию) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Проложить маршрут

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

В зависимости от запроса модель может превысить или не достичь лимита токенов.

## Подписи мыслей

Gemini API не сохраняет состояние, поэтому модель обрабатывает каждый запрос к API независимо и не имеет доступа к контексту рассуждений из предыдущих шагов в пошаговых взаимодействиях.

Чтобы поддерживать контекст рассуждений в многошаговых взаимодействиях, Gemini возвращает сигнатуры рассуждений – зашифрованные представления внутреннего процесса рассуждений модели.

- **Модели Gemini 2.5** возвращают сигнатуры размышлений, если эта функция включена и запрос включает [вызов функций](https://ai.google.dev/gemini-api/docs/function-calling?hl=ru#thinking), в частности [объявления функций](https://ai.google.dev/gemini-api/docs/function-calling?hl=ru#step-2).
- **Модели Gemini 4 и Gemini 3** могут возвращать сигнатуры мыслей для всех типов [частей](https://ai.google.dev/api/caching?hl=ru#Part). Мы рекомендуем всегда передавать все подписи в том виде, в котором они были получены, но для подписей вызовов функций это *обязательно*. Подробнее [о подписях Thought Signatures](https://ai.google.dev/gemini-api/docs/generate-content/thought-signatures?hl=ru)…

При использовании вызова функций также следует учитывать следующие ограничения:

- Подписи возвращаются моделью в других частях ответа, например в вызовах функций или текстовых частях.
  [Возвращайте модели весь ответ](https://ai.google.dev/gemini-api/docs/function-calling?hl=ru#step-4) со всеми частями в последующих запросах.
- Не объединяйте части письма с подписями.
- Не объединяйте часть с подписью с частью без подписи.

## Цены

Если функция "Размышления" включена, цена ответа будет равна сумме токенов для выходных данных и токенов для размышлений. Общее количество сгенерированных токенов мышления можно получить из поля `thoughtsTokenCount`.

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Проложить маршрут

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

Модели мышления генерируют полные мысли, чтобы улучшить качество окончательного ответа, а затем выводят [краткие изложения](#summaries), чтобы дать представление о процессе мышления. Таким образом, цена зависит от количества токенов, которые модели нужно сгенерировать, чтобы создать краткий пересказ, несмотря на то, что API возвращает только сам пересказ.

Подробнее [о подсчете токенов](https://ai.google.dev/gemini-api/docs/tokens?hl=ru)…

## Рекомендации

В этом разделе приведены рекомендации по эффективному использованию моделей мышления.
Как всегда, следуйте нашим [рекомендациям по составлению запросов](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ru), чтобы получать наилучшие результаты.

### Отладка и управление

- **Проверяйте рассуждения.** Если вы не получаете ожидаемый ответ от думающих моделей, может быть полезно внимательно проанализировать краткие пересказы рассуждений Gemini.
  Вы можете посмотреть, как модель разбила задачу на части и пришла к выводу, и использовать эту информацию, чтобы исправить результаты.
- **Укажите, как рассуждать.** Если вы хотите получить длинный ответ, укажите в запросе, [сколько времени](#set-budget) модель должна потратить на размышления. Это позволяет зарезервировать больше
  выходных токенов для ответа.

### Сложность задачи

- **Простые задачи (мышление может быть отключено).** Для простых запросов, не требующих сложных рассуждений, например для поиска фактов или классификации, мышление не требуется. Примеры:
  - "Где была основана компания DeepMind?"
  - "В этом письме предлагается встреча или просто предоставляется информация?"
- **Задачи средней сложности (по умолчанию/требующие размышлений).** Многие распространенные запросы требуют пошаговой обработки или более глубокого понимания. Gemini может использовать способность рассуждать для таких задач, как:
  - Проведи аналогию между фотосинтезом и взрослением.
  - Сравнивать электромобили и гибридные автомобили.
- **Сложные задачи (максимальная способность к рассуждению).** Для действительно сложных задач, таких как решение сложных математических задач или задач по программированию, мы рекомендуем установить высокий лимит на рассуждения. Для выполнения таких задач модели необходимо задействовать все свои возможности рассуждения и планирования, что часто включает в себя множество внутренних шагов, прежде чем будет предоставлен ответ. Примеры:
  - Реши задачу 1 из AIME 2025: найди сумму всех целых оснований b > 9, для которых 17b является делителем 97b.
  - Напиши код Python для веб-приложения, которое визуализирует данные фондового рынка в реальном времени, включая аутентификацию пользователей. Сделайте его максимально эффективным.

## Поддерживаемые модели, инструменты и возможности

Функции рассуждения поддерживаются во всех моделях серий 4, 3 и 2.5.
Все возможности моделей перечислены на странице [Обзор моделей](https://ai.google.dev/gemini-api/docs/models?hl=ru).

Думающие модели работают со всеми инструментами и функциями Gemini. Это позволяет моделям взаимодействовать с внешними системами, выполнять код или получать информацию в реальном времени, а затем использовать полученные результаты в своих рассуждениях и окончательном ответе.

Примеры использования инструментов с думающими моделями можно найти в [руководстве по думающим моделям][Colab].

## Что дальше?

- Информация о покрытии функции "Размышление" приведена в нашем руководстве по [совместимости с OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=ru#thinking).

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

Отправить отзыв

Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-10-14 UTC.

Хотите рассказать подробнее?

[[["Прост для понимания","easyToUnderstand","thumb-up"],["Помог мне решить мою проблему","solvedMyProblem","thumb-up"],["Другое","otherUp","thumb-up"]],[["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"],["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"],["Устарел","outOfDate","thumb-down"],["Проблема с переводом текста","translationIssue","thumb-down"],["Проблемы образцов/кода","samplesCodeIssue","thumb-down"],["Другое","otherDown","thumb-down"]],["Последнее обновление: 2026-10-14 UTC."],[],[]]
