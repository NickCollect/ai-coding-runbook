---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/google-search?hl=de
fetched_at: 2026-07-20T04:48:42.916414+00:00
title: "Fundierung mit der Google Suche \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Fundierung mit der Google Suche

Durch die Fundierung mit der Google Suche wird das Gemini-Modell in Echtzeit mit Webinhalten verbunden und kann mit allen verfügbaren Sprachen genutzt werden. So kann Gemini genauere Antworten geben und überprüfbare Quellen zitieren, die über den Wissensstichtag des Modells hinausgehen.

Mit der Fundierung können Sie Anwendungen erstellen, die Folgendes können:

- **Sachliche Genauigkeit erhöhen**:Reduzieren Sie Modellhalluzinationen, indem Sie Antworten auf realen Informationen basieren.
- **Auf Echtzeitinformationen zugreifen**:Beantworten Sie Fragen zu aktuellen Ereignissen und Themen.
- **Zitate bereitstellen**:Bauen Sie Vertrauen bei den Nutzern auf, indem Sie die Quellen für die Aussagen des Modells angeben.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Who won the euro 2024?",
    config=config,
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const groundingTool = {
  googleSearch: {},
};

const config = {
  tools: [groundingTool],
};

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: "Who won the euro 2024?",
  config,
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

Weitere Informationen finden Sie im [Notebook zum Tool „Suche“](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=de).

## So funktioniert die Fundierung mit der Google Suche

Wenn Sie das Tool `google_search` aktivieren, verarbeitet das Modell den gesamten Workflow der Suche, Verarbeitung und Zitation von Informationen automatisch.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=de)

1. **Nutzer-Prompt**:Ihre Anwendung sendet einen Nutzer-Prompt an die Gemini API, wobei das Tool `google_search` aktiviert ist.
2. **Promptanalyse**:Das Modell analysiert den Prompt und ermittelt, ob eine Google Suche die Antwort verbessern kann.
3. **Google Suche**:Bei Bedarf generiert das Modell automatisch eine oder mehrere Suchanfragen und führt sie aus.
4. **Verarbeitung der Suchergebnisse**:Das Modell verarbeitet die Suchergebnisse, fasst die Informationen zusammen und formuliert eine Antwort.
5. **Fundierte Antwort**:Die API gibt eine endgültige, nutzerfreundliche Antwort zurück, die auf den Suchergebnissen basiert. Diese Antwort enthält die Textantwort des Modells und `groundingMetadata` mit den Suchanfragen, Webergebnissen und Zitaten.

## Informationen zur Fundierungsantwort

Wenn eine Antwort erfolgreich fundiert wurde, enthält sie das Feld `groundingMetadata`. Diese strukturierten Daten sind wichtig, um Aussagen zu überprüfen und eine umfassende Zitationsfunktion in Ihrer Anwendung zu erstellen.

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

Die Gemini API gibt die folgenden Informationen mit `groundingMetadata` zurück:

