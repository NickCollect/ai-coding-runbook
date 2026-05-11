---
source_url: https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=pt-BR
fetched_at: 2026-05-11T05:01:27.255967+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Geração de texto

A API Gemini pode gerar saídas de texto com base em entradas de texto, imagens, vídeo e áudio.

Confira um exemplo básico:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="How does AI work?"
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "How does AI work?",
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "How does AI work?"
  }'
```

## Pensar com o Gemini

Os modelos do Gemini geralmente têm o ["raciocínio"](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=pt-br) ativado por padrão, o que permite que o modelo pense antes de responder a uma solicitação.

Cada modelo é compatível com diferentes configurações de pensamento, o que dá controle sobre custo, latência e inteligência. Para mais detalhes, consulte o [guia de pensamento](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=pt-br#set-budget).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="How does AI work?",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## Instruções do sistema e outras configurações

É possível orientar o comportamento dos modelos do Gemini com instruções do sistema. Transmita um parâmetro `system_instruction` para configurar o comportamento do modelo.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    system_instruction="You are a cat. Your name is Neko.",
    input="Hello there"
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Hello there",
    system_instruction: "You are a cat. Your name is Neko.",
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "system_instruction": "You are a cat. Your name is Neko.",
    "input": "Hello there"
  }'
```

Você também pode substituir os parâmetros de geração padrão, como
temperatura, usando o parâmetro `generation_config`.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Explain how AI works",
    generation_config={
        "temperature": 0.1
    }
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Explain how AI works",
    generation_config: {
      temperature: 0.1,
    },
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain how AI works",
    "generation_config": {
      "temperature": 0.1
    }
  }'
```

Consulte a [referência da API Interactions](https://ai.google.dev/api/interactions-api?hl=pt-br) para ver uma lista completa de parâmetros configuráveis e as descrições deles.

## Entradas multimodais

A API Gemini aceita entradas multimodais, permitindo combinar texto com
arquivos de mídia. O exemplo a seguir mostra como fornecer uma imagem:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/organ.jpg")

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "Tell me about this instrument"},
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.steps[-1].content[0].text)
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
    model: "gemini-3-flash-preview",
    input: [
      {type: "text", text: "Tell me about this instrument"},
      {
        type: "image",
        uri: uploadedFile.uri,
        mime_type: uploadedFile.mimeType
      }
    ],
  });
  console.log(interaction.steps.at(-1).content[0].text);
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
    "model": "gemini-3-flash-preview",
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

Para conhecer outros métodos de fornecimento de imagens e um processamento mais avançado,
consulte nosso [guia de compreensão de imagens](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=pt-br).
A API também oferece suporte a entradas e compreensão de [documentos](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=pt-br), [vídeos](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=pt-br) e [áudios](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=pt-br).

## Respostas de streaming

Por padrão, o modelo retorna uma resposta somente depois que todo o processo de geração é concluído.

Para interações mais fluidas, use o streaming para processar partes da resposta
à medida que são geradas.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3-flash-preview",
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
    model: "gemini-3-flash-preview",
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
    "model": "gemini-3-flash-preview",
    "input": "Explain how AI works",
    "stream": true
  }'
```

## Conversas com vários turnos

A API Interactions é compatível com conversas multiturno ao encadear interações
usando `previous_interaction_id`. Cada turno é uma interação separada, e a API gerencia automaticamente o histórico da conversa.

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="I have 2 dogs in my house.",
)
print(interaction1.steps[-1].content[0].text)

interaction2 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print(interaction2.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

  const interaction2 = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
  });
  console.log("Response 2:", interaction2.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "I have two dogs in my house. How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

O streaming também pode ser usado em conversas de várias interações combinando `previous_interaction_id` com os métodos de streaming.

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="I have 2 dogs in my house.",
)
print(interaction1.steps[-1].content[0].text)

stream = client.interactions.create(
    model="gemini-3-flash-preview",
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
    model: "gemini-3-flash-preview",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

  const stream = await ai.interactions.create({
    model: "gemini-3-flash-preview",
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
    "model": "gemini-3-flash-preview",
    "input": "I have 2 dogs in my house."
  }')
INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "stream": true
  }'
```

## Dicas de comandos

Consulte nosso [guia de engenharia de comandos](https://ai.google.dev/gemini/docs/prompting-strategies?hl=pt-br) para
sugestões sobre como aproveitar ao máximo o Gemini.

## A seguir

- Teste o [Gemini no Google AI Studio](https://aistudio.google.com?hl=pt-br).
- Teste [saídas estruturadas](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=pt-br) para respostas semelhantes a JSON.
- Conheça as capacidades de compreensão de [imagens](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=pt-br), [vídeos](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=pt-br), [áudios](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=pt-br) e [documentos](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=pt-br) do Gemini.
- Saiba mais sobre as
  [estratégias de comando de arquivos](https://ai.google.dev/gemini-api/docs/interactions/files?hl=pt-br#prompt-guide) multimodais.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-09 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-09 UTC."],[],[]]
