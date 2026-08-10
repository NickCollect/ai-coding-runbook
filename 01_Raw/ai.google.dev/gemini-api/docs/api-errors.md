---
source_url: https://ai.google.dev/gemini-api/docs/api-errors?hl=pl
fetched_at: 2026-08-10T03:20:28.302682+00:00
title: "B\u0142\u0119dy interfejsu API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Błędy interfejsu API

Ta strona zawiera informacje o wszystkich kodach błędów interfejsu Interactions API, opisuje format odpowiedzi na błędy i wyjaśnia, jak interfejs API dostarcza błędy w przypadku różnych typów żądań.

## Standardowe kody błędów interfejsu API

Te ogólne kody błędów na poziomie żądania odpowiadają standardowym kodom stanu HTTP.
Aby programowo obsługiwać błędy, użyj pola `code` w logice aplikacji.

| Kod | Stan HTTP | Opis | Zalecane działanie |
| --- | --- | --- | --- |
| `invalid_request` | 400 Nieprawidłowe żądanie | Żądanie jest nieprawidłowe lub zawiera nieprawidłowe parametry. | Sprawdź dane wejściowe w [dokumentacji API](https://ai.google.dev/api/interactions-api?hl=pl). |
| `parameter_unknown` | 400 Nieprawidłowe żądanie | Żądanie zawiera nieznany parametr. | Usuń nierozpoznany parametr i spróbuj ponownie. |
| `authentication` | 401 Brak autoryzacji | Brakujący lub nieprawidłowy klucz interfejsu API. | [Sprawdź kl0}ucz interfejsu API](https://ai.google.dev/gemini-api/docs/api-key?hl=pl). |
| `permission_denied` | 403 Dostęp zabroniony | Twój klucz interfejsu API nie ma uprawnień do tego zasobu. | Sprawdź uprawnienia klucza interfejsu API i dostęp do projektu. |
| `not_found` | 404 Nie znaleziono | Nie znaleziono żądanego zasobu. | Sprawdź ścieżkę zasobu i parametry. |
| `model_not_found` | 404 Nie znaleziono | Nie znaleziono określonego modelu. | Sprawdź nazwę modelu lub użyj innego modelu. |
| `rate_limit_exceeded` | 429 Zbyt wiele żądań | Przekroczono limit żądań lub tokenów na minutę lub sekundę. | Poczekaj i spróbuj ponownie ze wzrastającym czasem do ponowienia. |
| `quota_exceeded` | 429 Zbyt wiele żądań | Przekroczono dzienny limit. | Poczekaj, aż limit się zresetuje, lub poproś o jego zwiększenie. |
| `cancelled` | 499 Klient zamknął żądanie | Klient anulował żądanie przed jego zakończeniem. | Nie musisz niczego robić. Zwykle oznacza to, że klient się rozłączył. |
| `api_error` | 500 Wewnętrzny błąd serwera | Na serwerze wystąpił nieoczekiwany błąd. | Ponów próbę. Jeśli problem się powtórzy, skontaktuj się z zespołem pomocy. |
| `service_unavailable` | 503 Usługa niedostępna | Usługa jest tymczasowo przeciążona lub niedostępna. | Poczekaj i spróbuj ponownie ze wzrastającym czasem do ponowienia. |

## Kody zablokowanej generacji

Te kody błędów wskazują, że dane wyjściowe modelu zostały zablokowane przez ograniczenia dotyczące zasad, bezpieczeństwa lub ograniczenia treści. Gdy otrzymasz jeden z tych kodów, zmodyfikuj dane wejściowe i spróbuj ponownie.

| Kod | Opis |
| --- | --- |
| `safety` | Żądanie zostało zablokowane z powodu naruszenia zasad bezpieczeństwa (szkodliwe treści). |
| `recitation` | Żądanie zostało zablokowane z powodu ograniczeń dotyczących praw autorskich lub recytacji. |
| `language` | Żądanie zostało zablokowane z powodu nieobsługiwanego języka. |
| `prohibited_content` | Żądanie zostało zablokowane z powodu wytycznych dotyczących niedozwolonych treści. |
| `spii` | Żądanie zostało zablokowane z powodu ograniczeń dotyczących informacji poufnych umożliwiających identyfikację. |
| `blocklist` | Żądanie zostało zablokowane z powodu niedozwolonych terminów na liście zablokowanych. |
| `image_safety` | Generowanie obrazu zostało zablokowane z powodu naruszenia zasad bezpieczeństwa. |
| `image_prohibited_content` | Generowanie obrazu zostało zablokowane z powodu wytycznych dotyczących niedozwolonych treści. |
| `image_recitation` | Generowanie obrazu zostało zablokowane z powodu ograniczeń dotyczących praw autorskich lub recytacji. |
| `image_other` | Generowanie obrazu zostało zablokowane z nieokreślonych powodów. |
| `content_blocked` | Żądanie zostało zablokowane z nieokreślonego powodu związanego z zasadami. |

## Kody błędów generowania

Te kody błędów wskazują na problem strukturalny z wygenerowanymi danymi wyjściowymi modelu (np. nieprawidłowe wywołanie funkcji lub niezadeklarowane wywołanie narzędzia).

| Kod | Opis |
| --- | --- |
| `malformed_function_call` | Model wygenerował wywołanie funkcji, którego nie udało się przeanalizować. |
| `malformed_tool_call` | Model wygenerował wywołanie narzędzia, którego nie udało się przeanalizować. |
| `unexpected_tool_call` | Model wywołał narzędzie, które nie zostało zadeklarowane w żądaniu. |
| `no_image` | Model nie był w stanie wygenerować obrazu. |
| `too_many_tool_calls` | Model wygenerował więcej wywołań narzędzi niż jest to dozwolone. |
| `missing_thought_signature` | W odpowiedzi brakuje wymaganej sygnatury. |

## Format odpowiedzi na błędy

Wszystkie błędy z interfejsu Interactions API zwracają obiekt `error` zawierający `code` i `message`. Na przykład przekazanie nieobsługiwanego typu narzędzia zwraca:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'. Supported values: 'function', 'code_execution', 'mcp_server', 'filesystem', 'google_maps', 'google_search', 'bash', 'computer_use', 'file_search', 'url_context'."
  }
}
```

| Pole | Typ | Opis |
| --- | --- | --- |
| `code` | tekst | Kod błędu w formacie `snake_case`. |
| `message` | tekst | Zrozumiały dla człowieka opis tego, co poszło nie tak. |

## Jak są dostarczane błędy

Interfejs API dostarcza błędy w różny sposób w zależności od tego, czy wysyłasz standardowe żądanie HTTP, czy żądanie przesyłania strumieniowego (SSE).

### Standardowe żądania HTTP

W przypadku standardowych (niestrumieniowych) żądań interfejs API ustawia kod stanu odpowiedzi HTTP (np. `400 Bad Request`, `401 Unauthorized`, lub `429 Too Many Requests`) i zwraca obiekt `error` w treści odpowiedzi JSON:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'."
  }
}
```

### Żądania przesyłania strumieniowego (SSE)

W przypadku żądań przesyłania strumieniowego (`stream: true`) interfejs API wysyła zdarzenia błędów w strumieniu Server-Sent Events (SSE) z ustawionym parametrem `event_type` na wartość `"error"`. Pole `error` zawiera tę samą strukturę `code` i `message`:

```
{
  "event_type": "error",
  "error": {
    "code": "not_found",
    "message": "Failed to get completed interaction: Result not found."
  }
}
```

Pełny schemat zdarzeń SSE znajdziesz w dokumentacji interfejsu [Interactions API](https://ai.google.dev/api/interactions-api?hl=pl).

## Co dalej?

- [Rozwiązywanie problemów z interfejsem API](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=pl): rozwiązywanie typowych problemów i scenariuszy błędów.
- [Limity](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl): informacje o limitach żądań i obsłudze limitów.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
