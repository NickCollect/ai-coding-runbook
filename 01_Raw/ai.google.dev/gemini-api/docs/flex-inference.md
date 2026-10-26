---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=ru
fetched_at: 2026-10-26T05:55:20.829987+00:00
title: "\u0413\u0438\u0431\u043a\u0438\u0439 \u0438\u043d\u0444\u0435\u0440\u0435\u043d\u0441 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Доступна новая модель Gemini 4 Argon. [Попробовать](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ru)

![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Чтобы переводить контент на ваш предпочитаемый язык, Google использует технологии на основе искусственного интеллекта. Переводы от ИИ могут содержать ошибки.

- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs?hl=ru)

Отправить отзыв

# Гибкий инференс

Gemini Flex API – это уровень инференса, который позволяет снизить затраты на 50% по сравнению со стандартными тарифами в обмен на переменную задержку и доступность по мере возможности. Он предназначен для рабочих нагрузок, допускающих задержку и требующих синхронной обработки, но не нуждающихся в производительности стандартного API в реальном времени.

## Как использовать Flex

Чтобы использовать уровень Flex, укажите в запросе `service_tier` как `flex`. Если это поле не заполнено, по умолчанию используется стандартный уровень.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Analyze this dataset for trends...",
    service_tier='flex'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: 'gemini-3.8-flash',
        input: 'Analyze this dataset for trends...',
        service_tier: 'flex'
    });
    console.log(interaction.output_text);
}
await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Analyze this dataset for trends..."))
        .serviceTier(ServiceTier.FLEX)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Проложить маршрут

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("Analyze this dataset for trends..."),
            ServiceTier: interactions.ServiceTierFlex.ToPointer(),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.8-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## Как работает гибкий инференс

Gemini Flex Inference позволяет сократить разрыв между стандартным API и 24-часовым временем обработки [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ru). Она использует вычислительные мощности, которые не задействованы в часы пиковой нагрузки, и позволяет экономично выполнять фоновые задачи и последовательные рабочие процессы.

| Функция | Согнуть | Приоритет | Стандартный | Пакетное задание |
| --- | --- | --- | --- | --- |
| **Цены** | Скидка 50 % | На 75–100% больше, чем в Standard | Полная цена | Скидка 50 % |
| **Задержка** | Минуты (цель: 1–15 мин.) | Низкая (секунды) | Секунды в минуты | До 24 часов |
| **Надежность** | Лучший возможный результат (сбрасываемый) | Высокий (неосыпающийся) | Высокий / выше среднего | Высокая (для пропускной способности) |
| **Интерфейс** | Синхронная | Синхронная | Синхронная | Асинхронный код |

### Основные преимущества

- **Экономическая эффективность.** Существенная экономия при оценке непроизводственных систем, использовании фоновых агентов и обогащении данных.
- **Простота.** Достаточно добавить один параметр в существующие запросы.
- **Синхронные рабочие процессы.** Идеально подходят для последовательных цепочек API, в которых следующий запрос зависит от результата предыдущего. Это делает их более гибкими, чем пакетные запросы, для рабочих процессов с агентами.

### Примеры использования

- **Офлайн-оценка.** Проведение регрессионных тестов или составление рейтингов с помощью LLM-as-a-judge.
- **Фоновые агенты.** Последовательные задачи, такие как обновление CRM, создание профилей или модерация контента, где допустимы задержки в несколько минут.
- **Исследования с ограниченным бюджетом.** Академические эксперименты, требующие большого объема токенов при ограниченном бюджете.

### Ограничение частоты запросов

Трафик гибкого инференса учитывается в общих [ограничениях частоты запросов](https://aistudio.google.com/rate-limit?hl=ru). Для него не действуют расширенные ограничения, как для [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ru).

### Сбрасываемая мощность

Трафик Flex имеет более низкий приоритет. Если происходит всплеск стандартного трафика, запросы Flex могут быть вытеснены или отклонены, чтобы обеспечить емкость для пользователей с высоким приоритетом. Если вам нужен высокоприоритетный вывод, ознакомьтесь с разделом [Приоритетный вывод](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ru).

### Коды ошибок

Если гибкая емкость недоступна или система перегружена, API возвращает стандартные коды ошибок:

- **503 Service Unavailable** – система перегружена.
- **429 Too Many Requests** – превышено ограничение частоты запросов или исчерпаны ресурсы.

### Ответственность клиента

- **Нет резервного варианта на стороне сервера.** Чтобы избежать непредвиденных расходов, система не будет автоматически переводить запрос Flex на уровень Standard, если емкость Flex заполнена.
- **Повторные попытки.** Вам необходимо реализовать собственную логику повторных попыток на стороне клиента с экспоненциальной выдержкой.
- **Тайм-ауты.** Поскольку запросы Flex могут находиться в очереди, мы рекомендуем увеличить тайм-ауты на стороне клиента до 10 минут или более, чтобы избежать преждевременного закрытия соединения.

## Как настроить окна ожидания

Вы можете настроить время ожидания для каждого запроса в REST API и клиентских библиотеках.
Всегда следите за тем, чтобы клиентское время ожидания покрывало предполагаемое время ожидания на стороне сервера (например, 600 секунд и более для очередей ожидания Flex). В SDK время ожидания указывается в миллисекундах.

### Время ожидания для каждого запроса

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="why is the sky blue?",
    service_tier="flex",
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: "gemini-3.8-flash",
        input: "why is the sky blue?",
        service_tier: "flex",
    }, {timeout: 900000});
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.HttpOptions;

