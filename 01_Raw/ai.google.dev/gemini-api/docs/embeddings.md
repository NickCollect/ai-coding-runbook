---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=id
fetched_at: 2026-10-12T07:08:20.144767+00:00
title: "Embedding \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Embedding

Gemini API menawarkan model embedding untuk menghasilkan embedding untuk teks, gambar, video, dan konten lainnya. Embedding yang dihasilkan ini kemudian dapat digunakan untuk tugas seperti penelusuran semantik, klasifikasi, dan pengelompokan, sehingga memberikan hasil yang lebih akurat dan sesuai konteks daripada pendekatan berbasis kata kunci.

Model terbaru, `gemini-embedding-2`, adalah model penyematan multimodal pertama di Gemini API. Model ini memetakan teks, gambar, video, audio, dan dokumen ke dalam ruang embedding terpadu, sehingga memungkinkan penelusuran, klasifikasi, dan pengelompokan lintas modal dalam lebih dari 100 bahasa. Lihat
[bagian embedding multimodal](#multimodal) untuk mempelajari lebih lanjut. Untuk kasus penggunaan hanya teks, `gemini-embedding-001` tetap tersedia.

Membangun sistem Retrieval Augmented Generation (RAG) adalah kasus penggunaan umum untuk produk AI. Penyematan memainkan peran penting dalam meningkatkan output model secara signifikan dengan akurasi faktual, koherensi, dan kekayaan kontekstual yang lebih baik. Jika Anda lebih memilih menggunakan solusi RAG terkelola, kami membuat alat [Penelusuran File](https://ai.google.dev/gemini-api/docs/file-search?hl=id) yang mempermudah pengelolaan RAG dan lebih hemat biaya.

## Membuat embedding

Gunakan metode `embedContent` untuk membuat embedding teks:

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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.EmbedContentResponse;

Client client = new Client();

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", "What is the meaning of life?", null);

System.out.println(response.embeddings().orElse(null));
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

## Menentukan jenis tugas untuk meningkatkan performa

Anda dapat menggunakan embedding untuk berbagai tugas, mulai dari klasifikasi hingga penelusuran dokumen. Menentukan jenis tugas yang tepat akan membantu mengoptimalkan penyematan untuk hubungan yang diinginkan, sehingga memaksimalkan akurasi dan efisiensi.

### Jenis tugas dengan Embeddings 2

Untuk tugas hanya teks dengan `gemini-embedding-2`, sebaiknya Anda
menambahkan petunjuk tugas dalam perintah Anda. Hal ini dapat dilakukan dengan memformat kueri dan dokumen dengan awalan tugas yang benar.

Saat membuat [satu embedding berdasarkan input multimodal](#embedding-aggregation), umumnya kami tidak merekomendasikan pemberian awalan pada bagian teks input dengan petunjuk tugas. Dalam beberapa kasus, hal ini meningkatkan
performa, tetapi dalam kasus lain, hal ini mengurangi performa.

Tabel berikut menunjukkan contoh cara memformat kueri dan dokumen untuk
kasus penggunaan simetris dan asimetris menggunakan model `gemini-embedding-2`.

**Kasus penggunaan pengambilan (Format asimetris)**

Dalam kasus penggunaan asimetris, tambahkan awalan tugas ke kueri dan terapkan struktur dokumen untuk konten yang ingin Anda sematkan dan ambil.

| Kasus penggunaan | Struktur kueri | Struktur dokumen |
| --- | --- | --- |
| Kueri penelusuran | `task: search result | query: {content}` | `title: {title} | text: {content}` Jika tidak ada judul, gunakan `title: none`. |
| Question answering | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| Pengecekan fakta | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| Pengambilan kode | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**Contoh penggunaan**

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

**Kasus penggunaan input tunggal (Format simetris)**

Dalam kasus penggunaan simetris, untuk tugas yang sama, gunakan format yang sama untuk kueri dan dokumen.

| Kasus penggunaan | Struktur input |
| --- | --- |
| Klasifikasi | `task: classification | query: {content}` |
| Pengelompokan | `task: clustering | query: {content}` |
| Kemiripan semantik | `task: sentence similarity | query: {content}` Jangan gunakan ini untuk penelusuran atau pengambilan. Tujuannya adalah untuk kemiripan tekstual semantik. |

**Contoh penggunaan**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

Penting agar tugas digunakan secara konsisten. Misalnya, jika dokumen disematkan dengan `f'task: classification | query: {content}'`, kueri juga harus disematkan mengikuti format tugas ini.

### Jenis tugas dengan Embeddings 1

Untuk `gemini-embedding-001`, Anda dapat menentukan `task_type` dalam metode `embedContent`. Untuk mengetahui daftar lengkap jenis tugas yang didukung, lihat tabel [Jenis tugas yang didukung](#supported-task-types).

Contoh berikut menunjukkan cara menggunakan `SEMANTIC_SIMILARITY` untuk memeriksa seberapa mirip makna string teks.

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

### Java

```
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.ContentEmbedding;
import com.google.genai.types.EmbedContentConfig;
import com.google.genai.types.EmbedContentResponse;
import java.util.List;

Client client = new Client();

List<String> texts =
    Arrays.asList(
        "What is the meaning of life?",
        "What is the purpose of existence?",
        "How do I bake a cake?");

EmbedContentConfig config =
    EmbedContentConfig.builder().taskType("SEMANTIC_SIMILARITY").build();

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-001", texts, config);

List<ContentEmbedding> embeddings = response.embeddings().get();

for (int i = 0; i < texts.size(); i++) {
  for (int j = i + 1; j < texts.size(); j++) {
    List<Float> v1 = embeddings.get(i).values().get();
    List<Float> v2 = embeddings.get(j).values().get();
    double dotProduct = 0.0;
    double normA = 0.0;
    double normB = 0.0;
    for (int k = 0; k < v1.size(); k++) {
      dotProduct += v1.get(k) * v2.get(k);
      normA += v1.get(k) * v1.get(k);
      normB += v2.get(k) * v2.get(k);
    }
    double similarity = dotProduct / (Math.sqrt(normA) * Math.sqrt(normB));
    System.out.printf(
        "Similarity between '%s' and '%s': %.4f%n", texts.get(i), texts.get(j), similarity);
  }
}
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

Cuplikan kode akan menunjukkan seberapa mirip berbagai bagian teks satu sama lain saat dijalankan.

#### Jenis tugas yang didukung

Jenis tugas yang didukung untuk `gemini-embedding-001`:

| Jenis tugas | Deskripsi | Contoh |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | Embedding yang dioptimalkan untuk menilai kemiripan teks. | Sistem rekomendasi, deteksi duplikat |
| **KLASIFIKASI** | Penyematan dioptimalkan untuk mengklasifikasikan teks menurut label preset. | Analisis sentimen, deteksi spam |
| **PENGELOMPOKAN** | Embedding dioptimalkan untuk mengelompokkan teks berdasarkan kemiripannya. | Pengaturan dokumen, riset pasar, deteksi anomali |
| **RETRIEVAL\_DOCUMENT** | Embedding yang dioptimalkan untuk penelusuran dokumen. | Mengindeks artikel, buku, atau halaman web untuk penelusuran. |
| **RETRIEVAL\_QUERY** | Penyematan yang dioptimalkan untuk kueri penelusuran umum. Gunakan `RETRIEVAL_QUERY` untuk kueri; `RETRIEVAL_DOCUMENT` untuk dokumen yang akan diambil. | Penelusuran khusus |
| **CODE\_RETRIEVAL\_QUERY** | Embedding yang dioptimalkan untuk pengambilan blok kode berdasarkan kueri bahasa alami. Gunakan `CODE_RETRIEVAL_QUERY` untuk kueri; `RETRIEVAL_DOCUMENT` untuk blok kode yang akan diambil. | Saran dan penelusuran kode |
| **QUESTION\_ANSWERING** | Penyematan untuk pertanyaan dalam sistem tanya jawab, yang dioptimalkan untuk menemukan dokumen yang menjawab pertanyaan. Gunakan `QUESTION_ANSWERING` untuk pertanyaan; `RETRIEVAL_DOCUMENT` untuk dokumen yang akan diambil. | Kotak chat |
| **FACT\_VERIFICATION** | Penyematan untuk pernyataan yang perlu diverifikasi, dioptimalkan untuk mengambil dokumen yang berisi bukti yang mendukung atau menyangkal pernyataan tersebut. Gunakan `FACT_VERIFICATION` untuk teks target; `RETRIEVAL_DOCUMENT` untuk dokumen yang akan diambil | Sistem pengecekan fakta otomatis |

## Mengontrol ukuran penyematan

`gemini-embedding-001` dan `gemini-embedding-2` dilatih menggunakan
teknik Matryoshka Representation Learning (MRL) yang mengajarkan model untuk
mempelajari sematan berdimensi tinggi yang memiliki segmen awal (atau awalan) yang
juga merupakan versi data yang sama yang berguna dan lebih sederhana.

Gunakan parameter `output_dimensionality` untuk mengontrol ukuran
vektor sematan output. Memilih dimensi output yang lebih kecil dapat menghemat
ruang penyimpanan dan meningkatkan efisiensi komputasi untuk aplikasi hilir,
sekaligus sedikit mengorbankan kualitas. Secara default, kedua model menghasilkan sematan 3072 dimensi, tetapi Anda dapat memangkasnya ke ukuran yang lebih kecil tanpa mengurangi kualitas untuk menghemat ruang penyimpanan. Sebaiknya gunakan dimensi output 768, 1536, atau 3072.

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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.ContentEmbedding;
import com.google.genai.types.EmbedContentConfig;
import com.google.genai.types.EmbedContentResponse;

Client client = new Client();

EmbedContentConfig config =
    EmbedContentConfig.builder().outputDimensionality(768).build();

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", "What is the meaning of life?", config);

ContentEmbedding embeddingObj = response.embeddings().get().get(0);
int embeddingLength = embeddingObj.values().get().size();

System.out.println("Length of embedding: " + embeddingLength);
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

Contoh output dari cuplikan kode:

```
Length of embedding: 768
```

## Memastikan kualitas untuk dimensi yang lebih kecil

Meskipun embedding 3072 dimensi default selalu dinormalisasi, Gemini Embedding 2 juga menormalisasi dimensi yang dipangkas secara otomatis (misalnya, 768, 1536). Hal ini memastikan kemiripan semantik dihitung melalui arah vektor, bukan besarnya, sehingga memberikan hasil yang lebih akurat secara langsung.

**Model Lama**: Jika Anda menggunakan `gemini-embedding-001`, Anda harus menormalisasi dimensi non-3072 secara manual sebagai berikut:

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

Contoh output dari cuplikan kode ini:

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

Tabel berikut menunjukkan skor MTEB, tolok ukur yang umum digunakan untuk
embedding, untuk dimensi yang berbeda. Khususnya, hasilnya menunjukkan bahwa performa tidak terikat secara ketat dengan ukuran dimensi embedding, dengan dimensi yang lebih rendah mencapai skor yang sebanding dengan dimensi yang lebih tinggi.

| Dimensi MRL | Skor MTEB (Gemini Embedding 001) |
| --- | --- |
| 2048 | 68.16 |
| 1536 | 68,17 |
| 768 | 67,99 |
| 512 | 67,55 |
| 256 | 66,19 |
| 128 | 63,31 |

## Embedding multimodal

Model `gemini-embedding-2` mendukung input multimodal, sehingga Anda dapat menyematkan konten gambar, video, audio, dan dokumen bersama teks. Semua modalitas dipetakan ke ruang penyematan yang sama, sehingga memungkinkan penelusuran dan perbandingan lintas modalitas.

### Modalitas dan batas yang didukung

Batas token input maksimum secara keseluruhan adalah 8.192 token.

| Metode | Spesifikasi dan batasan |
| --- | --- |
| **Teks** | Mendukung hingga 8.192 token. |
| **Gambar** | Maksimum 6 gambar per permintaan. Format yang didukung: PNG, JPEG. |
| **Audio** | Durasi maksimum 180 detik. Format yang didukung: MP3, WAV. |
| **Video** | Durasi maksimum 120 detik. Format yang didukung: MP4, MOV. Codec yang didukung: H264, H265, AV1, VP9.  Sistem memproses maksimum 32 frame per video: video pendek (≤32 detik) diambil sampelnya pada 1 fps, sedangkan video yang lebih panjang diambil sampelnya secara seragam hingga 32 frame. Trek audio tidak diproses dalam file video. |
| **Dokumen (PDF)** | Maksimum 1 file per permintaan, hingga 6 halaman. |

### Menyematkan gambar

Contoh berikut menunjukkan cara menyematkan gambar menggunakan
`gemini-embedding-2`.

Gambar dapat diberikan sebagai data inline atau sebagai file yang diupload
melalui [Files API](https://ai.google.dev/gemini-api/docs/files?hl=id).

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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("example.png"));

Content content = Content.fromParts(Part.fromBytes(imageBytes, "image/png"));

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", content, null);

System.out.println(response.embeddings().orElse(null));
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

### Agregasi penyematan

Saat bekerja dengan konten multimodal, cara Anda menyusun input akan memengaruhi output embedding:

- **Beberapa bagian (digabungkan):** Menambahkan beberapa input langsung ke parameter
  `contents` akan menghasilkan satu penyematan gabungan untuk semua input.
- **Beberapa objek `Content` (terpisah):** Membungkus setiap input dalam objek
  `Content` dan meneruskannya dalam parameter `contents` akan menampilkan
  embedding terpisah untuk setiap entri.
- **Representasi tingkat postingan:** Untuk objek kompleks seperti postingan media sosial dengan beberapa item media, sebaiknya gabungkan embedding terpisah (misalnya, dengan menghitung rata-rata) untuk membuat representasi tingkat postingan yang koheren.

Contoh berikut menunjukkan cara membuat satu embedding gabungan untuk input teks dan
gambar. Cukup tambahkan beberapa input ke parameter `contents`:

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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.ContentEmbedding;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Collections;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("dog.png"));

Content content =
    Content.fromParts(
        Part.fromText("An image of a dog"),
        Part.fromBytes(imageBytes, "image/png"));

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", content, null);

// This produces one embedding
for (ContentEmbedding embedding : response.embeddings().orElse(Collections.emptyList())) {
  System.out.println(embedding.values().orElse(Collections.emptyList()));
}
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

Di sisi lain, jika Anda menggunakan objek `Content` di dalam parameter `contents`,
objek tersebut akan menampilkan penyematan terpisah. Contoh ini membuat beberapa embedding dalam satu
panggilan embedding:

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
        types.Content(parts=[types.Part.from_text(text="task: classification | query: An image of a dog")]),
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
            { parts: [{ text: 'task: classification | query: An image of a dog' }] },
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

### Java

```
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.ContentEmbedding;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Collections;
import java.util.List;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("dog.png"));

List<Content> contents =
    Arrays.asList(
        Content.fromParts(Part.fromText("task: classification | query: An image of a dog")),
        Content.fromParts(Part.fromBytes(imageBytes, "image/png")));

// Embed each Content object separately to produce separate embeddings
for (Content content : contents) {
  EmbedContentResponse response =
      client.models.embedContent("gemini-embedding-2", content, null);
  for (ContentEmbedding embedding : response.embeddings().orElse(Collections.emptyList())) {
    System.out.println(embedding.values().orElse(Collections.emptyList()));
  }
}
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
                "content": {"parts": [{"text": "task: classification | query: An image of a dog"}]}
            },
            {
                "model": "models/gemini-embedding-2",
                "content": {"parts": [{"inline_data": {"mime_type": "image/png", "data": "'"${IMG_BASE64}"'"}}]}
            }
        ]
    }'
