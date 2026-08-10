---
source_url: https://ai.google.dev/gemini-api/docs/get-started?hl=de
fetched_at: 2026-08-10T03:22:05.431440+00:00
title: "Erste Schritte \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Erste Schritte

In diesem Leitfaden erfahren Sie, wie Sie mit der Gemini API und der [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) beginnen. Sie führen Ihren ersten API-Aufruf in weniger als einer Minute aus und lernen die Textgenerierung, das multimodale Verständnis, die Bildgenerierung, die strukturierte Ausgabe, Tools, Funktionsaufrufe, Agents und die Hintergrundausführung kennen.

Die Interactions API ist über die [Python](https://github.com/googleapis/python-genai)- und [JavaScript](https://github.com/googleapis/js-genai)-SDKs sowie über REST verfügbar.

## 1. API-Schlüssel anfordern

Wenn Sie die Gemini API verwenden möchten, benötigen Sie einen API-Schlüssel, um Ihre Anfragen zu authentifizieren, Sicherheitslimits durchzusetzen und die Nutzung Ihres Kontos zu verfolgen.

- In Google AI Studio werden für neue Nutzer automatisch ein Projekt und ein API-Schlüssel erstellt.
  Sie können ihn auf der Seite [API-Schlüssel](https://aistudio.google.com/api-keys?hl=de) kopieren.
- Wenn Sie einen neuen Schlüssel benötigen, klicken Sie in AI Studio auf **API-Schlüssel erstellen** und folgen Sie dem Dialogfeld, um ein neues Schlüssel-Projekt-Paar hinzuzufügen.

[Gemini API-Schlüssel erstellen](https://aistudio.google.com/apikey?hl=de)

Legen Sie Ihren Schlüssel als Umgebungsvariable fest:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### Upgrade auf die kostenpflichtige Stufe durchführen

Wenn Sie auf die kostenpflichtige Stufe upgraden, werden Ihre Ratenbegrenzungen erhöht. Außerdem müssen Sie Cloud Billing einrichten.

- Klicken Sie auf den Seiten [API-Schlüssel](https://aistudio.google.com/api-keys?hl=de) oder [Projekte](https://aistudio.google.com/projects?hl=de) von AI Studio auf **Abrechnung einrichten**.
- Folgen Sie dem Cloud-Abrechnungsdialogfeld, um ein Rechnungskonto zu erstellen oder zu verknüpfen, eine Zahlungsmethode hinzuzufügen und mindestens 10 $ (oder den entsprechenden Betrag in Ihrer Landeswährung) als Prepaid-Guthaben hinzuzufügen.
- Ihre API-Nutzung können Sie in [Google AI Studio](https://aistudio.google.com/usage?hl=de) unter **Dashboard** > **Nutzung** einsehen.

Weitere Informationen finden Sie auf der [Abrechnungsseite](https://ai.google.dev/gemini-api/docs/billing?hl=de).

## 2. SDK installieren und ersten Aufruf ausführen

Installieren Sie das SDK und generieren Sie Text mit einem einzigen API-Aufruf.

### Python

Installieren Sie das SDK:

```
pip install -U google-genai
```

Client initialisieren und Anfrage stellen:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

Installieren Sie das SDK:

```
npm install @google/genai
```

Client initialisieren und Anfrage stellen:

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works in a few words"
  }'
```

**Antwort**

```
{
  "id": "v1_ChdpQUFvYXI...",
  "status": "completed",
  "usage": {
    "total_tokens": 197,
    "total_input_tokens": 8,
    "total_output_tokens": 12
  },
  "created": "2026-06-09T12:01:25Z",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4FAQw..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "AI learns patterns from data, then uses those patterns to make predictions or decisions on new data."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

Bei Verwendung von REST gibt die API die vollständige `Interaction`-Ressource mit Metadaten, Nutzungsstatistiken und dem detaillierten Verlauf des Zuges zurück.

Die SDKs machen zwar die vollständige Antwort verfügbar, bieten aber auch praktische Eigenschaften wie `interaction.output_text` und `interaction.output_image`, um direkt auf die endgültigen Ausgaben zuzugreifen. Weitere Informationen zur Antwortstruktur finden Sie in der [Übersicht über Interaktionen](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de). Details zu Systemanweisungen und der Generierungskonfiguration finden Sie im [Leitfaden zur Textgenerierung](https://ai.google.dev/gemini-api/docs/text-generation?hl=de).

## 3. Antwort streamen

Um die Interaktion flüssiger zu gestalten, können Sie die Antwort streamen, während sie generiert wird. Bei jedem `step.delta`-Ereignis wird ein Textblock geliefert, den Sie sofort anzeigen können.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works",
    stream=True
)
for event in stream:
    print(event)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const stream = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "Explain how AI works",
  stream: true,
});

for await (const event of stream) {
  console.log(event);
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works",
    "stream": true
  }'
```

Beim Streaming antwortet der Server mit einem Stream von Server-Sent Events (SSE). Jedes Ereignis enthält einen Typ und JSON-Daten.

**Antwort**

```
event: interaction.created
data: {"interaction":{"id":"v1_Chd...","status":"in_progress","model":"gemini-3.6-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EvEFCu4F...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":"AI ","type":"text"},"event_type":"step.delta"}

event: step.delta
data: {"index":1,"delta":{"text":"works ","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_Chd...","status":"completed","usage":{"total_tokens":197}},"event_type":"interaction.completed"}
```

Eine detaillierte Beschreibung der Verarbeitung von Streaming-Ereignissen und ‑Deltatypen finden Sie in der [Anleitung zu Streaming-Interaktionen](https://ai.google.dev/gemini-api/docs/streaming?hl=de).

## 4. Unterhaltungen über mehrere Themen

Die Interactions API unterstützt Mehrfachdialog-Unterhaltungen mit zwei Ansätzen:

- **Zustandsbehaftet (empfohlen)**: Setzen Sie eine Unterhaltung auf dem Server mit `previous_interaction_id` fort. Ideal für die meisten Chat- und Agentic-Workflows, bei denen der Server den Verlauf verwalten und das Caching optimieren soll.
- **Zustandslos**: Verwalten Sie den Unterhaltungsverlauf auf dem Client, indem Sie alle vorherigen Turns (einschließlich der Zwischenschritte für das Modell und das Tool) in jeder Anfrage übergeben.

### Zustandsbehaftet (empfohlen)

Ketten Sie Interaktionen, indem Sie `previous_interaction_id` übergeben. Der Server verwaltet den gesamten Unterhaltungsverlauf für Sie.

### Python

```
from google import genai

client = genai.Client()

# Server-side state (recommended)
interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    input="I have 2 dogs in my house.",
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Server-side state (recommended)
const interaction1 = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "I have 2 dogs in my house.",
});
console.log("Response 1:", interaction1.output_text);

const interaction2 = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "How many paws are in my house?",
  previous_interaction_id: interaction1.id,
});
console.log("Response 2:", interaction2.output_text);
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
echo "Interaction 1 ID: $INTERACTION_ID"

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

