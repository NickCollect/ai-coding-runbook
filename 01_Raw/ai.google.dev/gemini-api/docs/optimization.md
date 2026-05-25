---
source_url: https://ai.google.dev/gemini-api/docs/optimization?hl=pl
fetched_at: 2026-05-25T05:27:45.908938+00:00
title: "Optymalizacja i\u00a0wnioskowanie w\u00a0interfejsie Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Optymalizacja i wnioskowanie w interfejsie Gemini API

Interfejs Gemini API oferuje różne mechanizmy optymalizacji, które pomagają zachować równowagę między szybkością, kosztem i niezawodnością w zależności od konkretnych potrzeb związanych z obciążeniem.
Niezależnie od tego, czy tworzysz boty konwersacyjne działające w czasie rzeczywistym, czy uruchamiasz złożone potoki przetwarzania danych offline, wybór odpowiedniego paradygmatu może znacznie obniżyć koszty lub zwiększyć wydajność.

| Funkcja | Standardowe | Flex | Priorytet | Wsad | Buforowanie |
| --- | --- | --- | --- | --- | --- |
| **Ceny** | Pełna cena | 50% zniżki | 75–100% więcej niż standardowa | 50% zniżki | 90% rabatu + proporcjonalne miejsce na tokeny |
| **Opóźnienie** | Sekundy na minuty | Minuty (docelowo 1–15 min) | Sekundy | Do 24 godzin | Krótszy czas do pierwszego tokena |
| **Niezawodność** | Wysoka / dość wysoka | Możliwie najlepsza obsługa (z możliwością odrzucenia) | Wysoka (niezrzucająca sierści) | Wysoki (dla przepustowości) | Nie dotyczy |
| **Interfejs** | Synchroniczna | Synchroniczna | Synchroniczna | Asynchroniczny | Stan zapisany |
| **Najlepsze zastosowanie** | Ogólne przepływy pracy aplikacji | Łańcuchy sekwencyjne o niskim priorytecie | Aplikacje produkcyjne przeznaczone dla użytkowników | Ogromne zbiory danych, oceny offline | Powtarzające się zapytania dotyczące tego samego pliku |

## Poziomy usług wnioskowania (synchroniczne)

Możesz przełączać się między ruchem synchronicznym zoptymalizowanym pod kątem niezawodności a ruchem synchronicznym zoptymalizowanym pod kątem kosztów, przekazując parametr `service_tier` w standardowych wywołaniach generowania.

### Standardowe wnioskowanie (domyślne)

Standardowa wersja jest domyślną opcją generowania treści sekwencyjnych.
Zapewnia normalne czasy reakcji bez dodatkowych opłat ani długich kolejek.

- **Niezawodność:** standardowa krytyczność
- **Cena:** standardowa.
- **Najlepsze w przypadku:** najbardziej interaktywnych aplikacji codziennego użytku.

### Wnioskowanie priorytetowe (zoptymalizowane pod kątem czasu oczekiwania)

Przetwarzanie [priorytetowe](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl) kieruje Twoje żądania do kolejek obliczeniowych o wysokim znaczeniu.
Ten ruch jest ściśle niepodlegający przerwaniu (nigdy nie jest wyprzedzany przez inne warstwy) i zapewnia najwyższą niezawodność. Jeśli przekroczysz limity dynamicznego priorytetu, system obniży priorytet żądania do przetwarzania standardowego zamiast zwracać błąd.

- **Niezawodność:** najwyższa krytyczność
- **Cena:** od 75% do 100% wyższa niż stawki standardowe.
- **Najlepsze w przypadku:** chatbotów dla klientów, wykrywania oszustw w czasie rzeczywistym i kluczowych dla firmy asystentów.

### Wnioskowanie Flex (optymalizacja pod kątem kosztów)

[Elastyczne wnioskowanie](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pl) oferuje 50% rabatu
w porównaniu ze stawkami standardowymi dzięki wykorzystaniu
okazjonalnej mocy obliczeniowej poza godzinami szczytu. Żądania są przetwarzane synchronicznie, co oznacza, że nie musisz ponownie pisać kodu, aby zarządzać obiektami zbiorczymi.
Ponieważ jest to ruch „zrzucany”, żądania mogą zostać wyprzedzone, jeśli system odnotuje standardowe skoki ruchu.

- **Niezawodność:** niegwarantowana, z możliwością obniżenia priorytetu
- **Cena:** 50% ceny standardowej (rozliczane za token).
- **Najlepsze rozwiązanie w przypadku:** wieloetapowych procesów opartych na agentach, w których połączenie N+1 zależy od wyniku połączenia N, aktualizacji systemu CRM w tle i ocen offline.

## Batch API (operacje zbiorcze, asynchroniczne)

[Interfejs Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl) został zaprojektowany do asynchronicznego przetwarzania dużych ilości żądań przy 50% standardowego kosztu. Żądania możesz przesyłać jako słowniki wbudowane lub za pomocą pliku wejściowego JSONL (maksymalnie 2 GB). Przetwarza żądania przy użyciu kolejek przepustowości w tle z docelowym czasem realizacji wynoszącym 24 godziny.

- **Niezawodność:** możliwość odrzucenia, ale z automatycznymi ponownymi próbami wysyłania co 24 godziny i systemem kolejkowania.
- **Cena:** 50% ceny standardowej.
- **Najlepsze do:** wstępnego przetwarzania ogromnych zbiorów danych, uruchamiania okresowych pakietów testów regresji i generowania dużej liczby obrazów lub osadzonych danych.

## Buforowanie kontekstu (oszczędność danych wejściowych)

[Buforowanie kontekstu](https://ai.google.dev/gemini-api/docs/caching?hl=pl) jest używane, gdy obszerny kontekst początkowy jest wielokrotnie przywoływany przez krótsze żądania.

- **Pamięć podręczna niejawna:** automatycznie włączona w modelach Gemini 2.5 i nowszych.
  Jeśli Twoja prośba trafi do istniejących pamięci podręcznych na podstawie wspólnych prefiksów promptów, system przekaże Ci oszczędności.
- **Jawne buforowanie:** możesz ręcznie utworzyć obiekt pamięci podręcznej z określonym czasem życia (TTL). Po utworzeniu możesz odwoływać się do tokenów w pamięci podręcznej w przypadku kolejnych żądań, aby uniknąć wielokrotnego przekazywania tego samego ładunku korpusu.
- **Cena:** rozliczana na podstawie liczby tokenów pamięci podręcznej i czasu przechowywania (TTL).
- **Najlepsze rozwiązanie w przypadku:** chatbotów z rozbudowanymi instrukcjami systemowymi, powtarzalnej analizy długich plików wideo lub zapytań dotyczących dużych zbiorów dokumentów.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-04-29 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-04-29 UTC."],[],[]]
