---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=pl
fetched_at: 2026-10-26T05:40:34.789619+00:00
title: "Konfiguracja agenta do kodowania i\u00a0materia\u0142y dla deweloper\u00f3w \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Konfiguracja agenta do kodowania i materiały dla deweloperów

Agenty AI do kodowania korzystają z danych treningowych, które kończą się w określonym dniu. Z tego powodu agenci często sugerują wycofane modele (`gemini-1.5`), starsze pakiety SDK (`google-generativeai`) lub nieaktualne wzorce kodu.

Połączenie agenta z oficjalnymi zasobami dla programistów Gemini pomaga mu pisać dokładny kod z użyciem bieżących modeli, pakietu `google-genai` SDK i [interfejsu Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl).

Możesz przyznać agentowi do kodowania dostęp do dokumentacji i zasad Gemini na 4 sposoby:

## Podsumowanie zasobów agenta

| Zasób | Co zapewnia | Dostępność |
| --- | --- | --- |
| **[Umiejętności agenta Gemini](https://ai.google.dev/gemini-api/docs/coding-agents?hl=pl#available-skills)** | Szczegółowe reguły, wzorce pakietu SDK i skrypty pomocnicze dotyczące konkretnych funkcji (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`). | Jest wstępnie zainstalowany w [AI Studio Build](https://ai.studio/build). Możesz go zainstalować za pomocą `skills.sh`, Context7 lub zarządzanych agentów. |
| **[Serwer MCP Gemini Docs](https://ai.google.dev/gemini-api/docs/coding-agents?hl=pl#mcp-setup)** | Wyszukiwanie na żywo (`gemini_search_docs`) i czytanie całej strony (`gemini_get_doc`) w całej dokumentacji. | Obsługiwane w Claude Code, Cursor, OpenAI Codex i VS Code. |
| **[Wtyczka Gemini API](https://ai.google.dev/gemini-api/docs/coding-agents?hl=pl#gemini-api-plugin)** | Pakiet łączony zawierający oficjalne umiejętności Gemini, serwer MCP Dokumentów i narzędzia klucza interfejsu API. | Antigravity. |
| **[Dokumenty w formacie do odczytu maszynowego](https://ai.google.dev/gemini-api/docs/coding-agents?hl=pl#machine-readable-docs)** | Oczyść strony Markdown i `llms.txt` indeksy. | Wszystkie strony dokumentacji w domenie `ai.google.dev/gemini-api/docs`. |

## Instalowanie umiejętności agenta Gemini

Umiejętności agenta zapewniają agentowi do kodowania reguły proceduralne, aktualne nazwy modeli i wzorce kodu pakietu SDK. Zamiast dodawać do prompta długich instrukcji, Twój agent wczytuje każdą umiejętność tylko wtedy, gdy jest to potrzebne. Dzięki temu Twój agent uniknie przestarzałych pakietów SDK i będzie korzystać z nowoczesnych wzorców Gemini.

Umiejętności działają razem z serwerem MCP Dokumentów Gemini. Jeśli agent nie ma zainstalowanego serwera MCP, usługa przełącza się na [`llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=pl). Aby dowiedzieć się więcej o tym, jak działają umiejętności, przeczytaj [przewodnik po umiejętnościach interfejsu Gemini API](https://aistudio.google.com/learn/gemini-api-skills?hl=pl).

### Instalowanie za pomocą interfejsu wiersza poleceń (`skills.sh` lub Context7)

Zainstaluj umiejętności za pomocą skryptu [skills.sh](https://skills.sh) (zalecane) lub
[Context7](https://context7.com):

```
# List all available skills in the repository
npx skills add google-gemini/gemini-skills --list

# Install a specific skill globally with skills.sh
npx skills add google-gemini/gemini-skills --skill <skill-name> --global

# Or install with Context7
npx ctx7 skills install /google-gemini/gemini-skills <skill-name>
```

### Dostępne umiejętności

#### `gemini-api-dev`

Umiejętność tworzenia aplikacji za pomocą [interfejsu API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) i oficjalnych pakietów SDK Gemini API (`google-genai` dla Pythona i `@google/genai` dla TypeScript). Ta umiejętność obejmuje:

- generowanie tekstu, czat wieloetapowy, przesyłanie strumieniowe, dane wyjściowe strukturalne i wywoływanie funkcji;
- Generowanie obrazów, zamiana tekstu na mowę (TTS) i dane wejściowe multimodalne
- Zarządzanie stanem rozmowy po stronie serwera, wykonywanie w tle, Deep Research i zarządzani agenci
- Obecne nazwy modeli i migracja starszego kodu `generateContent` lub `google-generativeai`

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### `gemini-live-api-dev`

Umiejętność tworzenia aplikacji do strumieniowania dźwięku i wideo w czasie rzeczywistym za pomocą [interfejsu Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=pl). Ta umiejętność obejmuje:

- zarządzanie sesjami WebSocket, tymczasowe tokeny klienta i wznawianie sesji;
- Strumieniowanie dźwięku, wideo i tekstu z wykrywaniem aktywności głosowej (VAD) i obsługą przerywania
- Uzasadnianie w tle (rozszerzone myślenie), nieblokujące asynchroniczne wywołania narzędzi, transkrypcja i tłumaczenie mowy na żywo

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### `gemini-omni-flash-api`

Umiejętność generowania i edytowania filmów za pomocą Gemini Omni Flash przy użyciu interfejsu Interactions API. Zawiera skrypty pomocnicze (`upload_file.py`, `generate_video.py`, `prep_video.py`, `inspect_video.py`) i obejmuje:

- Generowanie filmów na podstawie tekstu i tworzenie promptów
- Przejścia między pierwszą a ostatnią klatką i generowanie filmów na podstawie klatek referencyjnych
- Rozszerzenia wideo i przepływy pracy związane z wstępnym przetwarzaniem multimediów

```
npx skills add google-gemini/gemini-skills --skill gemini-omni-flash-api --global
```

### Montowanie umiejętności w zarządzanych agentach

Gdy uruchamiasz zdalnie zarządzane agenty za pomocą interfejsu Interactions API, możesz zamontować repozytorium `google-gemini/gemini-skills` w przestrzeni roboczej agenta. Szczegółowe informacje znajdziesz w [przewodniku po umiejętnościach interfejsu Gemini API](https://aistudio.google.com/learn/gemini-api-skills?hl=pl):

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Build a script that generates a 5-second video of a neon cityscape.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/google-gemini/gemini-skills",
                "target": ".agents",
            }
        ],
    },
)
```

## Łączenie serwera MCP Gemini Docs

Publiczny **serwer MCP Dokumentów Gemini** (`https://gemini-api-docs-mcp.dev`) zapewnia agentowi dostęp na żywo do całej witryny z dokumentacją. Agent może wyszukiwać i czytać strony dokumentacji, aby sprawdzać schematy żądań, limity modeli i nowe funkcje:

- `gemini_search_docs`: wyszukuje w dokumentacji interfejsu Gemini API według tematu lub zapytania.
- `gemini_get_doc`: Odczytuje pełną treść w formacie Markdown na określonej stronie dokumentacji.

### Szybka konfiguracja

Uruchom to polecenie w terminalu lub w katalogu głównym projektu, aby automatycznie skonfigurować wykryte agenty do kodowania:

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

### Konfiguracja według środowiska

### Claude Code

Uruchom w terminalu:

```
$ claude mcp add --transport http geminiDocs https://gemini-api-docs-mcp.dev
```

### Kursor

Dodaj do `~/.cursor/mcp.json` (globalnie) lub `.cursor/mcp.json` (w projekcie):

```
{
  "mcpServers": {
    "geminiDocs": {
      "url": "https://gemini-api-docs-mcp.dev"
    }
  }
}
```

### OpenAI Codex

Uruchom w terminalu:

```
$ codex mcp add geminiDocs --url https://gemini-api-docs-mcp.dev
```

Możesz też dodać do `~/.codex/config.toml`:

```
[mcp_servers.geminiDocs]
url = "https://gemini-api-docs-mcp.dev"
```

### VS Code (Copilot)

Dodaj do `.vscode/mcp.json` w obszarze roboczym:

```
{
  "servers": {
    "geminiDocs": {
      "type": "http",
      "url": "https://gemini-api-docs-mcp.dev"
    }
  }
}
```

## Wtyczka Gemini API

Jeśli używasz **Antigravity**, **wtyczka Gemini API** to najszybszy sposób na skonfigurowanie obszaru roboczego. Zawiera serwer MCP Dokumentów Gemini, wszystkie oficjalne umiejętności Gemini (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`) i narzędzia klucza interfejsu API w jednym pakiecie do pobrania.

- **Instalacja w Antigravity (interfejs):** otwórz **Ustawienia > Dostosowywanie > Twórz za pomocą wtyczek Google** i pobierz **Gemini API**.
- **Instalacja za pomocą interfejsu wiersza poleceń:**
  `bash
  agy plugin install https://github.com/google-gemini/gemini-skills`

## Dokumentacja czytelna dla komputerów

Standardowe strony internetowe zawierają tagi HTML, paski nawigacyjne i skrypty, które zajmują miejsce w oknie kontekstu. `ai.google.dev` udostępnia punkty końcowe czytelne dla maszyn, dzięki czemu agenci i skrypty mogą pobierać czysty kod Markdown bezpośrednio:

- **`llms.txt` index**
  ([`https://ai.google.dev/gemini-api/docs/llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=pl)):
  zawiera listę wszystkich stron dokumentacji interfejsu Gemini API z linkami do każdej z nich.
- **Bezpośrednie adresy URL Markdown (`.md.txt`):** dodaj `.md.txt` do dowolnego adresu URL dokumentacji na stronie `ai.google.dev` (np. [`https://ai.google.dev/gemini-api/docs/coding-agents.md.txt`](https://ai.google.dev/gemini-api/docs/coding-agents.md.txt?hl=pl)), aby uzyskać czyste źródło Markdown dla zapisanych promptów, reguł `AGENTS.md` lub skryptów automatycznych.

## Zalecane reguły projektu (`AGENTS.md`)

Plik reguł projektu (`AGENTS.md`, `.cursorrules` lub `CLAUDE.md`) zawiera podstawowe reguły, które są wczytywane na początku każdej sesji agenta. Dodaj te wytyczne do katalogu głównego projektu, aby agenci kodujący domyślnie korzystali z bieżących modeli i pakietów SDK:

```
# Gemini API Guidelines

- Before writing Gemini API code, consult the `geminiDocs` MCP server (`gemini_search_docs` / `gemini_get_doc`) or `https://ai.google.dev/gemini-api/docs/llms.txt`.
- Always use the current Gemini API SDK (`google-genai` for Python, `@google/genai` for TypeScript/JavaScript). Never use legacy SDKs (`google-generativeai` or `@google/generative-ai`).
- Use the Interactions API (`client.interactions.create`) for new applications unless a specific feature requires `generateContent`.
- Use current recommended models (see https://ai.google.dev/gemini-api/docs/models) and avoid deprecated models.
```

## Sprawdzanie i rozwiązywanie problemów

### Sprawdzanie konfiguracji

Aby przetestować konfigurację, zapytaj asystenta kodowania:

```
Look up the request schema for the Gemini Interactions API in the documentation.
```

Skonfigurowany agent będzie używać `gemini_search_docs` na `geminiDocs` serwerze MCP i pisać kod za pomocą `client.interactions.create` z pakietem SDK `google-genai` lub `@google/genai`.

### Polecenia stanu

| Środowisko | Weryfikacja MCP | Weryfikacja umiejętności |
| --- | --- | --- |
| **Claude Code** | Uruchom `/mcp` | Uruchom `/skills` |
| **Kursor** | Otwórz **Ustawienia > Funkcje > MCP**. | Otwórz **Ustawienia > Reguły**. |
| **OpenAI Codex** | Uruchom `codex mcp list` | Sprawdź `.codex/skills/` lub `~/.codex/skills/` |
| **Antigravity** | Otwórz **Dostosowywanie > Połączenia**. | Otwórz **Dostosowania > Reguły** lub uruchom `/skills list` |
| **VS Code (Copilot)** | Otwórz **Rozszerzenia > MCP** lub panel wyjściowy. | W Copilot Chat kliknij **Wybierz narzędzia**. |

### Rozwiązywanie problemów

- **Nie wykryto umiejętności ani serwera MCP:** ponownie uruchom edytor (Cursor lub VS Code) lub sesję terminala (Claude Code lub Codex). Większość agentów wczytuje serwery MCP i umiejętności tylko podczas uruchamiania.
- **Konflikt umiejętności globalnej:** jeśli Twój agent ignoruje zainstalowaną globalnie umiejętność, zainstaluj ją w katalogu głównym projektu bez `--global`:
  `bash
  npx skills add google-gemini/gemini-skills --skill gemini-api-dev`
- **Zignorowane reguły:** upewnij się, że plik `AGENTS.md`, `.cursorrules` lub `CLAUDE.md` znajduje się w katalogu głównym projektu.

## Co dalej?

- [Przewodnik po umiejętnościach interfejsu Gemini API](https://aistudio.google.com/learn/gemini-api-skills?hl=pl)
- [Umiejętności związane z interfejsem Gemini API na GitHubie](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl)
- [Dostępne modele](https://ai.google.dev/gemini-api/docs/models?hl=pl)
- [Biblioteki i pakiety SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=pl)

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-10-06 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-10-06 UTC."],[],[]]
