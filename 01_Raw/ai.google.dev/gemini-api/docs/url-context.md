---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=pl
fetched_at: 2026-05-11T04:57:30.640475+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Kontekst adresu URL

Narzędzie Kontekst adresu URL umożliwia przekazywanie modelom dodatkowych informacji kontekstowych w postaci adresów URL. Jeśli w żądaniu uwzględnisz adresy URL, model uzyska dostęp do treści z tych stron (o ile nie jest to typ adresu URL wymieniony w sekcji [Ograniczenia](#limitations)), aby wzbogacić swoją odpowiedź.

Narzędzie Kontekst adresu URL jest przydatne w przypadku takich zadań jak:

- **Pozyskiwanie danych**: pobieranie konkretnych informacji, takich jak ceny, nazwy lub kluczowe
  ustalenia, z wielu adresów URL.
- **Porównywanie dokumentów**: analizowanie wielu raportów, artykułów lub plików PDF w celu
  identyfikowania różnic i śledzenia trendów.
- **Synteza i tworzenie treści:** łączenie informacji z kilku źródłowych adresów URL w celu generowania dokładnych podsumowań, postów na blogu lub raportów.
- **Analizowanie kodu i dokumentów:** wskazywanie repozytorium GitHub lub dokumentacji technicznej w celu wyjaśnienia kodu, wygenerowania instrukcji konfiguracji lub udzielenia odpowiedzi na pytania.

Z przykładu poniżej dowiesz się, jak porównać 2 przepisy z różnych witryn.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()
model_id = "gemini-3-flash-preview"

tools = [
  {"url_context": {}},
]

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

response = client.models.generate_content(
    model=model_id,
    contents=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)

# For verification, you can inspect the metadata to see which URLs the model retrieved
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
        "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    ],
    config: {
      tools: [{urlContext: {}}],
    },
  });
  console.log(response.text);

  // For verification, you can inspect the metadata to see which URLs the model retrieved
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          }
      ]
  }' > result.json

cat result.json
```

## Jak to działa

Narzędzie Kontekst adresu URL korzysta z 2-etapowego procesu pobierania, aby zachować równowagę między szybkością, kosztem a dostępem do aktualnych danych. Gdy podasz adres URL, narzędzie najpierw spróbuje pobrać treść z wewnętrznej pamięci podręcznej indeksu. Działa ona jak wysoce zoptymalizowana pamięć podręczna. Jeśli adres URL nie jest dostępny w indeksie (np. jeśli jest to bardzo nowa strona), narzędzie automatycznie przełączy się na pobieranie na żywo.
Dzięki temu bezpośrednio uzyskuje dostęp do adresu URL, aby pobrać jego zawartość w czasie rzeczywistym.

## Łączenie z innymi narzędziami

Aby tworzyć bardziej zaawansowane procesy, możesz połączyć narzędzie Kontekst adresu URL z innymi narzędziami.

[Modele Gemini 3](#supported-models) obsługują łączenie wbudowanych narzędzi
(takich jak Kontekst adresu URL) z narzędziami niestandardowymi (wywołanie funkcji). Więcej informacji znajdziesz na
[stronie dotyczącej kombinacji narzędzi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl).

### Powiązanie ze źródłem informacji przy użyciu wyszukiwarki

Gdy włączone są zarówno Kontekst adresu URL, jak i
[Powiązanie ze źródłem informacji przy użyciu wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/grounding?hl=pl),
model może korzystać z funkcji wyszukiwania, aby znajdować
odpowiednie informacje w internecie, a następnie używać narzędzia Kontekst adresu URL, aby lepiej zrozumieć znalezione
strony. To podejście jest skuteczne w przypadku promptów, które wymagają zarówno szerokiego wyszukiwania, jak i dogłębnej analizy konkretnych stron.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client()
model_id = "gemini-3-flash-preview"

tools = [
      {"url_context": {}},
      {"google_search": {}}
  ]

response = client.models.generate_content(
    model=model_id,
    contents="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
# get URLs retrieved for context
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
        "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    ],
    config: {
      tools: [
        {urlContext: {}},
        {googleSearch: {}}
        ],
    },
  });
  console.log(response.text);
  // To get URLs retrieved for context
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          },
          {
              "google_search": {}
          }
      ]
  }' > result.json

cat result.json
```

## Opis odpowiedzi

Gdy model używa narzędzia Kontekst adresu URL, odpowiedź zawiera obiekt `url_context_metadata`. Ten obiekt zawiera listę adresów URL, z których model pobrał treści, oraz stan każdej próby pobrania. Jest to przydatne do weryfikacji i debugowania.

