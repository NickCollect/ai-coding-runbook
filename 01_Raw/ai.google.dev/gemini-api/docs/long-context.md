---
source_url: https://ai.google.dev/gemini-api/docs/long-context?hl=pl
fetched_at: 2026-08-03T04:35:03.388615+00:00
title: "D\u0142ugi kontekst \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Długi kontekst

Wiele modeli Gemini ma duże okna kontekstu o wielkości co najmniej 1 mln tokenów.
W przeszłości duże modele językowe (LLM) były znacznie ograniczone przez ilość tekstu (lub tokenów), które można było przekazać do modelu jednocześnie.
Długie okno kontekstu Gemini otwiera wiele nowych przypadków użycia i paradygmatów deweloperskich.

Kod, którego używasz już w przypadkach takich jak [tekst
generowanie](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl) lub [multimodalne
dane wejściowe](https://ai.google.dev/gemini-api/docs/vision?hl=pl), będzie działać bez zmian w przypadku długiego kontekstu.

Z tego dokumentu dowiesz się, co możesz osiągnąć za pomocą modeli z oknami kontekstu o wielkości co najmniej 1 mln tokenów. Na tej stronie znajdziesz krótki opis okna kontekstu oraz informacje o tym, jak deweloperzy powinni myśleć o długim kontekście, o różnych przypadkach użycia długiego kontekstu w rzeczywistych sytuacjach oraz o sposobach optymalizacji wykorzystania długiego kontekstu.

Rozmiary okien kontekstu poszczególnych modeli znajdziesz na stronie
[Modele](https://ai.google.dev/gemini-api/docs/models?hl=pl).

## Czym jest okno kontekstu?

Podstawowy sposób korzystania z modeli Gemini polega na przekazywaniu do modelu informacji (kontekstu), na podstawie których model generuje odpowiedź. Okno kontekstu można porównać do pamięci krótkotrwałej. Ilość informacji, które można przechowywać w pamięci krótkotrwałej, jest ograniczona. To samo dotyczy modeli generatywnych.

Więcej informacji o tym, jak działają modele, znajdziesz w naszym [przewodniku po modelach generatywnych](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pl#under-the-hood).

## Pierwsze kroki z długim kontekstem

Wcześniejsze wersje modeli generatywnych mogły przetwarzać tylko 8 tys. tokenów naraz. Nowsze modele poszły o krok dalej i akceptują 32 tys. lub nawet 128 tys. tokenów. Gemini to pierwszy model, który może akceptować 1 mln tokenów.

W praktyce 1 mln tokenów to:

- 50 tys. wierszy kodu (przy standardowej liczbie 80 znaków w wierszu);
- wszystkie wiadomości tekstowe wysłane w ciągu ostatnich 5 lat;
- 8 powieści w języku angielskim o średniej długości;
- transkrypcje ponad 200 odcinków podcastów o średniej długości.

W przypadku bardziej ograniczonych okien kontekstu, które są powszechne w wielu innych modelach, często trzeba stosować strategie takie jak arbitralne usuwanie starych wiadomości, podsumowywanie treści, używanie RAG z bazami danych wektorowych lub filtrowanie promptów w celu zaoszczędzenia tokenów.

Chociaż te techniki pozostają przydatne w określonych scenariuszach, rozbudowane okno kontekstu Gemini umożliwia bardziej bezpośrednie podejście: przekazywanie wszystkich istotnych informacji z góry. Ponieważ modele Gemini zostały zaprojektowane specjalnie z myślą o obsłudze dużego kontekstu, wykazują one dużą skuteczność w uczeniu się w kontekście. Na
przykład, korzystając tylko z materiałów instruktażowych w kontekście (500-stronicowej gramatyki
, słownika i ok. 400 równoległych zdań), Gemini
[nauczył się tłumaczyć](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf)
z angielskiego na kalamang – język papuaski, którym posługuje się
mniej niż 200 osób – z jakością podobną do jakości tłumaczenia wykonanego przez człowieka, który korzysta z tych samych
materiałów. Ilustruje to zmianę paradygmatu, którą umożliwia długi kontekst Gemini, otwierając nowe możliwości dzięki solidnemu uczeniu się w kontekście.

## Przypadki użycia długiego kontekstu

Chociaż standardowym przypadkiem użycia większości modeli generatywnych jest nadal wprowadzanie tekstu, rodzina modeli Gemini umożliwia nowy paradygmat przypadków użycia multimodalnych. Modele te mogą natywnie rozumieć tekst, filmy, dźwięk i obrazy. Towarzyszy im
interfejs [Gemini API, który dla
wygody przyjmuje multimodalne typy
plików](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=pl).

### Długi tekst

Tekst okazał się warstwą inteligencji, która leży u podstaw wielu postępów w dziedzinie LLM. Jak wspomnieliśmy wcześniej, wiele praktycznych ograniczeń LLM wynikało z tego, że nie miały one wystarczająco dużego okna kontekstu, aby wykonywać określone zadania. Doprowadziło to do szybkiego przyjęcia generowania wspomaganego wyszukiwaniem (RAG) i innych technik, które dynamicznie dostarczają modelowi odpowiednie informacje kontekstowe. Teraz, dzięki coraz większym oknom kontekstu, dostępne są nowe techniki, które otwierają nowe przypadki użycia.

Do nowych i standardowych przypadków użycia długiego kontekstu opartego na tekście należą:

- Podsumowywanie dużych korpusów tekstowych
  - Wcześniejsze opcje podsumowywania w przypadku modeli z mniejszym kontekstem wymagały użycia okna przesuwnego lub innej techniki, aby zachować stan poprzednich sekcji, gdy do modelu przekazywane są nowe tokeny.
- Pytania i odpowiedzi
  - W przeszłości było to możliwe tylko w przypadku RAG ze względu na ograniczoną ilość kontekstu i niską zdolność modeli do przywoływania faktów.
- Przepływy pracy agentów
  - Tekst jest podstawą tego, jak agenci zachowują stan tego, co zrobili i co muszą zrobić. Brak wystarczających informacji o świecie i celu agenta ogranicza jego niezawodność.

[Uczenie się w kontekście z wieloma przykładami](https://arxiv.org/pdf/2404.11018) to jedna z
najbardziej unikalnych możliwości, które otwierają modele z długim kontekstem. Badania wykazały, że przyjęcie powszechnego paradygmatu „jednego przykładu” lub „wielu przykładów”, w którym model otrzymuje jeden lub kilka przykładów zadania, i zwiększenie tej liczby do setek, tysięcy, a nawet setek tysięcy przykładów może prowadzić do nowych możliwości modelu. Wykazano również, że to podejście z wieloma przykładami działa podobnie jak modele, które zostały dostrojone do konkretnego zadania. W przypadkach użycia, w których skuteczność modelu Gemini nie jest jeszcze wystarczająca do wdrożenia produkcyjnego, możesz wypróbować podejście z wieloma przykładami. Jak dowiesz się później w sekcji Optymalizacja długiego kontekstu, buforowanie kontekstu sprawia, że ten typ obciążenia z dużą liczbą tokenów wejściowych jest znacznie bardziej opłacalny, a w niektórych przypadkach nawet zmniejsza opóźnienie.

### Długi film

Użyteczność treści wideo była przez długi czas ograniczona brakiem dostępności samego medium. Trudno było przeglądać treści, transkrypcje często nie oddawały niuansów filmu, a większość narzędzi nie przetwarza obrazu, tekstu i dźwięku razem. Dzięki Gemini możliwości tekstowe w długim kontekście przekładają się na zdolność do rozumowania i odpowiadania na pytania dotyczące danych wejściowych multimodalnych z zachowaniem stałej wydajności.

Do nowych i standardowych przypadków użycia długiego kontekstu wideo należą:

- Pytania i odpowiedzi dotyczące filmu
- Pamięć wideo, jak pokazano w projekcie [Google Project Astra](https://deepmind.google/technologies/gemini/project-astra/?hl=pl)
- Dodawanie napisów do filmów
- Systemy rekomendacji filmów, dzięki wzbogacaniu istniejących metadanych o nowe informacje multimodalne
- Dostosowywanie filmów poprzez analizowanie korpusu danych i powiązanych metadanych wideo, a następnie usuwanie części filmów, które nie są istotne dla widza
- Moderowanie treści wideo
- Przetwarzanie filmów w czasie rzeczywistym

Podczas pracy z filmami ważne jest, aby wziąć pod uwagę, jak są one [przetwarzane na tokeny](https://ai.google.dev/gemini-api/docs/tokens?hl=pl#media-token), co wpływa na
rozliczenia i limity użycia. Więcej informacji o promptach z plikami wideo znajdziesz w
[przewodniku po promptach](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=pl#prompting-with-videos).

### Długi dźwięk

Modele Gemini były pierwszymi natywnie multimodalnymi dużymi modelami językowymi, które potrafiły rozumieć dźwięk. W przeszłości typowy przepływ pracy dewelopera polegał na łączeniu ze sobą wielu modeli specyficznych dla danej domeny, np. modelu zamiany mowy na tekst i modelu tekst na podstawie tekstu, w celu przetwarzania dźwięku. Prowadziło to do dodatkowego opóźnienia wymaganego przez wykonywanie wielu żądań typu round-trip oraz do zmniejszenia wydajności, co zwykle przypisywano rozłączonym architekturam konfiguracji wielu modeli.

Do nowych i standardowych przypadków użycia kontekstu audio należą:

- Transkrypcja i tłumaczenie w czasie rzeczywistym
- Pytania i odpowiedzi dotyczące podcastów i filmów
- Transkrypcja i podsumowywanie spotkań
- Asystenci głosowi

Więcej informacji o promptach z plikami audio znajdziesz w [przewodniku po promptach](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=pl#prompting-with-videos).

## Optymalizacje długiego kontekstu

Podstawową optymalizacją podczas pracy z długim kontekstem i modelami Gemini
jest używanie [buforowania
kontekstu](https://ai.google.dev/gemini-api/docs/caching?hl=pl). Oprócz wcześniejszej niemożliwości przetwarzania dużej liczby tokenów w jednym żądaniu, głównym ograniczeniem był koszt. Jeśli masz aplikację „czat z danymi”, w której użytkownik przesyła 10 plików PDF, film i kilka dokumentów roboczych, w przeszłości musiałbyś pracować z bardziej złożonym narzędziem lub platformą generowania wspomaganego wyszukiwaniem (RAG), aby przetworzyć te żądania i zapłacić znaczną kwotę za tokeny przeniesione do okna kontekstu. Teraz możesz buforować pliki przesyłane przez użytkownika i płacić za ich przechowywanie na podstawie godzin. Na przykład koszt danych wejściowych i wyjściowych na żądanie w przypadku Gemini Flash jest ok. 4 razy niższy niż standardowy koszt danych wejściowych i wyjściowych, więc jeśli użytkownik wystarczająco często czatuje z danymi, możesz jako deweloper zaoszczędzić sporo pieniędzy.

## Ograniczenia długiego kontekstu

W różnych sekcjach tego przewodnika mówiliśmy o tym, jak modele Gemini osiągają wysoką skuteczność w różnych testach wyszukiwania igły w stogu siana. Testy te uwzględniają najbardziej podstawową konfigurację, w której szukasz jednej igły. W przypadkach, w których możesz mieć wiele „igieł” lub konkretnych informacji, których szukasz, model nie działa z taką samą dokładnością. Skuteczność może się znacznie różnić w zależności od kontekstu. Należy o tym pamiętać, ponieważ istnieje nieodłączny kompromis między uzyskaniem odpowiednich informacji a kosztem. Możesz uzyskać ok. 99% skuteczności w przypadku pojedynczego zapytania, ale za każdym razem, gdy je wysyłasz, musisz zapłacić za tokeny wejściowe. Jeśli więc chcesz uzyskać 100 informacji i potrzebujesz 99% skuteczności, prawdopodobnie będziesz musiał wysłać 100 żądań. To dobry przykład sytuacji, w której buforowanie kontekstu może znacznie zmniejszyć koszty związane z używaniem modeli Gemini przy zachowaniu wysokiej skuteczności.

## Najczęstsze pytania

### Gdzie najlepiej umieścić zapytanie w oknie kontekstu?

W większości przypadków, zwłaszcza jeśli całkowity kontekst jest długi, skuteczność modelu będzie lepsza, jeśli umieścisz zapytanie lub pytanie na końcu prompta (po całym innym kontekście).

### Czy dodanie większej liczby tokenów do zapytania pogarsza skuteczność modelu?

Ogólnie rzecz biorąc, jeśli nie musisz przekazywać tokenów do modelu, najlepiej ich nie przekazywać. Jeśli jednak masz dużą liczbę tokenów z informacjami i chcesz zadać pytania dotyczące tych informacji, model jest w stanie je wyodrębnić (w wielu przypadkach z dokładnością do 99%).

### Jak mogę obniżyć koszty związane z zapytaniami w długim kontekście?

[Jeśli masz podobny zestaw tokenów lub kontekst, którego chcesz używać wielokrotnie, buforowanie kontekstu może pomóc zmniejszyć koszty związane z zadawaniem pytań dotyczących tych informacji.](https://ai.google.dev/gemini-api/docs/caching?hl=pl)

### Czy długość kontekstu wpływa na opóźnienie modelu?

W przypadku każdego żądania występuje pewne stałe opóźnienie, niezależnie od jego rozmiaru, ale ogólnie dłuższe zapytania będą miały większe opóźnienie (czas do pierwszego tokena).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-22 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-22 UTC."],[],[]]
