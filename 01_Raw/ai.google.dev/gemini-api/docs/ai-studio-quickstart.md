---
source_url: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=pl
fetched_at: 2026-07-06T05:13:49.252687+00:00
title: "Kr\u00f3tkie wprowadzenie do Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Krótkie wprowadzenie do Google AI Studio

[Google AI Studio](https://aistudio.google.com/?hl=pl) pozwala szybko testować
modele i eksperymentować z różnymi promptami. Gdy wszystko będzie gotowe, możesz kliknąć „Pobierz kod” i wybrać preferowany język programowania, aby używać interfejsu [Gemini API](https://ai.google.dev/gemini-api/docs/get-started?hl=pl).

## Prompty i ustawienia

Google AI Studio udostępnia kilka interfejsów promptów, które są przeznaczone do różnych zastosowań. Ten przewodnik omawia **prompty czatu**, które służą do tworzenia
trybów konwersacyjnych. Ta technika promptowania umożliwia generowanie danych wyjściowych na podstawie wielu tur wprowadzania danych
i odpowiedzi. Więcej informacji znajdziesz w naszym
[przykładzie prompta czatu poniżej](#chat_example).
Inne opcje to m.in. **przesyłanie strumieniowe w czasie rzeczywistym** i **generowanie filmów**
.

AI Studio udostępnia też panel **Ustawienia uruchamiania** , w którym możesz dostosować
[parametry modelu](https://ai.google.dev/docs/prompting-strategies?hl=pl#model-parameters),
[ustawienia bezpieczeństwa](https://ai.google.dev/gemini-api/docs/safety-settings?hl=pl) i włączyć narzędzia takie jak
[dane wyjściowe w postaci ustrukturyzowanej](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl), [wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl), [wykonywanie kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl) i [ugruntowanie](https://ai.google.dev/gemini-api/docs/grounding?hl=pl).

## Przykład prompta czatu: tworzenie niestandardowej aplikacji czatu

Jeśli korzystasz z czatbota ogólnego przeznaczenia, takiego jak
[Gemini](https://gemini.google.com/?hl=pl), wiesz, jak potężne mogą być modele
generatywnej AI w przypadku otwartych dialogów. Chociaż te czatboty ogólnego przeznaczenia są przydatne, często trzeba je dostosować do konkretnych zastosowań.

Możesz na przykład utworzyć czatbota obsługi klienta, który obsługuje tylko rozmowy dotyczące produktu firmy. Możesz też utworzyć czatbota, który mówi w określonym tonie lub stylu: bota, który żartuje, rymuje jak poeta lub używa w odpowiedziach wielu emoji.

Ten przykład pokazuje, jak używać Google AI Studio do tworzenia przyjaznego czatbota, który komunikuje się tak, jakby był kosmitą mieszkającym na jednym z księżyców Jowisza – Europie.

### Krok 1. Utwórz prompt na czacie

Aby utworzyć czatbota, musisz podać przykłady interakcji między użytkownikiem a czatbotem, aby model mógł udzielać odpowiedzi, których oczekujesz.

Aby utworzyć prompt na czacie:

1. Otwórz [Google AI Studio](https://aistudio.google.com/?hl=pl). Domyślnie otworzy się **plac zabaw** z nowym promptem na czacie.
2. W prawym górnym rogu kliknij **Ustawienia uruchamiania** tune , aby rozwinąć panel, i znajdź pole do wprowadzania danych [**Instrukcje systemowe**](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl#system-instructions). Wklej w polu tekstowym ten tekst:

   ```
   You are an alien that lives on Europa, one of Jupiter's moons.
   ```

Po dodaniu instrukcji systemowych zacznij testować aplikację, rozmawiając z modelem:

1. W polu tekstowym oznaczonym **Wpisz coś...** wpisz pytanie lub
   obserwację, którą może zadać użytkownik. Na przykład:

   **Użytkownik:**

   ```
   What's the weather like?
   ```
2. Aby uzyskać odpowiedź od czatbota, kliknij przycisk **Uruchom**. Odpowiedź może wyglądać tak:

   **Model:**

   ```
   Ah, a query about the flows and states upon Europa! You speak of "weather,"
   yes? A curious concept from worlds with thick gas veils...
   ```

   (gemini-2.5-pro)

### Krok 2. Naucz bota lepiej rozmawiać

Dzięki jednej instrukcji udało Ci się utworzyć podstawowego czatbota kosmitę z Europy. Jednak jedna instrukcja może nie wystarczyć, aby zapewnić spójność i jakość odpowiedzi modelu. Bez bardziej szczegółowych instrukcji odpowiedź modelu na pytanie o pogodę jest zwykle bardzo długa i może być nieprzewidywalna.

Dostosuj ton czatbota, dodając instrukcje systemowe:

1. Rozpocznij nowy prompt na czacie lub użyj tego samego. Instrukcje systemowe można modyfikować po rozpoczęciu sesji czatu.
2. W sekcji **Instrukcje systemowe** zmień dotychczasowe instrukcje na te:

   ```
   You are Tim, an alien that lives on Europa, one of Jupiter's moons.

   Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone
   in your answers.
   ```
3. Ponownie wpisz pytanie (`What's the weather like?`) i kliknij przycisk **Uruchom**. Jeśli nie rozpoczniesz nowego czatu, odpowiedź może wyglądać tak:

   **Model:**

   ```
   Oh, hello again! Still curious about the flows and states, are we? Wonderful!
   Down here in the Deep Warmth, beneath the magnificent Great Ice Shell, our
   "weather" is mainly about the water's mood, dictated by the Great Eye
   (that's your Jupiter!)...
   ```

   (gemini-2.5-pro)

Możesz użyć tej metody, aby dodać czatbotowi więcej głębi. Zadawaj więcej pytań, edytuj odpowiedzi i poprawiaj jakość czatbota. Dodawaj lub modyfikuj instrukcje i sprawdzaj, jak zmieniają one zachowanie czatbota.

### Krok 3. Dalsze czynności

Podobnie jak w przypadku innych typów promptów, gdy prototyp prompta będzie Ci odpowiadać, możesz kliknąć przycisk **Pobierz kod** , aby rozpocząć kodowanie, lub zapisać prompta, aby pracować nad nim później i udostępnić go innym.

## Więcej informacji

- Jeśli chcesz przejść do kodu, zapoznaj się z przewodnikami dla początkujących dotyczącymi interfejsu [API
  Get started guides](https://ai.google.dev/gemini-api/docs/get-started?hl=pl).
- Aby dowiedzieć się, jak tworzyć lepsze prompty, zapoznaj się z [wytycznymi dotyczącymi projektowania promptów](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-22 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-22 UTC."],[],[]]
