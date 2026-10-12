---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=pt-BR
fetched_at: 2026-10-12T07:08:55.522760+00:00
title: "Combinar ferramentas integradas e chamadas de fun\u00e7\u00e3o \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Combinar ferramentas integradas e chamadas de função

O Gemini permite a combinação de [ferramentas integradas](https://ai.google.dev/gemini-api/docs/tools?hl=pt-br), como
o `google_search`, e a [chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br)
(também conhecida como *ferramentas personalizadas*) em uma única interação, preservando e expondo
o histórico de contexto das chamadas de ferramentas. As combinações de ferramentas integradas e personalizadas permitem fluxos de trabalho complexos e de agentes em que, por exemplo, o modelo pode se basear em dados da Web em tempo real antes de chamar sua lógica de negócios específica.

Confira um exemplo que ativa combinações de ferramentas integradas e personalizadas com
`google_search` e uma função personalizada `getWeather`:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");

Function customFunc =
    Function.builder()
        .name("get_user_location")
        .description("Retrieves user current location.")
        .parameters(parameters)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What is the weather like where I am right now?"))
        .tools(Arrays.asList(customFunc, new GoogleSearch()))
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

    customFunc := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_user_location"),
        Description: genai.Ptr("Retrieves user current location."),
        Parameters: map[string]any{
            "type": "object",
        },
    })

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("What is the weather like where I am right now?"),
            Tools: []interactions.Tool{
                customFunc,
                interactions.NewTool(interactions.GoogleSearch{}),
            },
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
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "model": "gemini-3.8-flash",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }
  ]
}'
```

## Como funciona

Os modelos do Gemini 3 usam a *circulação de contexto de ferramentas* para ativar combinações de ferramentas integradas e personalizadas. A circulação do contexto da ferramenta permite preservar e
expor o contexto das ferramentas integradas e compartilhá-lo com ferramentas personalizadas na mesma
interação.

### Ativar a combinação de ferramentas

- Inclua o [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br#function-declarations), além das ferramentas integradas que você quer usar, para acionar o comportamento de combinação.

### Etapas retornadas pela API

Em uma resposta de interação, a API retorna etapas separadas para chamadas de ferramentas integradas e de funções (ferramentas personalizadas):

- **Etapas da ferramenta integrada**: a API gerencia essas etapas automaticamente, preservando o contexto em todas as interações.
- **Etapas de chamada de função**: a API retorna `function_call` etapas para suas funções personalizadas. Você executa a função e fornece o resultado de volta.

### Campos críticos nas etapas retornadas

Alguns campos nas etapas retornadas são essenciais para manter o contexto da ferramenta e permitir combinações de ferramentas:

- **`id`**: encontrado nas etapas `function_call` e `function_response`. Um identificador exclusivo que mapeia uma chamada para a resposta dela.
- **`signature`**: encontrado nas etapas `thought`, bem como em todas as etapas de chamada de ferramenta (por exemplo, `function_call`) e resultado (por exemplo, `function_response`) para modelos do Gemini 3 e versões mais recentes. Esse contexto criptografado permite a **circulação do contexto da ferramenta** nas interações.

**Gerenciar esses campos**:

- **Modo com estado (recomendado)**: quando você usa `previous_interaction_id`, o servidor processa automaticamente os campos `id` e `signature`.
- **Modo sem estado**: ao gerenciar o histórico de conversas manualmente, transmita os campos `id` e `signature` de volta ao modelo em solicitações subsequentes para validar a autenticidade e manter o contexto. Os SDKs oficiais fazem isso automaticamente se você transmitir o objeto de resposta completo de volta ao histórico.

### Dados específicos da ferramenta

Algumas ferramentas integradas retornam argumentos de dados visíveis para o usuário específicos do tipo de ferramenta.

| Ferramenta | Argumentos de chamada de ferramenta visíveis ao usuário (se houver) | Resposta da ferramenta visível para o usuário (se houver) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` URLs a serem pesquisados | `status`: status de navegação `retrieved_url`: URLs navegados |
| **file\_search** | Nenhum | Nenhum |

## Tokens e preços

As partes de chamadas de função integradas em solicitações são contabilizadas em `prompt_token_count`. Como essas etapas intermediárias da ferramenta agora estão visíveis e são retornadas para você, elas fazem parte do histórico da conversa. Isso só acontece com *solicitações*, não com *respostas*.

A ferramenta Pesquisa Google é uma exceção a essa regra. A Pesquisa Google já aplica o próprio modelo de preços no nível da consulta, então os tokens não são cobrados duas vezes. Consulte a página [Preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br).

Leia a página [Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br) para mais informações.

## Limitações

- Use o modo `validated` (o modo `auto` não é compatível) quando a circulação de contexto da ferramenta estiver ativada.
- Ferramentas integradas, como o `google_search`, dependem de informações de localização e hora atual. Portanto, se o `system_instruction` ou o `function_declaration.description` tiver informações conflitantes de localização e hora, o recurso de combinação de ferramentas poderá não funcionar bem.

## Ferramentas compatíveis

A circulação padrão de contexto de ferramentas se aplica a ferramentas do lado do servidor (integradas).
A execução de código também é uma ferramenta do lado do servidor, mas tem uma solução integrada própria para
circulação de contexto. O uso do computador e a chamada de função são ferramentas do lado do cliente e também têm soluções integradas para a circulação de contexto.

| Ferramenta | Lado da execução | Suporte à circulação de contexto |
| --- | --- | --- |
| [Pesquisa Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br) | Servidor | Compatível |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pt-br) | Servidor | Compatível |
| [Contexto do URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br) | Servidor | Compatível |
| [Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/file-search?hl=pt-br) | Servidor | Compatível |
| [Execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br) | Servidor | Com suporte (integrado, usa etapas `code_execution` e `code_execution_result`) |
| [Uso do computador](https://ai.google.dev/gemini-api/docs/computer-use?hl=pt-br) | Lado do cliente | Com suporte (integrado, usa etapas `function_call` e `function_response`) |
| [Funções personalizadas](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br) | Lado do cliente | Com suporte (integrado, usa as etapas `function_call` e `function_response`) |

## A seguir

- Saiba mais sobre a [chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br) na API Gemini.
- Conheça as ferramentas compatíveis:
  - [Pesquisa Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pt-br)
  - [Contexto do URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br)
  - [Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/file-search?hl=pt-br)

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-24 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-24 UTC."],[],[]]
