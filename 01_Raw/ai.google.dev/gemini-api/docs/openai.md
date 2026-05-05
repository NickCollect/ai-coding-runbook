---
source_url: https://ai.google.dev/gemini-api/docs/openai?hl=pl
fetched_at: 2026-05-05T13:17:17.087410+00:00
title: "Zgodno\u015b\u0107 z\u00a0OpenAI \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

- [Strona główna](https://ai.google.dev/gemini-api/docs/Strona główna)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Dokumenty](https://ai.google.dev/gemini-api/docs/Dokumenty)

Prześlij opinię

# Zgodność z OpenAI

Modele Gemini są dostępne przy użyciu bibliotek OpenAI (Python i TypeScript/JavaScript) oraz interfejsu REST API. Wystarczy zaktualizować 3 linie kodu i użyć [klucza interfejsu Gemini API](https://ai.google.dev/gemini-api/docs/klucza interfejsu Gemini API). Jeśli nie korzystasz jeszcze z bibliotek OpenAI, zalecamy bezpośrednie wywoływanie [interfejsu Gemini API](https://ai.google.dev/gemini-api/docs/interfejsu Gemini API).

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {   "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3-flash-preview",
    messages: [
        {   role: "system",
            content: "You are a helpful assistant." 
        },
        {
            role: "user",
            content: "Explain to me how AI works",
        },
    ],
});

console.log(response.choices[0].message);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3-flash-preview",
    "messages": [
      {
        "role": "user",
        "content": "Explain to me how AI works"
      }
    ]
  }'
```

Co się zmieniło? Tylko 3 wiersze!

- **`api_key="GEMINI_API_KEY"`**: zastąp „`GEMINI_API_KEY`” rzeczywistym kluczem interfejsu Gemini API, który możesz uzyskać w [Google AI Studio](https://ai.google.dev/gemini-api/docs/Google AI Studio).
- **`base_url="https://generativelanguage.googleapis.com/v1beta/openai/"`:** ten kod informuje bibliotekę OpenAI, aby wysyłała żądania do punktu końcowego Gemini API zamiast do domyślnego adresu URL.
- **`model="gemini-3-flash-preview"`**: wybierz zgodny model Gemini

## Myślę

Modele Gemini są trenowane w taki sposób, aby analizować złożone problemy, co znacznie poprawia ich zdolność do rozumowania. Interfejs Gemini API ma [parametry myślenia](https://ai.google.dev/gemini-api/docs/parametry myślenia), które zapewniają precyzyjną kontrolę nad tym, jak bardzo model będzie myśleć.

Różne modele Gemini mają różne konfiguracje rozumowania. Możesz sprawdzić, jak odpowiadają one działaniom OpenAI w zakresie rozumowania:

| `reasoning_effort` (OpenAI) | `thinking_level` (Gemini 3.1 Pro) | `thinking_level` (Gemini 3.1 Flash-Lite) | `thinking_level` (Gemini 3 Flash) | `thinking_budget` (Gemini 2.5) |
| --- | --- | --- | --- | --- |
| `minimal` | `low` | `minimal` | `minimal` | `1,024` |
| `low` | `low` | `low` | `low` | `1,024` |
| `medium` | `medium` | `medium` | `medium` | `8,192` |
| `high` | `high` | `high` | `high` | `24,576` |

Jeśli nie podasz wartości `reasoning_effort`, Gemini użyje domyślnego [poziomu](https://ai.google.dev/gemini-api/docs/poziomu) lub [budżetu](https://ai.google.dev/gemini-api/docs/budżetu) modelu.

Jeśli chcesz wyłączyć myślenie, możesz ustawić `reasoning_effort` na `"none"` w przypadku modeli 2.5. Nie można wyłączyć rozumowania w przypadku modeli Gemini 2.5 Pro ani 3.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    reasoning_effort="low",
    messages=[
        {   "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3-flash-preview",
    reasoning_effort: "low",
    messages: [
        {   role: "system",
            content: "You are a helpful assistant." 
        },
        {
            role: "user",
            content: "Explain to me how AI works",
        },
    ],
});

console.log(response.choices[0].message);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3-flash-preview",
    "reasoning_effort": "low",
    "messages": [
      {
        "role": "user",
        "content": "Explain to me how AI works"
      }
    ]
  }'
```

