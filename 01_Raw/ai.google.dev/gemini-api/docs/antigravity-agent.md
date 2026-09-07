---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pt-BR
fetched_at: 2026-09-07T05:36:27.222626+00:00
title: "Agente do Antigravity \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Agente do Antigravity

O agente do Antigravity é um agente gerenciado de uso geral na API Gemini. Uma única chamada de API oferece um agente que raciocina, executa código, gerencia arquivos e navega na Web dentro do seu próprio sandbox seguro do Linux, hospedado pelo Google.

Ele é alimentado pelo Gemini 3.7 Flash e usa o mesmo arnês do IDE do Antigravity. É possível configurar o modelo do Gemini usando `agent_config`. Disponível na [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) e no [Google AI Studio](https://aistudio.google.com?hl=pt-br).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## Recursos

Cada chamada pode provisionar uma sandbox do Linux e iniciar um loop de uso de ferramentas. O agente planeja, age, observa os resultados e repete até que a tarefa seja concluída.

- **Execução de código**:execute comandos Bash, Python e Node.js. Instale pacotes, execute testes e crie apps.
- **Gerenciamento de arquivos**:leia, grave, edite, pesquise e liste arquivos na sandbox. Os arquivos são mantidos entre as interações.
- **Acesso à Web**:Pesquisa Google e busca de URLs para dados.
- **Compactação de contexto**:compactação automática de contexto (acionada com aproximadamente 135 mil tokens) para oferecer suporte a sessões longas e multiturno sem perder o contexto ou atingir os limites de tokens.

Consulte o [Guia de início rápido](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pt-br) para uso multiturno e streaming.

## Ferramentas compatíveis

Por padrão, o agente tem acesso a `code_execution`, `google_search` e `url_context`. As ferramentas do sistema de arquivos são ativadas automaticamente quando você especifica o parâmetro `environment`. Também é possível definir **funções personalizadas** para conectar o agente às suas próprias APIs e ferramentas. Só é necessário especificar o parâmetro `tools` ao personalizar ou restringir o conjunto padrão ou ao adicionar funções personalizadas.

| Ferramenta | Valor "Tipo" | Descrição |
| --- | --- | --- |
| execução de código | `code_execution` | Execute comandos do shell (bash, Python, Node) com captura de stdout/stderr. |
| Pesquisa Google | `google_search` | Pesquise na Web pública. |
| Contexto do URL | `url_context` | Buscar e ler páginas da Web. |
| Sistema de arquivos | *(ativado por `environment`)* | Ler, gravar, editar, pesquisar e listar arquivos na sandbox. O sistema ativa essas ferramentas automaticamente quando você define o `environment`. |
| Funções personalizadas | `function` | Defina funções personalizadas que o agente pode solicitar para executar. Consulte [Chamada de função](#function-calling). |
| Servidor MCP remoto | `mcp_server` | Registre servidores externos do Protocolo de Contexto de Modelo (MCP) como ferramentas. Consulte [Servidores MCP](#mcp-servers). |

É possível interceptar e validar a execução das ferramentas `code_execution` e `filesystem` diretamente no sandbox remoto usando [hooks](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=pt-br) síncronos.

Para limitar o agente a ferramentas específicas, transmita apenas as que você precisa:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Search for the latest AI research papers on reasoning and summarize them.",
    environment="remote",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"},
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Search for the latest AI research papers on reasoning and summarize them.",
    environment: "remote",
    tools: [
        { type: "google_search" },
        { type: "url_context" },
    ],
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Search for the latest AI research papers on reasoning and summarize them.",
    "environment": "remote",
    "tools": [
        {"type": "google_search"},
        {"type": "url_context"}
    ]
}'
```

## Entrada multimodal

O agente do Antigravity é compatível com entradas multimodais. No momento, apenas entradas `text` e `image` são aceitas. As imagens precisam ser fornecidas como strings in-line codificadas em base64 (`data`).

### Python

```
import base64
from google import genai

client = genai.Client()

with open("path/to/chart.png", "rb") as f:
    image_bytes = f.read()

interaction_inline = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=[
        {"type": "text", "text": "Analyze this chart and summarize the trends."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png",
        },
    ],
    environment="remote",
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64Image = fs.readFileSync("path/to/chart.png", { encoding: "base64" });

const interactionInline = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: [
        { type: "text", text: "Analyze this chart and summarize the trends." },
        {
            type: "image",
            data: base64Image,
            mime_type: "image/png",
        },
    ],
    environment: "remote",
}, { timeout: 300000 });
```

### REST

```
BASE64_IMAGE=$(base64 -w0 /path/to/chart.png)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d "{
    \"agent\": \"antigravity-preview-05-2026\",
    \"input\": [
        {\"type\": \"text\", \"text\": \"Analyze this chart and summarize the trends.\"},
        {
            \"type\": \"image\",
            \"mime_type\": \"image/png\",
            \"data\": \"$BASE64_IMAGE\"
        }
    ],
    \"environment\": \"remote\"
}"
```

## Chamadas de função

Com a chamada de função, é possível conectar o agente do Antigravity a APIs e bancos de dados externos definindo ferramentas personalizadas que o agente pode invocar. Para conceitos gerais, consulte [Chamada de função com a API Gemini](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pt-br).

O exemplo a seguir demonstra uma interação de duas rodadas. Primeiro, o agente solicita uma chamada de função `get_weather` personalizada. O cliente a executa e retorna o resultado na segunda vez.

### Python

```
from google import genai

