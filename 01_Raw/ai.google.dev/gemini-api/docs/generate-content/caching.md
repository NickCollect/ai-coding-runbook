---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=ru
fetched_at: 2026-10-19T05:42:50.897224+00:00
title: "\u041a\u0435\u0448\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043d\u0442\u0435\u043a\u0441\u0442\u0430 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Доступна новая модель Gemini 4 Argon. [Попробовать](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ru)

![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Чтобы переводить контент на ваш предпочитаемый язык, Google использует технологии на основе искусственного интеллекта. Переводы от ИИ могут содержать ошибки.

- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs/generate-content?hl=ru)

Отправить отзыв

# Кеширование контекста

В типичном рабочем процессе с ИИ одни и те же входные токены могут передаваться модели многократно. Gemini API предлагает два разных механизма кеширования:

- Неявное кеширование (автоматически включено в Gemini 2.5 и более новых моделях, экономия средств не гарантируется).
- Явное кеширование (можно включить вручную в моделях Gemini 3 и 2.5, гарантирует экономию средств; не поддерживается в Gemini 4 Argon и более поздних версиях).

Явное кеширование полезно, когда вы хотите гарантированно снизить расходы, но при этом готовы к дополнительной работе по разработке.

## Неявное кеширование

Неявное кеширование включено по умолчанию для всех моделей Gemini 2.5 и более новых. Если ваш запрос попадает в кеш, мы автоматически снижаем стоимость. Чтобы включить ее, ничего настраивать не нужно. В таблице ниже указано минимальное количество входных токенов для каждой модели.

| Модель | Минимальный лимит токенов |
| --- | --- |
| Gemini 4 Argon | 4096 |
| Gemini 3.8 Flash | 4096 |
| Gemini 3.6 Flash | 4096 |
| Gemini 3.1 Pro Preview | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

Чтобы повысить вероятность неявного совпадения в кеше:

- Попробуйте разместить в начале запроса крупные и распространенные объекты.
- Попробуйте отправить запросы с похожим префиксом за короткий промежуток времени.

Количество токенов, которые были совпадением в кеше, можно посмотреть в поле `usage_metadata` объекта ответа.

## Явное кеширование

С помощью функции явного кеширования Gemini API вы можете передать модели определенный контент один раз, кешировать входные токены, а затем ссылаться на них в последующих запросах. При определенных объемах использование кешированных токенов обходится дешевле, чем многократная передача одного и того же корпуса токенов.

При кешировании набора токенов можно указать, как долго должен существовать кеш, прежде чем токены будут автоматически удалены. Время, в течение которого данные хранятся в кеше, называется *временем жизни* (TTL). Если значение не задано, по умолчанию используется 1 час. Стоимость кеширования зависит от размера входного токена и того, как долго вы хотите хранить токены.

В этом разделе предполагается, что вы установили Gemini SDK (или curl) и настроили ключ API, как описано в [руководстве по началу работы](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ru).

### Как генерировать контент с помощью кеша

### Python

В следующем примере показано, как генерировать контент с помощью кэшированной системной инструкции и видеофайла.

### Видео

```
import os
import pathlib
import requests
import time

from google import genai
from google.genai import types

client = genai.Client()

# Download a test video file and save it locally
url = 'https://storage.googleapis.com/generativeai-downloads/data/SherlockJr._10min.mp4'
path_to_video_file = pathlib.Path('SherlockJr._10min.mp4')
if not path_to_video_file.exists():
    path_to_video_file.write_bytes(requests.get(url).content)

# Upload the video using the Files API
video_file = client.files.upload(file=path_to_video_file)

# Wait for the file to finish processing
while video_file.state.name == 'PROCESSING':
    time.sleep(2.5)
    video_file = client.files.get(name=video_file.name)

print(f'Video processing complete: {video_file.uri}')

model='models/gemini-3.8-flash'

# Create a cache with a 5 minute TTL (300 seconds)
cache = client.caches.create(
    model=model,
    config=types.CreateCachedContentConfig(
        display_name='sherlock jr movie', # used to identify the cache
        system_instruction=(
            'You are an expert video analyzer, and your job is to answer '
            'the user\'s query based on the video file you have access to.'
        ),
        contents=[video_file],
        ttl="300s",
    )
)

response = client.models.generate_content(
    model = model,
    contents= (
    'Introduce different characters in the movie by describing '
    'their personality, looks, and names. Also list the timestamps '
    'they were introduced for the first time.'),
    config=types.GenerateContentConfig(cached_content=cache.name)
)

print(response.usage_metadata)

print(response.text)
```

