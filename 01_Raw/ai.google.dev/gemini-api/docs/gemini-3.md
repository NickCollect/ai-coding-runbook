---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=de
fetched_at: 2026-08-03T04:37:45.874090+00:00
title: "Entwicklerleitfaden f\u00fcr Gemini\u00a03 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)

Feedback geben

# Entwicklerleitfaden für Gemini 3

Gemini 3 ist unsere bisher intelligenteste Modellfamilie, die auf modernster Problemlösungsfähigkeit basiert. Sie wurde entwickelt, um jede Idee zum Leben zu erwecken, indem sie agentenbasierte Workflows, autonomes Programmieren und komplexe multimodale Aufgaben beherrscht.
In diesem Leitfaden werden die wichtigsten Funktionen der Gemini 3-Modellfamilie und die optimale Nutzung beschrieben.

In unserer [Sammlung von Gemini 3-Apps](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=de) können Sie sehen, wie das Modell mit logischem Schlussfolgern, autonomem Programmieren und komplexen multimodalen Aufgaben umgeht.

Erste Schritte mit wenigen Codezeilen:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.output_text);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## Die Gemini 3-Serie

Gemini 3.1 Pro eignet sich am besten für komplexe Aufgaben, die umfassendes Weltwissen und fortschrittliches logisches Schlussfolgern über verschiedene Modalitäten hinweg erfordern.

Gemini 3 Flash ist unser neuestes Modell der 3-Serie mit Pro-Level-Intelligenz und der Geschwindigkeit und dem Preis von Flash.

Nano Banana Pro (auch bekannt als Gemini 3 Pro Image) ist unser hochwertigstes Modell für die Bildgenerierung. Nano Banana 2 (auch bekannt als Gemini 3.1 Flash Image) ist das entsprechende Modell für große Mengen und hohe Effizienz zu einem niedrigeren Preis.

Gemini 3.1 Flash-Lite ist unser Arbeitstier-Modell, das auf Kosteneffizienz und Aufgaben mit hohem Volumen ausgelegt ist.

Alle Gemini 3-Modelle sind derzeit als Vorabversion verfügbar.

| Modell-ID | Kontextfenster (Ein-/Ausgabe) | Wissensstichtag | Preise (Ein-/Ausgabe)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1 Mio. / 64.000 | Januar 2025 | 0,25 $ (Text, Bild, Video), 0,50 $ (Audio) / 1,50 $ |
| **gemini-3.1-flash-image-preview** | 128.000 / 32.000 | Januar 2025 | 0,25 $ (Texteingabe) / 0,067 $ (Bildausgabe)\*\* |
| **gemini-3.1-pro-preview** | 1 Mio. / 64.000 | Januar 2025 | 2 $ / 12 $ (< 200.000 Tokens)   4 $ / 18 $ (> 200.000 Tokens) |
| **gemini-3-flash-preview** | 1 Mio. / 64.000 | Januar 2025 | 0,50 $ / 3 $ |
| **gemini-3-pro-image-preview** | 65.000 / 32.000 | Januar 2025 | 2 $ (Texteingabe) / 0,134 $ (Bildausgabe)\*\* |

