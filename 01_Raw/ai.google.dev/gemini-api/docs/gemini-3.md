---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=de
fetched_at: 2026-06-15T06:22:10.559109+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=de)

Feedback geben

# Entwicklerleitfaden für Gemini 3

Gemini 3 ist unsere bisher intelligenteste Modellfamilie, die auf modernsten Schlussfolgerungsfunktionen basiert. Sie wurde entwickelt, um jede Idee zu verwirklichen, indem sie agentische Workflows, autonomes Programmieren und komplexe multimodale Aufgaben beherrscht.
In diesem Leitfaden werden die wichtigsten Funktionen der Gemini 3-Modellfamilie und die optimale Nutzung beschrieben.

[Gemini 3.1 Pro (Vorschau) ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=de)
[Gemini 3 Flash (Vorschau) ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=de)
[Gemini 3.1 Flash-Lite ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-lite&hl=de)
[Nano Banana 2 ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=de)

Entdecken Sie unsere [Sammlung von Gemini 3-Apps](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=de), um zu sehen, wie das Modell mit logischem Schlussfolgern, autonomer Programmierung und komplexen multimodalen Aufgaben umgeht.

So können Sie mit wenigen Codezeilen loslegen:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## Die Gemini 3-Serie

Gemini 3.1 Pro eignet sich am besten für komplexe Aufgaben, die umfassendes Weltwissen und fortschrittliches multimodales logisches Schlussfolgern erfordern.

Gemini 3 Flash ist unser neuestes Modell der 3-Serie. Es bietet Intelligenz auf Pro-Niveau mit der Geschwindigkeit und dem Preis von Flash.

Nano Banana Pro (auch bekannt als Gemini 3 Pro Image) ist unser hochwertigstes Modell für die Bildgenerierung. Nano Banana 2 (auch bekannt als Gemini 3.1 Flash Image) ist das Äquivalent für große Mengen und hohe Effizienz zu einem niedrigeren Preis.

Gemini 3.1 Flash-Lite ist unser Modell für den Alltag, das auf Kosteneffizienz und Aufgaben mit hohem Volumen ausgelegt ist.

| Modell-ID | Verlaufszeitraum (Ein-/Ausgang) | Wissensstichtag | Preise (Eingabe / Ausgabe)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1 Mio. / 64.000 | Januar 2025 | 0,25 $ (Text, Bild, Video), 0,50 $ (Audio) / 1,50 $ |
| **gemini-3.1-flash-image-preview** | 128.000 / 32.000 | Januar 2025 | 0,25 $ (Texteingabe) / 0,067 $ (Bildausgabe)\*\* |
| **gemini-3.1-pro-preview** | 1 Mio. / 64.000 | Januar 2025 | 2 $ / 12 $ (< 200.000 Tokens)   4 $ / 18 $ (> 200.000 Tokens) |
| **gemini-3-flash-preview** | 1 Mio. / 64.000 | Januar 2025 | 0,50 $ / 3 $ |
| **gemini-3-pro-image-preview** | 65.000 / 32.000 | Januar 2025 | 2 $ (Texteingabe) / 0,134 $ (Bildausgabe)\*\* |

