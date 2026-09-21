---
source_url: https://ai.google.dev/gemini-api/docs/agent-hooks?hl=pt-BR
fetched_at: 2026-09-21T05:57:56.654152+00:00
title: "Hooks \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Hooks

Os hooks permitem executar scripts personalizados ou solicitações HTTP externas imediatamente antes ou depois que o agente executa o código ou modifica arquivos no sandbox remoto. Use hooks para estender o loop do agente com proteções automatizadas e fluxos de trabalho em segundo plano, como:

- **Aplicar proteções de segurança e acesso** antes da execução de comandos shell de alto risco ou leituras de arquivos restritas.
- **Automatizar transformações de pipeline de dados** logo depois que um agente cria ou modifica arquivos.
- **Transmita telemetria de auditoria empresarial** para sistemas de monitoramento externos após a execução da ferramenta.

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

## Eventos de ciclo de vida compatíveis

Os hooks são compatíveis com dois eventos no sandbox:

| Evento | Quando é disparado | O que faz? |
| --- | --- | --- |
| `pre_tool_execution` | Logo antes de uma ferramenta ser executada | Pode aprovar (`allow`) ou bloquear (`deny`) a ferramenta antes da execução. Quando bloqueado, o modelo vê o motivo da sua rejeição e se adapta. |
| `post_tool_execution` | Logo após a conclusão de uma ferramenta | Executa tarefas de acompanhamento, como formatação de código, execução de testes de unidade ou registro de telemetria. Não é possível bloquear ou desfazer ações concluídas. |

### `pre_tool_execution`

Disparado logo antes da execução de uma ferramenta. Seu script lê os detalhes da chamada de função de `stdin` e gera o JSON de decisão (`allow` ou `deny`) em `stdout`.

**Payload de entrada (`stdin`):**

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

**Resposta da saída (`stdout`):**

Para aprovar a chamada de ferramenta:

```
{
  "decision": "allow"
}
```

Para bloquear a chamada de ferramenta e retornar feedback ao modelo:

```
{
  "decision": "deny",
  "reason": "Destructive command blocked by security gate."
}
```

Quando um hook nega um comando, a chamada de ferramenta é ignorada imediatamente. O agente mostra um resultado de erro com o motivo da rejeição na mesma vez. Em seguida, o modelo pode se autocorrigir escolhendo um comando alternativo ou explicando o bloqueio ao usuário.

Se o script gerar JSON não reconhecido, texto simples ou algo diferente de `{"decision": "deny"}`, o tempo de execução vai tratar a resposta como uma aprovação (`allow`).

### `post_tool_execution`

Disparado logo após a conclusão de uma ferramenta. O script lê os detalhes da execução e qualquer status de erro de `stdin`.

**Payload de entrada (`stdin`):**

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

Se um comando do shell imprimir erros no erro padrão (`stderr`) ou se uma operação do sistema de arquivos falhar, um campo `"error"` contendo o texto do erro será incluído no payload. Quando o comando é executado sem erros, o campo `"error"` é omitido por completo.

**Resposta da saída (`stdout`):**

```
{}
```

Como os hooks pós-ferramenta são executados estritamente para tarefas em segundo plano, como formatação de código ou geração de registros, o tempo de execução ignora todos os valores de decisão retornados em `stdout`.

## Descoberta de configuração

