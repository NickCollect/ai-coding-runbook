---
source_url: https://ai.google.dev/gemini-api/docs/text-generation?hl=de
fetched_at: 2026-07-20T04:45:45.652433+00:00
title: "Textgenerierung \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Textgenerierung

Die Gemini API kann Textausgabe aus Text-, Bild-, Video- und Audioeingaben generieren.

Hier ein einfaches Beispiel:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="How does AI work?"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "How does AI work?",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "How does AI work?"
  }'
```

Die Google GenAI SDKs bieten praktische Attribute direkt für das zurückgegebene `Interaction`-Objekt, um auf die Antwort des Modells zuzugreifen.

Die häufigste Hilfsfunktion ist **`interaction.output_text`** (String), die die letzten Textblöcke in der Antwort des Modells zurückgibt. Wenn die Antwort auf mehrere aufeinanderfolgende `TextContent`-Blöcke aufgeteilt ist, werden diese automatisch zusammengefügt.
`.output_text` umfasst keine früheren Textblöcke, die durch nicht textbezogene Inhalte (z. B. Gedanken, Bilder, Audio oder Tool-Aufrufe) getrennt sind. Bei komplexen oder verschachtelten multimodalen Antworten müssen Sie stattdessen manuell über `steps` iterieren. Weitere Informationen zu anderen Media-Convenience-Properties finden Sie in der [Übersicht zu Interaktionen](https://ai.google.dev/gemini-api/docs/interactions?hl=de#convenience-properties).

## Mit Gemini Ideen entwickeln

Bei Gemini-Modellen ist [„Denken“](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=de) oft standardmäßig aktiviert. Dadurch kann das Modell Schlussfolgerungen ziehen, bevor es auf eine Anfrage antwortet.

Jedes Modell unterstützt unterschiedliche Denkkonfigurationen, sodass Sie Kosten, Latenz und Intelligenz steuern können. Weitere Informationen finden Sie im [Leitfaden zum Denken](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=de#set-budget).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="How does AI work?",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## Systemanweisungen und andere Konfigurationen

Mit Systemanweisungen können Sie das Verhalten von Gemini-Modellen steuern. Übergeben Sie einen `system_instruction`-Parameter, um das Verhalten des Modells zu konfigurieren.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    system_instruction="You are a cat. Your name is Neko.",
    input="Hello there"
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Hello there",
    system_instruction: "You are a cat. Your name is Neko.",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "system_instruction": "You are a cat. Your name is Neko.",
    "input": "Hello there"
  }'
```

Sie können auch Standardparameter für die Generierung, z. B. die Temperatur, mit dem Parameter `generation_config` überschreiben.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works",
    generation_config={
        "temperature": 1.0
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works",
    generation_config: {
      temperature: 1.0,
    },
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works",
    "generation_config": {
      "temperature": 1.0
    }
  }'
```

Eine vollständige Liste der konfigurierbaren Parameter und ihrer Beschreibungen finden Sie in der [Interactions API-Referenz](https://ai.google.dev/api/interactions-api?hl=de).

## Multimodale Eingaben

Die Gemini API unterstützt multimodale Eingaben, sodass Sie Text mit Mediendateien kombinieren können. Im folgenden Beispiel wird gezeigt, wie ein Bild bereitgestellt wird:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/organ.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Tell me about this instrument"},
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const uploadedFile = await ai.files.upload({
    file: "path/to/organ.jpg",
    config: { mimeType: "image/jpeg" }
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: [
      {type: "text", text: "Tell me about this instrument"},
      {
        type: "image",
        uri: uploadedFile.uri,
        mime_type: uploadedFile.mimeType
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Tell me about this instrument"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

Alternative Methoden zum Bereitstellen von Bildern und zur erweiterten Bildverarbeitung finden Sie in unserem [Leitfaden zur Bildanalyse](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=de).
Die API unterstützt auch [Dokument-](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=de), [Video-](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=de) und [Audioeingaben](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=de).

## Streamingantworten

Standardmäßig gibt das Modell erst dann eine Antwort zurück, wenn der gesamte Generierungsprozess abgeschlossen ist.

Für flüssigere Interaktionen können Sie Streaming verwenden, um Antwortblöcke zu verarbeiten, sobald sie generiert werden. Einen umfassenden Leitfaden zu Ereignistypen, Streaming mit Tools, Denken, Agents und Bilderstellung finden Sie im [Leitfaden zu Streaming-Interaktionen](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=de).

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works",
    stream=True
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const stream = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works",
    stream: true,
  });

  for await (const event of stream) {
    if (event.event_type === "step.delta") {
      if (event.delta.type === "text") {
        process.stdout.write(event.delta.text);
      }
    }
  }
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works",
    "stream": true
  }'
```

