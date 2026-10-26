---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ru
fetched_at: 2026-10-26T05:51:52.305754+00:00
title: "\u041e\u0431\u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0441 Google \u041a\u0430\u0440\u0442\u0430\u043c\u0438 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Доступна новая модель Gemini 4 Argon. [Попробовать](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ru)

![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Чтобы переводить контент на ваш предпочитаемый язык, Google использует технологии на основе искусственного интеллекта. Переводы от ИИ могут содержать ошибки.

- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs?hl=ru)

Отправить отзыв

# Обоснование с Google Картами

Обоснование с Google Картами связывает генеративные возможности Gemini с подробными, фактическими и актуальными данными Google Карт. Эта функция позволяет разработчикам легко добавлять в свои приложения функции, связанные с местоположением. Когда запрос пользователя связан с данными Карт, модель Gemini использует Google Карты, чтобы предоставить точные и актуальные ответы, относящиеся к указанному местоположению или приблизительному местоположению пользователя.

- **Точные ответы с учетом местоположения.** Используйте обширные и актуальные данные Google Карт для запросов, связанных с географическим положением.
- **Улучшенная персонализация.** Рекомендации и информация подбираются с учетом местоположений, указанных пользователями.

## Начать

В этом примере показано, как интегрировать обоснование с Google Картами в приложение, чтобы предоставлять точные ответы на запросы пользователей с учетом местоположения. В запросе запрашиваются местные рекомендации с необязательным местоположением пользователя, что позволяет модели Gemini использовать данные Google Карт.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "What are the best Italian restaurants within a 15-minute walk from here?"))
        .tools(
            Arrays.asList(
                GoogleMaps.builder().latitude(34.050481).longitude(-118.248526).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// Print the model's text response and annotations
if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
  }
}
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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("What are the best Italian restaurants within a 15-minute walk from here?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(34.050481),
                        Longitude: genai.Ptr(-118.248526),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Print the model's text response and annotations
    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    fmt.Println(content.TextContent.Text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.PlaceCitation != nil {
                                c := annotation.PlaceCitation
                                name := ""
                                if c.Name != nil {
                                    name = *c.Name
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  - %s: %s\n", name, url)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Как работает обоснование с Google Картами

Обоснование с Google Картами интегрирует Gemini API с экосистемой Google Geo, используя Maps API в качестве источника обоснования. Если запрос пользователя содержит географический контекст, модель Gemini может вызвать инструмент обоснования с Google Картами. Затем модель может генерировать ответы на основе данных Google Карт, относящихся к указанному местоположению.

Обычно процесс включает следующие этапы:

1. **Запрос пользователя.** Пользователь отправляет запрос в ваше приложение, который может содержать географический контекст (например, "кофейни рядом", "музеи в Сан-Франциско").
2. **Вызов инструмента.** Модель Gemini распознает географический контекст и вызывает инструмент обоснования с Google Картами. Этот инструмент можно использовать вместе с `latitude` и `longitude` пользователя. Это инструмент текстового поиска, который работает так же, как поиск на Картах: в локальных запросах ("рядом со мной") используются координаты, а на конкретные или нелокальные запросы явное указание местоположения вряд ли повлияет.
3. **Получение данных.** Сервис обоснования с Google Картами запрашивает у Google Карт нужную информацию, например о местах, отзывах, фотографиях, адресах и часах работы.
4. **Обоснованная генерация.** Извлеченные данные Карт используются для формирования ответа модели Gemini, что обеспечивает его фактическую точность и релевантность.
5. **Ответ и аннотации.** Модель возвращает текстовый ответ со встроенными аннотациями, которые ссылаются на источники Google Карт. Это позволяет разработчикам показывать цитаты.

## Зачем и когда использовать обоснование с Google Картами

Основание на Google Картах идеально подходит для приложений, которым требуется точная, актуальная и привязанная к местоположению информация. Это повышает удобство использования, предоставляя релевантный и персонализированный контент, основанный на обширной базе данных Google Карт, содержащей более 250 миллионов мест по всему миру.

Обоснование с Google Картами следует использовать, если вашему приложению нужно:

- Дайте полные и точные ответы на вопросы, связанные с местоположением.
- Создавайте разговорных организаторов путешествий и Местных экспертов.
- Рекомендовать интересные места на основе местоположения и предпочтений пользователя, например рестораны или магазины.
- Создавайте сервисы с учетом местоположения для социальных сетей, розничной торговли или доставки еды.

Обоснование с Google Картами отлично подходит для случаев, когда важны близость и актуальные фактические данные, например при поиске лучшей кофейни поблизости или построении маршрута.

## Примеры использования

Обоснование с Google Картами поддерживает различные варианты использования с учетом местоположения.

### Как отвечать на вопросы о местах

Задавайте подробные вопросы о конкретном месте и получайте ответы на основе отзывов пользователей Google и других данных Карт.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Is there a cafe near the corner of 1st and Main that has outdoor seating?"))
        .tools(
            Arrays.asList(
                GoogleMaps.builder().latitude(34.050481).longitude(-118.248526).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
  }
}
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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Is there a cafe near the corner of 1st and Main that has outdoor seating?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(34.050481),
                        Longitude: genai.Ptr(-118.248526),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    fmt.Println(content.TextContent.Text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.PlaceCitation != nil {
                                c := annotation.PlaceCitation
                                name := ""
                                if c.Name != nil {
                                    name = *c.Name
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  - %s: %s\n", name, url)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### Персонализация на основе местоположения

Получайте рекомендации, адаптированные к предпочтениям пользователя и конкретному географическому региону.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Which family-friendly restaurants near here have the best playground reviews?"))
        .tools(
            Arrays.asList(GoogleMaps.builder().latitude(30.2672).longitude(-97.7431).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
  }
}
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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Which family-friendly restaurants near here have the best playground reviews?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(30.2672),
                        Longitude: genai.Ptr(-97.7431),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    fmt.Println(content.TextContent.Text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.PlaceCitation != nil {
                                c := annotation.PlaceCitation
                                name := ""
                                if c.Name != nil {
                                    name = *c.Name
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  - %s: %s\n", name, url)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### помощь в планировании маршрута;

Создавайте планы на несколько дней с маршрутами и информацией о различных местах. Это отлично подходит для приложений, связанных с путешествиями.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

String prompt =
    "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .tools(
            Arrays.asList(GoogleMaps.builder().latitude(37.78193).longitude(-122.40476).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// ... code to process response
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

    prompt := "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput(prompt),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(37.78193),
                        Longitude: genai.Ptr(-122.40476),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    // ... code to process response
    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## Требования к использованию сервиса

В этом разделе описаны требования к использованию сервиса обоснования с Google Картами.

### Уведомляйте пользователей о том, что вы используете источники Google Карт

В каждом результате, обоснованном Google Картами, вы получите аннотации источников в блоках контента шага `model_output`, которые подтверждают каждый ответ. Возвращаются следующие метаданные:

- URL источника
- name

При показе результатов обоснования с Google Картами вы должны указать связанные источники Google Карт и сообщить пользователям следующее:

- Источники Google Карт должны быть указаны сразу после сгенерированного контента, который они подтверждают. Этот сгенерированный контент также называется результатом, обоснованным Google Картами.
- Источники Google Карт должны быть видны в рамках одного взаимодействия с пользователем.

### Показывать источники Google Карт со ссылками на Карты

Для каждой аннотации источника необходимо создать предварительный просмотр ссылки, отвечающий следующим требованиям:

- Укажите Google Карты в качестве источника данных в соответствии с [правилами указания авторства Google Карт](#maps-attribution-guidelines).
- Показывать название источника, указанное в ответе.
- Укажите ссылку на источник, используя `url` из аннотации.

### Рекомендации по текстовой атрибуции Google Карт

При указании источников Google Карт в тексте следуйте этим рекомендациям:

- Не изменяйте текст "Google Карты":
  - Не меняйте регистр в названии "Google Карты".
  - Не переносите название Google Maps на несколько строк.
  - Не переводите Google Карты на другой язык.
  - Запретите браузерам переводить Google Карты с помощью HTML-атрибута translate="no".

Дополнительную информацию о некоторых поставщиках данных для Google Карт и условиях их лицензий можно найти в [юридических уведомлениях для Google Карт и Google Планеты Земля](https://www.google.com/help/legalnotices_maps/?hl=ru).

## Рекомендации

- **Укажите местоположение пользователя.** Чтобы ответы были максимально релевантными и персонализированными, всегда добавляйте `latitude` и `longitude` в конфигурацию инструмента `google_maps`, если известно местоположение пользователя.
- **Информируйте конечных пользователей.** Четко сообщайте конечным пользователям, что для ответов на их запросы используются данные Google Карт, особенно когда инструмент включен.
- **Отключайте, когда не нужно.** Обоснование с Google Картами по умолчанию отключено. Включайте его (`"tools": [{"type": "google_maps"}]`), только когда у запроса есть явный географический контекст. Это позволит оптимизировать производительность и расходы.

## Ограничения

- Обоснование с Google Картами сейчас поддерживает запросы и ответы только на английском языке.
- Инструмент может быть доступен не во всех регионах.
- Результаты могут различаться в зависимости от точности геолокации и доступных данных Карт.
- **Географический охват.** Обоснование с Google Картами доступно во всем мире.
- **Состояние по умолчанию.** Инструмент "Обоснование с Google Картами" по умолчанию отключен.
  Его нужно явно включить в запросах к API.

## Цены и ограничения частоты запросов

Цены на обоснование с Google Картами зависят от поколения модели:

- **Gemini 3 и более новые модели.** За каждый поисковый запрос, который модель решит выполнить, с вашего проекта будет взиматься плата. При этом 5000 запросов в месяц предоставляются бесплатно для всех моделей Gemini 3 и более новых версий. После этого стоимость составит **14 долларов США за 1000 поисковых запросов**. Один поисковый запрос (ваш запрос к API к модели) может привести к тому, что модель выполнит несколько поисковых запросов, чтобы найти необходимую информацию. Каждый из этих запросов считается платным использованием инструмента.
- **Gemini 2.5 и более ранние модели.** Оплата взимается за каждый поисковый запрос (25 долларов США за 1000 запросов с обоснованием). Плата за запрос взимается, только если в ответ на него возвращается хотя бы один результат, заземленный на Google Картах, независимо от того, сколько поисковых запросов выполнила модель, чтобы получить этот результат.

Квота на обоснование с Google Картами обычно соответствует ограничениям частоты запросов базовой модели Gemini. Подробную информацию о ценах можно найти на [странице цен Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=ru).

## Поддерживаемые модели

Обоснование с Google Картами поддерживается на следующих моделях:

| Модель | Обоснование с Google Картами |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=ru) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=ru) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ru) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ru) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ru) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ru) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ru) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ru) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ru) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ru) | ✔️ |

## Поддерживаемые сочетания инструментов

Вы можете использовать Grounding with Google Maps вместе с другими встроенными инструментами, например [Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=ru) (поддерживается в Gemini 3.5 Flash-Lite и более поздних моделях), чтобы решать более сложные задачи.
Модели Gemini 3 также поддерживают сочетание встроенных инструментов с пользовательскими (вызов функций). Подробнее [о сочетаниях инструментов](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ru)…

## Дальнейшие действия

- Подробнее [о других доступных инструментах](https://ai.google.dev/gemini-api/docs/tools?hl=ru)…
- Чтобы узнать больше о принципах ответственного использования ИИ и фильтрах безопасности Gemini API, ознакомьтесь с [руководством по настройкам безопасности](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ru).

Отправить отзыв

Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-10-13 UTC.

Хотите рассказать подробнее?

[[["Прост для понимания","easyToUnderstand","thumb-up"],["Помог мне решить мою проблему","solvedMyProblem","thumb-up"],["Другое","otherUp","thumb-up"]],[["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"],["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"],["Устарел","outOfDate","thumb-down"],["Проблема с переводом текста","translationIssue","thumb-down"],["Проблемы образцов/кода","samplesCodeIssue","thumb-down"],["Другое","otherDown","thumb-down"]],["Последнее обновление: 2026-10-13 UTC."],[],[]]
