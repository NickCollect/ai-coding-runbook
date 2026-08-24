---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=pl
fetched_at: 2026-08-24T02:20:38.464935+00:00
title: "Generowanie tekstu \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Generowanie tekstu

Gemini API może generować dane wyjściowe w postaci tekstu na podstawie tekstu, obrazów, filmów i dźwięku.

Oto podstawowy przykład:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="How does AI work?"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "How does AI work?",
  });
  console.log(response.text);
}

await main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.6-flash",
      genai.Text("Explain how AI works in a few words"),
      nil,
  )

  fmt.Println(result.Text())
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateContentWithTextInput {
  public static void main(String[] args) {

    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent("gemini-3.6-flash", "How does AI work?", null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "How does AI work?"
          }
        ]
      }
    ]
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const payload = {
    contents: [
      {
        parts: [
          { text: 'How AI does work?' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

## Myślenie z Gemini

Modele Gemini mają często domyślnie włączoną funkcję [„myślenia”](https://ai.google.dev/gemini-api/docs/thinking?hl=pl)
, która umożliwia modelowi przeprowadzenie rozumowania przed udzieleniem odpowiedzi na żądanie.

Każdy model obsługuje różne konfiguracje myślenia, co daje Ci kontrolę nad kosztami, opóźnieniem i inteligencją. Więcej informacji znajdziesz w
[przewodniku po myśleniu](https://ai.google.dev/gemini-api/docs/thinking?hl=pl#set-budget).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="How does AI work?",
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
    model: "gemini-3.6-flash",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    }
  });
  console.log(response.text);
}

await main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.6-flash",
      genai.Text("How does AI work?"),
      &genai.GenerateContentConfig{
        ThinkingConfig: &genai.ThinkingConfig{
            ThinkingLevel: &thinkingLevelVal,
        },
      }
  )

  fmt.Println(result.Text())
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.ThinkingConfig;
import com.google.genai.types.ThinkingLevel;

public class GenerateContentWithThinkingConfig {
  public static void main(String[] args) {

    Client client = new Client();

    GenerateContentConfig config =
        GenerateContentConfig.builder()
            .thinkingConfig(ThinkingConfig.builder().thinkingLevel(new ThinkingLevel("low")))
            .build();

    GenerateContentResponse response =
        client.models.generateContent("gemini-3.6-flash", "How does AI work?", config);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "How does AI work?"
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

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const payload = {
    contents: [
      {
        parts: [
          { text: 'How AI does work?' },
        ],
      },
    ],
    generationConfig: {
      thinkingConfig: {
        thinkingLevel: 'low'
      }
    }
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

## Instrukcje systemowe i inne konfiguracje

Zachowanie modeli Gemini możesz określać za pomocą instrukcji systemowych. Aby to zrobić,
przekaż obiekt [`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=pl#v1beta.GenerationConfig).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a cat. Your name is Neko."),
    contents="Hello there"
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Hello there",
    config: {
      systemInstruction: "You are a cat. Your name is Neko.",
    },
  });
  console.log(response.text);
}

await main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  config := &genai.GenerateContentConfig{
      SystemInstruction: genai.NewContentFromText("You are a cat. Your name is Neko.", genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.6-flash",
      genai.Text("Hello there"),
      config,
  )

  fmt.Println(result.Text())
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;

public class GenerateContentWithSystemInstruction {
  public static void main(String[] args) {

    Client client = new Client();

    GenerateContentConfig config =
        GenerateContentConfig.builder()
            .systemInstruction(
                Content.fromParts(Part.fromText("You are a cat. Your name is Neko.")))
            .build();

    GenerateContentResponse response =
        client.models.generateContent("gemini-3.6-flash", "Hello there", config);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "system_instruction": {
      "parts": [
        {
          "text": "You are a cat. Your name is Neko."
        }
      ]
    },
    "contents": [
      {
        "parts": [
          {
            "text": "Hello there"
          }
        ]
      }
    ]
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const systemInstruction = {
    parts: [{
      text: 'You are a cat. Your name is Neko.'
    }]
  };

  const payload = {
    systemInstruction,
    contents: [
      {
        parts: [
          { text: 'Hello there' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

Obiekt [`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=pl#v1beta.GenerationConfig)
umożliwia też zastępowanie domyślnych parametrów generowania, takich jak
[`max_output_tokens`](https://ai.google.dev/api/generate-content?hl=pl#v1beta.GenerationConfig).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=["Explain how AI works"],
    config=types.GenerateContentConfig(
        max_output_tokens=1000
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works",
    config: {
      maxOutputTokens: 1000,
    },
  });
  console.log(response.text);
}

await main();
```

### Go

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

  config := &genai.GenerateContentConfig{
    MaxOutputTokens:   1000,
    ResponseMIMEType:  "application/json",
  }

  result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.6-flash",
    genai.Text("What is the average size of a swallow?"),
    config,
  )

  fmt.Println(result.Text())
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;

public class GenerateContentWithConfig {
  public static void main(String[] args) {

    Client client = new Client();

    GenerateContentConfig config = GenerateContentConfig.builder().maxOutputTokens(1000).build();

    GenerateContentResponse response =
        client.models.generateContent("gemini-3.6-flash", "Explain how AI works", config);

    System.out.println(response.text());
  }
}
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works"
          }
        ]
      }
    ],
    "generationConfig": {
      "stopSequences": [
        "Title"
      ],
      "maxOutputTokens": 1000
    }
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const generationConfig = {
    maxOutputTokens: 1000,
    responseFormat: { text: { mimeType: "text/plain" } },
  };

  const payload = {
    generationConfig,
    contents: [
      {
        parts: [
          { text: 'Explain how AI works in a few words' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

Pełną listę konfigurowalnych parametrów i ich
opisów znajdziesz w dokumentacji interfejsu API w sekcji [`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=pl#v1beta.GenerationConfig).

## Dane wejściowe multimodalne

Gemini API obsługuje dane wejściowe multimodalne, co umożliwia łączenie tekstu z plikami multimedialnymi. Poniższy przykład pokazuje, jak podać obraz:

### Python

```
from PIL import Image
from google import genai

client = genai.Client()

image = Image.open("/path/to/organ.png")
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[image, "Tell me about this instrument"]
)
print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const image = await ai.files.upload({
    file: "/path/to/organ.png",
  });
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: [
      createUserContent([
        "Tell me about this instrument",
        createPartFromUri(image.uri, image.mimeType),
      ]),
    ],
  });
  console.log(response.text);
}

await main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  imagePath := "/path/to/organ.jpg"
  imgData, _ := os.ReadFile(imagePath)

  parts := []*genai.Part{
      genai.NewPartFromText("Tell me about this instrument"),
      &genai.Part{
          InlineData: &genai.Blob{
              MIMEType: "image/jpeg",
              Data:     imgData,
          },
      },
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.6-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.Content;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;

public class GenerateContentWithMultiModalInputs {
  public static void main(String[] args) {

    Client client = new Client();

    Content content =
      Content.fromParts(
          Part.fromText("Tell me about this instrument"),
          Part.fromUri("/path/to/organ.jpg", "image/jpeg"));

    GenerateContentResponse response =
        client.models.generateContent("gemini-3.6-flash", content, null);

    System.out.println(response.text());
  }
}
```

### REST

```
# Use a temporary file to hold the base64 encoded image data
TEMP_B64=$(mktemp)
trap 'rm -f "$TEMP_B64"' EXIT
base64 $B64FLAGS $IMG_PATH > "$TEMP_B64"

# Use a temporary file to hold the JSON payload
TEMP_JSON=$(mktemp)
trap 'rm -f "$TEMP_JSON"' EXIT

cat > "$TEMP_JSON" << EOF
{
  "contents": [
    {
      "parts": [
        {
          "text": "Tell me about this instrument"
        },
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "$(cat "$TEMP_B64")"
          }
        }
      ]
    }
  ]
}
EOF

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d "@$TEMP_JSON"
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const imageUrl = 'https://example.com/image.jpg';
  const image = getImageData(imageUrl);
  const payload = {
    contents: [
      {
        parts: [
          { image },
          { text: 'Tell me about this instrument' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}

function getImageData(url) {
  const blob = UrlFetchApp.fetch(url).getBlob();

  return {
    mimeType: blob.getContentType(),
    data: Utilities.base64Encode(blob.getBytes())
  };
}
```

Alternatywne metody podawania obrazów i bardziej zaawansowane przetwarzanie obrazów, znajdziesz w naszym [przewodniku po rozpoznawaniu obrazów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl).
Interfejs API obsługuje też dane wejściowe i analizę [dokumentów](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl), [filmów](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pl) i [dźwięku](https://ai.google.dev/gemini-api/docs/audio?hl=pl).

## Strumieniowanie odpowiedzi

Domyślnie model zwraca odpowiedź dopiero po zakończeniu całego procesu generowania.

Aby uzyskać płynniejsze interakcje, użyj strumieniowania, aby otrzymywać [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=pl#v1beta.GenerateContentResponse) instancje przyrostowo
w miarę ich generowania.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content_stream(
    model="gemini-3.6-flash",
    contents=["Explain how AI works"]
)
for chunk in response:
    print(chunk.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works",
  });

  for await (const chunk of response) {
    console.log(chunk.text);
  }
}

await main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  stream := client.Models.GenerateContentStream(
      ctx,
      "gemini-3.6-flash",
      genai.Text("Write a story about a magic backpack."),
      nil,
  )

  for chunk, _ := range stream {
      part := chunk.Candidates[0].Content.Parts[0]
      fmt.Print(part.Text)
  }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.ResponseStream;
import com.google.genai.types.GenerateContentResponse;

public class GenerateContentStream {
  public static void main(String[] args) {

    Client client = new Client();

    ResponseStream<GenerateContentResponse> responseStream =
      client.models.generateContentStream(
          "gemini-3.6-flash", "Write a story about a magic backpack.", null);

    for (GenerateContentResponse res : responseStream) {
      System.out.print(res.text());
    }

    // To save resources and avoid connection leaks, it is recommended to close the response
    // stream after consumption (or using try block to get the response stream).
    responseStream.close();
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:streamGenerateContent?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works"
          }
        ]
      }
    ]
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const payload = {
    contents: [
      {
        parts: [
          { text: 'Explain how AI works' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:streamGenerateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

## Rozmowy wieloetapowe (czat)

Nasze pakiety SDK udostępniają funkcję zbierania wielu rund promptów i odpowiedzi w czacie, co ułatwia śledzenie historii rozmowy.

### Python

```
from google import genai

client = genai.Client()
chat = client.chats.create(model="gemini-3.6-flash")

response = chat.send_message("I have 2 dogs in my house.")
print(response.text)

response = chat.send_message("How many paws are in my house?")
print(response.text)

for message in chat.get_history():
    print(f'role - {message.role}',end=": ")
    print(message.parts[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const chat = ai.chats.create({
    model: "gemini-3.6-flash",
    history: [
      {
        role: "user",
        parts: [{ text: "Hello" }],
      },
      {
        role: "model",
        parts: [{ text: "Great to meet you. What would you like to know?" }],
      },
    ],
  });

  const response1 = await chat.sendMessage({
    message: "I have 2 dogs in my house.",
  });
  console.log("Chat response 1:", response1.text);

  const response2 = await chat.sendMessage({
    message: "How many paws are in my house?",
  });
  console.log("Chat response 2:", response2.text);
}

await main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  history := []*genai.Content{
      genai.NewContentFromText("Hi nice to meet you! I have 2 dogs in my house.", genai.RoleUser),
      genai.NewContentFromText("Great to meet you. What would you like to know?", genai.RoleModel),
  }

  chat, _ := client.Chats.Create(ctx, "gemini-3.6-flash", nil, history)
  res, _ := chat.SendMessage(ctx, genai.Part{Text: "How many paws are in my house?"})

  if len(res.Candidates) > 0 {
      fmt.Println(res.Candidates[0].Content.Parts[0].Text)
  }
}
```

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentResponse;

public class MultiTurnConversation {
  public static void main(String[] args) {

    Client client = new Client();
    Chat chatSession = client.chats.create("gemini-3.6-flash");

    GenerateContentResponse response =
        chatSession.sendMessage("I have 2 dogs in my house.");
    System.out.println("First response: " + response.text());

    response = chatSession.sendMessage("How many paws are in my house?");
    System.out.println("Second response: " + response.text());

    // Get the history of the chat session.
    // Passing 'true' to getHistory() returns the curated history, which excludes
    // empty or invalid parts.
    // Passing 'false' here would return the comprehensive history, including
    // empty or invalid parts.
    ImmutableList<Content> history = chatSession.getHistory(true);
    System.out.println("History: " + history);
  }
}
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "Hello"
          }
        ]
      },
      {
        "role": "model",
        "parts": [
          {
            "text": "Great to meet you. What would you like to know?"
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "text": "I have two dogs in my house. How many paws are in my house?"
          }
        ]
      }
    ]
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const payload = {
    contents: [
      {
        role: 'user',
        parts: [
          { text: 'Hello' },
        ],
      },
      {
        role: 'model',
        parts: [
          { text: 'Great to meet you. What would you like to know?' },
        ],
      },
      {
        role: 'user',
        parts: [
          { text: 'I have two dogs in my house. How many paws are in my house?' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

Strumieniowanie można też stosować w przypadku rozmów wieloetapowych.

### Python

```
from google import genai

client = genai.Client()
chat = client.chats.create(model="gemini-3.6-flash")

response = chat.send_message_stream("I have 2 dogs in my house.")
for chunk in response:
    print(chunk.text, end="")

response = chat.send_message_stream("How many paws are in my house?")
for chunk in response:
    print(chunk.text, end="")

for message in chat.get_history():
    print(f'role - {message.role}', end=": ")
    print(message.parts[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const chat = ai.chats.create({
    model: "gemini-3.6-flash",
    history: [
      {
        role: "user",
        parts: [{ text: "Hello" }],
      },
      {
        role: "model",
        parts: [{ text: "Great to meet you. What would you like to know?" }],
      },
    ],
  });

  const stream1 = await chat.sendMessageStream({
    message: "I have 2 dogs in my house.",
  });
  for await (const chunk of stream1) {
    console.log(chunk.text);
    console.log("_".repeat(80));
  }

  const stream2 = await chat.sendMessageStream({
    message: "How many paws are in my house?",
  });
  for await (const chunk of stream2) {
    console.log(chunk.text);
    console.log("_".repeat(80));
  }
}

await main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  history := []*genai.Content{
      genai.NewContentFromText("Hi nice to meet you! I have 2 dogs in my house.", genai.RoleUser),
      genai.NewContentFromText("Great to meet you. What would you like to know?", genai.RoleModel),
  }

  chat, _ := client.Chats.Create(ctx, "gemini-3.6-flash", nil, history)
  stream := chat.SendMessageStream(ctx, genai.Part{Text: "How many paws are in my house?"})

  for chunk, _ := range stream {
      part := chunk.Candidates[0].Content.Parts[0]
      fmt.Print(part.Text)
  }
}
```

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.ResponseStream;
import com.google.genai.types.GenerateContentResponse;

public class MultiTurnConversationWithStreaming {
  public static void main(String[] args) {

    Client client = new Client();
    Chat chatSession = client.chats.create("gemini-3.6-flash");

    ResponseStream<GenerateContentResponse> responseStream =
        chatSession.sendMessageStream("I have 2 dogs in my house.", null);

    for (GenerateContentResponse response : responseStream) {
      System.out.print(response.text());
    }

    responseStream = chatSession.sendMessageStream("How many paws are in my house?", null);

    for (GenerateContentResponse response : responseStream) {
      System.out.print(response.text());
    }

    // Get the history of the chat session. History is added after the stream
    // is consumed and includes the aggregated response from the stream.
    System.out.println("History: " + chatSession.getHistory(false));
  }
}
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:streamGenerateContent?alt=sse \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "Hello"
          }
        ]
      },
      {
        "role": "model",
        "parts": [
          {
            "text": "Great to meet you. What would you like to know?"
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "text": "I have two dogs in my house. How many paws are in my house?"
          }
        ]
      }
    ]
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const payload = {
    contents: [
      {
        role: 'user',
        parts: [
          { text: 'Hello' },
        ],
      },
      {
        role: 'model',
        parts: [
          { text: 'Great to meet you. What would you like to know?' },
        ],
      },
      {
        role: 'user',
        parts: [
          { text: 'I have two dogs in my house. How many paws are in my house?' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:streamGenerateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

## Wskazówki dotyczące tworzenia promptów

Wskazówki dotyczące pełnego wykorzystania możliwości Gemini znajdziesz w [przewodniku po tworzeniu promptów](https://ai.google.dev/gemini/docs/prompting-strategies?hl=pl).

## Co dalej?

- Wypróbuj [Gemini w Google AI Studio](https://aistudio.google.com?hl=pl).
- Eksperymentuj z [uporządkowanymi danymi wyjściowymi](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl) w przypadku
  odpowiedzi w formacie JSON.
- Poznaj możliwości Gemini w zakresie analizy [obrazów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl),
  [filmów](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pl), [dźwięku](https://ai.google.dev/gemini-api/docs/audio?hl=pl)
  i [dokumentów](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl).
- Dowiedz się więcej o strategiach tworzenia promptów multimodalnych
  [plików](https://ai.google.dev/gemini-api/docs/files?hl=pl#prompt-guide).

## Generowanie treści

Jest to centralny punkt końcowy do wysyłania promptów do modelu. Istnieją 2 punkty końcowe do generowania treści, a główna różnica polega na sposobie otrzymywania odpowiedzi:

- **[`generateContent`](https://ai.google.dev/api/generate-content?hl=pl#method:-models.generatecontent)
  (REST)**: odbiera żądanie i po zakończeniu całego procesu generowania przez model wysyła pojedynczą odpowiedź.
- **[`streamGenerateContent`](https://ai.google.dev/api/generate-content?hl=pl#method:-models.streamgeneratecontent)
  (SSE)**: odbiera dokładnie to samo żądanie, ale model przesyła strumieniowo fragmenty odpowiedzi w miarę ich generowania. Zapewnia to lepsze wrażenia użytkownika w przypadku aplikacji interaktywnych, ponieważ umożliwia natychmiastowe wyświetlanie częściowych wyników.

### Struktura treści żądania

Treść [żądania](https://ai.google.dev/api/generate-content?hl=pl#request-body) to obiekt JSON, który jest
**identyczny** w przypadku trybu standardowego i strumieniowego. Składa się z kilku podstawowych
obiektów:

- [`Content`](https://ai.google.dev/api/caching?hl=pl#Content) obiekt: reprezentuje pojedynczą rundę
  rozmowy.
- [`Part`](https://ai.google.dev/api/caching?hl=pl#Part) obiekt: fragment danych w rundzie `Content`
  (np. tekst lub obraz).
- `inline_data` ([`Blob`](https://ai.google.dev/api/caching?hl=pl#Blob)): kontener na surowe bajty multimediów
  i ich typ MIME.

Na najwyższym poziomie treść żądania zawiera obiekt `contents`, który jest listą obiektów `Content`, z których każdy reprezentuje rundę rozmowy. W większości przypadków w przypadku podstawowego generowania tekstu będziesz mieć pojedynczy obiekt `Content`, ale jeśli chcesz zachować historię rozmowy, możesz użyć wielu obiektów `Content`.

Poniżej przedstawiono typową treść żądania `generateContent`:

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
          "role": "user",
          "parts": [
              // A list of Part objects goes here
          ]
      },
      {
          "role": "model",
          "parts": [
              // A list of Part objects goes here
          ]
      }
    ]
  }'
```

### Struktura treści odpowiedzi

Treść [odpowiedzi](https://ai.google.dev/api/generate-content?hl=pl#response-body) jest podobna w przypadku trybu strumieniowego i standardowego, z wyjątkiem tych różnic:

- Tryb standardowy: treść odpowiedzi zawiera instancję
  [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=pl#v1beta.GenerateContentResponse).
- Tryb strumieniowy: treść odpowiedzi zawiera strumień
  [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=pl#v1beta.GenerateContentResponse)
  instancji.

Na wysokim poziomie treść odpowiedzi zawiera obiekt `candidates`, który jest listą obiektów `Candidate`. Obiekt `Candidate` zawiera obiekt `Content`, który zawiera wygenerowaną odpowiedź zwróconą przez model.

## Przykłady interfejsu API REST

### Prompt multimodalny (tekst i obraz)

Aby w prompcie podać zarówno tekst, jak i obraz, tablica `parts` powinna zawierać 2 obiekty `Part`: jeden na tekst, a drugi na `inline_data` obrazu.

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
    "contents": [{
    "parts":[
        {
            "inline_data": {
            "mime_type":"image/jpeg",
            "data": "/9j/4AAQSkZJRgABAQ... (base64-encoded image)"
            }
        },
        {"text": "What is in this picture?"},
      ]
    }]
  }'
```

### Rozmowy wieloetapowe (czat)

Aby utworzyć rozmowę z wieloma rundami, zdefiniuj tablicę `contents` z wieloma obiektami `Content`. Interfejs API użyje całej tej historii jako kontekstu następnej odpowiedzi. `role` każdego obiektu `Content` powinna być na przemian `user` i `model`.

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          { "text": "Hello." }
        ]
      },
      {
        "role": "model",
        "parts": [
          { "text": "Hello! How can I help you today?" }
        ]
      },
      {
        "role": "user",
        "parts": [
          { "text": "Please write a four-line poem about the ocean." }
        ]
      }
    ]
  }'
```

### Najważniejsze punkty

- `Content` to obwiednia: jest to kontener najwyższego poziomu dla rundy wiadomości, niezależnie od tego, czy pochodzi ona od użytkownika czy od modelu.
- `Part` umożliwia multimodalność: użyj wielu obiektów `Part` w jednym obiekcie `Content`, aby połączyć różne typy danych (tekst, obraz, URI filmu itp.).
- Wybierz metodę danych:
  - W przypadku małych, bezpośrednio osadzonych multimediów (takich jak większość obrazów) użyj elementu `Part` z elementem `inline_data`.
  - W przypadku większych plików lub plików, których chcesz używać ponownie w różnych żądaniach, użyj interfejsu File API, aby przesłać plik i odwołać się do niego za pomocą części `file_data`.
- Zarządzaj historią rozmowy: w przypadku aplikacji czatu korzystających z interfejsu API REST utwórz
  tablicę `contents`, dodając obiekty `Content` dla każdej rundy,
  na przemian z rolami `"user"` i `"model"`. Jeśli używasz pakietu SDK, zapoznaj się z jego dokumentacją, aby dowiedzieć się, jak zarządzać historią rozmowy.

## Przykłady odpowiedzi

Z poniższych przykładów dowiesz się, jak te komponenty współpracują w przypadku różnych typów żądań.

### Odpowiedź zawierająca tylko tekst

Domyślna odpowiedź tekstowa składa się z tablicy `candidates` z co najmniej 1 obiektem `content`, który zawiera odpowiedź modelu.

Oto przykład **standardowej** odpowiedzi:

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "At its core, Artificial Intelligence works by learning from vast amounts of data ..."
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 1
    }
  ],
}
```

Poniżej znajduje się seria odpowiedzi **strumieniowych**. Każda odpowiedź zawiera `responseId`, który łączy całą odpowiedź:

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "The image displays"
          }
        ],
        "role": "model"
      },
      "index": 0
    }
  ],
  "usageMetadata": {
    "promptTokenCount": ...
  },
  "modelVersion": "gemini-3.6-flash",
  "responseId": "mAitaLmkHPPlz7IPvtfUqQ4"
}

...

{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": " the following materials:\n\n*   **Wood:** The accordion and the violin are primarily"
          }
        ],
        "role": "model"
      },
      "index": 0
    }
  ],
  "usageMetadata": {
    "promptTokenCount": ...
  }
  "modelVersion": "gemini-3.6-flash",
  "responseId": "mAitaLmkHPPlz7IPvtfUqQ4"
}
```

## Interfejs Live API (BidiGenerateContent) WebSockets API

Interfejs Live API udostępnia stanowy interfejs API oparty na WebSocket do strumieniowania dwukierunkowego, co umożliwia korzystanie z przypadków użycia strumieniowania w czasie rzeczywistym. Więcej informacji znajdziesz w
[przewodniku po interfejsie Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl) i w [dokumentacji interfejsu Live API](https://ai.google.dev/api/live?hl=pl).

## Modele specjalizowane

Oprócz rodziny modeli Gemini interfejs Gemini API udostępnia punkty końcowe dla
modeli specjalizowanych, takich jak [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=pl),
[Lyria](https://ai.google.dev/gemini-api/docs/music-generation?hl=pl) i
[modele wektorów dystrybucyjnych](https://ai.google.dev/gemini-api/docs/embeddings?hl=pl). Te przewodniki znajdziesz w sekcji Modele.

## Interfejsy API platformy

Pozostałe punkty końcowe umożliwiają korzystanie z dodatkowych funkcji z głównymi punktami końcowymi opisanymi do tej pory. Więcej informacji znajdziesz w sekcji Przewodniki w tematach
[Tryb wsadowy](https://ai.google.dev/gemini-api/docs/batch-mode?hl=pl) i
[File API](https://ai.google.dev/gemini-api/docs/files?hl=pl).

## Co dalej?

Jeśli dopiero zaczynasz, zapoznaj się z tymi przewodnikami, które pomogą Ci zrozumieć model programowania Gemini API:

- [Przewodnik Pierwsze kroki z Gemini API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Przewodnik po modelu Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl)

Możesz też zapoznać się z przewodnikami po funkcjach, które przedstawiają różne funkcje Gemini API i zawierają przykłady kodu:

- [Generowanie tekstu](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl)
- [Buforowanie kontekstu](https://ai.google.dev/gemini-api/docs/caching?hl=pl)
- [Wektory dystrybucyjne](https://ai.google.dev/gemini-api/docs/embeddings?hl=pl)

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
