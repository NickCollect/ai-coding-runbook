---
source_url: https://ai.google.dev/gemini-api/docs/long-decode?hl=pt-BR
fetched_at: 2026-10-19T05:43:56.464641+00:00
title: "Decodifica\u00e7\u00e3o longa \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Decodificação longa

A decodificação longa permite que o Gemini 4 Argon gere mais de 64 mil tokens para tarefas de raciocínio complexas, até a janela de contexto unificada de 1 milhão de tokens (1.048.576 tokens compartilhados entre entrada, raciocínio e saída). Na API Interactions, você ativa a decodificação longa com execução em segundo plano para que nossos servidores gerem e combinem automaticamente cada salto de 64 mil em uma única interação.

## Como a decodificação longa funciona

Uma única chamada de modelo gera até 64 mil tokens. Quando uma resposta precisa de mais de 64 mil tokens, o servidor a gera em saltos de 64 mil que continuam de onde o salto anterior parou. Cada salto adiciona uma etapa `model_output` a `interaction.steps` no mesmo ID de interação. Assim, você une essas etapas para ler a resposta completa:

1. Você cria uma interação com `background: true` e `max_output_tokens` maior que 65.536, até 1 milhão.
2. O servidor gera o primeiro salto, até 64 mil tokens.
3. O servidor inicia o próximo salto de onde o último parou e repete até que o modelo termine ou use todos os `max_output_tokens`.
4. Você pesquisa a interação ou faz streaming dela para receber o resultado.

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
# 1. Create the background interaction. It returns an ID right away.
ID=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-4-argon",
    "input": "Write a complete, rigorous proof of the prime number theorem.",
    "background": true,
    "generation_config": {"max_output_tokens": 262144, "thinking_level": "high"}
  }' | jq -r '.id')

# 2. Poll until the status is no longer in_progress or queued.
#    The REST response has no output_text field, so join the text of every model_output step.
while true; do
  RESP=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY")
  STATUS=$(echo "$RESP" | jq -r '.status')
  if [[ "$STATUS" != "in_progress" && "$STATUS" != "queued" ]]; then
    echo "$RESP" | jq -r '[.steps[]? | select(.type == "model_output") | .content[]? | select(.type == "text") | .text] | join("")'
    echo "$RESP" | jq '{status, usage}'
    break
  fi
  sleep 5