### Файлы PDF

```
from google import genai
from google.genai import types
import io
import httpx

client = genai.Client()

long_context_pdf_path = "https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf"

# Retrieve and upload the PDF using the File API
doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

document = client.files.upload(
  file=doc_io,
  config=dict(mime_type='application/pdf')
)

model_name = "gemini-3.8-flash"
system_instruction = "You are an expert analyzing transcripts."

# Create a cached content object
cache = client.caches.create(
    model=model_name,
    config=types.CreateCachedContentConfig(
      system_instruction=system_instruction,
      contents=[document],
    )
)

print(f'{cache=}')

response = client.models.generate_content(
  model=model_name,
  contents="Please summarize this transcript",
  config=types.GenerateContentConfig(
    cached_content=cache.name
  ))

print(f'{response.usage_metadata=}')

print('\n\n', response.text)
```

### JavaScript

В следующем примере показано, как генерировать контент с помощью кэшированной системной инструкции и текстового файла.

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {
  const doc = await ai.files.upload({
    file: "path/to/file.txt",
    config: { mimeType: "text/plain" },
  });
  console.log("Uploaded file name:", doc.name);

  const modelName = "gemini-3.8-flash";
  const cache = await ai.caches.create({
    model: modelName,
    config: {
      contents: createUserContent(createPartFromUri(doc.uri, doc.mimeType)),
      systemInstruction: "You are an expert analyzing transcripts.",
    },
  });
  console.log("Cache created:", cache);

  const response = await ai.models.generateContent({
    model: modelName,
    contents: "Please summarize this transcript",
    config: { cachedContent: cache.name },
  });
  console.log("Response text:", response.text);
}

await main();
```

### Проложить маршрут

В следующем примере показано, как генерировать контент с помощью кеша.

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
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey: "GOOGLE_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    modelName := "gemini-3.8-flash"
    document, err := client.Files.UploadFromPath(
        ctx,
        "media/a11.txt",
        &genai.UploadFileConfig{
          MIMEType: "text/plain",
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    parts := []*genai.Part{
        genai.NewPartFromURI(document.URI, document.MIMEType),
    }
    contents := []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }
    cache, err := client.Caches.Create(ctx, modelName, &genai.CreateCachedContentConfig{
        Contents: contents,
        SystemInstruction: genai.NewContentFromText(
          "You are an expert analyzing transcripts.", genai.RoleUser,
        ),
    })
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("Cache created:")
    fmt.Println(cache)

    // Use the cache for generating content.
    response, err := client.Models.GenerateContent(
        ctx,
        modelName,
        genai.Text("Please summarize this transcript"),
        &genai.GenerateContentConfig{
          CachedContent: cache.Name,
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    printResponse(response) // helper for printing response parts
}
```

### REST

В примере ниже показано, как создать кеш и использовать его для генерации контента.

### Видео

```
wget https://storage.googleapis.com/generativeai-downloads/data/a11.txt
echo '{
  "model": "models/gemini-3.8-flash",
  "contents":[
    {
      "parts":[
        {
          "inline_data": {
            "mime_type":"text/plain",
            "data": "'$(base64 $B64FLAGS a11.txt)'"
          }
        }
      ],
    "role": "user"
    }
  ],
  "systemInstruction": {
    "parts": [
      {
        "text": "You are an expert at analyzing transcripts."
      }
    ]
  },
  "ttl": "300s"
}' > request.json

curl -X POST "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d @request.json \
> cache.json

CACHE_NAME=$(cat cache.json | grep '"name":' | cut -d '"' -f 4 | head -n 1)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [
        {
          "parts":[{
            "text": "Please summarize this transcript"
          }],
          "role": "user"
        },
      ],
      "cachedContent": "'$CACHE_NAME'"
    }'
```

### Файлы PDF

