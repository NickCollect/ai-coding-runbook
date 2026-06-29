---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=pl
fetched_at: 2026-06-29T05:32:24.655422+00:00
title: "Elastyczne wnioskowanie \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Elastyczne wnioskowanie

Gemini Flex API to poziom wnioskowania, który oferuje o 50% niższe koszty w porównaniu ze stawkami standardowymi. W zamian za to zapewnia zmienne opóźnienie i dostępność na zasadzie „najlepszej jakości”. Jest przeznaczony do zadań, które są odporne na opóźnienia i wymagają przetwarzania synchronicznego, ale nie potrzebują wydajności w czasie rzeczywistym, jaką zapewnia standardowy interfejs API.

## Jak korzystać z Flex

Aby używać warstwy Flex, w żądaniu określ `service_tier` jako `flex`. Jeśli to pole zostanie pominięte, żądania będą domyślnie korzystać z poziomu standardowego.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
        model: 'gemini-3.5-flash',
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
      "model": "gemini-3.5-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## Jak działa wnioskowanie Flex

Wnioskowanie Gemini Flex wypełnia lukę między standardowym interfejsem API a 24-godzinnym czasem realizacji [interfejsu Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl). Wykorzystuje moc obliczeniową poza godzinami szczytu, którą można „odłączyć”, aby zapewnić ekonomiczne rozwiązanie do zadań w tle i sekwencyjnych przepływów pracy.

| Funkcja | Flex | Priorytet | Standardowe | Wsad |
| --- | --- | --- | --- | --- |
| **Ceny** | 50% zniżki | 75–100% więcej niż w przypadku wersji Standard | Pełna cena | 50% zniżki |
| **Opóźnienie** | Minuty (docelowo 1–15 minut) | Niska (sekundy) | Sekundy na minuty | Do 24 godzin |
| **Niezawodność** | Możliwie najlepsza obsługa (możliwość odrzucenia) | Wysoka (nie gubią sierści) | Wysoki / dość wysoki | Wysoki (przepustowość) |
| **Interfejs** | Synchroniczna | Synchroniczna | Synchroniczna | Asynchroniczny |

### Główne zalety

- **Oszczędność kosztów:** znaczne oszczędności w przypadku ocen środowisk nieprodukcyjnych, agentów działających w tle i wzbogacania danych.
- **Łatwe wdrożenie:** wystarczy dodać jeden parametr do istniejących żądań.
- **Synchroniczne procesy**: idealne w przypadku sekwencyjnych łańcuchów interfejsów API, w których kolejne żądanie zależy od wyniku poprzedniego, co czyni je bardziej elastycznymi niż procesy wsadowe w przypadku procesów agentowych.

### Przypadki użycia

- **Oceny offline:** przeprowadzanie testów regresji lub tworzenie tabel wyników z użyciem dużego modelu językowego jako sędziego.
- **Agenci działający w tle:** sekwencyjne zadania, takie jak aktualizacje CRM, tworzenie profili czy moderowanie treści, w przypadku których dopuszczalne są kilkuminutowe opóźnienia.
- **Badania z ograniczonym budżetem:** eksperymenty akademickie, które wymagają dużej liczby tokenów przy ograniczonym budżecie.

### Ograniczenia liczby żądań

Ruch związany z elastycznym wnioskowaniem jest wliczany do ogólnych [limitów szybkości](https://aistudio.google.com/rate-limit?hl=pl). Nie oferuje on rozszerzonych limitów szybkości, takich jak [interfejs Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl).

### Rozmiar z możliwością zmniejszenia

Ruch elastyczny jest traktowany z niższym priorytetem. Jeśli nastąpi nagły wzrost standardowego ruchu, żądania Flex mogą zostać wyprzedzone lub usunięte, aby zapewnić przepustowość użytkownikom o wysokim priorytecie. Jeśli szukasz wnioskowania o wysokim priorytecie, zapoznaj się z sekcją [Wnioskowanie priorytetowe](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl).

### Kody błędów

Gdy elastyczna przepustowość jest niedostępna lub system jest przeciążony, interfejs API zwraca standardowe kody błędów:

- **503 Usługa niedostępna:** system jest obecnie zajęty.
- **429 Zbyt wiele żądań:** przekroczono limity częstotliwości lub wyczerpano zasoby.

### Odpowiedzialność klienta

- **Brak opcji zapasowej po stronie serwera:** aby zapobiec nieoczekiwanym opłatom, system nie będzie automatycznie uaktualniać żądania Flex do poziomu Standard, jeśli pula Flex jest pełna.
- **Ponowne próby:** musisz wdrożyć własną logikę ponownych prób po stronie klienta ze wzrastającym czasem do ponowienia.
- **Przekroczenia limitu czasu:** ponieważ żądania elastyczne mogą znajdować się w kolejce, zalecamy zwiększenie limitów czasu po stronie klienta do co najmniej 10 minut, aby uniknąć przedwczesnego zamknięcia połączenia.

## Dostosowywanie okien limitu czasu

Możesz skonfigurować limity czasu dla poszczególnych żądań w przypadku interfejsu REST API i bibliotek klienta.
Zawsze upewnij się, że limit czasu po stronie klienta obejmuje zamierzony okres oczekiwania serwera (np. ponad 600 s w przypadku elastycznych kolejek oczekiwania). Pakiety SDK oczekują wartości czasu oczekiwania w milisekundach.

### Limity czasu poszczególnych żądań

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
        model: "gemini-3.5-flash",
        input: "why is the sky blue?",
        service_tier: "flex",
    }, {timeout: 900000});
}

await main();
```

## Wdrażanie ponownych prób

Usługa Flex jest podatna na błędy i może zwracać błędy 503. Oto przykład opcjonalnego wdrożenia logiki ponawiania, aby kontynuować obsługę nieudanych żądań:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.5-flash",
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
                    model="gemini-3.5-flash",
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
        model: "gemini-3.5-flash",
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
          model: "gemini-3.5-flash",
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

Wnioskowanie elastyczne kosztuje 50% [standardowej ceny interfejsu API](https://ai.google.dev/gemini-api/docs/pricing?hl=pl) i jest rozliczane za token.

## Obsługiwane modele

Te modele obsługują wnioskowanie Flex:

| Model | Elastyczne wnioskowanie |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=pl) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl) | ✔️ |
| [Gemini 3.1 Pro (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pl) | ✔️ |
| [Gemini 3 Flash (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pl) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pl) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pl) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pl) | ✔️ |

## Co dalej?

- [Wnioskowanie o priorytecie](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl) w przypadku bardzo małego opóźnienia.
- [Tokeny:](https://ai.google.dev/gemini-api/docs/tokens?hl=pl) dowiedz się więcej o tokenach.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-22 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-22 UTC."],[],[]]
