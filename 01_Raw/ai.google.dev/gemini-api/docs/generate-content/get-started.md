---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de
fetched_at: 2026-10-19T05:52:36.100573+00:00
title: "Erste Schritte \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs/generate-content?hl=de)

Feedback geben

# Erste Schritte

In dieser Anleitung erfahren Sie, wie Sie die Legacy-**generateContent** verwenden. Für neue Projekte und Anwendungen empfehlen wir dringend, stattdessen die neue **Interactions API** zu verwenden. Sie ist die einfachste und beste Möglichkeit, mit Gemini-Modellen und -Agenten zu arbeiten.

In dieser Kurzanleitung erfahren Sie, wie Sie unsere
[Bibliotheken](https://ai.google.dev/gemini-api/docs/libraries?hl=de) installieren, Ihre erste Anfrage senden, Antworten streamen, Unterhaltungen über mehrere Themen erstellen und Tools mit der Standardmethode
`generateContent` verwenden.

## API-Schlüssel anfordern

Wenn Sie die Gemini API verwenden möchten, benötigen Sie einen API-Schlüssel, um Ihre Anfragen zu authentifizieren, Sicherheitslimits durchzusetzen und die Nutzung für Ihr Konto zu verfolgen.

- Google AI Studio erstellt automatisch ein Projekt und einen API-Schlüssel für neue Nutzer.
  Sie können ihn auf der Seite „[API-Schlüssel](https://aistudio.google.com/api-keys?hl=de)“ kopieren.
- Wenn Sie einen neuen Schlüssel benötigen, klicken Sie in AI Studio auf **API-Schlüssel erstellen** und folgen Sie der Anleitung, um ein neues Schlüssel-Projekt-Paar hinzuzufügen.

[Gemini API-Schlüssel erstellen](https://aistudio.google.com/apikey?hl=de)

Legen Sie Ihren Schlüssel als Umgebungsvariable fest:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### Auf die kostenpflichtige Stufe upgraden

Wenn Sie auf die kostenpflichtige Stufe upgraden, werden Ihre Ratenlimits erhöht. Außerdem müssen Sie die Cloud-Abrechnung einrichten.

- Klicken Sie auf den AI Studio
  [API-Schlüssel](https://aistudio.google.com/api-keys?hl=de) oder
  [Projekt](https://aistudio.google.com/projects?hl=de)-Seiten auf **Abrechnung einrichten**.
- Folgen Sie der Anleitung im Dialogfeld „Cloud-Abrechnung“, um ein Rechnungskonto zu erstellen oder zu verknüpfen, eine Zahlungsmethode hinzuzufügen und mindestens 10 $ (oder den entsprechenden Betrag in Ihrer Währung) an kostenpflichtigen Guthaben im Voraus zu bezahlen.
- Ihre API-Nutzung können Sie in [Google AI Studio](https://aistudio.google.com/usage?hl=de)
  unter **Dashboard** > **Nutzung** einsehen.

Weitere Informationen finden Sie auf der [Abrechnungsseite](https://ai.google.dev/gemini-api/docs/billing?hl=de).

## Google GenAI SDK installieren

### Python

Installieren Sie mit [Python 3.9 oder höher](https://www.python.org/downloads/) das
[`google-genai` Paket](https://pypi.org/project/google-genai/)
mit dem folgenden
[pip-Befehl](https://packaging.python.org/en/latest/tutorials/installing-packages/):

```
pip install -q -U google-genai
```

### JavaScript

Installieren Sie mit [Node.js Version 18 oder höher](https://nodejs.org/en/download/package-manager)
das
[Google Gen AI SDK für TypeScript und JavaScript](https://www.npmjs.com/package/@google/genai)
mit dem folgenden
[npm-Befehl](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm):

```
npm install @google/genai
```

## Text generieren

Verwenden Sie die `models.generate_content` Methode, um
[eine Textantwort zu generieren](https://ai.google.dev/gemini-api/docs/text-generation?hl=de).

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain how AI works in a few words"
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
    contents: "Explain how AI works in a few words",
  });

  console.log(response.text);
}

main();
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
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## Antworten streamen

Standardmäßig gibt das Modell erst dann eine Antwort zurück, wenn der gesamte Generierungsprozess abgeschlossen ist. Für eine schnellere und interaktivere Nutzung können Sie
[die Antwort](https://ai.google.dev/gemini-api/docs/text-generation?hl=de#stream) Teile streamen, sobald sie
generiert werden.

### Python

```
response = client.models.generate_content_stream(
    model="gemini-3.6-flash",
    contents="Explain how AI works in detail"
)

for chunk in response:
    print(chunk.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const responseStream = await ai.models.generateContentStream({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in detail",
  });

  for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in detail"
          }
        ]
      }
    ]
  }'
```

## Unterhaltungen über mehrere Themen

Für Unterhaltungen über mehrere Themen bieten die SDKs einen zustandsbehafteten `chats` Helfer, mit dem Sie eine [Unterhaltung über mehrere Themen erstellen können](https://ai.google.dev/gemini-api/docs/text-generation?hl=de#chat), bei der der Unterhaltungsverlauf automatisch verwaltet wird.

### Python

```
chat = client.chats.create(model="gemini-3.6-flash")

response1 = chat.send_message("I have 2 dogs in my house.")
print("Response 1:", response1.text)

response2 = chat.send_message("How many paws are in my house?")
print("Response 2:", response2.text)
```

### JavaScript

```
async function main() {
  const chat = ai.chats.create({ model: "gemini-3.6-flash" });

  let response = await chat.sendMessage({ message: "I have 2 dogs in my house." });
  console.log("Response 1:", response.text);

  response = await chat.sendMessage({ message: "How many paws are in my house?" });
  console.log("Response 2:", response.text);
}

main();
```

### REST

```
# REST is stateless. You must pass the full conversation history in the request.
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "I have 2 dogs in my house."}]
      },
      {
        "role": "model",
        "parts": [{"text": "That is nice! Two dogs mean you have plenty of company."}]
      },
      {
        "role": "user",
        "parts": [{"text": "How many paws are in my house?"}]
      }
    ]
  }'
```

## Tools verwenden

Erweitern Sie die Funktionen des Modells, indem Sie
[Antworten mit der Google Suche fundieren](https://ai.google.dev/gemini-api/docs/google-search?hl=de)
um auf Web-Inhalte in Echtzeit zuzugreifen. Das Modell entscheidet automatisch, wann eine Suche durchgeführt werden soll, führt die Abfragen aus und erstellt eine Antwort.

### Python

```
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Who won the euro 2024?",
    config=config
)

print(response.text)

metadata = response.candidates[0].grounding_metadata
if metadata.web_search_queries:
    print("\nSearch queries executed:")
    for query in metadata.web_search_queries:
        print(f" - {query}")

if metadata.grounding_chunks:
    print("\nSources:")
    for chunk in metadata.grounding_chunks:
        print(f" - [{chunk.web.title}]({chunk.web.uri})")
```

### JavaScript

```
async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Who won the euro 2024?",
    config: {
      tools: [{ googleSearch: {} }]
    }
  });

  console.log(response.text);

  const metadata = response.candidates[0]?.groundingMetadata;
  if (metadata?.webSearchQueries) {
    console.log("\nSearch queries executed:");
    for (const query of metadata.webSearchQueries) {
      console.log(` - ${query}`);
    }
  }
  if (metadata?.groundingChunks) {
    console.log("\nSources:");
    for (const chunk of metadata.groundingChunks) {
      console.log(` - [${chunk.web.title}](${chunk.web.uri})`);
    }
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

Die Gemini API unterstützt auch andere integrierte Tools:

- **[Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de)**:
  Das Modell kann Python-Code schreiben und ausführen, um komplexe mathematische Probleme zu lösen.
- **[URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de)**: Sie können Antworten auf bestimmte von Ihnen angegebene Webseiten-URLs fundieren.
- **[Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de)**: Sie können Dateien hochladen und Antworten mithilfe der semantischen Suche auf deren Inhalt fundieren.
- **[Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de)**: Sie können Antworten auf Standortdaten fundieren und nach Orten, Wegbeschreibungen und
  Karten suchen.
- **[Computernutzung](https://ai.google.dev/gemini-api/docs/computer-use?hl=de)**: Das
  Modell kann mit einem virtuellen Computerbildschirm, einer virtuellen Tastatur und einer virtuellen Maus interagieren, um
  Aufgaben auszuführen.

## Benutzerdefinierte Funktionen aufrufen

Mit **[Funktionsaufrufen](https://ai.google.dev/gemini-api/docs/function-calling?hl=de)** können Sie
Modelle mit Ihren benutzerdefinierten Tools und APIs verbinden. Das Modell bestimmt, wann Ihre Funktion aufgerufen werden soll, und gibt in der Antwort einen `functionCall` zurück, den Ihre Anwendung ausführen kann.

In diesem Beispiel wird eine Mock-Temperaturfunktion deklariert und geprüft, ob das Modell sie aufrufen möchte.

### Python

```
from google import genai
from google.genai import types

weather_function = {
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

tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

contents = ["What's the temperature in London?"]

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=contents,
    config=config,
)

part = response.candidates[0].content.parts[0]
if part.function_call:
    fc = part.function_call
    print(f"Model requested function: {fc.name} with args {fc.args}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    contents.append(response.candidates[0].content)

    fn_response_part = types.Part.from_function_response(
        name=fc.name,
        response=mock_result,
        id=fc.id
    )
    contents.append(types.Content(role="user", parts=[fn_response_part]))

    final_response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=contents,
        config=config,
    )
    print("Final Response:", final_response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

async function main() {
  const weatherFunction = {
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: Type.OBJECT,
      properties: {
        location: {
          type: Type.STRING,
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const contents = [{
    role: 'user',
    parts: [{ text: "What's the temperature in London?" }]
  }];

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: contents,
    config: {
      tools: [{ functionDeclarations: [weatherFunction] }],
    },
  });

  if (response.functionCalls && response.functionCalls.length > 0) {
    const fc = response.functionCalls[0];
    console.log(`Model requested function: ${fc.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    contents.push(response.candidates[0].content);

    contents.push({
      role: 'user',
      parts: [{
        functionResponse: {
          name: fc.name,
          response: mockResult,
          id: fc.id
        }
      }]
    });

    const finalResponse = await ai.models.generateContent({
      model: 'gemini-3.6-flash',
      contents: contents,
      config: {
        tools: [{ functionDeclarations: [weatherFunction] }],
      },
    });
    console.log("Final Response:", finalResponse.text);
  }
}

main();
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
        "role": "user",
        "parts": [{"text": "What'\''s the temperature in London?"}]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city name, e.g. San Francisco"
                }
              },
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

## Nächste Schritte

Nachdem Sie nun mit der Gemini API vertraut sind, können Sie sich die folgenden Anleitungen ansehen, um komplexere Anwendungen zu erstellen:

- [Textgenerierung](https://ai.google.dev/gemini-api/docs/text-generation?hl=de)
- [Bildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de)
- [Bildverständnis](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de)
- [Überlegung](https://ai.google.dev/gemini-api/docs/thinking?hl=de)
- [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de)
- [Fundierung mit der Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de)
- [Langer Kontext](https://ai.google.dev/gemini-api/docs/long-context?hl=de)
- [Einbettungen](https://ai.google.dev/gemini-api/docs/embeddings?hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-12 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-12 (UTC)."],[],[]]