client = genai.Client()

# 1. Define the custom function
get_weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the current weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and country, e.g. San Francisco, USA",
            }
        },
        "required": ["location"],
    },
}

# 2. Call the agent with the custom tool (Turn 1)
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[
        {"type": "code_execution"},  # Enable default code execution
        get_weather_tool,            # Add custom function
    ],
)

# Check if the agent requested a function call
if interaction.status == "requires_action":
    # Find function calls that do not have a matching function result.
    # Filesystem tools (like write_file) are also represented as function calls
    # but are executed automatically by the environment.
    executed_calls = {step.call_id for step in interaction.steps if step.type == "function_result"}
    pending_calls = [step for step in interaction.steps if step.type == "function_call" and step.id not in executed_calls]

    if pending_calls:
        fc_step = pending_calls[0]
        print(f"Function to call: {fc_step.name} (ID: {fc_step.id})")
        print(f"Arguments: {fc_step.arguments}")

        # 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
        function_result = {
            "temperature": 23,
            "unit": "celsius"
        }

        final_interaction = client.interactions.create(
            agent="antigravity-preview-05-2026",
            previous_interaction_id=interaction.id,  # Reference the interaction ID
            environment=interaction.environment_id,
            input=[
                {
                    "type": "function_result",
                    "name": fc_step.name,
                    "call_id": fc_step.id,
                    "result": function_result,
                }
            ],
        )

        print(final_interaction.output_text)
        # Output: The current weather in Tokyo, Japan is 23°C (Celsius).
    else:
        print("No pending function calls.")
else:
    print(f"Interaction completed with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// 1. Define the custom function
const get_weather_tool = {
  type: "function",
  name: "get_weather",
  description: "Gets the current weather for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city and country, e.g. San Francisco, USA",
      },
    },
    required: ["location"],
  },
};

// 2. Call the agent with the custom tool (Turn 1)
const interaction = await client.interactions.create({
  agent: "antigravity-preview-05-2026",
  input: "What is the weather in Tokyo?",
  environment: "remote",
  tools: [
    { type: "code_execution" },
    get_weather_tool,
  ],
}, { timeout: 300000 });

if (interaction.status === "requires_action") {
  // Find function calls that do not have a matching function result.
  // Filesystem tools (like write_file) are also represented as function calls
  // but are executed automatically by the environment.
  const executedCalls = new Set(
    interaction.steps
      .filter(s => s.type === "function_result")
      .map(s => s.call_id)
  );
  const pendingCalls = interaction.steps.filter(
    s => s.type === "function_call" && !executedCalls.has(s.id)
  );

  if (pendingCalls.length > 0) {
    const fcStep = pendingCalls[0];
    console.log(`Function to call: ${fcStep.name} (ID: ${fcStep.id})`);

    // 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
    const functionResult = {
      temperature: 23,
      unit: "celsius"
    };

    const finalInteraction = await client.interactions.create({
      agent: "antigravity-preview-05-2026",
      previous_interaction_id: interaction.id, // Reference the interaction ID
      environment: interaction.environment_id,
      input: [
        {
          type: "function_result",
          name: fcStep.name,
          call_id: fcStep.id,
          result: functionResult,
        }
      ],
    }, { timeout: 300000 });

    console.log(finalInteraction.output_text);
  } else {
    console.log("No pending function calls.");
  }
} else {
  console.log(`Interaction completed with status: ${interaction.status}`);
}
```

### REST

```
# 1. Turn 1: Request function call
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [
          {"type": "code_execution"},
          {
              "type": "function",
              "name": "get_weather",
              "description": "Gets the current weather for a given location.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {"type": "string"}
                  },
                  "required": ["location"]
              }
          }
      ]
  }')

