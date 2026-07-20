---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=pl
fetched_at: 2026-07-20T04:47:40.821721+00:00
title: "Kontekst adresu URL \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Kontekst adresu URL

Narzędzie kontekstu adresu URL umożliwia przekazywanie modelom dodatkowego kontekstu w postaci adresów URL. Jeśli w żądaniu uwzględnisz adresy URL, model uzyska dostęp do treści z tych stron (o ile nie jest to typ adresu URL wymieniony w [sekcji ograniczeń](#limitations)), aby uzyskać informacje i ulepszyć odpowiedź.

Narzędzie kontekstu adresu URL przydaje się w przypadku takich zadań:

- **Wyodrębnianie danych:** pobieranie z wielu adresów URL konkretnych informacji, takich jak ceny, nazwy lub kluczowe wnioski.
- **Porównywanie dokumentów:** analizuj wiele raportów, artykułów lub plików PDF, aby identyfikować różnice i śledzić trendy.
- **Synteza i tworzenie treści:** łączenie informacji z kilku adresów URL, aby generować dokładne podsumowania, posty na blogu lub raporty.
- **Analizowanie kodu i dokumentów:** wskaż repozytorium GitHub lub dokumentację techniczną, aby wyjaśnić kod, wygenerować instrukcje konfiguracji lub odpowiedzieć na pytania.

Poniższy przykład pokazuje, jak porównać 2 przepisy z różnych witryn.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## Jak to działa

Narzędzie Kontekst adresu URL korzysta z dwuetapowego procesu pobierania, aby zachować równowagę między szybkością, kosztem i dostępem do aktualnych danych. Gdy podasz adres URL, narzędzie najpierw spróbuje pobrać treść z wewnętrznej pamięci podręcznej indeksu. Pełni funkcję wysoce zoptymalizowanej pamięci podręcznej. Jeśli adres URL nie jest dostępny w indeksie (np. jeśli jest to bardzo nowa strona), narzędzie automatycznie przełącza się na pobieranie wersji opublikowanej.
Bezpośrednio uzyskuje dostęp do adresu URL, aby pobrać jego zawartość w czasie rzeczywistym.

## Łączenie z innymi narzędziami

Narzędzie kontekstu adresu URL możesz łączyć z innymi narzędziami, aby tworzyć bardziej zaawansowane
procesy.

[Modele Gemini 3](#supported-models) obsługują łączenie wbudowanych narzędzi (takich jak kontekst adresu URL) z narzędziami niestandardowymi (wywoływanie funkcji). Więcej informacji znajdziesz na stronie [kombinacje narzędzi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl).

### Powiązanie ze źródłem informacji przy użyciu wyszukiwarki

Gdy włączone są zarówno kontekst adresu URL, jak i [Grounding z użyciem wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/grounding?hl=pl), model może korzystać z funkcji wyszukiwania, aby znajdować w internecie odpowiednie informacje, a następnie używać narzędzia kontekstu adresu URL, aby lepiej zrozumieć znalezione strony. To podejście jest przydatne w przypadku promptów, które wymagają zarówno szerokiego wyszukiwania, jak i dogłębnej analizy konkretnych stron.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## Interpretowanie odpowiedzi

Gdy model używa narzędzia kontekstowego URL, jego odpowiedź tekstowa zawiera wbudowane `url_citation` adnotacje w bloku treści tekstowej. Każda adnotacja łączy segment tekstu odpowiedzi (za pomocą parametrów `start_index` i `end_index`) z adresem URL źródła, z którego pochodzi. Jest to podstawowy sposób wyświetlania cytatów w aplikacji. Aby dowiedzieć się, jak je wyodrębniać, zapoznaj się z [głównym przykładem powyżej](#get-started).

Odpowiedź zawiera też krok `url_context_result` z metadanymi dotyczącymi każdej próby pobrania adresu URL (stan, pobrany adres URL). Jest to przydatne głównie do debugowania.

### Kontrole bezpieczeństwa

System sprawdza adresy URL pod kątem moderacji treści, aby potwierdzić, że spełniają one standardy bezpieczeństwa. Jeśli URL nie przejdzie tego testu, w odpowiednim kroku`url_context_result` pojawi się `status` w kolorze `"unsafe"`.

### Liczba tokenów

Treści pobrane z adresów URL podanych w prompcie są liczone jako tokeny wejściowe. Liczbę tokenów możesz sprawdzić w `usage`obiekcie interakcji. Oto przykład:

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

Cena za token zależy od użytego modelu. Więcej informacji znajdziesz na stronie [cennika](https://ai.google.dev/gemini-api/docs/pricing?hl=pl).

## Obsługiwane modele

| Model | Kontekst adresu URL |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=pl) | ✔️ |
| [Gemini 3.1 Pro (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pl) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl) | ✔️ |
| [Gemini 3 Flash (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pl) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pl) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pl) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pl) | ✔️ |

## Sprawdzone metody

- **Podaj konkretne adresy URL:** aby uzyskać najlepsze wyniki, podaj bezpośrednie adresy URL treści, które mają być analizowane przez model. Model będzie pobierać treści tylko z podanych przez Ciebie adresów URL, a nie z linków zagnieżdżonych.
- **Sprawdź dostępność:** upewnij się, że podane adresy URL nie prowadzą do stron, które wymagają logowania lub są umieszczone w sekcji płatnej.
- **Używaj pełnego adresu URL:** podaj pełny adres URL, w tym protokół (np. https://www.google.com zamiast google.com).

## Ograniczenia

- Limit żądań: narzędzie może przetworzyć maksymalnie 20 adresów URL w jednym żądaniu.
- Rozmiar treści URL: maksymalny rozmiar treści pobranych z jednego adresu URL to 34 MB.
- Publiczna dostępność: adresy URL muszą być publicznie dostępne w internecie.
  Adresy hosta lokalnego (np. localhost, 127.0.0.1), sieci prywatne i usługi tunelowania (np. ngrok, pinggy) nie są obsługiwane.
- Tylko Gemini API: kontekst URL jest dostępny tylko w interfejsie Gemini API, a nie w Gemini Enterprise Agent Platform.

### Obsługiwane i nieobsługiwane typy treści

Narzędzie może wyodrębniać treści z adresów URL, które zawierają te typy treści:

- Tekst (text/html, application/json, text/plain, text/xml, text/css, text/javascript , text/csv, text/rtf)
- Obraz (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

Te typy treści **nie są** obsługiwane:

- Treści płatne
- filmy w YouTube (więcej informacji o przetwarzaniu adresów URL z YouTube znajdziesz w sekcji [rozumienie filmów](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pl#youtube));
- pliki Google Workspace, takie jak dokumenty lub arkusze kalkulacyjne Google;
- Pliki audio i wideo

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-06 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-06 UTC."],[],[]]
