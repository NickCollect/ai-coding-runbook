---
source_url: https://ai.google.dev/gemini-api/docs/billing?hl=pl
fetched_at: 2026-06-15T06:21:02.942510+00:00
title: "P\u0142atno\u015bci \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Płatności

Ten przewodnik zawiera omówienie różnych opcji płatności za interfejs Gemini API, wyjaśnienie, jak włączyć płatności i monitorować wykorzystanie, oraz odpowiedzi na najczęstsze pytania dotyczące płatności.

## Informacje o płatnościach i poziomach

Płatności za Gemini API są naliczane na podstawie Twojej historii płatności.

| Kategoria wykorzystania | Kwalifikacje | [Limit poziomu płatności](#spend-caps) |
| --- | --- | --- |
| **Free** | [Aktywny projekt](https://ai.google.dev/gemini-api/docs/api-key?hl=pl#google-cloud-projects) lub bezpłatny okres próbny | Nie dotyczy |
| **Poziom 1** | [Skonfiguruj i połącz aktywne konto rozliczeniowe](#setup-billing) | 250 USD |
| **Poziom 2** | Wypłata 100 USD + 3 dni od pierwszej udanej płatności | 2000 USD |
| **Pracownik obsługi klienta poziomu 3** | Wypłata 1000 USD + 30 dni od pierwszej udanej płatności | 20 000–100 000 USD i więcej |

Nowe konta zaczynają od poziomu bezpłatnego, który umożliwia dostęp do [określonych modeli](https://ai.google.dev/gemini-api/docs/pricing?hl=pl) w Gemini API i AI Studio, do limitów [szybkości](https://aistudio.google.com/rate-limit?hl=pl) na poziomie bezpłatnym.

Aby wdrażać aplikacje bezpośrednio z trybu kompilacji, możesz użyć **poziomu startowego Google Cloud**. Ten poziom umożliwia publikowanie maksymalnie 2 aplikacji full stack bez konfigurowania projektu w chmurze Google Cloud ani konta rozliczeniowego.
Szczegółowe informacje znajdziesz w artykule [Wdrażanie z Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=pl), a więcej informacji znajdziesz w [dokumentacji poziomu Starter Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=pl).

Aby uzyskać dostęp do wyższych limitów żądań, korzystać z zaawansowanych modeli i mieć pewność, że Twoje prompty i odpowiedzi **nie** będą używane do ulepszania usług Google\*, możesz [połączyć konto rozliczeniowe i [dokonać przedpłaty](#prepay), aby przejść na poziomy płatne](#setup-billing).
Następnie będziesz przechodzić na wyższe poziomy w zależności od łącznych wydatków i wieku konta. Na poziomie 3 możesz mieć możliwość przejścia na [płatność po wykonaniu usługi](#postpay).

Poziomy, limity szybkości i maksymalne kwoty na koncie rozliczeniowym są określane na poziomie [konta rozliczeniowego](#cloud-billing).

\* *Prywatność danych klasy korporacyjnej: więcej informacji o wykorzystywaniu danych w usługach płatnych znajdziesz w [Warunkach korzystania z usługi](https://ai.google.dev/gemini-api/terms?hl=pl#data-use-paid).*

## Konfigurowanie płatności w celu uzyskania dostępu do wersji płatnej

Możesz utworzyć projekt i skonfigurować rozliczenia lub zaimportować istniejący projekt, aby przejść na poziom płatny w [Google AI Studio](https://aistudio.google.com/projects?hl=pl). Przejście z poziomu bezpłatnego na poziom płatny oznacza połączenie konta rozliczeniowego i [dokonanie przedpłaty](#prepay) w wysokości co najmniej 10 USD (lub równowartości w innych walutach), aby dodać środki do konta.

1. Otwórz stronę [Klucze interfejsu API](https://aistudio.google.com/api-keys?hl=pl) w AI Studio, stronę [Projekty](https://aistudio.google.com/projects?hl=pl) lub dowolne miejsce w AI Studio, w którym widzisz przycisk **Skonfiguruj płatności**.
   - Nowi użytkownicy będą mieli domyślnie utworzony [projekt i klucz interfejsu API](https://ai.google.dev/gemini-api/docs/api-key?hl=pl#google-cloud-projects).
   - Jeśli potrzebujesz nowego klucza, kliknij [**Utwórz klucz interfejsu API**](https://aistudio.google.com/api-keys?hl=pl) i postępuj zgodnie z instrukcjami w oknie, aby dodać do tabeli parę klucz – projekt.
2. Znajdź projekt w ramach poziomu bezpłatnego, który chcesz przekształcić w projekt w ramach wersji płatnej, i w kolumnie *Wersja rozliczeniowa* kliknij **Skonfiguruj rozliczenia**.
3. Jeśli nigdy wcześniej nie konfigurowano konta rozliczeniowego Google:
   - Pojawi się prośba o wybranie kraju w celu zaakceptowania Warunków korzystania z usługi.
   - Następnie wpisz lub potwierdź informacje kontaktowe i formę płatności, aby kontynuować.
4. Jeśli masz już skonfigurowane konta rozliczeniowe Google:
   - Pojawi się prośba o wybranie jednego z dotychczasowych kont rozliczeniowych.
   - Jeśli nie chcesz używać żadnego z dotychczasowych kont, kliknij **Dodaj nowe konto rozliczeniowe** i wypełnij lub potwierdź dane kontaktowe oraz formę płatności, aby kontynuować.
5. Następnie możesz:
   - prośbę o dokonanie przedpłaty w wysokości co najmniej 10 PLN, aby dokończyć konfigurację rozliczeń (co oznacza, że Twoje konto zostało automatycznie przypisane do planu rozliczeniowego [Przedpłata](#prepay)),
   - Wybierz jeden z planów rozliczeniowych: [przedpłata](#prepay) lub [płatność po wykonaniu usługi](#postpay).
   - przypisany do abonamentu [Postpay](#postpay) na okres przejściowy, dopóki nowy system Prepay nie zostanie wdrożony u wszystkich użytkowników (od 23 marca 2026 r.);
6. Po dokonaniu przedpłaty lub wybraniu płatności po wykonaniu usługi zakładanie konta zostanie zakończone.

### Przejście na wyższy poziom płatny

Jeśli korzystasz już z płatnej wersji i spełniasz [kryteria](#about-billing) zmiany pakietu, automatycznie przejdziesz na wyższy pakiet (z uwzględnieniem [czasu przetwarzania](#processing-times)).

## Sprawdzanie stanu płatności

Po [połączeniu konta rozliczeniowego](#setup-billing) z projektem możesz monitorować jego stan na [stronie Rozliczenia AI Studio](https://aistudio.google.com/billing?hl=pl). W przeciwieństwie do poziomu bezpłatnego status poziomu płatnego jest dynamiczny. Poziom użytkowania jest określany na podstawie historii konta, ale Gemini API będzie obsługiwać żądania tylko wtedy, gdy masz dodatnie saldo środków [przedpłaty](#prepay).

Na stronie [Projekty](https://aistudio.google.com/projects?hl=pl) w kolumnie *Wersja usługi* możesz sprawdzić wersję usługi i abonament projektu. W kolumnach *Wersja usługi* lub *Stan* wyświetlają się działania związane ze stanem płatności, które musisz wykonać w przypadku projektu:

- „***Skonfiguruj płatności***”, jeśli do projektu nie jest dołączone konto rozliczeniowe.
- „***Skonfiguruj płatność z góry***”, jeśli projekt ma przypisane konto rozliczeniowe, ale wymaga korzystania z planu płatności [z góry](#prepay), który należy skonfigurować.
- „***Brak środków***”, jeśli konto rozliczeniowe jest wymagane do zakupu środków, ale konto płatności przedpłaconych nie jest skonfigurowane lub dostępne środki zostały wyczerpane.

Kliknij dowolny komunikat, aby wykonać niezbędne działania.

## Monitorowanie wykorzystania

Wykorzystanie Gemini API możesz śledzić w [Google AI Studio](https://aistudio.google.com/usage?hl=pl) w sekcji **Panel** > **Wykorzystanie**.

## Abonamenty

Plany płatności za Gemini API i AI Studio dzielą się na 2 kategorie, które określają, kiedy płacisz za korzystanie z usługi: przedpłata i płatność po wykorzystaniu. Przypisany plan płatności możesz sprawdzić, a metodami płatności zarządzać na stronie [Płatności za AI Studio](https://aistudio.google.com/billing?hl=pl).

### Przedpłata

W ramach abonamentu z przedpłatą kupujesz środki, które są dodawane do salda przedpłaty przed rozpoczęciem korzystania z Gemini API. Koszty korzystania z interfejsu API są odejmowane od salda przedpłaty [w czasie zbliżonym do rzeczywistego](#processing-times).
Możesz dokonywać przedpłat, [dodając środki](#buy-credits) do konta lub konfigurując [automatyczne doładowanie](#auto-reload). Po zakupie środków niewykorzystane środki tracą ważność po 12 miesiącach i [nie podlegają zwrotowi](#refunds), z wyjątkiem sytuacji, gdy [przejdziesz na konto z płatnościami po fakcie](#postpay).

Gdy saldo środków przedpłaty na koncie rozliczeniowym osiągnie 0 USD, wszystkie klucze interfejsu API we wszystkich projektach połączonych z tym kontem rozliczeniowym przestaną działać jednocześnie. Środki przedpłaty można wykorzystać tylko na pokrycie kosztów korzystania z Gemini API. Nie można ich używać do płacenia za inne usługi Google Cloud.

Nowi użytkownicy domyślnie korzystają z planu płatności z przedpłatą. W przypadku projektów, które powstały przed wprowadzeniem planów rozliczeniowych przedpłaty i płatności z dołu, może być konieczne [zaktualizowanie szczegółów rozliczeniowych projektu](#verify-billing), zanim będzie można dalej korzystać z interfejsu Gemini API.

*Pamiętaj, że przedpłata nie jest dostępna w przypadku kont [zafakturowanych (offline)](https://docs.cloud.google.com/billing/docs/concepts?hl=pl#billing_account_types).*

#### Kupowanie środków

Możesz ręcznie kupić środki przed rozpoczęciem korzystania z Gemini API, aby zasilić nimi saldo konta przedpłaty.

Aby kupić środki, otwórz stronę [Płatności w AI Studio](https://aistudio.google.com/billing?hl=pl) i kliknij **Kup środki**. Minimalny zakup to 10 USD. Maksymalna kwota środków, za które możesz zapłacić z góry, to 5000 USD.

#### Odświeżaj automatycznie

Automatyczne doładowanie to opcjonalna funkcja, która automatycznie doładowuje środki na koncie przedpłaconym, gdy są one na wyczerpaniu. Jest to przydatne, aby zapobiec przerwom w działaniu usługi.

Automatyczne doładowanie możesz skonfigurować, a jego stan sprawdzić na karcie *Dostępne środki* na stronie [Płatności w AI Studio](https://aistudio.google.com/billing?hl=pl). Kliknij **Skonfiguruj automatyczne doładowanie** lub **Zarządzaj automatycznym doładowaniem**, aby ustawić formę płatności, kwotę doładowania i minimalne saldo, które aktywuje płatność za doładowanie.

#### Miesięczny limit automatycznego obciążenia

Miesięczny limit automatycznych obciążeń jest dostępny dla użytkowników płatności z góry i pomaga zapobiegać nieoczekiwanym kosztom wynikającym z częstych automatycznych doładowań środków. Za pomocą tej funkcji możesz ustawić maksymalny limit automatycznych doładowań środków w ramach jednego cyklu rozliczeniowego. Gdy łączna kwota automatycznych doładowań w cyklu rozliczeniowym osiągnie ten limit, system wyłączy automatyczne doładowanie do początku następnego miesiąca. Jednorazowe płatności inicjowane ręcznie nie są wliczane do tego limitu.

Aby ustawić miesięczny limit automatycznego obciążenia, gdy włączone jest automatyczne doładowanie:

1. Otwórz stronę [Rozliczenia AI Studio](https://aistudio.google.com/billing?hl=pl).
2. Kliknij **Zarządzaj automatycznym doładowaniem**.
3. Rozwiń sekcję **Limit miesięczny** i wpisz maksymalny limit miesięczny automatycznego doładowania.
4. Kliknij **Zapisz**.

### Płatność po wykonaniu usługi

W przypadku planu rozliczeniowego z płatnością po wykonaniu usługi na Twoim koncie rozliczeniowym Cloud gromadzą się koszty, a płatność jest pobierana automatycznie na koniec miesiąca lub gdy koszty osiągną [automatycznie przypisany limit wydatków](#tier-spend-caps) na podstawie poziomu konta.
Płatność zostanie pobrana z formy płatności powiązanej z Twoim kontem płatności Postpay, którym możesz zarządzać na stronie [Rozliczenia AI Studio](https://aistudio.google.com/billing?hl=pl).

Gdy spełnisz [kryteria poziomu 3](#about-billing), możesz ręcznie przejść z abonamentu przedpłaconego na abonament z płatnością po wykorzystaniu. Aby zmienić abonament, musisz kliknąć przycisk **Przejdź na abonament z płatnością po wykorzystaniu**, który pojawi się w prawym górnym rogu strony [Płatności w AI Studio](https://aistudio.google.com/billing?hl=pl), gdy Twoje konto będzie spełniać wymagania.

Na stronie **Rozliczenia** możesz sprawdzić saldo, terminy płatności i wcześniejsze płatności, a także dokonywać płatności i zarządzać formami płatności.

Podczas [konfigurowania płatności](#setup-billing) za nowy projekt, jeśli kwalifikujesz się do płatności po wykonaniu usługi, w oknie dialogowym [konfiguracji płatności](#setup-billing) możesz wybrać przedpłatę lub płatność po wykonaniu usługi.

Po przełączeniu konta rozliczeniowego Cloud na plan płatności po wykorzystaniu wszystkie projekty połączone z tym kontem rozliczeniowym zostaną przełączone na ten plan. Nie możesz przenieść tego konta rozliczeniowego z powrotem na abonament z przedpłatą. Możesz przenieść projekt na konto rozliczeniowe z innym planem rozliczeniowym, aby zmienić cykl rozliczeniowy tego projektu. Więcej informacji znajdziesz w dokumentacji Cloud na temat [zarządzania rozliczeniami projektów](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=pl).

Więcej informacji o cyklu płatności po wykonaniu usługi znajdziesz w [przewodniku po Rozliczeniach usługi Google Cloud](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=pl).

## Limity wydatków

Interfejs Gemini API obsługuje miesięczne limity wydatków na poziomie konta rozliczeniowego i projektu. Te ustawienia mają na celu ochronę Twojego konta przed nieoczekiwanymi przekroczeniami limitu oraz ochronę ekosystemu, aby zapewnić dostępność usługi.

*Pamiętaj, że limity wydatków nie są dostępne w przypadku kont [zafakturowanych (offline)](https://docs.cloud.google.com/billing/docs/concepts?hl=pl#billing_account_types).*

### Limity wydatków na projekt

W AI Studio możesz ustawić własne limity wydatków na [poziomie projektu](https://ai.google.dev/gemini-api/docs/api-key?hl=pl#google-cloud-projects). Jest to przydatne, jeśli masz kilka projektów na tym samym koncie rozliczeniowym i chcesz mieć pewność, że każdy z nich ma dostęp do wystarczającej części łącznego limitu wydatków.

Konta z [rolami](https://docs.cloud.google.com/iam/docs/roles-overview?hl=pl) edytującego, właściciela lub administratora projektu mogą ustawiać limity wydatków na projekt w AI Studio na stronie [Wydatki](https://aistudio.google.com/spend?hl=pl) w sekcji **Miesięczny limit wydatków** > **Edytuj limit wydatków**.

Szczegółowe informacje o konkretnych uprawnieniach Google Cloud IAM wymaganych do wyświetlania lub edytowania limitów wydatków i informacji rozliczeniowych w AI Studio znajdziesz w [przewodniku rozwiązywania problemów z AI Studio](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=pl#iam-permissions).

Jeśli [przeniesiesz projekt na inne konto rozliczeniowe](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=pl#change_the_billing_account_for_a_project), ustawiony wcześniej limit wydatków dla tego projektu zostanie zachowany, ale zgromadzone wydatki zostaną zresetowane do 0 USD w nowym cyklu rozliczeniowym.

W przypadku długotrwałych zadań, takich jak zakończenie [trybu wsadowego](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl) i sesje agenta, mogą wystąpić przekroczenia limitu wydatków projektu.

Czas przetwarzania danych rozliczeniowych w AI Studio może się opóźnić nawet o 10 minut. Jeśli dane rozliczeniowe nie zostaną przetworzone przed naliczeniem kolejnych opłat, możesz przekroczyć limit projektu.

### Limity wydatków na poszczególnych poziomach konta rozliczeniowego

Każdy [poziom](#about-billing) ma maksymalny limit wydatków miesięcznych:

| Kategoria wykorzystania | Limit wydatków |
| --- | --- |
| **Free** | Nie dotyczy |
| **Poziom 1** | 250 USD |
| **Poziom 2** | 2000 USD |
| **Pracownik obsługi klienta poziomu 3** | 20 000–100 000 USD |

Miesięczne limity wykorzystania interfejsu Gemini API są egzekwowane na poziomie [konta rozliczeniowego](#cloud-billing). Domyślne limity są wstępnie ustawione, ale możesz [poprosić o ich zwiększenie](https://docs.google.com/forms/d/e/1FAIpQLSdiP6BWJyNNN65lnwnlOr-5Kv0MOFp0jLQyqi_ixVCfddqWBw/viewform?hl=pl), aby dostosować je do większego wykorzystania. Łączne wydatki są sumowane we wszystkich połączonych projektach, w których włączona jest usługa Gemini API. Gdy łączna kwota na koncie osiągnie limit poziomu, usługa zostanie wstrzymana we wszystkich projektach połączonych z tym kontem rozliczeniowym do początku następnego cyklu rozliczeniowego (1 dnia każdego miesiąca).

#### Sprawdzanie wydatków na koncie rozliczeniowym

Aby ocenić historyczne miesięczne wydatki i sprawdzić, czy nowe [limity wydatków na poziomie konta rozliczeniowego](#tier-spend-caps) będą miały wpływ na bieżące projekty, wykonaj te czynności:

1. W konsoli Google Cloud otwórz stronę [Raporty konta rozliczeniowego Cloud](https://console.cloud.google.com/billing/reports?hl=pl).
   - Jeśli masz więcej niż 1 konto rozliczeniowe, w oknie potwierdzenia wybierz konto rozliczeniowe Cloud, dla którego chcesz wyświetlić raporty o kosztach.
2. W sekcji „Bieżący miesiąc” raport jest domyślnie ustawiony na „Grupuj według usługi”. W kolumnie **Usługa** zobaczysz **Gemini API**, a w kolumnie **Koszt użycia** – łączne wydatki.
3. Aby wyświetlić szczegółowe koszty ograniczone do użycia Gemini API, ustaw filtr **Grupuj według** na **SKU**, a filtr **Usługi** na **Gemini API**.
4. Dostosuj filtr **Zakres czasu według daty wykorzystania** do wybranego zakresu, aby ocenić wydatki historyczne w danym okresie.

## Czas oczekiwania

Sygnały i aktualizacje dotyczące rozliczeń nie zawsze są wysyłane w czasie rzeczywistym.

- **Wykorzystanie środków:** koszty wykorzystania są zwykle pobierane z Twojego salda w ciągu kilku minut.
- **Potwierdzenie płatności:** większość płatności kartą jest realizowana natychmiast, ale niektóre formy płatności (np. przelewy bankowe) mogą być przetwarzane przez kilka dni. Usługi
  zostaną wznowione lub uaktualnione dopiero po oficjalnym potwierdzeniu zakupu środków.
- **Przejście na wyższy poziom:** po dokonaniu płatności lub spełnieniu [kryteriów przejścia na wyższy poziom](#about-billing) zwykle następuje w ciągu 10 minut.
- **Wykresy z podziałem łącznego kosztu:** wykresy pokazujące podział łącznego kosztu na stronach [Płatności](https://aistudio.google.com/billing?hl=pl) i [Wydatki](https://aistudio.google.com/spend?hl=pl) mogą być aktualizowane do 24 godzin.

Aby dowiedzieć się więcej o potencjalnych opóźnieniach w rozliczeniach, zapoznaj się z przewodnikami po Rozliczeniach usługi Google Cloud dotyczącymi [cyklu rozliczeniowego](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=pl#delayed-billing) i [opóźnień transakcji](https://docs.cloud.google.com/billing/docs/how-to/view-history?hl=pl#missing-transactions).

## Zwroty środków

W przypadku kont rozliczeniowych **przedpłaconych** zwroty środków nie są dozwolone, z wyjątkiem sytuacji, gdy zmieniasz typ konta.

**Gdy konto z przedpłatą zostanie przekształcone w konto z płatnościami po fakcie** (po spełnieniu [kryteriów](#about-billing) i [ręcznym uaktualnieniu](#postpay) konta), konto z przedpłatą zostanie zamknięte, a wszystkie pozostałe środki z przedpłaty zostaną automatycznie zwrócone na zarejestrowaną formę płatności.

Jeśli [zamkniesz](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=pl#close-a-billing-account)
konto przedpłacone z innego powodu niż przejście na płatności po fakcie, wszystkie
pozostałe środki przedpłacone zostaną utracone.

Zakupione środki wygasają po roku. Po wygaśnięciu środki przepadają i nie można ich odzyskać.

Konta **płatności odroczonych** podlegają [zasadom zwrotów Google Cloud](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=pl#request_a_refund).

## Konta rozliczeniowe Cloud

Usługa Gemini API korzysta z [kont rozliczeniowych Cloud](https://cloud.google.com/billing/docs/concepts?hl=pl) do rozliczeń, które możesz [skonfigurować bezpośrednio w AI Studio](#setup-billing). W AI Studio możesz śledzić wydatki, analizować koszty i dokonywać płatności.

Poziomy, limity szybkości i maksymalne kwoty na koncie rozliczeniowym są określane na poziomie konta rozliczeniowego.

### Projekty i klucze interfejsu API

Wszystkie [projekty](https://ai.google.dev/gemini-api/docs/api-key?hl=pl#google-cloud-projects) połączone z kontem rozliczeniowym Cloud dziedziczą poziom wykorzystania tego konta oraz powiązane z nim limity stawek i limity konta. Jeśli [zmienisz projekt](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=pl#change_the_billing_account_for_a_project) z jednego konta rozliczeniowego na inne, jego poziom, a w konsekwencji limity stawek i limity konta, zostaną zmienione na poziom nowego konta rozliczeniowego.

Łączne wydatki (na wszystkie usługi Google Cloud) i wiek konta we wszystkich projektach powiązanych z kontem rozliczeniowym są brane pod uwagę przy określaniu [poziomu](#about-billing) tego konta rozliczeniowego.

Możesz [odłączyć projekt](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=pl#disable_billing_for_a_project) od konta rozliczeniowego, aby wrócić do bezpłatnego poziomu.

[Klucze interfejsu API](https://ai.google.dev/gemini-api/docs/api-key?hl=pl) to dane logowania generowane w projekcie.
Nie mają one niezależnych ustawień płatności, ale dziedziczą limity poziomów i stan płatności projektu. Łączne wykorzystanie wszystkich kluczy w projekcie jest wliczane do limitu wydatków tego projektu i całkowitych wydatków na koncie rozliczeniowym.

## Najczęstsze pytania

W kolejnych sekcjach znajdziesz odpowiedzi na najczęstsze pytania.

### Za co płacę?

Ceny Gemini API zależą od tych czynników:

- Liczba tokenów wejściowych
- Liczba tokenów wyjściowych
- Liczba tokenów w pamięci podręcznej
- Czas przechowywania tokena w pamięci podręcznej

Informacje o cenach znajdziesz na [stronie z cennikiem](https://ai.google.dev/pricing?hl=pl).

### Gdzie mogę sprawdzić swój limit?

Limity przydziału i limity systemu możesz sprawdzić w [AI Studio](https://aistudio.google.com/usage?hl=pl).

### Jak przejść na wyższy poziom limitu szybkości lub poprosić o większy limit?

Gdy Twoje konto spełni [wymagania kolejnego poziomu](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl#usage-tiers), automatycznie otrzymasz większy limit.

### Czy mogę korzystać z Gemini API bezpłatnie w Europejskim Obszarze Gospodarczym (w tym w UE), Wielkiej Brytanii i Szwajcarii?

Tak, bezpłatna i płatna wersja są dostępne w [wielu regionach](https://ai.google.dev/gemini-api/docs/available-regions?hl=pl).

### Czy jeśli skonfiguruję rozliczenia za Gemini API, będę obciążany opłatami za korzystanie z Google AI Studio?

Korzystanie z AI Studio pozostaje bezpłatne, chyba że użytkownicy połączą płatny klucz interfejsu API, aby uzyskać dostęp do płatnych funkcji.
Gdy połączysz płatny klucz API w ramach płatnego projektu w AI Studio, będziemy naliczać opłaty za korzystanie z AI Studio w przypadku tego klucza. W razie potrzeby możesz przełączać się między projektami w ramach płatnej wersji a projektami w ramach poziomu bezpłatnego, używając odpowiednich kluczy interfejsu API powiązanych z każdym typem.

### Jeśli korzystam z poziomu bezpłatnego, jak mogę przejść na wyższe poziomy?

Aby uzyskać dostęp do wyższych poziomów, musisz skonfigurować rozliczenia w projekcie. W Google AI Studio kliknij [**Skonfiguruj rozliczenia**](#setup-billing). Przeprowadzimy Cię przez proces wybierania lub tworzenia konta rozliczeniowego Cloud. Jeśli musisz korzystać z modelu rozliczeń przedpłaconych, proces **Skonfiguruj rozliczenia** przeprowadzi Cię przez proces tworzenia konta przedpłaconego połączonego z kontem rozliczeniowym Cloud.

### Czy w ramach poziomu bezpłatnego mogę używać 1 miliona tokenów?

Bezpłatny poziom Gemini API różni się w zależności od wybranego modelu. Obecnie możesz wypróbować okno kontekstu z milionem tokenów w ten sposób:

- W Google AI Studio
- W przypadku wybranych modeli dostępne są bezpłatne plany.
- Abonamenty płatne po wykonaniu usługi

### Czy po przejściu na wyższy (płatny) poziom mogę wrócić do poziomu bezpłatnego?

Aby przejść na poziom bezpłatny, możesz [wyłączyć płatności](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=pl#disable_billing_for_a_project) w każdym projekcie, w którym chcesz to zrobić.

### Jak mogę obliczyć liczbę używanych tokenów?

Użyj metody [`GenerativeModel.count_tokens`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=pl#count_tokens), aby zliczyć liczbę tokenów. Więcej informacji o tokenach znajdziesz w [przewodniku po tokenach](https://ai.google.dev/gemini-api/docs/tokens?hl=pl).

### Czy jeśli zarejestruję pierwsze konto rozliczeniowe Cloud w AI Studio, nadal będę mieć dostęp do bezpłatnego okresu próbnego Google Cloud?

Gdy zarejestrujesz pierwsze konto rozliczeniowe Cloud, rozpocznie się [bezpłatny okres próbny Google Cloud](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=pl#free-trial) i otrzymasz [środki powitalne](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=pl#welcome-credits) w wysokości 300 USD. Nie możesz jednak używać tych środków do płacenia za korzystanie z AI Studio. Możesz ich używać do płacenia za inne kwalifikujące się usługi w Google Cloud (pamiętaj, że gdy te środki zostaną wykorzystane lub wygasną (w ciągu 90 dni), wszelkie dodatkowe koszty użytkowania zostaną automatycznie obciążone wybranym przez Ciebie środkiem płatności).

### Czy mogę wykorzystać środki na powitanie w Google Cloud w przypadku Gemini API?

Nie, [środków na powitanie](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=pl#welcome-credits) ani środków z bezpłatnego okresu próbnego Google Cloud nie można wykorzystać na Gemini API ani AI Studio.

Jeśli środki na powitanie w Google Cloud zostały przyznane przed utratą uprawnień, możesz wykorzystać pozostałe środki na Gemini API i AI Studio do momentu ich wygaśnięcia (po 90 dniach).

### Czy bezpłatny okres próbny Google Cloud obejmuje korzystanie z Gemini API?

Nie. Od marca 2026 r. koszty korzystania z Gemini API są wyraźnie wyłączone z programu [bezpłatnego okresu próbnego Google Cloud o wartości 300 USD](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=pl#free-trial).

### Jak działają środki w Google Cloud w przypadku przedpłaty?

Użytkownicy korzystający z płatności z góry muszą najpierw [kupić środki przedpłacone](#buy-credits), zanim będzie można zastosować kwalifikujące się środki Google Cloud do korzystania z Gemini API. Gdy będziesz mieć aktywne saldo środków przedpłaconych, środki Google Cloud, które kwalifikują się do Gemini API, będą wykorzystywane przed saldem środków przedpłaconych. Gdy saldo środków przedpłaconych na koncie rozliczeniowym osiągnie 0 USD, środki Google Cloud nie będą już wykorzystywane.

Nie wszystkie środki Google Cloud, takie jak [środki na powitanie w Google Cloud](#cloud-credits), można wykorzystać w Gemini API i AI Studio.

### Jak przebiegają procesy płatności?

Rozliczenia za Gemini API są obsługiwane przez system [rozliczeń Cloud](https://cloud.google.com/billing/docs/concepts?hl=pl). Więcej informacji o konfiguracji płatności w usłudze Rozliczenia usługi Google Cloud znajdziesz w [dokumentacji Rozliczeń usługi Google Cloud](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=pl).

### Czy pobierana jest opłata za nieudane żądania?

Jeśli Twoje żądanie zakończy się niepowodzeniem i zostanie zwrócony błąd 400 lub 500, nie obciążymy Cię opłatą za użyte tokeny. Prośba będzie jednak nadal wliczać się do limitu.

### Czy za `GetTokens` naliczono opłatę?

Żądania do interfejsu `GetTokens` API nie są rozliczane i nie są wliczane do limitu wnioskowania.

### Jak są obsługiwane moje dane w Google AI Studio, jeśli mam płatne konto API?

Szczegółowe informacje o tym, jak są przetwarzane dane, gdy włączone jest rozliczanie w Cloud, znajdziesz w [Warunkach korzystania z usługi](https://ai.google.dev/gemini-api/terms?hl=pl#paid-services) (sekcja „Jak Google wykorzystuje Twoje dane” w części „Usługi płatne”). Pamiętaj, że Twoje prompty w Google AI Studio są traktowane zgodnie z warunkami „Usług płatnych”, o ile co najmniej 1 projekt interfejsu API ma włączone rozliczenia. Możesz to sprawdzić na [stronie klucza Gemini API](https://aistudio.google.com/api-keys?hl=pl), jeśli w sekcji „Plan” widzisz projekty oznaczone jako „Płatne”.

### Co to jest płatność z góry i kto musi korzystać z tego modelu płatności?

Płatności z przedpłatą umożliwiają użytkownikom Gemini API w AI Studio zakupienie środków z wyprzedzeniem.
Od 23 marca 2026 roku nowi użytkownicy AI Studio mogą być zobowiązani do korzystania z abonamentu przedpłaconego. Podczas procesu [konfigurowania płatności](#setup-billing) w AI Studio interfejs użytkownika poprowadzi Cię przez proces konfiguracji płatności i wskaże, czy musisz dokonać przedpłaty.

### Jak kupić środki przedpłacone i czy obowiązuje minimalna lub maksymalna kwota?

[Środki możesz kupić](#buy-credits) na stronie Rozliczenia AI Studio. Podczas procesu zakupu interfejs użytkownika wyświetli minimalną kwotę przedpłaty wymaganą w Twoim regionie i na Twoim poziomie, a także maksymalną kwotę, która może znajdować się na Twoim koncie w danym momencie.

### Czy mogę skonfigurować konto przedpłacone tak, aby w razie potrzeby automatycznie kupować więcej środków?

Tak, zalecamy skonfigurowanie [automatycznego doładowania](#auto-reload) w ustawieniach płatności AI Studio. Określasz „wyzwalacz” salda środków (np. „gdy saldo spadnie poniżej 30 zł”) i „wartość doładowania” (np. „dodaj 100 zł”).

### Czy mogę ograniczyć liczbę automatycznych doładowań?

Tak. Użytkownicy korzystający z płatności z góry mogą ustawić [miesięczny limit automatycznych obciążeń](#monthly-auto-charge-limit) w widżecie **Automatyczne doładowanie**. Gdy łączna kwota automatycznych doładowań w cyklu rozliczeniowym osiągnie ten limit, system wyłączy automatyczne doładowanie do następnego miesiąca. Zakupy ręczne nie wliczają się do tego limitu.

### Czy mogę otrzymać zwrot środków za niewykorzystane środki?

Wszystkie środki na koncie przedpłaconym API wygasają po roku i nie podlegają zwrotowi. Zapoznaj się z [zasadami zwrotów dotyczącymi kont przedpłaconych](#refunds).

### Czy środki przedpłacone mają termin ważności?

Tak, środki wygasają po 12 miesiącach od daty zakupu.

### Co się stanie, gdy saldo środków przedpłaconych osiągnie 0 PLN?

Wszystkie usługi Gemini API we wszystkich projektach opłacanych z tego konta przedpłaty Rozliczeń usługi Google Cloud zostaną natychmiast zatrzymane, aby zapobiec naliczaniu kolejnych opłat. Projekty nie są automatycznie przenoszone na niższy poziom bezpłatny.

Aby przywrócić usługę na obecnym poziomie płatnym, musisz [kupić dodatkowe środki](#buy-credits). Po zakupieniu środków powinna być możliwość korzystania z Gemini API. Pamiętaj, że aktualizacja salda środków w naszych systemach może nastąpić z [opóźnieniem](#processing-times).

Opcjonalnie, aby przejść na poziom bezpłatny, możesz [wyłączyć płatności](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=pl#disable_billing_for_a_project) w projektach, w których chcesz to zrobić.

### Dlaczego moje wykorzystanie zostało zatrzymane, mimo że saldo kredytu przedpłaconego jest większe niż 0 PLN?

Możliwe, że osiągnięto [limit wykorzystania](#tier-spend-caps) w przypadku obecnego poziomu.
Limity wykorzystania będą automatycznie zwiększane w miarę przechodzenia na wyższe poziomy. Na korzystanie z Gemini API w Google AI Studio może też wpływać [stan Twojego konta rozliczeniowego Cloud](#missed-payment).

### Dlaczego saldo konta przedpłaconego jest ujemne?

Ze względu na złożoność naszych systemów rozliczeniowych i przetwarzania mogą wystąpić [opóźnienia](#processing-times) w odcięciu dostępu do usługi po wykorzystaniu wszystkich środków. Wykorzystanie przekraczające limit może być widoczne na panelu płatności AI Studio jako ujemne saldo środków. W takim przypadku usługa zostanie wstrzymana, a ujemne saldo zostanie odjęte od następnego zakupu środków.

Aby uniknąć wstrzymania usługi Gemini API, zalecamy skonfigurowanie [automatycznego doładowania](#auto-reload), które będzie automatycznie kupować więcej środków, gdy saldo spadnie poniżej określonej przez Ciebie wartości.

### Czy mogę wykorzystać środki przedpłacone na inne usługi Google Cloud, takie jak Gemini Enterprise Agent Platform?

Nie. Środki z przedpłaty są przeznaczone wyłącznie na korzystanie z Gemini API. Wszystkie inne usługi Google Cloud, z których korzystasz (Compute, Storage, Gemini Enterprise Agent Platform), są rozliczane zgodnie ze standardowym [cyklem rozliczeniowym Cloud](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=pl).

### Czy mogę przejść na abonament z płatnościami po wykonaniu usługi?

Gdy uzyskasz historię płatności i [osiągniesz poziom uprawniający](#about-billing) do korzystania z abonamentu z płatnością po zakończeniu okresu rozliczeniowego, możesz opcjonalnie przenieść wszystkie przyszłe koszty korzystania z interfejsu Gemini API na standardowy, skonsolidowany [cykl rozliczeniowy z płatnością po zakończeniu okresu rozliczeniowego](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=pl#view-your-charging-cycle) w Google Cloud.

### Co się stanie z moimi środkami przedpłaconymi, jeśli przejdę na płatność z dołu?

Gdy przejdziesz na [płatność po wykonaniu usługi](#postpay), Rozliczenia usługi Google Cloud zamkną Twoje konto płatności przed faktem, wyłączą [automatyczne doładowanie](#auto-reload) i automatycznie zwrócą Ci niewykorzystane środki przedpłacone (zgodnie ze standardowym czasem przetwarzania zwrotu środków).

### Gdzie mogę sprawdzić aktualne saldo środków przedpłaconych i historię transakcji?

Wszystkie czynności związane z zarządzaniem saldem i historią transakcji w przypadku Gemini API muszą być wykonywane bezpośrednio na karcie Płatności w Google AI Studio.

### Dlaczego widzę komunikat „Typ konta rozliczeniowego jest nieaktywny lub nieobsługiwany”?

Interakcje związane z płatnościami na [stronie Płatności w AI Studio](https://aistudio.google.com/billing?hl=pl) mogą być blokowane i zastępowane komunikatem „Typ konta rozliczeniowego jest nieaktywny lub nieobsługiwany”, jeśli wybrany typ konta rozliczeniowego lub stan konta rozliczeniowego nie kwalifikuje się do płatnej wersji AI Studio.

Sprawdź stan konta rozliczeniowego w [Cloud Console](https://console.cloud.google.com/billing/?hl=pl). Jednym z rodzajów konta, które nie kwalifikuje się do programu, może być *konto w bezpłatnej wersji próbnej*. W takim przypadku możesz [aktywować płatności](#setup-billing) w AI Studio, aby spełnić wymagania. Jednym ze stanów nieaktywnych może być *Zamknięte*. W takim przypadku możesz [ponownie otworzyć konto](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=pl).

### Czy koszty korzystania z Gemini API będą widoczne w konsoli Google Cloud?

Tak. Koszty interfejsu Gemini API oraz koszty związane z innymi usługami Google Cloud, za które płacisz z konta rozliczeniowego Cloud, możesz wyświetlić na [stronach zarządzania kosztami](https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle?hl=pl#cost-reports) w [konsoli Rozliczeń usługi Google Cloud](https://console.cloud.google.com/billing?hl=pl). Pamiętaj, że saldem kredytu z przedpłaty możesz zarządzać tylko w AI Studio.

### Dlaczego w konsoli Rozliczenia usługi Google Cloud nie widzę wykorzystania Gemini API, mimo że widzę je w sekcji Rozliczenia w AI Studio wraz z wykorzystaniem środków?

Usługi Google Cloud i AI Studio zgłaszają dane o wykorzystaniu do rozliczeń usługi Google Cloud w różnych odstępach czasu. Ze względu na złożoność naszych systemów rozliczeniowych i przetwarzania danych może wystąpić opóźnienie między użyciem usług a dostępnością informacji o wykorzystaniu i kosztach w Rozliczeniach usługi Google Cloud. Zwykle szczegóły kosztów są dostępne w ciągu 1 dnia, ale czasem trwa to dłużej niż 24 godziny.
Więcej informacji o opóźnionych płatnościach znajdziesz w [dokumentacji Rozliczeń usługi Google Cloud](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=pl#delayed-billing).

### Jeśli korzystam z innych usług Google Cloud, których koszty podlegają cyklowi rozliczeniowemu po zakończeniu okresu rozliczeniowego, co się stanie, jeśli nie dokonam płatności?

Brak płatności za inne usługi Google Cloud może spowodować zawieszenie dostępu do Gemini API w AI Studio, **niezależnie od liczby dostępnych środków z przedpłaty**. Korzystanie z AI Studio jest możliwe dzięki kontu rozliczeniowemu Google Cloud, które może być używane zarówno do rozliczeń przedpłaconych za AI Studio, jak i do rozliczeń popłaconych za inne usługi Cloud. Problem z saldem Postpay wstrzymuje wszystkie usługi powiązane z tym kontem. Korzystanie z Gemini API zostanie zawieszone, jeśli na Twoim koncie rozliczeniowym Cloud zostaną wykryte problemy, takie jak:

- zaległe należności,
- odrzuconą płatność,
- nieprawidłowa lub nieważna forma płatności;

Aby przywrócić usługę, musisz [rozwiązać problem z kontem z płatnościami po wykonaniu usługi](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=pl#resolving-declined-payments) w konsoli Rozliczenia usługi Google Cloud. Po rozwiązaniu problemu odzyskasz dostęp do środków przedpłaconych Gemini API i usług.

### Gdzie mogę uzyskać pomoc dotyczącą płatności?

Aby uzyskać pomoc dotyczącą płatności, przeczytaj artykuł [Uzyskiwanie pomocy dotyczącej płatności za Google Cloud](https://cloud.google.com/support/billing?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-10 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-10 UTC."],[],[]]
