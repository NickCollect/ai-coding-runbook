---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=pl
fetched_at: 2026-09-28T06:29:59.414504+00:00
title: "Buforowanie kontekstu \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Buforowanie kontekstu

W typowym procesie AI możesz wielokrotnie przekazywać te same tokeny wejściowe do modelu. Interfejs Gemini API oferuje niejawne buforowanie, które optymalizuje wydajność i koszty.

## Niejawne buforowanie

Niejawne buforowanie jest domyślnie włączone w przypadku wszystkich modeli Gemini 2.5 i nowszych. Jest ono
obsługiwane zarówno w trybie rozmowy ze stanem [(przy użyciu parametru `previous_interaction_id`)](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl#multi-turn-conversations)
i [bezstanowym](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl#stateless-conversations).
Jeśli Twoje żądanie trafi do pamięci podręcznej, automatycznie przekażemy Ci oszczędności. Aby to włączyć, nie musisz nic robić. Minimalna liczba tokenów wejściowych do buforowania kontekstu jest podana w tabeli poniżej dla każdego modelu:

| Model | Minimalny limit tokenów |
| --- | --- |
| Gemini 3.8 Flash | 4096 |
| Gemini 3.7 Flash | 4096 |
| Gemini 3.6 Flash | 4096 |
| Gemini 3.5 Flash | 4096 |
| Gemini 3.1 Pro (wersja testowa) | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

Aby zwiększyć szansę na trafienie do niejawnej pamięci podręcznej:

- Spróbuj umieścić duże i popularne treści na początku prompta.
- Spróbuj wysyłać żądania z podobnym prefiksem w krótkim czasie.

Liczbę tokenów, które zostały trafione do pamięci podręcznej, możesz sprawdzić w polu `usage.total_cached_tokens` (Python i JavaScript) obiektu odpowiedzi.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-10 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-10 UTC."],[],[]]
