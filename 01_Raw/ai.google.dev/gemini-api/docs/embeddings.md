---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=pt-BR
fetched_at: 2026-05-25T05:27:06.050594+00:00
title: "Embeddings \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Embeddings

A API Gemini oferece modelos de incorporação para gerar incorporações de texto, imagens, vídeo e outros conteúdos. Os embeddings resultantes podem ser usados para tarefas como pesquisa semântica, classificação e agrupamento, fornecendo resultados mais precisos e contextualizados do que abordagens baseadas em palavras-chave.

O modelo mais recente, `gemini-embedding-2`, é o primeiro modelo de incorporação multimodal na API Gemini. Ele mapeia texto, imagens, vídeo, áudio e documentos em um espaço de embedding unificado, permitindo pesquisa, classificação e clustering entre modalidades em mais de 100 idiomas. Consulte a [seção de embeddings multimodais](#multimodal) para saber mais. Para casos de uso somente de texto, o `gemini-embedding-001` continua disponível.

A criação de sistemas de geração aumentada de recuperação (RAG) é um caso de uso comum para
produtos de IA. As incorporações são fundamentais para melhorar significativamente os resultados do modelo com mais acurácia factual, coerência e riqueza contextual. Se preferir usar uma solução de RAG gerenciada, criamos a ferramenta [Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/file-search?hl=pt-br), que facilita o gerenciamento e reduz os custos da RAG.

## Gerar embeddings

Use o método `embedContent` para gerar embeddings de texto:

### Python

```
from google import genai

client = genai.Client()

result = client.models.embed_content(
        model="gemini-embedding-2",
        contents="What is the meaning of life?"
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

async function main() {

    const ai = new GoogleGenAI({});

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: 'What is the meaning of life?',
    });

    console.log(response.embeddings);
}

main();
```

### Go

```
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    contents := []*genai.Content{
        genai.NewContentFromText("What is the meaning of life?", genai.RoleUser),
    }
    result, err := client.Models.EmbedContent(ctx,
        "gemini-embedding-2",
        contents,
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }

    embeddings, err := json.MarshalIndent(result.Embeddings, "", "  ")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(string(embeddings))
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "model": "models/gemini-embedding-2",
        "content": {
        "parts": [{
            "text": "What is the meaning of life?"
        }]
        }
    }'
```

## Especificar o tipo de tarefa para melhorar a performance

É possível usar embeddings para várias tarefas, desde classificação até pesquisa de documentos. Especificar o tipo de tarefa certo ajuda a otimizar os embeddings para as relações pretendidas, maximizando a precisão e a eficiência.

### Tipos de tarefa com Embeddings 2

Para tarefas somente de texto com o `gemini-embedding-2`, recomendamos
adicionar a instrução da tarefa no comando. Para isso, formate a consulta e o documento com o prefixo de tarefa correto.

As tabelas a seguir mostram exemplos de como formatar consultas e documentos para casos de uso simétricos e assimétricos usando o modelo `gemini-embedding-2`.

**Casos de uso de recuperação (formato assimétrico)**

Em casos de uso assimétricos, adicione o prefixo da tarefa à consulta e aplique
a estrutura do documento ao conteúdo que você quer incorporar e recuperar.

| Caso de uso | Estrutura da consulta | Estrutura do documento |
| --- | --- | --- |
| Consulta de pesquisa | `task: search result | query: {content}` | `title: {title} | text: {content}` Se não houver um título, use `title: none`. |
| Respostas a perguntas | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| Checagem de fatos | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| Recuperação de código | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**Exemplo de uso**

### Python

```
# Generate embedding for a task's query. Use your correct task here:
def prepare_query(query):
    # return f"task: question answering | query: {query}"
    # return f"task: fact checking | query: {query}"
    # return f"task: code retrieval | query: {query}"
    return f"task: search result | query: {query}"

# Generate embedding for document of an asymmetric retrieval task:
def prepare_document(content, title=None):
    if title is None:
        title = "none"
    return f"title: {title} | text: {content}"
```

**Casos de uso de entrada única (formato simétrico)**

Em casos de uso simétricos, para a mesma tarefa, use a mesma formatação para a consulta e o documento.

| Caso de uso | Estrutura de entrada |
| --- | --- |
| Classificação | `task: classification | query: {content}` |
| Clustering | `task: clustering | query: {content}` |
| Similaridade semântica | `task: sentence similarity | query: {content}` Não use para pesquisa ou recuperação. Ela é destinada à similaridade textual semântica. |

**Exemplo de uso**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

É importante que a tarefa seja usada de forma consistente. Por exemplo, se os documentos forem incorporados com `f'task: classification | query: {content}'`, a consulta também precisará ser incorporada seguindo esse formato de tarefa.

### Tipos de tarefa com Embeddings 1

Para `gemini-embedding-001`, é possível especificar o `task_type` no método `embedContent`. Para uma lista completa dos tipos de tarefas compatíveis, consulte a tabela [Tipos de tarefas compatíveis](#supported-task-types).

O exemplo a seguir mostra como usar `SEMANTIC_SIMILARITY` para verificar a semelhança entre strings de texto.

### Python

```
from google import genai
from google.genai import types
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

client = genai.Client()

texts = [
    "What is the meaning of life?",
    "What is the purpose of existence?",
    "How do I bake a cake?",
]

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=texts,
    config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
)

# Create a 3x3 table to show the similarity matrix
df = pd.DataFrame(
    cosine_similarity([e.values for e in result.embeddings]),
    index=texts,
    columns=texts,
)

print(df)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
// npm i compute-cosine-similarity
import * as cosineSimilarity from "compute-cosine-similarity";

async function main() {
    const ai = new GoogleGenAI({});

    const texts = [
        "What is the meaning of life?",
        "What is the purpose of existence?",
        "How do I bake a cake?",
    ];

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-001',
        contents: texts,
        config: { taskType: 'SEMANTIC_SIMILARITY' },
    });

    const embeddings = response.embeddings.map(e => e.values);

    for (let i = 0; i < texts.length; i++) {
        for (let j = i + 1; j < texts.length; j++) {
            const text1 = texts[i];
            const text2 = texts[j];
            const similarity = cosineSimilarity(embeddings[i], embeddings[j]);
            console.log(`Similarity between '${text1}' and '${text2}': ${similarity.toFixed(4)}`);
        }
    }
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "math"

    "google.golang.org/genai"
)

// cosineSimilarity calculates the similarity between two vectors.
func cosineSimilarity(a, b []float32) (float64, error) {
    if len(a) != len(b) {
        return 0, fmt.Errorf("vectors must have the same length")
    }

    var dotProduct, aMagnitude, bMagnitude float64
    for i := 0; i < len(a); i++ {
        dotProduct += float64(a[i] * b[i])
        aMagnitude += float64(a[i] * a[i])
        bMagnitude += float64(b[i] * b[i])
    }

    if aMagnitude == 0 || bMagnitude == 0 {
        return 0, nil
    }

    return dotProduct / (math.Sqrt(aMagnitude) * math.Sqrt(bMagnitude)), nil
}

func main() {
    ctx := context.Background()
    client, _ := genai.NewClient(ctx, nil)
    defer client.Close()

    texts := []string{
        "What is the meaning of life?",
        "What is the purpose of existence?",
        "How do I bake a cake?",
    }

    var contents []*genai.Content
    for _, text := range texts {
        contents = append(contents, genai.NewContentFromText(text, genai.RoleUser))
    }

    result, _ := client.Models.EmbedContent(ctx,
        "gemini-embedding-001",
        contents,
        &genai.EmbedContentRequest{TaskType: genai.TaskTypeSemanticSimilarity},
    )

    embeddings := result.Embeddings

    for i := 0; i < len(texts); i++ {
        for j := i + 1; j < len(texts); j++ {
            similarity, _ := cosineSimilarity(embeddings[i].Values, embeddings[j].Values)
            fmt.Printf("Similarity between '%s' and '%s': %.4f\n", texts[i], texts[j], similarity)
        }
    }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -d '{
    "taskType": "SEMANTIC_SIMILARITY",
    "content": {
        "parts": [
        {
            "text": "What is the meaning of life?"
        },
        {
            "text": "How much wood would a woodchuck chuck?"
        },
        {
            "text": "How does the brain work?"
        }
        ]
    }
    }'
```

Os snippets de código vão mostrar o quanto os diferentes trechos de texto são semelhantes entre si quando executados.

#### Tipos de tarefas com suporte

Tipos de tarefas compatíveis com `gemini-embedding-001`:

| Tipo de tarefa | Descrição | Exemplos |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | Embeddings otimizados para avaliar a semelhança de texto. | Sistemas de recomendação, detecção de duplicidade |
| **CLASSIFICAÇÃO** | Embeddings otimizados para classificar textos de acordo com rótulos predefinidos. | Análise de sentimento, detecção de spam |
| **CLUSTERING** | Embeddings otimizados para agrupar textos com base nas semelhanças deles. | Organização de documentos, pesquisa de mercado, detecção de anomalias |
| **RETRIEVAL\_DOCUMENT** | Embeddings otimizados para pesquisa de documentos. | Indexação de artigos, livros ou páginas da Web para pesquisa. |
| **RETRIEVAL\_QUERY** | Embeddings otimizados para consultas de pesquisa gerais. Use `RETRIEVAL_QUERY` para consultas e `RETRIEVAL_DOCUMENT` para documentos a serem recuperados. | Pesquisa personalizada |
| **CODE\_RETRIEVAL\_QUERY** | Embeddings otimizados para recuperação de blocos de código com base em consultas de linguagem natural. Use `CODE_RETRIEVAL_QUERY` para consultas e `RETRIEVAL_DOCUMENT` para blocos de código a serem recuperados. | Sugestões e pesquisa de código |
| **QUESTION\_ANSWERING** | Embeddings para perguntas em um sistema de respostas a perguntas, otimizados para encontrar documentos que respondam à pergunta. Use `QUESTION_ANSWERING` para perguntas e `RETRIEVAL_DOCUMENT` para documentos a serem recuperados. | Caixa de chat |
| **FACT\_VERIFICATION** | Embeddings para declarações que precisam ser verificadas, otimizados para recuperar documentos que contenham evidências que apoiem ou refutem a declaração. Use `FACT_VERIFICATION` para o texto de destino e `RETRIEVAL_DOCUMENT` para os documentos a serem recuperados. | Sistemas automatizados de checagem de fatos |

## Como controlar o tamanho do embedding

`gemini-embedding-001` e `gemini-embedding-2` são treinados usando a técnica de aprendizado de representação Matryoshka (MRL, na sigla em inglês), que ensina um modelo a aprender incorporações de alta dimensão com segmentos iniciais (ou prefixos) que também são versões úteis e mais simples dos mesmos dados.

Use o parâmetro `output_dimensionality` para controlar o tamanho do vetor de embedding de saída. Selecionar uma dimensionalidade de saída menor pode economizar espaço de armazenamento e aumentar a eficiência computacional para aplicativos downstream, sem sacrificar muito a qualidade. Por padrão, os dois modelos geram uma incorporação de 3.072 dimensões, mas é possível truncá-la para um tamanho menor sem perder qualidade e economizar espaço de armazenamento. Recomendamos usar dimensões de saída de 768, 1536 ou 3072.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

result = client.models.embed_content(
    model="gemini-embedding-2",
    contents="What is the meaning of life?",
    config=types.EmbedContentConfig(output_dimensionality=768)
)

[embedding_obj] = result.embeddings
embedding_length = len(embedding_obj.values)

print(f"Length of embedding: {embedding_length}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

async function main() {
    const ai = new GoogleGenAI({});

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: 'What is the meaning of life?',
        config: { outputDimensionality: 768 },
    });

    const embeddingLength = response.embeddings[0].values.length;
    console.log(`Length of embedding: ${embeddingLength}`);
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    // The client uses Application Default Credentials.
    // Authenticate with 'gcloud auth application-default login'.
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    contents := []*genai.Content{
        genai.NewContentFromText("What is the meaning of life?", genai.RoleUser),
    }

    result, err := client.Models.EmbedContent(ctx,
        "gemini-embedding-2",
        contents,
        &genai.EmbedContentRequest{OutputDimensionality: 768},
    )
    if err != nil {
        log.Fatal(err)
    }

    embedding := result.Embeddings[0]
    embeddingLength := len(embedding.Values)
    fmt.Printf("Length of embedding: %d\n", embeddingLength)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H 'Content-Type: application/json' \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -d '{
        "content": {"parts":[{ "text": "What is the meaning of life?"}]},
        "output_dimensionality": 768
    }'
```

Exemplo de saída do snippet de código:

```
Length of embedding: 768
```

## Como garantir a qualidade para dimensões menores

Embora os embeddings padrão de 3.072 dimensões sejam sempre normalizados, o Gemini Embedding 2 também normaliza automaticamente as dimensões truncadas (por exemplo, 768, 1536). Isso garante que a similaridade semântica seja calculada por direção vetorial, e não por magnitude, oferecendo resultados mais precisos.

**Modelos mais antigos**: se você estiver usando `gemini-embedding-001`, será necessário normalizar manualmente as dimensões que não sejam 3072 da seguinte maneira:

### Python

```
import numpy as np
from numpy.linalg import norm

# Only for embeddings from `gemini-embedding-001`
embedding_values_np = np.array(embedding_obj.values)
normed_embedding = embedding_values_np / np.linalg.norm(embedding_values_np)

print(f"Normed embedding length: {len(normed_embedding)}")
print(f"Norm of normed embedding: {np.linalg.norm(normed_embedding):.6f}") # Should be very close to 1
```

Exemplo de saída deste snippet de código:

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

A tabela a seguir mostra as pontuações do MTEB, um comparativo de mercado usado com frequência para incorporações, em diferentes dimensões. O resultado mostra que a performance não está estritamente vinculada ao tamanho da dimensão do embedding. Dimensões menores alcançam pontuações comparáveis às maiores.

| Dimensão MRL | Pontuação do MTEB (incorporação do Gemini 001) |
| --- | --- |
| 2048 | 68,16 |
| 1536 | 68,17 |
| 768 | 67,99 |
| 512 | 67,55 |
| 256 | 66,19 |
| 128 | 63,31 |

## Embeddings multimodais

O modelo `gemini-embedding-2` aceita entradas multimodais, permitindo que você
incorpore conteúdo de imagens, vídeos, áudios e documentos junto com texto. Todas as modalidades são mapeadas no mesmo espaço de embedding, permitindo pesquisa e comparação entre modalidades.

### Modalidades e limites compatíveis

O limite máximo geral de tokens de entrada é de 8.192 tokens.

| Modalidade | Especificações e limites |
| --- | --- |
| **Texto** | Aceita até 8.192 tokens. |
| **Imagem** | Máximo de seis imagens por solicitação. Formatos aceitos: PNG e JPEG. |
| **Áudio** | Duração máxima de 180 segundos. Formatos compatíveis: MP3, WAV. |
| **Vídeo** | Duração máxima de 120 segundos. Formatos aceitos: MP4, MOV. Codecs compatíveis: H264, H265, AV1 e VP9.  O sistema processa no máximo 32 frames por vídeo: vídeos curtos (≤32s) são amostrados a 1 fps, enquanto vídeos mais longos são amostrados uniformemente em 32 frames. As faixas de áudio não são processadas em arquivos de vídeo. |
| **Documentos (PDF)** | Máximo de seis páginas. |

### Incorporar imagens

O exemplo a seguir mostra como incorporar uma imagem usando
`gemini-embedding-2`.

As imagens podem ser fornecidas como dados in-line ou como arquivos enviados por upload pela [API Files](https://ai.google.dev/gemini-api/docs/files?hl=pt-br).

### Python

```
from google import genai
from google.genai import types

with open('example.png', 'rb') as f:
    image_bytes = f.read()

client = genai.Client()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/png',
        ),
    ]
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const imgBase64 = fs.readFileSync("example.png", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'image/png',
                data: imgBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### REST

```
IMG_PATH="/path/to/your/image.png"
IMG_BASE64=$(base64 -w0 "${IMG_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "image/png",
                    "data": "'"${IMG_BASE64}"'"
                }
            }]
        }
    }'
```

### Agregação de incorporações

Ao trabalhar com conteúdo multimodal, a forma como você estrutura a entrada afeta a saída de incorporação:

- **Várias partes (agregadas)**: adicionar várias entradas diretamente ao parâmetro `contents` produz uma incorporação agregada para todas as entradas.
- **Vários objetos `Content` (separados)**: ao encapsular cada entrada em um objeto `Content` e transmiti-los no parâmetro `contents`, você recebe incorporações separadas para cada entrada.
- **Representação no nível da postagem**:para objetos complexos, como postagens em redes sociais com vários itens de mídia, recomendamos agregar incorporações separadas (por exemplo, fazendo a média) para criar uma representação coerente no nível da postagem.

O exemplo a seguir mostra como criar um embedding agregado para entrada de texto e imagem. Basta adicionar várias entradas ao parâmetro `contents`:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('dog.png', 'rb') as f:
    image_bytes = f.read()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        "An image of a dog",
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/png',
        ),
    ]
)

