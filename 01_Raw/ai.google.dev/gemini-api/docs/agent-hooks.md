---
source_url: https://ai.google.dev/gemini-api/docs/agent-hooks?hl=pl
fetched_at: 2026-10-26T05:41:37.791860+00:00
title: "Hooks \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Hooks

Haczyki umożliwiają uruchamianie niestandardowych skryptów lub zewnętrznych żądań HTTP bezpośrednio przed lub po wykonaniu przez agenta kodu lub zmodyfikowaniu plików w zdalnym środowisku piaskownicy. Używaj hooków, aby rozszerzać pętlę agenta o automatyczne zabezpieczenia i przepływy pracy w tle, takie jak:

- **Wymuszanie zabezpieczeń i ograniczeń dostępu** przed wykonaniem poleceń powłoki wysokiego ryzyka lub odczytaniem plików o ograniczonym dostępie.
- **Automatyzacja przekształceń potoku danych** natychmiast po utworzeniu lub zmodyfikowaniu plików przez agenta.
- **Przesyłanie strumieniowe danych telemetrycznych kontroli przedsiębiorstwa** do zewnętrznych systemów monitorowania po wykonaniu narzędzia.

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "security-gate": {
        "pre_tool_execution": [
            {
                "matcher": "code_execution",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/gate.py",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

gate_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
"""

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Run `rm -rf /tmp/forbidden` using code_execution.",
    tools=[{"type": "code_execution"}],
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/gate.py",
                "content": gate_script,
            },
        ],
    },
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const hooksConfig = {
    "security-gate": {
        pre_tool_execution: [
            {
                matcher: "code_execution",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/gate.py",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const gateScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
`;

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Run `rm -rf /tmp/forbidden` using code_execution.",
    tools: [{ type: "code_execution" }],
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                target: ".agents/hooks-scripts/gate.py",
                content: gateScript,
            },
        ],
    },
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

String hooksConfig = """
{
  "security-gate": {
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
""";

String gateScript = "#!/usr/bin/env python3\n"
    + "import sys, json\n"
    + "data = json.load(sys.stdin)\n"
    + "cmd = str(data.get(\"tool_call\", {}).get(\"args\", {}))\n"
    + "if \"rm -rf\" in cmd:\n"
    + "    print(json.dumps({\"decision\": \"deny\", \"reason\": \"Destructive command blocked by security gate.\"}))\n"
    + "else:\n"
    + "    print(json.dumps({\"decision\": \"allow\"}))\n";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks-scripts/gate.py")
            .content(gateScript)
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Run `rm -rf /tmp/forbidden` using code_execution."))
    .tools(List.of(CodeExecution.builder().build()))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    hooksConfig := `{
  "security-gate": {
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}`

    gateScript := `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks-scripts/gate.py"),
                Content: genai.Ptr(gateScript),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Run `rm -rf /tmp/forbidden` using code_execution."),
            Tools:       []interactions.Tool{interactions.NewTool(interactions.CodeExecution{})},
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": [{"type": "text", "text": "Run `rm -rf /tmp/forbidden` using code_execution."}],
      "tools": [{"type": "code_execution"}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"security-gate\": {\"pre_tool_execution\": [{\"matcher\": \"code_execution\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/gate.py\", \"timeout\": 10}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/gate.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\ncmd = str(data.get(\"tool_call\", {}).get(\"args\", {}))\nif \"rm -rf\" in cmd:\n    print(json.dumps({\"decision\": \"deny\", \"reason\": \"Destructive command blocked by security gate.\"}))\nelse:\n    print(json.dumps({\"decision\": \"allow\"}))\n"
              }
          ]
      }
  }'
```

## Obsługiwane zdarzenia cyklu życia

Haki obsługują w piaskownicy 2 zdarzenia:

| Zdarzenie | Kiedy się uruchamia | Działanie |
| --- | --- | --- |
| `pre_tool_execution` | Bezpośrednio przed uruchomieniem narzędzia | Może zatwierdzić (`allow`) lub zablokować (`deny`) narzędzie przed jego wykonaniem. Gdy model zostanie zablokowany, zobaczy powód odrzucenia i dostosuje się do niego. |
| `post_tool_execution` | od razu po zakończeniu działania narzędzia, | Wykonuje zadania uzupełniające, takie jak formatowanie kodu, uruchamianie testów jednostkowych czy rejestrowanie danych telemetrycznych. Nie można blokować ani cofać wykonanych działań. |

### `pre_tool_execution`

Uruchamia się tuż przed wykonaniem narzędzia. Skrypt odczytuje szczegóły wywołania narzędzia z `stdin` i zapisuje decyzję w formacie JSON (`allow` lub `deny`) w `stdout`.

**Ładunek wejściowy (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "rm -rf /tmp/forbidden",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

**Odpowiedź wyjściowa (`stdout`):**

Aby zatwierdzić wywołanie narzędzia:

```
{
  "decision": "allow"
}
```

Aby zablokować wywołanie narzędzia i przekazać opinię do modelu:

```
{
  "decision": "deny",
  "reason": "Destructive command blocked by security gate."
}
```

Gdy funkcja hook odrzuci polecenie, wywołanie narzędzia zostanie natychmiast pominięte. Agent widzi wynik błędu zawierający przyczynę odrzucenia bezpośrednio w bieżącej turze. Model może wtedy samodzielnie skorygować błąd, wybierając alternatywne polecenie lub wyjaśniając użytkownikowi, dlaczego polecenie zostało zablokowane.

Jeśli skrypt zwraca nierozpoznany format JSON, zwykły tekst lub cokolwiek innego niż `{"decision": "deny"}`, środowisko wykonawcze traktuje odpowiedź jako zatwierdzenie (`allow`).

### `post_tool_execution`

Wysyłane natychmiast po zakończeniu działania narzędzia. Skrypt odczytuje szczegóły wykonania i stan błędu z `stdin`.

**Ładunek wejściowy (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "python3 /workspace/app.py",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

Jeśli polecenie powłoki wyświetla błędy w standardowym strumieniu błędów (`stderr`) lub operacja w systemie plików kończy się niepowodzeniem, w ładunku znajduje się pole `"error"` zawierające tekst błędu. Jeśli polecenie zakończy się bez błędów, pole `"error"` zostanie całkowicie pominięte.

**Odpowiedź wyjściowa (`stdout`):**

```
{}
```

Ponieważ funkcje wywoływane po użyciu narzędzia są uruchamiane wyłącznie w przypadku zadań w tle, takich jak formatowanie kodu lub rejestrowanie, środowisko wykonawcze ignoruje wszystkie wartości decyzji zwrócone w przypadku funkcji `stdout`.

## Wykrywanie konfiguracji

Środowisko wykonawcze automatycznie wykrywa definicje funkcji hook z `.agents/hooks.json` lub `/.agents/hooks.json` w środowisku piaskownicy. Możesz podać `hooks.json` wraz ze skryptami niestandardowymi, korzystając z dowolnego obsługiwanego [źródła środowiska](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl#mount_from_a_source):

- **Montowanie repozytorium:** repozytorium Git zawierające `.agents/hooks.json` wraz z `AGENTS.md`.
- **Cloud Storage (`gcs`):** zasobnik GCS zawierający `hooks.json` skopiowane do środowiska.
- **Źródła wbudowane:** nieprzetworzony ciąg znaków JSON i zawartość skryptu przekazywane w parametrze `environment.sources` podczas wywoływania funkcji `client.interactions.create`.

### `hooks.json` schemat

Plik `hooks.json` grupuje definicje zdarzeń (`pre_tool_execution` lub `post_tool_execution`) pod niestandardowymi nazwami. Każdą grupę możesz włączyć lub wyłączyć osobno:

```
{
  "security-gate": {
    "enabled": true,
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  },
  "auto-format": {
    "post_tool_execution": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/auto_lint.py",
            "timeout": 15
          }
        ]
      }
    ]
  }
}
```

### Składnia i reguły dopasowywania

Każda grupa reguł w `hooks.json` określa, kiedy i jak wywoływane są moduły obsługi, za pomocą właściwości `matcher` i `hooks`:

| Pole | Typ | Opis |
| --- | --- | --- |
| `enabled` | `boolean` | Opcjonalnie: Ustaw wartość `false`, aby wyłączyć grupę (domyślnie `true`). |
| `matcher` | `string` | Wyrażenie regularne pasujące do nazw narzędzi w kontenerze. |
| `hooks` | `array` | Uporządkowana lista definicji modułów obsługi (`command` lub `http`). Moduły obsługi są uruchamiane sekwencyjnie w kolejności deklaracji. |

#### Jak działa ocena wyrażeń regularnych

Gdy agent wywołuje narzędzie w piaskownicy, środowisko wykonawcze porównuje nazwę kontenera narzędzia z wzorcem `matcher` przy użyciu standardowych wyrażeń regularnych RE2. Jeśli wyrażenie regularne pasuje do nazwy narzędzia, wszystkie moduły obsługi w tablicy `hooks` są wykonywane po kolei. Jeśli do tego samego narzędzia pasuje kilka grup reguł, uruchamiane są wszystkie odpowiednie tablice obsługi.

Możesz kierować reklamy na dowolną nazwę wbudowanego narzędzia kontenera: wykonywanie kodu (`code_execution`) lub operacje na systemie plików (`view_file`, `write_to_file`, `replace_file_content`, `list_dir` i `delete_file`).

#### Typowe wyrażenia dopasowujące

- `"code_execution"`: dokładne dopasowanie ciągu znaków w przypadku poleceń powłoki i wykonywania skryptów.
- `"write_to_file"`: Dokładne dopasowanie do tworzenia plików w systemie plików i zapisywania na dysku.
- `"view_file|write_to_file"`: Rozdzielanie pionową kreską dopasowuje kilka konkretnych nazw narzędzi w jednej regule.
- `".*_file"`: wyrażenie regularne z wieloznacznym dopasowaniem do dowolnego narzędzia kończącego się na `_file` (np. `view_file`, `write_to_file` lub `delete_file`). Obejmuje to tylko część zestawu narzędzi systemu plików. Narzędzia `replace_file_content` i `list_dir` nie kończą się na `_file`, więc w razie potrzeby musisz je podać wprost. Standardowe wyrażenia regularne RE2 wymagają znaku `.*`. Proste wzorce powłoki, takie jak `*_file`, mają nieprawidłową składnię wyrażenia regularnego i nie będą pasować.
- `".*"` lub `"*"` lub `""`: wzorzec ogólny, który przechwytuje każde wywołanie narzędzia w kontenerze.

## Typy obsługi

### Haczyki Command

Haczyki poleceń wykonują polecenie powłoki lub skrypt w piaskownicy. Skrypt otrzymuje kod JSON zdarzenia w `stdin` i zwraca kod JSON decyzji w `stdout`.

| Pole | Typ | Opis |
| --- | --- | --- |
| `type` | `string` | Musi to być `"command"`. |
| `command` | `string` | Wiersz poleceń do uruchomienia w piaskownicy (np. `python3 /.agents/hooks-scripts/gate.py`). |
| `timeout` | `integer` | Czas oczekiwania w sekundach. Domyślnie: `30`. |

### Haczyki HTTP

Haczyki HTTP wysyłają zdarzenie JSON jako żądanie POST na zewnętrzny adres URL HTTPS bezpośrednio z sieci piaskownicy. Serwer docelowy zwraca swoją decyzję w treści odpowiedzi HTTP w tym samym formacie JSON (`{"decision": "allow"}` lub `{"decision": "deny", "reason": "..."}`).

| Pole | Typ | Opis |
| --- | --- | --- |
| `type` | `string` | Musi to być `"http"`. |
| `url` | `string` | Zewnętrzny punkt końcowy HTTPS, do którego ma być wysyłany ładunek zdarzenia. |
| `headers` | `object` | Opcjonalne pary klucz-wartość dla niestandardowych nagłówków nie zawierających informacji poufnych (np. `{"X-Event-Source": "agent-sandbox"}`). Do uwierzytelniania używaj [danych logowania](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=pl) na liście dozwolonych sieci. |
| `timeout` | `integer` | Czas oczekiwania w sekundach. Domyślnie: `30`. |

#### Serwer proxy ruchu wychodzącego i transformacja tokena

Haczyki HTTP są wykonywane bezpośrednio w przestrzeni nazw sieci piaskownicy, więc żądania wychodzące przechodzą przez przezroczysty serwer proxy ruchu wychodzącego. Ta architektura zapewnia 2 kluczowe zalety w zakresie bezpieczeństwa:

- **Dodawanie sieci do białej listy:** punkty końcowe docelowe muszą być wyraźnie dozwolone w `network.allowlist` Twojego środowiska. Ruch zwrotny (`127.0.0.1` lub `localhost`) jest blokowany przez serwer proxy. Zawsze kieruj ruch do zewnętrznych punktów końcowych na liście dozwolonych.
- **Wstrzykiwanie danych logowania:** nie musisz przechowywać kluczy interfejsu API ani tajnych tokenów dostępu w `.agents/hooks.json` ani montować ich w kontenerze. Zapisz obiekt tajny jako [dane logowania](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=pl) i odwołuj się do niego za pomocą identyfikatora z `network.allowlist` środowiska. Serwer proxy wychodzący automatycznie przechwytuje wychodzący ruch HTTP hook i wstrzykuje prawdziwy nagłówek uwierzytelniania przed opuszczeniem piaskownicy. Nagłówki zestawu reguł wbudowanych `transform` są ustawiane w ten sam sposób, a dane logowania są używane, gdy chcesz ponownie użyć obiektu tajnego w projekcie i zmienić go w jednym miejscu. Patrz [konfiguracja sieci](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl#network-configuration).

## Jak środowisko wykonawcze obsługuje decyzje i błędy

- **Synchroniczne oczekiwanie:** agent wstrzymuje działanie i czeka na zakończenie działania Twoich funkcji, zanim przejdzie dalej.
- **Blokowanie wykonania narzędzia:** jeśli funkcja pre-tool hook zwróci wartość `{"decision": "deny", "reason": "<your reason>"}`, środowisko wykonawcze natychmiast anuluje wywołanie narzędzia. Model widzi powód odrzucenia w historii rozmowy i dostosowuje się, wybierając bezpieczną alternatywę lub wyjaśniając użytkownikowi blokadę.
- **Obsługa awarii skryptu, błędów HTTP i przekroczenia limitu czasu:** jeśli skrypt polecenia ulegnie awarii (stan wyjścia różny od zera), wywołanie HTTP zwróci kod stanu inny niż 2xx (np. błąd serwera 4xx lub 5xx) albo operacja przekroczy limit czasu lub zwróci nierozpoznany format JSON, środowisko wykonawcze potraktuje to jako zatwierdzenie (`allow`). Wykonanie narzędzia będzie kontynuowane normalnie, więc uszkodzony skrypt lub nieosiągalny serwer telemetrii nigdy nie spowoduje zakleszczenia aplikacji.

## Częste przypadki użycia

### Wielokrotne przywracanie danych w celu zapewnienia prywatności i zgodności z przepisami

Gdy funkcja blokuje dostęp do zasobów o ograniczonym dostępie, takich jak katalogi zawierające informacje umożliwiające identyfikację osoby lub poufne dokumenty finansowe, możesz przekazać wartość `previous_interaction_id` w następnym wywołaniu, aby kontynuować turę w tym samym środowisku. Agent odczytuje wyjaśnienie odmowy i automatycznie przywraca działanie, wysyłając zapytanie do zatwierdzonych tabel publicznych.

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "privacy-gate": {
        "pre_tool_execution": [
            {
                "matcher": "view_file",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/check_privacy.py",
                        "timeout": 5,
                    }
                ],
            }
        ]
    }
}

check_privacy_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
"""

# Step 1: Agent attempts to read confidential PII records and is intercepted
int_1 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                "content": check_privacy_script,
            },
            {
                "type": "inline",
                "target": "workspace/private/employees.json",
                "content": '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                "type": "inline",
                "target": "workspace/public/summary.json",
                "content": '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
)
print(int_1.output_text)

# Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
int_2 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment=int_1.environment_id,
    previous_interaction_id=int_1.id,
)
print(int_2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const hooksConfig = {
    "privacy-gate": {
        pre_tool_execution: [
            {
                matcher: "view_file",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/check_privacy.py",
                        timeout: 5,
                    },
                ],
            },
        ],
    },
};

const checkPrivacyScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential \`/private/\` records is blocked by PII compliance policy. Query approved \`/public/\` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
`;

const int1 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                "target": ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                content: checkPrivacyScript,
            },
            {
                type: "inline",
                "target": "workspace/private/employees.json",
                content: '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                type: "inline",
                "target": "workspace/public/summary.json",
                content: '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
});
console.log(int1.output_text);

