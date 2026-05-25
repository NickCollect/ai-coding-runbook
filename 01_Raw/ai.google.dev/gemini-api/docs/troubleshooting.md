---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=pl
fetched_at: 2026-05-25T05:19:05.162183+00:00
title: "Przewodnik rozwi\u0105zywania problem\u00f3w \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Przewodnik rozwiązywania problemów

Ten przewodnik pomoże Ci zdiagnozować i rozwiązać typowe problemy, które mogą wystąpić podczas wywoływania interfejsu Gemini API. Problemy mogą występować zarówno w usłudze backendu Gemini API, jak i w pakietach SDK klienta. Nasze pakiety SDK klienta są udostępniane na licencji open source w tych repozytoriach:

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

Jeśli napotkasz problemy z kluczem interfejsu API, sprawdź, czy został on prawidłowo skonfigurowany zgodnie z [przewodnikiem konfiguracji klucza interfejsu API](https://ai.google.dev/gemini-api/docs/api-key?hl=pl).

## Kody błędów usługi backendu Gemini API

W tabeli poniżej znajdziesz listę typowych kodów błędów backendu, które możesz napotkać, wraz z wyjaśnieniami ich przyczyn i sposobami rozwiązywania problemów:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Kod HTTP** | **Stan** | **Opis** | **Przykład** | **Rozwiązanie** |
| 400 | INVALID\_ARGUMENT | Treść żądania jest błędnie sformatowana. | W żądaniu jest błąd w pisowni lub brakuje wymaganego pola. | Format żądania, przykłady i obsługiwane wersje znajdziesz w [dokumentacji interfejsu API](https://ai.google.dev/api?hl=pl). Używanie funkcji z nowszej wersji interfejsu API ze starszym punktem końcowym może powodować błędy. |
| 400 | FAILED\_PRECONDITION | Bezpłatny poziom Gemini API nie jest dostępny w Twoim kraju. Włącz płatności w projekcie w Google AI Studio. | Wysyłasz żądanie w regionie, w którym poziom bezpłatny nie jest obsługiwany, a w Google AI Studio nie masz włączonych rozliczeń w projekcie. | Aby korzystać z Gemini API, musisz skonfigurować abonament w [Google AI Studio](https://aistudio.google.com/app/apikey?hl=pl). |
| 403 | PERMISSION\_DENIED | Twój klucz API nie ma wymaganych uprawnień. | Używasz nieprawidłowego klucza interfejsu API. Próbujesz użyć dostosowanego modelu bez [prawidłowego uwierzytelniania](https://ai.google.dev/gemini-api/docs/model-tuning?hl=pl). | Sprawdź, czy klucz interfejsu API jest ustawiony i ma odpowiedni dostęp. Aby korzystać z dostosowanych modeli, musisz przejść odpowiednią weryfikację. |
| 404 | NOT\_FOUND | Nie znaleziono żądanego zasobu. | Nie znaleziono pliku obrazu, audio ani wideo, do którego odwołuje się Twoja prośba. | Sprawdź, czy wszystkie [parametry w żądaniu są prawidłowe](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=pl#check-api) w przypadku Twojej wersji interfejsu API. |
| 429 | RESOURCE\_EXHAUSTED | Przekroczono limit częstotliwości. | Wysyłasz zbyt wiele żądań na minutę za pomocą bezpłatnego poziomu Gemini API. | Sprawdź, czy nie przekraczasz [limitu żądań](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl) modelu. W razie potrzeby [poproś o zwiększenie limitu](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl#request-rate-limit-increase). |
| 500 | INTERNAL | Po stronie Google wystąpił nieoczekiwany błąd. | Kontekst wejściowy jest za długi. | Sprawdź [stronę stanu Gemini API](https://aistudio.google.com/status?hl=pl), aby dowiedzieć się o bieżących incydentach. Zmniejsz kontekst wejściowy lub tymczasowo przełącz się na inny model (np. z Gemini 2.5 Pro na Gemini 2.5 Flash) i sprawdź, czy to pomoże. Możesz też poczekać chwilę i ponowić prośbę. Jeśli problem będzie się powtarzać, zgłoś go, klikając przycisk **Prześlij opinię** w Google AI Studio. |
| 503 | PRODUKT NIEDOSTĘPNY | Usługa może być tymczasowo przeciążona lub niedostępna. | Usługa tymczasowo nie ma wystarczającej mocy obliczeniowej. | Sprawdź [stronę stanu Gemini API](https://aistudio.google.com/status?hl=pl), aby dowiedzieć się o bieżących incydentach. Tymczasowo przełącz się na inny model (np. z Gemini 2.5 Pro na Gemini 2.5 Flash) i sprawdź, czy działa. Możesz też poczekać chwilę i ponowić prośbę. Jeśli problem będzie się powtarzać, zgłoś go, klikając przycisk **Prześlij opinię** w Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | Usługa nie może zakończyć przetwarzania w terminie. | Prompt (lub kontekst) jest zbyt duży, aby można go było przetworzyć na czas. | Aby uniknąć tego błędu, ustaw w żądaniu klienta dłuższy „limit czasu”. |

## Sprawdzanie wywołań interfejsu API pod kątem błędów parametrów modelu

Sprawdź, czy parametry modelu mieszczą się w tych zakresach wartości:

|  |  |
| --- | --- |
| **Parametr modelu** | **Wartości (zakres)** |
| Liczba kandydatów | 1–8 (liczba całkowita) |
| Temperatura | 0,0–1,0 |
| Maksymalna liczba tokenów wyjściowych | Na [stronie modeli](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl) możesz sprawdzić maksymalną liczbę tokenów dla używanego modelu. |
| TopP | 0,0–1,0 |

Oprócz sprawdzania wartości parametrów upewnij się, że używasz prawidłowej [wersji interfejsu API](https://ai.google.dev/gemini-api/docs/api-versions?hl=pl) (np. `/v1` lub `/v1beta`) i modelu, który obsługuje potrzebne Ci funkcje. Jeśli na przykład funkcja jest w wersji beta, będzie dostępna tylko w wersji interfejsu API `/v1beta`.

## Sprawdź, czy masz odpowiedni model

Sprawdź, czy używasz obsługiwanego modelu wymienionego na naszej [stronie z modelami](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl).

## Większe opóźnienie lub wykorzystanie tokenów w przypadku modeli 2.5

Jeśli zauważysz większe opóźnienia lub zużycie tokenów w przypadku modeli 2.5 Flash i Pro, może to być spowodowane tym, że **myślenie jest w nich domyślnie włączone**, aby zwiększyć jakość. Jeśli priorytetem jest szybkość lub chcesz zminimalizować koszty, możesz dostosować lub wyłączyć myślenie.

Wskazówki i przykładowy kod znajdziesz na [stronie z informacjami](https://ai.google.dev/gemini-api/docs/thinking?hl=pl#set-budget).

## Problemy z bezpieczeństwem

Jeśli zobaczysz komunikat o tym, że prompt został zablokowany z powodu ustawienia bezpieczeństwa w wywołaniu interfejsu API, sprawdź, czy jest on zgodny z filtrami ustawionymi w wywołaniu interfejsu API.

Jeśli zobaczysz symbol `BlockedReason.OTHER`, zapytanie lub odpowiedź mogą naruszać [warunki korzystania z usługi](https://ai.google.dev/terms?hl=pl) lub być w inny sposób nieobsługiwane.

## Problem z odczytywaniem

Jeśli zobaczysz, że model przestał generować dane wyjściowe z powodu RECITATION, oznacza to, że dane wyjściowe modelu mogą przypominać określone dane. Aby to naprawić, spróbuj jak najbardziej urozmaicić prompt lub kontekst i użyj wyższej temperatury.

## Problem z powtarzającymi się tokenami

Jeśli widzisz powtarzające się tokeny wyjściowe, wypróbuj te sugestie, aby je ograniczyć lub wyeliminować.

| Opis | Przyczyna | Sugerowane obejście |
| --- | --- | --- |
| Powtórzone łączniki w tabelach Markdown | Może się to zdarzyć, gdy zawartość tabeli jest długa, ponieważ model próbuje utworzyć wizualnie wyrównaną tabelę Markdown. Wyrównanie w Markdownie nie jest jednak konieczne do prawidłowego renderowania. | Dodaj do prompta instrukcje, aby podać modelowi konkretne wytyczne dotyczące generowania tabel w formacie Markdown. Podaj przykłady zgodne z tymi wytycznymi. Możesz też spróbować dostosować temperaturę. W przypadku generowania kodu lub bardzo uporządkowanych danych wyjściowych, takich jak tabele w formacie Markdown, lepiej sprawdzają się wysokie wartości parametru temperatura (≥ 0,8).  Oto przykładowy zestaw wytycznych, które możesz dodać do prompta, aby zapobiec temu problemowi:     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Powtarzające się tokeny w tabelach Markdown | Podobnie jak w przypadku powtarzających się łączników, dzieje się tak, gdy model próbuje wizualnie wyrównać zawartość tabeli. Wyrównanie w Markdown nie jest wymagane do prawidłowego renderowania. | - Spróbuj dodać do promptu systemowego instrukcje takie jak te:      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - Spróbuj dostosować temperaturę. Wyższe temperatury (>= 0,8) zwykle pomagają wyeliminować powtórzenia w wyniku. |
| Powtórzone znaki nowego wiersza (`\n`) w uporządkowanych danych wyjściowych | Jeśli dane wejściowe modelu zawierają znaki Unicode lub sekwencje ucieczki, takie jak `\u` lub `\t`, może to prowadzić do powtarzających się znaków nowego wiersza. | - Sprawdź, czy w prompcie nie ma zabronionych sekwencji ucieczki, i zastąp je znakami UTF-8. Na przykład sekwencja ucieczki `\u` w przykładach JSON może spowodować, że model będzie jej używać również w danych wyjściowych. - Poinformuj model o dozwolonych znakach ucieczki. Dodaj instrukcję systemową, np. taką:      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| Powtarzający się tekst w przypadku korzystania z uporządkowanych danych wyjściowych | Jeśli dane wyjściowe modelu mają inną kolejność pól niż zdefiniowany schemat strukturalny, może to prowadzić do powtarzania się tekstu. | - Nie określaj kolejności pól w prompcie. - Ustaw wszystkie pola wyjściowe jako wymagane. |
| Powtarzające się wywołania narzędzi | Może się tak zdarzyć, jeśli model utraci kontekst poprzednich przemyśleń lub wywoła niedostępny punkt końcowy, do którego jest zmuszony. | Poinstruuj model, aby zachowywał stan w procesie myślowym. Dodaj ten tekst na końcu instrukcji systemowych:    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| Powtarzający się tekst, który nie jest częścią uporządkowanych danych wyjściowych | Może się tak zdarzyć, jeśli model utknie na żądaniu, którego nie może rozwiązać. | - Jeśli myślenie jest włączone, w instrukcjach unikaj podawania wyraźnych poleceń dotyczących tego, jak rozwiązać problem. Po prostu poproś o ostateczny wynik. - Wypróbuj wyższą temperaturę >= 0,8. - Dodaj instrukcje, np. „Bądź zwięzły”, „Nie powtarzaj się” lub „Podaj odpowiedź tylko raz”. |

## Zablokowane lub niedziałające klucze interfejsu API

Z tej sekcji dowiesz się, jak sprawdzić, czy Twój klucz interfejsu Gemini API jest zablokowany, i co w takiej sytuacji zrobić.

### Dlaczego klucze są blokowane

Wykryliśmy lukę w zabezpieczeniach, w wyniku której niektóre klucze interfejsu API mogły zostać publicznie ujawnione. Aby chronić Twoje dane i zapobiegać nieautoryzowanemu dostępowi, aktywnie blokujemy dostęp do interfejsu Gemini API za pomocą tych znanych, ujawnionych kluczy.

### Sprawdź, czy zmiana dotyczy Twoich kluczy

Jeśli Twój klucz został ujawniony, nie możesz już używać go w interfejsie Gemini API. W [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=pl) możesz sprawdzić, czy któryś z Twoich kluczy API jest zablokowany i nie może wywoływać Gemini API, a także wygenerować nowe klucze. Podczas próby użycia tych kluczy może też pojawić się ten błąd:

```
Your API key was reported as leaked. Please use another API key.
```

### Działanie w przypadku zablokowanych kluczy interfejsu API

Nowe klucze interfejsu API do integracji z Gemini API należy generować za pomocą [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=pl). Zdecydowanie zalecamy sprawdzenie metod zarządzania kluczami interfejsu API, aby upewnić się, że nowe klucze są bezpieczne i nie są publicznie udostępniane.

### Nieoczekiwane opłaty z powodu luki w zabezpieczeniach

[Prześlij zgłoszenie do zespołu pomocy ds. płatności](https://console.cloud.google.com/support/chat?hl=pl)
Nasz zespół ds. płatności pracuje nad tym problemem i jak najszybciej poinformujemy Cię o postępach.

### Środki bezpieczeństwa Google w przypadku wycieku kluczy

**Jak Google pomoże mi zabezpieczyć konto przed przekroczeniem kosztów i nadużyciami, jeśli moje klucze interfejsu API wyciekną?**

- Wprowadzamy zmianę, która polega na tym, że gdy poprosisz o nowy klucz w [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=pl), będziemy wydawać klucze API, które domyślnie będą ograniczone tylko do Google AI Studio i nie będą akceptować kluczy z innych usług.
  Pomoże to zapobiec niezamierzonemu użyciu klucza krzyżowego.
- Domyślnie blokujemy klucze interfejsu API, które wyciekły i są używane z interfejsem Gemini API, co pomaga zapobiegać nadużyciom związanym z kosztami i danymi aplikacji.
- Stan kluczy interfejsu API możesz sprawdzić w [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=pl). Jeśli wykryjemy, że Twoje klucze interfejsu API zostały ujawnione, będziemy Cię o tym informować, aby umożliwić Ci podjęcie natychmiastowych działań.

## Ulepszanie danych wyjściowych modelu

Aby uzyskać wyższą jakość wyników modelu, spróbuj pisać bardziej ustrukturyzowane prompty. Na stronie [Przewodnik po inżynierii promptów](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pl) znajdziesz podstawowe koncepcje, strategie i sprawdzone metody, które pomogą Ci zacząć.

## Limity tokenów

Aby dowiedzieć się więcej o liczeniu tokenów i ich limitach, przeczytaj nasz [przewodnik po tokenach](https://ai.google.dev/gemini-api/docs/tokens?hl=pl).

## Znane problemy

- Interfejs API obsługuje tylko wybrane języki. Przesyłanie promptów w nieobsługiwanych językach może skutkować nieoczekiwanymi lub nawet zablokowanymi odpowiedziami. Aktualne informacje o [dostępnych językach](https://ai.google.dev/gemini-api/docs/models?hl=pl#supported-languages) znajdziesz na tej stronie.

## Zgłoś błąd

Jeśli masz pytania, dołącz do dyskusji na [forum dla deweloperów Google AI](https://discuss.ai.google.dev?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-04-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-04-30 UTC."],[],[]]
