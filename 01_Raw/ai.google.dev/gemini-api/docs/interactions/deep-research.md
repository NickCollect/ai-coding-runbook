---
source_url: https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=pt-BR
fetched_at: 2026-06-15T06:31:48.985499+00:00
title: "Agente de Deep Research do Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Agente de Deep Research do Gemini

O agente Deep Research do Gemini planeja, executa e sintetiza de forma autônoma tarefas de pesquisa em várias etapas. Com a tecnologia do Gemini, ele navega por informações complexas para produzir relatórios detalhados e citados. Novas funcionalidades permitem planejar em colaboração com o agente, se conectar a ferramentas externas usando servidores MCP, incluir visualizações (como gráficos) e fornecer documentos diretamente como entrada.

As atividades de pesquisa envolvem busca e leitura iterativas e podem levar vários minutos para serem concluídas. Você precisa usar a execução em segundo plano (defina `background=true`)
para executar o agente de forma assíncrona e pesquisar resultados ou transmitir atualizações. Consulte
[Como lidar com tarefas de longa duração](#long-running-tasks) para mais detalhes.

O exemplo a seguir mostra como iniciar uma tarefa de pesquisa em segundo plano
e consultar os resultados.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.output_text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.output_text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Versões compatíveis

O agente Deep Research está disponível em duas versões:

- **Deep Research** (`deep-research-preview-04-2026`): projetado para velocidade e eficiência, ideal para ser transmitido de volta a uma interface do cliente.
- **Deep Research Max** (`deep-research-max-preview-04-2026`): máxima abrangência para coleta e síntese automatizadas de contexto.

## Planejamento colaborativo

O planejamento colaborativo permite controlar a direção da pesquisa
antes que o agente comece a trabalhar. Quando ativado, o agente retorna um plano de pesquisa proposto em vez de executar imediatamente. Em seguida, você pode
analisar, modificar ou aprovar o plano com interações de várias etapas.

### Etapa 1: pedir um plano

Defina `collaborative_planning=True` na primeira interação. O agente retorna um plano de pesquisa em vez de um relatório completo.

### Python

```
from google import genai

client = genai.Client()

plan_interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Do some research on Google TPUs.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    background=True,
)

while (result := client.interactions.get(id=plan_interaction.id)).status != "completed":
    time.sleep(5)
print(result.output_text)
```

### JavaScript

```
const planInteraction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Do some research on Google TPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    background: true
});

let result;
while ((result = await client.interactions.get(planInteraction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Do some research on Google TPUs.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "background": true
}'
```

### Etapa 2: refinar o plano (opcional)

Use `previous_interaction_id` para continuar a conversa e iterar
no plano. Mantenha `collaborative_planning=True` para continuar no modo de planejamento.

### Python

```
refined_plan = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    previous_interaction_id=plan_interaction.id,
    background=True,
)

while (result := client.interactions.get(id=refined_plan.id)).status != "completed":
    time.sleep(5)
print(result.output_text)
```

### JavaScript

```
const refinedPlan = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Focus more on the differences between Google TPUs and competitor hardware, and less on the history.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    previous_interaction_id: planInteraction.id,
    background: true
});

let result;
while ((result = await client.interactions.get(refinedPlan.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

### Etapa 3: aprovar e executar

Defina `collaborative_planning=False` (ou omita) para aprovar o plano e iniciar a pesquisa.

### Python

```
final_report = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Plan looks good!",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": False,
    },
    previous_interaction_id=refined_plan.id,
    background=True,
)

while (result := client.interactions.get(id=final_report.id)).status != "completed":
    time.sleep(5)
print(result.output_text)
```

### JavaScript

```
const finalReport = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Plan looks good!',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: false
    },
    previous_interaction_id: refinedPlan.id,
    background: true
});

