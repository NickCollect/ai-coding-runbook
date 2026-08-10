---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=pl
fetched_at: 2026-08-10T03:25:39.622204+00:00
title: "Grounding z\u00a0u\u017cyciem wyszukiwarki Google \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Grounding z użyciem wyszukiwarki Google

Powiązanie ze źródłem informacji przy użyciu wyszukiwarki Google łączy model Gemini z treściami z internetu w czasie rzeczywistym i działa we wszystkich dostępnych językach. Pozwala to Gemini udzielać dokładniejszych odpowiedzi i cytować zweryfikowane źródła poza jego granicą wiedzy.

Grounding pomaga tworzyć aplikacje, które mogą:

- **Zwiększać dokładność faktów:** zmniejszaj halucynacje modelu, opierając odpowiedzi na informacjach ze świata rzeczywistego.
- **Uzyskiwać dostęp do informacji w czasie rzeczywistym:** odpowiadaj na pytania dotyczące najnowszych wydarzeń i tematów.
- **Podawać cytaty:** buduj zaufanie użytkowników, pokazując źródła twierdzeń modelu.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## Jak działa powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google

Gdy włączysz narzędzie `google_search`, model automatycznie obsługuje cały przepływ pracy związany z wyszukiwaniem, przetwarzaniem i cytowaniem informacji.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=pl)

1. **Prompt użytkownika:** Twoja aplikacja wysyła prompt użytkownika do Gemini API z włączonym narzędziem `google_search`.
2. **Analiza prompta:** model analizuje prompt i określa, czy wyszukiwanie w Google może poprawić odpowiedź.
3. **Wyszukiwanie w Google:** w razie potrzeby model automatycznie generuje jedno lub kilka zapytań i je wykonuje.
4. **Przetwarzanie wyników wyszukiwania:** model przetwarza wyniki wyszukiwania, syntetyzuje informacje i formułuje odpowiedź.
5. **Odpowiedź oparta na wynikach wyszukiwania:** interfejs API zwraca ostateczną, przyjazną dla użytkownika odpowiedź opartą na wynikach wyszukiwania. Ta odpowiedź zawiera tekstową odpowiedź modelu z wbudowanymi `annotations` zawierającymi cytaty, a także kroki `google_search_call` i `google_search_result` z zapytaniami i sugestiami wyszukiwania.

## Informacje o odpowiedzi opartej na wynikach wyszukiwania

Gdy odpowiedź jest oparta na wynikach wyszukiwania, tekstowe dane wyjściowe modelu zawierają wbudowane `annotations` bezpośrednio w bloku treści tekstowej. Te adnotacje zawierają informacje o cytowaniu, które łączą części odpowiedzi z ich źródłami.

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

Kluczowe pola w odpowiedzi:

- `google_search_call` : zawiera `queries` wyszukiwania wykonane przez model.
- `google_search_result` : zawiera `search_suggestions`, czyli fragment kodu HTML do renderowania sugestii wyszukiwania w interfejsie. Pełne wymagania dotyczące użytkowania są
  opisane w [Warunkach korzystania z usługi](https://ai.google.dev/gemini-api/terms?hl=pl#grounding-with-google-search).
- `text` z `annotations` : syntetyzowana odpowiedź modelu z wbudowanymi cytatami. Każda adnotacja `url_citation` łączy segment tekstu (zdefiniowany przez `start_index` i `end_index`) z adresem URL źródła. Jest to klucz do tworzenia wbudowanych cytatów.

Powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google można też stosować w połączeniu z narzędziem kontekstu [adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl), aby opierać odpowiedzi zarówno na publicznych danych internetowych
, jak i na konkretnych adresach URL, które podasz.

## Podawanie źródeł za pomocą wbudowanych cytatów

Interfejs API zwraca wbudowane adnotacje `url_citation` w bloku treści tekstowej, co daje Ci pełną kontrolę nad sposobem wyświetlania źródeł w interfejsie.
Każda adnotacja zawiera `start_index` i `end_index`, aby określić, którą część tekstu cytuje. Oto jak je wyodrębnić i wyświetlić.

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

Dane wyjściowe będą zawierać tekst, a następnie jego cytaty:

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## Ceny

Gdy używasz powiązania ze źródłami informacji przy użyciu wyszukiwarki Google z Gemini 3, za każde zapytanie, które model zdecyduje się wykonać, zostanie naliczona opłata. Jeśli model zdecyduje się wykonać kilka zapytań, aby odpowiedzieć na jeden prompt (np. wyszukać hasła `"UEFA Euro 2024 winner"` i `"Spain vs England Euro 2024 final
score"` w ramach tego samego wywołania interfejsu API), będzie to liczone jako 2 płatne użycia narzędzia w przypadku tego żądania. Na potrzeby rozliczeń ignorujemy puste zapytania w wyszukiwarce podczas zliczania unikalnych zapytań. Ten model rozliczeń dotyczy tylko modeli Gemini 3. Jeśli używasz groundingu przy użyciu wyszukiwarki z Gemini 2.5 lub starszymi modelami, opłata jest naliczana za prompt.

Szczegółowe informacje o cenach znajdziesz na stronie cennika [Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=pl).

## Obsługiwane modele

Pełne możliwości znajdziesz na stronie z informacjami o [modelu
overview](https://ai.google.dev/gemini-api/docs/models?hl=pl).

| Model | Powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google |
| --- | --- |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash Image (wersja testowa) | ✔️ |
| Gemini 3.1 Pro (wersja testowa) | ✔️ |
| Gemini 3 Pro Image (wersja testowa) | ✔️ |
| Gemini 3 Flash (wersja testowa) | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Obsługiwane kombinacje narzędzi

Powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google możesz używać z innymi narzędziami, takimi jak
[wykonanie kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl) i
[kontekst adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl), aby obsługiwać bardziej złożone
przypadki użycia.

Modele Gemini 3 obsługują łączenie narzędzi wbudowanych (takich jak grounding przy użyciu wyszukiwarki Google) z narzędziami niestandardowymi (wywoływanie funkcji). Więcej informacji znajdziesz na
[stronie dotyczącej kombinacji narzędzi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl).

## Co dalej?

- Dowiedz się więcej o innych dostępnych narzędziach, takich jak [wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl).
- [Dowiedz się, jak rozszerzać prompty o konkretne adresy URL za pomocą narzędzia kontekstu adresu URL.](https://ai.google.dev/gemini-api/docs/url-context?hl=pl)

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
