---
source_url: https://ai.google.dev/gemini-api/docs/interactions/caching?hl=pl
fetched_at: 2026-06-01T06:09:00.292255+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Buforowanie kontekstu

W typowym procesie AI możesz wielokrotnie przekazywać te same tokeny wejściowe do modelu. Interfejs Gemini API oferuje niejawne buforowanie, które optymalizuje wydajność i koszty.

## Niejawne buforowanie

Niejawne buforowanie jest domyślnie włączone w przypadku wszystkich modeli Gemini 2.5 i nowszych. Jeśli Twoje żądanie trafi do pamięci podręcznej, automatycznie przekażemy Ci oszczędności. Aby włączyć tę funkcję, nie musisz nic robić. Minimalna liczba tokenów wejściowych w przypadku buforowania kontekstu jest podana w tabeli poniżej dla każdego modelu:

| Model | Minimalny limit tokenów |
| --- | --- |
| Gemini 3.5 Flash | 1024 |
| Gemini 3 Pro (wersja testowa) | 4096 |
| Gemini 2.5 Flash | 1024 |
| Gemini 2.5 Pro | 4096 |

Aby zwiększyć szansę na trafienie w niejawnej pamięci podręcznej:

- Spróbuj umieścić duże i popularne treści na początku prompta.
- Spróbuj wysyłać żądania z podobnym prefiksem w krótkim czasie.

Liczbę tokenów, które zostały trafione do pamięci podręcznej, możesz sprawdzić w polu `usage_metadata` (Python) lub `usageMetadata` (JavaScript) obiektu odpowiedzi.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-28 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-28 UTC."],[],[]]