# Extract interaction ID, environment ID, and call ID (requires jq)
INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')
ENVIRONMENT_ID=$(echo $RESPONSE | jq -r '.environment_id')
CALL_ID=$(echo $RESPONSE | jq -r '.steps[] | select(.type=="function_call") | .id')

# 2. Turn 2: Send function result back using variables
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"input\": [
          {
              \"type\": \"function_result\",
              \"name\": \"get_weather\",
              \"call_id\": \"$CALL_ID\",
              \"result\": {
                  \"temperature\": 23,
                  \"unit\": \"celsius\"
              }
          }
      ]
  }"
```

## Servidores MCP

É possível conectar o agente do Antigravity a ferramentas externas registrando servidores remotos do Protocolo de Contexto de Modelo (MCP). O agente é compatível com servidores MCP remotos por HTTP transmitível.

Ao registrar um servidor MCP, especifique os seguintes campos na matriz `tools`:

| Campo | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `type` | string | Sim | Precisa ser `"mcp_server"`. |
| `name` | string | Sim | Um identificador exclusivo do servidor. Precisa ser estritamente minúsculo e alfanumérico (correspondente a `^[a-z0-9_-]+$`). |
| `url` | string | Sim | O URL do endpoint do servidor MCP remoto. |
| `headers` | objeto | Não | Cabeçalhos personalizados (por exemplo, autenticação) enviados com solicitações. |
| `allowed_tools` | matriz | Não | Lista de nomes de ferramentas que podem ser executadas. Se for omitido, todas as ferramentas serão permitidas. |

### Python

```
from google import genai

client = genai.Client()

# Register a remote HTTP MCP server
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[{
        "type": "mcp_server",
        "name": "weather", # Must be lowercase
        "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "What is the weather in Tokyo?",
    environment: "remote",
    tools: [{
        type: "mcp_server",
        name: "weather", // Must be lowercase
        url: "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [{
          "type": "mcp_server",
          "name": "weather",
          "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
      }]
  }'
```

## Seleção de modelos

Para `antigravity-preview-05-2026`, o modelo padrão é o **Gemini 3.7 Flash** (`gemini-3.7-flash`). Se você omitir `agent_config`, o agente vai usar `gemini-3.7-flash` por padrão.

É possível configurar o modelo do Gemini usando `agent_config` para otimizar a velocidade, o custo ou a capacidade de raciocínio.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Summarize the key differences between functional and object-oriented programming.",
    environment="remote",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.5-flash-lite",
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Summarize the key differences between functional and object-oriented programming.",
    environment: "remote",
    agent_config: {
        type: "antigravity",
        model: "gemini-3.5-flash-lite",
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Summarize the key differences between functional and object-oriented programming.",
      "environment": "remote",
      "agent_config": {
          "type": "antigravity",
          "model": "gemini-3.5-flash-lite"
      }
  }'
```

Os valores aceitos para `agent_config.model` são:

| Modelo | Valor em `agent_config.model` | Descrição |
| --- | --- | --- |
| **Gemini 3.7 Flash** (padrão) | `gemini-3.7-flash` | Modelo equilibrado padrão para raciocínio, programação e uso de ferramentas. |
| **Gemini 3.6 Flash** | `gemini-3.6-flash` | Modelo Flash de geração anterior para fluxos de trabalho gerais com agentes. |
| **Gemini 3.5 Flash** | `gemini-3.5-flash` | Modelo leve para fluxos de trabalho gerais. |
| **Gemini 3.5 Flash-Lite** | `gemini-3.5-flash-lite` | Modelo leve otimizado para baixa latência e tarefas econômicas. |

Ao criar um agente gerenciado com `agents.create`, você configura o modelo da mesma forma, transmitindo `base_agent` e `agent_config`. Não é possível substituir o modelo no momento da interação de um agente gerenciado criado com `agents.create`. O modelo é bloqueado para o que foi definido quando o agente foi criado. Isso garante um comportamento previsível de chamada de função, depuração consistente e adesão aos limites de segurança.

## Personalizar o agente

É possível ampliar o agente do Antigravity personalizando as instruções, ferramentas e ambiente dele. O agente oferece suporte a uma abordagem nativa do sistema de arquivos para personalização: é possível montar arquivos como `AGENTS.md` para instruções e habilidades em `.agents/skills/` diretamente no sandbox ou transmitir a configuração inline no momento da interação. Você pode iterar na configuração in-line e salvá-la como um agente gerenciado quando estiver tudo pronto.

Para saber todos os detalhes sobre como criar agentes personalizados, consulte [Como criar agentes gerenciados](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pt-br).

## Execução em segundo plano

As tarefas do agente que envolvem raciocínio em várias etapas, execução de código ou operações de arquivo podem levar minutos para serem concluídas. Use `background=True` para executar a interação de forma assíncrona. A API retorna imediatamente com um ID de interação que você pesquisa até que o status seja `completed` ou `failed`.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Start the interaction in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Run a complex analysis on the repository.",
    environment="remote",
    background=True,
)