O ambiente de execução descobre automaticamente as definições de hook de `.agents/hooks.json` ou `/.agents/hooks.json` no ambiente de sandbox. É possível fornecer `hooks.json` com seus scripts personalizados usando qualquer [origem de ambiente](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br#mount_from_a_source) compatível:

- **Montagem do repositório**: um repositório Git que contém `.agents/hooks.json` e `AGENTS.md`.
- **Cloud Storage (`gcs`)**: um bucket do GCS que contém `hooks.json` copiado para o ambiente.
- **Fontes inline**: string JSON bruta e conteúdo do script transmitidos em `environment.sources` ao chamar `client.interactions.create`.

### `hooks.json` esquema

Um arquivo `hooks.json` agrupa definições de eventos (`pre_tool_execution` ou `post_tool_execution`) com nomes personalizados. É possível ativar ou desativar cada grupo de forma independente:

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

### Sintaxe e regras do comparador

Cada grupo de regras em `hooks.json` define quando e como os manipuladores são acionados usando as propriedades `matcher` e `hooks`:

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `enabled` | `boolean` | Opcional. Defina como `false` para desativar o grupo (`true` por padrão). |
| `matcher` | `string` | Expressão regular para fazer a correspondência de padrões com os nomes das ferramentas de destino dentro do contêiner. |
| `hooks` | `array` | Lista ordenada de definições de gerenciadores (`command` ou `http`). Os gerenciadores são executados em sequência na ordem de declaração. |

#### Como funciona a avaliação de regex

Quando o agente invoca uma ferramenta na sandbox, o tempo de execução avalia o nome do contêiner da ferramenta em relação ao seu padrão `matcher` usando expressões regulares RE2 padrão. Se a regex corresponder ao nome da ferramenta, todos os manipuladores na matriz `hooks` serão executados em ordem. Se vários grupos de regras corresponderem à mesma ferramenta, todas as matrizes de manipuladores correspondentes serão executadas.

Você pode segmentar qualquer nome de ferramenta de contêiner integrada: execução de código (`code_execution`) ou operações do sistema de arquivos (`view_file`, `write_to_file`, `replace_file_content`, `list_dir` e `delete_file`).

#### Expressões de correspondência comuns

- `"code_execution"`: correspondência exata de string para comandos do shell e execuções de script.
- `"write_to_file"`: correspondência exata para criação de arquivos do sistema de arquivos e gravações em disco.
- `"view_file|write_to_file"`: a separação por barra vertical corresponde a vários nomes de ferramentas específicas em uma única regra.
- `".*_file"`: curinga de regex que corresponde a qualquer ferramenta que termine em `_file` (como `view_file`, `write_to_file` ou `delete_file`). Isso abrange apenas parte do conjunto de ferramentas do sistema de arquivos. `replace_file_content` e `list_dir` não terminam em `_file`. Portanto, nomeie-os explicitamente quando precisar deles. As expressões regulares RE2 padrão exigem `.*`. Globs de shell simples, como `*_file`, são sintaxes de regex inválidas e não vão corresponder.
- `".*"` ou `"*"` ou `""`: padrão abrangente que intercepta todas as chamadas de função dentro do contêiner.

## Tipos de gerenciadores

### Hooks de comando

Os hooks de comando executam um comando ou script de shell dentro do sandbox. O script recebe o JSON do evento em `stdin` e gera o JSON de decisão em `stdout`.

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `type` | `string` | Precisa ser `"command"`. |
| `command` | `string` | Linha de comando a ser executada no sandbox (por exemplo, `python3 /.agents/hooks-scripts/gate.py`). |
| `timeout` | `integer` | Tempo limite em segundos. Padrão: `30`. |

### Hooks HTTP

Os hooks HTTP enviam o JSON do evento como uma solicitação POST para um URL HTTPS externo diretamente da rede sandbox. O servidor de destino retorna a decisão no corpo da resposta HTTP usando exatamente o mesmo formato JSON (`{"decision": "allow"}` ou `{"decision": "deny", "reason": "..."}`).

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `type` | `string` | Precisa ser `"http"`. |
| `url` | `string` | Endpoint HTTPS externo para POST do payload do evento. |
| `headers` | `object` | Pares de chave-valor opcionais para cabeçalhos personalizados não sensíveis (como `{"X-Event-Source": "agent-sandbox"}`). Para autenticação, use uma [credencial](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=pt-br) na lista de permissão de rede. |
| `timeout` | `integer` | Tempo limite em segundos. Padrão: `30`. |

#### Proxy de saída e transformação de token

Como os hooks HTTP são executados diretamente de dentro do namespace de rede da sandbox, as solicitações de saída passam pelo proxy de saída transparente. Essa arquitetura oferece duas vantagens de segurança importantes:

- **Lista de permissões de rede**:os endpoints de destino precisam ser explicitamente permitidos no `network.allowlist` do seu ambiente. O tráfego de loopback (`127.0.0.1` ou `localhost`) é bloqueado pelo proxy. Sempre direcione endpoints externos na lista de permissões.
- **Injeção de credenciais**:não é necessário armazenar chaves de API ou tokens de autenticação secretos em `.agents/hooks.json` nem montá-los no contêiner. Armazene o segredo uma vez como uma [credencial](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=pt-br) e faça referência a ele por ID no `network.allowlist` do seu ambiente. O proxy de saída intercepta automaticamente o tráfego de hook HTTP de saída e injeta o cabeçalho de autenticação real no fio antes de sair da sandbox. As regras `transform` inline definem cabeçalhos da mesma forma no fio. Uma credencial é a que deve ser usada quando você quer reutilizar o segredo em todo o projeto e fazer a rotação em um só lugar. Consulte [configuração de rede](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br#network-configuration).

## Como o ambiente de execução lida com decisões e falhas

- **Espera síncrona**:o agente faz uma pausa e aguarda a conclusão dos seus hooks antes de continuar.
- **Bloqueio da execução da ferramenta**:se o hook pré-ferramenta retornar `{"decision": "deny", "reason": "<your reason>"}`, o ambiente de execução vai cancelar imediatamente a chamada da ferramenta. O modelo vê o motivo da sua rejeição no histórico de conversas e se adapta escolhendo uma alternativa segura ou explicando o bloqueio ao usuário.
- **Como lidar com falhas de script, erros HTTP e tempos limite**:se um script de comando falhar (status de saída diferente de zero), um hook HTTP retornar um código de status diferente de 2xx (como um erro de servidor 4xx ou 5xx) ou uma operação atingir o tempo limite ou retornar JSON não reconhecido, o ambiente de execução vai tratar isso como uma aprovação (`allow`). A execução da ferramenta continua normalmente para que um script corrompido ou um servidor de telemetria inacessível nunca cause um deadlock no seu aplicativo.

## Casos de uso comuns

### Recuperação multiturno para privacidade de dados e compliance

Quando um hook bloqueia o acesso a recursos restritos, como diretórios que contêm informações de identificação pessoal (PII) ou registros financeiros confidenciais, é possível transmitir `previous_interaction_id` na próxima chamada para continuar a vez no mesmo ambiente. O agente lê a explicação da recusa e se recupera automaticamente consultando tabelas públicas aprovadas.

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

### Telemetria e geração de registros de auditoria externos

Envie eventos de auditoria em tempo real de dentro da sandbox para um servidor de monitoramento externo sempre que os arquivos forem lidos ou modificados.

- **Corresponder a várias ferramentas**:como os matchers usam regex padrão, é possível combinar várias ferramentas em uma única regra usando barras verticais (`view_file|write_to_file|replace_file_content`) ou caracteres curinga (`.*_file`).
- **Mantenha segredos fora da sua configuração**:armazene o token de autenticação como uma [credencial](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=pt-br) e faça referência a ele por ID na [configuração de rede](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br#network-configuration) do seu ambiente (`network.allowlist.credential`). O proxy de saída injeta o token de autenticação real em solicitações de saída. Este exemplo define o cabeçalho inline com `transform`, que é protegido pelo mesmo proxy e se encaixa quando o token pertence a essa configuração.

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
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("telemetry.example.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer telemetry_secret_token_123"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("*").build()
            ))
            .build()
    )))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
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

