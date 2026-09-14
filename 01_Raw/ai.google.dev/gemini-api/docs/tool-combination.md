---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=de
fetched_at: 2026-09-14T05:45:19.485510+00:00
title: "Integrierte Tools und Funktionsaufrufe kombinieren \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Integrierte Tools und Funktionsaufrufe kombinieren

Mit Gemini können Sie die Kombination von [integrierten Tools](https://ai.google.dev/gemini-api/docs/tools?hl=de) wie `google_search` und [Funktionsaufrufen](https://ai.google.dev/gemini-api/docs/function-calling?hl=de) (*benutzerdefinierte Tools* genannt) in einer einzigen Interaktion kombinieren, indem der Kontextverlauf von Toolaufrufen beibehalten und verfügbar gemacht wird. Kombinationen aus integrierten und benutzerdefinierten Tools ermöglichen komplexe, agentenbasierte Arbeitsabläufe, bei denen sich das Modell beispielsweise auf Echtzeit-Webdaten stützen kann, bevor es Ihre spezifische Geschäftslogik aufruft.

Hier ist ein Beispiel, das Kombinationen aus integrierten und benutzerdefinierten Tools mit `google_search` und einer benutzerdefinierten Funktion `getWeather` ermöglicht:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

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

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "model": "gemini-3.6-flash",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }
  ]
}'
```

## Funktionsweise

Gemini 3-Modelle verwenden die *Toolkontextweitergabe* , um Kombinationen aus integrierten und benutzerdefinierten Tools zu ermöglichen. Durch die Toolkontextweitergabe kann der Kontext von integrierten Tools beibehalten und verfügbar gemacht und mit benutzerdefinierten Tools in derselben Interaktion geteilt werden.

### Toolkombination aktivieren

- Fügen Sie die [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=de#function-declarations) zusammen
  mit den integrierten Tools ein, die Sie verwenden möchten, um das Kombinationsverhalten auszulösen.

### Von der API zurückgegebene Schritte

In einer Interaktionsantwort gibt die API separate Schritte für Aufrufe von integrierten Tools und Aufrufe von Funktionen (benutzerdefinierten Tools) zurück:

- **Schritte für integrierte Tools**: Diese werden von der API automatisch verwaltet, wobei der Kontext über mehrere Züge hinweg beibehalten wird.
- **Schritte für Funktionsaufrufe**: Die API gibt `function_call` Schritte für Ihre
  benutzerdefinierten Funktionen zurück. Sie führen die Funktion aus und geben das Ergebnis zurück.

### Wichtige Felder in zurückgegebenen Schritten

Bestimmte Felder in den zurückgegebenen Schritten sind entscheidend, um den Toolkontext beizubehalten und Toolkombinationen zu ermöglichen:

- **`id`**: In den Schritten `function_call` und `function_response` enthalten. Eine eindeutige ID, die einen Aufruf seiner Antwort zuordnet.
- **`signature`**: In den Schritten `thought` sowie in allen Schritten für Toolaufrufe (z.B. `function_call`) und Ergebnisse (z.B. `function_response`) für Gemini 3-Modelle und höher enthalten. Dieser verschlüsselte Kontext ermöglicht die **Toolkontextweitergabe** über Interaktionen hinweg.

**Verwaltung dieser Felder** :

- **Zustandsbehafteter Modus (empfohlen)**: Wenn Sie `previous_interaction_id` verwenden, verarbeitet der Server automatisch die Felder `id` und `signature`.
- **Zustandsloser Modus**: Wenn Sie den Unterhaltungsverlauf manuell verwalten, müssen Sie sowohl das Feld `id` als auch das Feld `signature` in nachfolgenden Anfragen an das Modell zurückgeben, um die Authentizität zu bestätigen und den Kontext beizubehalten. Die offiziellen SDKs verarbeiten dies automatisch, wenn Sie das vollständige Antwortobjekt an den Verlauf zurückgeben.

### Toolspezifische Daten

Einige integrierte Tools geben für den Nutzer sichtbare Datenargumente zurück, die für den Tooltyp spezifisch sind.

| Tool | Für den Nutzer sichtbare Toolaufrufargumente (falls vorhanden) | Für den Nutzer sichtbare Toolantwort (falls vorhanden) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` URLs, die durchsucht werden sollen | `status`: Status der Suche `retrieved_url`: Durchsuchte URLs |
| **file\_search** | Keine | Keine |

## Tokens und Preise

Teile von Aufrufen integrierter Tools in Anfragen werden auf `prompt_token_count` angerechnet. Da diese Zwischenschritte für Tools jetzt sichtbar sind und an Sie zurückgegeben werden, sind sie Teil des Unterhaltungsverlaufs. Dies gilt nur für den
Fall von *Anfragen*, nicht für *Antworten*.

Das Tool Google Suche ist eine Ausnahme von dieser Regel. Google Suche verwendet bereits ein eigenes Preismodell auf Abfrageebene, sodass Tokens nicht doppelt berechnet werden (siehe die [Preisseite](https://ai.google.dev/gemini-api/docs/pricing?hl=de)).

Weitere Informationen finden Sie auf der Seite [Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=de).

## Beschränkungen

- Wenn die Toolkontextweitergabe aktiviert ist, wird standardmäßig der Modus `validated` verwendet (`auto` wird nicht unterstützt).
- Integrierte Tools wie `google_search` verwenden Informationen zum Standort und zur aktuellen Uhrzeit. Wenn Ihre `system_instruction` oder `function_declaration.description` widersprüchliche Standort- und Zeitinformationen enthält, funktioniert die Toolkombination möglicherweise nicht richtig.

## Unterstützte Tools

Die standardmäßige Toolkontextweitergabe gilt für serverseitige (integrierte) Tools.
Die Codeausführung ist ebenfalls ein serverseitiges Tool, hat aber eine eigene integrierte Lösung für die Kontextweitergabe. Die Computernutzung und der Funktionsaufruf sind clientseitige Tools und haben ebenfalls integrierte Lösungen für die Kontextweitergabe.

| Tool | Ausführungsseite | Unterstützung der Kontextweitergabe |
| --- | --- | --- |
| [Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de) | Serverseitig | Unterstützt |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de) | Serverseitig | Unterstützt |
| [URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de) | Serverseitig | Unterstützt |
| [Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de) | Serverseitig | Unterstützt |
| [Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) | Serverseitig | Unterstützt (integriert, verwendet die Schritte `code_execution` und `code_execution_result`) |
| [Computernutzung](https://ai.google.dev/gemini-api/docs/computer-use?hl=de) | Clientseitig | Unterstützt (integriert, verwendet die Schritte `function_call` und `function_response`) |
| [Benutzerdefinierte Funktionen](https://ai.google.dev/gemini-api/docs/function-calling?hl=de) | Clientseitig | Unterstützt (integriert, verwendet die Schritte `function_call` und `function_response`) |

## Nächste Schritte

- Weitere Informationen zum [Funktionsaufruf](https://ai.google.dev/gemini-api/docs/function-calling?hl=de) in der Gemini API.
- Unterstützte Tools:
  - [Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de)
  - [URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de)
  - [Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-12 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-12 (UTC)."],[],[]]
