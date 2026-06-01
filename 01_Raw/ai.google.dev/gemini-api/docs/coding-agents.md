---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=pl
fetched_at: 2026-06-01T05:58:54.360300+00:00
title: "Konfigurowanie asystenta do kodowania za pomoc\u0105 Gemini MCP i\u00a0umiej\u0119tno\u015bci \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Konfigurowanie asystenta do kodowania za pomocą Gemini MCP i umiejętności

Asystenci kodowania AI są potężni, ale mają ograniczenia – dane treningowe są aktualne tylko do określonej daty, brakuje w nich nowych funkcji i zmian w interfejsie API. Bez dostępu do dokumentacji dotyczącej Gemini agenci mogą sugerować ogólne wzorce zamiast zoptymalizowanych rozwiązań.

Aby asystent kodowania był na bieżąco z rozwijającym się interfejsem Gemini API i jego zalecanym użyciem, zalecamy skonfigurowanie **MCP Gemini Docs** i rozszerzenie środowiska o **umiejętności Gemini API**. Chociaż te narzędzia można używać niezależnie, zostały one zaprojektowane tak, aby współpracować ze sobą i zapewniać pełne pokrycie.

## Łączenie MCP Gemini Docs

Gemini hostuje publiczny serwer Model Context Protocol (MCP) pod adresem `https://gemini-api-docs-mcp.dev`. Połączenie agenta kodowania z tym serwerem zapewnia, że wszystkie zapytania mają dostęp do najnowszych interfejsów API, aktualizacji kodu i optymalnych przykładów konfiguracji.

Aby zainstalować serwer, uruchom to polecenie w terminalu agenta lub w katalogu głównym projektu:

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

Ten serwer dodaje funkcję `search_documentation`, której agent może używać do pobierania definicji interfejsu API i wzorców integracji w czasie rzeczywistym z oficjalnych plików dokumentacji Gemini.

## Dodawanie umiejętności programowania interfejsu API

Umiejętności zapewniają **wbudowane reguły i sprawdzone metody** (np. wymuszanie prawidłowego pakietu SDK i bieżących wersji modelu) bezpośrednio w kontekście asystenta. Umiejętność współpracuje z usługą MCP Gemini Docs: jeśli masz zainstalowane obie te usługi, umiejętność używa usługi MCP do dokumentacji, ale nawet bez zainstalowanego MCP pobierze `llms.txt` z `ai.google.dev` jako rezerwę.

Aby zainstalować te umiejętności, możesz użyć jednego z tych obsługiwanych narzędzi. Instrukcje instalacji obu narzędzi znajdziesz poniżej każdego modułu umiejętności:

