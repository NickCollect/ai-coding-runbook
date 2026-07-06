---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/priority-inference?hl=pl
fetched_at: 2026-07-06T05:17:29.796783+00:00
title: "Wnioskowanie o\u00a0priorytecie \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Wnioskowanie o priorytecie

Opis: jak zoptymalizować czas oczekiwania dzięki warstwie wnioskowania Priority

Gemini Priority API to warstwa wnioskowania Premium przeznaczona do zbiorów zadań o kluczowym znaczeniu dla firmy, które wymagają krótszego czasu oczekiwania i najwyższej niezawodności w cenie Premium. Ruch w warstwie Priority ma wyższy priorytet niż ruch w standardowym interfejsie API i warstwie Flex.

Wnioskowanie Priority jest dostępne dla użytkowników [warstwy 2 i 3](https://ai.google.dev/gemini-api/docs/billing?hl=pl#about-billing) w przypadku punktów końcowych interfejsu GenerateContent API
i Interactions API.

## Jak korzystać z warstwy Priority

Aby korzystać z warstwy Priority, ustaw w treści żądania wartość `priority` w polu `service_tier`. Jeśli to pole zostanie pominięte, domyślną warstwą będzie Standard.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3.5-flash",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## Jak działa wnioskowanie Priority

Wnioskowanie Priority kieruje żądania do kolejek obliczeniowych o wysokim priorytecie, co zapewnia przewidywalną i szybką wydajność w przypadku aplikacji dostępnych dla użytkowników. Jego głównym mechanizmem jest łagodna degradacja po stronie serwera do standardowego przetwarzania w przypadku ruchu, który przekracza limity dynamiczne. Dzięki temu aplikacja zachowuje stabilność, a żądanie nie jest odrzucane.

| Funkcja | Priorytet | Standardowe | Flex | Wsad |
| --- | --- | --- | --- | --- |
| **Ceny** | 75–100% więcej niż w przypadku warstwy Standard | Bilet normalny | 50% rabatu | 50% rabatu |
| **Czas oczekiwania** | Sekundy | Sekundy do minut | Minuty (docelowo 1–15 min) | Do 24 godzin |
| **Niezawodność** | Wysoka (nie można jej obniżyć) | Wysoka / średnio wysoka | Bez gwarancji (można ją obniżyć) | Wysoka (w przypadku przepustowości) |
| **Interfejs** | Synchroniczna | Synchroniczna | Synchroniczna | Asynchroniczny |

### Główne korzyści

- **Krótki czas oczekiwania**: zaprojektowana pod kątem czasu odpowiedzi w sekundach w przypadku interaktywnych,
  narzędzi AI dostępnych dla użytkowników.
- **Wysoka niezawodność**: ruch jest traktowany z najwyższym priorytetem i jest
  ściśle nieobniżalny.
- **Łagodna degradacja**: w przypadku nagłego wzrostu ruchu przekraczającego limity dynamiczne następuje
  automatyczne obniżenie do warstwy Standard, co zapobiega przerwom w działaniu usługi.
- **Niewielkie utrudnienia**: używa tej samej synchronicznej `generateContent` metody co
  warstwy Standard i Flex.

### Przypadki użycia

Przetwarzanie Priority jest idealne w przypadku zbiorów zadań o kluczowym znaczeniu dla firmy, w których najważniejsza jest wydajność i niezawodność.

- **Interaktywne aplikacje AI**: czatboty i asystenci obsługi klienta, w przypadku których
  użytkownicy płacą więcej i oczekują szybkich, spójnych odpowiedzi.
- **Silniki podejmowania decyzji w czasie rzeczywistym**: systemy wymagające wysoce niezawodnych wyników o niskim czasie oczekiwania
  , takich jak triage zgłoszeń na żywo czy wykrywanie oszustw.
- **Funkcje Premium dla klientów**: deweloperzy, którzy muszą zagwarantować wyższe cele poziomu usług (SLO) dla płacących klientów.

### Ograniczenia liczby żądań

Zużycie Priority ma własne ograniczenia liczby żądań, mimo że jest wliczane do [ogólnych ograniczeń liczby żądań dotyczących ruchu interaktywnego](https://aistudio.google.com/rate-limit?hl=pl). Domyślne ograniczenia liczby żądań w przypadku wnioskowania Priority to **0,3-krotność standardowego ograniczenia liczby żądań dla modelu / warstwy**.

### Logika łagodnego obniżania jakości

Jeśli limity Priority zostaną przekroczone z powodu przeciążenia, żądania przekraczające limit zostaną **automatycznie i łagodnie** obniżone do standardowego przetwarzania zamiast odrzucenia z błędem 503 lub 429. Żądania o obniżonym priorytecie są rozliczane według stawki standardowej, a nie stawki Premium Priority.

### Odpowiedzialność klienta

- **Monitorowanie odpowiedzi**: deweloperzy powinni monitorować `x-gemini-service-tier`
  nagłówek w odpowiedzi interfejsu API, aby wykryć, czy żądania są często obniżane do poziomu
  `standard`.
- **Ponawianie prób**: klienci muszą wdrożyć logikę ponawiania prób/wzrastający czas do ponowienia w przypadku standardowych błędów, takich jak `DEADLINE_EXCEEDED`.

## Ceny

Wnioskowanie Priority jest o 75–100% droższe niż [standardowy interfejs API](https://ai.google.dev/gemini-api/docs/pricing?hl=pl) i jest rozliczane za token.

## Obsługiwane modele

Wnioskowanie Priority jest obsługiwane w tych modelach:

| Model | Wnioskowanie Priority |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=pl) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl) | ✔️ |
| [Gemini 3.1 Pro (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pl) | ✔️ |
| [Gemini 3 Flash (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pl) | ✔️ |
| [Gemini 3 Pro Image (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=pl) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pl) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pl) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=pl) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pl) | ✔️ |

## Co dalej?

Przeczytaj o innych opcjach [wnioskowania i optymalizacji](https://ai.google.dev/gemini-api/docs/optimization?hl=pl) Gemini:

- [Wnioskowanie Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pl), które pozwala obniżyć koszty o 50%.
- [Interfejs Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl) do przetwarzania asynchronicznego w ciągu 24 godzin.
- [Buforowanie kontekstu](https://ai.google.dev/gemini-api/docs/caching?hl=pl), które pozwala obniżyć koszty tokenów wejściowych.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-23 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-23 UTC."],[],[]]