const int2 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment: int1.environment_id,
    previous_interaction_id: int1.id,
});
console.log(int2.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

String hooksConfig = """
{
  "privacy-gate": {
    "pre_tool_execution": [
      {
        "matcher": "read_file",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/check_privacy.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
""";

String checkPrivacyScript = "#!/usr/bin/env python3\n"
    + "import sys, json\n"
    + "data = json.load(sys.stdin)\n"
    + "path = str(data.get(\"tool_call\", {}).get(\"args\", {}).get(\"path\", \"\"))\n"
    + "if \"/private/\" in path:\n"
    + "    resp = {\n"
    + "        \"decision\": \"deny\",\n"
    + "        \"reason\": \"Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead.\"\n"
    + "    }\n"
    + "else:\n"
    + "    resp = {\"decision\": \"allow\"}\n"
    + "print(json.dumps(resp))\n";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks-scripts/check_privacy.py")
            .content(checkPrivacyScript)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target("workspace/private/employees.json")
            .content("{\"employees\": [{\"id\": 1, \"salary\": 150000, \"ssn\": \"000-00-0000\"}]}")
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target("workspace/public/summary.json")
            .content("{\"department\": \"Engineering\", \"team_size\": 42, \"status\": \"active\"}")
            .build()
    ))
    .build();

