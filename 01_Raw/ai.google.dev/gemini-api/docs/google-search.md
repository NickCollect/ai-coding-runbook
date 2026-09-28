---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=pl
fetched_at: 2026-09-28T06:24:15.212409+00:00
title: "Grounding z\u00a0u\u017cyciem wyszukiwarki Google \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Grounding z użyciem wyszukiwarki Google

Powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google łączy model Gemini z treściami z internetu w czasie rzeczywistym i działa we wszystkich dostępnych językach. Pozwala to Gemini udzielać dokładniejszych odpowiedzi i cytować zweryfikowane źródła poza jego granicą wiedzy.

Uziemienie pomaga tworzyć aplikacje, które mogą:

- **Zwiększanie dokładności:** zmniejsz halucynacje modelu, opierając odpowiedzi na informacjach ze świata rzeczywistego.
- **Dostęp do informacji w czasie rzeczywistym:** odpowiadanie na pytania dotyczące ostatnich wydarzeń i tematów.
- **Podawaj cytaty:** buduj zaufanie użytkowników, podając źródła twierdzeń modelu.

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

## Jak działa powiązanie ze źródłem informacji przy użyciu wyszukiwarki Google

Gdy włączysz to `google_search`narzędzie, model automatycznie obsłuży cały przepływ pracy związany z wyszukiwaniem, przetwarzaniem i cytowaniem informacji.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=pl)

1. **Prompt użytkownika:** Twoja aplikacja wysyła prompt użytkownika do interfejsu Gemini API z włączonym narzędziem `google_search`.
2. **Analiza promptu:** model analizuje prompt i określa, czy wyszukiwarka Google może ulepszyć odpowiedź.
3. **Wyszukiwarka Google:** w razie potrzeby model automatycznie generuje jedno lub kilka zapytań i je wykonuje.
4. **Przetwarzanie wyników wyszukiwania:** model przetwarza wyniki wyszukiwania, syntetyzuje informacje i formułuje odpowiedź.
5. **Odpowiedź oparta na wynikach wyszukiwania:** interfejs API zwraca ostateczną, przyjazną dla użytkownika odpowiedź, która jest oparta na wynikach wyszukiwania. Odpowiedź zawiera tekstową odpowiedź modelu z wstawionymi elementami `annotations` zawierającymi cytaty, a także kroki `google_search_call` i `google_search_result` z wyszukiwanymi hasłami i sugestiami wyszukiwania.

## Informacje o odpowiedzi uzasadniającej

Gdy odpowiedź zostanie prawidłowo ugruntowana, wygenerowany przez model tekst będzie zawierać wstawiony symbol `annotations` bezpośrednio w bloku treści tekstowej. Te adnotacje
zawierają informacje o cytowaniu, które łączą części odpowiedzi z ich źródłami.

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

Kluczowe pola w odpowiedzi:

- `google_search_call` : zawiera wyszukiwanie `queries` wykonane przez model.
- `google_search_result` : zawiera `search_suggestions`, czyli fragment kodu HTML do renderowania sugestii wyszukiwania w interfejsie. Pełne wymagania dotyczące korzystania z usługi są szczegółowo opisane w [Warunkach korzystania z usługi](https://ai.google.dev/gemini-api/terms?hl=pl#grounding-with-google-search).
- `text` z `annotations` : wygenerowana przez model odpowiedź z cytatami w tekście. Każda adnotacja `url_citation` łączy segment tekstu (zdefiniowany przez `start_index` i `end_index`) z adresem URL źródła. To klucz do tworzenia cytatów w tekście.

Powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google można też stosować w połączeniu z [narzędziem do kontekstu adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl), aby powiązać odpowiedzi ze źródłami informacji zarówno na podstawie danych z publicznej sieci, jak i określonych adresów URL.

## Podawanie źródeł za pomocą cytatów w tekście

Interfejs API zwraca w bloku tekstu adnotacje wstawione w tekście `url_citation`, dzięki czemu masz pełną kontrolę nad sposobem wyświetlania źródeł w interfejsie użytkownika.
Każda adnotacja zawiera znaki `start_index` i `end_index`, które wskazują, do której części tekstu się odnosi. Dowiedz się, jak je wyodrębnić i wyświetlić.

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

Wynik będzie zawierać tekst wraz z cytatami:

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## Ceny

Gdy używasz funkcji powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google w Gemini 3, za każde zapytanie, które model zdecyduje się wykonać, Twój projekt jest obciążany opłatą. Jeśli model zdecyduje się wykonać kilka zapytań, aby odpowiedzieć na jeden prompt (np. wyszukać `"UEFA Euro 2024 winner"` i `"Spain vs England Euro 2024 final
score"` w ramach jednego wywołania interfejsu API), będzie to liczone jako 2 płatne użycia narzędzia w przypadku tego żądania. Na potrzeby rozliczeń ignorujemy puste zapytania w wyszukiwarce internetowej podczas zliczania unikalnych zapytań. Ten model rozliczeń dotyczy tylko modeli Gemini 3. Jeśli używasz groundingu w wyszukiwarce z modelami Gemini 2.5 lub starszymi, za każdy prompt w Twoim projekcie zostanie naliczona opłata.

Szczegółowe informacje o cenach znajdziesz na [stronie z cennikiem Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=pl).

## Obsługiwane modele

Pełną listę funkcji znajdziesz na stronie [Przegląd modelu](https://ai.google.dev/gemini-api/docs/models?hl=pl).

| Model | Powiązanie ze źródłem informacji przy użyciu wyszukiwarki Google |
| --- | --- |
| Gemini 3.8 Flash | ✔️ |
| Gemini 3.7 Flash | ✔️ |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash Image (wersja testowa) | ✔️ |
| Gemini 3.1 Pro (wersja testowa) | ✔️ |
| Gemini 3 Pro Image (wersja testowa) | ✔️ |
| Gemini 3 Flash (wersja testowa) | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Obsługiwane kombinacje narzędzi

Możesz używać powiązania ze źródłami informacji przy użyciu wyszukiwarki Google z innymi narzędziami, takimi jak [wykonanie kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl), [kontekst adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl) i [powiązanie ze źródłami informacji przy użyciu Map Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl) (obsługiwane w przypadku Gemini 3.5 Flash i nowszych modeli), aby obsługiwać bardziej złożone przypadki użycia. Modele Gemini 3 obsługują też łączenie tych wbudowanych narzędzi z narzędziami niestandardowymi (wywoływanie funkcji). Więcej informacji znajdziesz na stronie [kombinacje narzędzi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl).

## Co dalej?

- Poznaj inne dostępne narzędzia, takie jak [wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl).
- Dowiedz się, jak wzbogacać prompty o konkretne adresy URL za pomocą [narzędzia do sprawdzania kontekstu adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-24 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-24 UTC."],[],[]]