print(f"Interaction started in background: {interaction.id}")

# 2. Poll for completion
while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Run a complex analysis on the repository.",
    environment: "remote",
    background: true,
});

console.log(`Interaction started in background: ${interaction.id}`);

let result = interaction;
while (result.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    result = await client.interactions.get(interaction.id);
}

if (result.status === "completed") {
    console.log(result.output_text);
} else {
    console.log(`Finished with status: ${result.status}`);
}
```

### REST

```
# 1. Start the interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Run a complex analysis on the repository.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll for results (repeat until status is "completed")
curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

A execução em segundo plano requer `store=True`, que é o padrão. Para atualizações de progresso em tempo real durante a execução em segundo plano, consulte [Interações em segundo plano de streaming](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=pt-br#streaming-background).

É possível cancelar uma interação em segundo plano em execução usando o método `cancel`.

### Python

```
client.interactions.cancel(id="INTERACTION_ID")
```

### JavaScript

```
await client.interactions.cancel("INTERACTION_ID");
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID:cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

**Multiturno com execução em segundo plano**

Quando uma interação em segundo plano envolve ferramentas com estado (como execução de código em uma sandbox), use o `environment_id` da interação concluída para continuar no mesmo ambiente. Isso garante que o agente retome de onde parou com todos os arquivos e estados intactos.

### Python

```
import time
from google import genai

client = genai.Client()

# First turn: run a task in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Clone https://github.com/google/generative-ai-python and run its tests.",
    environment="remote",
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Second turn: continue in the same environment
followup = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Fix any failing tests and re-run them.",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    background=True,
)

while followup.status == "in_progress":
    time.sleep(5)
    followup = client.interactions.get(id=followup.id)

print(followup.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First turn: run a task in the background
let interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Clone https://github.com/google/generative-ai-python and run its tests.",
    environment: "remote",
    background: true,
});

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

// Second turn: continue in the same environment
let followup = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Fix any failing tests and re-run them.",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    background: true,
});

while (followup.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    followup = await client.interactions.get(followup.id);
}

console.log(followup.output_text);
```

### REST

```
# 1. Start first interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Clone https://github.com/google/generative-ai-python and run its tests.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll until completed (repeat until status is "completed")
RESULT=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY")

ENVIRONMENT_ID=$(echo $RESULT | jq -r '.environment_id')

# 3. Continue in the same environment
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"input\": \"Fix any failing tests and re-run them.\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"background\": true
  }"