// Step 1: Agent attempts to read confidential PII records and is intercepted
CreateAgentInteraction params1 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction int1 = client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();
System.out.println(int1.outputText().orElse(""));

// Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
CreateAgentInteraction params2 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary."))
    .environment(CreateAgentInteractionEnvironment.of(int1.environmentId().orElse("")))
    .previousInteractionId(int1.id().orElse(""))
    .build();

Interaction int2 = client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();
System.out.println(int2.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    hooksConfig := `{
  "privacy-gate": {
    "pre_tool_execution": [
      {
        "matcher": "read_file",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/check_privacy.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}`

    checkPrivacyScript := `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))
if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential '/private/' records is blocked by PII compliance policy. Query approved '/public/' summary tables instead."
    }
else:
    resp = {"decision": "allow"}
print(json.dumps(resp))
`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks-scripts/check_privacy.py"),
                Content: genai.Ptr(checkPrivacyScript),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr("workspace/private/employees.json"),
                Content: genai.Ptr(`{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}`),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr("workspace/public/summary.json"),
                Content: genai.Ptr(`{"department": "Engineering", "team_size": 42, "status": "active"}`),
            },
        },
    }

    // Step 1: Agent attempts to read confidential PII records and is intercepted
    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    int1 := res1.Interaction
    if int1.OutputText != nil {
        fmt.Println(*int1.OutputText)
    }

    // Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary."),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*int1.EnvironmentID)),
            PreviousInteractionID: int1.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res2.Interaction.OutputText != nil {
        fmt.Println(*res2.Interaction.OutputText)
    }
}
```

### REST

```
# Step 1: Attempt to access restricted PII directory (blocked by hook)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to read /workspace/private/employees.json and summarize the employee details."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"privacy-gate\": {\"pre_tool_execution\": [{\"matcher\": \"view_file\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/check_privacy.py\", \"timeout\": 5}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/check_privacy.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\npath = str(data.get(\"tool_call\", {}).get(\"args\", {}).get(\"path\", \"\"))\nif \"/private/\" in path:\n    resp = {\"decision\": \"deny\", \"reason\": \"Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead.\"}\nelse:\n    resp = {\"decision\": \"allow\"}\nprint(json.dumps(resp))\n"
              },
              {
                  "type": "inline",
                  "target": "workspace/private/employees.json",
                  "content": "{\"employees\": [{\"id\": 1, \"salary\": 150000, \"ssn\": \"000-00-0000\"}]}"
              },
              {
                  "type": "inline",
                  "target": "workspace/public/summary.json",
                  "content": "{\"department\": \"Engineering\", \"team_size\": 42, \"status\": \"active\"}"
              }
          ]
      }
  }'