# This produces one embedding
for embedding in result.embeddings:
    print(embedding.values)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const imgBase64 = fs.readFileSync("dog.png", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [
            'An image of a dog',
            {
                inlineData: {
                    mimeType: 'image/png',
                    data: imgBase64,
                },
            },
        ],
    });

    // This produces one embedding
    for (const embedding of response.embeddings) {
        console.log(embedding.values);
    }
}

main();
```

### REST

```
IMG_PATH="/path/to/your/dog.png"
IMG_BASE64=$(base64 -w0 "${IMG_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [
                {"text": "An image of a dog"},
                {
                    "inline_data": {
                        "mime_type": "image/png",
                        "data": "'"${IMG_BASE64}"'"
                    }
                }
            ]
        }
    }'
```

Por outro lado, se você usar objetos `Content` dentro do parâmetro `contents`,
serão retornados encodings separados. Este exemplo cria vários embeddings em uma
chamada de embedding:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('dog.png', 'rb') as f:
    image_bytes = f.read()

result = client.models.embed_content(
    model="gemini-embedding-2",
    contents=[
        types.Content(parts=[types.Part.from_text(text="An image of a dog")]),
        types.Content(
            parts=[
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type="image/png",
                ),
            ]
        ),
    ],
)

# This produces two embeddings
for embedding in result.embeddings:
    print(embedding.values)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const imgBase64 = fs.readFileSync("dog.png", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [
            { parts: [{ text: 'An image of a dog' }] },
            {
                parts: [{
                    inlineData: {
                        mimeType: 'image/png',
                        data: imgBase64,
                    },
                }],
            },
        ],
    });

    // This produces two embeddings
    for (const embedding of response.embeddings) {
        console.log(embedding.values);
    }
}

main();
```

