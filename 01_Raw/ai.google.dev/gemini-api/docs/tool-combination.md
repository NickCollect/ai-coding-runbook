---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl
fetched_at: 2026-08-17T02:27:11.683837+00:00
title: "\u0141\u0105czenie wbudowanych narz\u0119dzi i\u00a0wywo\u0142ywania funkcji \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Łączenie wbudowanych narzędzi i wywoływania funkcji

Gemini umożliwia łączenie [narzędzi wbudowanych](https://ai.google.dev/gemini-api/docs/tools?hl=pl), takich
jak `google_search`, i [wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl)
(znanych też jako *narzędzia niestandardowe*) w ramach jednej interakcji dzięki zachowaniu i udostępnianiu
historii kontekstu wywołań narzędzi. Kombinacje narzędzi wbudowanych i niestandardowych umożliwiają tworzenie złożonych przepływów pracy, w których np. model może opierać się na danych internetowych w czasie rzeczywistym przed wywołaniem konkretnej logiki biznesowej.

Oto przykład, który umożliwia łączenie narzędzi wbudowanych i niestandardowych za pomocą `google_search` i funkcji niestandardowej `getWeather`:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "model": "gemini-3.6-flash",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }
  ]
}'
```

## Jak to działa

Modele Gemini 3 używają *cyrkulacji kontekstu narzędzia*, aby umożliwić łączenie narzędzi wbudowanych i niestandardowych. Cyrkulacja kontekstu narzędzia umożliwia zachowanie i udostępnianie kontekstu narzędzi wbudowanych oraz udostępnianie go narzędziom niestandardowym w ramach tej samej interakcji.

### Włączanie łączenia narzędzi

- Aby wywołać zachowanie łączenia, dołącz [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#function-declarations) wraz
  z narzędziami wbudowanymi, których chcesz używać.

### Kroki zwracane przez interfejs API

W odpowiedzi na interakcję interfejs API zwraca osobne kroki dla wywołań narzędzi wbudowanych i wywołań funkcji (narzędzi niestandardowych):

- **Kroki narzędzi wbudowanych**: interfejs API zarządza nimi automatycznie, zachowując
  kontekst między turami.
- **Kroki wywołań funkcji**: interfejs API zwraca kro2/}ki dla Twoich
  funkcji niestandardowych.`function_call` Wykonujesz funkcję i podajesz wynik.

### Krytyczne pola w zwracanych krokach

Niektóre pola w zwracanych krokach są niezbędne do zachowania kontekstu narzędzia i umożliwienia łączenia narzędzi:

- **`id`**: znajduje się w krokach `function_call` i `function_response`. Unikalny identyfikator, który przypisuje wywołanie do jego odpowiedzi.
- **`signature`**: znajduje się w krokach `thought` oraz we wszystkich krokach wywołań narzędzi (np. `function_call`) i wyników (np. `function_response`) w przypadku modeli Gemini 3 i nowszych. Ten zaszyfrowany kontekst umożliwia **cyrkulację kontekstu narzędzia** w ramach interakcji.

**Zarządzanie tymi polami:**

- **Tryb stanowy (zalecany)**: gdy używasz `previous_interaction_id`, serwer automatycznie obsługuje pola `id` i `signature`.
- **Tryb bezstanowy**: podczas ręcznego zarządzania historią rozmów musisz się upewnić, że w kolejnych żądaniach przekazujesz do modelu zarówno pole `id`, jak i `signature`, aby zweryfikować autentyczność i zachować kontekst. Oficjalne pakiety SDK obsługują to automatycznie, jeśli przekazujesz pełny obiekt odpowiedzi do historii.

### Dane specyficzne dla narzędzia

Niektóre narzędzia wbudowane zwracają argumenty danych widoczne dla użytkownika, które są specyficzne dla typu narzędzia.

| Narzędzie | Argumenty wywołania narzędzia widoczne dla użytkownika (jeśli występują) | Odpowiedź narzędzia widoczna dla użytkownika (jeśli występuje) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` Adresy URL do przeglądania | `status`: stan przeglądania `retrieved_url`: przeglądane adresy URL |
| **file\_search** | Brak | Brak |

## Tokeny i ceny

Pamiętaj, że części wywołań narzędzi wbudowanych w żądaniach są wliczane do `prompt_token_count`. Ponieważ te pośrednie kroki narzędzi są teraz widoczne i zwracane, stanowią część historii rozmów. Dotyczy to tylko
przypadku *żądań*, a nie *odpowiedzi*.

Wyjątkiem od tej reguły jest narzędzie wyszukiwarki Google. Wyszukiwarka Google stosuje już
własny model cenowy na poziomie zapytania, więc tokeny nie są
naliczane podwójnie (patrz strona [Ceny](https://ai.google.dev/gemini-api/docs/pricing?hl=pl)).

Więcej informacji znajdziesz na stronie [Tokeny](https://ai.google.dev/gemini-api/docs/tokens?hl=pl).

## Ograniczenia

- Gdy włączona jest cyrkulacja kontekstu narzędzia, domyślnie używaj trybu `validated` (tryb `auto` nie jest obsługiwany).
- Narzędzia wbudowane, takie jak `google_search`, korzystają z informacji o lokalizacji i aktualnej godzinie. Jeśli więc w `system_instruction` lub `function_declaration.description` występują sprzeczne informacje o lokalizacji i czasie, funkcja łączenia narzędzi może nie działać prawidłowo.

## Obsługiwane narzędzia

Standardowa cyrkulacja kontekstu narzędzia dotyczy narzędzi po stronie serwera (wbudowanych).
Wykonywanie kodu to też narzędzie po stronie serwera, ale ma własne wbudowane rozwiązanie do cyrkulacji kontekstu. Korzystanie z komputera i wywoływanie funkcji to narzędzia po stronie klienta, które też mają wbudowane rozwiązania do cyrkulacji kontekstu.

| Narzędzie | Strona wykonania | Obsługa cyrkulacji kontekstu |
| --- | --- | --- |
| [Wyszukiwarka Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl) | Po stronie serwera | Obsługiwane |
| [Mapy Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl) | Po stronie serwera | Obsługiwane |
| [Kontekst adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl) | Po stronie serwera | Obsługiwane |
| [Wyszukiwanie plików](https://ai.google.dev/gemini-api/docs/file-search?hl=pl) | Po stronie serwera | Obsługiwane |
| [Wykonywanie kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl) | Po stronie serwera | Obsługiwane (wbudowane, używa kroków `code_execution` i `code_execution_result`) |
| [Korzystanie z komputera](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl) | Po stronie klienta | Obsługiwane (wbudowane, używa kroków `function_call` i `function_response`) |
| [Funkcje niestandardowe](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl) | Po stronie klienta | Obsługiwane (wbudowane, używa kroków `function_call` i `function_response`) |

## Co dalej?

- Dowiedz się więcej o [wywoływaniu funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl) w interfejsie Gemini API.
- Poznaj obsługiwane narzędzia:
  - [Wyszukiwarka Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl)
  - [Mapy Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl)
  - [Kontekst adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl)
  - [Wyszukiwanie plików](https://ai.google.dev/gemini-api/docs/file-search?hl=pl)

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
