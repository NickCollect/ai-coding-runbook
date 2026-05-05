---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=de
fetched_at: 2026-05-05T19:49:25.694957+00:00
title: "Erl\u00e4uterung der API-Versionen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [API-Referenz](https://ai.google.dev/api?hl=de)

Feedback geben

# Erläuterung der API-Versionen

In diesem Dokument finden Sie einen allgemeinen Überblick über die Unterschiede zwischen den `v1`
und `v1beta` Versionen der Gemini API.

- **v1**: Stabile Version der API. Funktionen in der stabilen Version werden während der gesamten Lebensdauer der Hauptversion vollständig unterstützt. Bei grundlegenden Änderungen wird die nächste Hauptversion der API erstellt und die vorhandene Version nach einem angemessenen Zeitraum eingestellt.
  Nicht grundlegende Änderungen können an der API vorgenommen werden, ohne die Hauptversion zu ändern.
- **v1beta**: Diese Version enthält frühe Funktionen, die sich möglicherweise noch in der Entwicklung befinden und grundlegenden Änderungen unterliegen. Es gibt auch keine Garantie, dass die Funktionen in der Betaversion in die stabile Version übernommen werden. **Wenn Sie in Ihrer Produktionsumgebung Stabilität benötigen und keine grundlegenden Änderungen riskieren können, sollten Sie diese Version nicht in der Produktion verwenden.**

| Funktion | v1 | v1beta |
| --- | --- | --- |
| Inhalte generieren – Nur Texteingabe |  |  |
| Inhalte generieren – Text- und Bildeingabe |  |  |
| Inhalte generieren – Textausgabe |  |  |
| Inhalte generieren – Multi-Turn-Unterhaltungen (Chat) |  |  |
| Inhalte generieren – Funktionsaufrufe |  |  |
| Inhalte generieren – Streaming |  |  |
| Inhalte einbetten – Nur Texteingabe |  |  |
| Antwort generieren |  |  |
| Semantischer Retriever |  |  |
| Interactions API |  |  |

- – Unterstützt
- – Wird nie unterstützt

## API-Version in einem SDK konfigurieren

Die Gemini API SDKs verwenden standardmäßig `v1beta`. Sie können aber auch andere Versionen verwenden, indem Sie die API-Version wie im folgenden Codebeispiel gezeigt festlegen:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents="Explain how AI works",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1/models/gemini-3-flash-preview:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "Explain how AI works."}]
    }]
   }'
```

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-04-29 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-04-29 (UTC)."],[],[]]
