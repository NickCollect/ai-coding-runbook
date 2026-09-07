---
source_url: https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-BR
fetched_at: 2026-09-07T05:35:27.160992+00:00
title: "Gera\u00e7\u00e3o de texto \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Geração de texto

A API Gemini pode gerar saída de texto com base em entradas de texto, imagens, vídeo e áudio.

Confira um exemplo básico:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="How does AI work?"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "How does AI work?",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "How does AI work?"
  }'
```

Os SDKs do Google GenAI fornecem propriedades de conveniência diretamente no objeto `Interaction` retornado para acessar a resposta do modelo.

O auxiliar mais comum é **`interaction.output_text`** (string), que retorna os últimos blocos de texto na resposta do modelo. Se a resposta for dividida em vários blocos `TextContent` consecutivos, ela será unida automaticamente.
O `.output_text` não inclui blocos de texto anteriores separados por conteúdo não textual (como pensamentos, imagens, áudio ou chamadas de ferramentas). Para respostas multimodais complexas ou intercaladas, é necessário iterar manualmente em `steps`. Para saber mais sobre outras propriedades de conveniência de mídia, consulte a
[visão geral das interações](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br#convenience-properties).

## Pensando com o Gemini

Os modelos do Gemini geralmente têm o ["pensamento"](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=pt-br)
ativado por padrão, o que permite que o modelo raciocine antes de responder a uma
solicitação.

Cada modelo oferece suporte a diferentes configurações de pensamento, o que permite controlar o custo, a latência e a inteligência. Para mais detalhes, consulte o
[guia de pensamento](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=pt-br#set-budget).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="How does AI work?",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## Instruções do sistema e outras configurações

Você pode orientar o comportamento dos modelos do Gemini com instruções do sistema. Transmita um parâmetro `system_instruction` para configurar o comportamento do modelo.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    system_instruction="You are a cat. Your name is Neko.",
    input="Hello there"
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Hello there",
    system_instruction: "You are a cat. Your name is Neko.",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "system_instruction": "You are a cat. Your name is Neko.",
    "input": "Hello there"
  }'
```

Também é possível substituir os parâmetros de geração padrão, como a temperatura, usando o parâmetro `generation_config`.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works",
    generation_config={
        "temperature": 1.0
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain how AI works",
    generation_config: {
      temperature: 1.0,
    },
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works",
    "generation_config": {
      "temperature": 1.0
    }
  }'
```

Consulte a [referência da API Interactions](https://ai.google.dev/api/interactions-api?hl=pt-br)
para uma lista completa de parâmetros configuráveis e as
descrições deles.

## Entradas multimodais

A API Gemini oferece suporte a entradas multimodais, permitindo combinar texto com arquivos de mídia. O exemplo a seguir demonstra como fornecer uma imagem:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/organ.jpg")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Tell me about this instrument"},
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const uploadedFile = await ai.files.upload({
    file: "path/to/organ.jpg",
    config: { mimeType: "image/jpeg" }
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: [
      {type: "text", text: "Tell me about this instrument"},
      {
        type: "image",
        uri: uploadedFile.uri,
        mime_type: uploadedFile.mimeType
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Tell me about this instrument"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

Para métodos alternativos de fornecimento de imagens e processamento de imagens mais avançado,
consulte nosso [guia de compreensão de imagens](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=pt-br).
A API também oferece suporte a [documentos](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=pt-br), [vídeos](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=pt-br) e
[áudio](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=pt-br) entradas e compreensão.

## Respostas de streaming

Por padrão, o modelo retorna uma resposta somente após a conclusão de todo o processo de geração.

Para interações mais fluidas, use o streaming para processar blocos de resposta à medida que eles são gerados. Para um guia abrangente que abrange tipos de eventos,
streaming com ferramentas, pensamento, agentes e geração de imagens, consulte o
guia dedicado [de interações de streaming](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=pt-br).

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works",
    stream=True
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const stream = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain how AI works",
    stream: true,
  });

  for await (const event of stream) {
    if (event.event_type === "step.delta") {
      if (event.delta.type === "text") {
        process.stdout.write(event.delta.text);
      }
    }
  }
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works",
    "stream": true
  }'
```