Modele myślowe Gemini generują też [podsumowania myśli](https://ai.google.dev/gemini-api/docs/podsumowania myśli).
W polu [`extra_body`](https://ai.google.dev/gemini-api/docs/`extra_body`) możesz uwzględnić w żądaniu pola Gemini.

Pamiętaj, że funkcje `reasoning_effort` i `thinking_level`/`thinking_budget` nakładają się na siebie, więc nie można ich używać w tym samym czasie.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[{"role": "user", "content": "Explain to me how AI works"}],
    extra_body={
      'extra_body': {
        "google": {
          "thinking_config": {
            "thinking_level": "low",
            "include_thoughts": True
          }
        }
      }
    }
)

print(response.choices[0].message)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3-flash-preview",
    messages: [{role: "user", content: "Explain to me how AI works",}],
    extra_body: {
      "google": {
        "thinking_config": {
          "thinking_level": "low",
          "include_thoughts": true
        }
      }
    }
});

console.log(response.choices[0].message);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3-flash-preview",
        "messages": [{"role": "user", "content": "Explain to me how AI works"}],
        "extra_body": {
          "google": {
            "thinking_config": {
              "thinking_level": "low",
              "include_thoughts": true
            }
          }
        }
      }'
```

Gemini 3 obsługuje zgodność z OpenAI w przypadku sygnatur myśli w interfejsach API do uzupełniania czatu. Pełny przykład znajdziesz na stronie [podpisów myślowych](https://ai.google.dev/gemini-api/docs/podpisów myślowych).

## Streaming

Interfejs Gemini API obsługuje [strumieniowanie odpowiedzi](https://ai.google.dev/gemini-api/docs/strumieniowanie odpowiedzi).

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
  model="gemini-3-flash-preview",
  messages=[
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {   "role": "user",
        "content": "Hello!"
    }
  ],
  stream=True
)

for chunk in response:
    print(chunk.choices[0].delta)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
  const completion = await openai.chat.completions.create({
    model: "gemini-3-flash-preview",
    messages: [
      {
          "role": "system",
          "content": "You are a helpful assistant."
      },
      {
          "role": "user",
          "content": "Hello!"
      }
    ],
    stream: true,
  });

  for await (const chunk of completion) {
    console.log(chunk.choices[0].delta.content);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3-flash-preview",
      "messages": [
          {"role": "user", "content": "Explain to me how AI works"}
      ],
      "stream": true
    }'
```

## Wywoływanie funkcji

Wywoływanie funkcji ułatwia uzyskiwanie ustrukturyzowanych danych wyjściowych z modeli generatywnych i jest [obsługiwane w interfejsie Gemini API](https://ai.google.dev/gemini-api/docs/obsługiwane w interfejsie Gemini API).

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

tools = [
  {
    "type": "function",
    "function": {
      "name": "get_weather",
      "description": "Get the weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. Chicago, IL",
          },
          "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        },
        "required": ["location"],
      },
    }
  }
]

messages = [{"role": "user", "content": "What's the weather like in Chicago today?"}]
response = client.chat.completions.create(
  model="gemini-3-flash-preview",
  messages=messages,
  tools=tools,
  tool_choice="auto"
)

