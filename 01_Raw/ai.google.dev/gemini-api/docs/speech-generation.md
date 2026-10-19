---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=ru
fetched_at: 2026-10-19T05:37:49.090201+00:00
title: "\u0421\u0438\u043d\u0442\u0435\u0437 \u0440\u0435\u0447\u0438 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Доступна новая модель Gemini 4 Argon. [Попробовать](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ru)

![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Чтобы переводить контент на ваш предпочитаемый язык, Google использует технологии на основе искусственного интеллекта. Переводы от ИИ могут содержать ошибки.

- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs?hl=ru)

Отправить отзыв

# Синтез речи

Gemini API может преобразовывать текстовые входные данные в аудио с одним или несколькими динамиками, используя возможности генерации синтеза речи (TTS) Gemini.
Генерация речи *[управляема](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ru#controllable)*. Вы можете комбинировать структурированные метаданные (`speech_metadata`) и встроенные теги, чтобы задавать *стиль*, *акцент*, *темп* и *тон* аудио.

Функция TTS отличается от генерации речи, предоставляемой через [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ru), который предназначен для интерактивного неструктурированного аудио, а также мультимодальных входных и выходных данных. Live API отлично подходит для динамичных разговорных контекстов, а TTS через Gemini API – для сценариев, в которых требуется точное воспроизведение текста с детальным контролем стиля и звука, например при создании подкастов или аудиокниг.

В этом руководстве рассказывается, как генерировать аудио с одним или несколькими голосами из текста с помощью [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ru) (`gemini-3.8-flash-tts`) и [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=ru) (`gemini-3.8-flash-lite-tts`).

## Подготовка

Убедитесь, что вы используете модель Gemini TTS, указанную в разделе [Поддерживаемые модели](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ru#supported-models), и обновите Google GenAI SDK до последней версии (`google-genai >= 2.25.0` для Python или `@google/genai >= 2.24.0` для JavaScript/TypeScript) или используйте REST API.
Чтобы получить оптимальные результаты, ознакомьтесь с информацией о том, [когда какую модель использовать](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ru#when-to-use-which-model), и выберите подходящую для вашей рабочей нагрузки.

Рекомендуем [протестировать модели Gemini TTS в AI Studio](https://aistudio.google.com/generate-speech?hl=ru), прежде чем начинать разработку.

## Озвучивание текста одним голосом

Чтобы преобразовать текст в аудио с одним говорящим, используя модели Gemini 3.8 TTS, передайте дословную расшифровку в `input`, добавьте стили на уровне реплик с помощью аннотации `speech_metadata` и настройте голос в `generation_config.speech_config`. Вы можете выбрать голос из готовых [вариантов](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ru#voices), расширенной библиотеки голосов (`GET /v1beta/voices`), а также указать идентификатор [собственного голоса](https://ai.google.dev/gemini-api/docs/voice-design?hl=ru) (`voice_...`) или [репликации голоса](https://ai.google.dev/gemini-api/docs/voice-replication?hl=ru) (`voice_...` или необязательный параметр `voicekey_...`).

В этом примере аудио в формате WAV (`audio/wav`), полученное от модели, сохраняется напрямую в файл:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }' | jq -r '[.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio")] | last | .data' | base64 --decode > out.wav
```

В SDK для Python и JavaScript вы можете получить сгенерированные аудиоданные с помощью свойства `interaction.output_audio`, которое возвращает последний сгенерированный аудиофрагмент. В необработанных ответах REST JSON аудио, закодированное по алгоритму Base64, хранится в `steps[].content[].data`. Подробную информацию о свойствах вы найдете в [обзоре взаимодействий](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ru#convenience-properties).

## Озвучивание текста несколькими голосами

Для диалога с несколькими говорящими настройте два голоса в `speech_config.speakers` и передавайте каждую реплику как отдельный текстовый элемент с аннотацией `speech_metadata`, указывающей на `speaker` и необязательный `style` на уровне реплики. Обратите внимание, что `speech_config` принимает массив (`[{"voice": "..."}]`) для генерации с одним голосом и объект (`{"speakers": [...]}`) для генерации с несколькими голосами:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [
            {
                "type": "text",
                "text": "How's it going today Jane?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Joe",
                    "style": "cheerful and friendly",
                }],
            },
            {
                "type": "text",
                "text": "Not too bad, how about you? Ready to test these new voices?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Jane",
                    "style": "calm and relaxed",
                }],
            },
        ],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": {
            "speakers": [
                {"speaker": "Joe", "voice": "Puck"},
                {"speaker": "Jane", "voice": "Kore"},
            ],
        }
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [
            {
               type: 'text',
               text: "How's it going today Jane?",
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Joe',
                  style: 'cheerful and friendly',
               }],
            },
            {
               type: 'text',
               text: 'Not too bad, how about you? Ready to test these new voices?',
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Jane',
                  style: 'calm and relaxed',
               }],
            },
         ],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: {
            speakers: [
               { speaker: 'Joe', voice: 'Puck' },
               { speaker: 'Jane', voice: 'Kore' },
            ],
         },
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [
        {
          "type": "text",
          "text": "How'\''s it going today Jane?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Joe",
            "style": "cheerful and friendly"
          }]
        },
        {
          "type": "text",
          "text": "Not too bad, how about you? Ready to test these new voices?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Jane",
            "style": "calm and relaxed"
          }]
        }
      ]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": {
        "mode": "conversational",
        "speakers": [
          { "speaker": "Joe", "voice": "Puck" },
          { "speaker": "Jane", "voice": "Kore" }
        ]
      }
    }
  }'
```

## Как управлять стилем речи с помощью метаданных и тегов

Gemini 3.8 TTS обрабатывает поле `text` строго как дословную расшифровку. Чтобы управлять подачей, не зачитывая ремарки вслух, разделите инструкции по области действия:

- **Постоянная подача на уровне реплики (`speech_metadata.style`).** Укажите в поле `style` эмоции, стиль подачи, просодию, темп и громкость, которые применяются ко всей реплике (например, `"style": "whispered urgently"`, `"style": "out of breath"` или `"style": "warm and enthusiastic"`).
- **Моментальные события (встроенные теги).** Обозначайте кратковременные неречевые звуки или паузы непосредственно в расшифровке с помощью угловых скобок, например `"Wait... <short pause> did you hear that? <sigh>"` или `"Excuse me <cough> as I was saying..."`.

Подробные рекомендации вы найдете в [руководстве по составлению запросов](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ru#prompting-guide).

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [
            {
                "type": "text",
                "text": "Wait... <short pause> look under that fallen log! Is that a blue-spotted salamander?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Dr. Anya",
                    "style": "whispered urgently",
                }],
            },
            {
                "type": "text",
                "text": "<gasp> No way! <laugh> We've been searching for this species all season!",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Liam",
                    "style": "warm and enthusiastic",
                }],
            },
        ],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": {
            "speakers": [
                {"speaker": "Dr. Anya", "voice": "Kore"},
                {"speaker": "Liam", "voice": "Puck"},
            ],
        }
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [
            {
               type: 'text',
               text: 'Wait... <short pause> look under that fallen log! Is that a blue-spotted salamander?',
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Dr. Anya',
                  style: 'whispered urgently',
               }],
            },
            {
               type: 'text',
               text: "<gasp> No way! <laugh> We've been searching for this species all season!",
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Liam',
                  style: 'warm and enthusiastic',
               }],
            },
         ],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: {
            speakers: [
               { speaker: 'Dr. Anya', voice: 'Kore' },
               { speaker: 'Liam', voice: 'Puck' },
            ],
         },
      },
   });

   if (interaction.output_audio?.data) {
      const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
      fs.writeFileSync('out.wav', audioBuffer);
   }
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [
        {
          "type": "text",
          "text": "Wait... <short pause> look under that fallen log! Is that a blue-spotted salamander?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Dr. Anya",
            "style": "whispered urgently"
          }]
        },
        {
          "type": "text",
          "text": "<gasp> No way! <laugh> We'\''ve been searching for this species all season!",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Liam",
            "style": "warm and enthusiastic"
          }]
        }
      ]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": {
        "speakers": [
          { "speaker": "Dr. Anya", "voice": "Kore" },
          { "speaker": "Liam", "voice": "Puck" }
        ]
      }
    }
  }'