```

## Ambientes

Cada chamada cria ou reutiliza um sandbox do Linux. O parâmetro `environment` tem três formas:

| Formulário | Descrição |
| --- | --- |
| `"remote"` | Provisione um novo sandbox com as configurações padrão. |
| `"env_abc123"` | Reutilize um ambiente existente por ID, preservando todos os arquivos e estados. |
| `{...}` | `EnvironmentConfig` completo com fontes personalizadas e regras de rede. |

Consulte [Ambientes](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br) para detalhes sobre fontes (Git, GCS, inline), rede, ciclo de vida e limites de recursos.

## Gatilhos

Com os gatilhos, é possível programar um agente para ser executado automaticamente em uma programação cron. Um acionador vincula um agente, um ambiente, um comando e uma programação a um recurso persistente que é disparado sem intervenção manual. Cada execução reutiliza o mesmo ambiente. Portanto, os arquivos criados em uma execução persistem e ficam visíveis para a próxima.

### Criar um gatilho

Crie um gatilho especificando uma programação cron, um fuso horário e a configuração de interação. O acionador começa no status `active` e é ativado no próximo horário de cron correspondente. Salve o `id` retornado para gerenciar o gatilho em chamadas subsequentes.

### Python

```
from google import genai

client = genai.Client()

trigger = client.triggers.create(
    schedule="0 9 * * *",
    time_zone="America/Argentina/Buenos_Aires",
    display_name="issue-solver",
    interaction={
        "agent": "antigravity-preview-05-2026",
        "input": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        "environment": {
            "type": "remote",
            "network": {
                "allowlist": [
                    {
                        "domain": "api.github.com",
                        "transform": {
                            "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                        },
                    },
                    {"domain": "github.com"},
                ]
            },
        },
    },
)

print(f"Trigger created: {trigger.id}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const trigger = await client.triggers.create({
    schedule: "0 9 * * *",
    time_zone: "America/Argentina/Buenos_Aires",
    display_name: "issue-solver",
    interaction: {
        agent: "antigravity-preview-05-2026",
        input: [{
            type: "text",
            text: "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        }],
        environment: {
            type: "remote",
            network: {
                allowlist: [
                    {
                        domain: "api.github.com",
                        transform: {
                            "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                        },
                    },
                    { domain: "github.com" },
                ],
            },
        },
    },
});

console.log(`Trigger created: ${trigger.id}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "schedule": "0 9 * * *",
      "time_zone": "America/Argentina/Buenos_Aires",
      "display_name": "issue-solver",
      "interaction": {
          "agent": "antigravity-preview-05-2026",
          "input": [{"type": "text", "text": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled accepted, skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/."}],
          "environment": {
              "type": "remote",
              "network": {
                  "allowlist": [
                      {
                          "domain": "api.github.com",
                          "transform": {
                              "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                          }
                      },
                      {"domain": "github.com"}
                  ]
              }
          }
      }
  }'
```

A solicitação `CreateTrigger` aceita os seguintes campos:

| Campo | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `schedule` | string | Sim | Expressão cron (por exemplo, `0 * * * *` para horária, `0 9 * * 1-5` para manhãs de dias da semana). |
| `time_zone` | string | Sim | Fuso horário da IANA (por exemplo, `UTC`, `America/Argentina/Buenos_Aires`). |
| `display_name` | string | Não | Nome legível do acionador. |
| `max_consecutive_failures` | número inteiro | Não | Número máximo de falhas antes que o gatilho seja pausado automaticamente. Padrão: 5. |
| `execution_timeout_seconds` | número inteiro | Não | Tempo limite por execução em segundos. Padrão: 600. |
| `interaction` | objeto | Sim | Um `CreateInteractionRequest` que define o agente, a entrada, as ferramentas e o ambiente. |

A resposta inclui os seguintes campos principais:

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `id` | string | Identificador exclusivo do gatilho. Use isso em todas as operações subsequentes. |
| `status` | string | Estado atual: `active`, `paused` ou `disabled`. |
| `next_run_time` | string | Carimbo de data/hora ISO 8601 da próxima execução programada. |
| `consecutive_failure_count` | número inteiro | Número de execuções consecutivas com falha desde o último sucesso. |

### Listar gatilhos

Recupere todos os acionadores associados ao seu projeto.

### Python

```
triggers = client.triggers.list()
for trigger in triggers.triggers:
    print(f"{trigger.id}: {trigger.display_name} ({trigger.status})")
```

### JavaScript

```
const triggers = await client.triggers.list();
for (const trigger of triggers.triggers) {
    console.log(`${trigger.id}: ${trigger.display_name} (${trigger.status})`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Receber um gatilho

Extrai a configuração completa e o estado atual de um único gatilho.

### Python

```
trigger = client.triggers.get(id="TRIGGER_ID")
print(f"Schedule: {trigger.schedule}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
const trigger = await client.triggers.get("TRIGGER_ID");
console.log(`Schedule: ${trigger.schedule}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Pausar e retomar

É possível pausar um gatilho para interromper as execuções programadas e retomá-lo para reativar a programação. A pausa não afeta as execuções manuais.

### Python

```
# Pause
client.triggers.update(id="TRIGGER_ID", status="paused")

# Resume
client.triggers.update(id="TRIGGER_ID", status="active")
```

### JavaScript

```
// Pause
await client.triggers.update("TRIGGER_ID", { status: "paused" });

// Resume
await client.triggers.update("TRIGGER_ID", { status: "active" });
```

### REST

```
# Pause
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "paused"}'

# Resume
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "active"}'
```

### Excluir um gatilho

Remover um gatilho permanentemente. O histórico de execuções anteriores não é excluído.

### Python

```
client.triggers.delete(id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.delete("TRIGGER_ID");
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Executar um gatilho imediatamente

Disparar um gatilho sob demanda sem esperar o próximo horário programado. Isso funciona mesmo se o gatilho estiver pausado.

### Python

```
client.triggers.run(trigger_id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.run("TRIGGER_ID");
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Listar execuções

Confira o histórico de execução de um gatilho. Cada execução inclui um `status`, carimbos de data/hora, um `interaction_id` que pode ser usado para buscar a saída completa da interação e um `environment_id` confirmando que todas as execuções compartilham a mesma sandbox.

### Python

```
executions = client.triggers.list_executions(trigger_id="TRIGGER_ID")
for ex in executions.trigger_executions:
    print(f"{ex.id}: {ex.status} ({ex.start_time} - {ex.end_time})")

# Fetch the full interaction for an execution
interaction = client.interactions.get(id=ex.interaction_id)
print(interaction.output_text)
```

### JavaScript

```
const executions = await client.triggers.listExecutions("TRIGGER_ID");
for (const ex of executions.trigger_executions) {
    console.log(`${ex.id}: ${ex.status} (${ex.start_time} - ${ex.end_time})`);
}

// Fetch the full interaction for an execution
const interaction = await client.interactions.get(ex.interaction_id);
console.log(interaction.output_text);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Disponibilidade e preços

O agente do Antigravity está disponível em versão prévia pela
[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) no Google AI Studio
e na API Gemini para projetos de nível sem custo financeiro e pago.

Os preços seguem um [modelo de pagamento por uso](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#pricing-for-agents)
com base nos tokens do modelo do Gemini e nas ferramentas usadas pelo agente. Ao contrário de uma
solicitação de chat padrão que produz uma única saída, uma interação do Antigravity é um
fluxo de trabalho de agente. Uma única solicitação aciona um loop autônomo de raciocínio, execução de ferramentas, execução de código e gerenciamento de arquivos. Os projetos do nível sem custo financeiro incluem um limite de taxa e uma cota de uso sem custo financeiro.

As interações de antigravidade executam loops autônomos multiturno e podem consumir muitos tokens. Defina [controles de orçamento](#budget-controls) na sua solicitação para limitar o uso de tokens. Também é possível monitorar o progresso em tempo real com o
[streaming de SSE](https://ai.google.dev/gemini-api/docs/streaming?hl=pt-br) ou cancelar solicitações em execução.

### Controles de orçamento

Além da [seleção de modelo](#model-selection), defina `max_total_tokens` em `agent_config` (com `"type": "antigravity"`) para limitar o número total de tokens (entrada + saída + pensamento) que uma interação pode consumir.
Os tokens em cache não são contabilizados nesse limite. Quando o agente atinge o limite, a
interação é interrompida e retorna com `status: "incomplete"`. O limite é o melhor possível: o uso real pode exceder ligeiramente esse valor, dependendo de quando o agente verifica o orçamento entre as etapas.

Defina o orçamento na solicitação de interação em `agent_config` junto com `agent` e `input`.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    },
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": "/workspace/data.csv",
                "content": "id,name,value\n1,alpha,100\n2,beta,200\n",
            }
        ],
    }
)
print(f"Status: {interaction.status}")  # "incomplete" if budget was hit
print(f"Tokens used: {interaction.usage.total_tokens}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config: {
        type: "antigravity",
        max_total_tokens: 50000
    },
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: "/workspace/data.csv",
                content: "id,name,value\n1,alpha,100\n2,beta,200\n",
            },
        ],
    },
});
console.log(`Status: ${interaction.status}`);
console.log(`Tokens used: ${interaction.usage.total_tokens}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    },
    "environment": {
      "type": "remote",
      "sources": [
        {
          "type": "inline",
          "target": "/workspace/data.csv",
          "content": "id,name,value\n1,alpha,100\n2,beta,200\n"
        }
      ]
    }
  }'
```

#### Continuar uma interação incompleta

Quando uma interação retorna `status: "incomplete"`, o trabalho e o contexto do agente são preservados. Envie uma nova interação referenciando a interação original `id` e
`environment_id` para continuar de onde parou. A nova interação recebe um orçamento
`max_total_tokens` próprio.

### Python

```
# Continue from where the agent stopped
continuation = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="continue",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    }
)
print(f"Status: {continuation.status}")
```

### JavaScript

```
const continuation = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "continue",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    agent_config: {
        type: "antigravity",
        max_total_tokens: 50000
    }
});
console.log(`Status: ${continuation.status}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "continue",
    "previous_interaction_id": "INTERACTION_ID",
    "environment": "ENVIRONMENT_ID",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    }
  }'