# Step 2: Continue in the same environment using $ENV_ID and $INTERACTION_ID from the previous response
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "Content-Type: application/json" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -d '{
#       "agent": "antigravity-preview-09-2026",
#       "input": [{"type": "text", "text": "Understood. Please read the approved /workspace/public/summary.json file instead and provide the summary."}],
#       "environment": "'"$ENV_ID"'",
#       "previous_interaction_id": "'"$INTERACTION_ID"'"
#   }'
```

### Logowanie kontrolne i telemetria zewnętrzne

Wysyłanie zdarzeń kontrolnych w czasie rzeczywistym z piaskownicy na zewnętrzny serwer monitorowania za każdym razem, gdy pliki są odczytywane lub modyfikowane.

- **Dopasowywanie wielu narzędzi:** ponieważ dopasowywanie odbywa się za pomocą standardowych wyrażeń regularnych, możesz połączyć wiele narzędzi w jednej regule, używając pionowych kresek (`view_file|write_to_file|replace_file_content`) lub symboli wieloznacznych (`.*_file`).
- **Nie umieszczaj informacji poufnych w konfiguracji:** przechowuj token uwierzytelniający jako [dane logowania](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=pl) i odwołuj się do niego za pomocą identyfikatora z [konfiguracji sieci](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl#network-configuration) środowiska (`network.allowlist.credential`). Serwer proxy ruchu wychodzącego wstrzykuje rzeczywisty token dostępu do żądań wychodzących. W tym przykładzie nagłówek jest ustawiany w wierszu za pomocą `transform`, który jest chroniony przez ten sam serwer proxy i pasuje, gdy token należy do tej konfiguracji.

### Python

```
import json
from google import genai