```

## Потоковая генерация речи

Вы можете транслировать сгенерированное аудио по мере его синтеза, задав значение `stream: true`. В отличие от унарных запросов, которые возвращают полный WAV-файл с заголовком RIFF, **потоковые запросы по умолчанию возвращают необработанные 16-битные фрагменты линейной импульсно-кодовой модуляции со знаком и прямым порядком байтов без заголовков (`audio/l16`, 24 кГц, моно)**. Это позволяет воспроизводить или объединять аудиофрагменты без заголовков контейнеров.

### Python

```
import base64
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "audio":
            audio_data = base64.b64decode(event.delta.data)
            # Process the audio chunk (e.g. play it or write to a file)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const stream = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
      stream: true,
   });

   for await (const event of stream) {
      if (event.event_type === 'step.delta') {
         if (event.delta.type === 'audio') {
            const audioBuffer = Buffer.from(event.delta.data, 'base64');
            // Process the audio buffer
         }
      }
   }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    },
    "stream": true
  }'
```

## Форматы аудиовыхода

Модели Gemini 3.8 TTS используют разные форматы аудио по умолчанию в зависимости от того, является ли запрос унарным или потоковым:

- **Унарные запросы (`stream=False`).** Возвращают полный аудиофайл **WAV (`audio/wav`)** со стандартным заголовком RIFF (24 кГц, моно, 16-битный PCM с прямым порядком байтов). Вы можете сохранить декодированные аудиобайты непосредственно в файл `.wav`, не добавляя вручную заголовок WAV.
- **Запросы на потоковую передачу (`stream=True`).** По умолчанию возвращают фрагменты **необработанного линейного PCM без заголовков (`audio/l16`)** (24 кГц, моно, 16-битный PCM с прямым порядком байтов), чтобы фрагменты можно было передавать в потоковом режиме или объединять непрерывно без заголовков контейнеров в каждом фрагменте.

Чтобы запросить другую кодировку или частоту дискретизации аудио, настройте `mime_type` и необязательный параметр `sample_rate` внутри `response_format`:

| Формат | На сумму `mime_type` | Описание |
| --- | --- | --- |
| **WAV** *(унарный по умолчанию)* | `"audio/wav"` | Несжатый файл WAV с заголовком RIFF (16-битный знаковый PCM с прямым порядком байтов, моно, по умолчанию 24 кГц). Значение по умолчанию для унарных запросов. |
| **Raw PCM (L16)** *(по умолчанию для потоковой передачи)* | `"audio/l16"` | Несжатый 16-битный аудиофайл PCM с линейной модуляцией, без заголовка, с прямым порядком байтов (24 кГц, моно). Значение по умолчанию для запросов на потоковую передачу. |
| **Mu-law** | `"audio/mulaw"` | 8-битный звук, закодированный по закону мю G.711 (обычно используется в североамериканских и японских системах телефонии/IVR). |
| **A-law** | `"audio/alaw"` | 8-битный аудиофайл, закодированный по алгоритму G.711 A-law (обычно используется в европейских и международных телефонных системах). |

Вы также можете указать `sample_rate` частоту обновления в герцах (например, `24000`, `16000` или
`8000`).

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={
        "type": "audio",
        "mime_type": "audio/l16",  # "audio/wav" (default), "audio/l16", "audio/mulaw", or "audio/alaw"
        "sample_rate": 24000,
    },
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
)

with open("out.pcm", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: {
         type: 'audio',
         mime_type: 'audio/l16', // 'audio/wav' (default), 'audio/l16', 'audio/mulaw', or 'audio/alaw'
         sample_rate: 24000,
      },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.pcm', audioBuffer);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio",
      "mime_type": "audio/l16",
      "sample_rate": 24000
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

## Параметры голосового ввода

Gemini 3.8 TTS поддерживает четыре способа выбора или создания голосов:

1. **Готовые студийные голоса.** 30 голосов, перечисленных в таблице ниже.
2. **Расширенная библиотека голосов.** Сотни дополнительных голосов на разных языках, с разными акцентами и архетипами персонажей, доступные через `client.voices.list()` (`GET /v1beta/voices`).
3. **[Голосовой дизайн.](https://ai.google.dev/gemini-api/docs/voice-design?hl=ru)** Создайте персонализированный голос на основе описания на естественном языке в [Google AI Studio](https://aistudio.google.com/generate-speech?hl=ru) или с помощью `POST /v1beta/voices` (`type="prompted"`, который возвращает постоянный идентификатор `voice_...` и предварительный просмотр WAV `sample_audio` в `CreateVoice` и `GetVoice`).
4. **[Репликация голоса.](https://ai.google.dev/gemini-api/docs/voice-replication?hl=ru)** Воспроизводите голос говорящего на основе референсного аудио и аудио с согласием в [Google AI Studio](https://aistudio.google.com/generate-speech?hl=ru) или с помощью `POST /v1beta/voices` (`type="replicated"`, постоянный `store=True` по умолчанию или необязательный `store=False` без сохранения состояния).

### Ограничения на использование собственного голоса и TTL

| Голосовой ввод | Режим хранения | Квота / лимит | Хранение (TTL) |
| --- | --- | --- | --- |
| **Голоса с сохранением состояния** (`voice_...`, с подсказками или скопированные) | `store=True` | **200 голосов на проект** (включая голоса, созданные по запросу и реплицированные). | **1 год с момента последнего использования\*** |
| **Ключи голосовой связи без сохранения состояния** (`voicekey_...`, реплицированные) | `store=False` | Управляемый клиентом | **7 дней** |

\* **Продление срока хранения TTL.** Годичный срок хранения сбрасывается каждый раз, когда голос активно используется (для синтеза речи или в качестве базового голоса для создания ремикса). Голоса, которые не использовались в течение года, удаляются автоматически.

### Готовые голоса

|  |  |  |
| --- | --- | --- |
| **Zephyr** – *Яркий* | **Puck** – *Upbeat* | **Харон** – *информативный*. |
| **Kore** – *Firm* | **Fenrir** – *возбудимый*. | **Leda** – *молодой голос*. |
| **Orus** – *Firm* | **Aoede** – *Breezy* | **Callirrhoe** – *расслабленный*. |
| **Autonoe** – *Bright* | **Enceladus** – *с придыханием* | **Iapetus** – *Clear* |
| **Umbriel** – *спокойный* | **Algieba** – *Smooth* | **Despina** – *Smooth* |
| **Erinome** – *Clear* | **Algenib** – *Gravelly* | **Rasalgethi** – *информативный* |
| **Лаомедея** – *энергичный* | **Achernar** – *Soft* | **Alnilam** – *фирма* |
| **Шедар** – *Равномерная ротация* | **Gacrux** – *зрелая* | **Pulcherrima** – *вперед* |
| **Ахирд** – *дружелюбный* | **Zubenelgenubi** – *Casual* | **Vindemiatrix** – *ласковый*. |
| **Sadachbia** – *Lively* | **Sadaltager** – *знающий* | **Сулафат** – *теплая* |

### Расширенная библиотека голосов и фильтрация

Помимо 30 голосов, перечисленных в таблице выше, в **расширенной библиотеке голосов** доступны сотни дополнительных голосов на разных языках, с региональными акцентами, а также голоса персонажей и из разных областей. Вы можете просматривать, фильтровать и прослушивать всю библиотеку голосов в интерактивном режиме в [Google AI Studio](https://aistudio.google.com/generate-speech?hl=ru) или запрашивать ее программно с помощью `client.voices.list()` (`GET /v1beta/voices`, используя `google-genai` 2.25.0+ / `@google/genai` 2.24.0+).

`ListVoices` возвращает ваши сохраненные голоса (сначала новые), а затем голоса из каталога, соответствующие критериям фильтра. Если для фильтра списка передано несколько значений, возвращаются голоса, соответствующие **любому** значению в этом фильтре (`OR`), а отдельные параметры фильтра объединяются с помощью `AND`:

| Параметр | Тип | Описание |
| --- | --- | --- |
| `language_code` | `list[str]` | Языковые теги BCP-47 (например, `["en-US", "en-GB"]`). Точное соответствие без учета регистра. |
| `region_code` | `list[str]` | Код региона ISO 3166-1 alpha-2 или UN M.49 (например, `["US", "GB"]`). |
| `accent` | `list[str]` | Региональный акцент (например, `["American", "British"]`). |
| `gender` | `list[str]` | Представление пола (`"female"`, `"male"` или `"neutral"`). |
| `pitch` | `list[str]` | Классификация высоты голоса (`"low"`, `"medium"` или `"high"`). |
| `persona` | `list[str]` | Архетип персонажа или голоса (например, `["Warm, Friendly"]`, `["Narrator"]`). |
| `contexts` (`context` в REST) | `list[str]` | Домен оптимального использования (например, `["Audiobook", "Conversational", "News"]`). |
| `type` (`type_` в Python) | `list[str]` | Фильтр по источнику голоса: `"prebuilt"`, `"prompted"` ([дизайн голоса](https://ai.google.dev/gemini-api/docs/voice-design?hl=ru)) или `"replicated"` ([воспроизведение голоса](https://ai.google.dev/gemini-api/docs/voice-replication?hl=ru)). |
| `search` | `str` | Поиск подстроки в свободном тексте без учета регистра по параметрам `display_name` и `description`. |
| `page_size` | `int` | Максимальное количество голосов, возвращаемых на страницу (по умолчанию `50`, максимум `1000`). |
| `page_token` | `str` | Токен из `response.next_page_token` для получения следующей страницы результатов. |

### Python

```
from google import genai

