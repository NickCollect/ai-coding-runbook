---
source_url: https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=pt-BR
fetched_at: 2026-06-01T06:04:50.372630+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Raciocínio do Gemini

Os modelos das séries [Gemini 3 e 2.5](https://ai.google.dev/gemini-api/docs/models?hl=pt-br) usam um
"processo de raciocínio" que melhora significativamente as habilidades de raciocínio e planejamento em várias etapas, tornando-os altamente eficazes para tarefas complexas, como
programação, matemática avançada e análise de dados.

Quando você usa um modelo de raciocínio, o Gemini raciocina internamente antes de responder. A API Interactions mostra esse raciocínio por meio de etapas `thought`, etapas dedicadas que aparecem cronologicamente ao lado de chamadas de função, entradas do usuário ou saídas do modelo na matriz `steps`.

Cada etapa de raciocínio contém dois campos:

| Campo | Obrigatório | Descrição |
| --- | --- | --- |
| `signature` | ✅ Sim | Uma representação criptografada do estado de raciocínio interno do modelo. Sempre presente, mesmo quando o modelo realiza um raciocínio mínimo. |
| `summary` | ❌ Não | Uma matriz de conteúdo (texto e/ou imagens) que resume o raciocínio. Pode estar vazia dependendo da configuração [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=pt-br), se o modelo realizou raciocínio suficiente ou do tipo de conteúdo (por exemplo, latentes de imagem podem não ter resumos de texto). |

## Interações com raciocínio

Iniciar uma interação com um modelo de raciocínio é semelhante a qualquer outra solicitação de interação. Especifique um dos [modelos com suporte de raciocínio](#thinking-levels) no campo `model`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## Resumos de raciocínio

Os resumos de raciocínio fornecem insights sobre o processo de raciocínio interno do modelo.
Por padrão, apenas a saída final é retornada. É possível ativar resumos de raciocínio com `thinking_summaries`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

Um bloco de raciocínio pode conter **apenas uma assinatura sem resumo** nestes casos:

- Solicitações simples, em que o modelo não raciocinou o suficiente para gerar um resumo
- `thinking_summaries: "none"`, em que os resumos são explicitamente desativados
- Alguns tipos de conteúdo de raciocínio, como imagens, podem não ter resumos de texto

O código sempre precisa processar blocos de raciocínio em que `summary` está vazio ou ausente.

## Streaming com raciocínio

Use o streaming para receber resumos de raciocínio incrementais durante a geração.
Os blocos de raciocínio são entregues usando eventos enviados pelo servidor (SSE, na sigla em inglês) com dois tipos de delta distintos:

| Tipo de delta | Contém | Quando o envio é feito |
| --- | --- | --- |
| `thought_summary` | Conteúdo de resumo de texto ou imagem | Um ou mais deltas com resumo incremental |
| `thought_signature` | A assinatura criptográfica | o último delta antes de `step.stop` |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

A resposta de streaming usa eventos enviados pelo servidor (SSE) e é composta de etapas e eventos, por exemplo:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3-flash-preview"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## Controlar o raciocínio

Os modelos do Gemini se envolvem no raciocínio dinâmico por padrão, ajustando automaticamente a quantidade de esforço de raciocínio com base na complexidade da solicitação. É possível controlar esse comportamento usando o parâmetro `thinking_level`.

| Modelo | Raciocínio padrão | Níveis aceitos |
| --- | --- | --- |
| gemini-3.1-pro-preview | Ativado (alto) | baixo, médio, alto |
| gemini-3-flash-preview | Ativado (alto) | mínimo, baixo, médio, alto |
| gemini-3-pro-preview | Ativado (alto) | baixo, alto |
| gemini-2.5-pro | Ativado | baixo, médio, alto |
| gemini-2.5-flash | Ativado | baixo, médio, alto |
| gemini-2.5-flash-lite | Desativado | baixo, médio, alto |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## Assinaturas de raciocínio

As assinaturas de raciocínio são representações criptografadas do raciocínio interno do modelo. Elas são necessárias para manter a continuidade do raciocínio em interações de várias etapas.

A API Interactions simplifica muito o processamento de assinaturas de raciocínio em comparação com a API `generateContent`.

### Modo com estado (recomendado)

Por padrão, quando você usa a API Interactions no modo com estado (definindo `store: true` e transmitindo o `previous_interaction_id` em turnos subsequentes), o servidor gerencia automaticamente o estado da conversa, incluindo todos os blocos e assinaturas de raciocínio. Nesse modo, você não precisa fazer nada em relação às assinaturas. Elas são processadas totalmente no lado do servidor.

### Modo sem estado

Se você estiver gerenciando o estado da conversa (modo sem estado) e transmitindo o histórico completo de entradas e saídas em cada solicitação:

- Você **PRECISA** sempre reenviar todos os blocos `thought` exatamente como foram recebidos do modelo.
- Você **NÃO** deve remover ou modificar blocos de raciocínio do histórico, porque eles contêm as assinaturas necessárias para que o modelo continue o raciocínio.
- Ao mudar de modelo em uma sessão, ainda é necessário reenviar os blocos de raciocínio do modelo anterior. O back-end gerencia a compatibilidade.

## Preços

Quando o raciocínio está ativado, o preço da resposta é a soma dos tokens de saída e de raciocínio. É possível acessar o número total de tokens de raciocínio gerados no campo `total_thought_tokens`.

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

Os modelos de raciocínio geram raciocínios completos para melhorar a qualidade da resposta final
e, em seguida, resumos de saída para fornecer insights sobre o
processo de raciocínio. O preço é baseado nos tokens de raciocínio completos que o modelo precisa gerar, embora apenas o resumo seja gerado pela API.

Saiba mais sobre tokens no guia [Contagem de tokens](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=pt-br).

## Práticas recomendadas

Use modelos de raciocínio de maneira eficiente seguindo estas diretrizes.

- **Analisar o raciocínio**: analise os resumos de raciocínio para entender falhas e melhorar os comandos.
- **Controlar o orçamento de raciocínio**: peça ao modelo para pensar menos em saídas longas para economizar tokens.
- **Tarefas simples**: use o raciocínio mínimo para recuperação de fatos ou classificação (por exemplo, "Onde a DeepMind foi fundada?").
- **Tarefas moderadas**: use o raciocínio padrão para comparar conceitos ou raciocínio criativo (por exemplo, compare carros elétricos e híbridos).
- **Tarefas complexas**: use o raciocínio máximo para programação avançada, matemática ou planejamento em várias etapas (por exemplo, resolva problemas de matemática AIME).

## A seguir

- [Geração de texto](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=pt-br): respostas de texto básicas
- [Chamada de função](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pt-br): conectar-se a ferramentas
- [Guia do Gemini 3](https://ai.google.dev/gemini-api/docs/interactions/gemini-3?hl=pt-br): recursos específicos do modelo

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-28 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-28 UTC."],[],[]]
