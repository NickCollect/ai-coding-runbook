---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=de
fetched_at: 2026-09-07T05:50:25.876361+00:00
title: "Neu in Gemini\u00a03.8 Flash \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Neu in Gemini 3.8 Flash

[Alle Modelle ansehen](https://ai.google.dev/gemini-api/docs/models?hl=de)

Gemini 3.8 Flash (`gemini-3.8-flash`) ist allgemein verfügbar und kann in der Produktion eingesetzt werden. Es ist unser intelligentestes Flash-Modell, das für langfristige Softwareentwicklung, autonome Agenten und komplexe Unternehmensworkflows entwickelt wurde.

In diesem Leitfaden erfahren Sie mehr über die Neuerungen in Gemini 3.8 Flash, API-Änderungen, Codebeispiele und Migrationsanleitungen.

## Neues Modell

| Modell | Modell-ID | Standard-Denkstufe | Preise | Beschreibung |
| --- | --- | --- | --- | --- |
| Gemini 3.8 Flash | `gemini-3.8-flash` | `medium` | 3.8 Flash ist bis zum Jahresende zum Einführungspreis von 0,75 $/1 Mio. Eingabetokens und 3,75 $/1 Mio. Ausgabetokens verfügbar. Weitere Informationen finden Sie unter [Preise](https://ai.google.dev/gemini-api/docs/pricing?hl=de). | Unser intelligentestes Flash-Modell, das für langfristige Softwareentwicklung, autonome Agenten und komplexe Unternehmensworkflows entwickelt wurde. |

Gemini 3.8 Flash unterstützt ein Kontextfenster von 1 Million Tokens, maximal 64.000 Ausgabetokens, anpassbare Denkstufen (`low`, `medium`, `high`) und dieselbe Suite integrierter Tools.

Die vollständigen Spezifikationen finden Sie auf der [Modellseite von Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=de). Einführungspreise finden Sie im [Abschnitt Preise](#pricing) unten oder auf der [Preisseite](https://ai.google.dev/gemini-api/docs/pricing?hl=de#gemini-3.8-flash).

## Kurzanleitung

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Write a three.js script that renders a realistic 3D black hole."
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Write a three.js script that renders a realistic 3D black hole.",
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders a realistic 3D black hole."}]
    }]
  }'
```

## Neuerungen in Gemini 3.8 Flash

- **Langfristige Softwareentwicklung**:Erzielt gute Ergebnisse bei realen Coding-Benchmarks, komplexem Refactoring mehrerer Dateien und deterministischer Toolausführung. Weitere Informationen finden Sie unter der [Bewertungsmethodik](https://deepmind.google/models/evals-methodology/gemini-3-8-flash/?hl=de).
- **Autonome Agenten**:Ermöglicht das Erstellen robuster mehrstufiger Planungs- und Tool-Orchestrierungs-Workflows, wodurch fehlgeschlagene Schleifen und Fehler erheblich reduziert werden.
- **Komplexe Unternehmensworkflows**:Bietet überragende Genauigkeit, tiefes Schlussfolgern und hohe faktische Strenge bei anspruchsvollen Aufgaben in bestimmten Bereichen und großen Datenpipelines.
- **Standardmodell für verwaltete KI-Agenten**: Der Standardagent für verwaltete KI-Agenten, der [Antigravity-Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=de), verwendet jetzt Gemini 3.8 Flash. Das [Antigravity SDK](https://antigravity.google/docs/sdk/overview/?hl=de) verwendet standardmäßig auch Gemini 3.8 Flash.
- **Einführungspreise**:Gemini 3.8 Flash ist bis zum 31. Dezember 2026 zum Einführungspreis von 0,75 $/1 Mio. Eingabetokens und 3,75 $/1 Mio. Ausgabetokens verfügbar. Die Standardpreise von 1,50 $/1 Mio. Eingabetokens und 7,50 $/1 Mio. Ausgabetokens gelten ab dem 1. Januar 2027.

Gemini 3.8 Flash kann für längere und komplexere Aufgaben mehr Tokens verwenden. Um bei schwierigen, mehrstufigen Zielen qualitativ hochwertigere Ergebnisse zu erzielen, führt das Modell kleinere Schlussfolgerungsschritte aus, ruft Tools iterativ auf und überprüft seine Arbeit während des Prozesses. Nicht für jeden Workflow ist diese Überprüfungsebene erforderlich. Bei alltäglichen Aufgaben können Sie den [Aufwand für die Schlussfolgerung](#understanding-reasoning-levels) reduzieren, um den Tokenverbrauch zu senken. Alternativ wird Gemini 3.7 Flash weiterhin vollständig unterstützt.

## Informationen zu den Denkstufen

Mit Gemini 3.8 Flash können Sie die Latenz und Intelligenz flexibel steuern, indem Sie die Denkstufe des Modells anpassen:

- **Geringer Denkaufwand**: Reduziert die Antwortzeit für latenzkritische Aufgaben wie Incident Response Pipelines, Echtzeit-Chats, das Verfassen von Entwürfen und schnelle Datenanalysen.
- **Mittel (Standard)** : Beste Qualität für die meisten Aufgaben. Empfohlen für komplexe Code- und agentische Anwendungsfälle, da eine höhere Genauigkeit beim ersten Durchlauf erzielt wird.
- **Hoher Denkaufwand**: Maximiert die Schlussfolgerungs- und Tool-Orchestrierungsfunktionen des Modells. Optimal für tiefes Schlussfolgern, Mathematik und schwierige mehrstufige Aufgaben.

Im folgenden Beispiel wird `thinking_level` für eine komplexe Codeanalyseanfrage auf `medium` gesetzt:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="medium"  # Balanced reasoning effort for complex tasks
        ),
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
  config: {
    thinkingConfig: {
      thinkingLevel: "medium", // Balanced reasoning effort for complex tasks
    },
  },
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely."}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "medium"
      }
    }
  }'
```

