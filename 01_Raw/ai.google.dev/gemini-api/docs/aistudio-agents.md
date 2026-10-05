---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=pl
fetched_at: 2026-10-05T06:27:28.704798+00:00
title: "Agenty na placu zabaw AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Agenty na placu zabaw AI Studio

Plac zabaw Google AI Studio udostępnia wizualny interfejs do tworzenia prototypów i uczenia się, jak tworzyć zarządzanych agentów bez konieczności tworzenia i pisania wywołań interfejsu API.

Aby rozpocząć, w panelu nawigacyjnym Google AI Studio otwórz kartę **Playground** i przesuń przełącznik na **Agenci**.

## Gotowe szablony

Na karcie **Agenci** znajduje się szereg szablonów, które wstępnie konfigurują podstawowego agenta Antigravity, ustawiając konfiguracje narzędzi i środowiska. Wszystkie szablony są dostępne na licencji open source i opublikowane w repozytorium [google-gemini/gemini-managed-agents-templates](https://github.com/google-gemini/gemini-managed-agents-templates/). Zapoznanie się z tymi szablonami to świetny sposób na nauczenie się, jak tworzyć własnego agenta zarządzanego i jak go strukturyzować.

Na przykład po wybraniu szablonu AI Radio włączone zostaną wszystkie dozwolone narzędzia i połączone specjalistyczne `AGENTS.md` pliki i umiejętności do produkcji audycji radiowych. Te ustawienia możesz wyświetlić w interfejsie Playground w sekcji **Środowisko**, klikając przycisk **Źródła**.

## Konfiguracja narzędzia

W ustawieniach agenta w Playground możesz włączyć lub wyłączyć dostęp do tych wbudowanych narzędzi:

- **Wyszukiwarka Google:** dostęp do otwartego internetu w celu uzyskania informacji w czasie rzeczywistym.
- **Kontekst adresu URL:** pobieranie i analizowanie treści tekstowych z określonych adresów URL stron internetowych.
- **Wykonywanie kodu:** uruchamiaj polecenia Bash i Python bezpośrednio w izolowanym środowisku piaskownicy.
- **Narzędzia systemu plików:** odczytywanie, zapisywanie, wyświetlanie listy i usuwanie plików w obszarze roboczym.

## Konfiguracja środowiska

Zarządzane agenty działają w bezpiecznej, tymczasowej piaskownicy Linuksa (środowisku), która zapewnia im przestrzeń roboczą i narzędzia potrzebne do działania. Więcej informacji znajdziesz w przewodniku po [zarządzanym środowisku agenta](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl).

### Kontrolowanie zachowania agenta

Zachowanie, osobowość i możliwości agenta są w głównej mierze określone przez pliki znajdujące się w jego środowisku. Agent automatycznie wykrywa i wczytuje konfiguracje ze specjalnego folderu `.agents`:

- **`AGENTS.md`**: wstępnie załadowane do kontekstu agenta w celu zdefiniowania instrukcji systemowych i profilu.
- **`SKILL.md`**: znajdują się w odpowiednich folderach umiejętności (np. `.agents/skills/my-skill/SKILL.md`) i służą do definiowania konkretnych funkcji i przepływów pracy.

### Provisioning the Environment

Środowisko, z którego będzie korzystać agent, możesz skonfigurować, montując w nim pliki przed rozpoczęciem sesji. Możesz utworzyć nowe środowisko, montując źródła, lub przywrócić poprzednie:

- **Aby utworzyć nowe środowisko**, w panelu Ustawienia środowiska kliknij **Dodaj źródła** i wybierz jeden z tych typów źródeł:

| Typ źródła | Opis | Ścieżka montażu |
| --- | --- | --- |
| **Pliki w treści** | Pisz lub wklejaj pliki konfiguracyjne, przykładowe zbiory danych lub skrypty narzędziowe (do 100 KB) bezpośrednio w interfejsie Playground. | Ścieżka docelowa zdefiniowana przez użytkownika (np. `/workspace/scripts/parser.py`). |
| **Google Cloud Storage** | Zamontuj publiczny lub prywatny zasobnik Cloud Storage.  Prywatne zasobniki wymagają standardowego tokena okaziciela OAuth 2.0. Więcej informacji znajdziesz w sekcji [Źródła prywatne](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl#private-sources). | Mapuje ścieżkę zasobnika GCS (np. `gs://your-bucket-name/data/`) na katalog obszaru roboczego (np. `/workspace/data/`). |
| **Repozytoria GitHub** | Klonuj publiczne i prywatne bazy kodu.  Prywatne repozytoria wymagają uwierzytelniania podstawowego za pomocą osobistego tokena dostępu (PAT) GitHub. Więcej informacji znajdziesz w sekcji [Źródła prywatne](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl#private-sources). | Sklonowane bezpośrednio do `/workspace/` (zwykle w ciągu `/workspace/<repo-name>`). |

- **Aby przywrócić poprzednie środowisko**, możesz [użyć istniejącego identyfikatora środowiska](#reusing-an-existing-environment-id), aby sklonować i rozwidlić jego dokładny stan.

### Ponowne użycie istniejącego identyfikatora środowiska

Jeśli masz już skonfigurowane środowisko piaskownicy, nie musisz zaczynać od zera. Aby użyć istniejącego środowiska:

1. Otwórz panel Środowiska w AI Studio i przełącz **Typ** na **Istniejące**.
2. Wpisz **identyfikator środowiska** (np.`env_abc123`).

Więcej informacji znajdziesz w artykule [Konfigurowanie środowiska](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl#configure-an-environment). Identyfikator środowiska bieżącej sesji możesz też pobrać z karty Środowisko w interfejsie.

Gdy wyślesz pierwszą wiadomość do agenta, konfiguracja środowiska zostanie ustalona na potrzeby tej sesji. Nie możesz montować nowych źródeł ani modyfikować listy dozwolonych sieci, gdy interakcja jest aktywna.

## Pobieranie środowiska

Po utworzeniu środowiska możesz w dowolnym momencie pobrać jego zrzut, klikając przycisk **Pobierz** w ustawieniach środowiska na platformie AI Studio Playground, aby pobrać pliki środowiska jako plik tar.

## Bezpieczeństwo i zarządzanie kosztami

### Zarządzanie wykorzystaniem tokenów

W odróżnieniu od standardowej prośby o czat, która generuje pojedyncze dane wyjściowe, Antigravity Agent wykonuje autonomiczny przepływ pracy. Planuje, uruchamia kod, obserwuje wyniki i powtarza proces. Oznacza to, że jeden prompt może spowodować nieograniczone zużycie tokenów.

Aby zarządzać kosztami, **podaj w promptach jasne kryteria zakończenia i zawęź zakres zadań agenta**. Dobrym przykładem może być prompt:*Sprawdź żądanie pull i zatrzymaj się po wygenerowaniu podsumowania w formacie Markdown.
Nie próbuj samodzielnie pisać poprawki*.

### Dodatkowe koszty

Domyślnie wszystkie szablony agentów w Playground mają dostęp do usługi Gemini API i mogą wykonywać wywołania interfejsu API ze środowiska, aby realizować żądania. Mogą się one wiązać z dodatkowymi kosztami, które nie będą odzwierciedlone w zużyciu tokenów.

Podobnie, jeśli dodasz inne usługi zewnętrzne, agent może ponieść dodatkowe koszty, wywołując te usługi w Twoim imieniu.

### Lista dozwolonych sieci

Domyślnie w AI Studio wszystkie wychodzące żądania sieciowe z piaskownicy Twojego agenta są ściśle kontrolowane i ograniczone, aby zapewnić bezpieczeństwo. Aby przyznać agentowi możliwość korzystania z zewnętrznych interfejsów API, usług internetowych lub menedżerów pakietów, musisz je wyraźnie zadeklarować:

1. Otwórz panel Środowiska w AI Studio.
2. Kliknij przycisk **reguły** obok opcji **Sieć**.
3. W panelu **Konfiguracja sieci** kliknij **Dodaj do listy dozwolonych** i wpisz odpowiednie informacje:
   - **Ograniczenie domeny:** maszyna wirtualna agenta może uzyskiwać dostęp tylko do określonych domen lub wzorców z symbolami wieloznacznymi dodanych do listy. Możesz na przykład wpisać dokładne domeny, takie jak `api.github.com`, lub ogólne wzorce, takie jak `*.googleapis.com`.
   - **Dodawanie nagłówka HTTP i wstrzykiwanie tokena:** użyj opcji **Dodaj nagłówek HTTP**, aby bezpiecznie wstrzyknąć wymagane dane logowania (np. token API) dla określonej domeny. Te dane logowania są bezpiecznie przekazywane przez serwer proxy ruchu wychodzącego i nigdy nie są bezpośrednio ujawniane w formie nieprzetworzonego tekstu w piaskownicy agenta.

Zawsze zachowuj ostrożność podczas dodawania domen do listy dozwolonych. Przyznanie agentowi dostępu do uwierzytelnionych usług oznacza, że może on działać w Twoim imieniu, co w przypadku braku starannego monitorowania może prowadzić do niezamierzonych działań.

### Sprawdzone metody dotyczące danych logowania

Jeśli Twój przepływ pracy wymaga uwierzytelniania agenta w usługach zewnętrznych, musisz udostępnić i określić zakres tych danych logowania. Aby zmniejszyć ryzyko, postępuj zgodnie z tymi wytycznymi:

- **Używaj danych logowania o jak najmniejszych uprawnieniach:** utwórz konta usługi lub klucze API
  z uprawnieniami, których potrzebuje Twój agent. Unikaj przekazywania danych logowania z szerokim lub administracyjnym dostępem.
- **Preferuj tokeny o krótkim czasie ważności:** w miarę możliwości używaj danych logowania lub tokenów o ograniczonym czasie ważności, które wygasają, zamiast kluczy API o długim czasie ważności.
- **Załóż pełny dostęp:** agent może używać dowolnych danych logowania, do których ma dostęp, aby wykonać zadanie, które mu zlecisz. Podawaj tylko dane logowania, w przypadku których chcesz przyznać pełny zakres dostępu.
- **Regularnie wykonuj rotację danych logowania:** traktuj dane logowania udostępniane agentowi tak samo jak inne dane logowania zautomatyzowane. Wykonuj ich rotację zgodnie z regularnym harmonogramem.

### Łączenie narzędzi zewnętrznych i interfejsów API

Możesz połączyć narzędzia zewnętrzne i interfejsy API (np. serwery Model Context Protocol / MCP), aby rozszerzyć możliwości agenta. Pamiętaj, aby:

- Łącz tylko narzędzia pochodzące z zaufanych źródeł. Złośliwe lub źle napisane narzędzie może ujawniać dane lub wykonywać niezamierzone działania.
- Skonfiguruj narzędzia z minimalnymi uprawnieniami wymaganymi w Twoim przypadku. Jeśli narzędzie obsługuje tryb tylko do odczytu, używaj go, chyba że zapisywanie jest bezwzględnie konieczne.
- Zanim połączysz narzędzie ze źródłem danych produkcyjnych, przetestuj je na przykładowych lub syntetycznych danych, aby sprawdzić, czy agent używa go zgodnie z oczekiwaniami.

### Nadzór ze strony człowieka

Agenty mogą rozumować, planować i wykonywać wieloetapowe przepływy pracy z dużą autonomią. Jest to bardzo przydatne, ale oznacza też, że należy sprawować odpowiedni nadzór, zwłaszcza w przypadku zadań, które modyfikują dane lub wchodzą w interakcje z systemami zewnętrznymi.

Przed wdrożeniem zawsze sprawdzaj krytyczne dane wyjściowe, takie jak wygenerowany kod, transformacje danych czy zmiany konfiguracji.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-08-19 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-08-19 UTC."],[],[]]
