---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=pt-BR
fetched_at: 2026-10-12T06:57:07.380206+00:00
title: "Guia para desenvolvedores do Gemini 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)

Envie comentários

# Guia para desenvolvedores do Gemini 3

O Gemini 3 é nossa família de modelos mais inteligente até o momento, criada com base em um raciocínio de última geração. Ele foi projetado para dar vida a qualquer ideia com Agentic Workflows, programação autônoma e tarefas multimodais complexas.
Este guia aborda os principais recursos da família de modelos Gemini 3 e como aproveitar ao máximo.

Conheça nossa [coleção de apps do Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=pt-br) para
ver como o modelo lida com raciocínio avançado, programação autônoma e tarefas
multimodais complexas.

Comece com algumas linhas de código:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.output_text);
}

run();
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

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-pro-preview"))
        .input(
            InteractionsInput.of(
                "Find the race condition in this multi-threaded C++ snippet: [code here]"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

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
            Model: interactions.Model("gemini-3.1-pro-preview"),
            Input: interactions.NewInteractionsInput("Find the race condition in this multi-threaded C++ snippet: [code here]"),
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
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## Conheça a série Gemini 3

O Gemini 3.1 Pro é ideal para tarefas complexas que exigem amplo conhecimento geral e raciocínio avançado em várias modalidades.

O Gemini 3 Flash é nosso modelo mais recente da série 3, com inteligência de nível Pro na velocidade e nos preços do Flash.

O Nano Banana Pro (também conhecido como Gemini 3 Pro Image) é nosso modelo de geração de imagens de mais alta qualidade, e o Nano Banana 2 (também conhecido como Gemini 3.1 Flash Image) é o equivalente de alto volume, alta eficiência e menor faixa de preços.

O Gemini 3.1 Flash-Lite é nosso modelo de trabalho criado para ser econômico e realizar tarefas de grande volume.

Todos os modelos do Gemini 3 estão em pré-lançamento.

| ID do modelo | Janela de contexto (dentro / fora) | Limite de conhecimento | Preços (entrada / saída)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1M / 64k | Jan 2025 | US$ 0,25 (texto, imagem, vídeo), US$ 0,50 (áudio) / US$ 1,50 |
| **gemini-3.1-flash-image-preview** | 128k / 32k | Jan 2025 | US$ 0,25 (entrada de texto) / US$ 0,067 (saída de imagem)\*\* |
| **gemini-3.1-pro-preview** | 1M / 64k | Jan 2025 | US$ 2 / US$ 12 (<200 mil tokens)   US $4 / US$ 18 (>200 mil tokens) |
| **gemini-3-flash-preview** | 1M / 64k | Jan 2025 | US$ 0,50 / US$ 3 |
| **gemini-3-pro-image-preview** | 65 mil / 32 mil | Jan 2025 | US$ 2 (entrada de texto) / US$ 0,134 (saída de imagem)\*\* |

*\* Os preços são por 1 milhão de tokens, a menos que indicado de outra forma.*
*\*\* O preço das imagens varia de acordo com a resolução. Consulte a [página de preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br) para mais detalhes.*

Para limites detalhados, preços e mais informações, consulte a
[página de modelos](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pt-br).

## Novos recursos da API no Gemini 3

O Gemini 3 apresenta novos parâmetros projetados para dar aos desenvolvedores mais controle sobre latência, custo e fidelidade multimodal.

### Nível de raciocínio

Por padrão, os modelos da série Gemini 3 usam o raciocínio dinâmico para analisar comandos. Você pode usar o parâmetro `thinking_level`, que controla a
profundidade **máxima** do processo de raciocínio interno do modelo antes de gerar uma
resposta. O Gemini 3 trata esses níveis como permissões relativas para raciocínio, e não como garantias estritas de tokens.

Se `thinking_level` não for especificado, o Gemini 3 vai usar `high` como padrão. Para respostas mais rápidas e com menor latência quando não é necessário um raciocínio complexo, você pode restringir o nível de pensamento do modelo a `low`.

| Nível de raciocínio | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Descrição |
| --- | --- | --- | --- | --- |
| **`minimal`** | incompatível | Compatível (padrão) | Compatível | Corresponde à configuração "sem pensar" para a maioria das consultas. O modelo pode pensar de forma muito minimalista para tarefas de programação complexas. Minimiza a latência para aplicativos de chat ou de alta capacidade de processamento. Vale lembrar que `minimal` não garante que o pensamento esteja desativado. |
| **`low`** | Compatível | Compatível | Compatível | Minimiza a latência e o custo. Ideal para seguir instruções simples, conversar ou aplicativos de alta capacidade de processamento. |
| **`medium`** | Compatível | Compatível | Compatível | Pensamento equilibrado para a maioria das tarefas. |
| **`high`** | Compatível (padrão, dinâmico) | Compatível (dinâmico) | Compatível (padrão, dinâmico) | Maximiza a profundidade do raciocínio. O modelo pode levar muito mais tempo para gerar o primeiro token de saída (sem pensar), mas a saída será mais bem fundamentada. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-pro-preview"))
        .input(InteractionsInput.of("How does AI work?"))
        .generationConfig(
            GenerationConfig.builder()
                .thinkingLevel(ThinkingLevel.LOW)
                .build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

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
            Model: interactions.Model("gemini-3.1-pro-preview"),
            Input: interactions.NewInteractionsInput("How does AI work?"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelLow.ToPointer(),
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### Temperatura

Para todos os modelos do Gemini 3, recomendamos manter o parâmetro de temperatura no valor padrão de `1.0`.

Embora os modelos anteriores se beneficiassem da temperatura de ajuste para controlar a criatividade em relação ao determinismo, os recursos de raciocínio do Gemini 3 são otimizados para a configuração padrão. Mudar a temperatura (definindo-a abaixo de 1,0) pode levar a um comportamento inesperado, como looping ou desempenho degradado, principalmente em tarefas complexas de matemática ou raciocínio.

### Assinaturas de raciocínio

Os modelos do Gemini 3 usam assinaturas de pensamento para manter o contexto de raciocínio em todas as chamadas de API. Essas assinaturas são representações criptografadas do processo de raciocínio interno do modelo.

- **Modo com estado (recomendado)**: ao usar a API Interactions no modo com estado (fornecendo `previous_interaction_id`), o servidor gerencia automaticamente o histórico de conversas e as assinaturas de pensamento.
- **Modo sem estado**: se você estiver gerenciando o histórico de conversas manualmente, inclua blocos de pensamento com as assinaturas deles em solicitações subsequentes para validar a autenticidade.

Para informações detalhadas, consulte a página [Assinaturas de pensamento](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br).

### Respostas estruturadas com ferramentas

Os modelos do Gemini 3 permitem combinar [saídas estruturadas](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br) com ferramentas integradas, incluindo [embasamento com a Pesquisa Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br), [contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br), [execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br) e [chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.output_text));
  console.log(match);
}

run();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.interactions.URLContext;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();
properties.put("winner", Map.of("type", "string", "description", "The name of the winner."));
properties.put(
    "final_match_score", Map.of("type", "string", "description", "The final match score."));
properties.put(
    "scorers",
    Map.of(
        "type", "array",
        "items", Map.of("type", "string"),
        "description", "The name of the scorer."));

Map<String, Object> schema = new HashMap<>();
schema.put("type", "object");
schema.put("properties", properties);
schema.put("required", Arrays.asList("winner", "final_match_score", "scorers"));

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-pro-preview"))
        .input(InteractionsInput.of("Search for all details for the latest Euro."))
        .tools(Arrays.asList(GoogleSearch.builder().build(), URLContext.builder().build()))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(
                    TextResponseFormat.builder()
                        .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                        .schema(schema)
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

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

    schema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "winner": map[string]any{
                "type":        "string",
                "description": "The name of the winner.",
            },
            "final_match_score": map[string]any{
                "type":        "string",
                "description": "The final match score.",
            },
            "scorers": map[string]any{
                "type":        "array",
                "items":       map[string]any{"type": "string"},
                "description": "The name of the scorer.",
            },
        },
        "required": []string{"winner", "final_match_score", "scorers"},
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.1-pro-preview"),
            Input: interactions.NewInteractionsInput("Search for all details for the latest Euro."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
                interactions.NewTool(interactions.URLContext{}),
            },
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.TextResponseFormat{
                    MimeType: interactions.TextResponseFormatMimeType("application/json").ToPointer(),
                    Schema:   schema,
                }),
            )),
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
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### Geração de imagens

