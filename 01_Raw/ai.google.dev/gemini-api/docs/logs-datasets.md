---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pl
fetched_at: 2026-07-06T05:15:23.339765+00:00
title: "Logi i zbiory danych \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Logi i zbiory danych

Ten przewodnik zawiera wszystkie informacje potrzebne do rozpoczęcia włączania logowania w istniejących aplikacjach Gemini API. Z tego przewodnika dowiesz się, jak wyświetlać logi z istniejącej lub nowej aplikacji na panelu Google AI Studio, aby lepiej zrozumieć zachowanie modelu i sposób, w jaki użytkownicy mogą wchodzić w interakcje z Twoimi aplikacjami. Używaj logowania do obserwowania, debugowania i *opcjonalnie udostępniania Google opinii o użytkowaniu
aby pomóc w ulepszaniu Gemini w różnych przypadkach użycia przez deweloperów*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=pl)

Obsługiwane są wszystkie wywołania interfejsu API `GenerateContent` i `StreamGenerateContent`,
w tym te, które są wykonywane za pomocą punktów końcowych zgodności z [OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pl).

## 1. Włącz logowanie w Google AI Studio

Zanim zaczniesz, upewnij się, że masz projekt z włączonymi płatnościami, którego jesteś właścicielem.

1. Otwórz stronę logów w Google [AI Studio](https://aistudio.google.com/logs?hl=pl).
2. Wybierz projekt z menu i naciśnij przycisk włączania, aby domyślnie włączyć logowanie dla wszystkich żądań.

![](https://ai.google.dev/static/gemini-api/docs/images/logs-state.png?hl=pl)

Możesz włączyć lub wyłączyć logowanie dla wszystkich projektów albo tylko dla wybranych projektów. Te ustawienia możesz w każdej chwili zmienić w Google AI Studio.

## 2. Wyświetlanie logów w AI Studio

1. Otwórz [AI Studio](https://aistudio.google.com/logs?hl=pl).
2. Wybierz projekt, w którym włączono logowanie.
3. Logi powinny pojawić się w tabeli w odwrotnej kolejności chronologicznej.

![](https://storage.googleapis.com/generativeai-downloads/images/nano-banana-logs.gif)

Kliknij wpis, aby wyświetlić parę żądanie-odpowiedź na pełnej stronie. Możesz sprawdzić cały prompt, pełną odpowiedź Gemini i kontekst z poprzedniej tury. Pamiętaj,że każdy projekt ma domyślny limit miejsca na dane wynoszący 1000 logów, a logi niezapisane w zbiorach danych wygasną po 55 dniach. Jeśli projekt osiągnie limit miejsca na dane, pojawi się prośba o usunięcie logów.

## 3. Tworzenie i udostępnianie zbiorów danych

- W tabeli logów znajdź pasek filtrowania u góry, aby wybrać właściwość, według której chcesz filtrować.
- W przefiltrowanym widoku logów użyj pól wyboru, aby zaznaczyć wszystkie lub kilka logów.
- Kliknij przycisk „Utwórz zbiór danych”, który pojawi się u góry listy.
- Nadaj nowemu zbiorowi danych opisową nazwę i opcjonalnie dodaj opis.
- Zobaczysz utworzony zbiór danych z wybranym zestawem logów.
- Wyeksportuj zbiór danych do dalszej analizy jako pliki CSV lub JSONL albo do Arkuszy Google.

![](https://storage.googleapis.com/generativeai-downloads/images/sales-dataset.gif)

Zbiory danych mogą być przydatne w wielu różnych przypadkach użycia.

- **Tworzenie zestawów wyzwań:** wprowadzaj przyszłe ulepszenia, które będą dotyczyć obszarów, w których chcesz, aby Twoja sztuczna inteligencja działała lepiej.
- **Tworzenie zestawów próbek:** na przykład próbka z rzeczywistego użytkowania, aby generować odpowiedzi z innego modelu, lub zbiór przypadków brzegowych do rutynowych kontroli przed wdrożeniem.
- **Zestawy do oceny:** zestawy reprezentujące rzeczywiste użytkowanie w przypadku ważnych funkcji, do porównywania z innymi modelami lub iteracjami instrukcji systemowych.

Możesz pomóc w rozwoju badań nad sztuczną inteligencją, Gemini API i Google AI Studio, udostępniając swoje zbiory danych jako przykłady demonstracyjne. Pozwala nam to udoskonalać nasze modele w różnych kontekstach i tworzyć systemy AI, które są przydatne dla deweloperów w wielu dziedzinach i aplikacjach.

## Dalsze kroki i co testować

Teraz, gdy masz włączone logowanie, możesz wypróbować te czynności:

- **Tworzenie prototypów z historią sesji:** użyj [AI Studio Build](https://aistudio.google.com/apps?hl=pl), aby tworzyć aplikacje z kodem i dodać klucz interfejsu API, który umożliwi zapisywanie historii logów użytkowników.
- **Ponowne uruchamianie logów za pomocą Gemini Batch API:** używaj zbiorów danych do próbkowania odpowiedzi
  i oceny modeli lub logiki aplikacji, ponownie uruchamiając logi za pomocą
  [Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

## Zgodność

Logowanie nie jest obecnie obsługiwane w przypadku:

- modeli Imagen i Veo,
- modelu Gemini do tworzenia osadzeń,
- danych wejściowych zawierających filmy, GIF-y lub pliki PDF.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-01 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-01 UTC."],[],[]]