print(response)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
  const messages = [{"role": "user", "content": "What's the weather like in Chicago today?"}];
  const tools = [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "Get the weather in a given location",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. Chicago, IL",
              },
              "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
          },
        }
      }
  ];

  const response = await openai.chat.completions.create({
    model: "gemini-3-flash-preview",
    messages: messages,
    tools: tools,
    tool_choice: "auto",
  });

  console.log(response);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer GEMINI_API_KEY" \
-d '{
  "model": "gemini-3-flash-preview",
  "messages": [
    {
      "role": "user",
      "content": "What'\''s the weather like in Chicago today?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. Chicago, IL"
            },
            "unit": {
              "type": "string",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["location"]
        }
      }
    }
  ],
  "tool_choice": "auto"
}'
```

## Rozpoznawanie obrazów

Modele Gemini są natywnie multimodalne i zapewniają najlepszą w swojej klasie wydajność w przypadku [wielu typowych zadań związanych z analizą obrazu](https://ai.google.dev/gemini-api/docs/wielu typowych zadań związanych z analizą obrazu).

### Python

```
import base64
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Getting the base64 string
base64_image = encode_image("Path/to/agi/image.jpeg")

response = client.chat.completions.create(
  model="gemini-3-flash-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url":  f"data:image/jpeg;base64,{base64_image}"
          },
        },
      ],
    }
  ],
)

print(response.choices[0])
```

### JavaScript

```
import OpenAI from "openai";
import fs from 'fs/promises';

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function encodeImage(imagePath) {
  try {
    const imageBuffer = await fs.readFile(imagePath);
    return imageBuffer.toString('base64');
  } catch (error) {
    console.error("Error encoding image:", error);
    return null;
  }
}

async function main() {
  const imagePath = "Path/to/agi/image.jpeg";
  const base64Image = await encodeImage(imagePath);

  const messages = [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url": `data:image/jpeg;base64,${base64Image}`
          },
        },
      ],
    }
  ];

  try {
    const response = await openai.chat.completions.create({
      model: "gemini-3-flash-preview",
      messages: messages,
    });

    console.log(response.choices[0]);
  } catch (error) {
    console.error("Error calling Gemini API:", error);
  }
}

main();
```

### REST

```
bash -c '
  base64_image=$(base64 -i "Path/to/agi/image.jpeg");
  curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer GEMINI_API_KEY" \
    -d "{
      \"model\": \"gemini-3-flash-preview\",
      \"messages\": [
        {
          \"role\": \"user\",
          \"content\": [
            { \"type\": \"text\", \"text\": \"What is in this image?\" },
            {
              \"type\": \"image_url\",
              \"image_url\": { \"url\": \"data:image/jpeg;base64,${base64_image}\" }
            }
          ]
        }
      ]
    }"
'
```

## Generowanie obrazu

Wygeneruj obraz za pomocą ikony `gemini-2.5-flash-image` lub `gemini-3-pro-image-preview`. Obsługiwane parametry to `prompt`, `model`, `n`, `size` i `response_format`. Wszelkie inne parametry, których nie ma na tej liście ani w sekcji [`extra_body`](https://ai.google.dev/gemini-api/docs/`extra_body`), będą cicho ignorowane przez warstwę zgodności.

### Python

```
import base64
from openai import OpenAI
from PIL import Image
from io import BytesIO

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = client.images.generate(
    model="gemini-2.5-flash-image",
    prompt="a portrait of a sheepadoodle wearing a cape",
    response_format='b64_json',
    n=1,
)

for image_data in response.data:
  image = Image.open(BytesIO(base64.b64decode(image_data.b64_json)))
  image.show()
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

async function main() {
  const image = await openai.images.generate(
    {
      model: "gemini-2.5-flash-image",
      prompt: "a portrait of a sheepadoodle wearing a cape",
      response_format: "b64_json",
      n: 1,
    }
  );

  console.log(image.data);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/images/generations" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer GEMINI_API_KEY" \
  -d '{
        "model": "gemini-2.5-flash-image",
        "prompt": "a portrait of a sheepadoodle wearing a cape",
        "response_format": "b64_json",
        "n": 1,
      }'