Com o Gemini 3.1 Flash Image e o Gemini 3 Pro Image, você pode gerar e editar imagens
com comandos de texto. Ele usa o raciocínio para "pensar" em um comando e pode recuperar dados em tempo real, como previsões do tempo ou gráficos de ações, antes de usar a fundamentação da [Pesquisa Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br) e gerar imagens de alta fidelidade.

**Recursos novos e aprimorados:**

- **Renderização de texto e 4K**:gere textos e diagramas nítidos e legíveis com resoluções de até 2K e 4K.
- **Geração embasada**:use a ferramenta `google_search` para verificar fatos e gerar imagens com base em informações do mundo real. O embasamento com a Pesquisa de *Imagens* do Google está disponível para o Gemini 3.1 Flash Image.
- **Edição conversacional**:edição de imagens multiturno. Basta pedir as mudanças que você quer (por exemplo, "Mude o plano de fundo para um pôr do sol"). Esse fluxo de trabalho usa as **assinaturas de pensamento** para preservar o contexto visual entre as interações.

Para detalhes completos sobre proporções, fluxos de trabalho de edição e opções de configuração, consulte o [guia de geração de imagens](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br).

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

generated_image = interaction.output_image
if generated_image:
    image_data = base64.b64decode(generated_image.data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  const buffer = Buffer.from(interaction.output_image.data, 'base64');

  fs.writeFileSync('weather_tokyo.png', buffer);
}

