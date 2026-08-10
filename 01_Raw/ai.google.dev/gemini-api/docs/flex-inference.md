---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=pl
fetched_at: 2026-08-10T03:12:53.370527+00:00
title: "Elastyczne wnioskowanie \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Elastyczne wnioskowanie

Gemini Flex API to poziom wnioskowania, który oferuje 50% obniżkę kosztów w porównaniu ze stawkami standardowymi w zamian za zmienne opóźnienie i dostępność bez gwarancji. Jest on przeznaczony do zbiorów zadań, które są odporne na opóźnienia i wymagają przetwarzania synchronicznego, ale nie potrzebują wydajności w czasie rzeczywistym, jaką zapewnia standardowy interfejs API.

## Jak korzystać z Flex

Aby korzystać z poziomu Flex, w żądaniu określ `service_tier` jako `flex`. Jeśli to pole zostanie pominięte, żądania będą domyślnie korzystać z poziomu standardowego.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Analyze this dataset for trends...",
    service_tier='flex'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: 'gemini-3.6-flash',
        input: 'Analyze this dataset for trends...',
        service_tier: 'flex'
    });
    console.log(interaction.output_text);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## Jak działa wnioskowanie Flex

Wnioskowanie Gemini Flex wypełnia lukę między standardowym interfejsem API a 24-godzinnym
czasem realizacji interfejsu [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl). Wykorzystuje ono moc obliczeniową poza godzinami szczytu, którą można wyłączyć, aby zapewnić ekonomiczne rozwiązanie dla zadań wykonywanych w tle i sekwencyjnych przepływów pracy.

| Funkcja | Flex | Priorytet | Standardowe | Wsad |
| --- | --- | --- | --- | --- |
| **Ceny** | 50% rabatu | 75–100% więcej niż w przypadku poziomu standardowego | Bilet normalny | 50% rabatu |
| **Opóźnienie** | Minuty (docelowo 1–15 min) | Niskie (sekundy) | Sekundy do minut | Do 24 godzin |
| **Niezawodność** | Bez gwarancji (możliwość wyłączenia) | Wysoka (bez możliwości wyłączenia) | Wysoka / średnio wysoka | Wysoka (w przypadku przepustowości) |
| **Interfejs** | Synchroniczna | Synchroniczna | Synchroniczna | Asynchroniczny |

### Główne korzyści

- **Opłacalność**: znaczne oszczędności w przypadku ocen nieprodukcyjnych, agentów działających w tle i wzbogacania danych.
- **Niewielkie utrudnienia**: wystarczy dodać jeden parametr do istniejących żądań.
- **Synchroniczne przepływy pracy**: idealne do sekwencyjnych łańcuchów interfejsów API, w których kolejne żądanie zależy od wyniku poprzedniego, co sprawia, że jest bardziej elastyczne niż w przypadku zbiorów zadań.

### Przypadki użycia

- **Oceny offline**: przeprowadzanie testów regresyjnych lub tworzenie tabel wyników „LLM-as-a-judge”.
- **Agenci działający w tle**: zadania sekwencyjne, takie jak aktualizacje CRM, tworzenie profili lub moderowanie treści, w których dopuszczalne są kilkuminutowe opóźnienia.
- **Badania z ograniczonym budżetem**: eksperymenty akademickie, które wymagają dużej liczby tokenów przy ograniczonym budżecie.

### Ograniczenia liczby żądań

Ruch związany z wnioskowaniem Flex wlicza się do ogólnych [limitów liczby żądań](https://aistudio.google.com/rate-limit?hl=pl). Nie oferuje on
rozszerzonych limitów liczby żądań, takich jak [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl).

### Możliwość wyłączenia

Ruch Flex jest traktowany z niższym priorytetem. Jeśli nastąpi wzrost ruchu standardowego, żądania Flex mogą zostać wywłaszczone lub usunięte, aby zapewnić zasoby użytkownikom o wysokim priorytecie. Jeśli szukasz wnioskowania o wysokim priorytecie, sprawdź
[wnioskowanie priorytetowe](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl)

### Kody błędów

Gdy zasoby Flex są niedostępne lub system jest przeciążony, interfejs API zwraca standardowe kody błędów:

- **503 Usługa niedostępna**: system jest obecnie zajęty.
- **429 Zbyt wiele żądań**: limity liczby żądań lub wyczerpanie zasobów.

### Odpowiedzialność klienta

- **Brak rezerwowego serwera**: aby zapobiec nieoczekiwanym opłatom, system nie będzie
  automatycznie uaktualniać żądania Flex do poziomu standardowego, jeśli zasoby Flex są
  wyczerpane.
- **Ponowne próby**: musisz zaimplementować własną logikę ponawiania prób po stronie klienta z wzrastającym czasem do ponowienia.
- **Limity czasu**: ponieważ żądania Flex mogą znajdować się w kolejce, zalecamy
  zwiększenie limitów czasu po stronie klienta do co najmniej 10 minut, aby uniknąć przedwczesnego
  zamknięcia połączenia.

## Dostosowywanie limitów czasu

Limity czasu dla poszczególnych żądań możesz skonfigurować w przypadku interfejsu REST API i bibliotek klienta.
Zawsze upewnij się, że limit czasu po stronie klienta obejmuje zamierzony czas oczekiwania serwera (np. 600 s lub więcej w przypadku kolejek oczekiwania Flex). Pakiety SDK oczekują wartości limitu czasu w milisekundach.

### Limity czasu dla poszczególnych żądań

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="why is the sky blue?",
    service_tier="flex",
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: "gemini-3.6-flash",
        input: "why is the sky blue?",
        service_tier: "flex",
    }, {timeout: 900000});
}

await main();
```

## Wdrażanie ponownych prób

Ponieważ Flex można wyłączyć i zwraca błędy 503, poniżej znajdziesz przykład opcjonalnego wdrożenia logiki ponawiania prób, aby kontynuować nieudane żądania:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.6-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.6-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.6-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.6-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

## Ceny

Wnioskowanie Flex jest wyceniane na 50% [standardowego interfejsu API](https://ai.google.dev/gemini-api/docs/pricing?hl=pl)
i rozliczane za token.

## Obsługiwane modele

Wnioskowanie Flex jest obsługiwane przez te modele:

| Model | Wnioskowanie Flex |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=pl) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=pl) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=pl) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl) | ✔️ |
| [Gemini 3.1 Pro (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pl) | ✔️ |
| [Gemini 3 Flash (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pl) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pl) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pl) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pl) | ✔️ |

## Co dalej?

- [Wnioskowanie priorytetowe](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl) w przypadku bardzo małych opóźnień.
- [Tokeny](https://ai.google.dev/gemini-api/docs/tokens?hl=pl): dowiedz się więcej o tokenach.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
