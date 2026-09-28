---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=de
fetched_at: 2026-09-28T06:32:26.245878+00:00
title: "Neueste Gemini-Modelle verwenden \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs/generate-content?hl=de)

Feedback geben

# Neueste Gemini-Modelle verwenden

[Diese Seite](#)
[Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=de)

Gemini 3.6 Flash (`gemini-3.6-flash`) und Gemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`) sind allgemein verfügbar und können in der Produktion eingesetzt werden.

- **Gemini 3.6 Flash**: Bessere Leistung bei komplexen agentischen und multimodalen Aufgaben bei geringerer Tokennutzung und zu einem niedrigeren Preis als Gemini 3.5 Flash.
- **Gemini 3.5 Flash-Lite**: Das schnellste und kostengünstigste Modell der 3.5-Familie. Übertrifft frühere Flash-Lite-Generationen bei der Ausführung mit hohem Durchsatz.

In diesem Leitfaden erfahren Sie, was es Neues in den einzelnen Modellen gibt, welche API-Änderungen sich auf Ihren Code auswirken und wie Sie migrieren.

### Gemini 3.6 Flash

1. Skill installieren:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Skill anwenden:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. Skill installieren:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Skill anwenden:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

## Neue Modelle

| Modell | Modell-ID | Standard-Denkstufe | Preise | Beschreibung |
| --- | --- | --- | --- | --- |
| Gemini 3.6 Flash | `gemini-3.6-flash` | `medium` | 1,50 $ pro 1 Mio.Eingabetokens und 7,50 $ pro 1 Mio.Ausgabetokens | Bietet ein ausgewogenes Verhältnis zwischen Geschwindigkeit und Intelligenz für agentische und multimodale Aufgaben. |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | `minimal` | 0,30 $ pro 1 Mio.Eingabetokens und 2,50 $ pro 1 Mio.Ausgabetokens | Das schnellste und kostengünstigste Modell der 3.5-Familie für die Ausführung mit hohem Durchsatz. |

Beide Modelle unterstützen das Kontextfenster mit 1 Mio. Tokens, maximal 64.000 Ausgabetokens, Denkprozesse und die gesamte Palette der integrierten Tools, einschließlich [der Computernutzung](https://ai.google.dev/gemini-api/docs/computer-use?hl=de).

Die vollständigen Spezifikationen finden Sie auf den Modellseiten:

- [Gemini 3.6 Flash-Modellseite](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=de)
- [Gemini 3.5 Flash-Lite-Modellseite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=de)

Ausführliche Informationen zu den Preisen finden Sie auf der [Preisseite](https://ai.google.dev/gemini-api/docs/pricing?hl=de).

## Kurzanleitung

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Write a three.js script that renders an interactive 3D robot.",
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
    contents: "Write a three.js script that renders an interactive 3D robot.",
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
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders an interactive 3D robot."}]
    }]
  }'
```

## Neuerungen in Gemini 3.6 Flash

- **Weniger Tokens und weniger Turns**:Erledigt mehrstufige Workflows mit weniger Denkprozessen, Konversations-Turns und Tool-Aufrufen als Gemini 3.5. Außerdem wird die Spirale der Ausführungsschleife reduziert.
- **Verbesserte Codeerstellung**:Erstellt hochwertigeren, produktionsfertigen Code mit weniger unerwünschten Änderungen und weniger Debugging-Schleifen.
- **Bessere Befolgung von Anweisungen**: Reduziert unerwünschte Dateiänderungen bei Diagnoseaufgaben.
- **Starkes multimodales und räumliches Denken**:Verbesserte Leistung bei der Diagramminterpretation, der visuellen Blueprint-Konvertierung und der Erstellung von Web-Layouts mit mehreren Elementen.
- **Vorab-Programmierprüfung**:Führt häufiger Diagnose-Code-Skripts aus, bevor Änderungen vorgenommen werden, als Gemini 3.5 Flash. Dies verbessert die Genauigkeit bei komplexen Aufgaben, kann aber bei einfachen Frontend-Aufgaben zusätzliche explorative Schritte erfordern.
- **Unterstützung der Computernutzung**:Wird als natives Tool für die agentische UI-Automatisierung unterstützt.
- **UI-Stilpräferenz**: Erstellt besseren funktionalen Code, aber menschliche Tester bevorzugten frühere Modelle für visuelles Layout und Styling. Sie können dies durch explizite Designrichtlinien abmildern.
- **Standard-Denkaufwand (mittel)** : Verwendet dieselbe Standard-Denkstufe `medium` wie Gemini 3.5 Flash.
- **Niedrigere Preise**: Geringere Kosten für Ausgabetokens (7,50 $ pro 1 Mio. gegenüber 9,00 $ pro 1 Mio. für Gemini 3.5 Flash). Die Kosten für Eingabetokens bleiben bei 1,50 $ pro 1 Mio.

## Neuerungen in Gemini 3.5 Flash-Lite

- **Geringere Latenz bei der Aufgabenausführung**:Höchster Durchsatz in der 3.5-Familie für das Parsen großer Datenmengen und die Dokumentextraktion.
- **Verbesserte Denk- und multimodale Leistung**:Starker Migrationspfad von Gemini 2.5 Flash mit höheren Werten bei Denkaufgaben wie HLE (18,0% gegenüber 11,0%) und multimodalen Benchmarks wie CharXIV (74,5% gegenüber 63,7%).
- **Orchestrierung von Sub-Agenten und Tool-Zuverlässigkeit**:Verbessert die Zuverlässigkeit der Tool-Ausführung für Code-Ausführung, Suche und MCP-Workflows. Erhöhen Sie die Denkstufe für die autonome Planung und komplexe Sub-Agenten-Aufgaben.
- **Verbessertes Dokumentverständnis**:Verbessert die Genauigkeit beim Parsen von Dokumenten und bei der Extraktion strukturierter Daten. Je nach Komplexität des Dokuments können Sie sowohl die minimale als auch die hohe Denkstufe verwenden.
- **Interaktive Webprogrammierung und Verarbeitung von Tabellendaten**:Erbringt eine starke Leistung bei der Frontend-JavaScript- und Tabellendatenverarbeitung durch Planung über eine einfache Codeausführung.
- **Chatbot- und Persona-Persistenz**:Bessere Befolgung von Anweisungen in Mehrfachdialogen und Persona-Konsistenz als bei Gemini 3.1 Flash-Lite.
- **Unterstützung der Computernutzung**:Wird als natives Tool für die agentische UI-Automatisierung unterstützt.

## Das richtige Flash- oder Flash-Lite-Modell auswählen

In dieser Tabelle können Sie das richtige Modell und den richtigen Migrationspfad für Ihre Arbeitslasten auswählen.

Bei beiden Modellen müssen die veralteten Parameter für die Stichprobenerhebung (`temperature`, `top_p`, `top_k`) und die vorab ausgefüllten Modell-Turns entfernt werden. Weitere Informationen finden Sie unter [API-Änderungen](#api-changes-and-parameter-updates).

| Modell | Primäre Anwendungsfälle | Empfohlenes Migrationsziel |
| --- | --- | --- |
| **Gemini 3.6 Flash** `gemini-3.6-flash` | Codeerstellung, räumliches/multimodales Denken, mehrstufige agentische Workflows | **Gemini 3.5 Flash**, **Gemini 3 Flash (Vorschau)** oder **Gemini 3.1 Pro** |
| **Gemini 3.5 Flash-Lite**  `gemini-3.5-flash-lite` | Autonome Sub-Agenten-Ausführung, Analyse großer Datenmengen und Dokumentextraktion, strukturiertes JSON-Parsing | **Gemini 3.1 Flash-Lite** oder **Gemini 2.5 Flash** |

## Aktualisierter Antigravity-Agent

Aufgrund seiner verbesserten Leistung ist Gemini 3.6 Flash jetzt das neue Standardmodell für den [Antigravity-Agenten](https://ai.google.dev/gemini-api/docs/antigravity-agentn?hl=de) in Verwaltete KI-Agenten. Dies kann durch Festlegen eines neuen Felds in der API geändert werden.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## API-Änderungen und Parameteraktualisierungen

Ab Gemini 3.6 Flash und Gemini 3.5 Flash-Lite gelten die folgenden API-Änderungen für diese Modelle und alle zukünftigen Gemini-Modellversionen.

- **Veraltete Parameter für die Stichprobenerhebung**: `temperature`, `top_p` und `top_k` sind veraltet. Die API ignoriert diese Parameter und gibt in zukünftigen Modellgenerationen einen Fehler zurück.
- **Validierung vorab ausgefüllter Modell-Turns**: Das Vorab-Ausfüllen von Modell-Turns wird nicht mehr unterstützt. Wenn der letzte nicht leere Turn in der Anfrage ein `model`-Turn ist, gibt die API einen `400`-Fehler zurück.

Im Folgenden finden Sie detaillierte Erklärungen und Codebeispiele für jede API-Änderung.

### 1. Veraltete Parameter für die Stichprobenerhebung (`temperature`, `top_p`, `top_k`)

`temperature`, `top_p` und `top_k` sind veraltet und werden ignoriert. In zukünftigen Modellgenerationen führt die Angabe dieser Parameter zu einem HTTP 400-Fehler. **Entfernen Sie diese Parameter aus allen Anfragen.**

```
# ⚠️ Remove these parameters (deprecated)
generation_config = {
     "temperature": 0.7,
     "top_p": 0.9,
     "top_k": 40,
}
```

Um die Deterministik zu verbessern, definieren Sie eine Systemanweisung mit expliziten Regeln für Ihren Anwendungsfall.

### 2. Validierung vorab ausgefüllter Modell-Turns

API-Anfragen, die mit einem nicht leeren Turn der Modellrolle enden, sind nicht zulässig und geben einen **HTTP 400-Fehler** zurück.

#### ⚠️ Vermeiden

In Legacy-`generateContent`- oder Raw-REST-Nutzlasten ist das Beenden mit einem Turn der Modellrolle jetzt nicht mehr zulässig:

```
/* ❌ DO NOT: End payload contents with a 'model' role turn */
{
  "contents": [
    {"role": "user", "parts": [{"text": "Translate 'Hello world' to Spanish."}]},
    {"role": "model", "parts": [{"text": "Translation:"}]}  /* ❌ Returns error */
  ]
}
```

#### ✅ Empfohlene Migration

Wenn Ihre Anwendung zuvor einen Modell-Turn vorab ausgefüllt hat, um Präambeln zu unterdrücken oder die JSON-Formatierung zu erzwingen, verwenden Sie stattdessen `system_instruction` oder [strukturierte Ausgaben](https://ai.google.dev/gemini-api/docs/structured-output?hl=de).

```
# ✅ RECOMMENDED: Use system_instruction to specify output format
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Translate 'Hello world' to Spanish.",
    config={"system_instruction": "Output only the translation without introductory text."},
)
```

## Checkliste für die Migration

### Gemini 3.6 Flash

1. Skill installieren:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Skill anwenden:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. Skill installieren:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Skill anwenden:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

### Zu Gemini 3.6 Flash migrieren

- **Modell-ID aktualisieren**:Ändern Sie den String des Zielmodells in `gemini-3.6-flash`.
- **Veraltete Parameter für die Stichprobenerhebung entfernen:**
  - Entfernen Sie `temperature`, `top_p` und `top_k` aus den Erstellungskonfigurationen.
  - Ersetzen Sie `thinking_budget` durch die String-Enum `thinking_level`, die auf `"medium"` oder `"high"` festgelegt ist.
  - Entfernen Sie `candidate_count` (wird in Gemini 3.x nicht unterstützt).
- **Regeln für die Turn-Validierung erzwingen:**
  - Entfernen Sie vorab ausgefüllte Modell-Turns.
  - Achten Sie darauf, dass der letzte Nutzer-Turn nicht leeren Text enthält.
- **Funktionsaufrufe prüfen**
  - Achten Sie darauf, dass alle `FunctionResponse`-Objekte `call_id` und `name` enthalten.
  - Platzieren Sie multimodale Assets in der Antwortnutzlast.
  - Formatieren Sie Inline-Anweisungen mit `\\n\\n`.
  - Wenn `Malformed_Function_Call` Fehler im Zusammenhang mit Text vor dem Tool auftreten, finden Sie unter [Problemumgehungen für Anforderungen an Text vor dem Tool](https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=de#workarounds-for-pre-tool-text-requirements) weitere Informationen.
- **Grundlegende Anforderungen für Gemini 3.x**:Informationen zu SDK-Updates und zur Beibehaltung der Denk-Signatur finden Sie in der [Checkliste für die Migration zu Gemini 3.5](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=de#migration).

### Zu Gemini 3.5 Flash-Lite migrieren

- **Modell-ID aktualisieren**:Ändern Sie den String des Zielmodells in `gemini-3.5-flash-lite`.
- **Denkaufwand konfigurieren**
  - Für die Extraktion, das Routing oder die Klassifizierung großer Datenmengen: Lassen Sie `thinking_level` auf `"minimal"` (Standard) eingestellt, um den Durchsatz zu maximieren.
  - Für autonome Sub-Agenten mit Tool-Aufrufen, Code-Ausführung oder mehrstufiger Problemlösung: Legen Sie `thinking_level` auf `"medium"` oder `"high"` fest, um eine vorzeitige Beendigung des Tools zu verhindern.
- **Veraltete Parameter entfernen und Funktionsaufrufe validieren**:Wenden Sie die [gleichen Regeln wie für Gemini 3.6 Flash an](#migrate-to-gemini-3-6-flash).
- **Grundlegende Anforderungen für Gemini 3.x**:Informationen finden Sie in der [Checkliste für die Migration zu Gemini 3.5](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=de#migration).

## Nächste Schritte

- API-Spezifikationen in der [Modellübersicht](https://ai.google.dev/gemini-api/docs/models?hl=de) ansehen
- Informationen zur Orchestrierung mehrerer Agenten im [Leitfaden zur Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=de)
- Prompts in [Google AI Studio](https://aistudio.google.com/?hl=de) testen und optimieren

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-12 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-12 (UTC)."],[],[]]