- `webSearchQueries` : Array der verwendeten Suchanfragen. Dies ist nützlich für das Debugging und um den Denkprozess des Modells zu verstehen.
- `searchEntryPoint` : Enthält das HTML und CSS, um die erforderlichen Suchvorschläge zu rendern. Die vollständigen Nutzungsanforderungen sind in den [Nutzungs
  bedingungen](https://ai.google.dev/gemini-api/terms?hl=de#grounding-with-google-search) aufgeführt.
- `groundingChunks` : Array von Objekten mit den Webquellen (`uri` und `title`).
- `groundingSupports` : Array von Chunks, um die Modellantwort `text` mit den Quellen in `groundingChunks` zu verknüpfen. Jeder Chunk verknüpft ein Textsegment (`segment`, definiert durch `startIndex` und `endIndex`) mit einem oder mehreren `groundingChunkIndices`. Dies ist der Schlüssel zum Erstellen von Inline-Zitaten.

Die Fundierung mit der Google Suche kann auch in Kombination mit dem [URL
Kontext-Tool](https://ai.google.dev/gemini-api/docs/url-context?hl=de) verwendet werden, um Antworten sowohl mit öffentlichen
Webdaten als auch mit den von Ihnen angegebenen URLs zu fundieren.

## Quellen mit Inline-Zitaten angeben

Die API gibt strukturierte Zitationsdaten zurück, sodass Sie die vollständige Kontrolle darüber haben, wie Sie Quellen in Ihrer Benutzeroberfläche anzeigen. Mit den Feldern `groundingSupports` und `groundingChunks` können Sie die Aussagen des Modells direkt mit ihren Quellen verknüpfen. Hier ist ein gängiges Muster für die Verarbeitung der Metadaten, um eine Antwort mit Inline-Zitaten zu erstellen, auf die geklickt werden kann.

### Python

```
def add_citations(response):
    text = response.text
    supports = response.candidates[0].grounding_metadata.grounding_supports
    chunks = response.candidates[0].grounding_metadata.grounding_chunks

    # Sort supports by end_index in descending order to avoid shifting issues when inserting.
    sorted_supports = sorted(supports, key=lambda s: s.segment.end_index, reverse=True)

    for support in sorted_supports:
        end_index = support.segment.end_index
        if support.grounding_chunk_indices:
            # Create citation string like [1](link1)[2](link2)
            citation_links = []
            for i in support.grounding_chunk_indices:
                if i < len(chunks):
                    uri = chunks[i].web.uri
                    citation_links.append(f"[{i + 1}]({uri})")

            citation_string = ", ".join(citation_links)
            text = text[:end_index] + citation_string + text[end_index:]

    return text

# Assuming response with grounding metadata
text_with_citations = add_citations(response)
print(text_with_citations)
```

### JavaScript

```
function addCitations(response) {
    let text = response.text;
    const supports = response.candidates[0]?.groundingMetadata?.groundingSupports;
    const chunks = response.candidates[0]?.groundingMetadata?.groundingChunks;

    // Sort supports by end_index in descending order to avoid shifting issues when inserting.
    const sortedSupports = [...supports].sort(
        (a, b) => (b.segment?.endIndex ?? 0) - (a.segment?.endIndex ?? 0),
    );

    for (const support of sortedSupports) {
        const endIndex = support.segment?.endIndex;
        if (endIndex === undefined || !support.groundingChunkIndices?.length) {
        continue;
        }

        const citationLinks = support.groundingChunkIndices
        .map(i => {
            const uri = chunks[i]?.web?.uri;
            if (uri) {
            return `[${i + 1}](${uri})`;
            }
            return null;
        })
        .filter(Boolean);

        if (citationLinks.length > 0) {
        const citationString = citationLinks.join(", ");
        text = text.slice(0, endIndex) + citationString + text.slice(endIndex);
        }
    }

    return text;
}

const textWithCitations = addCitations(response);
console.log(textWithCitations);
```

Die neue Antwort mit Inline-Zitaten sieht so aus:

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
```

## Preise

Wenn Sie die Fundierung mit der Google Suche mit Gemini 3 verwenden, wird Ihrem Projekt jede Suchanfrage in Rechnung gestellt, die das Modell ausführt. Wenn das Modell mehrere Suchanfragen ausführt, um einen einzelnen Prompt zu beantworten (z. B. die Suche nach `"UEFA Euro 2024 winner"` und `"Spain vs England Euro 2024 final
score"` im selben API-Aufruf), zählt dies als zwei kostenpflichtige Nutzungen des Tools für diese Anfrage. Für Abrechnungszwecke werden leere Websuchanfragen bei der Zählung eindeutiger Suchanfragen ignoriert. Dieses Abrechnungsmodell gilt nur für Gemini 3-Modelle. Wenn Sie die Suchfundierung mit Gemini 2.5 oder älteren Modellen verwenden, wird Ihrem Projekt pro Prompt eine Gebühr berechnet.

Ausführliche Preisinformationen finden Sie auf der Seite [Gemini API-Preise
page](https://ai.google.dev/gemini-api/docs/pricing?hl=de).

## Unterstützte Modelle

Eine vollständige Übersicht der Funktionen finden Sie auf der Seite [Modell
übersicht](https://ai.google.dev/gemini-api/docs/models?hl=de).

| Modell | Fundierung mit der Google Suche |
| --- | --- |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash Lite | ✔️ |
| Gemini 3.1 Flash Image Preview | ✔️ |
| Gemini 3.1 Pro (Vorabversion) | ✔️ |
| Gemini 3 Pro Image Preview | ✔️ |
| Gemini 3 Flash (Vorabversion) | ✔️ |
| Gemini 3.1 Flash Lite (Vorabversion) | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Unterstützte Toolkombinationen

Sie können die Fundierung mit der Google Suche mit anderen Tools wie
[der Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) und
[dem URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de) verwenden, um komplexere Anwendungsfälle zu ermöglichen.

Gemini 3-Modelle unterstützen die Kombination von integrierten Tools (z. B. Fundierung mit der Google Suche) mit benutzerdefinierten Tools (Funktionsaufrufe). Weitere Informationen finden Sie auf der
[Seite Toolkombinationen](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de).

## Nächste Schritte

- Probieren Sie die [Fundierung mit der Google Suche im Gemini API
  Kochbuch](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=de) aus.
- Informationen zu anderen verfügbaren Tools wie [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de)
- Informationen zum Erweitern von Prompts mit bestimmten URLs mithilfe des [Tools „URL-Kontext“](https://ai.google.dev/gemini-api/docs/url-context?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-23 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-23 (UTC)."],[],[]]