### Zustandslos

`store=false` festlegen und den Unterhaltungsverlauf clientseitig verwalten. Sie müssen alle vom Modell generierten Schritte (einschließlich `thought`- und `function_call`-Schritte) genau so beibehalten und noch einmal senden, wie Sie sie erhalten haben.

### Python

```
from google import genai

client = genai.Client()

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "I have 2 dogs in my house."}]
    }
]

interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    store=False,
    input=history
)
print("Response 1:", interaction1.steps[-1].content[0].text)

for step in interaction1.steps:
    history.append(step.model_dump())

history.append({
    "type": "user_input",
    "content": [{"type": "text", "text": "How many paws are in my house?"}]
})

interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
    store=False,
    input=history
)
print("Response 2:", interaction2.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "I have 2 dogs in my house." }]
  }
];

const interaction1 = await ai.interactions.create({
  model: "gemini-3.6-flash",
  store: false,
  input: history
});
console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

history.push(...interaction1.steps);

history.push({
  type: "user_input",
  content: [{ type: "text", text: "How many paws are in my house?" }]
});

const interaction2 = await ai.interactions.create({
  model: "gemini-3.6-flash",
  store: false,
  input: history
});
console.log("Response 2:", interaction2.steps.at(-1).content[0].text);
```

### REST