```
DOC_URL="https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf"
DISPLAY_NAME="A11_Mission_Report"
SYSTEM_INSTRUCTION="You are an expert at analyzing transcripts."
PROMPT="Please summarize this transcript"
MODEL="models/gemini-3.8-flash"
TTL="300s"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

MIME_TYPE=$(file -b --mime-type "${DISPLAY_NAME}.pdf")
NUM_BYTES=$(wc -c < "${DISPLAY_NAME}.pdf")

echo "MIME_TYPE: ${MIME_TYPE}"
echo "NUM_BYTES: ${NUM_BYTES}"

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files?key=${GOOGLE_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${DISPLAY_NAME}.pdf" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo "file_uri: ${file_uri}"

# Clean up the downloaded PDF
rm "${DISPLAY_NAME}.pdf"

# Create the cached content request
echo '{
  "model": "'$MODEL'",
  "contents":[
    {
      "parts":[
        {"file_data": {"mime_type": "'$MIME_TYPE'", "file_uri": '$file_uri'}}
      ],
    "role": "user"
    }
  ],
  "system_instruction": {
    "parts": [
      {
        "text": "'$SYSTEM_INSTRUCTION'"
      }
    ],
    "role": "system"
  },
  "ttl": "'$TTL'"
}' > request.json

# Send the cached content request
curl -X POST "${BASE_URL}/v1beta/cachedContents?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d @request.json \
> cache.json

CACHE_NAME=$(cat cache.json | grep '"name":' | cut -d '"' -f 4 | head -n 1)
echo "CACHE_NAME: ${CACHE_NAME}"
# Send the generateContent request using the cached content
curl -X POST "${BASE_URL}/${MODEL}:generateContent?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [
        {
          "parts":[{
            "text": "'$PROMPT'"
          }],
          "role": "user"
        }
      ],
      "cachedContent": "'$CACHE_NAME'"
    }' > response.json

cat response.json

echo jq ".candidates[].content.parts[].text" response.json
```

### Список кешей

Получить или посмотреть кешированный контент нельзя, но можно получить метаданные кеша (`name`, `model`, `display_name`, `usage_metadata`, `create_time`, `update_time` и `expire_time`).

### Python

Чтобы получить список метаданных для всех загруженных кешей, используйте команду `CachedContent.list()`:

```
for cache in client.caches.list():
  print(cache)
```

Чтобы получить метаданные для одного объекта кеша, если вы знаете его название, используйте `get`:

```
client.caches.get(name=name)
```

### JavaScript

Чтобы получить метаданные всех загруженных кешей, используйте `GoogleGenAI.caches.list()`:

```
console.log("My caches:");
const pager = await ai.caches.list({ config: { pageSize: 10 } });
let page = pager.page;
while (true) {
  for (const c of page) {
    console.log("    ", c.name);
  }
  if (!pager.hasNextPage()) break;
  page = await pager.nextPage();
}
```

### Проложить маршрут

В следующем примере перечислены все кеши.

```
caches, err := client.Caches.All(ctx)
if err != nil {
    log.Fatal(err)
}
fmt.Println("Listing all caches:")
for _, item := range caches {
    fmt.Println("   ", item.Name)
}
```

В следующем примере перечислены кеши с размером страницы 2.

```
page, err := client.Caches.List(ctx, &genai.ListCachedContentsConfig{PageSize: 2})
if err != nil {
    log.Fatal(err)
}

pageIndex := 1
for {
    fmt.Printf("Listing caches (page %d):\n", pageIndex)
    for _, item := range page.Items {
        fmt.Println("   ", item.Name)
    }
    if page.NextPageToken == "" {
        break
    }
    page, err = page.Next(ctx)
    if err == genai.ErrPageDone {
        break
    } else if err != nil {
        return err
    }
    pageIndex++
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY"
```

### Обновление кеша

Вы можете задать новое значение `ttl` или `expire_time` для кеша. Другие изменения кеша не поддерживаются.

### Python

В примере ниже показано, как обновить `ttl` кеша с помощью `client.caches.update()`.

```
from google import genai
from google.genai import types

client.caches.update(
  name = cache.name,
  config  = types.UpdateCachedContentConfig(
      ttl='300s'
  )
)
```

Чтобы задать срок действия, можно использовать объект `datetime` или строку даты и времени в формате ISO (`dt.isoformat()`, например `2025-01-27T16:02:36.473528+00:00`). Необходимо указать часовой пояс (`datetime.utcnow()` не добавляет часовой пояс, а `datetime.now(datetime.timezone.utc)` – добавляет).

```
from google import genai
from google.genai import types
import datetime

# You must use a time zone-aware time.
in10min = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=10)

client.caches.update(
  name = cache.name,
  config  = types.UpdateCachedContentConfig(
      expire_time=in10min
  )
)
```

