---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=fr
fetched_at: 2026-10-19T05:53:53.096236+00:00
title: "Ancrage avec la recherche\u00a0Google \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Ancrage avec la recherche Google

L'ancrage avec la recherche Google permet d'associer le modèle Gemini à des contenus Web en temps réel et fonctionne avec toutes les langues disponibles. Cela permet à Gemini de fournir des réponses plus précises et de citer des sources vérifiables au-delà de sa date limite de connaissances.

L'ancrage vous aide à créer des applications capables de :

- **Améliorer la justesse factuelle** : réduisez les hallucinations du modèle en basant les réponses sur des informations réelles.
- **Accéder à des informations en temps réel** : répondez à des questions sur des événements et des sujets récents.
- **Fournir des citations** : gagnez la confiance des utilisateurs en indiquant les sources des affirmations du modèle.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Who won the euro 2024?"))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Who won the euro 2024?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleSearch{}),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## Fonctionnement de l'ancrage avec la recherche Google

Lorsque vous activez l'outil `google_search`, le modèle gère automatiquement l'ensemble du workflow de recherche, de traitement et de citation des informations.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=fr)

1. **Requête utilisateur** : votre application envoie la requête d'un utilisateur à l'API Gemini avec l'outil `google_search` activé.
2. **Analyse de la requête** : le modèle analyse la requête et détermine si une recherche Google peut améliorer la réponse.
3. **Recherche Google** : si nécessaire, le modèle génère automatiquement une ou plusieurs requêtes de recherche et les exécute.
4. **Traitement des résultats de recherche** : le modèle traite les résultats de recherche, synthétise les informations et formule une réponse.
5. **Réponse ancrée** : l'API renvoie une réponse finale et conviviale qui est ancrée dans les résultats de recherche. Cette réponse inclut la réponse textuelle du modèle avec des `annotations` intégrées contenant les citations, ainsi que les étapes `google_search_call` et `google_search_result` avec les requêtes de recherche et les suggestions de recherche.

## Comprendre la réponse d'ancrage

Lorsqu'une réponse est correctement ancrée, la sortie textuelle du modèle inclut des `annotations` intégrées directement dans le bloc de contenu textuel. Ces annotations fournissent des informations de citation qui associent des parties de la réponse à leurs sources.

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

Les champs clés de la réponse sont les suivants :

- `google_search_call` : contient les `queries` de recherche exécutées par le modèle.
- `google_search_result` : contient `search_suggestions`, un extrait HTML permettant d'afficher des suggestions de recherche dans votre UI. Les conditions d'utilisation complètes sont
  détaillées dans les [Conditions d'utilisation](https://ai.google.dev/gemini-api/terms?hl=fr#grounding-with-google-search).
- `text` avec `annotations` : réponse synthétisée du modèle avec des citations intégrées. Chaque annotation `url_citation` associe un segment de texte (défini par `start_index` et `end_index`) à une URL source. C'est la clé pour créer des citations intégrées.

L'ancrage avec la recherche Google peut également être utilisé en combinaison avec l'outil de contexte d'[URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr) pour ancrer les réponses à la fois dans
les données Web publiques et les URL spécifiques que vous fournissez.

## Attribuer des sources avec des citations intégrées

L'API renvoie des annotations `url_citation` intégrées dans le bloc de contenu textuel, ce qui vous permet de contrôler entièrement la façon dont vous affichez les sources dans votre interface utilisateur.
Chaque annotation inclut `start_index` et `end_index` pour identifier la partie du texte qu'elle cite. Voici comment les extraire et les afficher.

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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.URLCitation;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Who won the euro 2024?"))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            String text = textContent.text().orElse("");
            System.out.println(text);
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nCitations:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof URLCitation) {
                  URLCitation citation = (URLCitation) annotation;
                  int start = citation.startIndex().orElse(0);
                  int end = citation.endIndex().orElse(0);
                  String citedText =
                      (start >= 0 && end <= text.length() && start <= end)
                          ? text.substring(start, end)
                          : "";
                  System.out.printf(
                      "  [%s](%s)%n", citation.title().orElse(""), citation.url().orElse(""));
                  System.out.printf("    Cited text: \"%s\"%n", citedText);
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### Go

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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Who won the euro 2024?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleSearch{}),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    text := content.TextContent.Text
                    fmt.Println(text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nCitations:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.URLCitation != nil {
                                c := annotation.URLCitation
                                start := 0
                                if c.StartIndex != nil {
                                    start = *c.StartIndex
                                }
                                end := 0
                                if c.EndIndex != nil {
                                    end = *c.EndIndex
                                }
                                citedText := ""
                                if start >= 0 && end <= len(text) && start <= end {
                                    citedText = text[start:end]
                                }
                                title := ""
                                if c.Title != nil {
                                    title = *c.Title
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  [%s](%s)\n", title, url)
                                fmt.Printf("    Cited text: %q\n", citedText)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

La sortie affiche le texte suivi de ses citations :

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## Tarifs

Lorsque vous utilisez l'ancrage avec la recherche Google avec les modèles Gemini 3 et versions ultérieures, votre projet est facturé pour **chaque** requête de recherche que le modèle décide d'exécuter.
Ce modèle de facturation par requête inclut 5 000 requêtes de recherche sans frais par mois partagées entre tous les modèles Gemini 3 et versions ultérieures, puis coûte **14 $ pour 1 000 requêtes de recherche**.

Par exemple, si le modèle décide d'exécuter plusieurs requêtes de recherche pour répondre
à une seule requête (par exemple, en recherchant `"UEFA Euro 2024 winner"` et `"Spain vs
England Euro 2024 final score"` dans le même appel d'API), cela compte comme deux
utilisations facturables de l'outil pour cette requête. À des fins de facturation, nous ignorons les requêtes de recherche Web vides lors du comptage des requêtes uniques.

Lorsque vous utilisez l'ancrage de recherche avec les modèles Gemini 2.5 ou versions antérieures, votre projet est facturé par requête.

Pour obtenir des informations détaillées sur les tarifs, consultez la [page Tarifs de l'API Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=fr).

## Modèles compatibles

Vous trouverez toutes les fonctionnalités sur la page de présentation du [modèle
vue d'ensemble](https://ai.google.dev/gemini-api/docs/models?hl=fr).

| Modèle | Ancrage avec la recherche Google |
| --- | --- |
| Gemini 4 Argon | ✔️ |
| Gemini 3.8 Flash | ✔️ |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Preview Gemini 3.1 Flash Image | ✔️ |
| Preview Gemini 3.1 Pro | ✔️ |
| Preview Gemini 3 Pro Image | ✔️ |
| Preview Gemini 3 Flash | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Combinaisons d'outils compatibles

Vous pouvez utiliser l'ancrage avec la Recherche Google avec d'autres outils tels que
[l'exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr),
[le contexte de l'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr) et
[l'ancrage avec Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr) (compatible avec les modèles
Gemini 3.5 Flash-Lite et versions ultérieures) pour gérer des cas d'utilisation plus complexes.
Les modèles Gemini 3 sont également compatibles avec la combinaison de ces outils intégrés avec des outils personnalisés (appels de fonction). Pour en savoir plus, consultez la
[page Combinaisons d'outils](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fr).

## Étape suivante

- Découvrez d'autres outils disponibles, comme les [appels de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr).
- Découvrez comment augmenter les requêtes avec des URL spécifiques à l'aide de l'[outil de contexte d'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/10/13 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/10/13 (UTC)."],[],[]]
