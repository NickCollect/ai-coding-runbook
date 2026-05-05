---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=fr
fetched_at: 2026-05-05T19:43:56.125430+00:00
title: "Embeddings \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Embeddings

L'API Gemini propose des modèles d'embedding pour générer des embeddings pour du texte, des images, des vidéos et d'autres contenus. Les embeddings obtenus peuvent ensuite être utilisés pour des tâches telles que la recherche sémantique, la classification et le clustering. Ils fournissent des résultats plus précis et plus adaptés au contexte que les approches basées sur les mots clés.

Le dernier modèle, `gemini-embedding-2`, est le premier modèle d'embedding multimodal de l'API Gemini. Il mappe le texte, les images, les vidéos, l'audio et les documents dans un espace d'embedding unifié, ce qui permet la recherche, la classification et le clustering cross-modal dans plus de 100 langues. Pour en savoir plus, consultez la section [Embeddings multimodaux](#multimodal). Pour les cas d'utilisation uniquement basés sur du texte, `gemini-embedding-001` reste disponible.

La création de systèmes de génération augmentée par récupération (RAG) est un cas d'utilisation courant pour les produits d'IA. Les embeddings jouent un rôle clé dans l'amélioration significative des résultats des modèles, en offrant une meilleure précision factuelle, une meilleure cohérence et une meilleure richesse contextuelle. Si vous préférez utiliser une solution RAG gérée, nous avons créé l'outil [Recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr), qui facilite la gestion et réduit les coûts du RAG.

## Générer des embeddings

Utilisez la méthode `embedContent` pour générer des embeddings de texte :

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

## Spécifier le type de tâche pour améliorer les performances

Vous pouvez utiliser des embeddings pour un large éventail de tâches, de la classification à la recherche de documents. Spécifier le bon type de tâche permet d'optimiser les embeddings pour les relations souhaitées, ce qui maximise la précision et l'efficacité.

### Types de tâches avec Embeddings 2

Pour les tâches textuelles avec `gemini-embedding-2`, nous vous recommandons vivement d'ajouter les instructions de la tâche dans votre requête. Pour ce faire, mettez en forme la requête et le document avec le préfixe de tâche approprié.

Les tableaux suivants montrent des exemples de mise en forme des requêtes et des documents pour les cas d'utilisation symétriques et asymétriques à l'aide du modèle `gemini-embedding-2`.

**Cas d'utilisation de la récupération (format asymétrique)**

Dans les cas d'utilisation asymétriques, ajoutez le préfixe de la tâche à la requête et appliquez la structure du document pour le contenu que vous souhaitez intégrer et récupérer.

| Cas d'utilisation | Structure d'une requête | Structure du document |
| --- | --- | --- |
| Requête de recherche | `task: search result | query: {content}` | `title: {title} | text: {content}` S'il n'y a pas de titre, utilisez `title: none`. |
| Systèmes de questions-réponses | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| Fact-checking | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| Récupération du code | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**Exemple d'utilisation**

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

**Cas d'utilisation à entrée unique (format symétrique)**

Dans les cas d'utilisation symétriques, utilisez le même format pour la requête et le document pour une même tâche.

| Cas d'utilisation | Structure d'entrée |
| --- | --- |
| Classification | `task: classification | query: {content}` |
| Clustering | `task: clustering | query: {content}` |
| Similarité sémantique | `task: sentence similarity | query: {content}` Ne pas utiliser pour la recherche ou la récupération. Elle est destinée à la similarité textuelle sémantique. |

**Exemple d'utilisation**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

Il est important que la tâche soit utilisée de manière cohérente. Par exemple, si les documents sont intégrés avec `f'task: classification | query: {content}'`, la requête doit également être intégrée en suivant ce format de tâche.

### Types de tâches avec Embeddings 1

Pour `gemini-embedding-001`, vous pouvez spécifier `task_type` dans la méthode `embedContent`. Pour obtenir la liste complète des types de tâches acceptés, consultez le tableau [Types de tâches acceptés](#supported-task-types).

L'exemple suivant montre comment utiliser `SEMANTIC_SIMILARITY` pour vérifier la similarité sémantique de chaînes de texte.

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

Les extraits de code montreront à quel point les différents blocs de texte sont similaires les uns aux autres lorsqu'ils sont exécutés.

#### Types de tâches compatibles

Types de tâches compatibles avec `gemini-embedding-001` :

| Type de tâche | Description | Exemples |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | Embeddings optimisés pour évaluer la similitude de texte. | Systèmes de recommandation, détection des doublons |
| **CLASSIFICATION** | Embeddings optimisés pour classer des textes en fonction d'étiquettes prédéfinies. | Analyse des sentiments, détection du spam |
| **CLUSTERING** | Embeddings optimisés pour regrouper des textes en fonction de leurs similitudes. | Organisation de documents, études de marché, détection d'anomalies |
| **RETRIEVAL\_DOCUMENT** | Embeddings optimisés pour la recherche de documents. | Indexation d'articles, de livres ou de pages Web pour la recherche. |
| **RETRIEVAL\_QUERY** | Embeddings optimisés pour les requêtes de recherche générales. Utilisez `RETRIEVAL_QUERY` pour les requêtes et `RETRIEVAL_DOCUMENT` pour les documents à récupérer. | Tests personnalisés sur le Réseau de Recherche |
| **CODE\_RETRIEVAL\_QUERY** | Embeddings optimisés pour la récupération de blocs de code en fonction de requêtes en langage naturel. Utilisez `CODE_RETRIEVAL_QUERY` pour les requêtes et `RETRIEVAL_DOCUMENT` pour les blocs de code à récupérer. | Suggestions de code et recherche |
| **QUESTION\_ANSWERING** | Embeddings pour les questions dans un système de questions-réponses, optimisés pour trouver les documents qui répondent à la question. Utilisez `QUESTION_ANSWERING` pour les questions et `RETRIEVAL_DOCUMENT` pour les documents à récupérer. | Chatbox |
| **FACT\_VERIFICATION** | Embeddings pour les déclarations à valider, optimisés pour récupérer les documents contenant des preuves qui soutiennent ou réfutent la déclaration. Utilisez `FACT_VERIFICATION` pour le texte cible et `RETRIEVAL_DOCUMENT` pour les documents à récupérer. | Systèmes de fact-checking automatisés |

## Contrôler la taille de l'intégration

`gemini-embedding-001` et `gemini-embedding-2` sont tous deux entraînés à l'aide de la technique d'apprentissage de la représentation Matryoshka (MRL, Matryoshka Representation Learning), qui apprend à un modèle à apprendre des embeddings de grande dimension dont les segments initiaux (ou préfixes) sont également des versions plus simples et utiles des mêmes données.

Utilisez le paramètre `output_dimensionality` pour contrôler la taille du vecteur d'embedding de sortie. En sélectionnant une dimensionnalité de sortie plus petite, vous pouvez économiser de l'espace de stockage et augmenter l'efficacité des calculs pour les applications en aval, tout en sacrifiant peu de qualité. Par défaut, les deux modèles génèrent un embedding de 3 072 dimensions, mais vous pouvez le tronquer à une taille plus petite sans perdre en qualité pour économiser de l'espace de stockage. Nous vous recommandons d'utiliser des dimensions de sortie de 768, 1 536 ou 3 072.

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

Exemple de résultat de l'extrait de code :

```
Length of embedding: 768
```

## Garantir la qualité pour les dimensions plus petites

Alors que les embeddings de dimension 3072 par défaut sont toujours normalisés, Gemini Embedding 2 normalise également automatiquement les dimensions tronquées (par exemple, 768, 1536). Cela garantit que la similarité sémantique est calculée à l'aide de la direction du vecteur plutôt que de son amplitude, ce qui permet d'obtenir des résultats plus précis prêts à l'emploi.

**Anciens modèles** : si vous utilisez `gemini-embedding-001`, vous devez normaliser manuellement les dimensions non 3072 comme suit :

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

Exemple de résultat de cet extrait de code :

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

Le tableau suivant présente les scores MTEB, un benchmark couramment utilisé pour les embeddings, pour différentes dimensions. Le résultat montre notamment que les performances ne sont pas strictement liées à la taille de la dimension d'intégration, les dimensions inférieures obtenant des scores comparables à ceux de leurs homologues de dimension supérieure.

| Dimension MRL | Score MTEB (Gemini Embedding 001) |
| --- | --- |
| 2048 | 68.16 |
| 1536 | 68.17 |
| 768 | 67.99 |
| 512 | 67,55 |
| 256 | 66,19 |
| 128 | 63.31 |

## Embeddings multimodaux

Le modèle `gemini-embedding-2` accepte les entrées multimodales, ce qui vous permet d'intégrer des images, des vidéos, des contenus audio et des documents en plus du texte. Toutes les modalités sont mappées dans le même espace d'embedding, ce qui permet la recherche et la comparaison intermodales.

### Modalités et limites acceptées

La limite globale maximale de jetons d'entrée est de 8 192 jetons.

| Modalité | Spécifications et limites |
| --- | --- |
| **Texte** | Il accepte jusqu'à 8 192 jetons. |
| **Image** | Six images maximum par requête. Formats acceptés : PNG, JPEG. |
| **Audio** | Durée maximale de 180 secondes. Formats compatibles : MP3, WAV. |
| **Vidéo** | Durée maximale de 120 secondes. Formats acceptés : MP4, MOV. Codecs compatibles : H264, H265, AV1, VP9.  Le système traite un maximum de 32 images par vidéo : les vidéos courtes (≤ 32 s) sont échantillonnées à 1 FPS, tandis que les vidéos plus longues sont échantillonnées de manière uniforme à 32 images. Les pistes audio ne sont pas traitées dans les fichiers vidéo. |
| **Documents (PDF)** | Six pages maximum. |

### Intégrer des images

L'exemple suivant montre comment intégrer une image à l'aide de `gemini-embedding-2`.

Les images peuvent être fournies sous forme de données intégrées ou de fichiers importés via l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr).

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

### Agrégation d'embeddings

Lorsque vous travaillez avec du contenu multimodal, la façon dont vous structurez votre entrée affecte la sortie d'embedding :

- **Plusieurs parties (agrégées)** : l'ajout de plusieurs entrées directement au paramètre `contents` produit un embedding agrégé pour toutes les entrées.
- **Plusieurs objets `Content` (séparés)** : en encapsulant chaque entrée dans un objet `Content` et en les transmettant dans le paramètre `contents`, des embeddings distincts sont renvoyés pour chaque entrée.
- **Représentation au niveau du post** : pour les objets complexes tels que les posts sur les réseaux sociaux comportant plusieurs éléments multimédias, nous vous recommandons d'agréger des embeddings distincts (par exemple, en les moyennant) afin de créer une représentation cohérente au niveau du post.

L'exemple suivant montre comment créer un embedding agrégé pour les entrées de texte et d'image. Il vous suffit d'ajouter plusieurs entrées au paramètre `contents` :

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

En revanche, si vous utilisez des objets `Content` dans le paramètre `contents`, il renvoie des embeddings distincts. Cet exemple crée plusieurs embeddings en un seul appel d'embedding :

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

### Intégrer de l'audio

L'exemple suivant montre comment intégrer un fichier audio à l'aide de `gemini-embedding-2`.

Les fichiers audio peuvent être fournis sous forme de données intégrées ou de fichiers importés via l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr).

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