client = genai.Client()

# Define hook without secrets; the egress proxy injects headers dynamically
hooks_config = {
    "audit-logging": {
        "post_tool_execution": [
            {
                "matcher": "view_file|write_to_file|replace_file_content",
                "hooks": [
                    {
                        "type": "http",
                        "url": "https://telemetry.example.com/api/v1/agent-events",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "telemetry.example.com",
                    "transform": {
                        "Authorization": "Bearer telemetry_secret_token_123",
                    },
                },
                {"domain": "*"},
            ]
        },
    },
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Define hook without secrets; the egress proxy injects headers dynamically
const hooksConfig = {
    "audit-logging": {
        post_tool_execution: [
            {
                matcher: "view_file|write_to_file|replace_file_content",
                hooks: [
                    {
                        type: "http",
                        url: "https://telemetry.example.com/api/v1/agent-events",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
        ],
        network: {
            allowlist: [
                {
                    domain: "telemetry.example.com",
                    transform: {
                        Authorization: "Bearer telemetry_secret_token_123",
                    },
                },
                { domain: "*" },
            ],
        },
    },
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

// Define hook without secrets; the egress proxy injects headers dynamically
String hooksConfig = """
{
  "audit-logging": {
    "post_tool_execution": [
      {
        "matcher": "read_file|write_file",
        "hooks": [
          {
            "type": "http",
            "url": "https://telemetry.example.com/api/v1/agent-events",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
""";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build()
    ))
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("telemetry.example.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer telemetry_secret_token_123"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("*").build()
            )))
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // Define hook without secrets; the egress proxy injects headers dynamically
    hooksConfig := `{
  "audit-logging": {
    "post_tool_execution": [
      {
        "matcher": "read_file|write_file",
        "hooks": [
          {
            "type": "http",
            "url": "https://telemetry.example.com/api/v1/agent-events",
            "timeout": 10
          }
        ]
      }
    ]
  }
}`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
        },
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "telemetry.example.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer telemetry_secret_token_123",
                    })),
                },
                {
                    Domain: "*",
                },
            })),
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to create /workspace/audit.log containing event 1, then immediately read it back using your filesystem read tool."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"audit-logging\": {\"post_tool_execution\": [{\"matcher\": \"view_file|write_to_file|replace_file_content\", \"hooks\": [{\"type\": \"http\", \"url\": \"https://telemetry.example.com/api/v1/agent-events\", \"timeout\": 10}]}]}}"
              }
          ],
          "network": {
              "allowlist": [
                  {
                      "domain": "telemetry.example.com",
                      "transform": {
                          "Authorization": "Bearer telemetry_secret_token_123"
                      }
                  },
                  {"domain": "*"}
              ]
          }
      }
  }'