```

## Wygeneruj film

Wygeneruj film za pomocą `veo-3.1-generate-preview` za pośrednictwem punktu końcowego zgodnego z Sora`/v1/videos`. Obsługiwane parametry najwyższego poziomu to `prompt` i `model`. Dodatkowe parametry, takie jak `duration_seconds`, `image` i `aspect_ratio`, muszą być przekazywane za pomocą parametru `extra_body`. Wszystkie dostępne parametry znajdziesz w sekcji [`extra_body`](https://ai.google.dev/gemini-api/docs/`extra_body`).

Generowanie filmu to długo trwająca operacja, która zwraca identyfikator operacji, za pomocą którego możesz sprawdzać, czy została ona zakończona.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Returns a Long Running Operation (status: processing)
response = client.videos.create(
    model="veo-3.1-generate-preview",
    prompt="A cinematic drone shot of a waterfall",
)

print(f"Operation ID: {response.id}")
print(f"Status: {response.status}")
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
    // Returns a Long Running Operation (status: processing)
    const response = await openai.videos.create({
        model: "veo-3.1-generate-preview",
        prompt: "A cinematic drone shot of a waterfall",
    });

    console.log(`Operation ID: ${response.id}`);
    console.log(`Status: ${response.status}`);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/videos" \
  -H "Authorization: Bearer $GEMINI_API_KEY" \
  -F "model=veo-3.1-generate-preview" \
  -F "prompt=A cinematic drone shot of a waterfall"
```

### Sprawdzanie stanu filmu

Generowanie filmu jest asynchroniczne. Użyj `GET /v1/videos/{id}`, aby sprawdzić stan
i pobrać końcowy adres URL filmu po zakończeniu:

### Python

```
import time
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Poll until video is ready
video_id = response.id  # From the create call
while True:
    video = client.videos.retrieve(video_id)
    if video.status == "completed":
        print(f"Video URL: {video.url}")
        break
    elif video.status == "failed":
        print(f"Generation failed: {video.error}")
        break
    print(f"Status: {video.status}. Waiting...")
    time.sleep(10)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
    // Poll until video is ready
    const videoId = response.id;  // From the create call
    while (true) {
        const video = await openai.videos.retrieve(videoId);
        if (video.status === "completed") {
            console.log(`Video URL: ${video.url}`);
            break;
        } else if (video.status === "failed") {
            console.log(`Generation failed: ${video.error}`);
            break;
        }
        console.log(`Status: ${video.status}. Waiting...`);
        await new Promise(resolve => setTimeout(resolve, 10000));
    }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/videos/VIDEO_ID" \
  -H "Authorization: Bearer $GEMINI_API_KEY"
```

## Rozpoznawanie dźwięku

Analizowanie danych wejściowych audio:

### Python

```
import base64
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

with open("/path/to/your/audio/file.wav", "rb") as audio_file:
  base64_audio = base64.b64encode(audio_file.read()).decode('utf-8')

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Transcribe this audio",
        },
        {
              "type": "input_audio",
              "input_audio": {
                "data": base64_audio,
                "format": "wav"
          }
        }
      ],
    }
  ],
)

print(response.choices[0].message.content)
```

### JavaScript

```
import fs from "fs";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

const audioFile = fs.readFileSync("/path/to/your/audio/file.wav");
const base64Audio = Buffer.from(audioFile).toString("base64");

async function main() {
  const response = await client.chat.completions.create({
    model: "gemini-3-flash-preview",
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "Transcribe this audio",
          },
          {
            type: "input_audio",
            input_audio: {
              data: base64Audio,
              format: "wav",
            },
          },
        ],
      },
    ],
  });

  console.log(response.choices[0].message.content);
}

main();
```

### REST

```
bash -c '
  base64_audio=$(base64 -i "/path/to/your/audio/file.wav");
  curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer GEMINI_API_KEY" \
    -d "{
      \"model\": \"gemini-3-flash-preview\",
      \"messages\": [
        {
          \"role\": \"user\",
          \"content\": [
            { \"type\": \"text\", \"text\": \"Transcribe this audio file.\" },
            {
              \"type\": \"input_audio\",
              \"input_audio\": {
                \"data\": \"${base64_audio}\",
                \"format\": \"wav\"
              }
            }
          ]
        }
      ]
    }"
'
```