### JavaScript

В следующем примере показано, как обновить `ttl` кеша с помощью `GoogleGenAI.caches.update()`.

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### Проложить маршрут

В примере ниже показано, как обновить `TTL` кеша.

```
// Update the TTL (2 hours).
cache, err = client.Caches.Update(ctx, cache.Name, &genai.UpdateCachedContentConfig{
    TTL: 7200 * time.Second,
})
if err != nil {
    log.Fatal(err)
}
fmt.Println("After update:")
fmt.Println(cache)
```

### REST

В следующем примере показано, как обновить `ttl` кеша.

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### Как удалить кеш

Сервис кеширования предоставляет операцию удаления для удаления контента из кеша вручную. В следующем примере показано, как удалить кеш:

### Python

```
client.caches.delete(cache.name)
```

### JavaScript

```
await ai.caches.delete({ name: cache.name });
```

### Проложить маршрут

```
_, err = client.Caches.Delete(ctx, cache.Name, &genai.DeleteCachedContentConfig{})
if err != nil {
    log.Fatal(err)
}
fmt.Println("Cache deleted:", cache.Name)
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY"
```

### Явное кеширование с помощью библиотеки OpenAI

Если вы используете [библиотеку OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=ru), то можете включить явное кеширование с помощью свойства `cached_content` в [`extra_body`](https://ai.google.dev/gemini-api/docs/openai?hl=ru#extra-body).

## Когда использовать явное кеширование

Кеширование контекста особенно хорошо подходит для сценариев, в которых на существенный начальный контекст неоднократно ссылаются более короткие запросы. Кеширование контекста можно использовать в следующих случаях:

- Чат-боты с подробными [системными инструкциями](https://ai.google.dev/gemini-api/docs/system-instructions?hl=ru)
- Повторяющийся анализ длинных видеофайлов
- Повторяющиеся запросы к большим наборам документов
- Частый анализ репозитория кода или исправление ошибок

### Как явное кеширование помогает снизить расходы

Кеширование контекста – это платная функция, которая позволяет снизить расходы. Стоимость услуг зависит от следующих факторов:

1. **Количество токенов в кеше.** Число токенов ввода, которые были закешированы и при использовании в последующих запросах оплачиваются по сниженной цене.
2. **Продолжительность хранения.** Время, в течение которого хранятся кешированные токены (TTL). Плата взимается в зависимости от TTL количества кешированных токенов. Минимальных и максимальных ограничений для TTL нет.
3. **Другие факторы.** Применяются другие тарифы, например за некешированные входные и выходные токены.

Актуальную информацию о ценах можно найти на [странице Gemini API](https://ai.google.dev/pricing?hl=ru). Чтобы узнать, как подсчитывать токены, ознакомьтесь с [руководством по токенам](https://ai.google.dev/gemini-api/docs/tokens?hl=ru).

### В видео есть другие нарушения?

При использовании кеширования контекста учитывайте следующее:

- *Минимальное* количество входных токенов для кеширования контекста зависит от модели. *Максимальное значение* совпадает с максимальным значением для данной модели. Подробнее о том, [как подсчитываются токены](https://ai.google.dev/gemini-api/docs/tokens?hl=ru)…
- Модель не делает различий между кешированными и обычными входными токенами. Кешированный контент – это префикс запроса.
- Для кеширования контекста не предусмотрено специальных ограничений на частоту запросов или использование. Действуют стандартные ограничения на частоту запросов для `GenerateContent`, а ограничения на количество токенов включают кешированные токены.
- Количество кешированных токенов возвращается в поле `usage_metadata` при выполнении операций создания, получения и вывода списка в сервисе кеширования, а также в поле `GenerateContent` при использовании кеша.

Отправить отзыв

Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-10-13 UTC.

Хотите рассказать подробнее?

[[["Прост для понимания","easyToUnderstand","thumb-up"],["Помог мне решить мою проблему","solvedMyProblem","thumb-up"],["Другое","otherUp","thumb-up"]],[["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"],["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"],["Устарел","outOfDate","thumb-down"],["Проблема с переводом текста","translationIssue","thumb-down"],["Проблемы образцов/кода","samplesCodeIssue","thumb-down"],["Другое","otherDown","thumb-down"]],["Последнее обновление: 2026-10-13 UTC."],[],[]]