## Conversas multiturno

A API Interactions oferece suporte a conversas multiturno encadeando interações usando `previous_interaction_id`. Cada turno é uma interação separada, e a API gerencia automaticamente o histórico de conversas.

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    input="I have 2 dogs in my house.",
)
print(interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print(interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.output_text);

  const interaction2 = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
  });
  console.log("Response 2:", interaction2.output_text);
}

await main();
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "I have two dogs in my house. How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

O streaming também pode ser usado para conversas multiturno combinando `previous_interaction_id` com os métodos de streaming.

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    input="I have 2 dogs in my house.",
)
print(interaction1.output_text)

stream = client.interactions.create(
    model="gemini-3.6-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
    stream=True
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.output_text);

  const stream = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
    stream: true,
  });
  for await (const event of stream) {
    if (event.event_type === "step.delta") {
      if (event.delta.type === "text") {
        process.stdout.write(event.delta.text);
      }
    }
  }
}

await main();
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "I have 2 dogs in my house."
  }')
INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "stream": true
  }'
```

## Conversas sem estado

Por padrão, a API Interactions gerencia o estado da conversa no lado do servidor quando você usa `previous_interaction_id`. No entanto, também é possível operar no modo sem estado gerenciando o histórico de conversas no lado do cliente.

Para usar o modo sem estado: 1. Defina `store=false` na solicitação para desativar o armazenamento no lado do servidor.
2. Mantenha o histórico de conversas como uma matriz de **etapas** no lado do cliente.
3. Em solicitações subsequentes, transmita as etapas acumuladas no campo `input` e anexe seu novo turno como uma etapa `user_input`.

### Python

```
from google import genai

client = genai.Client()

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "I have 2 dogs in my house."}]
    }
]

interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    store=False,
    input=history
)
print("Response 1:", interaction1.steps[-1].content[0].text)

for step in interaction1.steps:
    history.append(step.model_dump())

history.append({
    "type": "user_input",
    "content": [{"type": "text", "text": "How many paws are in my house?"}]
})

interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
    store=False,
    input=history
)
print("Response 2:", interaction2.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const history = [
    {
      type: "user_input",
      content: [{ type: "text", text: "I have 2 dogs in my house." }]
    }
  ];

  const interaction1 = await ai.interactions.create({
    model: "gemini-3.6-flash",
    store: false,
    input: history
  });
  console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

  history.push(...interaction1.steps);

  history.push({
    type: "user_input",
    content: [{ type: "text", text: "How many paws are in my house?" }]
  });

  const interaction2 = await ai.interactions.create({
    model: "gemini-3.6-flash",
    store: false,
    input: history
  });
  console.log("Response 2:", interaction2.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
# Turn 1: Send request with store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "I have 2 dogs in my house."
      }
    ]
  }')

# Extract the steps from response
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Reconstruct the full history for Turn 2 by combining:
# 1. First user input
# 2. Model response steps
# 3. Second user input
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "I have 2 dogs in my house."}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --argjson second_input '[{"type": "user_input", "content": "How many paws are in my house?"}]' \
  "'"'"'$first_input + $model_steps + $second_input'"'"'")

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.6-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

## Dicas de comandos

Consulte nosso [guia de engenharia de comandos](https://ai.google.dev/gemini/docs/prompting-strategies?hl=pt-br) para
sugestões sobre como aproveitar ao máximo o Gemini.

## A seguir

- Teste o [Gemini no Google AI Studio](https://aistudio.google.com?hl=pt-br).
- Faça experimentos com
  [saídas estruturadas](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=pt-br) para
  respostas semelhantes a JSON.
- Conheça os recursos de compreensão de [imagens](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=pt-br),
  [vídeos](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=pt-br),
  [áudio](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=pt-br) e
  [documentos](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=pt-br) do
  Gemini.
- Saiba mais sobre as estratégias de comandos de arquivos multimodais
  .

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-30 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-30 UTC."],[],[]]