```
# Turn 1: Send with store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "I have 2 dogs in my house."
      }
    ]
  }')

MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Turn 2: Build full history
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "I have 2 dogs in my house."}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --argjson second_input '[{"type": "user_input", "content": "How many paws are in my house?"}]' \
  '$first_input + $model_steps + $second_input')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.6-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

**Antwort**

```
{
  "id": "v2_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 240,
    "total_input_tokens": 60,
    "total_output_tokens": 20
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "There are 8 paws in your house. 2 dogs \u00d7 4 paws = 8 paws."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash"
}
```

Bei der zweiten Interaktion wird ein vollständiges Antwortobjekt zurückgegeben, das nur die neuen Schritte enthält, aber auf dem Kontext des vorherigen Turns basiert. Weitere Informationen zum Beibehalten des Status finden Sie im [Leitfaden für Mehrfachdialoge](https://ai.google.dev/gemini-api/docs/text-generation?hl=de#multi-turn-conversations). Informationen zur clientseitigen Verlaufsverwaltung finden Sie unter [Zustandsloser Modus](https://ai.google.dev/gemini-api/docs/text-generation?hl=de#stateless-conversations).

## 5. Multimodales Verstehen

Gemini-Modelle können Bilder, Audio, Video und Dokumente nativ verstehen. Media zusammen mit Text in einer einzigen Anfrage übergeben.

### Python

```
import base64
from google import genai

client = genai.Client()