let result;
while ((result = await client.interactions.get(finalReport.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Plan looks good!",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": false
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

## Visualização

Quando `visualization` está definido como `"auto"`, o agente pode gerar tabelas, gráficos e outros elementos visuais para apoiar as descobertas da pesquisa.
As imagens geradas são incluídas nas etapas de resposta e transmitidas como deltas `image`. Para ter os melhores resultados, peça recursos visuais na sua consulta. Por exemplo, "Inclua gráficos mostrando tendências ao longo do tempo" ou "Gere gráficos comparando a participação de mercado". Definir `visualization` como `"auto"` ativa o recurso, mas o agente só gera recursos visuais quando o comando os solicita.

### Python

```
import base64

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Analyze global semiconductor market trends. Include graphics showing market share changes.",
    agent_config={
        "type": "deep-research",
        "visualization": "auto",
    },
    background=True,
)

print(f"Research started: {interaction.id}")

while (result := client.interactions.get(id=interaction.id)).status != "completed":
    time.sleep(5)

for step in result.steps:
    if step.type == "model_output":
        for content_item in step.content:
            if content_item.type == "text":
                print(content_item.text)
            elif content_item.type == "image" and content_item.data:
                image_bytes = base64.b64decode(content_item.data)
                print(f"Received image: {len(image_bytes)} bytes")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Analyze global semiconductor market trends. Include graphics showing market share changes.',
    agent_config: {
        type: 'deep-research',
        visualization: 'auto'
    },
    background: true
});

console.log(`Research started: ${interaction.id}`);

let result;
while ((result = await client.interactions.get(interaction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}

for (const step of result.steps) {
    if (step.type === 'model_output') {
        for (const contentItem of step.content) {
            if (contentItem.type === 'text') {
                console.log(contentItem.text);
            } else if (contentItem.type === 'image' && contentItem.data) {
                console.log(`[Image Output: ${contentItem.data.substring(0, 20)}...]`);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Analyze global semiconductor market trends. Include graphics showing market share changes.",
    "agent_config": {
        "type": "deep-research",
        "visualization": "auto"
    },
    "background": true
}'
```

## Ferramentas compatíveis

O Deep Research é compatível com várias ferramentas integradas e externas. Por padrão (quando nenhum parâmetro `tools` é fornecido), o agente tem acesso à Pesquisa Google, ao contexto de URL e à execução de código. É possível especificar explicitamente ferramentas para restringir ou ampliar as capacidades do agente.

| Ferramenta | Valor "Tipo" | Descrição |
| --- | --- | --- |
| Pesquisa Google | `google_search` | Pesquise na Web pública. Ativado por padrão. |
| Contexto do URL | `url_context` | Ler e resumir o conteúdo de páginas da Web. Ativado por padrão. |
| execução de código | `code_execution` | Executar código para fazer cálculos e análise de dados. Ativado por padrão. |
| Servidor MCP | `mcp_server` | Conectar-se a servidores MCP remotos para acessar ferramentas externas. |
| Pesquisa de arquivos | `file_search` | Pesquise nos corpora de documentos enviados. |

### Pesquisa Google

Ative explicitamente a Pesquisa Google como a única ferramenta:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="What are the latest developments in quantum computing?",
    tools=[{"type": "google_search"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'What are the latest developments in quantum computing?',
    tools: [{ type: 'google_search' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "What are the latest developments in quantum computing?",
    "tools": [{"type": "google_search"}],
    "background": true
}'
```

### Contexto do URL

Permita que o agente leia e resuma páginas da Web específicas:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Summarize the content of https://www.wikipedia.org/.",
    tools=[{"type": "url_context"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Summarize the content of https://www.wikipedia.org/.',
    tools: [{ type: 'url_context' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Summarize the content of https://www.wikipedia.org/.",
    "tools": [{"type": "url_context"}],
    "background": true
}'
```

### execução de código

Permita que o agente execute código para cálculos e análise de dados:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Calculate the 50th Fibonacci number.",
    tools=[{"type": "code_execution"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Calculate the 50th Fibonacci number.',
    tools: [{ type: 'code_execution' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": "Calculate the 50th Fibonacci number.",
    "agent": "deep-research-preview-04-2026",
    "tools": [{"type": "code_execution"}],
    "background": true
}'
```

### Servidores MCP

Forneça o `name` e o `url` do servidor na configuração das ferramentas. Também é possível transmitir credenciais de autenticação e restringir quais ferramentas o agente pode chamar.

| Campo | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `type` | `string` | Sim | Precisa ser `"mcp_server"`. |
| `name` | `string` | Não | Um nome de exibição para o servidor MCP. |
| `url` | `string` | Não | O URL completo do endpoint do servidor MCP. |
| `headers` | `object` | Não | Pares de chave-valor enviados como cabeçalhos HTTP com cada solicitação ao servidor (por exemplo, tokens de autenticação). |
| `allowed_tools` | `array` | Não | Restringir quais ferramentas do servidor o agente pode chamar. |

#### Uso básico

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Check the status of my last server deployment.",
    tools=[
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"},
        }
    ],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Check the status of my last server deployment.',
    tools: [
        {
            type: 'mcp_server',
            name: 'Deployment Tracker',
            url: 'https://mcp.example.com/mcp',
            headers: { Authorization: 'Bearer my-token' }
        }
    ],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Check the status of my last server deployment.",
    "tools": [
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"}
        }
    ],
    "background": true
}'
```

### Pesquisa de arquivos

Use a ferramenta [Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=pt-br) para dar acesso aos seus dados.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Compare our 2025 fiscal year report against current public web news.",
    agent="deep-research-preview-04-2026",
    background=True,
    tools=[
        {
            "type": "file_search",
            "file_search_store_names": ['fileSearchStores/my-store-name']
        }
    ]
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Compare our 2025 fiscal year report against current public web news.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    tools: [
        { type: 'file_search', file_search_store_names: ['fileSearchStores/my-store-name'] },
    ]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": "Compare our 2025 fiscal year report against current public web news.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "tools": [
        {"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]},
    ]
}'
```

## Capacidade de direcionamento e formatação

Você pode direcionar a saída do agente fornecendo instruções de formatação específicas no comando. Isso permite estruturar relatórios em seções e subseções específicas, incluir tabelas de dados ou ajustar o tom para diferentes públicos-alvo (por exemplo, "técnico", "executivo", "informal").

Defina o formato de saída desejado explicitamente no texto de entrada.

### Python

```
prompt = """
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
"""

interaction = client.interactions.create(
    input=prompt,
    agent="deep-research-preview-04-2026",
    background=True
)
```

### JavaScript

```
const prompt = `
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
`;

const interaction = await client.interactions.create({
    input: prompt,
    agent: 'deep-research-preview-04-2026',
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": "Research the competitive landscape of EV batteries.\n\nFormat the output as a technical report with the following structure: \n1. Executive Summary\n2. Key Players (Must include a data table comparing capacity and chemistry)\n3. Supply Chain Risks",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'
```

## Entradas multimodais

Deep Research aceita entradas multimodais, incluindo imagens e documentos (PDFs), permitindo que o agente analise conteúdo visual e faça pesquisas baseadas na web contextualizadas pelas entradas fornecidas.

### Python

```
import time
from google import genai

client = genai.Client()

prompt = """Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground."""

interaction = client.interactions.create(
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"
        }
    ],
    agent="deep-research-preview-04-2026",
    background=True
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.output_text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const prompt = `Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground.`;

const interaction = await client.interactions.create({
    input: [
        { type: 'text', text: prompt },
        {
            type: 'image',
            mime_type: "image/jpeg",
            uri: 'https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg'
        }
    ],
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.output_text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task with image input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": [
        {"type": "text", "text": "Analyze the interspecies dynamics and behavioral risks present in the provided image of the African watering hole. Specifically, investigate the symbiotic relationship between the avian species and the pachyderms shown, and conduct a risk assessment for the reticulated giraffes based on their drinking posture relative to the specific predator visible in the foreground."},
        {"type": "image", "mime_type": "image/jpeg", "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"}
    ],
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Entendimento de documentos

Transmitir documentos diretamente como entrada multimodal. O agente analisa os documentos fornecidos e faz pesquisas com base no conteúdo deles.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input=[
        {"type": "text", "text": "What is this document about?"},
        {
            "type": "document",
            "uri": "https://arxiv.org/pdf/1706.03762",
            "mime_type": "application/pdf",
        },
    ],
    background=True,
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: [
        { type: 'text', text: 'What is this document about?' },
        {
            type: 'document',
            uri: 'https://arxiv.org/pdf/1706.03762',
            mime_type: 'application/pdf'
        }
    ],
    background: true
});
```

### REST

```
# 1. Start the research task with document input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": [
        {"type": "text", "text": "What is this document about?"},
        {"type": "document", "uri": "https://arxiv.org/pdf/1706.03762", "mime_type": "application/pdf"}
    ],
    "background": true
}'
```

## Como processar tarefas de longa duração

O Deep Research é um processo de várias etapas que envolve planejamento, pesquisa, leitura e escrita. Esse ciclo geralmente excede os limites de tempo limite padrão das chamadas de API síncronas.

Os agentes precisam usar o `background=True`. A API retorna um objeto `Interaction` parcial imediatamente. É possível usar a propriedade `id` para recuperar uma
interação para sondagem. O estado de interação vai mudar de
`in_progress` para `completed` ou `failed`.

### Streaming

O Deep Research é compatível com streaming para receber atualizações em tempo real sobre o progresso da pesquisa, incluindo resumos de ideias, saída de texto e imagens geradas.
Defina `stream=True` e `background=True`. Para um guia completo sobre streaming, incluindo tipos de eventos, streaming de ferramentas e pensamento, consulte [Interações de streaming](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=pt-br).

Para receber etapas de raciocínio intermediárias (reflexões) e atualizações de progresso,
ative os **resumos de reflexão** definindo `thinking_summaries` como
`"auto"` no `agent_config`. Sem isso, o stream só poderá fornecer os resultados finais.

#### Tipos de eventos de stream

| Tipo de evento | Tipo de delta | Descrição |
| --- | --- | --- |
| `step.delta` | `thought` | Etapa de raciocínio intermediário do agente. |
| `step.delta` | `text` | Parte da saída de texto final. |
| `step.delta` | `image` | Uma imagem gerada (codificada em base64). |

O exemplo a seguir inicia uma tarefa de pesquisa e processa o stream com
reconexão automática. Ele rastreia o `interaction_id` e o `last_event_id` para que, se a conexão cair (por exemplo, após o tempo limite de 600 segundos), ela possa ser retomada de onde parou.

### Python

```
from google import genai

client = genai.Client()

interaction_id = None
last_event_id = None
is_complete = False

def process_stream(stream):
    global interaction_id, last_event_id, is_complete
    for event in stream:
        if event.event_type == "interaction.created":
            interaction_id = event.interaction.id
        if event.event_id:
            last_event_id = event.event_id
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                print(event.delta.text, end="", flush=True)
            elif event.delta.type == "thought":
                print(f"Thought: {event.delta.text}", flush=True)
        elif event.event_type in ("interaction.completed", "error"):
            is_complete = True

stream = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
    stream=True,
    agent_config={"type": "deep-research", "thinking_summaries": "auto"},
)
process_stream(stream)

while not is_complete and interaction_id:
    status = client.interactions.get(interaction_id)
    if status.status != "in_progress":
        break
    stream = client.interactions.get(
        id=interaction_id, stream=True, last_event_id=last_event_id,
    )
    process_stream(stream)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interactionId;
let lastEventId;
let isComplete = false;

async function processStream(stream) {
    for await (const event of stream) {
        if (event.type === 'interaction.created') {
            interactionId = event.interaction.id;
        }
        if (event.event_id) lastEventId = event.event_id;
        if (event.type === 'step.delta') {
            if (event.delta.type === 'text') {
                process.stdout.write(event.delta.text);
            } else if (event.delta.type === 'thought') {
                console.log(`Thought: ${event.delta.text}`);
            }
        } else if (['interaction.completed', 'error'].includes(event.type)) {
            isComplete = true;
        }
    }
}

const stream = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    stream: true,
    agent_config: { type: 'deep-research', thinking_summaries: 'auto' },
});
await processStream(stream);

while (!isComplete && interactionId) {
    const status = await client.interactions.get(interactionId);
    if (status.status !== 'in_progress') break;
    const resumeStream = await client.interactions.get(interactionId, {
        stream: true, last_event_id: lastEventId,
    });
    await processStream(resumeStream);
}
```

### REST

```
# 1. Start the stream (save the INTERACTION_ID from the interaction.start event
#    and the last "event_id" you receive)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "stream": true,
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto"
    }
}'

# 2. If the connection drops, reconnect with your saved IDs
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID?stream=true&last_event_id=LAST_EVENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## Perguntas complementares e interações

Você pode continuar a conversa depois que o agente retornar o relatório final usando o `previous_interaction_id`. Assim, você pode pedir esclarecimentos, resumos ou mais detalhes sobre seções específicas da pesquisa sem precisar reiniciar toda a tarefa.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Can you elaborate on the second point in the report?",
    model="gemini-3.1-pro-preview",
    previous_interaction_id="COMPLETED_INTERACTION_ID"
)

print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Can you elaborate on the second point in the report?',
    model: 'gemini-3.1-pro-preview',
    previous_interaction_id: 'COMPLETED_INTERACTION_ID'
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Can you elaborate on the second point in the report?",
    "model": "gemini-3.1-pro-preview",
    "previous_interaction_id": "COMPLETED_INTERACTION_ID"
}'
```

## Quando usar o agente do Deep Research do Gemini

O Deep Research é um **agente**, não apenas um modelo. Ele é mais adequado para cargas de trabalho que exigem uma abordagem de "analista em uma caixa" em vez de um chat de baixa latência.

| Recurso | Modelos padrão do Gemini | Agente Deep Research do Gemini |
| --- | --- | --- |
| **Latência** | Segundos | Minutos (assíncrono/em segundo plano) |
| **Processo** | Gerar -> Saída | Planejar -> Pesquisar -> Ler -> Iterar -> Saída |
| **Saída** | Texto conversacional, código, resumos curtos | Relatórios detalhados, análises longas, tabelas comparativas |
| **Ideal para** | Chatbots, extração, escrita criativa | Análise de mercado, auditoria, revisões de literatura, análise da concorrência |

## Configuração do agente

Deep Research usa o parâmetro `agent_config` para controlar o comportamento.
Transmita como um dicionário com os seguintes campos:

| Campo | Tipo | Padrão | Descrição |
| --- | --- | --- | --- |
| `type` | `string` | Obrigatório | Precisa ser `"deep-research"`. |
| `thinking_summaries` | `string` | `"none"` | Defina como `"auto"` para receber etapas de raciocínio intermediárias durante o streaming. Defina como `"none"` para desativar. |
| `visualization` | `string` | `"auto"` | Defina como `"auto"` para ativar gráficos e imagens gerados pelo agente. Defina como `"off"` para desativar. |
| `collaborative_planning` | `boolean` | `false` | Defina como `true` para ativar a revisão do plano em várias etapas antes do início da pesquisa. |

### Python

```
agent_config = {
    "type": "deep-research",
    "thinking_summaries": "auto",
    "visualization": "auto",
    "collaborative_planning": False,
}

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Research the competitive landscape of cloud GPUs.",
    agent_config=agent_config,
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Research the competitive landscape of cloud GPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        visualization: 'auto',
        collaborative_planning: false,
    },
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of cloud GPUs.",
    "agent": "deep-research-preview-04-2026",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "visualization": "auto",
        "collaborative_planning": false
    },
    "background": true
}'
```

## Disponibilidade e preços

É possível acessar o Deep Research do Gemini usando a API Interactions no Google AI Studio e na API Gemini.

Os preços seguem um [modelo de pagamento por uso](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#pricing-for-agents) com base nos modelos do Gemini e nas ferramentas específicas usadas pelo agente. Ao contrário das solicitações de chat padrão, em que uma solicitação leva a uma saída, uma tarefa de Deep Research é um fluxo de trabalho de agente. Uma única solicitação aciona um ciclo autônomo de planejamento, pesquisa, leitura e raciocínio.

### Custos estimados

Os custos variam de acordo com a profundidade da pesquisa necessária. O agente determina de forma autônoma quanto é necessário ler e pesquisar para responder ao seu comando.

- **Deep Research** (`deep-research-preview-04-2026`): para uma consulta típica que exige análise moderada, o agente pode usar cerca de 80 consultas de pesquisa, 250 mil tokens de entrada (~50 a 70% em cache) e 60 mil tokens de saída.
  - **Total estimado**:de US$1,00 a US$ 3,00 por tarefa
- **Deep Research Max** (`deep-research-max-preview-04-2026`): para uma análise detalhada do cenário competitivo ou uma auditoria extensa, o agente pode usar até ~160 consultas de pesquisa, ~900 mil tokens de entrada (~50 a 70% em cache) e ~80 mil tokens de saída.
  - **Total estimado**:de US$3,00 a US$ 7,00 por tarefa

## Considerações sobre segurança

Dar acesso à Web e aos seus arquivos particulares exige uma análise cuidadosa dos riscos de segurança.

- **Injeção de comandos usando arquivos**:o agente lê o conteúdo dos arquivos
  que você fornece. Verifique se os documentos enviados (PDFs, arquivos de texto) são de fontes confiáveis. Um arquivo malicioso pode conter texto oculto projetado para
  manipular a saída do agente.
- **Riscos de conteúdo da Web**:o agente pesquisa na Web pública. Embora implementemos filtros de segurança robustos, há um risco de que o agente encontre e processe páginas da Web maliciosas. Recomendamos que você analise o `citations` fornecido
  na resposta para verificar as fontes.
- **Exfiltração**:tenha cuidado ao pedir para o agente resumir dados internos sensíveis se você também permitir que ele navegue na Web.

## Práticas recomendadas

- **Solicitar desconhecidos**:instrua o agente sobre como lidar com dados ausentes.
  Por exemplo, adicione *"Se números específicos para 2025 não estiverem disponíveis, declare explicitamente que são projeções ou que não estão disponíveis, em vez de estimar"* ao comando.
- **Forneça contexto**:embasar a pesquisa do agente com informações ou restrições diretamente no comando de entrada.
- **Use o planejamento colaborativo**:para consultas complexas, ative o planejamento colaborativo para revisar e refinar o plano de pesquisa antes da execução.
- **Entradas multimodais**:o agente Deep Research aceita entradas multimodais.
  Use com cuidado, porque isso aumenta os custos e o risco de estouro da janela de contexto.

## Limitações

- **Status Beta**: a API Interactions está na versão Beta pública. Os recursos e
  esquemas podem mudar.
- **Ferramentas personalizadas**:no momento, não é possível fornecer ferramentas personalizadas de chamada de função, mas você pode usar servidores MCP (Protocolo de Contexto de Modelo) remotos com o agente de pesquisa detalhada.
- **Resposta estruturada**:no momento, o agente Deep Research não aceita respostas estruturadas.
- **Tempo máximo de pesquisa**:o agente Deep Research tem um tempo máximo de pesquisa de 60 minutos. A maioria das tarefas é concluída em até 20 minutos.
- **Requisito da loja**:a execução do agente usando `background=True` exige
  `store=True`.
- **Pesquisa Google**:a [Pesquisa
  Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pt-br) fica ativada por
  padrão, e [restrições
  específicas](https://ai.google.dev/gemini-api/terms?hl=pt-br#use-restrictions2)
  se aplicam aos resultados embasados.

## A seguir

- Saiba mais sobre a [API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br).
- Saiba como usar seus próprios dados com a ferramenta [Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-29 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-29 UTC."],[],[]]
