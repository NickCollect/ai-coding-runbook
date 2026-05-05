---
source_url: https://ai.google.dev/gemini-api/docs/tools?hl=pl
fetched_at: 2026-05-05T13:15:53.454658+00:00
title: "Korzystanie z\u00a0narz\u0119dzi za pomoc\u0105 interfejsu Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

- [Strona główna](https://ai.google.dev/gemini-api/docs/Strona główna)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Dokumenty](https://ai.google.dev/gemini-api/docs/Dokumenty)

Prześlij opinię

# Korzystanie z narzędzi za pomocą interfejsu Gemini API

Narzędzia rozszerzają możliwości modeli Gemini, umożliwiając im podejmowanie działań w świecie rzeczywistym, dostęp do informacji w czasie rzeczywistym i wykonywanie złożonych zadań obliczeniowych. Modele mogą korzystać z narzędzi zarówno w standardowych interakcjach typu żądanie-odpowiedź, jak i
w sesjach przesyłania strumieniowego w czasie rzeczywistym za pomocą interfejsu [Live API](https://ai.google.dev/gemini-api/docs/Live API).

Narzędzia to konkretne funkcje (takie jak wyszukiwarka Google czy wykonywanie kodu), których model może używać do odpowiadania na zapytania. Interfejs Gemini API udostępnia zestaw w pełni
zarządzanych, wbudowanych narzędzi. Możesz też zdefiniować narzędzia niestandardowe za pomocą [wywoływania
funkcji](https://ai.google.dev/gemini-api/docs/wywoływaniafunkcji).

Aby tworzyć wieloetapowe systemy zorientowane na cel, zapoznaj się z omówieniem [agentów](https://ai.google.dev/gemini-api/docs/agentów).

## Dostępne narzędzia wbudowane

| Narzędzie | Opis | Przypadki użycia |
| --- | --- | --- |
| [Wyszukiwarka Google](https://ai.google.dev/gemini-api/docs/Wyszukiwarka Google) | Uzasadniaj odpowiedzi aktualnymi wydarzeniami i faktami z internetu, aby ograniczyć halucynacje. | \- Odpowiadanie na pytania o bieżące wydarzenia.   \- Weryfikowanie faktów za pomocą różnych źródeł. |
| [Mapy Google](https://ai.google.dev/gemini-api/docs/Mapy Google) | Twórz asystentów rozpoznających lokalizację, którzy mogą znajdować miejsca, wyznaczać trasy i dostarczać bogaty kontekst lokalny. | \- Planowanie tras podróży z wieloma przystankami   \- Znajdowanie lokalnych firm na podstawie kryteriów użytkownika. |
| [Wykonywanie kodu](https://ai.google.dev/gemini-api/docs/Wykonywanie kodu) | Pozwól modelowi pisać i uruchamiać kod w Pythonie, aby rozwiązywać problemy matematyczne lub dokładnie przetwarzać dane. | \- Rozwiązywanie złożonych równań matematycznych   \- Precyzyjne przetwarzanie i analizowanie danych tekstowych |
| [Kontekst adresu URL](https://ai.google.dev/gemini-api/docs/Kontekst adresu URL) | Poproś model o przeczytanie i przeanalizowanie treści z określonych stron internetowych lub dokumentów. | \- Odpowiadanie na pytania na podstawie konkretnych adresów URL lub dokumentów   \- Pobieranie informacji z różnych stron internetowych. |
| [Korzystanie z komputera (wersja testowa)](https://ai.google.dev/gemini-api/docs/Korzystanie z komputera (wersja testowa)) | Zezwól Gemini na wyświetlanie ekranu i generowanie działań w celu interakcji z interfejsami przeglądarek internetowych (wykonywanie po stronie klienta). | \- Automatyzowanie powtarzalnych przepływów pracy w internecie.   \- Testowanie interfejsów aplikacji internetowych. |
| [Wyszukiwanie plików](https://ai.google.dev/gemini-api/docs/Wyszukiwanie plików) | Indeksuj i przeszukuj własne dokumenty, aby włączyć generowanie wspomagane wyszukiwaniem (RAG). | \- Przeszukiwanie podręczników technicznych   \- Odpowiadanie na pytania na podstawie danych zastrzeżonych |

Szczegółowe informacje o kosztach związanych z konkretnymi narzędziami znajdziesz na stronie [Cennik](https://ai.google.dev/gemini-api/docs/Cennik).

## Jak działa wykonywanie narzędzi

Narzędzia umożliwiają modelowi żądanie działań podczas rozmowy. Przepływ różni się w zależności od tego, czy narzędzie jest wbudowane (zarządzane przez Google) czy niestandardowe (zarządzane przez Ciebie).

### Przepływ narzędzia wbudowanego

W przypadku narzędzi wbudowanych (wyszukiwarka Google, Mapy Google, kontekst adresu URL, wyszukiwanie plików, wykonywanie kodu) cały proces odbywa się w ramach jednego wywołania interfejsu API:

1. **Ty** wysyłasz prompta: „Ile wynosi pierwiastek kwadratowy z najnowszej ceny akcji GOOG?”
2. **Gemini** stwierdza, że potrzebuje narzędzi, i uruchamia je na serwerach Google (np. wyszukuje cenę akcji, a następnie uruchamia kod w Pythonie, aby obliczyć pierwiastek kwadratowy).
3. **Gemini** odsyła ostateczną odpowiedź opartą na wynikach narzędzia.

### Przepływ narzędzia niestandardowego (wywoływanie funkcji)

W przypadku narzędzi niestandardowych i korzystania z komputera wykonywanie jest obsługiwane przez Twoją aplikację:

1. **Ty** wysyłasz prompta wraz z deklaracjami funkcji (narzędzi).
2. **Gemini** może odesłać uporządkowany kod JSON, aby wywołać konkretną funkcję
   (np. `{"name": "get_order_status", "args": {"order_id": "123"}}`),
   zawsze z unikalnym `id`.
3. **Ty** uruchamiasz funkcję w swojej aplikacji lub środowisku.
4. **Ty** odsyłasz wyniki funkcji z tym samym `id` co wywołanie funkcji.
5. **Gemini** używa wyników do wygenerowania ostatecznej odpowiedzi lub innego wywołania narzędzia.

Więcej informacji znajdziesz w [przewodniku po wywoływaniu funkcji](https://ai.google.dev/gemini-api/docs/przewodniku po wywoływaniu funkcji).

### Łączenie przepływu narzędzi wbudowanych i niestandardowych

W przypadku żądań, które łączą narzędzia wbudowane i narzędzia niestandardowe (wywołania funkcji), model używa [obiegu kontekstu narzędzia](https://ai.google.dev/gemini-api/docs/obiegu kontekstu narzędzia) do koordynowania wykonywania w różnych środowiskach:

1. **Ty** wysyłasz prompta i deklarujesz narzędzia wbudowane oraz funkcje niestandardowe, które chcesz włączyć, ustawiając flagę, aby włączyć obsługę kombinacji.
2. **Gemini** uruchamia narzędzia wbudowane i przekazuje kontrolę użytkownikowi, jeśli zostaną wygenerowane wywołania funkcji po stronie klienta (kolejność zależy od prompta i decyzji modelu). Odsyła odpowiedź zawierającą:
   - potwierdzenie wywołania narzędzia;
   - wyniki odpowiedzi narzędzia (mogą one pojawić się po kodzie JSON, jeśli model wygenerował 2 równoległe wywołania funkcji);
   - uporządkowany kod JSON do wywołania funkcji;
   - zaszyfrowane sygnatury myśli, aby zachować kontekst.
3. **Ty** uruchamiasz funkcję w swojej aplikacji lub środowisku.
4. **Ty** zwracasz wszystkie części odpowiedzi Gemini oraz wyniki wywołania funkcji.
5. **Gemini** generuje ostateczną odpowiedź, używając całego połączonego kontekstu.

Aby dowiedzieć się, jak włączyć obsługę łączenia narzędzi wbudowanych i niestandardowych, oraz poznać przykłady obiegu kontekstu, przeczytaj [przewodnik po łączeniu narzędzi](https://ai.google.dev/gemini-api/docs/przewodnik po łączeniu narzędzi).

## Uporządkowane dane wyjściowe a wywoływanie funkcji

Gemini oferuje 2 metody generowania uporządkowanych danych wyjściowych. Używaj [wywoływania funkcji](https://ai.google.dev/gemini-api/docs/wywoływania funkcji) gdy model musi wykonać
krok pośredni, łącząc się z Twoimi narzędziami lub systemami danych. Używaj
[uporządkowanych danych wyjściowych](https://ai.google.dev/gemini-api/docs/uporządkowanych danych wyjściowych), gdy ostateczna odpowiedź modelu musi być ściśle zgodna z określonym schematem, np. w celu renderowania
niestandardowego interfejsu.

## Uporządkowane dane wyjściowe z narzędziami

 

Możesz łączyć [uporządkowane dane wyjściowe](https://ai.google.dev/gemini-api/docs/uporządkowane dane wyjściowe) z
narzędziami wbudowanymi, aby mieć pewność, że odpowiedzi modelu oparte na danych zewnętrznych lub
obliczeniach nadal będą zgodne z określonym schematem.

Przykłady kodu znajdziesz w artykule [Uporządkowane dane wyjściowe z narzędziami](https://ai.google.dev/gemini-api/docs/Uporządkowane dane wyjściowe z narzędziami).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://ai.google.dev/gemini-api/docs/licencją Creative Commons – uznanie autorstwa 4.0), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://ai.google.dev/gemini-api/docs/licencji Apache 2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://ai.google.dev/gemini-api/docs/zasady dotyczące witryny Google Developers). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-04-29 UTC.

Chcesz przekazać coś jeszcze?