# Load a local image
with open("sample.jpg", "rb") as f:
    image_bytes = f.read()
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Compare this local image and this remote audio file."},
        {
            "type": "image",
            "data": image_b64,
            "mime_type": "image/jpeg"
        },
        {
            "type": "audio",
            "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
            "mime_type": "audio/mp3"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import fs from "fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Load a local image
const imageBytes = fs.readFileSync("sample.jpg");
const imageB64 = imageBytes.toString("base64");

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: [
    { type: "text", text: "Compare this local image and this remote audio file." },
    {
      type: "image",
      data: imageB64,
      mime_type: "image/jpeg"
    },
    {
      type: "audio",
      uri: "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
      mime_type: "audio/mp3"
    }
  ],
});
console.log(interaction.output_text);
```

### REST

```
# Base64-encode local image
BASE64_IMAGE=$(base64 -w 0 sample.jpg)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions"   -H "x-goog-api-key: $GEMINI_API_KEY"   -H 'Content-Type: application/json'   -H "Api-Revision: 2026-05-20"   -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {
        "type": "text",
        "text": "Compare this local image and this remote audio file."
      },
      {
        "type": "image",
        "data": "'$BASE64_IMAGE'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "audio",
        "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

**Antwort**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 300
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The local image displays a pipe organ while the remote audio file is a sample MP3 clip..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

Informationen zum Übergeben von Bildern, Videos und Audiodateien finden Sie im [Leitfaden zum Bildverständnis](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de).

[hearing

Verständnis von Audioinhalten

Audioinhalte transkribieren, zusammenfassen oder Fragen dazu beantworten lassen](https://ai.google.dev/gemini-api/docs/audio?hl=de)
[videocam

Videos verstehen

Videoinhalte analysieren, Ereignisse lokalisieren und Aktionen beschreiben](https://ai.google.dev/gemini-api/docs/video-understanding?hl=de)
[description

Dokumentverarbeitung

Informationen aus PDFs und anderen Dokumentformaten extrahieren](https://ai.google.dev/gemini-api/docs/document-processing?hl=de)

## 6. Multimodale Generierung

Gemini kann Bilder nativ mit den Bildmodellen [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=de) generieren.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-image",
    input="Generate an image of a futuristic city skyline at sunset",
)

with open("generated_image.png", "wb") as f:
    f.write(base64.b64decode(interaction.output_image.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.1-flash-image",
  input: "Generate an image of a futuristic city skyline at sunset",
});

const generatedImage = interaction.output_image;
if (generatedImage) {
  const buffer = Buffer.from(generatedImage.data, "base64");
  fs.writeFileSync("generated_image.png", buffer);
}
```

### REST

```
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-flash-image",
    "input": [
      {"type": "text", "text": "Generate an image of a futuristic city skyline at sunset"}
    ]
  }'
```

**Antwort**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "image",
          "data": "BASE64_ENCODED_IMAGE",
          "mime_type": "image/png"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.1-flash-image",
}
```

Wenn das Modell ein Bild generiert, gibt es die base64-codierten Bilddaten in einem Schritt im `steps`-Array sowie über die Convenience-Property `output_image` zurück. Im [Leitfaden zur Bildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de) finden Sie Informationen zu Seitenverhältnissen, Bildbearbeitung und Referenzen.

[record\_voice\_over

Sprachgenerierung

Mit Gemini 3.1 Flash TTS ausdrucksstarke Sprache mit mehreren Sprechern generieren](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de)
[music\_note

Musikgenerierung

Mit Lyria 3 lassen sich Clips und vollständige Songs erstellen.](https://ai.google.dev/gemini-api/docs/music-generation?hl=de)

## 7. Strukturierte Ausgabe verwenden

Konfigurieren Sie das Modell so, dass es JSON zurückgibt, das einem von Ihnen definierten Schema entspricht. Die strukturierte Ausgabe funktioniert mit [Pydantic](https://docs.pydantic.dev/latest/) (Python) und [Zod](https://zod.dev/) (JavaScript).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional

class Recipe(BaseModel):
    recipe_name: str = Field(description="Name of the recipe.")
    ingredients: List[str] = Field(description="List of ingredients.")
    prep_time_minutes: Optional[int] = Field(description="Prep time in minutes.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Give me a recipe for banana bread",
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema()
    },
)

recipe = Recipe.model_validate_json(interaction.output_text)
print(recipe)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const ai = new GoogleGenAI({});

const recipeJsonSchema = {
  type: "object",
  properties: {
    recipe_name: { type: "string", description: "Name of the recipe." },
    ingredients: {
      type: "array",
      items: { type: "string" },
      description: "List of ingredients."
    },
    prep_time_minutes: {
      type: "integer",
      description: "Prep time in minutes."
    }
  },
  required: ["recipe_name", "ingredients"]
};

const recipeSchema = z.fromJSONSchema(recipeJsonSchema);

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "Give me a recipe for banana bread",
  response_format: {
    type: "text",
    mime_type: "application/json",
    schema: recipeJsonSchema
  },
});

const recipe = recipeSchema.parse(JSON.parse(interaction.output_text));
console.log(recipe);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Give me a recipe for banana bread",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "recipe_name": { "type": "string", "description": "Name of the recipe." },
          "ingredients": {
            "type": "array",
            "items": { "type": "string" },
            "description": "List of ingredients."
          },
          "prep_time_minutes": {
            "type": "integer",
            "description": "Prep time in minutes."
          }
        },
        "required": ["recipe_name", "ingredients"]
      }
    }
  }'
