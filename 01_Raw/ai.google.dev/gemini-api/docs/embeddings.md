---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=de
fetched_at: 2026-07-20T04:42:19.383948+00:00
title: "Einbettungen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Einbettungen

Die Gemini API bietet Einbettungsmodelle zum Generieren von Einbettungen für Text, Bilder, Videos und andere Inhalte. Die resultierenden Einbettungen können dann für Aufgaben wie die semantische Suche, Klassifizierung und Clustering verwendet werden. Sie liefern genauere, kontextbezogene Ergebnisse als stichwortbasierte Ansätze.

Das neueste Modell, `gemini-embedding-2`, ist das erste multimodale Embedding-Modell in der Gemini API. Es ordnet Text, Bilder, Videos, Audio und Dokumente einem einheitlichen Einbettungsbereich zu und ermöglicht so die multimodale Suche, Klassifizierung und das Clustering in über 100 Sprachen. Weitere Informationen finden Sie im [Abschnitt zu multimodalen Einbettungen](#multimodal). Für Nur-Text-Anwendungsfälle ist `gemini-embedding-001` weiterhin verfügbar.

Das Erstellen von RAG-Systemen (Retrieval Augmented Generation) ist ein häufiger Anwendungsfall für KI-Produkte. Embeddings spielen eine wichtige Rolle bei der deutlichen Verbesserung der Modellausgaben in Bezug auf faktenorientierte Genauigkeit, Kohärenz und Kontextreichtum. Wenn Sie lieber eine verwaltete RAG-Lösung verwenden möchten, haben wir das Tool [Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de) entwickelt, mit dem sich RAG einfacher verwalten lässt und kostengünstiger ist.

## Einbettungen generieren

Verwenden Sie die Methode `embedContent`, um Texteinbettungen zu generieren:

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

### Ok

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

## Aufgabentyp angeben, um die Leistung zu verbessern

Sie können Einbettungen für eine Vielzahl von Aufgaben verwenden, von der Klassifizierung bis zur Dokumentsuche. Wenn Sie den richtigen Aufgabentyp angeben, werden die Einbettungen für die beabsichtigten Beziehungen optimiert, wodurch die Genauigkeit und Effizienz maximiert werden.

### Aufgabentypen mit Embeddings 2

Bei reinen Textaufgaben mit `gemini-embedding-2` empfehlen wir dringend, die Aufgabenanweisung in den Prompt aufzunehmen. Dazu müssen Sie die Anfrage und das Dokument mit dem richtigen Aufgabenpräfix formatieren.

In den folgenden Tabellen finden Sie Beispiele für die Formatierung von Anfragen und Dokumenten für symmetrische und asymmetrische Anwendungsfälle mit dem Modell `gemini-embedding-2`.

**Abrufanwendungsfälle (asymmetrisches Format)**

In asymmetrischen Anwendungsfällen fügen Sie der Anfrage das Aufgabenpräfix hinzu und wenden Sie die Dokumentstruktur für die Inhalte an, die Sie einbetten und abrufen möchten.

| Anwendungsfall | Abfragestruktur | Dokumentstruktur |
| --- | --- | --- |
| Suchanfrage | `task: search result | query: {content}` | `title: {title} | text: {content}` Wenn kein Titel vorhanden ist, verwenden Sie `title: none`. |
| Question Answering | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| Faktenchecks | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| Codeabruf | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**Beispiel für die Verwendung**

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

**Anwendungsfälle mit einer Eingabe (symmetrisches Format)**

Verwenden Sie in symmetrischen Anwendungsfällen für dieselbe Aufgabe dieselbe Formatierung für die Anfrage und das Dokument.

| Anwendungsfall | Eingabestruktur |
| --- | --- |
| Klassifizierung | `task: classification | query: {content}` |
| Clustering | `task: clustering | query: {content}` |
| Semantische Ähnlichkeit | `task: sentence similarity | query: {content}` Nicht für die Suche oder den Abruf verwenden. Sie ist für die semantische Textähnlichkeit vorgesehen. |

**Beispiel für die Verwendung**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

Es ist wichtig, dass die Aufgabe konsistent verwendet wird. Wenn Dokumente beispielsweise mit `f'task: classification | query: {content}'` eingebettet werden, sollte auch die Anfrage in diesem Aufgabenformat eingebettet werden.

### Aufgabentypen mit Embeddings 1

Für `gemini-embedding-001` können Sie `task_type` in der Methode `embedContent` angeben. Eine vollständige Liste der unterstützten Aufgabentypen finden Sie in der Tabelle [Unterstützte Aufgabentypen](#supported-task-types).

Im folgenden Beispiel wird gezeigt, wie Sie `SEMANTIC_SIMILARITY` verwenden können, um zu prüfen, wie ähnlich sich Textstrings in ihrer Bedeutung sind.

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

### Ok

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

Die Code-Snippets zeigen, wie ähnlich die verschiedenen Textblöcke sind, wenn sie ausgeführt werden.

#### Unterstützte Aufgabentypen

Unterstützte Aufgabentypen für `gemini-embedding-001`:

| Aufgabentyp | Beschreibung | Beispiele |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | Einbettungen, die für die Beurteilung der Textähnlichkeit optimiert sind. | Empfehlungssysteme, Erkennung von Duplikaten |
| **CLASSIFICATION** | Einbettungen, die für die Klassifizierung von Texten nach vordefinierten Labels optimiert sind. | Sentimentanalyse, Spamerkennung |
| **CLUSTERING** | Einbettungen, die für das Clustern von Texten basierend auf ihren Ähnlichkeiten optimiert sind. | Dokumentorganisation, Marktforschung, Anomalieerkennung |
| **RETRIEVAL\_DOCUMENT** | Für die Dokumentsuche optimierte Einbettungen. | Artikel, Bücher oder Webseiten für die Suche indexieren. |
| **RETRIEVAL\_QUERY** | Einbettungen, die für allgemeine Suchanfragen optimiert sind. Verwenden Sie `RETRIEVAL_QUERY` für Abfragen und `RETRIEVAL_DOCUMENT` für abzurufende Dokumente. | Benutzerdefinierte Suche |
| **CODE\_RETRIEVAL\_QUERY** | Einbettungen, die für den Abruf von Codeblöcken auf Grundlage von Anfragen in natürlicher Sprache optimiert sind. Verwenden Sie `CODE_RETRIEVAL_QUERY` für Anfragen und `RETRIEVAL_DOCUMENT` für abzurufende Codeblöcke. | Codevorschläge und Suche |
| **QUESTION\_ANSWERING** | Einbettungen für Fragen in einem Frage-Antwort-System, die für das Auffinden von Dokumenten optimiert sind, die die Frage beantworten. Verwenden Sie `QUESTION_ANSWERING` für Fragen und `RETRIEVAL_DOCUMENT` für abzurufende Dokumente. | Chatbox |
| **FACT\_VERIFICATION** | Einbettungen für Aussagen, die überprüft werden müssen, optimiert für das Abrufen von Dokumenten, die Beweise für oder gegen die Aussage enthalten. Verwenden Sie `FACT_VERIFICATION` für den Zieltext und `RETRIEVAL_DOCUMENT` für abzurufende Dokumente. | Automatisierte Faktenchecksysteme |

## Größe von Einbettungen steuern

Sowohl `gemini-embedding-001` als auch `gemini-embedding-2` werden mit der MRL-Technik (Matryoshka Representation Learning) trainiert. Dabei wird ein Modell trainiert, um hochdimensionale Einbettungen zu lernen, deren Anfangssegmente (oder Präfixe) auch nützliche, einfachere Versionen derselben Daten sind.

Mit dem Parameter `output_dimensionality` können Sie die Größe des Ausgabebettungsvektors steuern. Durch die Auswahl einer kleineren Ausgabedimensionalität kann Speicherplatz gespart und die Recheneffizienz für Downstream-Anwendungen gesteigert werden, ohne dass die Qualität wesentlich beeinträchtigt wird. Standardmäßig geben beide Modelle ein 3.072-dimensionales Embedding aus. Sie können es jedoch auf eine kleinere Größe kürzen, ohne die Qualität zu beeinträchtigen, um Speicherplatz zu sparen. Wir empfehlen, die Ausgabedimensionen 768, 1536 oder 3072 zu verwenden.

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

### Ok

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

Beispielausgabe des Code-Snippets:

```
Length of embedding: 768
```

## Qualität bei kleineren Abmessungen sicherstellen

Während die Standardeinbettungen mit 3.072 Dimensionen immer normalisiert werden, normalisiert Gemini Embedding 2 auch automatisch gekürzte Dimensionen (z. B. 768, 1.536). So wird die semantische Ähnlichkeit über die Vektorrichtung und nicht über die Größe berechnet, was von vornherein genauere Ergebnisse liefert.

**Ältere Modelle**: Wenn Sie `gemini-embedding-001` verwenden, müssen Sie nicht 3072-Dimensionen manuell normalisieren:

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

Beispielausgabe dieses Code-Snippets:

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

In der folgenden Tabelle sind die MTEB-Werte aufgeführt, ein häufig verwendeter Benchmark für Einbettungen für verschiedene Dimensionen. Das Ergebnis zeigt, dass die Leistung nicht unbedingt an die Größe der Einbettungsdimension gebunden ist. Niedrigere Dimensionen erreichen Werte, die mit denen ihrer Pendants mit höherer Dimension vergleichbar sind.

| Dimension „MRL“ | MTEB-Punktzahl (Gemini Embedding 001) |
| --- | --- |
| 2048 | 68.16 |
| 1.536 | 68,17 |
| 768 | 67,99 |
| 512 | 67,55 |
| 256 | 66,19 |
| 128 | 63,31 |

## Multimodale Einbettungen

Das `gemini-embedding-2`-Modell unterstützt multimodale Eingaben, sodass Sie neben Text auch Bilder, Videos, Audio und Dokumente einbetten können. Alle Modalitäten werden in denselben Einbettungsbereich abgebildet, was die modalitätsübergreifende Suche und den modalitätsübergreifenden Vergleich ermöglicht.

### Unterstützte Modalitäten und Grenzwerte

Das maximale Limit für Eingabetokens beträgt insgesamt 8.192 Tokens.

| Modalität | Spezifikationen und Einschränkungen |
| --- | --- |
| **Text** | Unterstützt bis zu 8.192 Tokens. |
| **Bild** | Maximal 6 Bilder pro Anfrage. Unterstützte Formate: PNG, JPEG. |
| **Audio** | Maximale Dauer: 180 Sekunden. Unterstützte Formate: MP3, WAV. |
| **Video** | Maximale Dauer: 120 Sekunden Unterstützte Formate: MP4, MOV. Unterstützte Codecs: H264, H265, AV1, VP9.  Das System verarbeitet maximal 32 Frames pro Video. Bei kurzen Videos (≤ 32 Sekunden) wird eine Stichprobe mit 1 fps genommen, bei längeren Videos werden gleichmäßig 32 Frames ausgewählt. Audiotracks werden in Videodateien nicht verarbeitet. |
| **Dokumente (PDF)** | Max. 1 Datei pro Anfrage, bis zu 6 Seiten. |

### Bilder einbetten

Das folgende Beispiel zeigt, wie ein Bild mit `gemini-embedding-2` eingebettet wird.

Bilder können als Inline-Daten oder als hochgeladene Dateien über die [Files API](https://ai.google.dev/gemini-api/docs/files?hl=de) bereitgestellt werden.

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

### Aggregation von Einbettungen

Wenn Sie mit multimodalen Inhalten arbeiten, wirkt sich die Strukturierung Ihrer Eingabe auf die Einbettungsausgabe aus:

- **Mehrere Teile (aggregiert)**: Wenn Sie dem Parameter `contents` mehrere Eingaben hinzufügen, wird ein aggregiertes Embedding für alle Eingaben erstellt.
- **Mehrere `Content`-Objekte (separat)**: Wenn Sie jede Eingabe in ein `Content`-Objekt einfügen und diese im Parameter `contents` übergeben, werden separate Einbettungen für jeden Eintrag zurückgegeben.
- **Darstellung auf Beitragsebene**:Bei komplexen Objekten wie Social-Media-Beiträgen mit mehreren Media-Elementen empfehlen wir, separate Einbettungen zu aggregieren (z. B. durch Mittelwertbildung), um eine kohärente Darstellung auf Beitragsebene zu erstellen.

Im folgenden Beispiel wird gezeigt, wie eine aggregierte Einbettung für Text- und Bildeingaben erstellt wird. Fügen Sie dem Parameter `contents` einfach mehrere Eingaben hinzu:

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

Wenn Sie hingegen `Content`-Objekte im Parameter `contents` verwenden, werden separate Einbettungen zurückgegeben. In diesem Beispiel werden mehrere Einbettungen in einem Einbettungsaufruf erstellt:

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

### Audio einbetten

Das folgende Beispiel zeigt, wie Sie eine Audiodatei mit `gemini-embedding-2` einbetten.

Audiodateien können als Inline-Daten oder als hochgeladene Dateien über die [Files API](https://ai.google.dev/gemini-api/docs/files?hl=de) bereitgestellt werden.

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

### Videos einbetten

Das folgende Beispiel zeigt, wie ein Video mit `gemini-embedding-2` eingebettet wird.

Videos können als Inlinedaten oder als hochgeladene Dateien über die [Files API](https://ai.google.dev/gemini-api/docs/files?hl=de) bereitgestellt werden.

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

Wenn Sie Videos mit einer Länge von mehr als 120 Sekunden einbetten möchten, können Sie das Video in sich überschneidende Segmente aufteilen und diese Segmente einzeln einbetten.

### Dokumente einbetten

Dokumente im PDF-Format können direkt eingebettet werden. Das Modell verarbeitet die visuellen und textlichen Inhalte jeder Seite.

PDFs können als Inline-Daten oder als hochgeladene Dateien über die [Files API](https://ai.google.dev/gemini-api/docs/files?hl=de) bereitgestellt werden.

#### So verarbeitet das Modell PDFs

Wenn Sie ein PDF einbetten, verarbeitet das Modell das Dokument sowohl mit visuellen als auch mit Textfunktionen:

- **Visuelle Darstellung**:Das Modell rendert jede Seite als Bild, was **258 Tokens** pro Seite verbraucht.
- **Textextraktion**:Das Modell extrahiert Text aus dem Dokument. Bei **nativen PDFs** (die digitalen Text enthalten) wird der Text direkt vom Modell extrahiert. Bei **gescannten PDFs**, die Bilder von Text enthalten, führt das Modell automatisch eine optische Zeichenerkennung (OCR) durch, um den Text zu extrahieren.

Um die Gesamtzahl der Tokens für ein PDF zu berechnen, addieren Sie die visuellen Tokens (258 pro Seite) zu den Text-Tokens. Ihre Eingaben dürfen das **Token-Limit von 8.192** des Modells nicht überschreiten (gilt für alle Modalitäten). Eingaben, die dieses Limit überschreiten, werden vom System automatisch abgeschnitten.

#### PDF-Limits

- **Dateien pro Anfrage**:Sie können maximal eine PDF-Datei einreichen.
- **Seitenlimit**:Sie können maximal 6 Seiten pro Datei einreichen. Für eine optimale Qualität empfehlen wir dringend, nur eine Seite pro PDF zu verwenden.

Das folgende Beispiel zeigt, wie Sie ein PDF mit `gemini-embedding-2` einbetten:

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

## Anwendungsfälle

Texteinbettungen sind für eine Vielzahl gängiger KI-Anwendungsfälle unerlässlich, z. B.:

- **Retrieval-Augmented Generation (RAG):** Mit Embeddings lässt sich die Qualität von generiertem Text verbessern, indem relevante Informationen abgerufen und in den Kontext eines Modells eingebunden werden.
- **Information Retrieval**:Suchen Sie anhand eines Eingabetexts nach dem semantisch ähnlichsten Text oder den semantisch ähnlichsten Dokumenten.

  [Anleitung zur Dokumentsuchetask](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **Neubewertung der Suche**: Die relevantesten Elemente werden priorisiert, indem die ersten Ergebnisse semantisch anhand der Anfrage bewertet werden.

  [Tutorial zum Neuklassifizieren von Suchergebnissentask](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **Anomalieerkennung**:Durch den Vergleich von Gruppen von Einbettungen lassen sich verborgene Trends oder Ausreißer erkennen.

  [Anleitung zur Anomalieerkennungbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **Klassifizierung**:Text basierend auf seinem Inhalt automatisch kategorisieren, z. B. für die Sentimentanalyse oder die Spamerkennung

  [Anleitung zur Klassifizierungtoken](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **Clustering**:Erfassen Sie komplexe Beziehungen effektiv, indem Sie Cluster und Visualisierungen Ihrer Einbettungen erstellen.

  [Anleitung zur Visualisierung von Clusternbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## Einbettungen speichern

Wenn Sie Einbettungen in der Produktion verwenden, ist es üblich, **Vektordatenbanken** zu verwenden, um hochdimensionale Einbettungen effizient zu speichern, zu indexieren und abzurufen. Google Cloud bietet verwaltete Datendienste, die für diesen Zweck verwendet werden können, darunter [Gemini Enterprise Agent Platform Vector Search 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/BUILD/vector-search-2?hl=de), [BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=de), [AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=de) und [Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=de).

In den folgenden Anleitungen wird gezeigt, wie Sie andere Vektordatenbanken von Drittanbietern mit Gemini Embedding verwenden.

- [ChromaDB-Tutorialsbolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [QDrant-Tutorialsbolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [Weaviate-Tutorialsbolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [Pinecone-Anleitungenbolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## Modellversionen

### Gemini Embedding 2

| Attribut | Beschreibung |
| --- | --- |
| id\_cardModellcode | **Gemini API**  `gemini-embedding-2` |
| saveUnterstützte Datentypen | **Eingabe**  Text, Bild, Video, Audio, PDF  **Ausgabe**  Texteinbettungen |
| token\_autoToken-Limits[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=de) | **Eingabetokenlimit**  8.192  **Größe der Ausgabedimension**  Flexibel, unterstützt: 128–3072, empfohlen: 768, 1536, 3072 |
| 123-Versionen | Weitere Informationen finden Sie unter [Muster für Modellversionen](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#model-versions).  - Stabil: `gemini-embedding-2` |
| calendar\_monthLetzte Aktualisierung | April 2026 |

### Gemini Embedding

| Attribut | Beschreibung |
| --- | --- |
| id\_cardModellcode | **Gemini API**  `gemini-embedding-001` |
| saveUnterstützte Datentypen | **Eingabe**  Text  **Ausgabe**  Texteinbettungen |
| token\_autoToken-Limits[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=de) | **Eingabetokenlimit**  2.048  **Größe der Ausgabedimension**  Flexibel, unterstützt: 128–3072, empfohlen: 768, 1536, 3072 |
| 123-Versionen | Weitere Informationen finden Sie unter [Muster für Modellversionen](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#model-versions).  - Stabil: `gemini-embedding-001` |
| calendar\_monthLetzte Aktualisierung | Juni 2025 |

Informationen zu eingestellten Embeddings-Modellen finden Sie auf der Seite [Einstellungen](https://ai.google.dev/gemini-api/docs/deprecations?hl=de).

## Migration von gemini-embedding-001

Die Einbettungsräume zwischen `gemini-embedding-001` und `gemini-embedding-2` sind **nicht kompatibel**. Das bedeutet, dass Sie die von einem Modell generierten Einbettungen nicht direkt mit den von einem anderen Modell generierten Einbettungen vergleichen können. Wenn Sie auf `gemini-embedding-2` upgraden, müssen Sie alle vorhandenen Daten neu einbetten.

Neben der Inkompatibilität gibt es noch einige andere nennenswerte Unterschiede zwischen den beiden Modellen:

- **Spezifikation des Aufgabentyps**:Mit `gemini-embedding-001` geben Sie den Aufgabentyp mit dem Parameter `task_type` an (z.B. `SEMANTIC_SIMILARITY`, `RETRIEVAL_DOCUMENT`). Mit `gemini-embedding-2` wird der Parameter `task_type` nicht unterstützt. Stattdessen sollten Sie die Aufgabenanweisungen direkt in den Prompt für reine Textaufgaben einfügen. Unter [Aufgabentypen mit Embeddings 2](#task-types-embeddings-2) finden Sie Informationen zum Formatieren von Prompts für verschiedene Anwendungsfälle.
- **Aggregation von Einbettungen**:`gemini-embedding-001` generiert einzelne Einbettungen für jeden String in einer Liste von Eingaben. Im Gegensatz dazu wird bei `gemini-embedding-2` eine einzelne, aggregierte Einbettung erstellt, wenn mehrere Eingaben (z. B. Text und Bilder) direkt in einer Anfrage angegeben werden. Wenn Sie separate Einbettungen für einzelne Eingaben generieren möchten, schließen Sie jede Eingabe in ein `Content`-Objekt ein oder verwenden Sie die [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de#batch-embedding). Weitere Informationen finden Sie unter [Aggregation von Einbettungen](#embedding-aggregation).
- **Normalisierung**:Wenn Sie `output_dimensionality` verwenden, um Einbettungen mit weniger als 3.072 Dimensionen anzufordern, normalisiert `gemini-embedding-2` diese gekürzten Einbettungen automatisch. Bei `gemini-embedding-001` müssen Sie die Normalisierung für andere Dimensionen als 3.072 manuell vornehmen. Weitere Informationen finden Sie unter [Qualität bei kleineren Dimensionen sicherstellen](#quality-for-smaller-dimensions).

## Batch-Einbettungen

Wenn die Latenz kein Problem darstellt, können Sie die Gemini Embeddings-Modelle mit der [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de#batch-embedding) verwenden. Dadurch ist ein viel höherer Durchsatz zum halben Standardpreis für Einbettungen möglich.
Beispiele für die ersten Schritte finden Sie im [Batch API Cookbook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb).

## Hinweis zur verantwortungsvollen Nutzung

Im Gegensatz zu generativen KI-Modellen, die neue Inhalte erstellen, ist das Gemini Embedding-Modell nur dazu gedacht, das Format Ihrer Eingabedaten in eine numerische Darstellung zu transformieren. Google ist zwar für die Bereitstellung eines Einbettungsmodells verantwortlich, das das Format Ihrer Eingabedaten in das erforderliche numerische Format umwandelt, die Nutzer sind jedoch weiterhin für die von ihnen eingegebenen Daten und die resultierenden Einbettungen verantwortlich. Durch die Nutzung des Gemini Embedding-Modells bestätigen Sie, dass Sie über die erforderlichen Rechte für die von Ihnen hochgeladenen Inhalte verfügen. Erstellen Sie keine Inhalte, durch die die Rechte anderer, zum Beispiel Rechte an geistigem Eigentum oder das Recht auf Privatsphäre, verletzt werden. Die Nutzung dieses Dienstes unterliegt unserer [Richtlinie zur unzulässigen Nutzung](https://policies.google.com/terms/generative-ai/use-policy?hl=de) und den [Google-Nutzungsbedingungen](https://ai.google.dev/gemini-api/terms?hl=de).

## Mit Einbettungen entwickeln

Im [Notebook zur Kurzanleitung für Einbettungen](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb) können Sie die Modellfunktionen kennenlernen und erfahren, wie Sie Ihre Einbettungen anpassen und visualisieren.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-22 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-22 (UTC)."],[],[]]