### REST

```
IMG_PATH="/path/to/your/dog.png"
IMG_BASE64=$(base64 -w0 "${IMG_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:batchEmbedContents" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "requests": [
            {
                "model": "models/gemini-embedding-2",
                "content": {"parts": [{"text": "An image of a dog"}]}
            },
            {
                "model": "models/gemini-embedding-2",
                "content": {"parts": [{"inline_data": {"mime_type": "image/png", "data": "'"${IMG_BASE64}"'"}}]}
            }
        ]
    }'
```

### Incorporar áudio

O exemplo a seguir mostra como incorporar um arquivo de áudio usando
`gemini-embedding-2`.

Os arquivos de áudio podem ser fornecidos como dados inline ou como arquivos enviados por upload
pela [API Files](https://ai.google.dev/gemini-api/docs/files?hl=pt-br).

### Python

```
from google import genai
from google.genai import types

with open('example.mp3', 'rb') as f:
    audio_bytes = f.read()

client = genai.Client()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=audio_bytes,
            mime_type='audio/mpeg',
        ),
    ]
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const audioBase64 = fs.readFileSync("example.mp3", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'audio/mpeg',
                data: audioBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### REST

```
AUDIO_PATH="/path/to/your/example.mp3"
AUDIO_BASE64=$(base64 -w0 "${AUDIO_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "audio/mpeg",
                    "data": "'"${AUDIO_BASE64}"'"
                }
            }]
        }
    }'