*\* Die Preise gelten pro 1 Million Tokens, sofern nicht anders angegeben.*
*\*\* Die Preise für Bilder variieren je nach Auflösung. Weitere Informationen finden Sie auf der [Preisseite](https://ai.google.dev/gemini-api/docs/pricing?hl=de).*

Detaillierte Informationen zu Limits, Preisen und mehr finden Sie auf der [Seite zu Modellen](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de).

## Neue API-Funktionen in Gemini 3

Mit Gemini 3 werden neue Parameter eingeführt, mit denen Entwickler mehr Kontrolle über Latenz, Kosten und multimodale Genauigkeit erhalten.

### Denkaufwand

Gemini 3-Modelle verwenden standardmäßig dynamisches Denken, um Prompts zu analysieren. Sie können den Parameter `thinking_level` verwenden, der die **maximale** Tiefe des internen Denkprozesses des Modells steuert, bevor es eine Antwort generiert. Gemini 3 behandelt diese Ebenen als relative Kontingente für das Denken und nicht als strikte Token-Garantien.

Wenn `thinking_level` nicht angegeben ist, wird standardmäßig `high` verwendet. Wenn keine komplexen Schlussfolgerungen erforderlich sind, können Sie die Denkebene des Modells auf `low` beschränken, um schnellere Antworten mit geringerer Latenz zu erhalten.

| Denkaufwand | Gemini 3.1. Pro | Gemini 3.1 Flash Lite | Gemini 3 Flash | Beschreibung |
| --- | --- | --- | --- | --- |
| **`minimal`** | Nicht unterstützt | Unterstützt (Standard) | Unterstützt | Entspricht für die meisten Anfragen der Einstellung „Kein Denkprozess“. Das Modell kann bei komplexen Programmieraufgaben sehr wenig nachdenken. Minimiert die Latenz für Chat- oder Anwendungen mit hohem Durchsatz. Hinweis: `minimal` garantiert nicht, dass der Denkprozess deaktiviert ist. |
| **`low`** | Unterstützt | Unterstützt | Unterstützt | Minimiert Latenz und Kosten. Am besten geeignet für einfache Anweisungen, Chat oder Anwendungen mit hohem Durchsatz. |
| **`medium`** | Unterstützt | Unterstützt | Unterstützt | Ausgewogenes Denken für die meisten Aufgaben. |
| **`high`** | Unterstützt (Standard, dynamisch) | Unterstützt (dynamisch) | Unterstützt (Standard, dynamisch) | Maximiert die Tiefe des logischen Schlussfolgerns. Es kann deutlich länger dauern, bis das Modell das erste Ausgabetoken (nicht „thinking“) generiert, aber die Ausgabe ist sorgfältiger durchdacht. |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### Auflösung von Medien

Mit Gemini 3 wird die granulare Steuerung der multimodalen Bildverarbeitung über den Parameter `media_resolution` eingeführt. Höhere Auflösungen verbessern die Fähigkeit des Modells, feinen Text zu lesen oder kleine Details zu erkennen, erhöhen aber die Tokennutzung und die Latenz. Der Parameter `media_resolution` bestimmt die **maximale Anzahl der Token**, die pro Eingabebild oder Videoframes zugewiesen werden.

Sie können die Auflösung jetzt für jeden einzelnen Media-Teil oder global (über `generation_config`, global nicht für Ultra High verfügbar) auf `media_resolution_low`, `media_resolution_medium`, `media_resolution_high` oder `media_resolution_ultra_high` festlegen. Wenn nicht angegeben, verwendet das Modell optimale Standardwerte basierend auf dem Medientyp.

**Empfohlene Einstellungen**

| Medientyp | Empfohlene Einstellung | Maximale Anzahl an Tokens | Usage Guidance |
| --- | --- | --- | --- |
| **Bilder** | `media_resolution_high` | 1.120 | Für die meisten Bildanalyseaufgaben empfohlen, um maximale Qualität zu gewährleisten. |
| **PDFs** | `media_resolution_medium` | 560 | Optimal für das Verständnis von Dokumenten; die Qualität erreicht in der Regel bei `medium` ein Sättigungsniveau. Eine Erhöhung auf `high` führt bei Standarddokumenten selten zu besseren OCR-Ergebnissen. |
| **Video** (Allgemein) | `media_resolution_low` oder `media_resolution_medium` | 70 (pro Frame) | **Hinweis**:Bei Videos werden die Einstellungen für `low` und `medium` identisch behandelt (70 Tokens), um die Kontextnutzung zu optimieren. Das reicht für die meisten Aufgaben zur Aktionserkennung und ‑beschreibung aus. |
| **Video** (textlastig) | `media_resolution_high` | 280 (pro Frame) | Nur erforderlich, wenn der Anwendungsfall das Lesen von dichtem Text (OCR) oder kleinen Details in Videoframes umfasst. |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is currently only available in the v1alpha API version.
client = genai.Client(http_options={'api_version': 'v1alpha'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is currently only available in the v1alpha API version.
const ai = new GoogleGenAI({ apiVersion: "v1alpha" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1alpha/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### Temperatur

Für alle Gemini 3-Modelle empfehlen wir dringend, den Temperaturparameter auf dem Standardwert `1.0` zu belassen.

Bei früheren Modellen war es oft sinnvoll, die Temperatur anzupassen, um die Kreativität im Vergleich zum Determinismus zu steuern. Die Reasoning-Funktionen von Gemini 3 sind jedoch für die Standardeinstellung optimiert. Wenn Sie die Temperatur ändern (auf einen Wert unter 1,0), kann dies zu unerwartetem Verhalten führen, z. B. zu Schleifen oder einer schlechteren Leistung, insbesondere bei komplexen mathematischen oder Reasoning-Aufgaben.

### Gedankensignaturen

Gemini 3 verwendet [Thought signatures](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=de), um den Kontext der Argumentation über API-Aufrufe hinweg beizubehalten. Diese Signaturen sind verschlüsselte Darstellungen des internen Denkprozesses des Modells. Damit das Modell seine Argumentationsfähigkeiten beibehält, müssen Sie diese Signaturen in Ihrer Anfrage genau so an das Modell zurückgeben, wie sie empfangen wurden:

- **Funktionsaufruf (streng)**: Die API erzwingt eine strenge Validierung für den „Current Turn“. Fehlende Signaturen führen zu einem 400-Fehler.
- **Text/Chat**:Die Validierung wird nicht streng erzwungen, aber das Weglassen von Signaturen beeinträchtigt die Argumentation und Antwortqualität des Modells.
- **Bildgenerierung/‑bearbeitung (streng)**: Die API erzwingt eine strenge Validierung aller Modellteile, einschließlich eines `thoughtSignature`. Fehlende Signaturen führen zu einem 400-Fehler.

#### Funktionsaufrufe (strenge Validierung)

Wenn Gemini eine `functionCall` generiert, wird die `thoughtSignature` verwendet, um die Ausgabe des Tools im nächsten Zug korrekt zu verarbeiten. Der „aktuelle Zug“ umfasst alle Schritte des Modells (`functionCall`) und des Nutzers (`functionResponse`), die seit der letzten Standardnachricht **User** `text` erfolgt sind.

- **Einzelner Funktionsaufruf**:Der `functionCall`-Teil enthält eine Signatur. Sie müssen es zurückgeben.
- **Parallele Funktionsaufrufe**:Nur der erste `functionCall`-Teil in der Liste enthält die Signatur. Sie müssen die Teile in der genauen Reihenfolge zurücksenden, in der Sie sie erhalten haben.
- **Mehrstufig (sequenziell)**: Wenn das Modell ein Tool aufruft, ein Ergebnis empfängt und *ein anderes* Tool (im selben Zug) aufruft, haben **beide** Funktionsaufrufe Signaturen. Sie müssen **alle** im Verlauf gesammelten Signaturen zurückgeben.

#### Text und Streaming

Bei Standard-Chats oder der Textgenerierung ist das Vorhandensein einer Signatur nicht garantiert.

- **Nicht-Streaming**: Der letzte Inhaltsteil der Antwort kann ein `thoughtSignature` enthalten, ist aber nicht immer vorhanden. Wenn ein Gerät zurückgegeben wird, sollten Sie es zurücksenden, um eine optimale Leistung zu erzielen.
- **Streaming**: Wenn eine Signatur generiert wird, kann sie in einem letzten Chunk mit einem leeren Textteil ankommen. Achten Sie darauf, dass Ihr Stream-Parser auch dann nach Signaturen sucht, wenn das Textfeld leer ist.

#### Bilderstellung und -bearbeitung

Für `gemini-3-pro-image-preview` und `gemini-3.1-flash-image-preview` sind Gedanken-Signaturen für die Bildbearbeitung per Prompt entscheidend. Wenn Sie das Modell bitten, ein Bild zu ändern, stützt es sich auf die `thoughtSignature` aus dem vorherigen Zug, um die Komposition und Logik des Originalbilds zu verstehen.

- **Bearbeitung**:Signaturen sind garantiert im ersten Teil nach den Überlegungen der Antwort (`text` oder `inlineData`) und in jedem nachfolgenden `inlineData`-Teil. Sie müssen alle diese Signaturen zurückgeben, um Fehler zu vermeiden.

#### Codebeispiele

#### Mehrstufige Funktionsaufrufe (sequenziell)

Der Nutzer stellt eine Frage, die zwei separate Schritte erfordert („Flug prüfen“ –> „Taxi buchen“).   
  
**Schritt 1: Das Modell ruft das Flugtool auf.**  
Das Modell gibt die Signatur `<Sig_A>` zurück.

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**Schritt 2: Nutzer sendet Flugergebnis**  
Wir müssen `<Sig_A>` zurücksenden, um den Gedankengang des Modells beizubehalten.

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  {
    "role": "model",
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // REQUIRED
      }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**Schritt 3: Modell ruft Taxi Tool auf**  
Das Modell erinnert sich über `<Sig_A>` an die Flugverspätung und beschließt, ein Taxi zu buchen. Es generiert eine *neue* Signatur `<Sig_B>`.

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**Schritt 4: Nutzer sendet Taxi Result**  
Um den Zug abzuschließen, müssen Sie die gesamte Kette zurücksenden: `<Sig_A>` UND `<Sig_B>`.

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### Parallele Funktionsaufrufe

Der Nutzer fragt: „Wie ist das Wetter in Paris und London?“ Das Modell gibt zwei Funktionsaufrufe in einer Antwort zurück.

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### Text/Kontextbezogene Begründung (keine Validierung)

Der Nutzer stellt eine Frage, die eine kontextbezogene Argumentation ohne externe Tools erfordert. Die Signatur wird zwar nicht streng validiert, hilft dem Modell aber, die Kette der Argumentation für Folgefragen aufrechtzuerhalten.

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### Bildgenerierung und ‑bearbeitung

Bei der Bildgenerierung werden Signaturen streng validiert. Sie werden im **ersten Teil** (Text oder Bild) und **allen nachfolgenden Bildteilen** angezeigt. Alle müssen im nächsten Zug zurückgegeben werden.

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### Migration von anderen Modellen

Wenn Sie einen Unterhaltungsverlauf von einem anderen Modell (z.B. Gemini 2.5) übertragen oder einen benutzerdefinierten Funktionsaufruf einfügen, der nicht von Gemini 3 generiert wurde, haben Sie keine gültige Signatur.

Wenn Sie die strenge Validierung in diesen spezifischen Szenarien umgehen möchten, füllen Sie das Feld mit diesem bestimmten Dummy-String aus: `"thoughtSignature": "context_engineering_is_the_way
to_go"`

### Strukturierte Ausgaben mit Tools

Mit Gemini 3-Modellen können Sie [strukturierte Ausgaben](https://ai.google.dev/gemini-api/docs/structured-output?hl=de) mit integrierten Tools kombinieren, darunter [Fundierung mit der Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de), [URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de), [Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) und [Funktionsaufruf](https://ai.google.dev/gemini-api/docs/function-calling?hl=de).

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_format": {"text": {"mime_type": "application/json", "schema": MatchResult.model_json_schema()}},
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(matchSchema) } },
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
"responseFormat": {
  "text": {
    "mimeType": "application/json",
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
  }
}
},
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### Bildgenerierung

Mit Gemini 3.1 Flash Image und Gemini 3 Pro Image können Sie Bilder aus Text-Prompts generieren und bearbeiten. Dabei wird Reasoning verwendet, um einen Prompt zu „durchdenken“. Außerdem können Echtzeitdaten wie Wettervorhersagen oder Aktiencharts abgerufen werden, bevor mit [Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de) hochwertige Bilder generiert werden.

**Neue und verbesserte Funktionen**:

- **4K- und Textrendering**:Generieren Sie gestochen scharfen, gut lesbaren Text und Diagramme mit einer Auflösung von bis zu 2K und 4K.
- **Fundierte Generierung**:Verwenden Sie das `google_search`-Tool, um Fakten zu überprüfen und Bilder auf Grundlage von realen Informationen zu generieren. Die Fundierung mit der *Google Bildersuche* ist für Gemini 3.1 Flash Image verfügbar.
- **Bildbearbeitung per Prompt**:Sie können Bilder in mehreren Schritten bearbeiten, indem Sie einfach nach Änderungen fragen, z.B. „Mach den Hintergrund zu einem Sonnenuntergang“. Dieser Workflow basiert auf **Thought Signatures**, um den visuellen Kontext zwischen den Zügen beizubehalten.

Ausführliche Informationen zu Seitenverhältnissen, Bearbeitungs-Workflows und Konfigurationsoptionen finden Sie im [Leitfaden zur Bilderstellung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        response_format={"image": {"aspect_ratio": "16:9", "image_size": "4K"}}
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      responseFormat: {
    image: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
  }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
        "responseFormat": {
    "image": {
          "aspectRatio": "16:9",
          "imageSize": "4K"
      }
  }
    }
  }'
```

**Beispielantwort**

![Wetter in Tokio](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=de)

### Codeausführung mit Bildern

Gemini 3 Flash kann visuelle Informationen als aktive Untersuchung und nicht nur als statischen Blick betrachten. Durch die Kombination von Reasoning mit [Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) formuliert das Modell einen Plan und schreibt und führt dann Python-Code aus, um Bilder Schritt für Schritt zu vergrößern, zuzuschneiden, zu annotieren oder anderweitig zu bearbeiten, um seine Antworten visuell zu untermauern.

**Anwendungsbeispiele:**

- **Zoomen und prüfen**:Das Modell erkennt implizit, wenn Details zu klein sind (z.B. beim Lesen eines weit entfernten Messgeräts oder einer Seriennummer), und schreibt Code, um den Bereich zuzuschneiden und mit höherer Auflösung neu zu untersuchen.
- **Visuelle Mathematik und Diagramme**:Das Modell kann mehrstufige Berechnungen mit Code ausführen, z.B. Positionen auf einem Beleg summieren oder ein Matplotlib-Diagramm aus extrahierten Daten erstellen.
- **Bildanmerkungen**:Das Modell kann Pfeile, Begrenzungsrahmen oder andere Anmerkungen direkt in Bilder einfügen, um räumliche Fragen wie „Wo sollte dieser Artikel platziert werden?“ zu beantworten.

Wenn Sie visuelles Denken aktivieren möchten, konfigurieren Sie [Code Execution](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) (Code-Ausführung) als Tool. Das Modell verwendet bei Bedarf automatisch Code, um Bilder zu bearbeiten.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
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

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

Weitere Informationen zur Codeausführung mit Bildern finden Sie unter [Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de#images).

### Multimodale Funktionsantworten

Mit [multimodalen Funktionsaufrufen](https://ai.google.dev/gemini-api/docs/function-calling?hl=de#multimodal) können Nutzer Funktionsantworten mit multimodalen Objekten erhalten, wodurch die Möglichkeiten der Funktionsaufrufe des Modells besser genutzt werden können. Standard-Funktionsaufrufe unterstützen nur textbasierte Funktionsantworten:

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### Integrierte Tools und Funktionsaufrufe kombinieren

Mit Gemini 3 können integrierte Tools (z. B. die Google Suche, der URL-Kontext und [weitere](https://ai.google.dev/gemini-api/docs/tools?hl=de)) und benutzerdefinierte [Funktionsaufruf](https://ai.google.dev/gemini-api/docs/function-calling?hl=de)-Tools im selben API-Aufruf verwendet werden, was komplexere Workflows ermöglicht. [Weitere Informationen](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de)

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
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

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.models.generateContent({
        model: "gemini-3-flash-preview",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;
    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });
}

run();
```

## Von Gemini 2.5 migrieren

Gemini 3 ist unsere bisher leistungsstärkste Modellreihe und bietet eine schrittweise Verbesserung gegenüber Gemini 2.5. Bei der Migration sollten Sie Folgendes beachten:

- **Thinking**:Wenn Sie bisher komplexes Prompt-Engineering (z. B. Chain of Thought) verwendet haben, um Gemini 2.5 zum Schlussfolgern zu zwingen, probieren Sie Gemini 3 mit `thinking_level: "high"` und vereinfachten Prompts aus.
- **Temperatureinstellungen**:Wenn in Ihrem vorhandenen Code die Temperatur explizit festgelegt wird (insbesondere auf niedrige Werte für deterministische Ausgaben), empfehlen wir, diesen Parameter zu entfernen und den Gemini 3-Standardwert von 1,0 zu verwenden, um potenzielle Probleme mit Schleifen oder Leistungseinbußen bei komplexen Aufgaben zu vermeiden.
- **PDF- und Dokumentanalyse**:Wenn Sie sich auf ein bestimmtes Verhalten beim Parsen von dichten Dokumenten verlassen haben, testen Sie die neue Einstellung `media_resolution_high`, um die Genauigkeit beizubehalten.
- **Tokenverbrauch**:Durch die Migration zu Gemini 3-Standardeinstellungen kann der Tokenverbrauch für PDFs **steigen**, für Videos jedoch **sinken**. Wenn Anfragen aufgrund höherer Standardauflösungen das Kontextfenster überschreiten, empfehlen wir, die Media-Auflösung explizit zu verringern.
- **Bildsegmentierung**:Die Funktionen zur Bildsegmentierung (Rückgabe von Masken auf Pixelebene für Objekte) werden in Gemini 3 Pro oder Gemini 3 Flash nicht unterstützt. Für Arbeitslasten, die eine native Bildsegmentierung erfordern, empfehlen wir, weiterhin Gemini 2.5 Flash mit deaktivierter Denkfunktion oder [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=de) zu verwenden.
- **Computer Use**:Gemini 3 Pro und Gemini 3 Flash unterstützen [Computer Use](https://ai.google.dev/gemini-api/docs/computer-use?hl=de). Anders als bei der 2.5-Serie benötigen Sie kein separates Modell, um auf das Tool „Computer Use“ zuzugreifen.
- **Tool-Unterstützung**: [Die Kombination von integrierten Tools mit Funktionsaufrufen](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de) wird jetzt für Gemini 3-Modelle unterstützt. [Maps-Fundierung](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de) wird jetzt auch für Gemini 3-Modelle unterstützt.
- **Anzahl der Kandidaten**: Gemini 3-Modelle unterstützen `candidateCount > 1` nicht.
  Wenn Sie diesen Parameter auf einen Wert größer als `1` festlegen, wird ein 400-Fehler zurückgegeben.

## OpenAI-Kompatibilität

Für Nutzer, die die [OpenAI-Kompatibilitätsebene](https://ai.google.dev/gemini-api/docs/openai?hl=de) verwenden, werden Standardparameter (`reasoning_effort` von OpenAI) automatisch Gemini-Entsprechungen (`thinking_level`) zugeordnet.

## Best Practices für die Prompt-Erstellung

Gemini 3 ist ein Modell für das Schlussfolgern, was sich auf die Art und Weise auswirkt, wie Sie Prompts erstellen sollten.

- **Präzise Anweisungen**:Formulieren Sie Ihre Eingabeaufforderungen präzise. Gemini 3 reagiert am besten auf direkte, klare Anweisungen. Bei ausführlichen oder zu komplexen Prompt-Engineering-Techniken, die für ältere Modelle verwendet werden, kann es zu einer Überanalyse kommen.
- **Ausführlichkeit der Ausgabe**:Standardmäßig ist Gemini 3 weniger ausführlich und liefert lieber direkte, effiziente Antworten. Wenn für Ihren Anwendungsfall eine eher konversationelle oder „geschwätzige“ Persona erforderlich ist, müssen Sie das Modell im Prompt explizit darauf hinweisen (z.B. „Erkläre das als freundlicher, gesprächiger Assistent“).
- **Kontextverwaltung**:Wenn Sie mit großen Datasets arbeiten (z. B. ganze Bücher, Codebases oder lange Videos), platzieren Sie Ihre spezifischen Anweisungen oder Fragen am Ende des Prompts, nach dem Datenkontext. Verankern Sie die Argumentation des Modells in den bereitgestellten Daten, indem Sie Ihre Frage mit einer Formulierung wie „Basierend auf den oben genannten Informationen…“ beginnen.

Weitere Informationen zu Strategien für das Design von Prompts finden Sie im [Leitfaden zum Prompt-Engineering](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=de).

## FAQ

1. **Was ist der Wissensstand von Gemini 3?** Die Gemini 3-Modelle haben einen Wissensstand von Januar 2025. Aktuellere Informationen finden Sie im Tool [Search Grounding](https://ai.google.dev/gemini-api/docs/google-search?hl=de).
2. **What are the context window limits?** Gemini 3-Modelle unterstützen ein Eingabekontextfenster von 1 Million Tokens und bis zu 64.000 Tokens für die Ausgabe.
3. **Gibt es eine kostenlose Stufe für Gemini 3?** Für Gemini 3 Flash
   `gemini-3-flash-preview` und 3.1 Flash-Lite `gemini-3.1-flash-lite` gibt es kostenlose Stufen in der Gemini API. Sie können Gemini 3.1 Pro und 3 Flash kostenlos in Google AI Studio testen. Für `gemini-3.1-pro-preview` in der Gemini API ist jedoch keine kostenlose Stufe verfügbar.
4. **Funktioniert mein alter `thinking_budget`-Code weiterhin?** Ja, `thinking_budget` wird aus Gründen der Abwärtskompatibilität weiterhin unterstützt. Wir empfehlen jedoch, zu `thinking_level` zu migrieren, um eine besser vorhersagbare Leistung zu erzielen. Verwenden Sie nicht beide im selben Request.
5. **Unterstützt Gemini 3 die Batch API?** Ja, Gemini 3 unterstützt die [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de).
6. **Wird das Kontext-Caching unterstützt?** Ja, [Kontext-Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de) wird für Gemini 3 unterstützt.
7. **Welche Tools werden in Gemini 3 unterstützt?** Gemini 3 unterstützt die [Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de), [Fundierung mit Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de), die [Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de), die [Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) und den [URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de). Außerdem wird der Standard [Function Calling](https://ai.google.dev/gemini-api/docs/function-calling?hl=de) für Ihre eigenen benutzerdefinierten Tools und [in Kombination mit integrierten Tools](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de) unterstützt.
8. **Was ist `gemini-3.1-pro-preview-customtools`?** Wenn Sie `gemini-3.1-pro-preview` verwenden und das Modell Ihre benutzerdefinierten Tools zugunsten von Bash-Befehlen ignoriert, versuchen Sie es stattdessen mit dem Modell `gemini-3.1-pro-preview-customtools`. [Weitere Informationen](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=de#gemini-31-pro-preview-customtools)

## Nächste Schritte

- [Gemini 3 Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=de#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D)
- Weitere Informationen finden Sie im entsprechenden Cookbook-Leitfaden zu [Denkprozessebenen](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=de#gemini3) und zur Migration vom Budget für Denkprozesse zu Denkprozessebenen.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-04 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-04 (UTC)."],[],[]]
