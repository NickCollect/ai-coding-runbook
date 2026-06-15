---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=pl
fetched_at: 2026-06-15T06:32:20.561614+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Kontekst adresu URL

Narzędzie kontekstu adresu URL umożliwia przekazywanie modelom dodatkowego kontekstu w postaci adresów URL. Jeśli w żądaniu uwzględnisz adresy URL, model uzyska dostęp do treści z tych stron (o ile nie jest to typ adresu URL wymieniony w [sekcji ograniczeń](#limitations)), aby na ich podstawie tworzyć i ulepszać odpowiedzi.

Narzędzie kontekstu adresu URL przydaje się w przypadku takich zadań:

- **Wyodrębnianie danych:** pobieranie z wielu adresów URL konkretnych informacji, takich jak ceny, nazwy lub kluczowe wnioski.
- **Porównywanie dokumentów:** analizuj wiele raportów, artykułów lub plików PDF, aby identyfikować różnice i śledzić trendy.
- **Synteza i tworzenie treści:** łączenie informacji z kilku adresów URL, aby generować dokładne podsumowania, posty na blogu lub raporty.
- **Analizowanie kodu i dokumentów:** wskaż repozytorium GitHub lub dokumentację techniczną, aby wyjaśnić kod, wygenerować instrukcje konfiguracji lub odpowiedzieć na pytania.

Poniższy przykład pokazuje, jak porównać 2 przepisy z różnych witryn.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()
model_id = "gemini-3.5-flash"

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
    model: "gemini-3.5-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

Narzędzie Kontekst adresu URL korzysta z dwuetapowego procesu pobierania, aby zachować równowagę między szybkością, kosztem i dostępem do aktualnych danych. Gdy podasz adres URL, narzędzie najpierw spróbuje pobrać treść z wewnętrznej pamięci podręcznej indeksu. Pełni funkcję wysoce zoptymalizowanej pamięci podręcznej. Jeśli adres URL nie jest dostępny w indeksie (np. jeśli jest to bardzo nowa strona), narzędzie automatycznie przełącza się na pobieranie wersji opublikowanej.
Bezpośrednio uzyskuje dostęp do adresu URL, aby pobrać jego zawartość w czasie rzeczywistym.

## Łączenie z innymi narzędziami

Narzędzie kontekstu adresu URL możesz łączyć z innymi narzędziami, aby tworzyć bardziej zaawansowane
przepływy pracy.

[Modele Gemini 3](#supported-models) obsługują łączenie wbudowanych narzędzi (takich jak kontekst adresu URL) z narzędziami niestandardowymi (wywoływanie funkcji). Więcej informacji znajdziesz na stronie [kombinacje narzędzi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl).

### Powiązanie ze źródłem informacji przy użyciu wyszukiwarki

Gdy włączone są zarówno kontekst adresu URL, jak i [powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/grounding?hl=pl), model może korzystać z funkcji wyszukiwania, aby znajdować w internecie odpowiednie informacje, a następnie używać narzędzia kontekstu adresu URL, aby lepiej zrozumieć znalezione strony. To podejście jest przydatne w przypadku promptów, które wymagają zarówno szerokiego wyszukiwania, jak i dogłębnej analizy konkretnych stron.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client()
model_id = "gemini-3.5-flash"

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
    model: "gemini-3.5-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

## Interpretowanie odpowiedzi

Gdy model używa narzędzia kontekstu URL, odpowiedź zawiera obiekt `url_context_metadata`. Ten obiekt zawiera listę adresów URL, z których model pobrał treść, oraz stan każdej próby pobrania, co jest przydatne do weryfikacji i debugowania.

Oto przykład tej części odpowiedzi (dla zwięzłości pominięto niektóre jej fragmenty):

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

Szczegółowe informacje o tym obiekcie znajdziesz w [dokumentacji interfejsu API `UrlContextMetadata`](https://ai.google.dev/api/generate-content?hl=pl#UrlContextMetadata).

### Kontrole bezpieczeństwa

System sprawdza adres URL pod kątem moderacji treści, aby potwierdzić, że spełnia on standardy bezpieczeństwa. Jeśli podany przez Ciebie adres URL nie przejdzie tej weryfikacji, otrzymasz `url_retrieval_status` `URL_RETRIEVAL_STATUS_UNSAFE`.

### Liczba tokenów

Treści pobrane z adresów URL podanych w prompcie są liczone jako tokeny wejściowe. Liczbę tokenów w prompcie i wykorzystanie narzędzi możesz sprawdzić w obiekcie [`usage_metadata`](https://ai.google.dev/api/generate-content?hl=pl#UsageMetadata)
w danych wyjściowych modelu. Oto przykładowe dane wyjściowe:

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

Cena za token zależy od użytego modelu. Więcej informacji znajdziesz na stronie [cennika](https://ai.google.dev/gemini-api/docs/pricing?hl=pl).

## Obsługiwane modele

| Model | Kontekst adresu URL |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=pl) | ✔️ |
| [Gemini 3.1 Pro (wersja testowa)](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=pl) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl) | ✔️ |
| [Gemini 3 Flash (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pl) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pl) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pl) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pl) | ✔️ |

## Sprawdzone metody

- **Podaj konkretne adresy URL:** aby uzyskać najlepsze wyniki, podaj bezpośrednie adresy URL treści, które mają być analizowane przez model. Model pobierze tylko treści z podanych adresów URL, a nie z linków zagnieżdżonych.
- **Sprawdź dostępność:** upewnij się, że podane adresy URL nie prowadzą do stron, które wymagają logowania lub są umieszczone w sekcji płatnej.
- **Używaj pełnego adresu URL:** podaj pełny adres URL, w tym protokół (np. https://www.google.com zamiast google.com).

## Ograniczenia

- Wywoływanie funkcji: korzystanie z narzędzi (kontekst adresu URL, powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google itp.) z wywoływaniem funkcji jest obecnie nieobsługiwane.
- Limit żądań: narzędzie może przetworzyć maksymalnie 20 adresów URL w jednym żądaniu.
- Rozmiar treści URL: maksymalny rozmiar treści pobranych z jednego adresu URL to 34 MB.
- Publiczna dostępność: adresy URL muszą być publicznie dostępne w internecie.
  Adresy hosta lokalnego (np. localhost, 127.0.0.1), sieci prywatne i usługi tunelowania (np. ngrok, pinggy) nie są obsługiwane.
- Tylko interfejs Gemini API: kontekst adresu URL jest dostępny tylko w interfejsie Gemini API, a nie na platformie Gemini Enterprise Agent Platform.

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

## Co dalej?

- Więcej przykładów znajdziesz w [książce kucharskiej dotyczącej kontekstu adresu URL](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Grounding.ipynb?hl=pl#url-context).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-01 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-01 UTC."],[],[]]