client = genai.Client()

# Filter the Voice Library by language, gender, pitch, domain context, and keyword
response = client.voices.list(
    language_code=["en-US", "en-GB"],
    gender=["female"],
    pitch=["medium", "low"],
    contexts=["Audiobook", "Conversational"],
    type_=["prebuilt"],
    search="warm",
    page_size=50,
)

for voice in response.voices or []:
    print(
        f"{voice.id} | {voice.display_name} ({voice.language_code},"
        f" {voice.accent}, {voice.gender}, pitch={voice.pitch}):"
        f" {voice.description}"
    )
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// Filter the Voice Library by language, gender, pitch, domain context, and keyword
const response = await ai.voices.list({
  language_code: ["en-US", "en-GB"],
  gender: ["female"],
  pitch: ["medium", "low"],
  contexts: ["Audiobook", "Conversational"],
  type: ["prebuilt"],
  search: "warm",
  page_size: 50,
});

for (const voice of response.voices ?? []) {
  console.log(
    `${voice.id} | ${voice.display_name} (${voice.language_code}, ${voice.accent}, ${voice.gender}, pitch=${voice.pitch}): ${voice.description}`
  );
}
```

### REST

```
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB" \
  --data-urlencode "gender=female" \
  --data-urlencode "pitch=medium" \
  --data-urlencode "context=Audiobook" \
  --data-urlencode "type=prebuilt" \
  --data-urlencode "search=warm" \
  --data-urlencode "page_size=50"
