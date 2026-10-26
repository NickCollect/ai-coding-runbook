---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-BR
fetched_at: 2026-10-26T05:54:02.567000+00:00
title: "API Interactions \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# API Interactions

A API Interactions é a melhor maneira de criar com modelos do Gemini e agentes. Desde junho de 2026, ela está disponível para todos e é recomendada para todos os novos projetos. Embora agora seja considerada legada, a API
original
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=pt-br)ainda tem suporte total.

## Por que usar a API Interactions?

- **Interface universal para todos os aplicativos**: projetada como a interface padrão
  para todos os casos de uso, incluindo geração de texto de uma única rodada,
  compreensão multimodal, saídas estruturadas, orquestração de ferramentas e
  fluxos de trabalho de agentes.
- **API única para modelos e agentes**: um endpoint e padrão unificados para
  chamar modelos padrão do Gemini e agentes especializados diretamente (como
  Deep Research e agentes gerenciados personalizados).
- **Novos recursos prontos para uso**: recursos como estado de conversa opcional do lado do servidor
  usando `previous_interaction_id`, etapas de execução observáveis
  para depuração e renderização da interface e execução[em segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=pt-br) para tarefas de longa duração
  usando `background=true`.
- **Custo menor com taxas de ocorrência em cache mais altas**: ao usar conversas multiturno, o gerenciamento de estado opcional do lado do servidor permite um armazenamento em cache de contexto mais eficiente em todas as rodadas, reduzindo os custos de token.
- **Onde os novos recursos são lançados**: no futuro, todos os novos modelos, recursos multimodais
  capacidades, ferramentas e recursos de agentes serão lançados na API Interactions.

Por padrão, a API Interactions armazena solicitações para que você possa aproveitar os recursos de gerenciamento de estado do lado do servidor usando `previous_interaction_id`. Você pode ativar o comportamento sem estado definindo `store=false`. Consulte a seção de [retenção de dados](#data-storage-retention) para
detalhes.

## Primeiros passos

- **Configure seu agente de programação**: conecte-se ao **MCP do Gemini Docs** e instale
  a habilidade `gemini-api-dev` para dar ao seu assistente acesso direto aos
  documentos mais recentes para desenvolvedores e às práticas recomendadas. Para conferir as etapas detalhadas, consulte o
  [guia Configurar seu agente de programação](https://ai.google.dev/gemini-api/docs/coding-agents?hl=pt-br).
- **Migre de `generateContent`**: se você tiver uma integração,
  siga o [guia de migração](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=pt-br) para
  fazer a transição para a API Interactions.
- **Comece**: siga as etapas no guia [Introdução à API Interactions
  guide](https://ai.google.dev/gemini-api/docs/get-started?hl=pt-br).

### Guias de recursos

Conheça os recursos específicos da API Interactions nestes guias. Você pode usar o botão de alternância nessas páginas para mudar entre a API generateContent e a API Interactions:

- [Geração de texto](https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-br)
- [Geração de imagens](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br)
- [Compreensão de imagens](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pt-br)
- [Compreensão de áudio](https://ai.google.dev/gemini-api/docs/audio?hl=pt-br)
- [Compreensão do vídeo](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pt-br)
- [Processamento de documentos](https://ai.google.dev/gemini-api/docs/document-processing?hl=pt-br)
- [Chamadas de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br)
- [Resposta estruturada](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br)
- [Agente Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br)
- [Inferência flexível](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pt-br)
- [Inferência de prioridade](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pt-br)

## Como a API Interactions funciona

A API Interactions é centrada em um recurso principal: o [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=pt-br#Resource:Interaction). Uma `Interaction` representa uma rodada completa em uma conversa ou tarefa. Ela funciona como um registro de sessão, contendo todo o histórico de uma interação como uma sequência cronológica de **etapas de execução**. Essas etapas incluem ideias do modelo, chamadas e resultados de ferramentas do lado do servidor ou do cliente (como `function_call` e `function_result`) e a `model_output` final. O recurso armazenado (recuperado por `interactions.get`) também inclui etapas `user_input` para contexto completo, embora a resposta `interactions.create` retorne apenas etapas geradas pelo modelo.

Ao fazer uma chamada para
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=pt-br#CreateInteraction), você está
criando um novo `Interaction` recurso:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me a short story about a time-traveling lighthouse."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Tell me a short story about a time-traveling lighthouse.",
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Tell me a short story about a time-traveling lighthouse."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Tell me a short story about a time-traveling lighthouse."),
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
    "model": "gemini-3.8-flash",
    "input": "Tell me a short story about a time-traveling lighthouse."
  }'
```

### Gerenciamento de estado do lado do servidor

Você pode usar o `id` de uma interação concluída em uma chamada subsequente usando o
`previous_interaction_id` parâmetro para continuar a conversa. O servidor usa esse ID para recuperar o histórico de conversas, evitando que você precise reenviar todo o histórico de conversas:

### Python

```
from google import genai

client = genai.Client()

# 1. First turn
turn1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hi, my name is Phil."
)

# 2. Second turn (chained using previous_interaction_id)
turn2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is my name?",
    previous_interaction_id=turn1.id
)

print(turn2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

// 1. First turn
const turn1 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Hi, my name is Phil.",
});

// 2. Second turn (chained using previous_interaction_id)
const turn2 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "What is my name?",
  previous_interaction_id: turn1.id,
});