## Unterhaltungen über mehrere Themen

Die Interactions API unterstützt Multi-Turn-Unterhaltungen, indem Interaktionen mit `previous_interaction_id` verkettet werden. Jede Runde ist eine separate Interaktion und der Unterhaltungsverlauf wird automatisch von der API verwaltet.

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="I have 2 dogs in my house.",
)
print(interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print(interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.output_text);

  const interaction2 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
  });
  console.log("Response 2:", interaction2.output_text);
}

await main();
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "I have two dogs in my house. How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

Streaming kann auch für Multi-Turn-Unterhaltungen verwendet werden, indem `previous_interaction_id` mit den Streaming-Methoden kombiniert wird.

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="I have 2 dogs in my house.",
)
print(interaction1.output_text)

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
    stream=True
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.output_text);

  const stream = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
    stream: true,
  });
  for await (const event of stream) {
    if (event.event_type === "step.delta") {
      if (event.delta.type === "text") {
        process.stdout.write(event.delta.text);
      }
    }
  }
}

await main();
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "I have 2 dogs in my house."
  }')
INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "stream": true
  }'
```

## Zustandslose Unterhaltungen

Standardmäßig wird der Unterhaltungsstatus serverseitig von der Interactions API verwaltet, wenn Sie `previous_interaction_id` verwenden. Sie können den Dienst jedoch auch im statuslosen Modus verwenden, indem Sie den Unterhaltungsverlauf selbst auf der Clientseite verwalten.

So verwenden Sie den zustandslosen Modus:
1. Legen Sie `store=false` in Ihrer Anfrage fest, um die serverseitige Speicherung zu deaktivieren.
2. Der Unterhaltungsverlauf wird clientseitig als Array von **Schritten** verwaltet.
3. Übergeben Sie in nachfolgenden Anfragen die gesammelten Schritte im Feld `input` und hängen Sie Ihren neuen Zug als `user_input`-Schritt an.

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
    model="gemini-3.5-flash",
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
    model="gemini-3.5-flash",
    store=False,
    input=history
)
print("Response 2:", interaction2.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const history = [
    {
      type: "user_input",
      content: [{ type: "text", text: "I have 2 dogs in my house." }]
    }
  ];

  const interaction1 = await ai.interactions.create({
    model: "gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
    store: false,
    input: history
  });
  console.log("Response 2:", interaction2.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
# Turn 1: Send request with store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "I have 2 dogs in my house."
      }
    ]
  }')

# Extract the steps from response
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Reconstruct the full history for Turn 2 by combining:
# 1. First user input
# 2. Model response steps
# 3. Second user input
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "I have 2 dogs in my house."}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --argjson second_input '[{"type": "user_input", "content": "How many paws are in my house?"}]' \
  "'"'"'$first_input + $model_steps + $second_input'"'"'")

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.5-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

## Tipps für Prompts

In unserem [Leitfaden zum Erstellen von Prompts](https://ai.google.dev/gemini/docs/prompting-strategies?hl=de) finden Sie Vorschläge, wie Sie Gemini optimal nutzen können.

## Nächste Schritte

- [Gemini in Google AI Studio testen](https://aistudio.google.com?hl=de)
- Experimentieren Sie mit [strukturierten Ausgaben](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=de) für JSON-ähnliche Antworten.
- [Bild](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=de)-, [Video](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=de)-, [Audio](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=de)- und [Dokumentverständnis](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=de) von Gemini
- [Weitere Informationen zu multimodalen Strategien für Dateiprompts](https://ai.google.dev/gemini-api/docs/interactions/files?hl=de#prompt-guide)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-08 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-08 (UTC)."],[],[]]
