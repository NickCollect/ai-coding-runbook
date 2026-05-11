---
source_url: https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=pl
fetched_at: 2026-05-11T04:57:37.412467+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Wnioskowanie o priorytecie

Interfejs Gemini Priority API to poziom wnioskowania premium przeznaczony dla krytycznych zbiorów zadań biznesowych, które wymagają mniejszego opóźnienia i najwyższej niezawodności w wyższym pułapie cenowym. Ruch w ramach warstwy Priority ma wyższy priorytet niż ruch w ramach standardowego interfejsu API i warstwy Flex.

Wnioskowanie priorytetowe jest dostępne we wszystkich punktach końcowych interfejsu Interactions API.

## Jak korzystać z priorytetu

Aby używać poziomu priorytetu, ustaw w żądaniu pole `service_tier` na `priority`. Jeśli to pole zostanie pominięte, domyślnym poziomem będzie standardowy.

### Python

```
from google import genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input="Triage this critical customer support ticket immediately.",
        service_tier='priority'
    )

    # Validate for graceful downgrade
    # Note: Checking headers might vary by SDK implementation, this is illustrative
    # if interaction.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
    #     print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(interaction.steps[-1].content[0].text)

except Exception as e:
    print(f"Error during API call: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const interaction = await ai.interactions.create({
          model: "gemini-3-flash-preview",
          input: "Triage this critical customer support ticket immediately.",
          service_tier: "priority"
      });

      // Validate for graceful downgrade
      // if (interaction.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
      //     console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      // }

      console.log(interaction.steps.at(-1).content[0].text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## Jak działa wnioskowanie priorytetowe

Routowanie wnioskowania priorytetowego kieruje żądania do kolejek obliczeniowych o wysokim znaczeniu, zapewniając przewidywalną i szybką wydajność w przypadku aplikacji dostępnych dla użytkowników. Jego głównym mechanizmem jest płynne przejście po stronie serwera do standardowego przetwarzania w przypadku ruchu, który przekracza dynamiczne limity, co zapewnia stabilność aplikacji zamiast odrzucania żądania.

| Funkcja | Priorytet | Standardowe | Flex | Wsad |
| --- | --- | --- | --- | --- |
| **Ceny** | 75–100% więcej niż w przypadku wersji Standard | Bilet normalny | 50% zniżki | 50% zniżki |
| **Opóźnienie** | Sekundy | Sekundy na minuty | Minuty (docelowo 1–15 min) | Do 24 godzin |
| **Niezawodność** | Wysoka (niezrzucająca sierści) | Wysoka / dość wysoka | Możliwie najlepsza obsługa (z możliwością odrzucenia) | Wysoki (dla przepustowości) |
| **Interfejs** | Synchroniczna | Synchroniczna | Synchroniczna | Asynchroniczny |

### Główne zalety

- **Niskie opóźnienie:** zaprojektowany z myślą o czasie reakcji wynoszącym kilka sekund w przypadku interaktywnych narzędzi AI przeznaczonych dla użytkowników.
- **Wysoka niezawodność:** ruch jest traktowany jako najważniejszy i nie może być odrzucany.
- **Łagodna degradacja:** skoki ruchu przekraczające dynamiczne limity są automatycznie obniżane do poziomu Standard w celu przetworzenia zamiast powodować błędy, co zapobiega przerwom w działaniu usługi.
- **Niskie tarcie:** korzysta z tej samej synchronicznej metody `create` co w przypadku poziomów standardowego i Flex.

### Przypadki użycia

Przetwarzanie priorytetowe jest idealne w przypadku procesów o kluczowym znaczeniu dla firmy, w których wydajność i niezawodność mają największe znaczenie.

- **Interaktywne aplikacje AI:** czatboty i kopiloty obsługi klienta, w przypadku których użytkownicy płacą wyższą cenę i oczekują szybkich, spójnych odpowiedzi.
- **Silniki decyzyjne działające w czasie rzeczywistym:** systemy wymagające bardzo wiarygodnych wyników o niskim poziomie opóźnień, takie jak systemy triage zgłoszeń lub wykrywania oszustw.
- **Funkcje dla klientów premium:** deweloperzy, którzy muszą zagwarantować wyższe docelowe poziomy usług (SLO) dla klientów płacących.

### Ograniczenia liczby żądań

Zużycie priorytetowe ma własne limity szybkości, mimo że jest wliczane do [ogólnych limitów szybkości ruchu interaktywnego](https://aistudio.google.com/rate-limit?hl=pl). Domyślne limity szybkości
dla wnioskowania priorytetowego to **0,3x standardowego limitu szybkości dla modelu lub poziomu**.

### Logika przejścia na niższą wersję

Jeśli limity priorytetowe zostaną przekroczone z powodu przeciążenia, nadmiarowe żądania zostaną **automatycznie i bezproblemowo** obniżone do przetwarzania standardowego zamiast zwracać błąd 503 lub 429. Obniżone żądania są rozliczane według stawki standardowej, a nie według stawki premium Priority.

### Odpowiedzialność klienta

- **Monitorowanie odpowiedzi:** deweloperzy powinni monitorować `x-gemini-service-tier`nagłówek w odpowiedzi interfejsu API, aby wykrywać, czy żądania są często obniżane do poziomu`standard`.
- **Ponowne próby:** klienci muszą wdrożyć logikę ponawiania prób lub wzrastający czas do ponowienia w przypadku standardowych błędów, takich jak `DEADLINE_EXCEEDED`.

## Ceny

Wnioskowanie priorytetowe jest o 75–100% droższe niż [standardowy interfejs API](https://ai.google.dev/gemini-api/docs/pricing?hl=pl) i jest rozliczane za token.

## Obsługiwane modele

Priorytetowe wnioskowanie jest obsługiwane w tych modelach:

| Model | Wnioskowanie o priorytecie |
| --- | --- |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl) | ✔️ |
| [Gemini 3.1 Flash-Lite (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=pl) | ✔️ |
| [Gemini 3.1 Pro (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pl) | ✔️ |
| [Gemini 3 Flash (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pl) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pl) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pl) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pl) | ✔️ |

## Co dalej?

- [Elastyczne wnioskowanie](https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=pl) w celu obniżenia kosztów.
- [Tokeny:](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=pl) dowiedz się więcej o tokenach.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-09 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-09 UTC."],[],[]]