- **[skills.sh](https://skills.sh)**: zalecane. Otwarty standard przenośnych zachowań agenta.
- **[Context7](https://context7.com)**: obsługiwane w przypadku użytkowników, którzy już korzystają z ekosystemu Context7.

### gemini-api-dev

Podstawowa umiejętność do programowania Gemini do zwykłych obciążeń. Ta umiejętność zawiera dokumentację i sprawdzone metody dotyczące:

- przekierowywania promptów do bieżących modeli (np. Gemini 3.1 Pro/Flash) i unikania wycofanych modeli,
- tworzenie promptów multimodalnych, wywoływania funkcji, uporządkowanych danych wyjściowych i typowych wzorców integracji.

#### Instalacja za pomocą skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### Instalacja za pomocą Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

Umiejętność tworzenia aplikacji konwersacyjnej AI w czasie rzeczywistym za pomocą Gemini Live API. Ta umiejętność zawiera dokumentację i sprawdzone metody dotyczące:

- połączeń WebSocket do przesyłania strumieniowego z niskim opóźnieniem,
- przesyłania strumieniowego dźwięku, obrazu i tekstu,
- wykrywania aktywności głosowej i obsługi przerywania.

#### Instalacja za pomocą skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### Instalacja za pomocą Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

### gemini-interactions-api

Umiejętność tworzenia aplikacji za pomocą
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pl). Interactions API to ujednolicony interfejs do korzystania z modeli i agentów Gemini, zaprojektowany z myślą o aplikacjach agentowych. Ta umiejętność obejmuje:

- generowanie tekstu, czat wieloetapowy i przesyłanie strumieniowe,
- wywoływanie funkcji, uporządkowane dane wyjściowe i generowanie obrazów,
- wykonywanie w tle i agenci Deep Research,
- zarządzanie stanem rozmowy po stronie serwera,
- wzorce pakietu SDK w Pythonie i TypeScript.

#### Instalacja za pomocą skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
```

#### Instalacja za pomocą Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-interactions-api
```

## Zweryfikuj instalację

Po instalacji sprawdź, czy asystent kodowania może połączyć się z serwerem MCP Gemini Docs i korzystać z zainstalowanych umiejętności.

### 1. Sprawdź zachowanie agenta

Najbardziej niezawodnym sposobem sprawdzenia jest zadanie agentowi pytania technicznego dotyczącego Gemini API.

**Prompt:** „Jak używać buforowania kontekstu w Gemini API?”

Prawidłowa konfiguracja:

- **zapewnia dokładny kod**: odwołuje się do konkretnych metod Gemini, takich jak `cacheContent` lub `cachedContents.create`, z najnowszych punktów końcowych;
- **używa narzędzia MCP**: pokazuje, że jest połączona z **serwerem MCP Gemini Docs** lub używa narzędzia `search_documentation` do pobierania danych;
- **wywołuje załadowane umiejętności**: wyświetla wskaźnik „Using skill: gemini-api-dev” (jeśli korzysta z dodatkowej otoczki).

### 2. Sprawdź manifesty i narzędzia

Jeśli agent udzieli ogólnej odpowiedzi, użyj konkretnych poleceń Discovery lub Status dla swojego środowiska, aby sprawdzić, czy MCP lub umiejętność Docs są załadowane do pamięci.

| Środowisko | Weryfikacja MCP | Weryfikacja umiejętności |
| --- | --- | --- |
| **Claude Code** | Wpisz `/mcp` w terminalu, aby wyświetlić aktywne serwery i narzędzia `search_documentation`. | Wpisz `/skills` w terminalu, aby wyświetlić listę wszystkich aktywnych manifestów. |
| **Kursor** | Kliknij **Ustawienia > Funkcje > MCP**. Sprawdź, czy serwer jest „Połączony”. | Otwórz **Ustawienia > Reguły**. Sprawdź, czy umiejętność jest widoczna w sekcji „Agent Decides”. |
| **Antigravity** | Sprawdź stan MCP na pasku bocznym **Dostosowania > Połączenia**. | Wpisz `/skills list` lub sprawdź pasek boczny **Dostosowania > Reguły**. |
| **Interfejs wiersza poleceń Gemini** | Uruchom `gemini mcp list` lub użyj `/mcp list`. | Uruchom `gemini skills list` lub użyj polecenia po ukośniku `/skills` w sesji. |
| **Copilot** | Wpisz `@gemini /mcp`, aby wyświetlić listę aktywnych łączników danych. | Wpisz `@gemini /skills` (lub `/skills`), aby wyświetlić aktywne rozszerzenia. |

## Rozwiązywanie problemów

Jeśli agent podaje tylko ogólne informacje lub nie rozpoznaje metod specyficznych dla Gemini, sprawdź te kwestie:

### Agent nie wykrył umiejętności

Większość agentów indeksuje umiejętności tylko podczas uruchamiania.

**Rozwiązanie:** całkowicie uruchom ponownie IDE (Cursor/VS Code) lub zamknij i ponownie otwórz agenta opartego na terminalu (Claude Code).

### Konflikt globalny a lokalny

Jeśli instalacja została przeprowadzona z flagą `--global`, agent może ją ignorować na rzecz reguł specyficznych dla projektu.

**Rozwiązanie:** spróbuj zainstalować umiejętność bezpośrednio w katalogu głównym projektu bez flagi globalnej:

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## Zasoby

- [Umiejętności Gemini API na GitHubie](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pl)
- [Krótkie wprowadzenie](https://ai.google.dev/gemini-api/docs/quickstart?hl=pl)
- [Biblioteki](https://ai.google.dev/gemini-api/docs/libraries?hl=pl)

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-04-29 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-04-29 UTC."],[],[]]
