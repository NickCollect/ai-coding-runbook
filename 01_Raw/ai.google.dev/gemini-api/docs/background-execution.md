---
source_url: https://ai.google.dev/gemini-api/docs/background-execution?hl=pt-BR
fetched_at: 2026-09-07T05:49:23.547211+00:00
title: "Execu\u00e7\u00e3o em segundo plano \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Execução em segundo plano

Para tarefas de longa duração, como pesquisa detalhada, raciocínio complexo ou execuções de agentes de várias etapas, os tempos limite de conexão podem interromper as solicitações HTTP padrão (que normalmente são fechadas após 60 segundos). A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) oferece **execução em segundo plano** para executar essas tarefas de forma assíncrona.

Para permitir que a interação seja executada até concluir a tarefa no servidor, defina `"background": true` ao criar a interação. A API retorna imediatamente um ID de interação, que os aplicativos cliente podem usar para pesquisar o status, transmitir o progresso ou se reconectar a um stream desconectado.

A execução em segundo plano é compatível com modelos padrão do Gemini (como `gemini-3.8-flash` e `gemini-3.1-pro-preview`) e agentes gerenciados (como `antigravity-preview-05-2026`).

## Criar uma interação em segundo plano

Para iniciar uma interação em segundo plano, defina o parâmetro `background` como `true` ao criar o recurso.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Write a guide on space exploration.",
    background=True,
)
print(f"Created background interaction ID: {interaction.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Write a guide on space exploration.",
    background: true,
});
console.log(`Created background interaction ID: ${interaction.id}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.models.operations.GetInteractionByIdResponse;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Execute this background task."))
        .background(true)
        .environment(CreateModelInteractionEnvironment.of("remote"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
String interactionId = interaction.id().orElse("");

// Poll status using GetInteractionByIdRequest
GetInteractionByIdResponse getResponse =
    client.interactions.get(new GetInteractionByIdRequest(interactionId));
Interaction polled = getResponse.interaction().get();
System.out.println("Status: " + polled.status().orElse(null));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Write a guide on space exploration.",
    "background": true
  }'
```

## Como funciona a execução em segundo plano

Quando você cria uma interação em segundo plano, a tarefa é executada de forma assíncrona no servidor. A interação passa por vários estados de execução:

- `in_progress`: o servidor está executando ativamente a interação (como executar código ou pesquisar).
- `requires_action`: a interação foi pausada e está aguardando a entrada do cliente (como confirmar a execução de uma ferramenta ou responder a uma pergunta).
- `completed`: a interação foi concluída e a saída está disponível.
- `failed`: ocorreu um erro durante a execução (como falha na ferramenta ou limites de taxa).
- `cancelled`: uma solicitação do cliente interrompeu a execução.

### Casos de uso

Use a execução em segundo plano para:

- **Execuções de agentes**:tarefas que exigem execução de código, navegação na Web ou orquestração de subagentes (como `antigravity-preview-05-2026`).
- **Pesquisa detalhada**:execuções usando `deep-research-preview-04-2026` ou `deep-research-max-preview-04-2026`, que levam vários minutos.
- **Raciocínio longo**:tarefas em que as etapas de pensamento do modelo excedem os limites de conexão HTTP padrão.

## Recuperar resultados

Receba resultados de interação em segundo plano usando **polling** ou **streaming**.

### Padrão de polling (sem bloqueio)

O polling verifica o status da interação periodicamente usando solicitações GET sem bloqueio até que ela atinja um estado terminal.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.get(id="YOUR_INTERACTION_ID")

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

let interaction = await client.interactions.get("YOUR_INTERACTION_ID");

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

if (interaction.status === "completed") {
    console.log(interaction.output_text);
} else {
    console.log(`Finished with status: ${interaction.status}`);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.models.operations.GetInteractionByIdResponse;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Execute this background task."))
        .background(true)
        .environment(CreateModelInteractionEnvironment.of("remote"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
String interactionId = interaction.id().orElse("");

// Poll status using GetInteractionByIdRequest
GetInteractionByIdResponse getResponse =
    client.interactions.get(new GetInteractionByIdRequest(interactionId));
Interaction polled = getResponse.interaction().get();
System.out.println("Status: " + polled.status().orElse(null));
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

### Padrão de streaming

Se uma interrupção de rede desconectar um stream, o streaming poderá ser retomado do último evento recebido. Cada delta contém um `event_id` exclusivo no payload. A transmissão desse ID como `last_event_id` retoma o stream desse evento.

### Python

```
import time
from google import genai

client = genai.Client()
interaction_id = "YOUR_INTERACTION_ID"

def stream_with_reconnect(interaction_id: str):
    last_event_id = None
    while True:
        try:
            # Retrieve the stream. If resuming, pass last_event_id
            stream = client.interactions.get(
                id=interaction_id,
                stream=True,
                last_event_id=last_event_id
            )

            for event in stream:
                # Log event updates and capture event_id if present
                if event.event_id:
                    last_event_id = event.event_id

                if event.event_type == "step.delta" and event.delta.type == "text":
                    print(event.delta.text, end="", flush=True)

                if event.event_type == "interaction.completed":
                    return

        except Exception as e:
            print(f"\n[Connection lost: {e}. Reconnecting in 3s...]")
            time.sleep(3)

stream_with_reconnect(interaction_id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const interactionId = "YOUR_INTERACTION_ID";

async function streamWithReconnect(id) {
    let lastEventId = undefined;
    while (true) {
        try {
            // Retrieve the stream. If resuming, pass last_event_id in options
            const stream = await client.interactions.get(id, {
                stream: true,
                last_event_id: lastEventId
            });

            for await (const event of stream) {
                // Capture event_id if present
                const idVal = event.event_id || event.id;
                if (idVal) {
                    lastEventId = idVal;
                }

                if (event.event_type === "step.delta" && event.delta?.type === "text") {
                    process.stdout.write(event.delta.text);
                }

                if (event.event_type === "interaction.completed") {
                    return;
                }
            }
        } catch (error) {
            console.log(`\n[Connection lost: ${error.message}. Reconnecting in 3s...]`);
            await new Promise(resolve => setTimeout(resolve, 3000));
        }
    }
}

await streamWithReconnect(interactionId);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.models.operations.GetInteractionByIdResponse;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Execute this background task."))
        .background(true)
        .environment(CreateModelInteractionEnvironment.of("remote"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
String interactionId = interaction.id().orElse("");

// Poll status using GetInteractionByIdRequest
GetInteractionByIdResponse getResponse =
    client.interactions.get(new GetInteractionByIdRequest(interactionId));
Interaction polled = getResponse.interaction().get();
System.out.println("Status: " + polled.status().orElse(null));
```

### REST

```
curl -N -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID?stream=true&last_event_id=YOUR_LAST_EVENT_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## Conversas multiturno

As interações subsequentes podem ser encadeadas a uma conversa em segundo plano usando `previous_interaction_id`, sujeitas a estas restrições:

1. **Execuções ativas são bloqueadas**:o encadeamento de uma interação subsequente a uma com status `in_progress` retorna um erro `400 Bad Request`. Aguarde a interação atingir o estado `completed` antes de iniciar a próxima.
2. **Parâmetro de ambiente para agentes gerenciados**:ao encadear interações para agentes gerenciados (como `antigravity-preview-05-2026`), as solicitações precisam incluir `previous_interaction_id` e `environment`.

Os exemplos a seguir mostram como encadear interações:

### Python

```
import time
from google import genai

client = genai.Client()
agent_model = "antigravity-preview-05-2026"

# First interaction: Provision sandbox environment and execute first instruction
interaction1 = client.interactions.create(
    model=agent_model,
    input="Create a folder named project/ and write hello.py inside.",
    environment="remote",
    background=True
)

# Wait for completion
while True:
    check = client.interactions.get(id=interaction1.id)
    if check.status != "in_progress":
        break
    time.sleep(2)

# Second interaction: Chain using previous_interaction_id and environment
interaction2 = client.interactions.create(
    model=agent_model,
    input="List all files in the project/ directory.",
    previous_interaction_id=interaction1.id,
    environment="remote",
    background=True
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const agentModel = "antigravity-preview-05-2026";

// First interaction: Provision sandbox environment and execute first instruction
const interaction1 = await client.interactions.create({
    model: agentModel,
    input: "Create a folder named project/ and write hello.py inside.",
    environment: "remote",
    background: true
});

// Wait for completion
while (true) {
    const check = await client.interactions.get(interaction1.id);
    if (check.status !== "in_progress") {
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 2000));
}

// Second interaction: Chain using previous_interaction_id and environment
const interaction2 = await client.interactions.create({
    model: agentModel,
    input: "List all files in the project/ directory.",
    previous_interaction_id: interaction1.id,
    environment: "remote",
    background: true
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.models.operations.GetInteractionByIdResponse;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Execute this background task."))
        .background(true)
        .environment(CreateModelInteractionEnvironment.of("remote"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
String interactionId = interaction.id().orElse("");

// Poll status using GetInteractionByIdRequest
GetInteractionByIdResponse getResponse =
    client.interactions.get(new GetInteractionByIdRequest(interactionId));
Interaction polled = getResponse.interaction().get();
System.out.println("Status: " + polled.status().orElse(null));
```

### REST

```
# Chain second interaction (Make sure FIRST_INTERACTION_ID has status 'completed')
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "antigravity-preview-05-2026",
    "input": "List all files in the project/ directory.",
    "previous_interaction_id": "FIRST_INTERACTION_ID",
    "environment": "remote",
    "background": true
  }'
```

## Cancelamento e exclusão

Controle as execuções em andamento e gerencie o armazenamento usando solicitações de cancelamento e exclusão:

- **Cancelar (`POST /interactions/{id}/cancel`)** : interrompe a tarefa em execução. O status faz a transição para `cancelled`. As ações de limpeza no servidor podem causar um pequeno atraso antes que o status seja atualizado nas solicitações GET.
- **Excluir (`DELETE /interactions/{id}`)** : remove os registros de interação do servidor. As solicitações GET subsequentes retornam um erro `404 Not Found`.

### Python

```
from google import genai

client = genai.Client()

# Cancel a running interaction
client.interactions.cancel(id="YOUR_INTERACTION_ID")

# Delete the interaction record entirely
client.interactions.delete(id="YOUR_INTERACTION_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Cancel a running interaction
await client.interactions.cancel("YOUR_INTERACTION_ID");

// Delete the interaction record entirely
await client.interactions.delete("YOUR_INTERACTION_ID");
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.models.operations.GetInteractionByIdResponse;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Execute this background task."))
        .background(true)
        .environment(CreateModelInteractionEnvironment.of("remote"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
String interactionId = interaction.id().orElse("");

// Poll status using GetInteractionByIdRequest
GetInteractionByIdResponse getResponse =
    client.interactions.get(new GetInteractionByIdRequest(interactionId));
Interaction polled = getResponse.interaction().get();
System.out.println("Status: " + polled.status().orElse(null));
```

### REST

```
# Cancel the interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID/cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"

# Delete the interaction
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## Próximas etapas

- Leia a [visão geral da API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) para entender o gerenciamento de sessão e estado.
- Consulte o guia [Interações de streaming](https://ai.google.dev/gemini-api/docs/streaming?hl=pt-br) para detalhes sobre atualizações de eventos em tempo real.
- Confira o [guia de início rápido de agentes gerenciados](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pt-br) para criar agentes com estado multiturno.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-04 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-04 UTC."],[],[]]
