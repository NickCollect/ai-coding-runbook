---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=de
fetched_at: 2026-09-28T06:16:39.751515+00:00
title: "URL-Kontext \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# URL-Kontext

Mit dem Tool „URL-Kontext“ können Sie den Modellen zusätzlichen Kontext in Form von URLs zur Verfügung stellen. Wenn Sie URLs in Ihre Anfrage einfügen, greift das Modell auf die Inhalte dieser Seiten zu (sofern es sich nicht um einen im [Abschnitt zu Einschränkungen](#limitations) aufgeführten URL-Typ handelt), um seine Antwort zu informieren und zu verbessern.

Das Tool „URL-Kontext“ ist für Aufgaben wie die folgenden nützlich:

- **Daten extrahieren**: Bestimmte Informationen wie Preise, Namen oder wichtige Erkenntnisse aus mehreren URLs abrufen.
- **Dokumente vergleichen**: Sie können mehrere Berichte, Artikel oder PDFs analysieren, um Unterschiede zu erkennen und Trends zu verfolgen.
- **Inhalte zusammenfassen und erstellen**: Informationen aus mehreren Quell-URLs kombinieren, um präzise Zusammenfassungen, Blogposts oder Berichte zu erstellen.
- **Code und Dokumente analysieren**: Verweisen Sie auf ein GitHub-Repository oder eine technische Dokumentation, um Code zu erläutern, Einrichtungsanleitungen zu generieren oder Fragen zu beantworten.

Im folgenden Beispiel sehen Sie, wie Sie zwei Rezepte von verschiedenen Websites vergleichen können.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
```

### Ok

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    url1 := "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
    url2 := "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(
                fmt.Sprintf("Compare the ingredients and cooking times from the recipes at %s and %s", url1, url2),
            ),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.URLContext{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Print the model's text response and its source annotations
    for _, step := range res.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, contentBlock := range step.ModelOutputStep.Content {
                if contentBlock.TextContent != nil {
                    fmt.Println(contentBlock.TextContent.Text)
                    if len(contentBlock.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range contentBlock.TextContent.Annotations {
                            if annotation.URLCitation != nil {
                                fmt.Printf("  - %s: %s\n", annotation.URLCitation.GetTitle(), annotation.URLCitation.GetURL())
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.8-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## Funktionsweise

Das Tool „URL-Kontext“ verwendet einen zweistufigen Abrufprozess, um Geschwindigkeit, Kosten und Zugriff auf aktuelle Daten in Einklang zu bringen. Wenn Sie eine URL angeben, versucht das Tool zuerst, den Inhalt aus einem internen Indexcache abzurufen. Dies dient als hochoptimierter Cache. Wenn eine URL nicht im Index verfügbar ist (z. B. weil es sich um eine sehr neue Seite handelt), wird automatisch ein Live-Abruf durchgeführt.
Dadurch wird direkt auf die URL zugegriffen, um die Inhalte in Echtzeit abzurufen.

## Mit anderen Tools kombinieren

Sie können das Tool „URL-Kontext“ mit anderen Tools kombinieren, um leistungsstärkere Workflows zu erstellen.

[Gemini 3-Modelle](#supported-models) unterstützen die Kombination von integrierten Tools (z. B. URL-Kontext) mit benutzerdefinierten Tools (Funktionsaufruf). [Weitere Informationen zu Tool-Kombinationen](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de)

### Fundierung mit der Suche

Wenn sowohl der URL-Kontext als auch [Fundierung mit der Google Suche](https://ai.google.dev/gemini-api/docs/grounding?hl=de) aktiviert sind, kann das Modell seine Suchfunktionen nutzen, um relevante Informationen online zu finden, und dann das Tool für den URL-Kontext verwenden, um die gefundenen Seiten besser zu verstehen. Dieser Ansatz ist besonders hilfreich für Prompts, die sowohl eine breite Suche als auch eine detaillierte Analyse bestimmter Seiten erfordern.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
```

### Ok

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.URLContext{}),
                interactions.NewTool(interactions.GoogleSearch{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, contentBlock := range step.ModelOutputStep.Content {
                if contentBlock.TextContent != nil {
                    fmt.Println(contentBlock.TextContent.Text)
                }
            }
        }
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.8-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## Antwort verstehen

Wenn das Modell das Tool für den URL-Kontext verwendet, enthält die Textantwort Inline-`url_citation`-Anmerkungen im Textinhaltsblock. Jede Annotation verknüpft ein Segment des Antworttexts (über `start_index` und `end_index`) mit der Quell-URL, aus der es stammt. Dies ist die primäre Methode, um Zitationen in Ihrer Anwendung zu präsentieren. Im [Hauptbeispiel oben](#get-started) sehen Sie, wie Sie sie extrahieren.

Die Antwort enthält auch einen `url_context_result`-Schritt mit Metadaten zu jedem URL-Abrufversuch (Status, abgerufene URL). Das ist hauptsächlich für das Debugging nützlich.

### Sicherheitschecks

Das System führt eine Inhaltsmoderationsprüfung für URLs durch, um zu bestätigen, dass sie den Sicherheitsstandards entsprechen. Wenn eine URL diese Prüfung nicht besteht, wird im entsprechenden `url_context_result`-Schritt ein `status` von `"unsafe"` angezeigt.

### Tokenanzahl

Die Inhalte, die von den URLs abgerufen werden, die Sie in Ihrem Prompt angeben, werden als Teil der Eingabetokens gezählt. Die Anzahl der Tokens finden Sie im `usage`-Objekt der Interaktion. Hier ein Beispiel:

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

Der Preis pro Token hängt vom verwendeten Modell ab. Weitere Informationen finden Sie auf der [Preisseite](https://ai.google.dev/gemini-api/docs/pricing?hl=de).

## Unterstützte Modelle

| Modell | URL-Kontext |
| --- | --- |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=de) | ✔️ |
| [Gemini 3.7 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash?hl=de) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=de) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=de) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=de) | ✔️ |
| [Gemini 3.1 Pro (Vorabversion)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=de) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=de) | ✔️ |
| [Gemini 3 Flash (Vorabversion)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=de) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=de) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=de) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=de) | ✔️ |