## Aktualisierter Antigravity-Agent

## Checkliste für die Migration

```
  `/gemini-api-dev migrate my app to Gemini 3.8 Flash`
```

### Zu gemini-3.8-flash migrieren

- **Modell-ID aktualisieren**:Ändern Sie den String des Zielmodells in `gemini-3.8-flash`.
- **Veraltete Stichprobenparameter entfernen:**
  - Entfernen Sie `temperature`, `top_p` und `top_k` aus den Generierungskonfigurationen.
  - Ersetzen Sie `thinking_budget` durch die String-Enum `thinking_level`. Beachten Sie, dass `minimal` in 3.8 Flash nicht unterstützt wird.
  - Entfernen Sie `candidate_count` (wird in Gemini 3 und höher nicht unterstützt).
- **Regeln zur Zugvalidierung erzwingen:**
  - Entfernen Sie vorab ausgefüllte Modellzüge.
  - Achten Sie darauf, dass der letzte Zug des Nutzers nicht leeren Text enthält.
- **Funktionsaufrufe prüfen**
  - Platzieren Sie multimodale Assets in der Antwortnutzlast.
  - Formatieren Sie Inline-Anleitungen mit `\n\n`.
  - Wenn `Malformed_Function_Call` Fehler im Zusammenhang mit Text vor dem Tool auftreten, finden Sie unter [Workarounds für Anforderungen an Text vor dem Tool](https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=de#workarounds-for-pre-tool-text-requirements) weitere Informationen.
  - Nur bei Verwendung der generateContent API: Achten Sie darauf, dass alle `FunctionResponse`-Objekte `call_id` und `name` enthalten.
- **Gemini 3-Anforderungen als Baseline**:Informationen zu SDK-Updates und zur Beibehaltung der Gedanken-Signatur finden Sie in der [Checkliste für die Migration zu Gemini 3.5](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=de#migration).

## Preise

Bis zum 31. Dezember 2026 gelten für Gemini 3.8 Flash, Gemini 3.7 Flash und Gemini 3.6 Flash Einführungspreise in Google AI Studio und der Gemini Enterprise Agent Platform. Die Standardpreise gelten ab dem 1. Januar 2027. Die vollständigen Preisstufen finden Sie auf der [Preisseite](https://ai.google.dev/gemini-api/docs/pricing?hl=de#gemini-3.8-flash).

## Nächste Schritte

- API-Spezifikationen in der [Modellübersicht](https://ai.google.dev/gemini-api/docs/models?hl=de) ansehen
- Informationen zur Orchestrierung mehrerer Agenten in der [Übersicht zur Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de)
- Prompts in [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de) testen und optimieren

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-03 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-03 (UTC)."],[],[]]