```

**Antwort**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"recipe_name\": \"Classic Banana Bread\",\n  \"ingredients\": [\n    \"3 ripe bananas, mashed\",\n    \"1/3 cup melted butter\",\n    \"3/4 cup sugar\",\n    \"1 egg, beaten\",\n    \"1 teaspoon vanilla extract\",\n    \"1 teaspoon baking soda\",\n    \"Pinch of salt\",\n    \"1.5 cups all-purpose flour\"\n  ],\n  \"prep_time_minutes\": 15\n}"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

Der Ausgabetextblock enthält einen gültigen JSON-String, der genau dem angeforderten Schema entspricht. Informationen zum Definieren komplexerer Strukturen und rekursiver Schemas finden Sie im [Leitfaden zur strukturierten Ausgabe](https://ai.google.dev/gemini-api/docs/structured-output?hl=de).

## 8. Tools verwenden

Die Antwort des Modells mit Echtzeitinformationen aus der Google Suche fundieren. Die API sucht automatisch, verarbeitet Ergebnisse und gibt Zitationen zurück.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)

# Print citations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text" and content_block.annotations:
                print("\nCitations:")
                for annotation in content_block.annotations:
                    if annotation.type == "url_citation":
                        print(f"  [{annotation.title}]({annotation.url})")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "Who won the euro 2024?",
  tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);

// Print citations
for (const step of interaction.steps) {
  if (step.type === "model_output") {
    for (const contentBlock of step.content) {
      if (contentBlock.type === "text" && contentBlock.annotations) {
        console.log("\nCitations:");
        for (const annotation of contentBlock.annotations) {
          if (annotation.type === "url_citation") {
            console.log(`  [${annotation.title}](${annotation.url})`);
          }
        }
      }
    }
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

**Antwort**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4F..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024",
              "title": "uefa.com",
              "start_index": 0,
              "end_index": 56
            }
          ]
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

Die Suchschritte werden im Interaktionsverlauf detailliert beschrieben und die endgültige Ausgabe enthält Inline-Zitationen, die auf Webquellen verweisen.

Informationen zum Extrahieren von Suchzitaten finden Sie in der [Anleitung zur Fundierung mit der Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de). Informationen zum Kombinieren mehrerer Tools finden Sie in der [Anleitung zur Kombination von Tools](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de).

[code

Code-Ausführung

Python-Code in einer sicheren Sandbox-Borg-Umgebung ausführen](https://ai.google.dev/gemini-api/docs/code-execution?hl=de)
[link

URL-Kontext

Sie können öffentliche Web-URLs direkt übergeben, um Antworten auf Webseiteninhalten zu fundieren.](https://ai.google.dev/gemini-api/docs/url-context?hl=de)
[search

Dateisuche

Hochgeladene Dokumente und Mediendateien indexieren und durchsuchen](https://ai.google.dev/gemini-api/docs/file-search?hl=de)
[map

Google Maps

Antworten mit realen raumbezogenen Daten und Standortdaten fundieren.](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de)
[computer

Computernutzung

Browserautomatisierung und Bildschirminteraktion.](https://ai.google.dev/gemini-api/docs/computer-use?hl=de)

## 9. Eigene Funktionen aufrufen

Mit Funktionsaufrufen können Sie das Modell mit Ihrem Code verbinden. Sie deklarieren den Namen und die Parameter einer Funktion, das Modell entscheidet, wann sie aufgerufen wird, und gibt strukturierte Argumente zurück. Sie führen sie lokal aus und senden das Ergebnis zurück.

### Zustandsbehaftet (empfohlen)

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

user_input = "What is the temperature in London?"
previous_id = None

while True:
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=user_input,
        tools=[weather_tool],
        previous_interaction_id=previous_id,
    )

    function_results = []
    for step in interaction.steps:
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            function_results.append({
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            })

    if not function_results:
        break

    user_input = function_results
    previous_id = interaction.id

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

let input = "What is the temperature in London?";
let previousId = null;
let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input,
    tools: [weatherTool],
    previous_interaction_id: previousId,
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      functionResults.push({
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      });
    }
  }

  if (functionResults.length === 0) break;

  input = functionResults;
  previousId = interaction.id;
}

console.log(interaction.output_text);
```

### REST

```
# Turn 1: Send prompt with function declaration
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What is the temperature in London?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Turn 2: Send function result back
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "input": [{
      "type": "function_result",
      "name": "'$FC_NAME'",
      "call_id": "'$FC_ID'",
      "result": [{"type": "text", "text": "{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"}]
    }],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }'
```

### Zustandslos

