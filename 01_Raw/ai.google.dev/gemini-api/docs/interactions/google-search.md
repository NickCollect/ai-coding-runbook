---
source_url: https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=de
fetched_at: 2026-05-25T05:21:46.585957+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Fundierung mit der Google Suche

Die Fundierung mit der Google Suche verbindet das Gemini-Modell mit Web-Inhalten in Echtzeit und funktioniert mit allen verfügbaren Sprachen. So kann Gemini genauere Antworten geben und überprüfbare Quellen über den Wissensstand hinaus zitieren.

Mit der Fundierung können Sie Anwendungen erstellen, die Folgendes können:

- **Sachliche Richtigkeit erhöhen**:Reduzieren Sie Modellhalluzinationen, indem Sie Antworten auf realen Informationen basieren.
- **Auf Echtzeitinformationen zugreifen**:Beantworten Sie Fragen zu aktuellen Ereignissen und Themen.
- **Zitate angeben**:Bauen Sie Vertrauen bei Nutzern auf, indem Sie die Quellen für die Aussagen des Modells angeben.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## So funktioniert die Fundierung mit der Google Suche

Wenn Sie das Tool `google_search` aktivieren, verarbeitet das Modell den gesamten Workflow der Suche, Verarbeitung und Zitation von Informationen automatisch.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=de)

1. **Nutzer-Prompt**:Ihre Anwendung sendet einen Nutzer-Prompt an die Gemini API, wobei das Tool `google_search` aktiviert ist.
2. **Promptanalyse**:Das Modell analysiert den Prompt und ermittelt, ob eine Google Suche die Antwort verbessern kann.
3. **Google Suche**:Bei Bedarf generiert das Modell automatisch eine oder mehrere Suchanfragen und führt sie aus.
4. **Verarbeitung der Suchergebnisse**:Das Modell verarbeitet die Suchergebnisse, fasst die Informationen zusammen und formuliert eine Antwort.
5. **Fundierte Antwort**:Die API gibt eine endgültige, nutzerfreundliche Antwort zurück, die auf den Suchergebnissen basiert. Diese Antwort enthält die Textantwort des Modells mit Inline-`annotations`, die die Zitate enthalten, sowie die Schritte `google_search_call` und `google_search_result` mit den Suchanfragen und Suchvorschlägen.

## Antwort zur Fundierung verstehen

Wenn eine Antwort erfolgreich fundiert wurde, enthält die Textausgabe des Modells Inline-`annotations` direkt im Textinhaltsblock. Diese Annotationen enthalten Zitationsinformationen, die Teile der Antwort mit ihren Quellen verknüpfen.

```
{
  "steps": [
    {
      "type": "thought",
      "summary": [
        {
          "type": "text",
          "text": "The user is asking for the winner of Euro 2024. I need to search for the result of the Euro 2024 final."
        }
      ],
      "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0..."
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
          "search_suggestions": "<!-- HTML and CSS for the search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.aljazeera.com/sports/euro-2024-final",
              "title": "aljazeera.com",
              "start_index": 0,
              "end_index": 56
            },
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024/news/spain-wins-euro-2024",
              "title": "uefa.com",
              "start_index": 57,
              "end_index": 124
            }
          ]
        }
      ]
    }
  ]
}
```

Die wichtigsten Felder in der Antwort:

- `google_search_call` : Enthält die `queries`, die das Modell ausgeführt hat.
- `google_search_result` : Enthält `search_suggestions`, ein HTML-Snippet zum Rendern von Suchvorschlägen in Ihrer UI. Die vollständigen Nutzungsanforderungen sind
  in den [Nutzungsbedingungen](https://ai.google.dev/gemini-api/terms?hl=de#grounding-with-google-search) aufgeführt.
- `text` mit `annotations` : Die synthetisierte Antwort des Modells mit Inline-Zitaten. Jede `url_citation`-Annotation verknüpft ein Textsegment (definiert durch `start_index` und `end_index`) mit einer Quell-URL. Dies ist der Schlüssel zum Erstellen von Inline-Zitaten.

Die Fundierung mit der Google Suche kann auch in Kombination mit dem [URL
Kontexttool](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=de) verwendet werden, um Antworten sowohl auf
öffentlichen Webdaten als auch auf den von Ihnen angegebenen URLs zu fundieren.

## Quellen mit Inline-Zitaten angeben

Die API gibt Inline-`url_citation`-Annotationen für den Textinhaltsblock zurück, sodass Sie die vollständige Kontrolle darüber haben, wie Sie Quellen in Ihrer Benutzeroberfläche anzeigen.
Jede Annotation enthält `start_index` und `end_index`, um anzugeben, auf welchen Teil des Texts sie sich bezieht. So können Sie sie extrahieren und anzeigen.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nCitations:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            cited_text = content_block.text[annotation.start_index:annotation.end_index]
                            print(f"  [{annotation.title}]({annotation.url})")
                            print(f"    Cited text: \"{cited_text}\"")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
        if (contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              const citedText = contentBlock.text.slice(annotation.startIndex, annotation.endIndex);
              console.log(`  [${annotation.title}](${annotation.url})`);
              console.log(`    Cited text: "${citedText}"`);
            }
          }
        }
      }
    }
  }
}
```

Die Ausgabe zeigt den Text gefolgt von den Zitaten:

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## Preise

Wenn Sie die Fundierung mit der Google Suche mit Gemini 3 verwenden, wird Ihrem Projekt jede Suchanfrage in Rechnung gestellt, die das Modell ausführt. Wenn das Modell beschließt,
mehrere Suchanfragen auszuführen, um eine einzelne Anfrage zu beantworten (z. B.
die Suche nach `"UEFA Euro 2024 winner"` und `"Spain vs England Euro 2024 final
score"` im selben API-Aufruf), zählt dies als zwei kostenpflichtige Nutzungen des Tools
für diese Anfrage. Für Abrechnungszwecke werden leere Websuchanfragen bei der Zählung eindeutiger Anfragen ignoriert. Dieses Abrechnungsmodell gilt nur für Gemini 3-Modelle. Wenn Sie die Suchfundierung mit Gemini 2.5 oder älteren Modellen verwenden, wird Ihrem Projekt pro Prompt in Rechnung gestellt.

Ausführliche Preisinformationen finden Sie auf der Seite [Gemini API-Preise
page](https://ai.google.dev/gemini-api/docs/pricing?hl=de).

## Unterstützte Modelle

Die vollständigen Funktionen finden Sie auf der [Modell
übersichts](https://ai.google.dev/gemini-api/docs/models?hl=de)seite.

| Modell | Fundierung mit der Google Suche |
| --- | --- |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash Image (Vorabversion) | ✔️ |
| Gemini 3.1 Pro (Vorabversion) | ✔️ |
| Gemini 3 Pro Image (Vorabversion) | ✔️ |
| Gemini 3 Flash (Vorabversion) | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Unterstützte Toolkombinationen

Sie können die Fundierung mit der Google Suche mit anderen Tools wie
[der Codeausführung](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=de) und
[dem URL-Kontext](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=de) kombinieren, um komplexere
Anwendungsfälle zu ermöglichen.

Gemini 3-Modelle unterstützen die Kombination von integrierten Tools (z. B. Fundierung mit der Google Suche) mit benutzerdefinierten Tools (Funktionsaufrufe). Weitere Informationen finden Sie auf der
[Seite Toolkombinationen](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=de).

## Nächste Schritte

- Weitere Informationen zu anderen verfügbaren Tools wie [Funktionsaufrufen](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=de)
- Informationen zum Erweitern von Prompts mit bestimmten URLs mithilfe des [URL-Kontexttools](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-05-19 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-05-19 (UTC)."],[],[]]
