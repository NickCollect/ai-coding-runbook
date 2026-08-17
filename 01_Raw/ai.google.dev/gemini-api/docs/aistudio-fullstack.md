---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=pl
fetched_at: 2026-08-17T02:23:54.001985+00:00
title: "Tworzenie aplikacji pe\u0142nostosowych w\u00a0Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Tworzenie aplikacji pełnostosowych w Google AI Studio

Google AI Studio obsługuje teraz tworzenie aplikacji w pełnym stosie technologicznym, co umożliwia tworzenie aplikacji, które wykraczają poza prototypy po stronie klienta. Dzięki środowisku wykonawczemu po stronie serwera możesz zarządzać obiektami tajnymi, łączyć się z zewnętrznymi interfejsami API i tworzyć aplikacje wieloosobowe działające w czasie rzeczywistym.

## Środowisko wykonawcze po stronie serwera

Aplikacje Google AI Studio mogą teraz zawierać komponent po stronie serwera (Node.js).
Ma to następujące zalety:

- **Wykonywanie logiki po stronie serwera**: uruchamiaj kod, który nie powinien być widoczny dla
  klienta.
- **Dostęp do pakietów npm**: [Antigravity Agent](https://antigravity.google/docs/agent?hl=pl)
  może instalować i używać pakietów z rozbudowanego ekosystemu npm.
- **Obsługa obiektów tajnych**: bezpieczne używanie kluczy interfejsu API i danych logowania.

### Korzystanie z pakietów npm

Nie musisz ręcznie uruchamiać polecenia `npm install`. Po prostu poproś Agenta o dodanie funkcji, która wymaga pakietu, a on zajmie się instalacją i importem.

**Przykład**: > "Użyj `axios`, aby pobrać dane z zewnętrznego interfejsu API."

## Bezpieczne zarządzanie obiektami tajnymi

Dzięki kodowi po stronie serwera i zarządzaniu obiektami tajnymi możesz teraz tworzyć aplikacje, które wchodzą w interakcje ze światem.

### Klucz interfejsu Gemini API

Gdy tworzysz nową aplikację, która korzysta z Gemini API, AI Studio automatycznie konfiguruje Twój `GEMINI_API_KEY` jako obiekt tajny po stronie serwera – nie musisz niczego konfigurować ręcznie. Ten klucz możesz wyświetlić w panelu **Obiekty tajne** w Ustawieniach. Wywołania Gemini API w Twojej aplikacji są wykonywane z kodu po stronie serwera przy użyciu tego klucza, więc nigdy nie jest on widoczny w przeglądarce.

### Klucze interfejsów API innych firm

W przypadku innych usług możesz ręcznie dodać klucze interfejsu API:

- **Interfejsy API innych firm**: łącz się z usługami takimi jak Stripe, SendGrid czy niestandardowe
  interfejsy REST API.
- **Bazy danych**: łącz się z zewnętrznymi bazami danych (np. za pomocą Supabase, Firebase, lub MongoDB Atlas), aby przechowywać dane poza sesją.

Podczas tworzenia aplikacji w rzeczywistych warunkach często trzeba łączyć się z usługami innych firm (takimi jak Twilio, Slack czy bazy danych), które wymagają kluczy interfejsu API. Klucze możesz dodać ręcznie, wykonując te czynności:

1. **Dodaj obiekt tajny**: w Google AI Studio otwórz menu **Ustawienia** i znajdź
   sekcję Obiekty tajne.
2. **Przechowuj klucz**: dodaj tutaj klucze interfejsu API lub tajne tokeny.
3. **Dostęp w kodzie**: Agent może napisać kod po stronie serwera, który bezpiecznie uzyskuje dostęp do tych
   obiektów tajnych (zwykle za pomocą zmiennych środowiskowych), dzięki czemu nigdy nie są one
   widoczne w przeglądarce po stronie klienta.

W razie potrzeby Agent wyświetli też w czacie kartę z prośbą o dodanie kluczy, gdy będzie potrzebny nowy obiekt tajny lub gdy w zmiennych środowiskowych projektu zostanie wykryty nowy klucz.

### Integracja z Firebase na potrzeby bazy danych i uwierzytelniania

Google AI Studio ułatwia teraz dodawanie bazy danych lub uwierzytelniania do Twojej
aplikacji dzięki
[integracji z Firebase](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=pl).
Antigravity Agent może automatycznie udostępniać i konfigurować te usługi:

- **Baza danych Firestore**: elastyczna i skalowalna baza danych NoSQL w chmurze, która służy do przechowywania
  i synchronizowania danych na potrzeby programowania po stronie klienta i serwera.
- **Uwierzytelnianie Firebase**: umożliwia użytkownikom bezpieczne logowanie się w
  aplikacji za pomocą przepływów „Zaloguj się przez Google”.

Po prostu poproś Agenta o „dodanie bazy danych do mojej aplikacji” lub „skonfigurowanie logowania przez Google”, a on zajmie się niezbędną konfiguracją i wygenerowaniem kodu.

Firebase umożliwia bezpłatne rozpoczęcie pracy i opcjonalne skalowanie za pomocą płatnego konta, gdy będziesz potrzebować większego limitu lub chcesz korzystać z płatnych funkcji.

## Interfejsy Google Workspace API

Google AI Studio umożliwia tworzenie aplikacji, które łączą się z interfejsami Google Workspace API, dzięki czemu użytkownicy mogą pracować z rzeczywistymi danymi: e-mailami, arkuszami kalkulacyjnymi, dokumentami, wydarzeniami w kalendarzu i innymi danymi – wszystko w Twojej aplikacji. Nie musisz już konfigurować projektu w chmurze Google, konfigurować protokołu OAuth ani ręcznie zarządzać interfejsem API.

### Jak to działa

Integrację z Workspace możesz dodać na 2 sposoby:

- **Opisz ją w panelu czatu**: po prostu powiedz Agentowi, czego chcesz, w panelu czatu u dołu. Na przykład *„Utwórz narzędzie do śledzenia wydatków, które rejestruje paragony w moim Arkuszu Google”* lub *„Utwórz panel, który podsumowuje moje nieprzeczytane wiadomości w Gmailu”*
- **Wybierz w panelu integracji**: w prawym pasku bocznym trybu tworzenia otwórz panel **Integracje** i włącz aplikację Google Workspace, z którą chcesz się połączyć.

Gdy dodasz aplikację Google Workspace, AI Studio automatycznie:

1. łączy niezbędny interfejs Google API z Twoją aplikacją,
2. generuje kod po stronie serwera do wywoływania interfejsu API,
3. dodaje bezpieczny przepływ „Zaloguj się przez Google”, aby użytkownicy Twojej aplikacji mogli autoryzować dostęp do swoich danych.

### Obsługiwane aplikacje

Dostępne są te aplikacje Google Workspace:

| Aplikacja | Co możesz utworzyć |
| --- | --- |
| Kalendarz Google | Odczytywanie, tworzenie i zarządzanie wydarzeniami oraz kalendarzami |
| Google Chat | Odczytywanie rozmów i pokoi grupowych oraz wchodzenie z nimi w interakcje |
| Dokumenty Google | Tworzenie, odczytywanie, aktualizowanie i formatowanie dokumentów |
| Dysk Google | Porządkowanie, wyszukiwanie i zarządzanie plikami oraz folderami |
| Formularze Google | Tworzenie ankiet, aktualizowanie pytań i pobieranie odpowiedzi |
| Gmail | Odczytywanie, wysyłanie i zarządzanie treścią e-maili |
| Google Keep | Zarządzanie notatkami, listami i załącznikami |
| Google Meet | Planowanie rozmów wideo i zarządzanie nimi |
| Kontakty | Synchronizowanie kontaktów i zarządzanie nimi |
| Arkusze Google | Odczytywanie, zapisywanie i formatowanie danych arkusza kalkulacyjnego |
| Prezentacje Google | Tworzenie i modyfikowanie prezentacji |
| Lista zadań Google | Tworzenie zadań, zarządzanie nimi i porządkowanie ich |

### Uwierzytelnianie i uprawnienia

Jako twórca nie musisz konfigurować klientów OAuth, zarządzać danymi logowania ani konfigurować projektu w chmurze Google. AI Studio zajmie się tym za Ciebie.

Aplikacje zintegrowane z interfejsami Workspace API używają do uwierzytelniania użytkowników funkcji „Zaloguj się przez Google”. Gdy użytkownik otworzy Twoją aplikację, zostanie poproszony o zalogowanie się i przyznanie jej określonych uprawnień (np. dostępu do kalendarza tylko do odczytu lub możliwości edytowania arkusza kalkulacyjnego). Twoja aplikacja ma dostęp tylko do danych osoby, która jej używa. Każdy użytkownik autoryzuje dostęp do swojego konta.

### Przykładowe prompty

Oto kilka pomysłów na rozpoczęcie pracy z integracjami Workspace:

- *„Utwórz aplikację, która odczytuje mój Kalendarz Google i tworzy wersje robocze e-maili przygotowujących w
  Gmailu na każde spotkanie”*.
- *„Utwórz narzędzie, które pobiera Dokument Google i generuje 5-slajdową prezentację podsumowującą
  w Prezentacjach Google”*.
- *„Utwórz narzędzie do śledzenia wydatków, w którym mogę przesłać paragon, Gemini wyodrębni
  szczegóły, a narzędzie zapisze nowy wiersz w moim Arkuszu Google”*

### Skonfiguruj OAuth

Jednym z kluczowych przypadków użycia zarządzania obiektami tajnymi jest skonfigurowanie OAuth w celu połączenia się z innymi witrynami lub aplikacjami. Jeśli Twój prompt zawiera instrukcje dotyczące łączenia się z aplikacją innej firmy, która wymaga uwierzytelniania OAuth, Agent poda instrukcje dotyczące konfigurowania OAuth dla tej aplikacji. Te instrukcje będą zawierać niezbędne adresy URL wywołania zwrotnego do skonfigurowania aplikacji OAuth.
Adresy URL wywołania zwrotnego znajdziesz też w sekcji **Integracje** w panelu Ustawienia.

## Tworzenie aplikacji wieloosobowych

Środowisko wykonawcze w pełnym stosie technologicznym umożliwia korzystanie z funkcji współpracy w czasie rzeczywistym.

- **Stan w czasie rzeczywistym**: możesz poprosić Agenta o utworzenie funkcji takich jak "czat na żywo
  ," "tablica do współpracy" czy "gra wieloosobowa."
- **Zsynchronizowane sesje**: serwer zarządza stanem, co umożliwia wielu użytkownikom
  interakcję z tą samą instancją aplikacji w czasie rzeczywistym.

**Przykładowy prompt**: > "Utwórz grę wieloosobową, w której gracze mogą widzieć
kursory innych graczy."

### Wskazówki dotyczące testowania aplikacji wieloosobowych

Przed wdrożeniem aplikacji możesz przetestować tryb wieloosobowy na 2 sposoby.

1. Otwórz aplikację w Google AI Studio w trybie tworzenia na kilku kartach. Podczas tworzenia w trybie tworzenia aplikacja znajduje się w kontenerze deweloperskim. Otwarcie aplikacji na kilku kartach pozwoli Ci symulować korzystanie z niej przez wielu graczy.
2. Udostępnij aplikację innym osobom, korzystając z menu **Udostępnij** w prawym górnym rogu. Następnie użyj **udostępnionego adresu URL** na karcie **Integracje** w menu **Udostępnij**, aby korzystać z aplikacji z graczami, którym ją udostępniłeś.

## Sprawdzone metody

- **Wywołania Gemini API**: Twój `GEMINI_API_KEY` jest automatycznie konfigurowany jako obiekt tajny po stronie serwera. Użyj tego klucza, aby wywoływać Gemini API z kodu po stronie serwera. Możesz go wyświetlić w panelu **Obiekty tajne**.
- **Bezpieczeństwo obiektów tajnych**: w przypadku kluczy zawierających dane wrażliwe zawsze używaj Menedżera obiektów tajnych.
  Nigdy nie koduj ich na stałe w plikach.
- **Rozdzielenie odpowiedzialności**: logikę interfejsu użytkownika umieść w frameworku po stronie klienta
  (React/Angular), a logikę biznesową i obsługę danych – po stronie serwera.
- **Obsługa błędów**: upewnij się, że kod po stronie serwera niezawodnie obsługuje błędy
  wywołań zewnętrznych interfejsów API, aby zapobiec awariom aplikacji.

## Co dalej?

- [Tworzenie aplikacji w Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=pl)
- [Wdrażanie z Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=pl)
- [Galeria aplikacji](https://aistudio.google.com/apps?source=showcase&hl=pl)

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-19 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-19 UTC."],[],[]]