## Uporządkowane dane wyjściowe

Modele Gemini mogą generować obiekty JSON w dowolnej [zdefiniowanej przez Ciebie strukturze](https://ai.google.dev/gemini-api/docs/zdefiniowanej przez Ciebie strukturze).

### Python

```
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

completion = client.beta.chat.completions.parse(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "John and Susan are going to an AI conference on Friday."},
    ],
    response_format=CalendarEvent,
)

print(completion.choices[0].message.parsed)
```

### JavaScript

```
import OpenAI from "openai";
import { zodResponseFormat } from "openai/helpers/zod";
import { z } from "zod";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai"
});

const CalendarEvent = z.object({
  name: z.string(),
  date: z.string(),
  participants: z.array(z.string()),
});

const completion = await openai.chat.completions.parse({
  model: "gemini-3-flash-preview",
  messages: [
    { role: "system", content: "Extract the event information." },
    { role: "user", content: "John and Susan are going to an AI conference on Friday" },
  ],
  response_format: zodResponseFormat(CalendarEvent, "event"),
});

const event = completion.choices[0].message.parsed;
console.log(event);
```

## Wektory dystrybucyjne

Wektory dystrybucyjne tekstu mierzą podobieństwo ciągów tekstowych i można je generować za pomocą [interfejsu Gemini API](https://ai.google.dev/gemini-api/docs/interfejsu Gemini API). Możesz używać `gemini-embedding-2-preview` w przypadku multimodalnych wektorów dystrybucyjnych lub `gemini-embedding-001` w przypadku wektorów dystrybucyjnych tylko z tekstem.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.embeddings.create(
    input="Your text string goes here",
    model="gemini-embedding-2-preview"
)

print(response.data[0].embedding)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
  const embedding = await openai.embeddings.create({
    model: "gemini-embedding-2-preview",
    input: "Your text string goes here",
  });

  console.log(embedding);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/embeddings" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer GEMINI_API_KEY" \
-d '{
    "input": "Your text string goes here",
    "model": "gemini-embedding-2-preview"
  }'
```

## Batch API

Za pomocą biblioteki OpenAI możesz tworzyć [zadania wsadowe](https://ai.google.dev/gemini-api/docs/zadania wsadowe), przesyłać je i sprawdzać ich stan.

Musisz przygotować plik JSONL w formacie wejściowym OpenAI. Na przykład:

```
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3-flash-preview", "messages": [{"role": "user", "content": "Tell me a one-sentence joke."}]}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3-flash-preview", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}}
```

Zgodność z OpenAI w przypadku Batch umożliwia tworzenie zadań wsadowych, monitorowanie stanu zadań i wyświetlanie wyników zadań wsadowych.

Zgodność przesyłania i pobierania nie jest obecnie obsługiwana. Zamiast tego w poniższym przykładzie używamy klienta `genai` do przesyłania i pobierania [plików](https://ai.google.dev/gemini-api/docs/plików), tak samo jak w przypadku korzystania z interfejsu Gemini [Batch API](https://ai.google.dev/gemini-api/docs/Batch API).

### Python

```
from openai import OpenAI

# Regular genai client for uploads & downloads
from google import genai
client = genai.Client()

openai_client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Upload the JSONL file in OpenAI input format, using regular genai SDK
uploaded_file = client.files.upload(
    file='my-batch-requests.jsonl',
    config=types.UploadFileConfig(display_name='my-batch-requests', mime_type='jsonl')
)

# Create batch
batch = openai_client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/chat/completions",
    completion_window="24h"
)

# Wait for batch to finish (up to 24h)
while True:
    batch = client.batches.retrieve(batch.id)
    if batch.status in ('completed', 'failed', 'cancelled', 'expired'):
        break
    print(f"Batch not finished. Current state: {batch.status}. Waiting 30 seconds...")
    time.sleep(30)
print(f"Batch finished: {batch}")