## Limitações

- **Escopo da ferramenta de sandbox**:os hooks interceptam ferramentas integradas no sandbox: execução de código (`code_execution`) e operações do sistema de arquivos (`view_file`, `write_to_file`, `replace_file_content`, `list_dir` e `delete_file`). Eles não são acionados para chamadas de função personalizadas (`function`) ou ferramentas externas do Protocolo de Contexto de Modelo (`mcp_server`) processadas fora do contêiner.
- **Listas de permissão de rede**:os hooks HTTP são executados na rede do contêiner. É necessário permitir explicitamente os URLs de destino no `network.allowlist` do seu ambiente. Endereços de loopback (`localhost`, `127.0.0.1`) são bloqueados pelo proxy.
- **Aprovação automática em erros**:se um script de hook falhar (status de saída diferente de zero), atingir o tempo limite ou falhar, o tempo de execução vai registrar a falha e permitir que a chamada de ferramenta continue. Isso garante que scripts de linter corrompidos ou processos pendentes nunca causem um deadlock nos seus aplicativos.
- **Proteção da configuração do sandbox**:como os hooks são executados no sandbox do contêiner, os agentes com ferramentas de gravação do sistema de arquivos ou permissões de execução de código do shell podem modificar `.agents/hooks.json` locais ou scripts em espaços de trabalho graváveis. Use hooks de contêiner como orientação de política automatizada e proteções operacionais. Se for necessária uma resistência estrita contra execuções de modelos não confiáveis, monte fontes de configuração de repositórios somente leitura.

## A seguir

- Saiba como configurar [ambientes e sandboxes remotos](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br) persistentes.
- Conheça os recursos e as ferramentas integradas do [agente do Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pt-br).
- Consulte a [visão geral da API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) para sessões multiturno e streaming.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-18 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-18 UTC."],[],[]]
