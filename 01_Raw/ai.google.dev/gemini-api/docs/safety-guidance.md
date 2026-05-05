---
source_url: https://ai.google.dev/gemini-api/docs/safety-guidance?hl=pl
fetched_at: 2026-05-05T13:23:33.286324+00:00
title: "Wytyczne dotycz\u0105ce bezpiecze\u0144stwa i\u00a0rzetelno\u015bci \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

- [Strona główna](https://ai.google.dev/gemini-api/docs/Strona główna)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Dokumenty](https://ai.google.dev/gemini-api/docs/Dokumenty)

Prześlij opinię

# Wytyczne dotyczące bezpieczeństwa i rzetelności

Modele generatywnej sztucznej inteligencji to potężne narzędzia, ale mają one pewne ograniczenia. Ich wszechstronność i możliwość zastosowania mogą czasami prowadzić do nieoczekiwanych wyników, takich jak wyniki niedokładne, stronnicze lub obraźliwe. Przetwarzanie końcowe i rygorystyczna ocena ręczna są niezbędne, aby ograniczyć ryzyko szkód wynikających z takich danych wyjściowych.

Modele udostępniane przez Gemini API mogą być używane w wielu różnych aplikacjach generatywnej AI i przetwarzania języka naturalnego (NLP). Korzystanie z tych
funkcji jest możliwe tylko za pomocą Gemini API lub aplikacji internetowej Google AI Studio. Korzystanie z Gemini API podlega też [zasadom dotyczącym niedozwolonych zastosowań generatywnej AI](https://ai.google.dev/gemini-api/docs/zasadom dotyczącym niedozwolonych zastosowań generatywnej AI) oraz
[warunkom korzystania z usługi Gemini API](https://ai.google.dev/gemini-api/docs/warunkom korzystania z usługi Gemini API).

Duże modele językowe (LLM) są tak przydatne, ponieważ są to narzędzia kreatywne, które mogą wykonywać wiele różnych zadań językowych. Niestety oznacza to również, że duże modele językowe mogą generować dane wyjściowe, których się nie spodziewasz, w tym teksty obraźliwe, nietaktowne lub niezgodne z faktami.
Co więcej, niesamowita wszechstronność tych modeli utrudnia też przewidywanie, jakie dokładnie niepożądane dane wyjściowe mogą one generować. Interfejs
Gemini API został zaprojektowany z uwzględnieniem [zasad AI Google](https://ai.google.dev/gemini-api/docs/zasad AI Google), ale to deweloperzy muszą
stosować te modele w sposób odpowiedzialny. Aby pomóc deweloperom w tworzeniu bezpiecznych i odpowiedzialnych aplikacji, Gemini API ma wbudowane filtrowanie treści oraz dostosowywane ustawienia bezpieczeństwa w 4 wymiarach szkodliwości. Więcej informacji znajdziesz w
[przewodniku po ustawieniach bezpieczeństwa](https://ai.google.dev/gemini-api/docs/przewodniku po ustawieniach bezpieczeństwa). Oferuje też funkcję Grounding z włączoną wyszukiwarką Google, która zwiększa wiarygodność informacji. Deweloperzy, których przypadki użycia są bardziej kreatywne i nie polegają na wyszukiwaniu informacji, mogą jednak wyłączyć tę funkcję.

Ten dokument ma na celu przedstawienie niektórych zagrożeń dla bezpieczeństwa, które mogą wystąpić podczas korzystania z LLM, oraz przedstawienie nowych zaleceń dotyczących projektowania i tworzenia bezpiecznych aplikacji. (Pamiętaj, że przepisy prawa mogą również nakładać ograniczenia, ale te kwestie wykraczają poza zakres tego przewodnika).

Podczas tworzenia aplikacji z użyciem LLM zalecamy wykonanie tych czynności:

- Zrozumienie zagrożeń dla bezpieczeństwa związanych z aplikacją
- Rozważenie zmian, które pozwolą zmniejszyć zagrożenia dla bezpieczeństwa
- Przeprowadzenie testów bezpieczeństwa odpowiednich dla danego przypadku użycia
- Zbieranie opinii od użytkowników i monitorowanie użytkowania

Fazy dostosowywania i testowania powinny być powtarzane, aż osiągniesz wydajność odpowiednią dla swojej aplikacji.

![Cykl wdrażania modelu](https://ai.google.dev/static/gemini-api/docs/images/safety_diagram.png?hl=pl)

## Zrozumienie zagrożeń dla bezpieczeństwa związanych z aplikacją

W tym kontekście bezpieczeństwo definiujemy jako zdolność LLM do unikania wyrządzania szkód użytkownikom, na przykład przez generowanie toksycznych treści lub treści promujących stereotypy. Modele dostępne w Gemini API zostały zaprojektowane z
uwzględnieniem [zasad AI Google](https://ai.google.dev/gemini-api/docs/zasad AI Google) w myśl
i korzystanie z nich podlega zasadom dotyczącym [niedozwolonych zastosowań generatywnej AI](https://ai.google.dev/gemini-api/docs/niedozwolonych zastosowań generatywnej AI). Interfejs API ma wbudowane filtry bezpieczeństwa, które pomagają rozwiązać niektóre typowe problemy z modelami językowymi, takie jak toksyczne treści i szerzenie nienawiści, oraz dążą do inkluzywności i unikania stereotypów. Każda aplikacja może jednak stwarzać inne zagrożenia dla użytkowników. Jako właściciel aplikacji musisz znać swoich użytkowników i potencjalne szkody, jakie może wyrządzić Twoja aplikacja, oraz dbać o to, aby aplikacja korzystała z LLM w sposób bezpieczny i odpowiedzialny.

W ramach tej oceny należy wziąć pod uwagę prawdopodobieństwo wystąpienia szkody, określić jej powagę i podjąć kroki w celu jej ograniczenia. Na przykład aplikacja, która generuje eseje na podstawie faktów, musi bardziej uważać na unikanie dezinformacji niż aplikacja, która generuje fikcyjne historie dla rozrywki. Dobrym sposobem na rozpoczęcie badania potencjalnych zagrożeń dla bezpieczeństwa jest przeprowadzenie badań wśród użytkowników końcowych i innych osób, które mogą być narażone na skutki działania aplikacji. Może to przybierać różne formy, np. badanie najnowszych badań w dziedzinie aplikacji, obserwowanie, jak użytkownicy korzystają z podobnych aplikacji, lub przeprowadzenie badania opinii użytkowników, ankiety lub nieformalnych wywiadów z potencjalnymi użytkownikami.

#### Wskazówki dla zaawansowanych

- Porozmawiaj z różnymi potencjalnymi użytkownikami z grupy docelowej o swojej aplikacji i jej przeznaczeniu, aby uzyskać szerszą perspektywę na potencjalne zagrożenia i w razie potrzeby dostosować kryteria różnorodności.
- Więcej szczegółowych wskazówek i dodatkowych materiałów edukacyjnych dotyczących zarządzania ryzykiem związanym z AI znajdziesz w opracowanym przez amerykański Narodowy Instytut Norm i Techniki (NIST) dokumencie [AI Risk Management Framework](https://ai.google.dev/gemini-api/docs/AI Risk Management Framework).
- Publikacja DeepMind na temat
  [etycznych i społecznych zagrożeń związanych z modelami językowymi](https://ai.google.dev/gemini-api/docs/etycznych i społecznych zagrożeń związanych z modelami językowymi)
  szczegółowo opisuje, w jaki sposób aplikacje oparte na modelach językowych
  mogą wyrządzać szkody.

## Rozważenie zmian, które pozwolą zmniejszyć zagrożenia dla bezpieczeństwa i wiarygodności informacji

Teraz, gdy znasz już zagrożenia, możesz zdecydować, jak je ograniczyć. Określenie, które zagrożenia są priorytetowe i jak wiele należy zrobić, aby im zapobiec, to kluczowa decyzja, podobna do ustalania priorytetów błędów w projekcie oprogramowania. Gdy ustalisz priorytety, możesz zacząć zastanawiać się nad rodzajami środków zaradczych, które będą najbardziej odpowiednie. Często proste zmiany mogą przynieść efekty i zmniejszyć ryzyko.

Podczas projektowania aplikacji rozważ te kwestie:

- **Dostrajanie danych wyjściowych modelu** tak, aby lepiej odzwierciedlały to, co jest akceptowalne w kontekście aplikacji. Dostrajanie może sprawić, że dane wyjściowe modelu będą bardziej przewidywalne i spójne, co może pomóc w ograniczeniu niektórych zagrożeń.
- **Udostępnianie metody wprowadzania danych, która ułatwia uzyskiwanie bezpieczniejszych danych wyjściowych.** Dokładne dane wejściowe przekazywane do LLM mogą mieć wpływ na jakość danych wyjściowych.
  Eksperymentowanie z promptami wejściowymi, aby znaleźć te, które działają najbezpieczniej w Twoim przypadku użycia, jest warte wysiłku, ponieważ możesz wtedy udostępnić interfejs użytkownika, który to ułatwia. Możesz na przykład ograniczyć użytkownikom możliwość wyboru tylko z listy rozwijanej promptów wejściowych lub wyświetlać wyskakujące sugestie z opisowymi frazami, które w kontekście Twojej aplikacji działają bezpiecznie.
- **Blokowanie niebezpiecznych danych wejściowych i filtrowanie danych wyjściowych, zanim zostaną wyświetlone użytkownikowi.** W prostych sytuacjach listy blokowania można wykorzystać do identyfikowania i blokowania niebezpiecznych słów lub fraz w promptach lub odpowiedziach albo do wymagania od weryfikatorów ręcznego zmieniania lub blokowania takich treści.
- **Używanie wytrenowanych klasyfikatorów do oznaczania każdego promptu potencjalnymi szkodami lub złośliwymi sygnałami.** Wtedy można zastosować różne strategie obsługi żądań bazujące na typie wykrytych szkód. Jeśli na przykład dane wejściowe są ewidentnie szkodliwe lub mają charakter nadużycia, można je zablokować, a jako dane wyjściowe wyświetlić przygotowaną wcześniej odpowiedź.

  #### Wskazówka dla zaawansowanych

  - Jeśli sygnały wskazują, że dane wyjściowe są szkodliwe,
    aplikacja może zastosować te opcje:
    - Wyświetl komunikat o błędzie lub przygotowane dane wyjściowe.
    - Spróbuj ponownie użyć prompta, jeśli wygenerowane zostaną alternatywne bezpieczne dane wyjściowe, ponieważ czasami ten sam prompt może wywołać
      różne dane wyjściowe.
- **Wprowadzanie zabezpieczeń przed celowym nadużyciem** , np. przypisywanie każdemu użytkownikowi unikalnego identyfikatora i nakładanie limitu na liczbę zapytań użytkowników, które można przesłać w danym okresie. Kolejnym zabezpieczeniem jest próba ochrony przed możliwym wstrzyknięciem prompta. Wstrzyknięcie prompta, podobnie jak wstrzyknięcie kodu SQL, to sposób na to, aby złośliwi użytkownicy mogli zaprojektować prompt wejściowy, który manipuluje danymi wyjściowymi modelu, np. przez wysłanie prompta wejściowego, który instruuje model, aby ignorował wszystkie poprzednie przykłady. Szczegółowe informacje o celowym nadużyciu znajdziesz w
  [zasadach dotyczących niedozwolonych zastosowań generatywnej AI](https://ai.google.dev/gemini-api/docs/zasadach dotyczących niedozwolonych zastosowań generatywnej AI).
- **Dostosowywanie funkcjonalności do czegoś, co z natury wiąże się z mniejszym ryzykiem.**
  Zadania o węższym zakresie (np. wyodrębnianie słów kluczowych z fragmentów tekstu) lub te, które są bardziej nadzorowane przez człowieka (np. generowanie krótkich treści, które będą sprawdzane przez człowieka), często wiążą się z mniejszym ryzykiem. Na przykład zamiast tworzyć aplikację do pisania odpowiedzi na e-mail od zera, możesz ograniczyć ją do rozwijania konspektu lub sugerowania alternatywnych sformułowań.
- **Dostosowywanie ustawień bezpieczeństwa dotyczących szkodliwych treści, aby zmniejszyć prawdopodobieństwo napotkania odpowiedzi, które mogą być szkodliwe.** Gemini API udostępnia ustawienia bezpieczeństwa, które możesz dostosować na etapie prototypowania, aby określić, czy aplikacja wymaga bardziej czy mniej restrykcyjnej konfiguracji bezpieczeństwa. Te ustawienia możesz dostosować w 5 kategoriach filtrów, aby ograniczyć lub zezwolić na określone typy treści. Więcej informacji o
  dostosowywanych ustawieniach bezpieczeństwa dostępnych w Gemini API znajdziesz w przewodniku po [ustawieniach bezpieczeństwa](https://ai.google.dev/gemini-api/docs/ustawieniach bezpieczeństwa).
- **Zmniejszenie potencjalnych nieścisłości zgodnych z prawdą lub halucynacji przez włączenie funkcji powiązanie ze źródłem informacji przy użyciu wyszukiwarki Google.** Pamiętaj, że wiele modeli AI ma charakter eksperymentalny i może zawierać nieścisłe informacje, halucynacje lub inne problematyczne dane wyjściowe. Funkcja powiązania ze źródłem informacji przy użyciu wyszukiwarki Google łączy model Gemini z treściami z internetu w czasie rzeczywistym i działa we wszystkich dostępnych językach. Dzięki temu Gemini może udzielać dokładniejszych odpowiedzi i podawać zweryfikowane źródła poza granicą wiedzy modeli.

## Przeprowadzenie testów bezpieczeństwa odpowiednich dla danego przypadku użycia

Testowanie jest kluczowym elementem tworzenia niezawodnych i bezpiecznych aplikacji, ale zakres, zakres i strategie testowania będą się różnić. Na przykład generator haiku, który służy tylko do zabawy, prawdopodobnie będzie stwarzać mniejsze zagrożenia niż aplikacja przeznaczona do użytku przez kancelarie prawne, która ma podsumowywać dokumenty prawne i pomagać w tworzeniu umów. Generator haiku może być jednak używany przez szerszą grupę użytkowników, co oznacza, że potencjał prób ataku lub nawet niezamierzonych szkodliwych danych wejściowych może być większy. Ważny jest też kontekst implementacji. Na przykład aplikacja, której dane wyjściowe są sprawdzane przez ekspertów przed podjęciem jakichkolwiek działań, może być uznana za mniej prawdopodobną do generowania szkodliwych danych wyjściowych niż identyczna aplikacja bez takiego nadzoru.

Nawet w przypadku aplikacji o stosunkowo niskim ryzyku często trzeba wprowadzić kilka zmian i przeprowadzić kilka testów, zanim poczujesz się pewnie, że możesz ją uruchomić. W przypadku aplikacji AI szczególnie przydatne są 2 rodzaje testów:

- **Testy porównawcze bezpieczeństwa** polegają na zaprojektowaniu danych bezpieczeństwa, które odzwierciedlają sposoby, w jakie aplikacja może być niebezpieczna w kontekście sposobu jej używania, a następnie na sprawdzeniu, jak dobrze aplikacja działa w przypadku tych danych za pomocą zbiorów danych do oceny. Przed testowaniem warto zastanowić się nad minimalnymi akceptowalnymi poziomami danych bezpieczeństwa, aby 1) móc ocenić wyniki testów na podstawie tych oczekiwań i 2) zebrać zbiór danych do oceny na podstawie testów, które oceniają dane, na których najbardziej Ci zależy.

  #### Wskazówki dla zaawansowanych

  - Uważaj na nadmierne poleganie na gotowych rozwiązaniach, ponieważ prawdopodobnie
    będziesz musiał utworzyć własne zbiory danych do testowania przy użyciu oceniających, aby
    w pełni dostosować się do kontekstu aplikacji.
  - Jeśli masz więcej niż 1 dane, musisz zdecydować, jak będziesz je
    wymieniać, jeśli zmiana spowoduje poprawę w przypadku 1 danych, ale
    pogorszenie w przypadku innych. Podobnie jak w przypadku innych inżynierii wydajności, możesz skupić się na najgorszej wydajności w zbiorze danych do oceny, a nie na średniej wydajności.
- **Testy z użyciem szkodliwych danych wejściowych** polegają na proaktywnym próbowaniu zepsucia aplikacji. Celem jest zidentyfikowanie słabych punktów, aby można było podjąć odpowiednie kroki w celu ich naprawienia. Testy z użyciem szkodliwych danych wejściowych mogą wymagać znacznego nakładu czasu i wysiłku ze strony oceniających, którzy mają wiedzę specjalistyczną w zakresie Twojej aplikacji, ale im więcej testów przeprowadzisz, tym większa szansa na wykrycie problemów, zwłaszcza tych, które występują rzadko lub tylko po wielokrotnym uruchomieniu aplikacji.

  - Testy z użyciem szkodliwych danych wejściowych to metoda systematycznej oceny modelu ML z zamiarem ustalenia, jak się on zachowuje, gdy celowo lub nieumyślnie wprowadzimy do niego szkodliwe dane wejściowe:
    - Dane wejściowe mogą być złośliwe, gdy ewidentnie mają za zadanie wygenerować niebezpieczne lub szkodliwe dane wyjściowe – na przykład gdy poprosisz model generujący teksty o wygenerowanie wypowiedzi szerzącej nienawiść do określonej religii.
    - Dane wejściowe są nieumyślnie szkodliwe, gdy one same są nieszkodliwe, ale powodują wygenerowanie szkodliwych danych wyjściowych – na przykład gdy poprosisz model generujący teksty o opisanie osoby o określonym pochodzeniu etnicznym, co spowoduje, że model generuje rasistowską odpowiedź.
  - Test z użyciem szkodliwych danych wejściowych różni się od standardowej oceny składem danych używanych do testowania. W przypadku testów z użyciem szkodliwych danych wejściowych wybierz
    dane testowe, które najprawdopodobniej spowodują wygenerowanie przez model problematycznych danych wyjściowych. Oznacza to, że należy sprawdzić zachowanie modelu pod kątem wszystkich rodzajów szkód, w tym rzadkich lub nietypowych przykładów i przypadków brzegowych, które są istotne z punktu widzenia zasad bezpieczeństwa. Powinny one również uwzględniać różnorodność w różnych wymiarach zdania, takich jak struktura, znaczenie i długość. Więcej informacji o tym, co należy wziąć pod uwagę podczas tworzenia zbioru danych do testowania, znajdziesz w artykule [Google's Responsible AI
    dotyczącym praktyk
    odpowiedzialnej AI w zakresie](https://ai.google.dev/gemini-api/docs/Google's Responsible AI    dotyczącym praktyk    odpowiedzialnej AI w zakresie)
    sprawiedliwości.

    #### Wskazówki dla zaawansowanych

    - Zamiast tradycyjnej metody angażowania osób w „czerwone zespoły”, które mają próbować zepsuć Twoją aplikację, używaj
      [testów automatycznych](https://ai.google.dev/gemini-api/docs/testów automatycznych). W testach automatycznych „zespół red team” to inny model językowy, który znajduje tekst wejściowy, który wywołuje szkodliwe dane wyjściowe z testowanego modelu.może być konieczne przeprowadzenie kilku rund testów.

## Monitorowanie problemów

Niezależnie od tego, ile testów przeprowadzisz i jak wiele środków zaradczych zastosujesz, nigdy nie możesz zagwarantować doskonałości, dlatego z wyprzedzeniem zaplanuj, jak będziesz wykrywać i rozwiązywać problemy. Typowe podejścia obejmują skonfigurowanie monitorowanego kanału, na którym użytkownicy mogą dzielić się opiniami (np. ocena kciukiem w górę lub w dół), oraz przeprowadzenie badania opinii użytkowników, aby proaktywnie zbierać opinie od różnych użytkowników – jest to szczególnie przydatne, jeśli wzorce użytkowania różnią się od oczekiwań.

#### Wskazówki dla zaawansowanych

- Gdy użytkownicy przekazują opinie o produktach AI, mogą one znacznie poprawić wydajność AI
  i wygodę użytkowników, np.
  pomagając Ci wybrać lepsze przykłady do dostrajania promptów. W
  [rozdziale Opinie i kontrola](https://ai.google.dev/gemini-api/docs/rozdziale Opinie i kontrola)
  w [przewodniku Google dotyczącym ludzi i AI](https://ai.google.dev/gemini-api/docs/przewodniku Google dotyczącym ludzi i AI)
  znajdziesz najważniejsze kwestie, które należy wziąć pod uwagę podczas projektowania
  mechanizmów opinii.

## Dalsze kroki

- Więcej informacji o dostosowywanych
  ustawieniach bezpieczeństwa dostępnych w Gemini API znajdziesz w przewodniku po
  [ustawieniach bezpieczeństwa](https://ai.google.dev/gemini-api/docs/ustawieniach bezpieczeństwa).
- Aby zacząć pisać pierwsze prompty, zapoznaj się z [wprowadzeniem do promptów](https://ai.google.dev/gemini-api/docs/wprowadzeniem do promptów) aby zacząć
  pisać pierwsze prompty.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://ai.google.dev/gemini-api/docs/licencją Creative Commons – uznanie autorstwa 4.0), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://ai.google.dev/gemini-api/docs/licencji Apache 2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://ai.google.dev/gemini-api/docs/zasady dotyczące witryny Google Developers). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-04-29 UTC.

Chcesz przekazać coś jeszcze?
