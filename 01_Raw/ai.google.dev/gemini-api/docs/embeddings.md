---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=pl
fetched_at: 2026-07-06T05:12:55.030948+00:00
title: "Wektory dystrybucyjne \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Wektory dystrybucyjne

Interfejs Gemini API udostępnia modele wektorów dystrybucyjnych do generowania wektorów dystrybucyjnych tekstu, obrazów, filmów i innych treści. Powstałe w ten sposób wektory dystrybucyjne można następnie wykorzystać w zadaniach takich jak wyszukiwanie semantyczne, klasyfikacja i klastrowanie, co pozwala uzyskać dokładniejsze wyniki uwzględniające kontekst niż w przypadku podejść opartych na słowach kluczowych.

Najnowszy model, `gemini-embedding-2`, to pierwszy multimodalny model osadzania w interfejsie Gemini API. Mapuje tekst, obrazy, filmy, dźwięk i dokumenty w ujednoliconej przestrzeni osadzania, umożliwiając wyszukiwanie, klasyfikowanie i grupowanie w różnych trybach w ponad 100 językach. Więcej informacji znajdziesz w [sekcji poświęconej osadzaniu multimodalnemu](#multimodal). W przypadku zastosowań obejmujących tylko tekst `gemini-embedding-001` pozostaje dostępny.

Tworzenie systemów generowania rozszerzonego przez wyszukiwanie w zapisanych informacjach (RAG) jest typowym zastosowaniem usług AI. Osadzanie odgrywa kluczową rolę w znacznym ulepszaniu wyników modelu dzięki większej dokładności faktów, spójności i bogactwu kontekstowemu. Jeśli wolisz korzystać z zarządzanego rozwiązania RAG, stworzyliśmy narzędzie [File Search](https://ai.google.dev/gemini-api/docs/file-search?hl=pl), które ułatwia zarządzanie RAG i zmniejsza koszty.

## Generowanie wektorów dystrybucyjnych

Aby wygenerować osadzenia tekstu, użyj metody `embedContent`:

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

## Określ typ zadania, które ma poprawić skuteczność

Możesz używać wektorów do wielu różnych zadań, od klasyfikacji po wyszukiwanie dokumentów. Określenie właściwego typu zadania pomaga zoptymalizować osadzanie pod kątem zamierzonych relacji, co zwiększa dokładność i wydajność.

### Typy zadań z wektorami dystrybucyjnymi 2

W przypadku zadań tekstowych z `gemini-embedding-2` zdecydowanie zalecamy dodanie instrukcji do promptu. Możesz to zrobić, formatując zapytanie i dokument za pomocą odpowiedniego prefiksu zadania.

W tabelach poniżej znajdziesz przykłady formatowania zapytań i dokumentów w przypadku zastosowań symetrycznych i asymetrycznych z użyciem modelu `gemini-embedding-2`.

**Przypadki użycia wyszukiwania (format asymetryczny)**

W przypadku asymetrycznych przypadków użycia dodaj do zapytania prefiks zadania i zastosuj strukturę dokumentu do treści, które chcesz osadzić i pobrać.

| Przypadek użycia | Struktura zapytania | Struktura dokumentu |
| --- | --- | --- |
| Zapytanie | `task: search result | query: {content}` | `title: {title} | text: {content}` Jeśli nie ma tytułu, użyj `title: none`. |
| Odpowiadanie na pytania | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| Weryfikowanie informacji | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| Odzyskiwanie kodu | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**Przykładowe użycie**

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

**Przypadki użycia z 1 wejściem (format symetryczny)**

W przypadku symetrycznych przypadków użycia wykonuj to samo zadanie, stosując to samo formatowanie zapytania i dokumentu.

| Przypadek użycia | Struktura danych wejściowych |
| --- | --- |
| Klasyfikacja | `task: classification | query: {content}` |
| Grupowanie | `task: clustering | query: {content}` |
| Podobieństwo semantyczne | `task: sentence similarity | query: {content}` Nie używaj tej funkcji do wyszukiwania ani pobierania. Jest on przeznaczony do określania podobieństwa semantycznego tekstu. |

**Przykładowe użycie**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

Ważne jest, aby zadanie było używane konsekwentnie. Jeśli np. dokumenty są osadzone za pomocą funkcji `f'task: classification | query: {content}'`, zapytanie również powinno być osadzone zgodnie z formatem tego zadania.

### Typy zadań z osadzaniem 1

W przypadku `gemini-embedding-001` możesz określić `task_type` w metodzie `embedContent`. Pełną listę obsługiwanych typów zadań znajdziesz w tabeli [Obsługiwane typy zadań](#supported-task-types).

Przykład poniżej pokazuje, jak za pomocą funkcji `SEMANTIC_SIMILARITY` sprawdzić, jak podobne są do siebie ciągi tekstów.

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

Fragmenty kodu pokażą, jak podobne są do siebie różne fragmenty tekstu po uruchomieniu.

#### Obsługiwane typy zadań

Obsługiwane typy zadań w przypadku `gemini-embedding-001`:

| Typ zadania | Opis | Przykłady |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | Osadzanie zoptymalizowane pod kątem oceny podobieństwa tekstu. | Systemy rekomendacji, wykrywanie duplikatów |
| **KLASYFIKACJA** | Osadzanie zoptymalizowane pod kątem klasyfikowania tekstów według wstępnie ustawionych etykiet. | Analiza nastawienia, wykrywanie spamu |
| **KLASYFIKACJA** | Osadzanie zoptymalizowane pod kątem grupowania tekstów na podstawie ich podobieństwa. | Porządkowanie dokumentów, badania rynku, wykrywanie anomalii |
| **RETRIEVAL\_DOCUMENT** | Osadzanie zoptymalizowane pod kątem wyszukiwania dokumentów. | indeksowanie artykułów, książek lub stron internetowych na potrzeby wyszukiwania; |
| **RETRIEVAL\_QUERY** | Osadzanie zoptymalizowane pod kątem ogólnych zapytań. Używaj symbolu `RETRIEVAL_QUERY` w przypadku zapytań, a symbolu `RETRIEVAL_DOCUMENT` w przypadku dokumentów do pobrania. | Twoja wyszukiwarka |
| **CODE\_RETRIEVAL\_QUERY** | Osadzanie zoptymalizowane pod kątem wyszukiwania bloków kodu na podstawie zapytań w języku naturalnym. Używaj znaku `CODE_RETRIEVAL_QUERY` w przypadku zapytań, a znaku `RETRIEVAL_DOCUMENT` w przypadku bloków kodu, które mają zostać pobrane. | Sugestie dotyczące kodu i wyszukiwanie |
| **QUESTION\_ANSWERING** | Osadzanie pytań w systemie odpowiadania na pytania, zoptymalizowane pod kątem znajdowania dokumentów, które zawierają odpowiedź na pytanie. Używaj symbolu `QUESTION_ANSWERING` w przypadku pytań, a symbolu `RETRIEVAL_DOCUMENT` w przypadku dokumentów do pobrania. | Chatbox |
| **FACT\_VERIFICATION** | Osadzenia dla stwierdzeń, które wymagają weryfikacji, zoptymalizowane pod kątem wyszukiwania dokumentów zawierających dowody potwierdzające lub obalające to stwierdzenie. Użyj `FACT_VERIFICATION` w przypadku tekstu docelowego, a `RETRIEVAL_DOCUMENT` w przypadku dokumentów do pobrania. | Automatyczne systemy weryfikacji informacji |

## Określanie rozmiaru wektora dystrybucyjnego

Zarówno `gemini-embedding-001`, jak i `gemini-embedding-2` są trenowane przy użyciu techniki uczenia reprezentacji Matrioszka (MRL), która uczy model tworzenia osadzeń o wysokiej liczbie wymiarów, których początkowe segmenty (lub prefiksy) są również przydatnymi, prostszymi wersjami tych samych danych.

Użyj parametru `output_dimensionality`, aby kontrolować rozmiar wyjściowego wektora dystrybucyjnego. Wybór mniejszej liczby wymiarów wyjściowych może zaoszczędzić miejsce na dane i zwiększyć wydajność obliczeniową w przypadku aplikacji podrzędnych, przy niewielkiej utracie jakości. Domyślnie oba modele generują 3072-wymiarowe osadzanie, ale możesz je skrócić do mniejszego rozmiaru bez utraty jakości, aby zaoszczędzić miejsce na dane. Zalecamy używanie wymiarów wyjściowych 768, 1536 lub 3072.

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

Przykładowe dane wyjściowe z fragmentu kodu:

```
Length of embedding: 768
```

## Zapewnianie jakości w przypadku mniejszych wymiarów

Domyślne 3072-wymiarowe osadzanie jest zawsze normalizowane, ale Gemini Embedding 2 automatycznie normalizuje też obcięte wymiary (np. 768, 1536). Dzięki temu podobieństwo semantyczne jest obliczane na podstawie kierunku wektora, a nie jego wielkości, co zapewnia większą dokładność wyników od razu po wyjęciu z pudełka.

**Starsze modele:** jeśli używasz modelu `gemini-embedding-001`, musisz ręcznie znormalizować wymiary inne niż 3072 w ten sposób:

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

Przykładowe dane wyjściowe tego fragmentu kodu:

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

W tabeli poniżej znajdziesz wyniki MTEB, czyli powszechnie stosowanego testu porównawczego dla osadzania, w przypadku różnych wymiarów. Wyniki pokazują, że skuteczność nie jest ściśle związana z rozmiarem wymiaru osadzania, ponieważ mniejsze wymiary osiągają wyniki porównywalne z większymi.

| Wymiar MRL | Wynik MTEB (Gemini Embedding 001) |
| --- | --- |
| 2048 | 68,16 |
| 1536 | 68,17 |
| 768 | 67,99 |
| 512 | 67,55 |
| 256 | 66,19 |
| 128 | 63,31 |

## Multimodalne wektory dystrybucyjne

Model `gemini-embedding-2` obsługuje dane wejściowe multimodalne, co umożliwia osadzanie treści w formie obrazów, filmów, dźwięku i dokumentów obok tekstu. Wszystkie rodzaje danych są mapowane na tę samą przestrzeń osadzania, co umożliwia wyszukiwanie i porównywanie różnych rodzajów danych.

### Obsługiwane rodzaje i limity

Ogólny maksymalny limit tokenów wejściowych to 8192 tokeny.

| Modalność | Specyfikacje i limity |
| --- | --- |
| **Text** | Obsługuje do 8192 tokenów. |
| **Obraz** | Maksymalnie 6 obrazów na żądanie. Obsługiwane formaty: PNG, JPEG. |
| **Dźwięk** | Maksymalny czas trwania to 180 sekund. Obsługiwane formaty: MP3, WAV. |
| **Film** | Maksymalny czas trwania to 120 sekund. Obsługiwane formaty: MP4, MOV. Obsługiwane kodeki: H264, H265, AV1, VP9.  System przetwarza maksymalnie 32 klatki na film: w przypadku krótkich filmów (≤32 s) próbkowanie odbywa się z częstotliwością 1 klatki na sekundę, a w przypadku dłuższych filmów próbkowanie jest jednolite i obejmuje 32 klatki. Ścieżki audio nie są przetwarzane w plikach wideo. |
| **Dokumenty (PDF)** | Maksymalnie 1 plik na żądanie, do 6 stron. |

### Umieszczanie obrazów

Poniższy przykład pokazuje, jak umieścić obraz za pomocą tagu
`gemini-embedding-2`.

Obrazy można przesyłać jako dane wbudowane lub jako przesłane pliki za pomocą [interfejsu Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl).

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

### Agregacja wektorów dystrybucyjnych

Podczas pracy z treściami multimodalnymi struktura danych wejściowych wpływa na wygenerowane wektory dystrybucyjne:

- **Wiele części (zagregowanych):** dodanie wielu danych wejściowych bezpośrednio do parametru
  `contents` powoduje utworzenie jednego zagregowanego osadzenia dla wszystkich danych wejściowych.
- **Wiele obiektów `Content` (osobnych):** umieszczenie każdego wejścia w obiekcie `Content` i przekazanie ich w parametrze `contents` zwraca osobne wektory osadzeń dla każdego wpisu.
- **Reprezentacja na poziomie posta:** w przypadku złożonych obiektów, takich jak posty w mediach społecznościowych zawierające wiele elementów multimedialnych, zalecamy agregowanie oddzielnych osadzeń (np. przez uśrednianie), aby utworzyć spójną reprezentację na poziomie posta.

W przykładzie poniżej pokazujemy, jak utworzyć 1 zagregowane osadzenie dla tekstu i obrazu. Wystarczy dodać wiele danych wejściowych do parametru `contents`:

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

Z drugiej strony, jeśli użyjesz obiektów `Content` w parametrze `contents`, zwróci on oddzielne wektory. W tym przykładzie tworzymy wiele wektorów dystrybucyjnych w jednym wywołaniu:

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

### Osadzanie dźwięku

Poniższy przykład pokazuje, jak umieścić plik audio za pomocą tagu`gemini-embedding-2`.

Pliki audio można przesyłać jako dane wbudowane lub jako przesłane pliki za pomocą [interfejsu Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl).

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

### Umieszczanie filmu

Poniższy przykład pokazuje, jak umieścić film za pomocą tagu `gemini-embedding-2`.

Filmy można przesyłać jako dane wbudowane lub jako przesłane pliki za pomocą [interfejsu Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl).

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

Jeśli chcesz osadzić filmy dłuższe niż 120 sekund, możesz podzielić je na nakładające się na siebie segmenty i osadzić je osobno.

### Umieszczanie dokumentów

Dokumenty w formacie PDF można umieszczać bezpośrednio. Model przetwarza treści wizualne i tekstowe na każdej stronie.

Pliki PDF można przesyłać jako dane wbudowane lub jako przesłane pliki za pomocą [interfejsu Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl).

#### Jak model przetwarza pliki PDF

Gdy osadzasz plik PDF, model przetwarza dokument za pomocą funkcji wizualnych i tekstowych:

- **Reprezentacja wizualna:** model renderuje każdą stronę jako obraz, co zużywa **258 tokenów** na stronę.
- **Wyodrębnianie tekstu:** model wyodrębnia tekst z dokumentu. W przypadku **natywnych plików PDF** (zawierających tekst cyfrowy) model wyodrębnia tekst bezpośrednio. W przypadku **zeskanowanych plików PDF** (zawierających obrazy tekstu) model automatycznie uruchamia optyczne rozpoznawanie znaków (OCR), aby wyodrębnić tekst.

Aby obliczyć łączną liczbę tokenów w pliku PDF, dodaj tokeny wizualne (258 na stronę) do tokenów tekstowych. Dane wejściowe muszą mieścić się w **limicie 8192 tokenów** (wspólnym dla wszystkich rodzajów danych). System automatycznie obcina dane wejściowe, które przekraczają ten limit.

#### Limity plików PDF

- **Pliki w żądaniu:** możesz przesłać maksymalnie 1 plik PDF.
- **Limit stron:** w każdym pliku możesz przesłać maksymalnie 6 stron. Aby uzyskać najlepszą jakość, zdecydowanie zalecamy używanie 1 strony na plik PDF.

Poniższy przykład pokazuje, jak umieścić plik PDF za pomocą `gemini-embedding-2`:

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

## Przypadki użycia

Osadzanie tekstu ma kluczowe znaczenie w przypadku wielu typowych zastosowań AI, takich jak:

- **Generowanie wspomagane wyszukiwaniem (RAG):** osadzanie poprawia jakość wygenerowanego tekstu, ponieważ pobiera i uwzględnia w kontekście modelu odpowiednie informacje.
- **Wyszukiwanie informacji:** wyszukiwanie najbardziej podobnego semantycznie tekstu lub dokumentów na podstawie fragmentu tekstu wejściowego.

  [Samouczek dotyczący wyszukiwania dokumentówtask](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **Ponowne rankingowanie wyników wyszukiwania:** nadawanie priorytetu najtrafniejszym elementom przez semantyczne ocenianie wstępnych wyników w odniesieniu do zapytania.

  [Samouczek dotyczący ponownego rankingu wyszukiwaniatask](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **Wykrywanie anomalii:** porównywanie grup osadzeń może pomóc w identyfikowaniu ukrytych trendów lub wartości odstających.

  [Samouczek dotyczący wykrywania anomaliibubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **Klasyfikacja:** automatyczne kategoryzowanie tekstu na podstawie jego treści, np. analiza nastawienia lub wykrywanie spamu.

  [Samouczek dotyczący klasyfikacjitoken](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **Grupowanie:** skutecznie analizuj złożone relacje, tworząc klastry i wizualizacje osadzeń.

  [Samouczek dotyczący wizualizacji klastrowaniabubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## Przechowywanie wektorów dystrybucyjnych

W przypadku wdrażania wektorów dystrybucyjnych w środowisku produkcyjnym często używa się **baz danych wektorowych** do wydajnego przechowywania, indeksowania i pobierania wektorów dystrybucyjnych o wysokiej liczbie wymiarów. Google Cloud oferuje zarządzane usługi danych, które można wykorzystać w tym celu, w tym [Gemini Enterprise Agent Platform Vector Search 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/BUILD/vector-search-2?hl=pl), [BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=pl), [AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=pl) i [Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=pl).

Z tych samouczków dowiesz się, jak używać innych baz danych wektorów innych firm z osadzaniem Gemini.

- [Samouczki dotyczące ChromaDBbolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [Samouczki QDrantbolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [Samouczki Weaviatebolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [Samouczki Pineconebolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## Wersje modelu

### Gemini Embedding 2

| Właściwość | Opis |
| --- | --- |
| id\_cardKod modelu | **Gemini API**  `gemini-embedding-2` |
| saveObsługiwane typy danych | **Wejście**  Tekst, obraz, film, dźwięk, PDF  **Dane wyjściowe**  Wektory dystrybucyjne tekstu |
| token\_autoLimity tokenów[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pl) | **Limit tokenów wejściowych**  8192  **Rozmiar wymiaru wyjściowego**  Elastyczny, obsługuje: 128–3072, zalecane: 768, 1536, 3072 |
| 123 wersje | Więcej informacji znajdziesz w [wzorcach wersji modelu](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl#model-versions).  - Stabilny: `gemini-embedding-2` |
| calendar\_monthOstatnia aktualizacja | Kwiecień 2026 r. |

### Osadzanie Gemini

| Właściwość | Opis |
| --- | --- |
| id\_cardKod modelu | **Gemini API**  `gemini-embedding-001` |
| saveObsługiwane typy danych | **Wejście**  Tekst  **Dane wyjściowe**  Wektory dystrybucyjne tekstu |
| token\_autoLimity tokenów[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pl) | **Limit tokenów wejściowych**  2048  **Rozmiar wymiaru wyjściowego**  Elastyczny, obsługuje: 128–3072, zalecane: 768, 1536, 3072 |
| 123 wersje | Więcej informacji znajdziesz w [wzorcach wersji modelu](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl#model-versions).  - Stabilny: `gemini-embedding-001` |
| calendar\_monthOstatnia aktualizacja | Czerwiec 2025 r. |

W przypadku wycofanych modeli Embeddings odwiedź stronę [Wycofane modele](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl).

## Migracja z modelu gemini-embedding-001

Przestrzenie osadzania między `gemini-embedding-001` a `gemini-embedding-2` są **niezgodne**. Oznacza to, że nie możesz bezpośrednio porównywać wektorów wygenerowanych przez jeden model z wektorami wygenerowanymi przez drugi. Jeśli przechodzisz na `gemini-embedding-2`, musisz ponownie osadzić wszystkie dotychczasowe dane.

Oprócz niezgodności istnieje kilka innych istotnych różnic między tymi modelami:

- **Specyfikacja typu zadania:** w przypadku `gemini-embedding-001` typ zadania określasz za pomocą parametru `task_type` (np. `SEMANTIC_SIMILARITY`, `RETRIEVAL_DOCUMENT`). W przypadku `gemini-embedding-2` parametr `task_type` nie jest obsługiwany. Zamiast tego w przypadku zadań tekstowych należy umieścić instrukcje bezpośrednio w prompcie. Więcej informacji o tym, jak formatować prompty w różnych przypadkach użycia, znajdziesz w sekcji [Typy zadań z Embeddings 2](#task-types-embeddings-2).
- **Agregacja wektorów dystrybucyjnych:** `gemini-embedding-001` generuje poszczególne wektory dystrybucyjne dla każdego ciągu znaków na liście danych wejściowych. Z kolei `gemini-embedding-2` generuje pojedynczy, zagregowany wektor, gdy w jednym żądaniu podawanych jest wiele danych wejściowych (np. tekst i obrazy). Aby wygenerować osobne wektory osadzania dla poszczególnych danych wejściowych, umieść każdy z nich w obiekcie `Content` lub użyj [interfejsu Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl#batch-embedding). Więcej informacji znajdziesz w sekcji [Osadzanie agregacji](#embedding-aggregation).
- **Normalizacja:** jeśli używasz `output_dimensionality` do żądania osadzeń o liczbie wymiarów mniejszej niż 3072, `gemini-embedding-2` automatycznie normalizuje te obcięte osadzenia. W przypadku `gemini-embedding-001` musisz przeprowadzić ręczną normalizację w przypadku wymiarów innych niż 3072. Więcej informacji znajdziesz w artykule [Zapewnianie jakości w przypadku mniejszych wymiarów](#quality-for-smaller-dimensions).

## Wektory dystrybucyjne w pakietach

Jeśli opóźnienie nie jest problemem, spróbuj użyć modeli Gemini Embeddings z [interfejsem Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl#batch-embedding). Umożliwia to znacznie większą przepustowość przy 50% domyślnej ceny za osadzanie.
Przykłady, jak zacząć, znajdziesz w [przewodniku po interfejsie Batch API](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb).

## Powiadomienie o odpowiedzialnym korzystaniu

W przeciwieństwie do modeli generatywnej AI, które tworzą nowe treści, model Gemini Embedding ma tylko przekształcać format danych wejściowych w reprezentację numeryczną. Google odpowiada za udostępnienie modelu osadzania, który przekształca format danych wejściowych na wymagany format numeryczny, ale użytkownicy ponoszą pełną odpowiedzialność za wprowadzane dane i powstałe osadzanie. Korzystając z modelu Gemini Embedding, potwierdzasz, że masz wymagane prawa do treści, które przesyłasz. Nie twórz treści naruszających prawa własności intelektualnej lub prawo do prywatności innych osób. Korzystanie z tej usługi podlega naszym [zasadom dotyczącym niedozwolonych zastosowań](https://policies.google.com/terms/generative-ai/use-policy?hl=pl) i [Warunkom korzystania z usług Google](https://ai.google.dev/gemini-api/terms?hl=pl).

## Zacznij tworzyć z użyciem wektorów

Zapoznaj się z [notebookiem z krótkim wprowadzeniem do wektorów](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb), aby poznać możliwości modelu i dowiedzieć się, jak dostosowywać i wizualizować wektory.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-22 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-22 UTC."],[],[]]
