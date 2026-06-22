---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pt-BR
fetched_at: 2026-06-22T06:35:29.435982+00:00
title: "Agente Antigravity \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Agente Antigravity

O agente do Antigravity é um agente gerenciado de uso geral na API Gemini. Uma única chamada de API oferece um agente que raciocina, executa código, gerencia arquivos e navega na Web dentro do seu próprio sandbox seguro do Linux, hospedado pelo Google.

Ele é alimentado pelo Gemini 3.5 Flash e usa o mesmo arnês da IDE do Antigravity. Disponível na [API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br) e no [Google AI Studio](https://aistudio.google.com?hl=pt-br).

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
-H "Api-Revision: 2026-05-20" \
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
| Sistema de arquivos | *(ativado por `environment`)* | Ler, gravar, editar, pesquisar e listar arquivos na sandbox. Não há um tipo de ferramenta separado. Ele é ativado automaticamente quando `environment` é definido. |
| Funções personalizadas | `function` | Defina funções personalizadas que o agente pode solicitar para executar. Consulte [Chamada de função](#function-calling). |

Para limitar o agente a ferramentas específicas, transmita apenas as necessárias:

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
-H "Api-Revision: 2026-05-20" \
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
-H "Api-Revision: 2026-05-20" \
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
  -H "Api-Revision: 2026-05-20" \
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
  -H "Api-Revision: 2026-05-20" \
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

## Personalizar o agente

É possível ampliar o agente do Antigravity personalizando as instruções, ferramentas e ambiente dele. O agente oferece suporte a uma abordagem nativa do sistema de arquivos para personalização: é possível montar arquivos como `AGENTS.md` para instruções e habilidades em `.agents/skills/` diretamente no sandbox ou transmitir a configuração inline no momento da interação. Você pode iterar na configuração in-line e salvá-la como um agente gerenciado quando estiver tudo pronto.

Para saber todos os detalhes sobre como criar agentes personalizados, consulte [Como criar agentes gerenciados](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pt-br).

## Ambientes

Cada chamada cria ou reutiliza um sandbox do Linux. O parâmetro `environment` tem três formas:

| Formulário | Descrição |
| --- | --- |
| `"remote"` | Provisione um novo sandbox com as configurações padrão. |
| `"env_abc123"` | Reutilize um ambiente atual por ID, preservando todos os arquivos e estados. |
| `{...}` | `EnvironmentConfig` completo com fontes personalizadas e regras de rede. |

Consulte [Ambientes](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br) para detalhes sobre fontes (Git, GCS, inline), rede, ciclo de vida e limites de recursos.

## Disponibilidade e preços

O agente do Antigravity está disponível em versão prévia pela [API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br) no Google AI Studio e na API Gemini.

Os preços seguem um [modelo de pagamento por utilização](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#pricing-for-agents) com base nos tokens do modelo do Gemini e nas ferramentas usadas pelo agente. Ao contrário de uma solicitação de chat padrão que produz uma única saída, uma interação do Antigravity é um fluxo de trabalho agêntico. Uma única solicitação aciona um loop autônomo de raciocínio, execução de ferramentas, execução de código e gerenciamento de arquivos.

### Custos estimados

Os custos variam de acordo com a complexidade da tarefa. O agente determina de forma autônoma quantas chamadas de ferramentas, execuções de código e operações de arquivo são necessárias. As estimativas a seguir são baseadas em execuções.

| Categoria da tarefa | Tokens de entrada | Tokens de saída | Custo normal |
| --- | --- | --- | --- |
| **Pesquisa e síntese de informações** | 100 mil a 500 mil | 10.000 a 40.000 | US$ 0,30 a US$ 1,00 |
| **Geração de documentos e conteúdo** | 100 mil a 500 mil | 15 mil a 50 mil | US$ 0,30 a US$ 1,30 |
| **Design de processos e sistemas** | 100 mil a 400 mil | 10.000 a 30.000 | US$ 0,25 a US$ 0,80 |
| **Processamento e análise de dados** | 300 mil a 3 milhões | 30 mil a 150 mil | R$ 0,70 a R$ 3,25 |

Normalmente, 50 a 70% dos tokens de entrada são armazenados em cache. Fluxos de trabalho complexos com muitas chamadas de ferramentas podem acumular de 3 a 5 milhões de tokens em uma única interação, com custos de até US$5.

O **computador do ambiente** (CPU, memória, execução de sandbox) **não é faturado** durante o período de pré-lançamento.

## Limitações

- **Status da prévia**:o agente do Antigravity e a API Interactions estão em prévia. Os recursos e esquemas podem mudar.
- **Configuração de geração sem suporte**:os parâmetros a seguir não são compatíveis e retornam um erro 400: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Saída estruturada**:o agente do Antigravity não aceita saídas estruturadas.
- **Ferramentas indisponíveis**:`file_search`, `computer_use`, `google_maps` e `mcp` ainda não são compatíveis.
- **Ferramenta de sistema de arquivos**:não há uma ferramenta de sistema de arquivos no momento. Ele faz parte do `environment`.
- **Contexto**:o agente não é compatível com o uso de `background=True` e exige `store=True`.
- **Chamada de função somente com estado**:a chamada de função só é compatível com o modo com estado. Você precisa usar `previous_interaction_id` para continuar a vez. Não é possível reconstruir o histórico manualmente (modo sem estado).
- **Tipos multimodais não aceitos.** No momento, não há suporte para entradas de áudio, vídeo e documentos. Somente texto e imagem são permitidos.

## A seguir

- [Guia de início rápido](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pt-br): conversas multiturno e streaming.
- [Criação de agentes personalizados](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pt-br): instruções, habilidades e salvamento de agentes personalizados.
- [Ambientes](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br): configuração do sandbox, fontes, rede.
- [Agente Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=pt-br): tarefas de pesquisa mais longas.
- [API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br): a API subjacente.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-06-17 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-06-17 UTC."],[],[]]