# Download results in OpenAI output format, using regular genai SDK
file_content = genai_client.files.download(file=batch.output_file_id).decode('utf-8')

# See batch_output JSONL in OpenAI output format
for line in file_content.splitlines():
    print(line)
```

Pakiet OpenAI SDK obsługuje też [generowanie wektorów za pomocą interfejsu Batch API](https://ai.google.dev/gemini-api/docs/generowanie wektorów za pomocą interfejsu Batch API). Aby to zrobić, zamień pole `endpoint` metody `create` na punkt końcowy osadzania, a także klucze `url` i `model` w pliku JSONL:

```
# JSONL file using embeddings model and endpoint
# {"custom_id": "request-1", "method": "POST", "url": "/v1/embeddings", "body": {"model": "ggemini-embedding-001", "messages": [{"role": "user", "content": "Tell me a one-sentence joke."}]}}
# {"custom_id": "request-2", "method": "POST", "url": "/v1/embeddings", "body": {"model": "gemini-embedding-001", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}}

# ...

# Create batch step with embeddings endpoint
batch = openai_client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/embeddings",
    completion_window="24h"
)
```

Pełny przykład znajdziesz w sekcji [Generowanie osadzania wsadowego](https://ai.google.dev/gemini-api/docs/Generowanie osadzania wsadowego) w przewodniku zgodności z OpenAI.

## Wnioskowanie Flex i Priority

Interfejs Gemini API jest zgodny z parametrem `service_tier` OpenAI pod względem nazwy i logiki. Wymusza limity i kieruje ruch w sposób kontrolowany w przypadku obu poziomów wnioskowania: Flex i Priority.

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

completion = client.chat.completions.create(
  model="gemini-3-flash-preview",
  messages=[
    {"role": "user", "content": "Write a short poem about clouds."}
  ],
  service_tier="priority" # Or service_tier="flex"
)

print(completion)
```