## Best Practices

- **Geben Sie bestimmte URLs an**: Für optimale Ergebnisse sollten Sie direkte URLs zu den Inhalten angeben, die das Modell analysieren soll. Das Modell ruft nur Inhalte von den von Ihnen angegebenen URLs ab, nicht von verschachtelten Links.
- **Zugänglichkeit prüfen**: Prüfen Sie, ob die von Ihnen angegebenen URLs zu Seiten führen, für die eine Anmeldung erforderlich ist oder die sich hinter einer Paywall befinden.
- **Vollständige URL verwenden**: Geben Sie die vollständige URL einschließlich des Protokolls an, z.B. https://www.google.com statt nur google.com.

## Beschränkungen

- Anfragelimit: Das Tool kann bis zu 20 URLs pro Anfrage verarbeiten.
- Größe von URL-Inhalten: Die maximale Größe für Inhalte, die von einer einzelnen URL abgerufen werden, beträgt 34 MB.
- Öffentliche Zugänglichkeit: Die URLs müssen öffentlich im Web zugänglich sein.
  Localhost-Adressen (z.B. localhost, 127.0.0.1), private Netzwerke und Tunneling-Dienste (z.B. ngrok, pinggy) werden nicht unterstützt.

### Unterstützte und nicht unterstützte Inhaltstypen

Das Tool kann Inhalte aus URLs mit den folgenden Inhaltstypen extrahieren:

- Text (text/html, application/json, text/plain, text/xml, text/css,
  text/javascript , text/csv, text/rtf)
- Bild (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

Die folgenden Inhaltstypen werden **nicht** unterstützt:

- Paywall-Inhalte
- YouTube-Videos ([Informationen zum Verarbeiten von YouTube-URLs](https://ai.google.dev/gemini-api/docs/video-understanding?hl=de#youtube))
- Google Workspace-Dateien wie Google-Dokumente oder ‑Tabellen
- Video- und Audiodateien

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-24 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-24 (UTC)."],[],[]]