Sie können Funktionsaufrufe auch im statuslosen Modus verwenden, indem Sie den Unterhaltungsverlauf clientseitig verwalten und `store=false` festlegen. Im zustandslosen Modus müssen Sie den vollständigen Verlauf der Unterhaltung im Feld `input` jeder nachfolgenden Anfrage übergeben. Dieser Verlauf muss Folgendes enthalten:

1. Der erste Schritt `user_input`.
2. Alle vom Modell generierten Schritte, die in Turn 1 zurückgegeben werden (einschließlich der Schritte `thought` und `function_call`), werden genau so zurückgegeben, wie sie empfangen wurden.
3. Der `function_result`-Schritt, der die Ausgabe Ihrer ausgeführten Funktion enthält.

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "What is the temperature in London?"}]
    }
]

while True:
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        store=False,
        input=history,
        tools=[weather_tool],
    )

    function_results = []
    for step in interaction.steps:
        history.append(step.model_dump())
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            fn_result = {
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            }
            function_results.append(fn_result)
            history.append(fn_result)

    if not function_results:
        break

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "What is the temperature in London?" }]
  }
];

let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    store: false,
    input: history,
    tools: [weatherTool],
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    history.push(step);
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      const fnResult = {
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      };
      functionResults.push(fnResult);
      history.push(fnResult);
    }
  }

  if (functionResults.length === 0) break;
}

console.log(interaction.output_text);
```

### REST

```
# Turn 1: Send request with tools and store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "What is the temperature in London?"
      }
    ],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

# Extract model steps (thought, function_call)
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Assume local execution returns:
RESULT="{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"

# Reconstruct history for Turn 2
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "What is the temperature in London?"}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --arg fc_name "$FC_NAME" \
  --arg fc_id "$FC_ID" \
  --arg result "$RESULT" \
  '$first_input + $model_steps + [{"type": "function_result", "name": $fc_name, "call_id": $fc_id, "result": [{"type": "text", "text": $result}]}]')

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.6-flash\",
    \"store\": false,
    \"input\": $HISTORY,
    \"tools\": [{
      \"type\": \"function\",
      \"name\": \"get_current_temperature\",
      \"description\": \"Gets the current temperature for a given location.\",
      \"parameters\": {
        \"type\": \"object\",
        \"properties\": {
          \"location\": {\"type\": \"string\", \"description\": \"The city name\"}
        },
        \"required\": [\"location\"]
      }
    }]
  }"
```

**Antwort**

In Runde 1 gibt das Modell eine Antwort mit dem Status `requires_action` und dem Schritt `function_call` zurück:

```
{
  "id": "v1_Chd...",
  "status": "requires_action",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash"
}
```

Nachdem Sie die Funktion lokal ausgeführt und das Ergebnis eingereicht haben (Turn 2), wird die endgültige abgeschlossene Interaktion zurückgegeben:

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The temperature in London is currently 22°C."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

Informationen zu erweiterten Funktionen wie parallele Funktionsaufrufe oder Modi für die Funktionsauswahl finden Sie im [Leitfaden für Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de).

## 10. Verwalteten Agent ausführen

Verwaltete Agents werden in einer Remote-Sandbox mit Zugriff auf Tools wie Codeausführung und Dateiverwaltung ausgeführt. Übergeben Sie ein `agent` anstelle eines `model` und legen Sie `environment="remote"` fest.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)
print(f"Environment: {interaction.environment_id}")
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  agent: "antigravity-preview-05-2026",
  input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
  environment: "remote",
});
console.log(`Environment: ${interaction.environment_id}`);
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    "environment": "remote"
  }'
```