```

### Menyematkan audio

Contoh berikut menunjukkan cara menyematkan file audio menggunakan
`gemini-embedding-2`.

File audio dapat diberikan sebagai data inline atau sebagai file yang diupload
melalui [Files API](https://ai.google.dev/gemini-api/docs/files?hl=id).

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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;

Client client = new Client();

byte[] audioBytes = Files.readAllBytes(Paths.get("example.mp3"));

Content content = Content.fromParts(Part.fromBytes(audioBytes, "audio/mpeg"));

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", content, null);

System.out.println(response.embeddings().orElse(null));
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

### Menyematkan video

Contoh berikut menunjukkan cara menyematkan video menggunakan
`gemini-embedding-2`.

Video dapat diberikan sebagai data inline atau sebagai file yang diupload
melalui [Files API](https://ai.google.dev/gemini-api/docs/files?hl=id).

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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Collections;

Client client = new Client();

byte[] videoBytes = Files.readAllBytes(Paths.get("example.mp4"));

Content content = Content.fromParts(Part.fromBytes(videoBytes, "video/mp4"));

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", content, null);

System.out.println(
    response.embeddings().get().get(0).values().orElse(Collections.emptyList()));
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

Jika perlu menyematkan video yang berdurasi >120 detik, Anda dapat membagi video menjadi segmen yang tumpang-tindih dan menyematkan setiap segmen secara terpisah.

### Menyematkan dokumen

Dokumen dalam format PDF dapat disematkan secara langsung. Model memproses konten visual dan teks
setiap halaman.

PDF dapat diberikan sebagai data inline atau sebagai file yang diupload
melalui [Files API](https://ai.google.dev/gemini-api/docs/files?hl=id).

#### Cara model memproses PDF

Saat Anda menyematkan PDF, model akan memproses dokumen menggunakan fitur visual dan teks:

- **Representasi visual:** Model merender setiap halaman sebagai gambar, yang menggunakan **258 token** per halaman.
- **Ekstraksi teks:** Model mengekstrak teks dari dokumen. Untuk **PDF native** (yang berisi teks digital), model akan mengekstrak teks secara langsung. Untuk **PDF hasil pindaian** (yang berisi gambar teks), model akan otomatis menjalankan pengenalan karakter optik (OCR) untuk mengekstrak teks.

Untuk menghitung jumlah total token untuk PDF, tambahkan token visual (258 per halaman) ke token teks. Input Anda harus sesuai dengan **batas token 8.192** model (dibagikan di semua modalitas). Sistem akan memangkas input yang melebihi batas ini tanpa pemberitahuan.

#### Batas PDF

- **File per permintaan:** Anda dapat mengirimkan maksimum 1 file PDF.
- **Batas halaman:** Anda dapat mengirimkan maksimum 6 halaman per file. Untuk kualitas terbaik, sebaiknya gunakan 1 halaman per PDF.

Contoh berikut menunjukkan cara menyematkan PDF menggunakan `gemini-embedding-2`:

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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;

Client client = new Client();

byte[] pdfBytes = Files.readAllBytes(Paths.get("example.pdf"));

Content content = Content.fromParts(Part.fromBytes(pdfBytes, "application/pdf"));

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", content, null);

System.out.println(response.embeddings().orElse(null));
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

## Kasus penggunaan

Embedding teks sangat penting untuk berbagai kasus penggunaan AI umum, seperti:

- **Retrieval-Augmented Generation (RAG):** Embedding meningkatkan kualitas teks yang dihasilkan dengan mengambil dan menggabungkan informasi yang relevan ke dalam konteks model.
- **Pengambilan informasi:** Menelusuri teks atau dokumen yang paling mirip secara semantik dengan teks input tertentu.

  [Tutorial penelusuran dokumentask](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **Pengurutan ulang penelusuran**: Memprioritaskan item yang paling relevan dengan memberi skor semantik pada hasil awal terhadap kueri.

  [Tutorial penyesuaian peringkat penelusurantask](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **Deteksi anomali:** Membandingkan grup embedding dapat membantu mengidentifikasi tren atau pencilan tersembunyi.

  [Tutorial deteksi anomalibubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **Klasifikasi:** Mengategorikan teks secara otomatis berdasarkan kontennya, seperti analisis sentimen atau deteksi spam

  [Tutorial klasifikasitoken](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **Pengelompokan:** Pahami hubungan yang kompleks secara efektif dengan membuat cluster dan visualisasi embedding Anda.

  [Tutorial visualisasi pengelompokanbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## Menyimpan embedding

Saat Anda menggunakan embedding dalam produksi, biasanya Anda akan menggunakan **database vektor** untuk menyimpan, mengindeks, dan mengambil embedding berdimensi tinggi secara efisien. Google Cloud menawarkan layanan data terkelola yang dapat digunakan untuk tujuan ini, termasuk [Gemini Enterprise Agent Platform Penelusuran Vektor 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/overview?hl=id), [BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=id), [AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=id), dan [Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=id).

Tutorial berikut menunjukkan cara menggunakan database vektor pihak ketiga lainnya dengan Gemini Embedding.

- [Tutorial ChromaDBbolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [Tutorial QDrantbolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [Tutorial Weaviatebolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [Tutorial Pineconebolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## Versi model

### Gemini Embedding 2

| Properti | Deskripsi |
| --- | --- |
| Kode model id\_card | **Gemini API**  `gemini-embedding-2` |
| saveJenis data yang didukung | **Input**  Teks, gambar, video, audio, PDF  **Output**  Embedding teks |
| token\_autoBatas token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=id) | **Batas token input**  8.192  **Ukuran dimensi output**  Fleksibel, mendukung: 128 - 3072, Direkomendasikan: 768, 1536, 3072 |
| Versi 123 | Baca [pola versi model](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#model-versions) untuk mengetahui detail selengkapnya.  - Stabil: `gemini-embedding-2` |
| calendar\_monthPembaruan terbaru | April 2026 |

### Penyematan Gemini

| Properti | Deskripsi |
| --- | --- |
| Kode model id\_card | **Gemini API**  `gemini-embedding-001` |
| saveJenis data yang didukung | **Input**  Teks  **Output**  Embedding teks |
| token\_autoBatas token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=id) | **Batas token input**  2.048  **Ukuran dimensi output**  Fleksibel, mendukung: 128 - 3072, Direkomendasikan: 768, 1536, 3072 |
| Versi 123 | Baca [pola versi model](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#model-versions) untuk mengetahui detail selengkapnya.  - Stabil: `gemini-embedding-001` |
| calendar\_monthPembaruan terbaru | Juni 2025 |

Untuk model Embedding yang tidak digunakan lagi, buka halaman
[Penghentian penggunaan](https://ai.google.dev/gemini-api/docs/deprecations?hl=id)

## Migrasi dari gemini-embedding-001

Ruang sematan antara `gemini-embedding-001` dan
`gemini-embedding-2` **tidak kompatibel**. Artinya, Anda tidak dapat
membandingkan secara langsung embedding yang dihasilkan oleh satu model dengan embedding yang dihasilkan oleh
model lainnya. Jika mengupgrade ke `gemini-embedding-2`, Anda harus menyematkan ulang semua data yang ada.

Selain ketidakcocokan, ada beberapa perbedaan penting lainnya antara kedua model tersebut:

- **Spesifikasi jenis tugas:** Dengan `gemini-embedding-001`, Anda menentukan
  jenis tugas menggunakan parameter `task_type` (misalnya, `SEMANTIC_SIMILARITY`,
  `RETRIEVAL_DOCUMENT`). Dengan `gemini-embedding-2`, parameter `task_type`
  tidak didukung. Sebagai gantinya, Anda harus menyertakan petunjuk tugas
  langsung dalam perintah untuk tugas khusus teks. Lihat
  [Jenis tugas dengan Embeddings 2](#task-types-embeddings-2) untuk mengetahui detail tentang cara memformat perintah untuk berbagai kasus penggunaan.
- **Agregasi embedding:** `gemini-embedding-001` menghasilkan embedding individual
  untuk setiap string dalam daftar input. Sebaliknya,
  `gemini-embedding-2` menghasilkan satu embedding gabungan saat beberapa
  input (seperti teks dan gambar) diberikan langsung dalam satu permintaan. Untuk
  membuat sematan terpisah untuk setiap input, bungkus setiap input dalam objek
  `Content`, atau gunakan
  [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id#batch-embedding). Lihat
  [Penyematan agregasi](#embedding-aggregation) untuk mengetahui informasi selengkapnya.
- **Normalisasi:** Jika Anda menggunakan `output_dimensionality` untuk meminta penyematan
  dengan dimensi kurang dari 3072, `gemini-embedding-2` akan otomatis
  menormalisasi penyematan yang dipangkas ini. Dengan `gemini-embedding-001`, Anda
  perlu melakukan normalisasi manual untuk dimensi selain 3072. Lihat bagian
  [Memastikan kualitas untuk dimensi yang lebih kecil](#quality-for-smaller-dimensions)
  untuk mengetahui detailnya.

## Embedding batch

Jika latensi tidak menjadi masalah, coba gunakan model Sematan Gemini dengan
[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id#batch-embedding). Hal ini
memungkinkan throughput yang jauh lebih tinggi dengan 50% harga Embedding default.
Temukan contoh cara memulai di
[Batch API cookbook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb).

## Pemberitahuan penggunaan yang bertanggung jawab

Tidak seperti model AI generatif yang membuat konten baru, model Embedding Gemini hanya ditujukan untuk mengubah format data input Anda menjadi representasi numerik. Meskipun Google bertanggung jawab untuk menyediakan model penyematan yang mengubah format data input Anda ke format numerik yang diminta, pengguna tetap bertanggung jawab sepenuhnya atas data yang mereka masukkan dan penyematan yang dihasilkan. Dengan menggunakan model Embedding Gemini, Anda mengonfirmasi bahwa Anda memiliki hak yang diperlukan atas konten apa pun yang Anda upload. Jangan membuat konten yang melanggar hak atas kekayaan intelektual atau hak privasi orang lain. Penggunaan layanan ini oleh Anda tunduk kepada [Kebijakan Penggunaan Terlarang](https://policies.google.com/terms/generative-ai/use-policy?hl=id) kami dan [Persyaratan Layanan Google](https://ai.google.dev/gemini-api/terms?hl=id).

## Mulai membangun dengan embedding

Lihat [notebook panduan memulai embedding](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb)
untuk menjelajahi kemampuan model dan mempelajari cara menyesuaikan serta memvisualisasikan
embedding Anda.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-10-09 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-10-09 UTC."],[],[]]