```

## Поддерживаемые языки

Модели TTS автоматически определяют язык ввода.
[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ru) (`gemini-3.8-flash-tts`) поддерживает **более 130 языков**, а [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=ru) (`gemini-3.8-flash-lite-tts`) – **более 100 языков**.

| Язык | Gemini 3.8 Flash TTS | Gemini 3.8 Flash-Lite TTS |
| --- | --- | --- |
| Ачехский (арабская письменность) | ✔️ | ✔️ |
| Африкаанс | ✔️ | ✔️ |
| Акан | ✔️ | ✔️ |
| Амхарский | ✔️ | ✔️ |
| Армянский | ✔️ | ✔️ |
| Ассамский | ✔️ | ✔️ |
| Авадхи | ✔️ | ✔️ |
| Балийский | ✔️ | ✔️ |
| Бенгальский | ✔️ | ✔️ |
| Банджарский (арабское письмо) | ✔️ | — |
| Банджарский (латиница) | ✔️ | ✔️ |
| Башкирский | ✔️ | — |
| Баскский | ✔️ | ✔️ |
| Belarusian | ✔️ | ✔️ |
| бемба | ✔️ | — |
| Бходжпури | ✔️ | ✔️ |
| Боснийский | ✔️ | ✔️ |
| Бугийский | ✔️ | ✔️ |
| Болгарский | ✔️ | ✔️ |
| Бирманский | ✔️ | — |
| Кантонский | ✔️ | ✔️ |
| Каталанский | ✔️ | ✔️ |
| Себуанский | ✔️ | ✔️ |
| Центральнокурдский | ✔️ | ✔️ |
| Чхаттисгархи | ✔️ | ✔️ |
| Китайский (упрощенный) | ✔️ | ✔️ |
| Китайский (традиционное письмо) | ✔️ | ✔️ |
| Крымско-татарский | ✔️ | — |
| Хорватский | ✔️ | ✔️ |
| Чешский | ✔️ | ✔️ |
| Датский | ✔️ | ✔️ |
| Нидерландский | ✔️ | ✔️ |
| Дьюла | ✔️ | — |
| Дзонг-кэ | ✔️ | — |
| арабский (Египет) | ✔️ | ✔️ |
| Английский | ✔️ | ✔️ |
| Эстонский | ✔️ | ✔️ |
| Филиппинский | ✔️ | ✔️ |
| Финский | ✔️ | — |
| Французский | ✔️ | ✔️ |
| Галисийский | ✔️ | ✔️ |
| Ganda | ✔️ | ✔️ |
| Грузинский | ✔️ | ✔️ |
| Немецкий | ✔️ | ✔️ |
| Греческий | ✔️ | ✔️ |
| Гуарани | ✔️ | — |
| Гуджарати | ✔️ | ✔️ |
| Гаитянский креольский | ✔️ | ✔️ |
| Халха-монгольский | ✔️ | ✔️ |
| Хауса | ✔️ | ✔️ |
| Иврит | ✔️ | ✔️ |
| хинди | ✔️ | ✔️ |
| Венгерский | ✔️ | ✔️ |
| Исландский | ✔️ | ✔️ |
| Игбо | ✔️ | — |
| илоканский | ✔️ | ✔️ |
| Индонезийский | ✔️ | ✔️ |
| персидский (Иран) | ✔️ | ✔️ |
| Итальянский | ✔️ | ✔️ |
| Японский | ✔️ | ✔️ |
| Яванский | ✔️ | ✔️ |
| кабильский | ✔️ | — |
| Камба | ✔️ | ✔️ |
| Каннада | ✔️ | ✔️ |
| кашмири (арабское письмо) | ✔️ | ✔️ |
| кашмири (деванагари) | ✔️ | ✔️ |
| Казахский | ✔️ | ✔️ |
| Кхмерский | ✔️ | ✔️ |
| Кикуйю | ✔️ | ✔️ |
| Киньяруанда | ✔️ | ✔️ |
| Конго | ✔️ | ✔️ |
| Корейский | ✔️ | ✔️ |
| Киргизский | ✔️ | ✔️ |
| Лаосский | ✔️ | ✔️ |
| Латгальский | ✔️ | — |
| Лингала | ✔️ | ✔️ |
| Литовский | ✔️ | — |
| Люксембургский | ✔️ | — |
| Македонский | ✔️ | ✔️ |
| Магахи | ✔️ | ✔️ |
| Майтхили | ✔️ | ✔️ |
| Малаялам | ✔️ | ✔️ |
| Мальтийский | ✔️ | ✔️ |
| Манипури | ✔️ | ✔️ |
| Маратхи | ✔️ | ✔️ |
| Минангкабау (арабское письмо) | ✔️ | ✔️ |
| Минангкабау (латиница) | ✔️ | — |
| Мизо | ✔️ | ✔️ |
| Непальский (отдельный язык) | ✔️ | ✔️ |
| Фула (Нигерия) | ✔️ | ✔️ |
| Североазербайджанский | ✔️ | ✔️ |
| Сото северный | ✔️ | ✔️ |
| Северный узбекский | ✔️ | ✔️ |
| Норвежский букмол | ✔️ | ✔️ |
| Норвежский (новонорвежский) | ✔️ | ✔️ |
| Ньянджа | ✔️ | ✔️ |
| Окситанский | ✔️ | — |
| Ория (отдельный язык) | ✔️ | ✔️ |
| Пангасинанский | ✔️ | — |
| Персидский (Афганистан) | ✔️ | ✔️ |
| Польский | ✔️ | ✔️ |
| Португальский | ✔️ | ✔️ |
| Пенджабский | ✔️ | ✔️ |
| Румынский | ✔️ | ✔️ |
| Русский | ✔️ | ✔️ |
| Сантали | ✔️ | ✔️ |
| Сербский | ✔️ | ✔️ |
| Синдхи | ✔️ | — |
| Сингальский | ✔️ | ✔️ |
| Словацкий | ✔️ | ✔️ |
| Словенский | ✔️ | — |
| Сомали | ✔️ | — |
| Южноазербайджанский | ✔️ | ✔️ |
| Южный пушту | ✔️ | ✔️ |
| Южный сото | ✔️ | — |
| Испанский | ✔️ | ✔️ |
| Стандартный арабский (арабское письмо) | ✔️ | ✔️ |
| Стандартный арабский (латиница) | ✔️ | ✔️ |
| Стандартный латышский | ✔️ | ✔️ |
| Стандартный малайский | ✔️ | ✔️ |
| Суахили (отдельный язык) | ✔️ | — |
| Свати | ✔️ | — |
| Шведский | ✔️ | — |
| Таджикский | ✔️ | — |
| Тамильский | ✔️ | ✔️ |
| Телугу | ✔️ | ✔️ |
| Тайский | ✔️ | — |
| Тигринский | ✔️ | — |
| Тоскский (албанский) | ✔️ | — |
| Турецкий | ✔️ | ✔️ |
| Уйгурский | ✔️ | — |
| Вьетнамский | ✔️ | ✔️ |

## Поддерживаемые модели

| Модель | Один говорящий | Несколько говорящих | Дизайн голоса | Репликация голоса |
| --- | --- | --- | --- | --- |
| [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ru) (`gemini-3.8-flash-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=ru) (`gemini-3.8-flash-lite-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Предварительная версия Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=ru) | ✔️ | ✔️ | — | — |
| [Gemini 2.5 Pro Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=ru) | ✔️ | ✔️ | — | — |

### Когда использовать ту или иную модель

Обе модели Gemini 3.8 TTS используют одну и ту же схему API и формат запросов, поэтому вы можете переключаться между ними, изменив всего один параметр:

- **Используйте [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ru) (`gemini-3.8-flash-tts`)**, когда максимальная акустическая точность, нюансы актерской игры и выразительность речи являются главными приоритетами. Она идеально подходит для создания креативов студийного качества, сложных диалогов с несколькими говорящими, тегов с тяжелыми вокальными всплесками, сложных произношений, региональных диалектов или диалектов меньшинств, а также длинных повествований, требующих стабильного голоса и тона помещения.
- **Используйте [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=ru)
  (`gemini-3.8-flash-lite-tts`)** в качестве быстрой и экономичной замены `gemini-3.1-flash-tts-preview`. Она оптимизирована для массового производства, каскадов разговорных голосовых агентов, функций чтения вслух, надежной репликации голоса и повседневной речи одного говорящего на основных языках.

### Руководство по переходу

Если вы переходите с `gemini-3.1-flash-tts-preview` или более ранних моделей Gemini TTS на Gemini 3.8 TTS:

1. **Перенос пошаговых инструкций в `speech_metadata`.** Gemini 3.8 TTS воспринимает входной текст как дословную транскрипцию. Переместите инструкции по непрерывной доставке (`style`, например `"whispering"`, `"out of breath"` или `"speaking slowly"`) и обозначения говорящих (`speaker`) в структурированные аннотации `speech_metadata`, а не встраивайте ремарки в текст расшифровки.
2. **Используйте встроенные теги в угловых скобках только для кратковременных звуков.** Кратковременные звуки, не являющиеся речью, и паузы следует обозначать в расшифровке с помощью угловых скобок, например `<laugh>`, `<sigh>`, `<cough>`, `<breath>` или `<short pause>`. Не используйте теги звуковых эффектов (например, аплодисментов или стука) и указывайте манеру речи в `speech_metadata.style`.
3. **Указывайте `speaker` в каждом ответе на запрос с несколькими говорящими.** Каждый ответ на запрос с несколькими говорящими должен явно содержать `speaker` внутри `speech_metadata`, соответствующий одному из настроенных говорящих.
4. **Заранее создавайте персонажей с помощью Voice Design.** Замените блоки `"Audio Profile"` или `"Director's Notes"`, состоящие из нескольких абзацев, голосом, созданным в [Voice Design](https://ai.google.dev/gemini-api/docs/voice-design?hl=ru), а затем передавайте идентификатор `voice_...` в запросах TTS с минимальными или пустыми строками `style`.
5. **Учитывайте, что по умолчанию для унарных запросов возвращается WAV-аудио (`audio/wav`).** В отличие от `gemini-3.1-flash-tts-preview` и более ранних моделей TTS, которые по умолчанию возвращали необработанный PCM-аудиопоток без заголовка (`audio/l16`), Gemini 3.8 TTS по умолчанию возвращает WAV-аудио (`audio/wav`) со стандартным заголовком RIFF для унарных запросов.
   - Если в вашем коде необработанные байты PCM ранее упаковывались в заголовок WAV (например, с помощью модуля `wave` в Python или `ffmpeg`), удалите упаковку заголовка вручную и запишите возвращенные байты непосредственно в файл `.wav`.
   - Если для вашего конвейера требуется необработанный PCM, mu-law или A-law без заголовка, явно задайте для `response_format.mime_type` значение `"audio/l16"`, `"audio/mulaw"` или `"audio/alaw"` (например, `{"response_format": {"type": "audio", "mime_type": "audio/l16"}}` в Interactions API или `AUDIO_L16` в `generateContent`). Подробнее [о форматах аудиовыхода](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ru#audio-output-formats)…

## Руководство по запросам

Модели Gemini 3.8 TTS воспринимают входной текст как **дословную расшифровку**.
В отличие от предыдущих предварительных версий моделей, в которых ремарки были встроены в обычный текст, в Gemini 3.8 TTS ремарки на уровне реплики (`speech_metadata`) отделены от встроенных тегов, относящихся к определенному моменту.

### Поле стиля и встроенные теги

Разделите инструкции по производительности по области применения:

- **Построчное воспроизведение (`speech_metadata.style`).** Укажите атрибуты, связанные с устойчивым воспроизведением, например эмоции, просодию, общий темп или стиль воспроизведения (`"whispering"`, `"out of breath"`, `"muttering"` или `"sarcastic"`), в поле `style` объекта `speech_metadata`. Чтобы создать стабильного персонажа и обеспечить стабильность его действий, сначала задайте его образ в разделе [Дизайн голоса](https://ai.google.dev/gemini-api/docs/voice-design?hl=ru), а затем используйте `style` только для необязательных изменений на уровне хода.
- **События в определенный момент времени (встроенные теги).** Помещайте мгновенные неречевые вокальные всплески, вдохи или паузы в расшифровку, используя угловые скобки (`<cough>`, `<breath>`, `<sigh>`, `<short pause>`). Используйте угловые скобки (`<...>`) для наивысшего качества звука и придерживайтесь человеческой вокализации, а не невокальных звуковых эффектов.

| Область действия | Где разместить | Примеры |
| --- | --- | --- |
| **На уровне поворота** (поддерживается на протяжении всего поворота) | `speech_metadata.style` | `"angry tone"`, `"speaking rapidly"`, `"out of breath"`, `"whispers"`, `"sarcastic"` |
| **В определенный момент** (в определенном слове). | Встроенный в `text` (`<...>`) | `"<cough> Thank you all for coming tonight! <throat-clearing> As I was saying..."` |

### Темп и паузы

Вы можете управлять ритмом и паузами на трех уровнях детализации:

- **Знаки препинания и многоточия.** Используйте запятые, тире (`--`) и многоточия (`...`), чтобы имитировать естественные паузы в речи.
- **Встроенные теги пауз.** Вставьте `<short pause>` или `<long pause>` в те места скрипта, где спикер должен сделать паузу:
  `text
  Hold on, let me think... <short pause> Alright, I've got it.`
- **Темп на уровне реплики.** Установите `"style": "speaking rapidly"` или `"style": "speaking slowly"` в `speech_metadata`, чтобы контролировать скорость речи на протяжении всей реплики.

### Просодия и высота тона

Используйте **`speech_metadata.style`**, чтобы управлять просодией, высотой тона и интонацией в реплике (например, `"style": "high pitch, cheerful and excited inflection"` или `"style": "monotone and flat"`). Если эмоция или просодия меняется в середине диалога, разделите скрипт на отдельные реплики с разными значениями `style` для каждой.

### Выделение

Чтобы сделать акцент на ключевых словах, пишите их с заглавной буквы, используйте знаки препинания и теги:

```
This is a VERY important point!
It was a VERY long day <sigh> ... nobody listens anymore.
```

### Вокальные всплески и неречевые звуки

Невербальные звуки, издаваемые человеком, следует вставлять в текст с помощью угловых скобок (`<...>`) в том месте, где должен звучать звук. Рекомендуемые теги для вокала:

|  |  |  |  |
| --- | --- | --- | --- |
| `<argh>` | `<breath>` | `<heavy breath>` | `<exhales>` |
| `<cackle>` | `<cheer>` | `<chuckle>`/`<chuckles>` | `<cough>` |
| `<cry>` | `<gasp>` | `<giggle>` | `<groan>` |
| `<growl>` | `<grunt>` | `<grr>` | `<hiss>` |
| `<laugh>`/`<laughter>` | `<moan>` | `<pant>` | `<pff>`/`<phew>` |
| `<scream>` | `<shout>` | `<shriek>` | `<sigh>`/`<sighs>` |
| `<sneeze>` | `<snicker>` | `<snort>` | `<sob>` |
| `<throat-clearing>` | `<tsk>` | `<whimper>` | `<whispers>`/`<whispering>` |
| `<yawn>` | `<short pause>` | `<long pause>` |  |

### Дополнительные каналы и перекрывающиеся реплики

В диалоге с несколькими говорящими заключайте реакции слушателей в вертикальные черты (`|reaction|`) внутри реплики говорящего, чтобы создать естественные фоновые звуки или перекрывающуюся речь, не разбивая каждую реакцию на отдельную реплику.

- **Короткие фоновые реплики.** Добавляйте короткие реакции слушателя (`|oh hmm|`, `|oh really?|`, `|absolutely|`) в реплику выступающего участника:
  - **Реплика 1 (собеседник А):** `"So the launch is Thursday |oh hmm| Are we actually ready?"`
  - **Ход 2 (Докладчик Б):** `"Ready enough |oh really?| The last blocker cleared this morning."`
  - **Реплика 3 (собеседник А):** `"Then let's ship it |absolutely| and watch the dashboards."`
- **Перекрывающаяся и чередующаяся речь.** Используйте несколько сегментов, разделенных вертикальной чертой, чтобы имитировать одновременную или чередующуюся речь двух говорящих (лучше всего работает с `gemini-3.8-flash-tts`):
  - **Одновременный обратный отсчет и припев:** `"Let's surprise him on three |ok| ready?"`, а затем `"one. two. three. |happy| happy |birthday| birthday!"`.
  - **Полное перекрытие динамиков:** `"Hello |oh| there |my| it |goodness| must |gracious| be |would| almost |you| time |look| for |at that| dinner"`

### Согласованность между поколениями и чего следует избегать

Чтобы голос не менялся от реплики к реплике, следуйте этим рекомендациям:

- **Задавайте персонажей в начале инструкций по стилю, а не в длинных блоках.**
  Длинные абзацы `"Audio Profile"` и списки `"Director's Notes"`, перенесенные из более ранних моделей, – самая распространенная причина отклонения от заданного стиля.
  Используйте ту же творческую интуицию в [Voice Design](https://ai.google.dev/gemini-api/docs/voice-design?hl=ru), чтобы создать постоянного персонажа `voice_...`, а затем используйте этот идентификатор голоса в вызовах TTS.
- **Опирайтесь на образец голоса (не используйте метаинструкции).** Модели Gemini 3.8 TTS обучены в первую очередь ориентироваться на аудиообразец.
  Не добавляйте инструкции, которые предписывают модели сохранять голос стабильным (например, `"do not switch speaker identity"` или `"maintain identical timbre"`). Дополнительный текст в запросе увеличивает дрейф. Удалите ненужные инструкции по стилю и позвольте модели естественно варьировать голос вокруг стабильной точки, заданной референсным голосом.
- **Не пытайтесь изменить неизменяемые характеристики говорящего в `style`.** Не указывайте в `speech_metadata.style` возраст, пол, имена или постоянные изменения акцента.
  Вместо этого выберите региональный голос из расширенной фонотеки или создайте его с помощью [Voice design](https://ai.google.dev/gemini-api/docs/voice-design?hl=ru).

### Рекомендуемый рабочий процесс

1. **Создайте персонажа.** Сделайте это в [Voice Design](https://ai.google.dev/gemini-api/docs/voice-design?hl=ru) или выберите региональный голос из расширенной библиотеки, который соответствует языку целевой аудитории и персонажу.
2. **Создавайте естественные расшифровки с ошибками речи.** Чтобы речь звучала максимально естественно, напишите `text` как реальную расшифровку, включая ошибки и колебания (например, `"Oh uh yeah I think... hm, so that's interesting"`).
3. **Сначала попробуйте обычное преобразование текста в речь.** Синтезируйте речь из расшифровки с пустым полем `style`. В большинстве случаев инструкции `style` не нужны.
4. **Добавляйте короткие подсказки `style` только для корректировок.** Добавляйте краткую строку `style` (например, `"casual, friendly"` или `"muttering, then reassuring"`) только для реплик, требующих определенной корректировки подачи, и повторно используйте эту короткую строку в разных репликах, когда хотите получить согласованную базовую линию.

### Диалоги с несколькими репликами и голосовые агенты

При создании голосовых агентов для разговоров в реальном времени или пошаговых приложений:

- Выполняйте **один вызов TTS за ход** по мере поступления текстовых фрагментов LLM.
- Пусть настроенный `voice` (готовый, разработанный `voice_...` или реплицированный `voice_...` / `voicekey_...`) передает личность говорящего в разных репликах. Никогда не отправляйте повторно длинную персону персонажа в каждой реплике.
- Оставьте поле `style` пустым или отправьте короткую строку (например, `"casual, friendly"`) для всего разговора.
- Разбивайте длинные ответы агента на более короткие, а не используйте более сильные запросы к стилю.

## Ограничения

- Модели TTS принимают на вход только текст и генерируют только аудио.
- Генерация аудио с несколькими говорящими по одному запросу (`speech_config.speakers`) поддерживает до двух говорящих со встроенными голосами. Чтобы объединить специально созданные (`voice_...`) или скопированные (`voice_...` / `voicekey_...`) голоса в диалоге с несколькими персонажами, синтезируйте реплики каждого из них по отдельности.
  Поскольку унарные запросы по умолчанию возвращают `audio/wav` с 44-байтовым заголовком RIFF, запросите необработанный PCM (`{"type": "audio", "mime_type": "audio/l16"}`) или удалите заголовок WAV из каждого поворота перед объединением аудиокадров PCM с частотой 24 кГц.
- **Ограничения на хранение и TTL собственного голоса.**
  - **Голоса с отслеживанием состояния (`store=True`, созданные по запросу или реплицированные):** максимум **200 голосов на проект** с **временем жизни 1 год (TTL)**.
  - **Ключи для голосового управления без сохранения состояния (`store=False`, `voicekey_...`):** **время жизни – 7 дней**.
- Ознакомьтесь с информацией о поддерживаемых языках в разделе [Поддерживаемые языки](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ru#languages).

## Дальнейшие действия

- Создавайте собственные голоса, используя запросы на естественном языке, с помощью функции [Голосовой дизайн](https://ai.google.dev/gemini-api/docs/voice-design?hl=ru).
- Воссоздать голос существующего докладчика с помощью [репликации голоса](https://ai.google.dev/gemini-api/docs/voice-replication?hl=ru).
- Сравните характеристики моделей на страницах [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ru) и [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=ru).
- Попробуйте интерактивное двустороннее аудио с [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ru).

Отправить отзыв

Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-10-12 UTC.

Хотите рассказать подробнее?

[[["Прост для понимания","easyToUnderstand","thumb-up"],["Помог мне решить мою проблему","solvedMyProblem","thumb-up"],["Другое","otherUp","thumb-up"]],[["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"],["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"],["Устарел","outOfDate","thumb-down"],["Проблема с переводом текста","translationIssue","thumb-down"],["Проблемы образцов/кода","samplesCodeIssue","thumb-down"],["Другое","otherDown","thumb-down"]],["Последнее обновление: 2026-10-12 UTC."],[],[]]