Sie können auch [benutzerdefinierte Agents](https://ai.google.dev/gemini-api/docs/custom-agents?hl=de) mit eigenen Anweisungen, Skills und Datenquellen definieren und speichern.

[rocket\_launch

Kurzanleitung

Ersten Agent-Aufruf starten, Antworten streamen und benutzerdefinierten Agenten erstellen](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=de)
[smart\_toy

Antigravity-Agent

Funktionen, Tools, multimodale Eingabe und Preise für den Standard-Agenten.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=de)
[experiment

KI-Agenten in AI Studio

Visuelle Umgebung zum Erstellen von Agent-Prototypen ohne Code.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=de)

## 11. Aufgaben im Hintergrund ausführen

Legen Sie `background=True` fest, um lange Aufgaben asynchron auszuführen. Rufen Sie `interactions.get()` auf, um die Ergebnisse abzufragen. Weitere Informationen finden Sie im [Leitfaden zur Ausführung im Hintergrund](https://ai.google.dev/gemini-api/docs/background-execution?hl=de).

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    background=True,
)
print(f"Started background task: {interaction.id}")
print(f"Status: {interaction.status}")

# Poll for completion
while True:
    result = client.interactions.get(interaction.id)
    print(f"Status: {result.status}")
    if result.status == "completed":
        print(f"\nResult:\n{result.output_text}")
        break
    elif result.status == "failed":
        print(f"Failed: {result.error}")
        break
    time.sleep(5)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
  background: true,
});
console.log(`Started background task: ${interaction.id}`);
console.log(`Status: ${interaction.status}`);

// Poll for completion
while (true) {
  const result = await ai.interactions.get(interaction.id);
  console.log(`Status: ${result.status}`);
  if (result.status === "completed") {
    console.log(`\nResult:\n${result.output_text}`);
    break;
  } else if (result.status === "failed") {
    console.log(`Failed: ${result.error}`);
    break;
  }
  await new Promise(r => setTimeout(r, 5000));
}
```

### REST

```
# Start a background task
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    "background": true
  }')

INTERACTION_ID=$(echo "$RESPONSE" | jq -r '.id')
echo "Started background task: $INTERACTION_ID"

# Poll for completion
while true; do
  RESULT=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20")
  STATUS=$(echo "$RESULT" | jq -r '.status')
  echo "Status: $STATUS"
  if [ "$STATUS" = "completed" ]; then
    echo "$RESULT" | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="text") | .text'
    break
  elif [ "$STATUS" = "failed" ]; then
    echo "Failed"
    break
  fi
  sleep 5
done
```

**Antwort**

Die erste Antwort wird sofort mit dem Status `in_progress` zurückgegeben:

```
{
  "id": "v1_abc123",
  "status": "in_progress",
  "object": "interaction",
  "model": "gemini-3.6-flash"
}
```

Nachdem die Hintergrundaufgabe vollständig ausgeführt wurde, wird beim Prüfen des Interaktionsstatus Folgendes zurückgegeben:

```
{
  "id": "v1_abc123",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Artificial intelligence has transformed modern healthcare in several..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

Informationen zum asynchronen Ausführen von Modellen und Agents finden Sie im [Leitfaden zur Hintergrundausführung](https://ai.google.dev/gemini-api/docs/background-execution?hl=de).

## Nächste Schritte

- [Hintergrundausführung](https://ai.google.dev/gemini-api/docs/background-execution?hl=de): Führen Sie lang andauernde Aufgaben asynchron aus und verwalten Sie den Status.
- [Textgenerierung](https://ai.google.dev/gemini-api/docs/text-generation?hl=de): Systemanweisungen, Generierungskonfiguration und erweiterte Textmuster.
- [Bildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de): Seitenverhältnisse, Bildbearbeitung und Stilreferenzen.
- [Bildverständnis](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de): Klassifizierung, Objekterkennung und visuelle Fragen und Antworten.
- [Denken](https://ai.google.dev/gemini-api/docs/thinking?hl=de): Verwenden Sie die Chain-of-Thought-Methode für komplexe Aufgaben.
- [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de): Parallele, zusammengesetzte und eingeschränkte Funktionsmodi.
- [Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de): Fundierung, Zitationen und Suchvorschläge.
- [Verwaltete KI-Agenten](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=de): Vordefinierte Agents mit Code-Ausführung und Dateiverwaltung.
- [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de): Autonome mehrstufige Recherche mit Planung und Synthese.
- [Strukturierte Ausgabe](https://ai.google.dev/gemini-api/docs/structured-output?hl=de): JSON-Schemas, Enums und rekursive Typdefinitionen.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