console.log(turn2.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

// 1. First turn
Interaction turn1 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("Hi, my name is Phil."))
                    .build()))
        .interaction()
        .get();

// 2. Second turn (chained using previousInteractionId)
Interaction turn2 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("What is my name?"))
                    .previousInteractionId(turn1.id().get())
                    .build()))
        .interaction()
        .get();

System.out.println(turn2.outputText().orElse(""));
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

    // 1. First turn
    turn1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Hi, my name is Phil."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // 2. Second turn (chained using PreviousInteractionID)
    turn2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-flash"),
            Input:                 interactions.NewInteractionsInput("What is my name?"),
            PreviousInteractionID: turn1.Interaction.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if turn2.Interaction.OutputText != nil {
        fmt.Println(*turn2.Interaction.OutputText)
    }
}
```

### REST

```
# Replace PREVIOUS_INTERACTION_ID with the id returned from the first turn
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is my name?",
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID"
  }'
```

O parâmetro `previous_interaction_id` preserva apenas o histórico da conversa (entradas e saídas) usando `previous_interaction_id`. Os outros parâmetros têm **escopo de interação** e se aplicam apenas à interação específica que você está gerando:

- `tools`
- `system_instruction`
- `generation_config` (incluindo `thinking_level`, `temperature` etc.)

Isso significa que você precisa especificar esses parâmetros novamente em cada nova interação se quiser que eles sejam aplicados. Esse gerenciamento de estado do lado do servidor é opcional. Você também pode operar no modo sem estado enviando o histórico completo da conversa em cada solicitação.

### Armazenamento e retenção de dados

Por padrão, a API armazena todos os objetos de interação (`store=true`) para
simplificar o uso dos recursos de gerenciamento de estado do lado do servidor (com
`previous_interaction_id`), [a execução em segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=pt-br) (usando `background=true`) e
fins de observabilidade.

- **Nível pago**: o sistema retém interações por **55 dias**.
- **Nível sem custo financeiro**: o sistema retém interações por **1 dia**.

Se você não quiser isso, defina `store=false` na sua solicitação. Esse controle é separado do gerenciamento de estado. Você pode desativar o armazenamento de qualquer interação. No entanto, observe que
`store=false` é incompatível com [a execução em segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=pt-br) e impede o uso de
`previous_interaction_id` para rodadas subsequentes.

Para projetos de nível pago, é possível configurar a janela de retenção no
[AI Studio](https://aistudio.google.com/logs?hl=pt-br) para marcar automaticamente os registros para
exclusão do armazenamento do projeto após 7, 14, 28 ou 55 dias. Uma retenção mais curta pode afetar a recuperação de conversas anteriores.

Você pode excluir interações armazenadas a qualquer momento usando o
[`delete`](https://ai.google.dev/api/interactions-api?hl=pt-br#deleteInteraction) método de maneira programática,
que exige o ID da interação. Também é possível visualizar e gerenciar registros de interações armazenadas, incluindo a exclusão do armazenamento do projeto, no
[AI Studio](https://aistudio.google.com/logs?hl=pt-br).

Após o período de retenção expirar, seus dados serão excluídos automaticamente.

Os objetos de interações são processados de acordo com os [termos](https://ai.google.dev/gemini-api/terms?hl=pt-br).

### Visualizar interações no AI Studio

A API armazena solicitações de API Interactions executadas com `store=true` para projetos no nível pago. É possível visualizá-las diretamente na
[página "Registros" do Google AI Studio](https://aistudio.google.com/logs?hl=pt-br). Consulte o
[guia de registros](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pt-br) para mais informações.

## Práticas recomendadas

- **Taxa de acerto de cache**: o armazenamento em cache implícito é compatível com os modos com e
  sem estado (consulte o
  [guia de início rápido](https://ai.google.dev/gemini-api/docs/get-started?hl=pt-br#4_multi-turn_conversations)). O uso de `previous_interaction_id` (com estado) para continuar conversas permite que o sistema utilize mais facilmente o armazenamento em cache implícito para o histórico da conversa, o que melhora a performance e reduz os custos.
- **Interações de mixagem**: você tem a flexibilidade de misturar e combinar interações de agentes e
  modelos em uma conversa. Por exemplo, você pode usar um agente especializado, como o agente Deep Research, para a coleta inicial de dados e, em seguida, usar um modelo padrão do Gemini para tarefas de acompanhamento, como resumir ou reformatar, vinculando essas etapas ao `previous_interaction_id`.

## Modelos e agentes compatíveis

| Nome do modelo | Tipo | ID do modelo |
| --- | --- | --- |
| Gemini 4 Argon | Modelo | `gemini-4-argon` |
| Gemini 3.8 Flash | Modelo | `gemini-3.8-flash` |
| Gemini 3.6 Flash | Modelo | `gemini-3.6-flash` |
| Pré-lançamento do Gemini 3.1 Pro | Modelo | `gemini-3.1-pro-preview` |
| Gemini 3.5 Flash Lite | Modelo | `gemini-3.5-flash-lite` |
| Gemini 3.1 Flash-Lite | Modelo | `gemini-3.1-flash-lite` |
| Pré-lançamento do Gemini 3 Flash | Modelo | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | Modelo | `gemini-2.5-pro` |
| Gemini 2.5 Flash | Modelo | `gemini-2.5-flash` |
| Gemini 2.5 Flash Lite | Modelo | `gemini-2.5-flash-lite` |
| Gemini 3 Pro Image | Modelo | `gemini-3-pro-image` |
| Gemini 3.1 Flash Image | Modelo | `gemini-3.1-flash-image` |
| Pré-lançamento do Gemini 3.1 Flash TTS | Modelo | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | Modelo | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | Modelo | `gemma-4-26b-a4b-it` |
| Lyria 3.5 | Modelo | `lyria-3.5` |
| Pré-lançamento do Lyria 3 Clip | Modelo | `lyria-3-clip-preview` |
| Pré-lançamento do Lyria 3 Pro | Modelo | `lyria-3-pro-preview` |
| Pré-lançamento do Deep Research | Agente | `deep-research-preview-04-2026` |
| Pré-lançamento do Deep Research | Agente | `deep-research-max-preview-04-2026` |
| Pré-lançamento do Antigravity | Agente | `antigravity-preview-09-2026` |

## SDKs

Você pode usar a versão mais recente dos SDKs do Google GenAI para acessar a API Interactions.

- No Python, esse é o pacote `google-genai` da versão `2.3.0` em diante.
- No JavaScript, esse é o pacote `@google/genai` da versão `2.3.0` em diante.
- No Go, esse é o pacote `google.golang.org/genai`.
- No Java, esse é o pacote `com.google.genai:google-genai`.

Saiba mais sobre como instalar os SDKs na
[página de bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=pt-br).

## Limitações

- **MCP remoto**: o Gemini 3 não oferece suporte ao MCP remoto. Esse recurso será lançado em breve.
- **Compatibilidade de modelos de várias rodadas**: ao misturar modelos diferentes em uma
  conversa (com ou sem estado), os modelos subsequentes precisam oferecer suporte
  às modalidades de saída dos modelos anteriores como entrada. Por exemplo, se você gerar uma imagem usando `gemini-3.1-flash-image`, não será possível continuar essa conversa com um modelo que não aceite entradas de imagem (como um modelo somente de texto ou um modelo de geração de música como o Lyria).

Os seguintes recursos são compatíveis com a
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=pt-br) API, mas **ainda não
estão disponíveis** na API Interactions:

- **[API em lote](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br)**
- **[Chamada de função automática (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=pt-br#automatic_function_calling_python_only)**
- **[Armazenamento em cache explícito](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br)**: o armazenamento em cache implícito do lado do servidor está disponível na API Interactions
  usando `previous_interaction_id`.

## Feedback

Seu feedback é fundamental para o desenvolvimento da API Interactions.
Compartilhe suas ideias, informe bugs ou solicite recursos no
[Fórum da comunidade de desenvolvedores do Google AI](https://discuss.ai.google.dev/c/gemini-api/4?hl=pt-br).

## A seguir

- Teste o [notebook de início rápido da API Interactions](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=pt-br).
- Saiba mais sobre o [agente Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-15 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-15 UTC."],[],[]]