Oto przykład tej części odpowiedzi (dla zwięzłości pominięto niektóre części):

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "... \n"
          }
        ],
        "role": "model"
      },
      ...
      "url_context_metadata": {
        "url_metadata": [
          {
            "retrieved_url": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          },
          {
            "retrieved_url": "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          }
        ]
      }
    }
  ]
}
```

Szczegółowe informacje o tym obiekcie znajdziesz w
[`UrlContextMetadata` dokumentacji API](https://ai.google.dev/api/generate-content?hl=pl#UrlContextMetadata).

### Testy zabezpieczeń

System przeprowadza kontrolę moderacji treści pod kątem adresu URL, aby potwierdzić, że spełnia on standardy bezpieczeństwa. Jeśli podany adres URL nie przejdzie tej kontroli, otrzymasz `url_retrieval_status` o wartości `URL_RETRIEVAL_STATUS_UNSAFE`.

### Liczba tokenów

Treści pobrane z adresów URL podanych w prompcie są liczone jako część tokenów wejściowych. Liczbę tokenów dla promptu i
użycia narzędzi możesz sprawdzić w [`usage_metadata`](https://ai.google.dev/api/generate-content?hl=pl#UsageMetadata)
obiekcie danych wyjściowych modelu. Oto przykład danych wyjściowych:

```
'usage_metadata': {
  'candidates_token_count': 45,
  'prompt_token_count': 27,
  'prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 27}],
  'thoughts_token_count': 31,
  'tool_use_prompt_token_count': 10309,
  'tool_use_prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 10309}],
  'total_token_count': 10412
  }
```

Cena za token zależy od używanego modelu. Szczegółowe informacje znajdziesz na
[stronie z cennikiem](https://ai.google.dev/gemini-api/docs/pricing?hl=pl).

## Obsługiwane modele

| Model | Kontekst adresu URL |
| --- | --- |
| [Gemini 3.1 Pro (wersja testowa)](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=pl) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl) | ✔️ |
| [Gemini 3.1 Flash-Lite (wersja testowa)](https://ai.google.dev/gemini-api/docs/gemini-3.1-flash-lite-preview?hl=pl) | ✔️ |
| [Gemini 3 Flash (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pl) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pl) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pl) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pl) | ✔️ |

## Sprawdzone metody

- **Podawaj konkretne adresy URL**: aby uzyskać najlepsze wyniki, podaj bezpośrednie adresy URL do
  treści, które chcesz analizować. Model będzie pobierać tylko treści z podanych adresów URL, a nie z linków zagnieżdżonych.
- **Sprawdzaj dostępność**: upewnij się, że podane adresy URL nie prowadzą do
  stron, które wymagają logowania lub są płatne.
- **Używaj pełnego adresu URL**: podaj pełny adres URL, w tym protokół
  (np. https://www.google.com zamiast google.com).

## Ograniczenia

- Wywołanie funkcji: używanie narzędzi (Kontekst adresu URL, Powiązanie ze źródłem informacji przy użyciu wyszukiwarki Google itp.) z wywołaniem funkcji nie jest obecnie obsługiwane.
- Limit żądań: narzędzie może przetworzyć maksymalnie 20 adresów URL na żądanie.
- Rozmiar treści adresu URL: maksymalny rozmiar treści pobranych z jednego adresu URL to 34 MB.
- Dostępność publiczna: adresy URL muszą być publicznie dostępne w internecie.
  Adresy localhost (np. localhost, 127.0.0.1), sieci prywatne i usługi tunelowania (np. ngrok, pinggy) nie są obsługiwane.
- Tylko interfejs Gemini API: Kontekst adresu URL jest dostępny tylko w interfejsie Gemini API, a nie na platformie agentów Gemini Enterprise.

### Obsługiwane i nieobsługiwane typy treści

Narzędzie może wyodrębniać treści z adresów URL o tych typach:

- Tekst (text/html, application/json, text/plain, text/xml, text/css, text/javascript , text/csv, text/rtf)
- Obraz (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

Te typy treści **nie są** obsługiwane:

- Treści płatne
- Filmy z YouTube (informacje o tym, jak przetwarzać adresy URL z YouTube, znajdziesz w artykule o
  [rozumieniu filmów](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pl#youtube))
- Pliki Google Workspace, takie jak dokumenty i arkusze Google
- Pliki audio i wideo

## Co dalej?

- Więcej przykładów znajdziesz w przewodniku [Kontekst adresu URL](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Grounding.ipynb?hl=pl#url-context).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-08 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-08 UTC."],[],[]]