run();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageResponseFormat;
import com.google.genai.gaos.models.interactions.ImageResponseFormatAspectRatio;
import com.google.genai.gaos.models.interactions.ImageResponseFormatImageSize;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.Optional;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-pro-image-preview"))
        .input(InteractionsInput.of("Generate an infographic of the current weather in Tokyo."))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(
                    ImageResponseFormat.builder()
                        .aspectRatio(ImageResponseFormatAspectRatio.ONE_HUNDRED_AND_SIXTY_NINE)
                        .imageSize(ImageResponseFormatImageSize.FOUR_K)
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

Optional<ImageContent> generatedImage = interaction.outputImage();
if (generatedImage.isPresent() && generatedImage.get().data().isPresent()) {
  byte[] imageBytes = Base64.getDecoder().decode(generatedImage.get().data().get());
  Files.write(Paths.get("weather_tokyo.png"), imageBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"
    "os"

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
            Model: interactions.Model("gemini-3-pro-image-preview"),
            Input: interactions.NewInteractionsInput("Generate an infographic of the current weather in Tokyo."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
            },
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.ImageResponseFormat{
                    AspectRatio: interactions.ImageResponseFormatAspectRatioOneHundredAndSixtyNine.ToPointer(),
                    ImageSize:   interactions.ImageResponseFormatImageSize("4K").ToPointer(),
                }),
            )),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if generatedImage := res.Interaction.GetOutputImage(); generatedImage != nil && generatedImage.Data != nil {
        imageBytes, err := base64.StdEncoding.DecodeString(*generatedImage.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("weather_tokyo.png", imageBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
  }'
```

**Exemplo de resposta**

![Clima em Tóquio](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=pt-br)

### Execução de código com imagens

O Gemini 3 Flash pode tratar a visão como uma investigação ativa, não apenas um olhar estático. Ao combinar o raciocínio com a [execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br), o modelo formula um plano, escreve e executa código Python para ampliar, cortar, anotar ou manipular imagens etapa por etapa para fundamentar visualmente as respostas.

**Casos de uso:**

- **Zoom e inspeção**:o modelo detecta implicitamente quando os detalhes estão muito pequenos (por exemplo, ao ler um medidor ou número de série distante) e escreve código para cortar e reexaminar a área em uma resolução mais alta.
- **Matemática e criação de gráficos visuais**:o modelo pode executar cálculos de várias etapas usando código (por exemplo, somar itens de linha em um recibo ou gerar um gráfico do Matplotlib com base em dados extraídos).
- **Anotação de imagem**:o modelo pode desenhar setas, caixas delimitadoras ou outras anotações diretamente nas imagens para responder a perguntas espaciais, como "Onde este item deve ser colocado?".

Para ativar o pensamento visual, configure a [Execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br) como uma ferramenta. O modelo vai usar automaticamente o código para manipular imagens quando necessário.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
    }
  }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CodeExecutionCallStep;
import com.google.genai.gaos.models.interactions.CodeExecutionResultStep;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.io.InputStream;
import java.net.URL;
import java.util.Arrays;
import java.util.Base64;
import java.util.Collections;

Client client = new Client();

URL url = new URL("https://goo.gle/instrument-img");
byte[] imageBytes;
try (InputStream is = url.openStream()) {
  imageBytes = is.readAllBytes();
}
String base64ImageData = Base64.getEncoder().encodeToString(imageBytes);

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-flash-preview"))
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    ImageContent.builder()
                        .mimeType(ImageContentMimeType.IMAGE_JPEG)
                        .data(base64ImageData)
                        .build(),
                    TextContent.builder()
                        .text("Zoom into the expression pedals and tell me how many pedals are there?")
                        .build())))
        .tools(Arrays.asList(CodeExecution.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof ModelOutputStep) {
    ModelOutputStep modelOutput = (ModelOutputStep) step;
    for (Content contentBlock : modelOutput.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent) {
        System.out.println("Text: " + ((TextContent) contentBlock).text().orElse(""));
      }
    }
  } else if (step instanceof CodeExecutionCallStep) {
    CodeExecutionCallStep callStep = (CodeExecutionCallStep) step;
    callStep.arguments().flatMap(args -> args.code()).ifPresent(code -> System.out.println("Code: " + code));
  } else if (step instanceof CodeExecutionResultStep) {
    CodeExecutionResultStep resultStep = (CodeExecutionResultStep) step;
    System.out.println("Output: " + resultStep.result().orElse(""));
  }
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "io"
    "log"
    "net/http"

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

    httpRes, err := http.Get("https://goo.gle/instrument-img")
    if err != nil {
        log.Fatal(err)
    }
    defer httpRes.Body.Close()
    imageBytes, err := io.ReadAll(httpRes.Body)
    if err != nil {
        log.Fatal(err)
    }
    base64ImageData := base64.StdEncoding.EncodeToString(imageBytes)

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3-flash-preview"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.ImageContent{
                    MimeType: interactions.ImageContentMimeType("image/jpeg").ToPointer(),
                    Data:     genai.Ptr(base64ImageData),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: "Zoom into the expression pedals and tell me how many pedals are there?",
                }),
            }),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if modelOutput := step.ModelOutputStep; modelOutput != nil {
            for _, contentBlock := range modelOutput.Content {
                if textContent := contentBlock.TextContent; textContent != nil {
                    fmt.Println("Text:", textContent.Text)
                }
            }
        } else if callStep := step.CodeExecutionCallStep; callStep != nil {
            if callStep.Arguments.Code != nil {
                fmt.Println("Code:", *callStep.Arguments.Code)
            }
        } else if resultStep := step.CodeExecutionResultStep; resultStep != nil {
            fmt.Println("Output:", resultStep.Result)
        }
    }
}
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

Para mais detalhes sobre a execução de código com imagens, consulte [Execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br#images).

### Respostas de funções multimodais

A [chamada de função multimodal](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br#multimodal)
permite que os usuários tenham respostas de função que contenham
objetos multimodais, melhorando a utilização dos recursos de chamada de função
do modelo. A chamada de função padrão só é compatível com respostas de função baseadas em texto:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

print(f"\nFinal model response: {interaction_2.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.output_text}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.FunctionResultSubcontent;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.io.InputStream;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Base64;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

Client client = new Client();

Map<String, Object> itemProp = new HashMap<>();
itemProp.put("type", "string");
itemProp.put("description", "The name or description of the item ordered (e.g., 'instrument').");

Map<String, Object> properties = new HashMap<>();
properties.put("item_name", itemProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("item_name"));

Function getImageTool =
    Function.builder()
        .name("get_image")
        .description("Retrieves the image file reference for a specific order item.")
        .parameters(parameters)
        .build();

CreateModelInteraction req1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-flash-preview"))
        .input(
            InteractionsInput.of(
                "Use the get_image tool to show me the instrument I ordered last month."))
        .tools(Arrays.asList(getImageTool))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(req1)).interaction().get();

FunctionCallStep fcStep = null;
for (Step step : interaction1.steps().orElse(Collections.emptyList())) {
  if (step instanceof FunctionCallStep) {
    fcStep = (FunctionCallStep) step;
    break;
  }
}

if (fcStep != null) {
  System.out.println("Tool Call: " + fcStep.name().orElse(""));

  URL url = new URL("https://goo.gle/instrument-img");
  byte[] imageBytes;
  try (InputStream is = url.openStream()) {
    imageBytes = is.readAllBytes();
  }
  String base64ImageData = Base64.getEncoder().encodeToString(imageBytes);

  List<FunctionResultSubcontent> subcontents = new ArrayList<>();
  subcontents.add(TextContent.builder().text("instrument.jpg").build());
  subcontents.add(
      ImageContent.builder()
          .mimeType(ImageContentMimeType.IMAGE_JPEG)
          .data(base64ImageData)
          .build());

  FunctionResultStep funcResult =
      FunctionResultStep.builder()
          .name(fcStep.name().orElse(""))
          .callId(fcStep.id().orElse(""))
          .result(FunctionResultStepResultUnion.of(subcontents))
          .build();

  CreateModelInteraction req2 =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3-flash-preview"))
          .input(InteractionsInput.ofStep(Arrays.asList(funcResult)))
          .tools(Arrays.asList(getImageTool))
          .previousInteractionId(interaction1.id().orElse(""))
          .build();

  Interaction interaction2 =
      client.interactions.create(CreateInteractionRequestBody.of(req2)).interaction().get();
  System.out.println("Final model response: " + interaction2.outputText().orElse(""));
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "io"
    "log"
    "net/http"

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

    getImageTool := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_image"),
        Description: genai.Ptr("Retrieves the image file reference for a specific order item."),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "item_name": map[string]any{
                    "type":        "string",
                    "description": "The name or description of the item ordered (e.g., 'instrument').",
                },
            },
            "required": []string{"item_name"},
        },
    })

    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3-flash-preview"),
            Input: interactions.NewInteractionsInput("Use the get_image tool to show me the instrument I ordered last month."),
            Tools: []interactions.Tool{getImageTool},
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res1.Interaction.Steps {
        if fcStep := step.FunctionCallStep; fcStep != nil {
            fmt.Println("Tool Call:", fcStep.Name)

            httpRes, err := http.Get("https://goo.gle/instrument-img")
            if err != nil {
                log.Fatal(err)
            }
            defer httpRes.Body.Close()
            imageBytes, err := io.ReadAll(httpRes.Body)
            if err != nil {
                log.Fatal(err)
            }
            base64ImageData := base64.StdEncoding.EncodeToString(imageBytes)

            funcResult := interactions.NewStep(interactions.FunctionResultStep{
                Name:   genai.Ptr(fcStep.Name),
                CallID: fcStep.ID,
                Result: interactions.NewFunctionResultStepResultUnion([]interactions.FunctionResultSubcontent{
                    interactions.NewFunctionResultSubcontent(interactions.TextContent{
                        Text: "instrument.jpg",
                    }),
                    interactions.NewFunctionResultSubcontent(interactions.ImageContent{
                        MimeType: interactions.ImageContentMimeType("image/jpeg").ToPointer(),
                        Data:     genai.Ptr(base64ImageData),
                    }),
                }),
            })

            res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model:                 interactions.Model("gemini-3-flash-preview"),
                    PreviousInteractionID: res1.Interaction.ID,
                    Tools:                 []interactions.Tool{getImageTool},
                    Input:                 interactions.NewInteractionsInput([]interactions.Step{funcResult}),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            if res2.Interaction.OutputText != nil {
                fmt.Println("Final model response:", *res2.Interaction.OutputText)
            }
            break
        }
    }
}
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### Combinar ferramentas integradas e chamadas de função

O Gemini 3 permite o uso de ferramentas integradas (como a Pesquisa Google, contexto de URL e [mais](https://ai.google.dev/gemini-api/docs/tools?hl=pt-br)) e ferramentas personalizadas de [chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br) na mesma chamada de API, permitindo fluxos de trabalho mais complexos.

### Python

```
from google import genai
from google.genai import types

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

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> cityProp = new HashMap<>();
cityProp.put("type", "string");
cityProp.put("description", "The city and state, e.g. Utqiaġvik, Alaska");

Map<String, Object> properties = new HashMap<>();
properties.put("city", cityProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("city"));

Function getWeather =
    Function.builder()
        .name("getWeather")
        .description("Gets the weather for a requested city.")
        .parameters(parameters)
        .build();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-flash-preview"))
        .input(
            InteractionsInput.of(
                "What is the northernmost city in the United States? What's the weather like there today?"))
        .tools(Arrays.asList(GoogleSearch.builder().build(), getWeather))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

FunctionCallStep fcStep = null;
for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof FunctionCallStep) {
    fcStep = (FunctionCallStep) step;
    break;
  }
}

