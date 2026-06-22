---
source_url: https://ai.google.dev/gemini-api/docs/zdr?hl=pl
fetched_at: 2026-06-22T06:30:46.048457+00:00
title: "Brak przechowywania danych w\u00a0interfejsie Gemini Developer API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Brak przechowywania danych w interfejsie Gemini Developer API

Na tej stronie znajdziesz szczegółowe informacje o tzw. „zerowym przechowywaniu danych” w interfejsie Gemini Developer API.

## Ograniczenie trenowania

Zgodnie z [Warunkami korzystania z Gemini API](https://ai.google.dev/gemini-api/terms?hl=pl), gdy korzystasz z usług płatnych, Google nie używa Twoich promptów (w tym powiązanych instrukcji systemowych, treści w pamięci podręcznej i plików, takich jak obrazy, filmy czy dokumenty) ani odpowiedzi do ulepszania naszych usług. Usługi płatne są zdefiniowane [tutaj](https://ai.google.dev/gemini-api/terms?hl=pl#paid-services).

## Przechowywanie danych klientów i osiąganie zerowego poziomu przechowywania danych

Dane klientów są zwykle przechowywane przez ograniczony czas w tych sytuacjach i na tych warunkach: Aby osiągnąć zerowy okres przechowywania danych, klienci muszą podjąć określone działania lub unikać określonych funkcji w każdym z tych obszarów:

- **Rejestrowanie promptów na potrzeby monitorowania nadużyć**: zgodnie z [Dodatkowymi warunkami korzystania z usług Gemini API](https://ai.google.dev/gemini-api/terms?hl=pl) w przypadku usług płatnych Google rejestruje prompty i odpowiedzi przez ograniczony czas wyłącznie w celu wykrywania naruszeń [zasad dotyczących niedozwolonych zastosowań](https://policies.google.com/terms/generative-ai/use-policy?hl=pl). Gdy Twoja prośba o ZDR w przypadku konkretnego projektu zostanie zatwierdzona, wszystkie treści użytkowników (prompty i odpowiedzi) oraz metadane umożliwiające identyfikację (takie jak adresy IP i identyfikatory kont Google) zostaną usunięte przed rejestrowaniem. Powstały rekord jest oznaczony jako oczyszczony i nie zawiera żadnych danych użytkownika możliwego do zidentyfikowania, co zapewnia zgodność z platformą agentów Gemini Enterprise z zerowym okresem przechowywania danych.
- **Powiązanie ze źródłem informacji przy użyciu wyszukiwarki Google**: zgodnie z [Dodatkowymi warunkami korzystania z Gemini API](https://ai.google.dev/gemini-api/terms?hl=pl#grounding-with-google-search) Google przechowuje prompty, informacje kontekstowe i wygenerowane dane wyjściowe przez 30 dni w celu tworzenia wyników opartych na powiązaniu ze źródłem informacji i sugestii wyszukiwania.
  Te zapisane informacje mogą być używane do debugowania i testowania systemów obsługujących uziemienie. **Jeśli korzystasz z powiązania ze źródłem informacji przy użyciu wyszukiwarki Google, nie możesz wyłączyć zapisywania tych informacji.**
- **Powiązanie ze źródłem informacji przy użyciu Map Google**: zgodnie z [Dodatkowymi warunkami korzystania z Gemini API](https://ai.google.dev/gemini-api/terms?hl=pl) Google przechowuje prompty, informacje kontekstowe i wygenerowane dane wyjściowe przez 30 dni w celu tworzenia powiązanych ze źródłem informacji wyników. Te przechowywane informacje mogą być używane wyłącznie do celów związanych z inżynierią niezawodności, np. do debugowania w przypadku problemów z usługą.
  **Jeśli korzystasz z powiązania ze źródłem informacji przy użyciu Map Google, nie możesz wyłączyć przechowywania tych informacji.**
- **Interfejs Interactions API:** zarządza aktywnym stanem rozmowy, aby umożliwić wielokrotne tury. **Domyślnie interfejs Interactions API umożliwia przechowywanie stanu**. Aby zapewnić brak śladu danych, musisz w żądaniach do interfejsu API wyraźnie ustawić parametr `store` na `false`, aby zrezygnować z domyślnego przechowywania stanu.
- **Live API**: ten interfejs API z zachowywaniem stanu umożliwia ponowne połączenie w czasie rzeczywistym dzięki przechowywaniu stanu rozmowy. Aby osiągnąć zerowy okres przechowywania danych, **nie konfiguruj
  SessionResumptionConfig**. Jeśli zostanie wygenerowany identyfikator sesji, stan rozmowy (w tym tekst, dźwięk i wideo) jest przechowywany przez maksymalnie 24 godziny.
- **File API Storage**: interfejs File API umożliwia użytkownikom przesyłanie dużych zasobów.
  Pliki są przechowywane w stanie spoczynku, dopóki nie zostaną usunięte przez użytkownika lub nie wygasną.
  Korzystanie z interfejsu File API jest niezależne od rejestrowania ZDR. Aby zapewnić brak śladów danych, użytkownicy muszą ręcznie usuwać pliki.
- **Jawne buforowanie kontekstu:** użytkownicy mogą ręcznie buforować duże zbiory danych (np. długie filmy lub biblioteki dokumentów) za pomocą pola `cached_content`. Chociaż dzienniki tych żądań są zgodne z zasadami usuwania danych ZDR, sam kontekst zapisany w pamięci podręcznej jest przechowywany z określonym przez użytkownika `ttl` lub `expire_time`. Aby osiągnąć absolutne zero danych, nie korzystaj z funkcji cached\_content.
- **Niejawne buforowanie w pamięci:** domyślnie modele Gemini buforują dane w pamięci, aby zmniejszyć opóźnienia i koszty dla deweloperów. Te dane są przechowywane wyłącznie w pamięci RAM (nie w spoczynku), są odizolowane na poziomie projektu i mają 24-godzinny czas życia.
  **Nie narusza to zasady zerowego przechowywania danych.**

## Co dalej?

- Dowiedz się więcej o [zasadach dotyczących niedozwolonych zastosowań generatywnej AI](https://policies.google.com/terms/generative-ai/use-policy?hl=pl).
- Zapoznaj się z [Dodatkowymi warunkami korzystania z Gemini API](https://ai.google.dev/gemini-api/terms?hl=pl).
- Jeśli potrzebujesz ustawień ZDR klasy korporacyjnej, które możesz samodzielnie konfigurować, zapoznaj się z [przewodnikiem po platformie agentów Gemini Enterprise
  Zero Data Retention](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-28 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-28 UTC."],[],[]]
