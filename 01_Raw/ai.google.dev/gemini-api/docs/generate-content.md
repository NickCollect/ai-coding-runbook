---
source_url: https://ai.google.dev/gemini-api/docs/generate-content?hl=ru
fetched_at: 2026-10-19T05:48:10.400671+00:00
title: "Gemini API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Доступна новая модель Gemini 4 Argon. [Попробовать](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ru)

![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Чтобы переводить контент на ваш предпочитаемый язык, Google использует технологии на основе искусственного интеллекта. Переводы от ИИ могут содержать ошибки.

- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs/generate-content?hl=ru)

# Gemini API

Gemini API – это самый быстрый способ перейти от запроса к готовому продукту с помощью Gemini, Veo, Nano Banana и других моделей. Он позволяет интегрировать эти генеративные модели в приложения, чтобы создавать сгенерированный текст и изображения, анализировать мультимодальные входные данные и разрабатывать разговорных агентов.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-4-argon",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-4-argon",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
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
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-4-argon",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-4-argon",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-4-argon", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

[Начать](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ru)

---

## Модели

[Весь список](https://ai.google.dev/gemini-api/docs/models?hl=ru)

[auto\_awesome
Gemini 4 Argon
Новое

Наша флагманская модель с окном контекста на 1 млн токенов и длинными декодированиями до 1 млн токенов.](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=ru)
[spark
Gemini 3.6 Flash
Новинка

Наша последняя модель, которая сочетает в себе скорость и интеллект, чтобы обеспечивать высокую производительность при выполнении агентских и мультимодальных задач.](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ru)
[graphic\_eq
Gemini 3.8 Flash TTS
Новинка

Модель студийного уровня для преобразования текста в речь с выразительной интонацией, возможностью создания собственного голоса и его копирования.](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ru)
[spark
Gemini 3.5 Flash-Lite
Новинка

Модель для больших объемов данных, оптимизированная для задач субагентов с высокой пропускной способностью и низкой задержкой.](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ru)
[spark
Gemini 3.1 Flash-Lite

Модель с высокой производительностью и качеством серии Gemini 3, которая позволяет снизить расходы.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ru)
[spark
Gemini 3 Flash

Производительность на уровне передовых моделей при значительно меньших затратах.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ru)
[🍌
Nano Banana

Передовые модели для создания и редактирования изображений.](https://ai.google.dev/gemini-api/docs/image-generation?hl=ru)
[video\_library
Veo 3.1

Наша передовая модель генерации видео с нативным аудио.](https://ai.google.dev/gemini-api/docs/video?hl=ru)
[spark
Gemini Robotics

Визуально-языковая модель (VLM), которая позволяет использовать агентные возможности Gemini в робототехнике и обеспечивает расширенные возможности рассуждения в физическом мире.](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ru)

## Изучить возможности

[imagesmode

Встроенная генерация изображений (Nano Banana)

Генерируйте и редактируйте изображения с учетом контекста с помощью Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation?hl=ru)
[article

Большое окно контекста

Передавайте моделям Gemini миллионы токенов и получайте информацию из неструктурированных изображений, видео и документов.](https://ai.google.dev/gemini-api/docs/long-context?hl=ru)
[code

Structured Outputs

Задайте Gemini ограничение, чтобы он отвечал в формате JSON – формате структурированных данных, подходящем для автоматической обработки.](https://ai.google.dev/gemini-api/docs/structured-output?hl=ru)
[functions

Вызов функций

Создавайте рабочие процессы с агентами, подключая Gemini к внешним API и инструментам.](https://ai.google.dev/gemini-api/docs/function-calling?hl=ru)
[videocam

Создание видео с помощью Veo 3.1

Создавайте высококачественный видеоконтент по текстовым или графическим запросам с помощью нашей передовой модели.](https://ai.google.dev/gemini-api/docs/video?hl=ru)
[android\_recorder

Голосовые агенты с Live API

Создавайте голосовые приложения и агентов, работающих в реальном времени, с помощью Live API.](https://ai.google.dev/gemini-api/docs/live-api?hl=ru)
[build

Инструменты

Подключите Gemini к миру с помощью встроенных инструментов, таких как Google Поиск, контекст URL, Google Карты, выполнение кода и использование компьютера.](https://ai.google.dev/gemini-api/docs/tools?hl=ru)
[stacks

Распознавание документов

Обрабатывайте до 1000 страниц PDF-файлов с полным пониманием мультимодальных запросов или другие текстовые файлы.](https://ai.google.dev/gemini-api/docs/document-processing?hl=ru)
[cognition\_2

Думающая

Узнайте, как возможности рассуждения улучшают логическое мышление при выполнении сложных задач и работе агентов.](https://ai.google.dev/gemini-api/docs/thinking?hl=ru)

[Google AI Studio

Тестируйте запросы, управляйте ключами API, отслеживайте использование и создавайте прототипы.](https://aistudio.google.com?hl=ru)
[group

Сообщество разработчиков

Задавайте вопросы и находите решения вместе с другими разработчиками и инженерами Google.](https://discuss.ai.google.dev/c/gemini-api/4?hl=ru)
[menu\_book

Документация по API

Подробную информацию о Gemini API можно найти в официальной справочной документации.](https://ai.google.dev/api?hl=ru)
[sensors

Статус

Проверьте статус Gemini API, Google AI Studio и наших сервисов моделей.](https://aistudio.google.com/status?hl=ru)

Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-10-16 UTC.

[[["Прост для понимания","easyToUnderstand","thumb-up"],["Помог мне решить мою проблему","solvedMyProblem","thumb-up"],["Другое","otherUp","thumb-up"]],[["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"],["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"],["Устарел","outOfDate","thumb-down"],["Проблема с переводом текста","translationIssue","thumb-down"],["Проблемы образцов/кода","samplesCodeIssue","thumb-down"],["Другое","otherDown","thumb-down"]],["Последнее обновление: 2026-10-16 UTC."],[],[]]