if (fcStep != null) {
  FunctionResultStep funcResult =
      FunctionResultStep.builder()
          .name(fcStep.name().orElse(""))
          .callId(fcStep.id().orElse(""))
          .result(
              FunctionResultStepResultUnion.of(
                  "{\"response\": \"Very cold. 22 degrees Fahrenheit.\"}"))
          .build();

  CreateModelInteraction finalRequest =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3-flash-preview"))
          .input(InteractionsInput.ofStep(Arrays.asList(funcResult)))
          .tools(Arrays.asList(GoogleSearch.builder().build(), getWeather))
          .previousInteractionId(interaction.id().orElse(""))
          .build();

  Interaction finalInteraction =
      client.interactions.create(CreateInteractionRequestBody.of(finalRequest)).interaction().get();
  System.out.println(finalInteraction.outputText().orElse(""));
}
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

    getWeather := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("getWeather"),
        Description: genai.Ptr("Gets the weather for a requested city."),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "city": map[string]any{
                    "type":        "string",
                    "description": "The city and state, e.g. Utqiaġvik, Alaska",
                },
            },
            "required": []string{"city"},
        },
    })

    tools := []interactions.Tool{
        interactions.NewTool(interactions.GoogleSearch{}),
        getWeather,
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3-flash-preview"),
            Input: interactions.NewInteractionsInput("What is the northernmost city in the United States? What's the weather like there today?"),
            Tools: tools,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if fcStep := step.FunctionCallStep; fcStep != nil {
            funcResult := interactions.NewStep(interactions.FunctionResultStep{
                Name:   genai.Ptr(fcStep.Name),
                CallID: fcStep.ID,
                Result: interactions.NewFunctionResultStepResultUnion(`{"response": "Very cold. 22 degrees Fahrenheit."}`),
            })

            finalRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model:                 interactions.Model("gemini-3-flash-preview"),
                    PreviousInteractionID: res.Interaction.ID,
                    Tools:                 tools,
                    Input:                 interactions.NewInteractionsInput([]interactions.Step{funcResult}),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            if finalRes.Interaction.OutputText != nil {
                fmt.Println(*finalRes.Interaction.OutputText)
            }
            break
        }
    }
}
```

## Migração do Gemini 2.5

O Gemini 3 é nossa família de modelos mais avançada até o momento e oferece uma melhoria gradual em relação ao Gemini 2.5. Ao migrar, considere o seguinte:

- **Raciocínio**:se você usava engenharia de comandos complexa (como cadeia de pensamento) para forçar o Gemini 2.5 a raciocinar, teste o Gemini 3 com `thinking_level: "high"` e comandos simplificados.
- **Configurações de temperatura**:se o código atual definir explicitamente a temperatura (especialmente para valores baixos em saídas determinísticas), recomendamos remover esse parâmetro e usar o padrão do Gemini 3, que é 1,0, para evitar possíveis problemas de loop ou degradação de desempenho em tarefas complexas.
- **PDF e compreensão de documentos**:se você dependia de um comportamento específico para a análise de documentos densos, teste a nova configuração
  `media_resolution_high` para garantir a precisão contínua.
- **Consumo de tokens**:a migração para os padrões do Gemini 3 pode **aumentar** o uso de tokens para PDFs, mas **diminuir** o uso de tokens para vídeos. Se as solicitações excederem a janela de contexto devido a resoluções padrão mais altas, recomendamos reduzir explicitamente a resolução da mídia.
- **Segmentação de imagens**:os recursos de segmentação de imagens (que retornam máscaras no nível do pixel para objetos) não são compatíveis com o Gemini 3 Pro ou o Gemini 3 Flash. Para
  fluxos de trabalho que exigem segmentação de imagens integrada, recomendamos continuar usando
  o Gemini 2.5 Flash com o recurso de pensamento desativado.
- **Uso de computador**:o Gemini 3 Pro e o Gemini 3 Flash são compatíveis com o [Uso de computador](https://ai.google.dev/gemini-api/docs/computer-use?hl=pt-br). Ao contrário da série 2.5, não é necessário usar um modelo separado para acessar a ferramenta "Uso do computador".
- **Suporte a ferramentas**: agora é possível [combinar ferramentas integradas com a chamada de função](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pt-br) nos modelos do Gemini 3. Agora, a [ancoragem do Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pt-br) também é compatível com os modelos do Gemini 3.

## Compatibilidade com a OpenAI

Para usuários que utilizam a [compatibilidade com a OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pt-br),
os parâmetros padrão (`reasoning_effort` do OpenAI) são mapeados automaticamente para
equivalentes do Gemini (`thinking_level`).

## Práticas recomendadas para comandos

O Gemini 3 é um modelo de raciocínio, o que muda a forma como você precisa dar comandos.

- **Instruções precisas**:seja conciso nos comandos de entrada. O Gemini 3 responde melhor a instruções diretas e claras. Ela pode analisar demais técnicas de engenharia de comandos detalhadas ou complexas usadas em modelos mais antigos.
- **Nível de detalhe da saída**:por padrão, o Gemini 3 é menos detalhista e prefere dar respostas diretas e eficientes. Se o caso de uso exigir uma persona mais conversacional ou "falante", você precisa direcionar explicitamente o modelo no comando (por exemplo, "Explique isso como um assistente amigável e falante").
- **Gerenciamento de contexto**:ao trabalhar com grandes conjuntos de dados (por exemplo, livros inteiros, bases de código ou vídeos longos), coloque suas instruções ou perguntas específicas no final do comando, depois do contexto de dados. Ancore o raciocínio do modelo nos dados fornecidos começando sua pergunta com uma frase como "Com base nas informações anteriores...".

Saiba mais sobre estratégias de design de comandos no [guia de engenharia de comandos](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pt-br).

## Perguntas frequentes

1. **Qual é o limite de conhecimento do Gemini 3?** Os modelos do Gemini 3 têm uma data limite de conhecimento de janeiro de 2025. Para informações mais recentes, use a ferramenta [Embasamento da pesquisa](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br).
2. **Quais são os limites da janela de contexto?** Os modelos do Gemini 3 oferecem suporte a uma janela de contexto de entrada de 1 milhão de tokens e até 64 mil tokens de saída.
3. **Existe um nível sem custo financeiro para o Gemini 3?** O Gemini 3 Flash
   `gemini-3-flash-preview` tem um nível sem custo financeiro na API Gemini. Você pode testar o
   Gemini 3.1 Pro e o 3 Flash sem custo no Google AI Studio, mas não
   há um nível sem custo financeiro disponível para `gemini-3.1-pro-preview` na API Gemini.
4. **Meu código `thinking_budget` antigo ainda vai funcionar?** Sim, o `thinking_budget` ainda tem suporte para compatibilidade com versões anteriores, mas recomendamos migrar para o `thinking_level` para ter uma performance mais previsível. Não use os dois na mesma
   solicitação.
5. **O Gemini 3 é compatível com a API Batch?** Sim, o Gemini 3 é compatível com a
   [API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br).
6. **O armazenamento em cache de contexto é compatível?** Sim, o [armazenamento em cache de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br) é compatível com o Gemini 3.
7. **Quais ferramentas são compatíveis com o Gemini 3?** O Gemini 3 é compatível com
   [Pesquisa Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br),
   [Embasamento com o Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pt-br),
   [Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/file-search?hl=pt-br),
   [Execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br) e
   [Contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br). Ele também oferece suporte a
   [chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br) padrão para
   suas próprias ferramentas personalizadas e em
   [combinação com ferramentas integradas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pt-br).
8. **O que é `gemini-3.1-pro-preview-customtools`?** Se você estiver usando
   `gemini-3.1-pro-preview` e o modelo ignorar suas ferramentas personalizadas em favor de
   comandos bash, tente o modelo `gemini-3.1-pro-preview-customtools`.
   Mais informações [aqui][customtools-model].

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-09 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-09 UTC."],[],[]]