```

## Ograniczenia

- **Zakres narzędzia w piaskownicy:** haki przechwytują wbudowane narzędzia w piaskownicy: wykonywanie kodu (`code_execution`) i operacje na systemie plików (`view_file`, `write_to_file`, `replace_file_content`, `list_dir` i `delete_file`). Nie są one wywoływane w przypadku wywoływania funkcji niestandardowych (`function`) ani zewnętrznych narzędzi Model Context Protocol (`mcp_server`) obsługiwanych poza kontenerem.
- **Listy dozwolonych sieci:** haki HTTP działają w sieci kontenera. Musisz wyraźnie zezwolić na docelowe adresy URL w `network.allowlist` środowiska. Adresy typu loopback (`localhost`, `127.0.0.1`) są blokowane przez serwer proxy.
- **Automatyczne zatwierdzanie w przypadku błędów:** jeśli skrypt hooka ulegnie awarii (niezerowy stan zakończenia), przekroczy limit czasu lub zakończy się niepowodzeniem, środowisko wykonawcze zarejestruje błąd i umożliwi kontynuowanie wywołania narzędzia. Dzięki temu uszkodzone skrypty narzędzia do sprawdzania kodu lub zawieszone procesy nigdy nie spowodują zakleszczenia aplikacji.
- **Ochrona konfiguracji piaskownicy:** ponieważ wywołania zwrotne są wykonywane w piaskownicy kontenera, agenci z narzędziami do zapisu w systemie plików lub uprawnieniami do wykonywania kodu powłoki mogą modyfikować lokalne `.agents/hooks.json` lub skrypty w obszarach roboczych z możliwością zapisu. Używaj punktów zaczepienia kontenera jako automatycznych wskazówek dotyczących zasad i operacyjnych zabezpieczeń. Jeśli wymagana jest ścisła odporność na manipulacje w przypadku wykonywania niezaufanych modeli, zamontuj źródła konfiguracji z repozytoriów tylko do odczytu.

## Co dalej?

- Dowiedz się, jak skonfigurować trwałe [zdalne piaskownice i środowiska](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl).
- Poznaj możliwości i wbudowane narzędzia [agenta Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl).
- Więcej informacji o sesjach wieloetapowych i przesyłaniu strumieniowym znajdziesz w [omówieniu interfejsu Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-10-07 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-10-07 UTC."],[],[]]
