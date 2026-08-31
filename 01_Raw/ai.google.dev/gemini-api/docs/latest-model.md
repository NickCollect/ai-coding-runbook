---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=pl
fetched_at: 2026-08-31T06:41:57.605777+00:00
title: "Z\u00a0u\u017cyciem najnowszych modeli Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Z użyciem najnowszych modeli Gemini

[Ta strona](#)
[3.5 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=pl)

Modele Gemini 3.6 Flash (`gemini-3.6-flash`) i Gemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`) są ogólnie dostępne i gotowe do użycia w środowisku produkcyjnym.

- **Gemini 3.6 Flash**: większa skuteczność w złożonych zadaniach agentowych i multimodalnych przy mniejszym zużyciu tokenów i niższej cenie niż w przypadku modelu 3.5 Flash.
- **Gemini 3.5 Flash-Lite**: najszybszy i najtańszy model z rodziny 3.5. W przypadku wykonywania zadań z dużą przepustowością przewyższa poprzednie generacje modelu Flash-Lite.

Z tego przewodnika dowiesz się, co nowego jest w każdym modelu, jakie zmiany w interfejsie API wpływają na Twój kod i jak przeprowadzić migrację.

### Gemini 3.6 Flash

1. Zainstaluj umiejętność:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Zastosuj umiejętność:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. Zainstaluj umiejętność:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Zastosuj umiejętność:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

## Nowe modele

| Model | Identyfikator modelu | Domyślny poziom myślenia | Ceny | Opis |
| --- | --- | --- | --- | --- |
| Gemini 3.6 Flash | `gemini-3.6-flash` | `medium` | 1,50 USD za milion tokenów wejściowych i 7,50 USD za milion tokenów wyjściowych | Łączy szybkość z inteligencją w przypadku zadań agentowych i multimodalnych. |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | `minimal` | 0,30 USD za milion tokenów wejściowych i 2,50 USD za milion tokenów wyjściowych | Najszybszy i najtańszy model 3.5 do wykonywania zadań z dużą przepustowością. |

Oba modele obsługują okno kontekstu o wielkości 1 mln tokenów, maksymalnie 64 tys. tokenów wyjściowych, myślenie i pełny zestaw wbudowanych narzędzi, w tym [korzystanie z komputera](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl).

Pełne specyfikacje znajdziesz na stronach modeli:

- [Strona modelu Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=pl)
- [Strona modelu Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=pl)

Szczegółowe informacje o cenach znajdziesz na [stronie z cennikiem](https://ai.google.dev/gemini-api/docs/pricing?hl=pl).

## Krótkie wprowadzenie

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Write a three.js script that renders an interactive 3D robot."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Write a three.js script that renders an interactive 3D robot.",
  });
  console.log(interaction.outputText);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.6-flash",
    "input": {
      "parts": [{"text": "Write a three.js script that renders an interactive 3D robot."}]
    }
  }'
```

## Co nowego w Gemini 3.6 Flash

- **Mniej tokenów i tur:** wykonuje wieloetapowe przepływy pracy z mniejszą liczbą kroków rozumowania, tur konwersacji i wywołań narzędzi niż Gemini 3.5. Ogranicza też spirale pętli wykonywania.
- **Ulepszone generowanie kodu:** tworzy kod wyższej jakości, gotowy do użycia w środowisku produkcyjnym, z mniejszą liczbą niechcianych zmian i pętli debugowania.
- **Lepsze wykonywanie instrukcji**: ogranicza niechciane zmiany plików podczas zadań diagnostycznych.
- **Zaawansowane rozumowanie multimodalne i przestrzenne:** lepsza skuteczność w interpretacji wykresów, konwersji wizualnych planów i generowaniu układów stron internetowych z wieloma elementami.
- **Wstępna kontrola programowa:** częściej niż Gemini 3.5 Flash preferuje uruchamianie skryptów kodu diagnostycznego przed wprowadzeniem zmian. Zwiększa to dokładność w przypadku złożonych zadań, ale może dodać dodatkowe kroki eksploracyjne w przypadku prostych prac frontendowych.
- **Obsługa korzystania z komputera:** obsługiwana jako natywne narzędzie do automatyzacji interfejsu agenta.
- **Preferencje dotyczące stylizacji interfejsu**: lepiej tworzy kod funkcjonalny, ale osoby oceniające preferowały wcześniejsze modele pod względem układu wizualnego i stylizacji. Możesz temu zapobiec, podając wyraźne wytyczne dotyczące projektowania.
- **Domyślny poziom myślenia (średni):** używa tego samego domyślnego poziomu myślenia `medium` co Gemini 3.5 Flash.
- **Niższe ceny**: niższe koszty tokenów wyjściowych (7,50 USD za milion w porównaniu z 9,00 USD za milion w przypadku modelu 3.5 Flash). Tokeny wejściowe nadal kosztują 1,50 USD za milion.

## Co nowego w Gemini 3.5 Flash-Lite

- **Krótszy czas oczekiwania na wykonanie zadania:** najwyższa przepustowość w rodzinie 3.5 w przypadku analizowania dużych ilości danych i wyodrębniania dokumentów.
- **Ulepszone rozumowanie i skuteczność multimodalna:** dobra ścieżka migracji z Gemini 2.5 Flash, z wyższymi wynikami w zadaniach rozumowania, takich jak HLE (18,0% w porównaniu z 11,0%), i testach porównawczych multimodalnych, takich jak CharXIV (74,5% w porównaniu z 63,7%).
- **Administrowanie subagentami i niezawodność narzędzi:** zwiększa niezawodność wykonywania narzędzi w przypadku wykonywania kodu, wyszukiwania i przepływów pracy MCP. Zwiększ poziom myślenia w przypadku autonomicznego planowania i złożonych zadań subagentów.
- **Lepsze rozumienie dokumentów:** zwiększa dokładność analizowania dokumentów i wyodrębniania uporządkowanych danych. W zależności od złożoności dokumentu eksperymentuj z minimalnym i wysokim poziomem myślenia.
- **Interaktywne kodowanie w internecie i przetwarzanie danych tabelarycznych:** dobrze radzi sobie z przetwarzaniem danych tabelarycznych i JavaScriptu frontendowego dzięki planowaniu za pomocą lekkiego wykonywania kodu.
- **Chatbot i trwałość persony:** lepsze wykonywanie instrukcji wieloetapowych i spójność persony w porównaniu z Gemini 3.1 Flash-Lite.
- **Obsługa korzystania z komputera:** obsługiwana jako natywne narzędzie do automatyzacji interfejsu agenta.

## Wybór odpowiedniego modelu Flash lub Flash-Lite

Użyj tej tabeli, aby wybrać odpowiedni model i ścieżkę migracji dla swoich zbiorów zadań.

Oba modele wymagają usunięcia wycofanych parametrów próbkowania (`temperature`, `top_p`, `top_k`) i wstępnie wypełnionych tur modelu. Więcej informacji znajdziesz w sekcji [Zmiany w interfejsie API](#api-changes-and-parameter-updates).

| Model | Główne przypadki użycia | Zalecany cel migracji |
| --- | --- | --- |
| **Gemini 3.6 Flash** `gemini-3.6-flash` | Generowanie kodu, wnioskowanie przestrzenne/multimodalne, wieloetapowe przepływy pracy agentów | **Gemini 3.5 Flash**, **Gemini 3 Flash (wersja testowa)** lub **Gemini 3.1 Pro** |
| **Gemini 3.5 Flash-Lite** `gemini-3.5-flash-lite` | Autonomiczne wykonywanie zadań przez subagentów, analiza dużych ilości danych i wyodrębnianie dokumentów, analizowanie uporządkowanych danych JSON | **Gemini 3.1 Flash-Lite** lub **Gemini 2.5 Flash** |

## Zaktualizowany agent Antigravity

Ze względu na lepszą skuteczność Gemini 3.6 Flash jest teraz nowym modelem domyślnym, który obsługuje agenta [Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl) w zarządzanych agentach Gemini. Możesz to zmienić, ustawiając nowe pole w interfejsie API.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## Zmiany w interfejsie API i aktualizacje parametrów

Począwszy od modeli Gemini 3.6 Flash i Gemini 3.5 Flash-Lite, te zmiany w interfejsie API dotyczą tych modeli i wszystkich przyszłych wersji modeli Gemini.

- **Wycofanie parametrów próbkowania**: parametry `temperature`, `top_p` i `top_k` zostały wycofane. Interfejs API ignoruje te parametry i w przyszłych generacjach modeli zwraca błąd.
- **Weryfikacja wstępnie wypełnionych tur modelu**: wstępne wypełnianie tur modelu nie jest już obsługiwane. Jeśli ostatnia niepusta tura w żądaniu jest turą `model`, interfejs API zwraca błąd `400`.

Poniżej znajdziesz szczegółowe wyjaśnienia i przykłady kodu dotyczące każdej zmiany w interfejsie API.

### 1. Wycofanie parametrów próbkowania (`temperature`, `top_p`, `top_k`)

Parametry `temperature`, `top_p` i `top_k` zostały wycofane i są ignorowane. W przyszłych generacjach modeli podanie tych parametrów spowoduje zwrócenie błędu HTTP 400. **Usuń te parametry ze wszystkich żądań.**

```
# ⚠️ Remove these parameters (deprecated)
generation_config = {
     "temperature": 0.7,
     "top_p": 0.9,
     "top_k": 40,
}
```

Aby zwiększyć determinizm, zdefiniuj instrukcję systemową z wyraźnymi regułami dotyczącymi konkretnego przypadku użycia.

### 2. Weryfikacja wstępnie wypełnionych tur modelu

Żądania API kończące się niepustą turą roli modelu są niedozwolone i zwracają **błąd HTTP 400**.

#### ⚠️ Unikaj

W starszych wersjach `generateContent` lub surowych ładunkach REST kończenie tury rolą modelu jest teraz niedozwolone:

```
/* ❌ DO NOT: End payload contents with a 'model' role turn */
{
  "contents": [
    {"role": "user", "parts": [{"text": "Translate 'Hello world' to Spanish."}]},
    {"role": "model", "parts": [{"text": "Translation:"}]}  /* ❌ Returns error */
  ]
}
```

#### ✅ Zalecana migracja (interfejs Interactions API)

W interfejsie Interactions API tury modelu nie są wstępnie wypełniane ręcznie. Jeśli Twoja aplikacja wcześniej wstępnie wypełniała turę modelu, aby pominąć wstępy lub wymusić formatowanie JSON, użyj zamiast tego instrukcji systemowej lub [uporządkowanych danych wyjściowych](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl).

```
# ✅ RECOMMENDED: Use system_instruction in the Interactions API to specify output format
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Translate 'Hello world' to Spanish.",
    system_instruction="Output only the translation without introductory text.",
)
```

## Lista kontrolna migracji

### Gemini 3.6 Flash

1. Zainstaluj umiejętność:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Zastosuj umiejętność:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. Zainstaluj umiejętność:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Zastosuj umiejętność:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

### Migracja do gemini-3.6-flash

- **Zaktualizuj identyfikator modelu:** zmień ciąg docelowego modelu na `gemini-3.6-flash`.
- **Usuń wycofane parametry próbkowania:**
  - Usuń parametry `temperature`, `top_p` i `top_k` z konfiguracji generowania.
  - Zastąp `thinking_budget` wyliczeniem ciągu znaków `thinking_level` ustawionym na `"medium"` lub `"high"`.
  - Usuń `candidate_count` (nieobsługiwany w Gemini 3.x).
- **Wymuś reguły weryfikacji tur:**
  - Ujednolicaj rozmowy wieloetapowe po stronie serwera `previous_interaction_id`.
  - Usuń wstępnie wypełnione tury modelu.
- **Sprawdź wywoływanie funkcji:**
  - Umieść zasoby multimodalne w ładunku odpowiedzi.
  - Formatuj instrukcje w tekście za pomocą `\n\n`.
  - Jeśli widzisz błędy `Malformed_Function_Call` związane z tekstem przed narzędziem, zapoznaj się z sekcją [Obejścia wymagań dotyczących tekstu przed narzędziem](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#workarounds-for-pre-tool-text-requirements).
  - Tylko w przypadku korzystania z interfejsu generateContent API: upewnij się, że wszystkie obiekty `FunctionResponse` zawierają `call_id` i `name`.
- **Podstawowe wymagania Gemini 3.x:** informacje o aktualizacjach pakietu SDK i zachowaniu sygnatury myślenia znajdziesz na [liście kontrolnej migracji do Gemini 3.5](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=pl#migration).

### Migracja do gemini-3.5-flash-lite

- **Zaktualizuj identyfikator modelu:** zmień ciąg docelowego modelu na `gemini-3.5-flash-lite`.
- **Skonfiguruj poziom myślenia:**
  - W przypadku wyodrębniania, routingu lub klasyfikacji dużych ilości danych: pozostaw `thinking_level` na poziomie `"minimal"` (domyślnym), aby uzyskać maksymalną przepustowość.
  - W przypadku autonomicznych subagentów z wywołaniami narzędzi, wykonywaniem kodu lub wieloetapowym wnioskowaniem: ustaw `thinking_level` na `"medium"` lub `"high"`, aby zapobiec przedwczesnemu zakończeniu narzędzia.
- **Usuń wycofane parametry i zweryfikuj wywoływanie funkcji:** zastosuj [te same reguły co w przypadku modelu 3.6 Flash](#migrate-to-gemini-3-6-flash).
- **Podstawowe wymagania Gemini 3.x:** zapoznaj się z [listą kontrolną migracji do Gemini 3.5](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=pl#migration).

## Dalsze kroki

- Zapoznaj się ze specyfikacjami interfejsu API w przeglądzie modeli [Models Overview](https://ai.google.dev/gemini-api/docs/models?hl=pl).
- Dowiedz się więcej o administrowaniu wieloma agentami w przewodniku po interfejsie [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pl).
- Testuj i ulepszaj prompty w [Google AI Studio](https://aistudio.google.com/?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