### Intégrer une vidéo

L'exemple suivant montre comment intégrer une vidéo à l'aide de `gemini-embedding-2`.

Les vidéos peuvent être fournies sous forme de données intégrées ou de fichiers importés via l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr).

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

Si vous devez intégrer des vidéos de plus de 120 secondes, vous pouvez les découper en segments qui se chevauchent et intégrer ces segments individuellement.

### Intégrer des documents

Les documents au format PDF peuvent être intégrés directement. Le modèle traite le contenu visuel et textuel de chaque page.

Les fichiers PDF peuvent être fournis sous forme de données intégrées ou de fichiers importés via l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr).

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

## Cas d'utilisation

Les embeddings de texte sont essentiels pour de nombreux cas d'utilisation courants de l'IA, tels que :

- **Génération augmentée par récupération (RAG)** : les embeddings améliorent la qualité du texte généré en récupérant et en intégrant des informations pertinentes dans le contexte d'un modèle.
- **Récupération d'informations** : recherchez le texte ou les documents les plus similaires d'un point de vue sémantique à partir d'un texte d'entrée.

  [Tutoriel sur la recherche de documentstask](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **Reclassement des résultats de recherche** : classez les éléments les plus pertinents en attribuant un score sémantique aux résultats initiaux par rapport à la requête.

  [Tutoriel sur le réordonnancement des résultats de recherchetask](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **Détection des anomalies** : la comparaison de groupes d'embeddings peut aider à identifier des tendances ou des valeurs aberrantes cachées.

  [Tutoriel sur la détection d'anomaliesbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **Classification** : catégorisez automatiquement le texte en fonction de son contenu, comme l'analyse des sentiments ou la détection du spam.

  [Tutoriel sur la classificationtoken](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **Clustering** : comprenez efficacement les relations complexes en créant des clusters et des visualisations de vos embeddings.

  [Tutoriel sur la visualisation du clusteringbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## Stocker les embeddings

Lorsque vous déployez des embeddings en production, il est courant d'utiliser des **bases de données vectorielles** pour stocker, indexer et récupérer efficacement des embeddings de grande dimension. Google Cloud propose des services de données gérés qui peuvent être utilisés à cette fin, y compris [Gemini Enterprise Agent Platform Vector Search 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/BUILD/vector-search-2?hl=fr), [BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=fr), [AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=fr) et [Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=fr).

Les tutoriels suivants montrent comment utiliser d'autres bases de données vectorielles tierces avec Gemini Embedding.

- [Tutoriels ChromaDBbolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [Tutoriels QDrantbolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [Tutoriels Weaviatebolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [Tutoriels Pineconebolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## Versions de modèle

### Embedding Gemini 2

| Propriété | Description |
| --- | --- |
| Code du modèle id\_card | **API Gemini**  `gemini-embedding-2` |
| Types de données acceptés pour save | **Entrée**  Texte, image, vidéo, audio, PDF  **Résultat**  Embeddings textuels |
| token\_autoLimites de jetons[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=fr) | **Limite de jetons d'entrée**  8 192  **Taille de la dimension de sortie**  Flexible, prend en charge : 128 à 3 072, recommandé : 768, 1 536, 3 072 |
| Versions 123 | Pour en savoir plus, consultez les [schémas de version de modèle](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#model-versions).  - Stable : `gemini-embedding-2` |
| calendar\_monthDernière mise à jour | Avril 2026 |

### Embedding Gemini

| Propriété | Description |
| --- | --- |
| Code du modèle id\_card | **API Gemini**  `gemini-embedding-001` |
| Types de données acceptés pour save | **Entrée**  Texte  **Résultat**  Embeddings textuels |
| token\_autoLimites de jetons[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=fr) | **Limite de jetons d'entrée**  2 048  **Taille de la dimension de sortie**  Flexible, prend en charge : 128 à 3 072, recommandé : 768, 1 536, 3 072 |
| Versions 123 | Pour en savoir plus, consultez les [schémas de version de modèle](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#model-versions).  - Stable : `gemini-embedding-001` |
| calendar\_monthDernière mise à jour | Juin 2025 |

Pour les modèles d'embeddings obsolètes, consultez la page [Obsolescence](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr).

## Migration depuis gemini-embedding-001

Les espaces d'intégration entre `gemini-embedding-001` et `gemini-embedding-2` sont **incompatibles**. Cela signifie que vous ne pouvez pas comparer directement les embeddings générés par un modèle avec ceux générés par l'autre. Si vous passez à `gemini-embedding-2`, vous devez réintégrer toutes vos données existantes.

Outre l'incompatibilité, il existe plusieurs autres différences notables entre les deux modèles :

- **Spécification du type de tâche** : avec `gemini-embedding-001`, vous spécifiez le type de tâche à l'aide du paramètre `task_type` (par exemple, `SEMANTIC_SIMILARITY`, `RETRIEVAL_DOCUMENT`). Avec `gemini-embedding-2`, le paramètre `task_type` n'est pas accepté. Au lieu de cela, vous devez inclure les instructions de la tâche directement dans la requête pour les tâches textuelles. Pour savoir comment mettre en forme les requêtes pour différents cas d'utilisation, consultez [Types de tâches avec Embeddings 2](#task-types-embeddings-2).
- **Agrégation d'embeddings** : `gemini-embedding-001` génère des embeddings individuels pour chaque chaîne d'une liste d'entrées. En revanche, `gemini-embedding-2` produit un seul embedding agrégé lorsque plusieurs entrées (comme du texte et des images) sont fournies directement dans une même requête. Pour générer des embeddings distincts pour chaque entrée, enveloppez chaque entrée dans un objet `Content` ou utilisez l'[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr#batch-embedding). Pour en savoir plus, consultez [Agrégation d'intégration](#embedding-aggregation).
- **Normalisation** : si vous utilisez `output_dimensionality` pour demander des embeddings avec moins de 3 072 dimensions, `gemini-embedding-2` normalise automatiquement ces embeddings tronqués. Avec `gemini-embedding-001`, vous devez effectuer une normalisation manuelle pour les dimensions autres que 3 072. Pour en savoir plus, consultez [Garantir la qualité pour les dimensions plus petites](#quality-for-smaller-dimensions).

## Embeddings par lot

Si la latence n'est pas un problème, essayez d'utiliser les modèles d'embeddings Gemini avec l'[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr#batch-embedding). Cela permet un débit beaucoup plus élevé à 50% du prix par défaut des embeddings.
Vous trouverez des exemples pour vous aider à vous lancer dans le [cookbook de l'API Batch](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb).

## Avis sur l'utilisation responsable

Contrairement aux modèles d'IA générative qui créent du contenu, le modèle Gemini Embedding est uniquement destiné à transformer le format de vos données d'entrée en représentation numérique. Bien que Google soit responsable de la fourniture d'un modèle d'embedding qui transforme le format de vos données d'entrée au format numérique demandé, les utilisateurs conservent l'entière responsabilité des données qu'ils saisissent et des embeddings qui en résultent. En utilisant le modèle d'embedding Gemini, vous confirmez que vous disposez des droits nécessaires sur tous les contenus que vous mettez en ligne. Ne générez aucun contenu qui porte atteinte à la propriété intellectuelle ou aux droits au respect de la confidentialité d'autrui. Votre utilisation de ce service est soumise à notre [Règlement sur les utilisations interdites](https://policies.google.com/terms/generative-ai/use-policy?hl=fr) et aux [Conditions d'utilisation de Google](https://ai.google.dev/gemini-api/terms?hl=fr).

## Commencer à créer avec des embeddings

Consultez le [notebook de démarrage rapide sur les embeddings](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb) pour explorer les capacités du modèle et découvrir comment personnaliser et visualiser vos embeddings.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/05/01 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/05/01 (UTC)."],[],[]]
