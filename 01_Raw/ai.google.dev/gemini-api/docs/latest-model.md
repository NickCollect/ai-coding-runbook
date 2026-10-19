---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=pt-BR
fetched_at: 2026-10-19T05:33:07.674797+00:00
title: "Novidades do Gemini 4 Argon \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Novidades do Gemini 4 Argon

O Gemini 4 Argon (`gemini-4-argon`) é nosso modelo mais recente e avançado. Ele pode raciocinar por mais tempo sobre problemas difíceis para gerar resultados melhores em tarefas complexas de programação, agentes, matemática e ciências. O Gemini 4 Argon está disponível pela API Gemini e no Google AI Studio.

O Gemini 4 Argon oferece uma janela de contexto unificada de 1 milhão de tokens, decodificação longa de até 1 milhão de tokens e níveis de raciocínio ajustáveis (`low`, `medium`, `high`).

[experiment

Teste no AI Studio

Crie apps do zero com o Gemini 4 Argon e o AI Studio.](https://aistudio.google.com/apps?model=gemini-4-argon&hl=pt-br)
[smart\_toy

Galeria de aplicativos

Brinque e remix apps criados com o Gemini 4 Argon.](https://aistudio.google.com/learn/gemini-4-argon-showcase?hl=pt-br)
[rocket\_launch

Primeiros passos

Comece a usar o Gemini 4 Argon com comandos iniciais.](https://aistudio.google.com/learn/gemini-4-argon?hl=pt-br)

Este guia explica as novidades do Gemini 4 Argon, as mudanças na API, exemplos de código e orientações de migração.

## Novo modelo

| Modelo | ID do modelo | Nível de raciocínio padrão | Preços | Descrição |
| --- | --- | --- | --- | --- |
| Gemini 4 Argon | `gemini-4-argon` | `medium` | Disponível até 30 de novembro de 2026 pelo preço inicial de US $2/1 milhão de tokens de entrada e US $10/1 milhão de tokens de saída (US$ 4/1 milhão de entrada e US $20/1 milhão de saída depois disso). Consulte os [preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br) para mais detalhes. | Nosso modelo mais avançado, criado para resolver os problemas mais difíceis com profundidade e precisão em tarefas de engenharia de software e trabalho intelectual do mundo real. |

Para mais detalhes, consulte a [página do modelo Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=pt-br). Para detalhes sobre os preços iniciais, consulte a [seção de preços](#pricing) mais adiante nesta página ou a [página de preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#gemini-4-argon).

## Guia de início rápido

Use o exemplo a seguir para enviar uma solicitação para `gemini-4-argon` com o `thinking_level` padrão recomendado (`medium`) e um limite de token de saída de 64K:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Write a three.js script that renders a realistic 3D black hole with gravitational lensing."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-4-argon",
  input: "Write a three.js script that renders a realistic 3D black hole with gravitational lensing.",
});

console.log(interaction.output_text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-4-argon",
    "input": "Write a three.js script that renders a realistic 3D black hole with gravitational lensing."
  }'
```

## Novidades do Gemini 4 Argon

- **Limite unificado de 1 milhão de tokens de entrada e saída**:a entrada, o processamento e a saída compartilham uma janela de 1.048.576 tokens.
- **Decodificação longa**:agora, uma única resposta pode ultrapassar 64 mil tokens, até 1 milhão de tokens menos sua entrada. Consulte [Decodificação longa](https://ai.google.dev/gemini-api/docs/long-decode?hl=pt-br).
- **A compreensão agêntica de vídeos está em disponibilidade geral**:a [compreensão agêntica de vídeos](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pt-br#agentic-video-understanding) já está em disponibilidade geral.
- **Disponível nos Agentes Gerenciados**:o [agente do Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pt-br) nos Agentes Gerenciados do Gemini agora é compatível com o Gemini 4 Argon.

Para ver as especificações completas, consulte a [página do modelo Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=pt-br). Para mais detalhes, consulte a [página de preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#gemini-4-argon).

## Saída maior e decodificação longa

O Gemini 4 Argon pode pensar mais sobre problemas difíceis de matemática, ciências e programação.

- **Use `thinking_level` para controlar a profundidade do raciocínio**:o nível de pensamento decide a profundidade do raciocínio do modelo antes de responder. `max_output_tokens` é um limite rígido: a resposta é interrompida quando o pensamento e a saída juntos o atingem. Portanto, defina um valor alto o suficiente para que a resposta não seja cortada.
- **Gere até 1 milhão de tokens com a execução em segundo plano**:use a execução em segundo plano com `max_output_tokens` maior que 65.536 para permitir que uma única resposta ultrapasse 64 mil tokens, até 1 milhão de tokens. O modelo gera respostas longas em saltos de até 64 mil tokens, e cada salto continua de onde o anterior parou. Com a execução em segundo plano, nossos servidores executam esses saltos de continuação para você. Como cada salto adiciona uma etapa `model_output` a `interaction.steps`, junte o texto de todas as etapas `model_output` quando a interação for concluída.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Write a complete, rigorous proof of the prime number theorem.",
    background=True,
    generation_config={
        "max_output_tokens": 262144,
        "thinking_level": "high",
    },
)

while interaction.status in ("in_progress", "queued"):
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Each hop adds a model_output step, so join the text of all of them.
text = "".join(
    content.text
    for step in interaction.steps
    if step.type == "model_output"
    for content in step.content
    if content.type == "text"
)
print(text)
print("Status:", interaction.status)
print("Usage:", interaction.usage)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
  model: "gemini-4-argon",
  input: "Write a complete, rigorous proof of the prime number theorem.",
  background: true,
  generation_config: {
    max_output_tokens: 262144,
    thinking_level: "high",
  },
});

while (interaction.status === "in_progress" || interaction.status === "queued") {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  interaction = await client.interactions.get(interaction.id);
}

// Each hop adds a model_output step, so join the text of all of them.
const text = interaction.steps
  .filter((step) => step.type === "model_output")
  .flatMap((step) => step.content ?? [])
  .filter((content) => content.type === "text")
  .map((content) => content.text)
  .join("");
console.log(text);
console.log("Status:", interaction.status);
console.log("Usage:", interaction.usage);
```

### REST

```
ID=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-4-argon",
    "input": "Write a complete, rigorous proof of the prime number theorem.",
    "background": true,
    "generation_config": {
      "max_output_tokens": 262144,
      "thinking_level": "high"
    }
  }' | jq -r '.id')

while true; do
  RESP=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY")
  STATUS=$(echo "$RESP" | jq -r '.status')
  if [[ "$STATUS" != "in_progress" && "$STATUS" != "queued" ]]; then
    echo "$RESP" | jq -r '[.steps[]? | select(.type == "model_output") | .content[]? | select(.type == "text") | .text] | join("")'
    break
  fi
  sleep 5
done
```

A execução em segundo plano é a maneira mais fácil de executar uma decodificação longa. Ele executa o loop de continuação do lado do servidor até que o modelo termine ou alcance `max_output_tokens`. Se você precisar de um controle mais detalhado sobre novas tentativas, espera e tratamento de erros (ou não quiser que suas interações sejam armazenadas), use a continuação do lado do cliente na [API GenerateContent](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=pt-br). A continuação do lado do cliente também será lançada em breve na API Interactions. Para streaming, reconexão, contagem de tokens e quando usar a decodificação longa, consulte o [guia de decodificação longa](https://ai.google.dev/gemini-api/docs/long-decode?hl=pt-br).

### Como definir limites de tokens de saída

`max_output_tokens` define o total de tokens de pensamento e saída para uma resposta. Defina um valor alto o suficiente para que o raciocínio não interrompa a resposta e baixo o suficiente para limitar os gastos quando um comando difícil usar todo o valor.

Use estes valores como ponto de partida:

- **Tarefas padrão**:mantenha o padrão de 65.536 ou não defina nenhum valor.
- **Apps com um limite inferior a 32 mil**:aumente `max_output_tokens` para pelo menos 32.768. O Gemini 4 Argon pode usar mais do limite para pensar do que os modelos anteriores. Para usar menos tokens, diminua o nível de raciocínio.
- **Raciocínio e programação complexos**:defina `background: true` e `max_output_tokens` como 131.072 ou 262.144, até 1.048.576 menos os tokens de entrada.

## Entender os níveis de raciocínio

O [nível de raciocínio](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br) é o principal controle sobre qualidade, latência e uso de tokens no Gemini 4 Argon:

| Nível de raciocínio | Uso de tokens | Quando usar |
| --- | --- | --- |
| `low` | Menos tokens, menor latência | Tarefas mais simples e trabalho sensível a custos. Também funciona para tarefas de análise e escrita que exigem um raciocínio simples. A qualidade pode cair em tarefas difíceis. |
| `medium` (padrão) | Equilibrada | Recomendado para a maioria das tarefas, incluindo código complexo e casos de uso agênticos. |
| `high` | Mais tokens, primeiro token mais lento | Raciocínio complexo, matemática e ciências avançadas e as tarefas mais difíceis de código ou agente. Combina bem com a decodificação longa para saídas longas. |

Execute as avaliações nos três níveis e escolha o mais baixo que atenda ao seu padrão de qualidade. Para saber mais, consulte o [guia de pensamento](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    generation_config={
        "thinking_level": "medium"  # Balanced reasoning effort for complex tasks
    }
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-4-argon",
  input: "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
  generation_config: {
    thinking_level: "medium", // Balanced reasoning effort for complex tasks
  },
});

console.log(interaction.output_text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-4-argon",
    "input": "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    "generation_config": {
      "thinking_level": "medium"
    }
  }'
```

## Gemini 4 Argon nos agentes gerenciados

O [agente do Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pt-br) nos Agentes Gerenciados do Gemini é compatível com o Gemini 4 Argon. Para usá-lo, defina o modelo em `agent_config`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input=(
        "Audit https://web.dev for performance, Core Web Vitals, and SEO. "
        "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. "
        "Check search indexing with Google Search for site:web.dev. "
        "Format the output as a side-by-side scorecard table with prioritized fixes."
    ),
    environment="remote",
    agent_config={
        "type": "antigravity",
        "model": "gemini-4-argon",
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  agent: "antigravity-preview-09-2026",
  input:
    "Audit https://web.dev for performance, Core Web Vitals, and SEO. " +
    "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. " +
    "Check search indexing with Google Search for site:web.dev. " +
    "Format the output as a side-by-side scorecard table with prioritized fixes.",
  environment: "remote",
  agent_config: {
    type: "antigravity",
    model: "gemini-4-argon",
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
    "agent": "antigravity-preview-09-2026",
    "input": "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google'\''s PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
    "environment": "remote",
    "agent_config": {
      "type": "antigravity",
      "model": "gemini-4-argon"
    }
  }'
```

Para mais opções, consulte [Seleção de modelo](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pt-br#model-selection) no guia do agente do Antigravity.

## Checklist de migração

```
  `/gemini-api-dev migrate my app to Gemini 4 Argon`
```

### Migrar para o gemini-4-argon

- **Atualizar o ID do modelo**:mude a string do modelo de destino para `gemini-4-argon`.
- **Revise `max_output_tokens`**:se você definiu esse valor explicitamente, considere aumentá-lo. Recomendamos pelo menos 32.768, já que o Gemini 4 Argon pode gastar mais do limite em raciocínio.
- **Configurar o nível de pensamento**:escolha `low`, `medium` (padrão) ou `high` e teste sua carga de trabalho nos três.
- **Não use o armazenamento em cache de contexto explícito**:o armazenamento em cache explícito (`cachedContents` / `caches.create`) não é compatível com o Gemini 4 Argon. Remova das suas solicitações as chamadas que criam ou fazem referência a `cached_content`. O [armazenamento em cache implícito](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br) é ativado por padrão para comandos de pelo menos 4.096 tokens e desconta em 95% os tokens de entrada armazenados em cache em ocorrências em cache.
- **Remova os parâmetros de amostragem**:remova `temperature`, `top_p` e `top_k` das suas solicitações. Se fornecidos, eles serão ignorados.
- **Use a execução em segundo plano para saídas longas**:para tarefas que precisam de mais de 64 mil tokens, defina `background` como verdadeiro e `max_output_tokens` como um valor maior que 65.536.
- **Aumente os tempos limite do cliente**:os comandos fixos podem levar vários minutos. Use a execução em segundo plano ou defina os tempos limite do cliente HTTP para pelo menos 15 minutos.
- **Manter o estado da conversa no servidor**:use `previous_interaction_id` para conversas com várias interações e chamadas de função.

## Preços

O Gemini 4 Argon está disponível com preço inicial até 30 de novembro de 2026:

- **Tokens de entrada**:US $2,00 por 1 milhão de tokens (US$ 4,00 a partir de 1º de dezembro de 2026)
  - **Tokens de entrada em cache**:o armazenamento em cache implícito reduz o custo da entrada em cache em 95%, para US $0,10 por 1 milhão de tokens (US$ 0,20 a partir de 1º de dezembro de 2026).
- **Tokens de saída, incluindo tokens de raciocínio**:US $10,00 por 1 milhão de tokens (US$ 20,00 a partir de 1º de dezembro de 2026)

O Gemini 4 Argon não está disponível no nível sem custo financeiro. Para ver os níveis de preços completos, consulte a [página de preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#gemini-4-argon).

## Outros modelos

- [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=pt-br)
- [Gemini 3.6 Flash e 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=pt-br)
- [Ver todos os modelos](https://ai.google.dev/gemini-api/docs/models?hl=pt-br)

## A seguir

- Leia o [guia de decodificação longa](https://ai.google.dev/gemini-api/docs/long-decode?hl=pt-br) para streaming, reconexão e contagem de tokens.
- Saiba como os níveis de raciocínio e os resumos de pensamento funcionam no [guia de raciocínio](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br).
- Saiba mais sobre jobs de longa duração no [guia de execução em segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=pt-br).
- Teste e refine comandos no [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-16 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-16 UTC."],[],[]]