```

### Incorporar vídeo

O exemplo a seguir mostra como incorporar um vídeo usando
`gemini-embedding-2`.

Os vídeos podem ser fornecidos como dados inline ou como arquivos enviados por upload
pela [API Files](https://ai.google.dev/gemini-api/docs/files?hl=pt-br).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('example.mp4', 'rb') as f:
    video_bytes = f.read()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=video_bytes,
            mime_type='video/mp4',
        ),
    ]
)

print(result.embeddings[0].values)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const videoBase64 = fs.readFileSync("example.mp4", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'video/mp4',
                data: videoBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### REST

```
VIDEO_PATH="/path/to/your/video.mp4"
VIDEO_BASE64=$(base64 -w0 "${VIDEO_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "video/mp4",
                    "data": "'"${VIDEO_BASE64}"'"
                }
            }]
        }
    }'
```

Se você precisar incorporar vídeos com mais de 120 segundos, divida o conteúdo em segmentos sobrepostos e incorpore cada um deles individualmente.

### Incorporação de documentos

documentos em formato PDF podem ser incorporados diretamente. O modelo processa o conteúdo visual e de texto de cada página.

Os PDFs podem ser fornecidos como dados inline ou como arquivos enviados pela [API Files](https://ai.google.dev/gemini-api/docs/files?hl=pt-br).

### Python

```
from google import genai
from google.genai import types