Jeśli nie zostanie przypisana jawnie, domyślna wartość `service_tier` to `standard`, co w przypadku OpenAI jest równoważne `default`.
Więcej informacji o poziomach wnioskowania znajdziesz w dokumentacji [Optymalizacja](https://ai.google.dev/gemini-api/docs/Optymalizacja).

## Włączanie funkcji Gemini za pomocą `extra_body`

Gemini obsługuje kilka funkcji, które nie są dostępne w modelach OpenAI, ale można je włączyć za pomocą pola `extra_body`.

| Parametr | Typ | Punkt końcowy | Opis |
| --- | --- | --- | --- |
| **`cached_content`** | Tekst | Czat | Odpowiada ogólnej pamięci podręcznej treści Gemini. |
| **`thinking_config`** | Obiekt | Czat | Odpowiada konfiguracji ThinkingConfig Gemini. |
| **`aspect_ratio`** | Tekst | Obrazy | Format obrazu wyjściowego (np. `"16:9"`, `"1:1"`, `"9:16"`). |
| **`generation_config`** | Obiekt | Obrazy | Obiekt konfiguracji generowania Gemini (np. `{"responseModalities": ["IMAGE"], "candidateCount": 2}`). |
| **`safety_settings`** | Lista | Obrazy | niestandardowe filtry progów bezpieczeństwa (np. `[{"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"}]`); |
| **`tools`** | Lista | Obrazy | Umożliwia umocowanie (np. `[{"google_search": {}}]`). Tylko w przypadku `gemini-3-pro-image-preview`. |
| **`aspect_ratio`** | Tekst | Wideo | Wymiary filmu wyjściowego (`16:9` w przypadku orientacji poziomej, `9:16` w przypadku orientacji pionowej). Jeśli nie zostanie podany, mapuje z `size`. |
| **`resolution`** | Tekst | Wideo | Rozdzielczość wyjściowa (`720p`, `1080p`, `4K`). Uwaga: `1080p` i `4K` uruchamiają potok upsamplera. |
| **`duration_seconds`** | Liczba całkowita | Wideo | Długość generowania (wartości: `4`, `6`, `8`). W przypadku korzystania z `reference_images`, interpolacji lub rozszerzenia musi mieć wartość `8`. |
| **`frame_rate`** | Tekst | Wideo | Liczba klatek na sekundę w przypadku wyjścia wideo (np. `"24"`). |
| **`input_reference`** | Tekst | Wideo | Dane wejściowe do generowania filmów. |
| **`extend_video_id`** | Tekst | Wideo | Identyfikator istniejącego filmu, który ma zostać rozszerzony. |
| **`negative_prompt`** | Tekst | Wideo | Elementy do wykluczenia (np. `"shaky camera"`). |
| **`seed`** | Liczba całkowita | Wideo | Liczba całkowita do deterministycznego generowania. |
| **`style`** | Tekst | Wideo | Styl wizualny (`cinematic` domyślny, `creative` zoptymalizowany pod kątem mediów społecznościowych). |
| **`person_generation`** | Tekst | Wideo | Kontroluje generowanie osób (`allow_adult`, `allow_all`, `dont_allow`). |
| **`reference_images`** | Lista | Wideo | Maksymalnie 3 obrazy jako odniesienie do stylu lub charakteru (komponenty w formacie base64). |
| **`image`** | Tekst | Wideo | Początkowy obraz wejściowy zakodowany w formacie Base64, który służy do warunkowania generowania filmu. |
| **`last_frame`** | Obiekt | Wideo | Obraz końcowy do interpolacji (wymaga `image` jako pierwszej klatki). |

### Przykład użycia `extra_body`

Oto przykład użycia właściwości `extra_body` do ustawienia właściwości `cached_content`:

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key=MY_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

stream = client.chat.completions.create(
    model="gemini-3-flash-preview",
    n=1,
    messages=[
        {
            "role": "user",
            "content": "Summarize the video"
        }
    ],
    stream=True,
    stream_options={'include_usage': True},
    extra_body={
        'extra_body':
        {
            'google': {
              'cached_content': "cachedContents/0000aaaa1111bbbb2222cccc3333dddd4444eeee"
          }
        }
    }
)

for chunk in stream:
    print(chunk)
    print(chunk.usage.to_dict())
```

## Wyświetlenie listy modeli

Aby uzyskać listę dostępnych modeli Gemini:

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

models = client.models.list()
for model in models:
  print(model.id)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

async function main() {
  const list = await openai.models.list();

  for await (const model of list) {
    console.log(model);
  }
}
main();
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/openai/models \
-H "Authorization: Bearer GEMINI_API_KEY"
```

## Pobieranie modelu

Pobierz model Gemini:

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = client.models.retrieve("gemini-3-flash-preview")
print(model.id)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

async function main() {
  const model = await openai.models.retrieve("gemini-3-flash-preview");
  console.log(model.id);
}

main();
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/openai/models/gemini-3-flash-preview \
-H "Authorization: Bearer GEMINI_API_KEY"
```

## Obecne ograniczenia

Obsługa bibliotek OpenAI jest nadal w wersji beta, ponieważ rozszerzamy obsługę funkcji.

Jeśli masz pytania dotyczące obsługiwanych parametrów, nadchodzących funkcji lub napotkasz problemy z rozpoczęciem korzystania z Gemini, dołącz do naszego [forum dla programistów](https://ai.google.dev/gemini-api/docs/forum dla programistów).

## Co dalej?

Aby zapoznać się ze szczegółowymi przykładami, wypróbuj nasz [notatnik Colab dotyczący zgodności z OpenAI](https://ai.google.dev/gemini-api/docs/notatnik Colab dotyczący zgodności z OpenAI).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://ai.google.dev/gemini-api/docs/licencją Creative Commons – uznanie autorstwa 4.0), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://ai.google.dev/gemini-api/docs/licencji Apache 2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://ai.google.dev/gemini-api/docs/zasady dotyczące witryny Google Developers). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-04-29 UTC.

Chcesz przekazać coś jeszcze?