```

### Custos estimados

Os custos variam de acordo com a complexidade da tarefa. O agente determina de forma autônoma quantas chamadas de ferramentas, execuções de código e operações de arquivo são necessárias. As estimativas a seguir são baseadas em execuções.

| Categoria da tarefa | Tokens de entrada | Tokens de saída | Custo normal |
| --- | --- | --- | --- |
| **Análise de Conteúdo e síntese de informações** | 100 mil a 500 mil | 10.000 a 40.000 | US$ 0,30 a US$ 1,00 |
| **Geração de documentos e conteúdo** | 100 mil a 500 mil | 15 mil a 50 mil | US$ 0,30 a US$ 1,30 |
| **Design de processos e sistemas** | 100 mil a 400 mil | 10.000 a 30.000 | US$ 0,25 a US$ 0,80 |
| **Processamento e análise de dados** | 300 mil a 3 milhões | 30 mil a 150 mil | US$ 0,70 a US$ 3,25 |

Normalmente, 50 a 70% dos tokens de entrada são armazenados em cache. Fluxos de trabalho complexos com muitas chamadas de ferramentas podem acumular de 3 a 5 milhões de tokens em uma única interação, com custos de até US$5.

A **computação de ambiente** (CPU, memória, execução de sandbox) **não é faturada** durante o período de pré-lançamento.

## Limitações

- **Status do pré-lançamento**:o agente do Antigravity e a API Interactions. Os recursos e esquemas podem mudar.
- **Configuração de geração sem suporte**:os parâmetros a seguir não são compatíveis e retornam um erro 400: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Saída estruturada**:o agente do Antigravity não aceita saídas estruturadas.
- **Ferramentas indisponíveis**:`file_search`, `computer_use` e `google_maps` ainda não são compatíveis.
- **Limitações do MCP remoto**:o transporte de eventos enviados pelo servidor (SSE) não é compatível. Use HTTP transmissível. Além disso, o servidor `name` precisa ser estritamente minúsculo e alfanumérico. O uso de letras maiúsculas aciona um erro genérico `400 Bad Request`.
- **Ferramenta de sistema de arquivos**:não há uma ferramenta de sistema de arquivos no momento. Ele faz parte do `environment`.
- **Requisito da loja**:a execução do agente usando `background=True` exige `store=True`.
- **Chamada de função somente com estado**:a chamada de função só é compatível com o modo com estado. Você precisa usar `previous_interaction_id` para continuar a vez. Não é possível reconstruir o histórico manualmente (modo sem estado).
- **Tipos multimodais não aceitos.** No momento, não há suporte para entradas de áudio, vídeo e documentos. Somente texto e imagem são permitidos.

## A seguir

- [Guia de início rápido](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pt-br): conversas multiturno e streaming.
- [Como criar agentes personalizados](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pt-br): instruções, habilidades e como salvar agentes.
- [Ambientes](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br): configuração do sandbox, fontes, rede.
- [Hooks](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=pt-br): aplicam portões de controle de segurança e validação de efeitos colaterais dentro do sandbox.
- [Agente Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br): tarefas de pesquisa mais longas.
- [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br): a API subjacente.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-08-19 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-08-19 UTC."],[],[]]