with open('example.pdf', 'rb') as f:
    pdf_bytes = f.read()

client = genai.Client()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=pdf_bytes,
            mime_type='application/pdf',
        ),
    ]
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const pdfBase64 = fs.readFileSync("example.pdf", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'application/pdf',
                data: pdfBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### REST

```
PDF_PATH="/path/to/your/example.pdf"
PDF_BASE64=$(base64 -w0 "${PDF_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "application/pdf",
                    "data": "'"${PDF_BASE64}"'"
                }
            }]
        }
    }'
```

## Casos de uso

As incorporações de texto são cruciais para vários casos de uso comuns de IA, como:

- **Geração aumentada por recuperação (RAG)**: os embeddings melhoram a qualidade do texto gerado ao recuperar e incorporar informações relevantes ao contexto de um modelo.
- **Recuperação de informações**:pesquise o texto ou os documentos mais semelhantes semanticamente com base em um trecho de texto de entrada.

  [Tutorial de pesquisa de documentostask](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **Reclassificação da pesquisa**: priorize os itens mais relevantes ao pontuar semanticamente os resultados iniciais em relação à consulta.

  [Tutorial de reclassificação da pesquisatask](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **Detecção de anomalias**:comparar grupos de embeddings pode ajudar a identificar tendências ou outliers ocultos.

  [Tutorial de detecção de anomaliasbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **Classificação**:categoriza automaticamente o texto com base no conteúdo, como análise de sentimento ou detecção de spam.

  [Tutorial de classificaçãotoken](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **Clustering**:entenda relações complexas criando clusters e visualizações dos seus embeddings.

  [Tutorial de visualização de clusteringbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## Armazenar embeddings

Ao levar embeddings para a produção, é comum usar **bancos de dados vetoriais** para armazenar, indexar e recuperar embeddings de alta dimensão com eficiência. O Google Cloud oferece serviços de dados gerenciados que podem ser usados para essa finalidade, incluindo [Pesquisa de vetor da plataforma do agente Gemini Enterprise 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/BUILD/vector-search-2?hl=pt-br), [BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=pt-br), [AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=pt-br) e [Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=pt-br).

Os tutoriais a seguir mostram como usar outros bancos de dados de vetores de terceiros com o Gemini Embedding.

- [Tutoriais do ChromaDBbolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [Tutoriais do QDrantbolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [Tutoriais do Weaviatebolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [Tutoriais do Pineconebolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## Versões do modelo

### Embedding do Gemini 2

| Propriedade | Descrição |
| --- | --- |
| Código do modelo id\_card | **API Gemini**  `gemini-embedding-2` |
| saveTipos de dados aceitos | **Entrada**  Texto, imagem, vídeo, áudio, PDF  **Saída**  Embeddings de textos |
| token\_autoLimites de token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br) | **Limite de tokens de entrada**  8.192  **Tamanho da dimensão de saída**  Flexível, compatível com: 128 a 3072. Recomendado: 768, 1536, 3072 |
| Versões do 123 | Leia os [padrões de versão do modelo](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pt-br#model-versions) para mais detalhes.  - Estável: `gemini-embedding-2` |
| calendar\_monthÚltima atualização | Abril de 2026 |

### Embedding do Gemini

| Propriedade | Descrição |
| --- | --- |
| Código do modelo id\_card | **API Gemini**  `gemini-embedding-001` |
| saveTipos de dados aceitos | **Entrada**  Texto  **Saída**  Embeddings de textos |
| token\_autoLimites de token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br) | **Limite de tokens de entrada**  2.048  **Tamanho da dimensão de saída**  Flexível, compatível com: 128 a 3072. Recomendado: 768, 1536, 3072 |
| Versões do 123 | Leia os [padrões de versão do modelo](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pt-br#model-versions) para mais detalhes.  - Estável: `gemini-embedding-001` |
| calendar\_monthÚltima atualização | Junho de 2025 |

Para modelos de embeddings descontinuados, acesse a página [Descontinuações](https://ai.google.dev/gemini-api/docs/deprecations?hl=pt-br).

## Migração de gemini-embedding-001

Os espaços de incorporação entre `gemini-embedding-001` e `gemini-embedding-2` são **incompatíveis**. Isso significa que não é possível comparar diretamente os embeddings gerados por um modelo com os gerados pelo outro. Se você estiver fazendo upgrade para o `gemini-embedding-2`, será necessário
reincorporar todos os dados atuais.

Além da incompatibilidade, há várias outras diferenças notáveis entre os dois modelos:

- **Especificação do tipo de tarefa**:com `gemini-embedding-001`, você especifica o tipo de tarefa usando o parâmetro `task_type` (por exemplo, `SEMANTIC_SIMILARITY`, `RETRIEVAL_DOCUMENT`). Com `gemini-embedding-2`, o parâmetro `task_type` não é compatível. Em vez disso, inclua instruções de tarefa
  diretamente no comando para tarefas somente de texto. Consulte [Tipos de tarefas com Embeddings 2](#task-types-embeddings-2) para saber como formatar comandos para diferentes casos de uso.
- **Agregação de embeddings**:o `gemini-embedding-001` gera embeddings individuais para cada string em uma lista de entradas. Por outro lado, o `gemini-embedding-2` produz um único embedding agregado quando várias entradas (como texto e imagens) são fornecidas diretamente em uma solicitação. Para
  gerar incorporações separadas para entradas individuais, encapsule cada entrada em um
  objeto `Content` ou use a
  [API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br#batch-embedding). Consulte
  [Agregação de incorporações](#embedding-aggregation) para mais informações.
- **Normalização**:se você usar `output_dimensionality` para solicitar incorporações com menos de 3.072 dimensões, `gemini-embedding-2` normalizará automaticamente essas incorporações truncadas. Com `gemini-embedding-001`, é necessário fazer a normalização manual para dimensões diferentes de 3.072. Consulte
  [Garantir a qualidade para dimensões menores](#quality-for-smaller-dimensions)
  para mais detalhes.

## Embeddings em lote

Se a latência não for um problema, use os modelos de incorporação do Gemini com a [API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br#batch-embedding). Isso permite um throughput muito maior com 50% do preço padrão de incorporação.
Encontre exemplos de como começar no [livro de receitas da API Batch](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb).

## Aviso sobre o uso responsável

Ao contrário dos modelos de IA generativa que criam novos conteúdos, o modelo de incorporação do Gemini
só transforma o formato dos seus dados de entrada em uma representação
numérica. Embora o Google seja responsável por fornecer um modelo de incorporação que transforma o formato dos dados de entrada no formato numérico solicitado, os usuários mantêm total responsabilidade pelos dados inseridos e pelas incorporações resultantes. Ao usar o modelo de embedding do Gemini, você confirma que tem os direitos necessários sobre qualquer conteúdo que enviar. Não gere conteúdo que viole a propriedade intelectual ou os direitos de privacidade de terceiros. O uso deste serviço está sujeito à nossa [Política de Uso Proibido](https://policies.google.com/terms/generative-ai/use-policy?hl=pt-br) e aos [Termos de Serviço do Google](https://ai.google.dev/gemini-api/terms?hl=pt-br).

## Comece a criar com embeddings

Confira o [notebook de início rápido de embeddings](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb) para conhecer os recursos do modelo e aprender a personalizar e visualizar seus embeddings.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-13 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-13 UTC."],[],[]]