*\* Sofern nicht anders angegeben, gelten die Preise pro 1 Million Tokens.*
*\*\* Die Preise für Bilder variieren je nach Auflösung. Weitere Informationen finden Sie auf der [Preisseite](https://ai.google.dev/gemini-api/docs/pricing?hl=de).*

Ausführliche Informationen zu Limits, Preisen und zusätzliche Informationen finden Sie auf der
[Seite Modelle](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de).

## Neue API-Funktionen in Gemini 3

In Gemini 3 werden neue Parameter eingeführt, mit denen Entwickler mehr Kontrolle über Latenz, Kosten und multimodale Genauigkeit haben.

### Denkaufwand

Die Modelle der Gemini 3-Serie verwenden standardmäßig dynamisches Denken, um Prompts zu verarbeiten. Sie können den Parameter `thinking_level` verwenden, der die **maximale** Tiefe des internen Denkprozesses des Modells steuert, bevor es eine Antwort generiert. Gemini 3 behandelt diese Stufen als relative Zulagen für den Denkaufwand und nicht als strikte Token-Garantien.

Wenn `thinking_level` nicht angegeben ist, verwendet Gemini 3 standardmäßig `high`. Für schnellere Antworten mit geringerer Latenz, wenn keine komplexe Problemlösung erforderlich ist, können Sie den Denkaufwand des Modells auf `low` beschränken.

| Denkaufwand | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Beschreibung |
| --- | --- | --- | --- | --- |
| **`minimal`** | Nicht unterstützt | Unterstützt (Standardeinstellung) | Unterstützt | Entspricht bei den meisten Abfragen der Einstellung „Kein Denkaufwand“. Bei komplexen Programmieraufgaben kann das Modell sehr wenig nachdenken. Minimiert die Latenz für Chat- oder Anwendungen mit hohem Durchsatz. Hinweis: `minimal` garantiert nicht, dass der Denkaufwand deaktiviert ist. |
| **`low`** | Unterstützt | Unterstützt | Unterstützt | Minimiert Latenz und Kosten. Am besten geeignet für einfache Anweisungen, Chat- oder Anwendungen mit hohem Durchsatz. |
| **`medium`** | Unterstützt | Unterstützt | Unterstützt | Ausgewogener Denkaufwand für die meisten Aufgaben. |
| **`high`** | Unterstützt (Standardeinstellung, dynamisch) | Unterstützt (dynamisch) | Unterstützt (Standardeinstellung, dynamisch) | Maximiert die Tiefe der Problemlösung. Es kann deutlich länger dauern, bis das Modell das erste Ausgabetoken (ohne Denkaufwand) erreicht, aber die Ausgabe ist sorgfältiger durchdacht. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### Temperatur

Für alle Gemini 3-Modelle empfehlen wir dringend, den Temperaturparameter auf dem Standardwert `1.0` zu belassen.

Bei früheren Modellen war es oft sinnvoll, die Temperatur anzupassen, um die Kreativität im Vergleich zum Determinismus zu steuern. Die Problemlösungsfähigkeiten von Gemini 3 sind jedoch für die Standardeinstellung optimiert. Wenn Sie die Temperatur ändern (auf einen Wert unter 1.0 setzen), kann dies zu unerwartetem Verhalten wie Schleifen oder einer geringeren Leistung führen, insbesondere bei komplexen mathematischen oder Problemlösungsaufgaben.

### Gedankensignaturen

Gemini 3-Modelle verwenden Gedankensignaturen, um den Kontext der Problemlösung über API-Aufrufe hinweg beizubehalten. Diese Signaturen sind verschlüsselte Darstellungen des internen Denkprozesses des Modells.

- **Statusbehafteter Modus (empfohlen)**: Wenn Sie die Interactions API im statusbehafteten Modus verwenden (mit Angabe von `previous_interaction_id`), verwaltet der Server automatisch den Unterhaltungsverlauf und die Gedankensignaturen.
- **Zustandsloser Modus**: Wenn Sie den Unterhaltungsverlauf manuell verwalten, müssen Sie in nachfolgenden Anfragen Gedankenblöcke mit ihren Signaturen einfügen, um die Authentizität zu bestätigen.

Weitere Informationen finden Sie auf der Seite [Gedankensignaturen](https://ai.google.dev/gemini-api/docs/thinking?hl=de).`

### Strukturierte Ausgaben mit Tools

Mit Gemini 3-Modellen können Sie [strukturierte Ausgaben](https://ai.google.dev/gemini-api/docs/structured-output?hl=de) mit integrierten Tools kombinieren, darunter
[Fundierung mit der Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de), [URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de), [Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) und [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.output_text));
  console.log(match);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### Bildgenerierung

Mit Gemini 3.1 Flash Image und Gemini 3 Pro Image können Sie Bilder aus Text-Prompts generieren und bearbeiten. Dabei wird die Problemlösungsfähigkeit genutzt, um einen Prompt zu verarbeiten. Außerdem können Echtzeitdaten wie Wettervorhersagen oder Aktienkurse abgerufen werden, bevor die Fundierung mit der [Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de) verwendet wird, um Bilder in hoher Qualität zu generieren.

**Neue und verbesserte Funktionen** :

- **4K- und Textrendering**:Generieren Sie scharfe, gut lesbare Texte und Diagramme mit einer Auflösung von bis zu 2K und 4K.
- **Fundierte Generierung**:Verwenden Sie das Tool `google_search`, um Fakten zu überprüfen und Bilder auf Grundlage von realen Informationen zu generieren. Die Fundierung mit der Google *Bildersuche* ist für Gemini 3.1 Flash Image verfügbar.
- **Bearbeitung per Prompt**:Bildbearbeitung in mehreren Schritten, indem Sie einfach Änderungen anfordern (z.B. „Ersetze den Hintergrund durch einen Sonnenuntergang“). Dieser Workflow basiert auf **Gedankensignaturen** , um den visuellen Kontext zwischen den Schritten beizubehalten.

Ausführliche Informationen zu Seitenverhältnissen, Bearbeitungs-Workflows und Konfigurations
optionen finden Sie im [Leitfaden zur Bildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de).

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

generated_image = interaction.output_image
if generated_image:
    image_data = base64.b64decode(generated_image.data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  const buffer = Buffer.from(interaction.output_image.data, 'base64');

  fs.writeFileSync('weather_tokyo.png', buffer);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
  }'
```

**Beispielantwort**

![Wetter in Tokio](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=de)

### Codeausführung mit Bildern

Gemini 3 Flash kann Vision als aktive Untersuchung behandeln und nicht nur als statischen Blick. Durch die Kombination von Schlussfolgern und [Code-Ausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) formuliert das Modell einen Plan, schreibt dann Python-Code und führt ihn aus, um Bilder Schritt für Schritt zu vergrößern, zuzuschneiden, mit Anmerkungen zu versehen oder anderweitig zu bearbeiten, um seine Antworten visuell zu untermauern.

**Anwendungsbeispiele** :

- **Vergrößern und prüfen**:Das Modell erkennt implizit, wenn Details zu klein sind (z.B. beim Lesen eines weit entfernten Messgeräts oder einer Seriennummer), und schreibt Code, um den Bereich zuzuschneiden und mit einer höheren Auflösung neu zu prüfen.
- **Visuelle Mathematik und Diagramme**:Das Modell kann mehrstufige Berechnungen mit Code ausführen (z.B. Summe der Positionen auf einer Rechnung oder Generieren eines Matplotlib-Diagramms aus extrahierten Daten).
- **Bildanmerkungen**:Das Modell kann Pfeile, Begrenzungsrahmen oder andere Anmerkungen direkt in Bilder einzeichnen, um räumliche Fragen wie „Wo soll dieser Artikel hin?“ zu beantworten.

Wenn Sie visuelles Denken aktivieren möchten, konfigurieren Sie [die Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) als Tool. Das Modell verwendet bei Bedarf automatisch Code, um Bilder zu bearbeiten.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

Weitere Informationen zur Code-Ausführung mit Bildern finden Sie unter [Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de#images).

### Multimodale Funktionsantworten

[Multimodale Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de#multimodal)
ermöglichen Nutzern Funktionsantworten mit
multimodalen Objekten, wodurch die Funktionsaufruffunktionen des Modells besser genutzt werden können. Standardmäßige Funktionsaufrufe unterstützen nur textbasierte Funktionsantworten:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

print(f"\nFinal model response: {interaction_2.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.output_text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### Integrierte Tools und Funktionsaufrufe kombinieren

Mit Gemini 3 können Sie integrierte Tools (z. B. Google Suche, URL
Kontext und [mehr](https://ai.google.dev/gemini-api/docs/tools?hl=de)) und benutzerdefinierte [Funktionsaufruf](https://ai.google.dev/gemini-api/docs/function-calling?hl=de)-Tools im selben API-Aufruf verwenden, was komplexere Workflows ermöglicht.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
}
```

## Migration von Gemini 2.5

Gemini 3 ist unsere bisher leistungsstärkste Modellfamilie und bietet eine schrittweise Verbesserung gegenüber Gemini 2.5. Beachten Sie bei der Migration Folgendes:

- **Denkaufwand:** Wenn Sie zuvor komplexe Prompt-Techniken (z. B.
  Chain of Thought) verwendet haben, um Gemini 2.5 zum Nachdenken zu zwingen, probieren Sie Gemini 3 mit
  `thinking_level: "high"` und vereinfachten Prompts aus.
- **Temperatureinstellungen**:Wenn Ihr vorhandener Code die Temperatur explizit festlegt (insbesondere auf niedrige Werte für deterministische Ausgaben), empfehlen wir, diesen Parameter zu entfernen und den Standardwert von Gemini 3 (1.0) zu verwenden, um potenzielle Schleifenprobleme oder Leistungseinbußen bei komplexen Aufgaben zu vermeiden.
- **PDF- und Dokumentenverständnis**:Wenn Sie sich auf ein bestimmtes Verhalten für die Analyse von Dokumenten mit vielen Informationen verlassen haben, testen Sie die neue Einstellung `media_resolution_high`, um die Genauigkeit beizubehalten.
- **Token-Verbrauch**:Bei der Migration zu den Standardeinstellungen von Gemini 3 kann der Token-Verbrauch für PDFs **steigen** , für Videos jedoch **sinken**. Wenn Anfragen aufgrund höherer Standardauflösungen jetzt das Kontextfenster überschreiten, empfehlen wir, die Medienauflösung explizit zu reduzieren.
- **Bildsegmentierung**:Die Bildsegmentierungsfunktionen (die Masken auf Pixelebene für Objekte zurückgeben) werden in Gemini 3 Pro oder Gemini 3 Flash nicht unterstützt. Für Arbeitslasten, die eine integrierte Bildsegmentierung erfordern, empfehlen wir, weiterhin Gemini 2.5 Flash mit deaktiviertem Denkaufwand zu verwenden.
- **Computernutzung:** Gemini 3 Pro und Gemini 3 Flash unterstützen die [Computer
  nutzung](https://ai.google.dev/gemini-api/docs/computer-use?hl=de). Im Gegensatz zur 2.5-Serie müssen Sie kein separates Modell verwenden, um auf das Tool für die Computernutzung zuzugreifen.
- **Toolunterstützung**: [Die Kombination von integrierten Tools mit Funktionsaufrufen](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de) wird jetzt für Gemini 3-Modelle unterstützt. [Die Fundierung mit Google Maps
  wird jetzt auch für Gemini 3
  Modelle unterstützt.](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de)

## OpenAI-Kompatibilität

Für Nutzer, die die [OpenAI-Kompatibilitätsebene](https://ai.google.dev/gemini-api/docs/openai?hl=de) verwenden,
werden Standardparameter (OpenAIs `reasoning_effort`) automatisch den entsprechenden
Gemini-Parametern (`thinking_level`) zugeordnet.

## Best Practices für Prompts

Gemini 3 ist ein Modell für die Problemlösung, was sich auf die Art und Weise auswirkt, wie Sie Prompts erstellen sollten.

- **Genaue Anweisungen**:Formulieren Sie Ihre Eingabe-Prompts präzise. Gemini 3 reagiert am besten auf direkte, klare Anweisungen. Es kann zu einer Überanalyse von ausführlichen oder übermäßig komplexen Prompt-Techniken kommen, die für ältere Modelle verwendet wurden.
- **Ausführlichkeit der Ausgabe**:Standardmäßig ist Gemini 3 weniger ausführlich und bevorzugt direkte, effiziente Antworten. Wenn Ihr Anwendungsfall eine gesprächigere oder „geschwätzige“ Persona erfordert, müssen Sie das Modell im Prompt explizit anweisen (z.B. „Erkläre das als freundlicher, gesprächiger Assistent“).
- **Kontextverwaltung**:Wenn Sie mit großen Datasets arbeiten (z.B. ganze Bücher, Codebasen oder lange Videos), platzieren Sie Ihre spezifischen Anweisungen oder Fragen am Ende des Prompts, nach dem Datenkontext. Verankern Sie die Problemlösung des Modells an den bereitgestellten Daten, indem Sie Ihre Frage mit einer Formulierung wie „Basierend auf den vorherigen Informationen…“ beginnen.

Weitere Informationen zu Strategien für das Design von Prompts finden Sie im [Leitfaden zum Prompt Engineering](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=de).

## FAQ

1. **Was ist der Wissensstichtag für Gemini 3?** Die Gemini 3-Modelle haben einen Wissensstichtag im Januar 2025. Aktuellere Informationen finden Sie mit dem
   [Tool für die Fundierung mit der Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de).
2. **Was sind die Limits für das Kontextfenster?** Gemini 3-Modelle unterstützen ein Kontextfenster für die Eingabe mit 1 Million Tokens und bis zu 64.000 Tokens für die Ausgabe.
3. **Gibt es eine kostenlose Stufe für Gemini 3?** Für Gemini 3 Flash `gemini-3-flash-preview` gibt es in der Gemini API eine kostenlose Stufe. Sie können Gemini 3.1 Pro und 3 Flash kostenlos in Google AI Studio testen. Für `gemini-3.1-pro-preview` ist in der Gemini API jedoch keine kostenlose Stufe verfügbar.
4. **Funktioniert mein alter `thinking_budget` Code noch?** Ja, `thinking_budget` wird weiterhin für die Abwärtskompatibilität unterstützt. Wir empfehlen jedoch, zu `thinking_level` zu migrieren, um eine besser vorhersagbare Leistung zu erzielen. Verwenden Sie nicht beide in derselben Anfrage.
5. **Unterstützt Gemini 3 die Batch API?** Ja, Gemini 3 unterstützt die
   [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de).
6. **Wird das Kontext-Caching unterstützt?** Ja, das [Kontext-Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de) wird für Gemini 3 unterstützt.
7. **Welche Tools werden in Gemini 3 unterstützt?** Gemini 3 unterstützt
   [die Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de),
   [die Fundierung mit Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de),
   [die Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de),
   [die Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) und
   [den URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de). Außerdem werden
   standardmäßige [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de) für
   Ihre eigenen benutzerdefinierten Tools und in
   [Kombination mit integrierten Tools](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de) unterstützt.
8. **Was ist `gemini-3.1-pro-preview-customtools`?** Wenn Sie
   `gemini-3.1-pro-preview` verwenden und das Modell Ihre benutzerdefinierten Tools zugunsten von
   Bash-Befehlen ignoriert, versuchen Sie stattdessen das `gemini-3.1-pro-preview-customtools` Modell.
   Weitere Informationen finden Sie [hier][customtools-model].

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