Client client =
    Client.builder()
        .httpOptions(HttpOptions.builder().timeout(900000).build())
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("why is the sky blue?"))
        .serviceTier(ServiceTier.FLEX)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Проложить маршрут

```
package main

import (
    "context"
    "log"
    "time"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        HTTPOptions: genai.HTTPOptions{
            Timeout: genai.Ptr(15 * time.Minute),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("why is the sky blue?"),
            ServiceTier: interactions.ServiceTierFlex.ToPointer(),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

## Реализация повторных попыток

Поскольку Flex может отклонять запросы и возвращать ошибку 503, ниже приведен пример реализации логики повторных попыток для обработки отклоненных запросов.

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.8-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.8-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.8-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.8-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

int maxRetries = 3;
int baseDelay = 5;
Interaction interaction = null;

for (int attempt = 0; attempt < maxRetries; attempt++) {
  try {
    CreateModelInteraction flexParams =
        CreateModelInteraction.builder()
            .model(Model.of("gemini-3.8-flash"))
            .input(InteractionsInput.of("Analyze this batch statement."))
            .serviceTier(ServiceTier.FLEX)
            .build();
    interaction =
        client.interactions.create(CreateInteractionRequestBody.of(flexParams)).interaction().get();
    break;
  } catch (Exception e) {
    if (attempt < maxRetries - 1) {
      int delay = baseDelay * (1 << attempt); // Exponential Backoff
      System.out.println("Flex busy, retrying in " + delay + "s...");
      Thread.sleep(delay * 1000L);
    } else {
      System.out.println("Flex exhausted, falling back to Standard...");
      CreateModelInteraction standardParams =
          CreateModelInteraction.builder()
              .model(Model.of("gemini-3.8-flash"))
              .input(InteractionsInput.of("Analyze this batch statement."))
              .build();
      interaction =
          client
              .interactions
              .create(CreateInteractionRequestBody.of(standardParams))
              .interaction()
              .get();
    }
  }
}

if (interaction != null) {
  System.out.println(interaction.outputText().orElse(""));
}
```

### Проложить маршрут

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    maxRetries := 3
    baseDelay := 5
    var interaction *interactions.Interaction

    for attempt := 0; attempt < maxRetries; attempt++ {
        res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
            Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                Model:       interactions.Model("gemini-3.8-flash"),
                Input:       interactions.NewInteractionsInput("Analyze this batch statement."),
                ServiceTier: interactions.ServiceTierFlex.ToPointer(),
            }),
        })
        if err == nil {
            interaction = res.Interaction
            break
        }

        if attempt < maxRetries-1 {
            delay := baseDelay * (1 << attempt) // Exponential Backoff
            fmt.Printf("Flex busy, retrying in %ds...\n", delay)
            time.Sleep(time.Duration(delay) * time.Second)
        } else {
            fmt.Println("Flex exhausted, falling back to Standard...")
            stdRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model: interactions.Model("gemini-3.8-flash"),
                    Input: interactions.NewInteractionsInput("Analyze this batch statement."),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            interaction = stdRes.Interaction
        }
    }

    if interaction != nil && interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
}
```

## Цены

Стоимость гибкого инференса составляет 50% от цены [стандартного API](https://ai.google.dev/gemini-api/docs/pricing?hl=ru). Оплата взимается за токен.

## Поддерживаемые модели

Гибкий инференс поддерживают следующие модели:

| Модель | Гибкий инференс |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=ru) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=ru) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ru) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ru) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ru) | ✔️ |
| [Gemini 3.1 Pro (предварительная версия)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ru) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ru) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ru) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ru) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ru) | ✔️ |

## Дальнейшие действия

- [Приоритетный вывод](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ru) для наименьшей задержки.
- [Токены.](https://ai.google.dev/gemini-api/docs/tokens?hl=ru) Узнайте, что такое токены.

Отправить отзыв

Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-10-13 UTC.

Хотите рассказать подробнее?

[[["Прост для понимания","easyToUnderstand","thumb-up"],["Помог мне решить мою проблему","solvedMyProblem","thumb-up"],["Другое","otherUp","thumb-up"]],[["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"],["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"],["Устарел","outOfDate","thumb-down"],["Проблема с переводом текста","translationIssue","thumb-down"],["Проблемы образцов/кода","samplesCodeIssue","thumb-down"],["Другое","otherDown","thumb-down"]],["Последнее обновление: 2026-10-13 UTC."],[],[]]