done
```

## Limites de saída

As interações de streaming e não streaming têm um limite padrão de 64 mil tokens de saída. Portanto, as respostas de até 64 mil tokens não precisam de mudanças no código. Para gerar mais de 64 mil tokens, ative a execução em segundo plano e aumente `max_output_tokens`.

| Como você cria a interação | Limite de saída |
| --- | --- |
| `background: false` (streaming ou não streaming) | 65.536 tokens. Valores maiores que 65.536 retornam um erro 400. A decodificação longa será lançada em breve. |
| `background: true`, `max_output_tokens` não definido | 65.536 tokens |
| `background: true`, `max_output_tokens` maior que 65.536 | Seu `max_output_tokens`, até 1.048.576 menos sua entrada |

## Quando usar a decodificação longa

A maioria das solicitações termina em até 64 mil tokens. Use a decodificação longa somente quando uma resposta precisar de mais raciocínio e saída do que isso.

| Carga de trabalho | Usar decodificação longa? | Por quê? |
| --- | --- | --- |
| Matemática, ciência, pesquisa e provas formais difíceis | Sim | O modelo pode gastar mais de 64 mil tokens para explorar e verificar o raciocínio. |
| As tarefas de programação e agênticas mais difíceis | Sim | Algumas tarefas precisam de mais de 64 mil tokens de raciocínio e código em uma resposta. A maioria das tarefas de programação e agênticas termina com menos de 64 mil. |
| Ferramentas de avaliação que param no limite de saída | Sim | A decodificação longa evita respostas cortadas quando o modelo gasta uma resposta inteira de 64 mil no raciocínio. |
| Chat, perguntas e respostas, resumo, classificação e extração | Não | Essas tarefas terminam com menos de 32 mil tokens. |
| Solicitações de um comprimento fixo, como "escreva um livro de 700 mil palavras" | Não | O modelo não segue metas de comprimento. |
| Agentes que chamam ferramentas em muitos turnos curtos | Não | Cada turno é curto. Grandes saídas em cada turno preenchem a janela de contexto compartilhada rapidamente. |
| Comandos próximos ao limite de entrada | Não | A saída pode usar apenas 1.048.576 tokens menos sua entrada. |
| Solicitações sensíveis à latência | Não | A decodificação longa pode ser executada por vários minutos. |

Definir um `max_output_tokens` alto dá ao modelo espaço para pensar mais em problemas difíceis, mas o modelo ainda decide quanto escrever. Para controlar o esforço de raciocínio usado pelo modelo, defina [`thinking_level`](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br).

## Escolher como executar a decodificação longa

A execução em segundo plano é a maneira mais fácil de executar a decodificação longa na API Interactions. A continuação do lado do cliente, em que o código inicia cada salto, está disponível na API GenerateContent. Ela será lançada em breve na API Interactions como uma opção mais avançada para gerenciar sua própria resiliência.

|  | Execução em segundo plano (API Interactions) | Continuação do lado do cliente (API GenerateContent) |
| --- | --- | --- |
| **Quem inicia cada salto** | Nossos servidores | O SDK de IA generativa do Google ou seu próprio código |
| **Tokens por solicitação** | Seu `max_output_tokens`, em uma interação | 64 mil por stream, 32 mil por solicitação não streaming |
| **Horário da execução** | Até 24 horas | 20 minutos |
| **Armazenamento** | Requer `store: true` | Nada armazenado no servidor. |
| **Ideal para** | A maneira mais fácil de executar a decodificação longa | Controle mais refinado sobre novas tentativas, para que você possa criar seu próprio backoff, tratamento de erros e resiliência |

Para usar a continuação do lado do cliente, consulte [Decodificação longa com a API GenerateContent](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=pt-br).

## Fazer streaming de decodificação longa

Para fazer streaming de saídas e resumos de pensamento à medida que chegam, adicione `stream: true` e `thinking_summaries: "auto"`. Streams longos podem cair, então o cliente precisa se reconectar. Siga o padrão de reconexão no [guia de execução em segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=pt-br). A decodificação longa adiciona estas regras:

- **Salve o ID da interação**:leia-o no evento `interaction.created`.
- **Salve cada `event_id`:** Um `event_id` pode chegar em eventos `interaction.status_update`, não apenas em deltas de texto.
- **Reconecte-se com `last_event_id`:** chame `interactions.get` com `stream: true` e o último `event_id`. O stream continua após esse evento.
- **Leia até o final**:depois de se reconectar, leia o stream até o final antes de verificar o status. O servidor reproduz eventos perdidos, mesmo após a conclusão da interação.
- **Defina tempos limite longos**:defina tempos limite de leitura HTTP de 15 a 20 minutos por stream.
- **Espere a saída em blocos de 5 mil tokens**:após os primeiros 64 mil tokens (cerca de 10 minutos), o stream envia a saída em blocos de cerca de 5 mil tokens. As pausas entre os blocos são normais. A interação não está travada, então mantenha a conexão aberta.

## Status em segundo plano

Uma interação em segundo plano pode ser executada por até 24 horas. Quando o status não for mais `in_progress` ou `queued`, processe o estado terminal usando esta tabela:

| Status | Significado | O que fazer |
| --- | --- | --- |
| `completed` | O modelo terminou. | Una as etapas `model_output` em `steps` e leia `usage`. Para continuar a conversa, transmita o `id` dessa interação como `previous_interaction_id`. |
| `requires_action` | O modelo pediu uma chamada de ferramenta. | Execute a ferramenta. Em seguida, envie o resultado com o `id` dessa interação. |
| `incomplete` | O modelo usou todos os `max_output_tokens`. O texto pode estar vazio se o modelo ainda estiver pensando. | Envie a solicitação novamente com um `max_output_tokens` maior. |
| `failed` | O servidor não conseguiu terminar ou a interação foi executada por mais de 24 horas. | Tente fazer a solicitação novamente. Se ela falhar de novo, compartilhe o `id` da interação com o suporte. |
| `cancelled` | Você cancelou a interação. | Leia `usage` para conferir os tokens faturados. |

Para interromper uma interação em execução, chame `client.interactions.cancel(id=interaction.id)` em Python, `client.interactions.cancel(interaction.id)` em JavaScript ou `POST /v1beta/interactions/{id}/cancel` em REST.

## Definir `max_output_tokens`

`max_output_tokens` define o limite combinado para raciocínio e saída em toda a interação. Diminuir esse valor não faz com que o modelo pense de forma mais concisa, mas corta a resposta mais cedo.

| Sua carga de trabalho | `max_output_tokens` recomendado |
| --- | --- |
| Apps atuais com um limite menor que 32 mil | Aumente para 32.768. A execução em segundo plano não é necessária. |
| Tarefas de programação e agênticas longas | Comece com 65.536 (o padrão). A execução em segundo plano não é necessária. |
| Raciocínio complexo, matemática, ciência e provas difíceis | Defina `background: true` e comece com 262.144, até 1.048.576 menos seus tokens de entrada. |

Para usar menos tokens, diminua `thinking_level`. Use `high` para as tarefas de raciocínio mais difíceis. Use `medium` (o padrão) para a maioria dos trabalhos de programação e agênticos.

## Contar tokens

`interaction.usage` informa os totais em todos os saltos. Leia estes campos: `total_input_tokens`, `total_cached_tokens`, `total_output_tokens`, `total_thought_tokens` e `total_tokens`.

`total_input_tokens` soma os tokens de entrada de cada salto. Cada salto envia o comando e tudo o que foi gerado até o momento de volta ao modelo como entrada. Assim, os mesmos tokens são contados novamente em cada salto posterior. Por exemplo, um comando de 1.000 tokens que produz 200 mil tokens de raciocínio e saída leva quatro saltos:

| Salto | Entrada enviada ao modelo | Tokens de entrada |
| --- | --- | --- |
| 1 | Comando | 1.000 |
| 2 | Comando + salto 1 | 66.536 |
| 3 | Comando + saltos 1 e 2 | 132.072 |
| 4 | Comando + saltos 1 a 3 | 197.608 |
| **Total** |  | **397.216** |

`total_input_tokens` informa cerca de 397 mil tokens (com entradas de salto repetidas automaticamente descontadas em 95% pelo armazenamento em cache implícito), embora o tamanho real do contexto seja de apenas cerca de 201 mil tokens: o comando de 1.000 tokens mais 200 mil tokens de raciocínio e saída.

Durante um stream, os eventos `step.stop` e `interaction.status_update` incluem `usage` (cumulativo para a interação). Leia o valor `usage` mais recente em vez de adicioná-los.

## Noções básicas sobre o faturamento

Você paga por cada token em cada salto, incluindo aqueles que contêm apenas raciocínio.

- **Desconto de cache**:o armazenamento em cache implícito desconta a entrada repetida em cada salto em 95%. A entrada armazenada em cache custa US $0,10 por 1 milhão de tokens em vez de US $2,00 durante o período introdutório.
- **Interações canceladas e com falha**:você paga por todo o trabalho concluído antes do término da interação.

## Solução de problemas

| Sintoma | Causa e correção |
| --- | --- |
| A saída para em 64 mil | `background` é `false` ou `max_output_tokens` não está definido. Defina `background: true` e `max_output_tokens` maior que 65.536. |
| 400: "max\_output\_tokens greater than 65536 is not yet supported with background=false." | A decodificação longa sem execução em segundo plano ainda não está disponível. Defina `background: true`. |
| 400: "store=true is required for background interactions" | A execução em segundo plano precisa de `store: true`. |
| Status `incomplete` com texto vazio | O modelo usou todos os tokens no raciocínio. Aumente `max_output_tokens` ou diminua `thinking_level`. |
| A compactação de contexto começa muito cedo | O framework do agente ou a ferramenta de avaliação lê `total_input_tokens`. Consulte [Contar tokens](#count-tokens). |

## Limitações

- **Não há decodificação longa sem execução em segundo plano**:as interações com `background: false` param em 65.536 tokens. O suporte será lançado em breve.
- **Sem metas de comprimento**:o modelo não segue metas de comprimento de token ou contagem de palavras.

## Próximas etapas

- [Novidades no Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/latest-model?hl=pt-br)
- [Execução em segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=pt-br)
- [Raciocínio](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br)
- [Decodificação longa com a API GenerateContent](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=pt-br)

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-13 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-13 UTC."],[],[]]
