---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=tr
fetched_at: 2026-06-15T06:25:44.889353+00:00
title: "Yerle\u015ftirmeler \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Yerleştirmeler

Gemini API, metin, resim, video ve diğer içerikler için yerleştirmeler oluşturmak üzere yerleştirme modelleri sunar. Elde edilen bu yerleştirmeler daha sonra semantik arama, sınıflandırma ve kümeleme gibi görevlerde kullanılabilir. Bu sayede, anahtar kelime tabanlı yaklaşımlara kıyasla daha doğru ve bağlamdan bağımsız sonuçlar elde edilebilir.

En yeni model olan `gemini-embedding-2`, Gemini API'deki ilk çok formatlı yerleştirme modelidir. Metin, resim, video, ses ve dokümanları birleştirilmiş bir yerleştirme alanına eşleyerek 100'den fazla dilde farklı formatlarda arama, sınıflandırma ve kümeleme yapılmasını sağlar. Daha fazla bilgi edinmek için [çok formatlı yerleştirmeler bölümüne](#multimodal) bakın. Yalnızca metin içeren kullanım alanlarında `gemini-embedding-001` kullanılmaya devam eder.

Veriyle artırılmış üretim (RAG) sistemleri oluşturmak, yapay zeka ürünlerinin yaygın kullanım alanlarından biridir. Gömme işlemleri, model çıkışlarını önemli ölçüde iyileştirerek doğruluk, tutarlılık ve bağlamsal zenginlik açısından daha iyi sonuçlar elde edilmesini sağlar. Yönetilen bir RAG çözümü kullanmayı tercih ederseniz RAG'yi yönetmeyi kolaylaştıran ve daha uygun maliyetli hale getiren [Dosya Arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr) aracını geliştirdik.

## Yerleştirilmiş öğeler oluşturma

Metin yerleştirmeleri oluşturmak için `embedContent` yöntemini kullanın:

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

## Performansı artırmak için görev türünü belirtin

Sınıflandırmadan belge aramaya kadar çeşitli görevler için gömmeleri kullanabilirsiniz. Doğru görev türünü belirtmek, yerleştirmelerin amaçlanan ilişkiler için optimize edilmesine yardımcı olarak doğruluğu ve verimliliği en üst düzeye çıkarır.

### Embeddings 2 ile görev türleri

`gemini-embedding-2` içeren yalnızca metin görevlerinde, isteminize görev talimatını eklemenizi önemle tavsiye ederiz. Bu işlem, sorguyu ve dokümanı doğru görev önekiyle biçimlendirerek yapılabilir.

Aşağıdaki tablolarda, `gemini-embedding-2` modelini kullanarak simetrik ve asimetrik kullanım alanları için sorguların ve dokümanların nasıl biçimlendirileceğine dair örnekler gösterilmektedir.

**Alma kullanım alanları (Asimetrik biçim)**

Asimetrik kullanım alanlarında, sorguya görev önekini ekleyin ve yerleştirmek ile almak istediğiniz içerik için belge yapısını uygulayın.

| Kullanım alanı | Sorgu yapısı | Belge yapısı |
| --- | --- | --- |
| Arama sorgusu | `task: search result | query: {content}` | `title: {title} | text: {content}` Başlık yoksa `title: none` kullanın. |
| Soru yanıtlama | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| Doğruluk kontrolü | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| Kod alma | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**Kullanım örneği**

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

**Tek girişli kullanım alanları (Simetrik biçim)**

Simetrik kullanım alanlarında, aynı görev için sorgu ve belgede aynı biçimlendirmeyi kullanın.

| Kullanım alanı | Giriş yapısı |
| --- | --- |
| Sınıflandırma | `task: classification | query: {content}` |
| Kümeleme | `task: clustering | query: {content}` |
| Semantik benzerlik | `task: sentence similarity | query: {content}` Arama veya alma için kullanmayın. Semantik metin benzerliği için tasarlanmıştır. |

**Kullanım örneği**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

Görevlerin tutarlı bir şekilde kullanılması önemlidir. Örneğin, dokümanlar `f'task: classification | query: {content}'` ile yerleştirilmişse sorgu da bu görev biçimine göre yerleştirilmelidir.

### Yerleştirme 1 ile görev türleri

`gemini-embedding-001` için `embedContent` yönteminde `task_type` değerini belirtebilirsiniz. Desteklenen görev türlerinin tam listesi için [Desteklenen görev türleri](#supported-task-types) tablosuna bakın.

Aşağıdaki örnekte, `SEMANTIC_SIMILARITY` kullanarak metin dizelerinin anlam olarak ne kadar benzer olduğunu nasıl kontrol edebileceğiniz gösterilmektedir.

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

Kod snippet'leri çalıştırıldığında farklı metin parçalarının birbirine ne kadar benzediğini gösterir.

#### Desteklenen görev türleri

`gemini-embedding-001` için desteklenen görev türleri:

| Görev türü | Açıklama | Örnekler |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | Metin benzerliğini değerlendirmek için optimize edilmiş yerleştirmeler. | Öneri sistemleri, yinelenen öğe algılama |
| **SINIFLANDIRMA** | Metinleri önceden ayarlanmış etiketlere göre sınıflandırmak için optimize edilmiş gömmeler. | Duygu analizi, spam yakalama |
| **KÜMELEME** (CLUSTERING) | Metinleri benzerliklerine göre kümelemek için optimize edilmiş gömmeler. | Belge düzenleme, pazar araştırması, anormallik algılama |
| **RETRIEVAL\_DOCUMENT** | Doküman arama için optimize edilmiş yerleştirmeler. | Arama için makaleleri, kitapları veya web sayfalarını dizine ekleme |
| **RETRIEVAL\_QUERY** | Genel arama sorguları için optimize edilmiş gömmeler. Sorgular için `RETRIEVAL_QUERY`, alınacak dokümanlar için `RETRIEVAL_DOCUMENT` kullanın. | Özel arama ağı |
| **CODE\_RETRIEVAL\_QUERY** | Doğal dil sorgularına dayalı kod bloklarının alınması için optimize edilmiş gömmeler. Sorgular için `CODE_RETRIEVAL_QUERY`, alınacak kod blokları için `RETRIEVAL_DOCUMENT` kullanın. | Kod önerileri ve arama |
| **QUESTION\_ANSWERING** | Soru-cevap sistemindeki sorular için yerleştirmeler. Bu yerleştirmeler, soruyu yanıtlayan belgeleri bulmak üzere optimize edilmiştir. Sorular için `QUESTION_ANSWERING`, alınacak belgeler için `RETRIEVAL_DOCUMENT` kullanın. | Chatbox |
| **FACT\_VERIFICATION** | Doğrulanması gereken ifadeler için yerleştirmeler. İfadeyi destekleyen veya çürüten kanıtlar içeren belgelerin alınması için optimize edilmiştir. Hedef metin için `FACT_VERIFICATION`, alınacak dokümanlar için `RETRIEVAL_DOCUMENT` kullanın. | Otomatik doğruluk kontrolü sistemleri |

## Yerleştirme boyutunu kontrol etme

Hem `gemini-embedding-001` hem de `gemini-embedding-2`, bir modele aynı verilerin faydalı, daha basit sürümleri olan başlangıç segmentlerine (veya öneklere) sahip yüksek boyutlu yerleştirmeleri öğrenmeyi öğreten Matryoshka Representation Learning (MRL) tekniği kullanılarak eğitilir.

Çıkış yerleştirme vektörünün boyutunu kontrol etmek için `output_dimensionality` parametresini kullanın. Daha küçük bir çıkış boyutu seçmek, depolama alanından tasarruf etmenizi ve sonraki uygulamalar için hesaplama verimliliğini artırmanızı sağlayabilir. Bu sırada kaliteden çok az ödün verilir. Her iki model de varsayılan olarak 3072 boyutlu bir yerleştirme çıktısı verir. Ancak depolama alanından tasarruf etmek için kaliteyi düşürmeden daha küçük bir boyuta kısaltabilirsiniz. 768, 1536 veya 3072 çıkış boyutlarını kullanmanızı öneririz.

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

Kod snippet'inden örnek çıkış:

```
Length of embedding: 768
```

## Daha küçük boyutlarda kaliteyi sağlama

Varsayılan 3.072 boyutlu yerleştirmeler her zaman normalleştirilirken Gemini Embedding 2, kesilmiş boyutları (ör. 768, 1.536) da otomatik olarak normalleştirir. Bu sayede, semantik benzerliğin büyüklük yerine vektör yönü üzerinden hesaplanması sağlanır ve kutudan çıkar çıkmaz daha doğru sonuçlar elde edilir.

**Eski Modeller**: `gemini-embedding-001` kullanıyorsanız 3072 olmayan boyutları aşağıdaki şekilde manuel olarak normalleştirmeniz gerekir:

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

Bu kod snippet'inden alınan örnek çıkış:

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

Aşağıdaki tabloda, farklı boyutlar için yerleştirmelerde en çok tercih edilen bir karşılaştırma ölçütü olan MTEB puanları gösterilmektedir. Sonuç, performansın kesinlikle yerleştirme boyutunun büyüklüğüne bağlı olmadığını ve daha düşük boyutların, daha yüksek boyutlu benzerleriyle karşılaştırılabilir puanlar elde ettiğini gösteriyor.

| MRL Boyutu | MTEB Puanı (Gemini Embedding 001) |
| --- | --- |
| 2048 | 68,16 |
| 1536 | 68,17 |
| 768 | 67,99 |
| 512 | 67,55 |
| 256 | 66,19 |
| 128 | 63,31 |

## Çok formatlı yerleştirmeler

`gemini-embedding-2` modeli, çok formatlı girişi destekler. Bu sayede metnin yanı sıra resim, video, ses ve belge içeriklerini de yerleştirebilirsiniz. Tüm yöntemler aynı yerleştirme alanına eşlenir. Bu sayede, yöntemler arası arama ve karşılaştırma yapılabilir.

### Desteklenen yöntemler ve sınırlar

Genel maksimum giriş jetonu sınırı 8.192 jetondur.

| Yöntem | Özellikler ve sınırlar |
| --- | --- |
| **Metin** | En fazla 8.192 jetonu destekler. |
| **Resim** | İstek başına en fazla 6 resim. Desteklenen biçimler: PNG, JPEG. |
| **Ses** | Maksimum süre 180 saniyedir. Desteklenen biçimler: MP3, WAV. |
| **Video** | Maksimum süre 120 saniyedir. Desteklenen biçimler: MP4, MOV. Desteklenen codec'ler: H264, H265, AV1, VP9.  Sistem, video başına en fazla 32 kare işler: Kısa videolar (≤32 sn) 1 FPS'de örneklenirken daha uzun videolar 32 kareye eşit şekilde örneklenir. Ses parçaları, video dosyalarında işlenmez. |
| **Belgeler (PDF)** | İstek başına en fazla 1 dosya (6 sayfaya kadar). |

### Resimleri yerleştirme

Aşağıdaki örnekte, `gemini-embedding-2` kullanarak resmin nasıl yerleştirileceği gösterilmektedir.

Resimler, satır içi veri olarak veya [Files API](https://ai.google.dev/gemini-api/docs/files?hl=tr) üzerinden yüklenen dosyalar olarak sağlanabilir.

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

### Yerleştirme toplama

Çok formatlı içeriklerle çalışırken girişinizi nasıl yapılandırdığınız, yerleştirme çıkışını etkiler:

- **Birden fazla bölüm (toplu):** Doğrudan `contents` parametresine birden fazla giriş eklemek, tüm girişler için toplu bir yerleştirme oluşturur.
- **Birden fazla `Content` nesne (ayrı):** Her girişi bir `Content` nesnesine sarmalayıp `contents` parametresinde iletmek, her giriş için ayrı yerleştirmeler döndürür.
- **Gönderi düzeyinde temsil:** Birden fazla medya öğesi içeren sosyal medya gönderileri gibi karmaşık nesneler için, tutarlı bir gönderi düzeyinde temsil oluşturmak üzere ayrı yerleştirmeleri (örneğin, ortalama alarak) toplamanızı öneririz.

Aşağıdaki örnekte, metin ve resim girişi için tek bir toplu yerleştirmenin nasıl oluşturulacağı gösterilmektedir. `contents` parametresine birden fazla giriş eklemeniz yeterlidir:

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

Diğer yandan, `contents` parametresinin içinde `Content` nesnelerini kullanırsanız ayrı yerleştirmeler döndürülür. Bu örnekte, tek bir yerleştirme çağrısında birden fazla yerleştirme oluşturulur:

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

### Ses yerleştirme

Aşağıdaki örnekte, `gemini-embedding-2` kullanarak ses dosyasının nasıl yerleştirileceği gösterilmektedir.

Ses dosyaları, satır içi veri olarak veya [Files API](https://ai.google.dev/gemini-api/docs/files?hl=tr) aracılığıyla yüklenen dosyalar olarak sağlanabilir.

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

### Video yerleştirme

Aşağıdaki örnekte, `gemini-embedding-2` kullanarak videonun nasıl yerleştirileceği gösterilmektedir.

Videolar, satır içi veri olarak veya [Files API](https://ai.google.dev/gemini-api/docs/files?hl=tr) aracılığıyla yüklenen dosyalar olarak sağlanabilir.

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

120 saniyeden uzun videoları yerleştirmeniz gerekiyorsa videoyu çakışan segmentlere ayırıp bu segmentleri ayrı ayrı yerleştirebilirsiniz.

### Dokümanları yerleştirme

PDF biçimindeki dokümanlar doğrudan yerleştirilebilir. Model, her sayfanın görsel ve metin içeriğini işler.

PDF'ler, satır içi veri olarak veya [Files API](https://ai.google.dev/gemini-api/docs/files?hl=tr) aracılığıyla yüklenen dosyalar olarak sağlanabilir.

#### Model, PDF'leri nasıl işler?

Bir PDF'yi yerleştirdiğinizde model, belgeyi hem görsel hem de metin özelliklerini kullanarak işler:

- **Görsel gösterim:** Model, her sayfayı resim olarak oluşturur. Bu işlem, sayfa başına **258 jeton** tüketir.
- **Metin çıkarma:** Model, belgedeki metni çıkarır. **Yerel PDF'ler** (dijital metin içerenler) için model, metni doğrudan ayıklar. **Taranmış PDF'lerde** (metin resimleri içeren) metni ayıklamak için model otomatik olarak optik karakter tanıma (OCR) gerçekleştirir.

Bir PDF'nin toplam jeton sayısını hesaplamak için görsel jetonları (sayfa başına 258) metin jetonlarına ekleyin. Girişleriniz,modelin **8.192 jeton sınırını** (tüm yöntemlerde geçerlidir) aşmamalıdır. Sistem, bu sınırı aşan girişleri sessizce keser.

#### PDF sınırları

- **İstek başına dosya sayısı:** En fazla 1 PDF dosyası gönderebilirsiniz.
- **Sayfa sınırı:** Dosya başına en fazla 6 sayfa gönderebilirsiniz. En iyi kalite için PDF başına 1 sayfa kullanmanızı önemle tavsiye ederiz.

Aşağıdaki örnekte, `gemini-embedding-2` kullanarak PDF'nin nasıl yerleştirileceği gösterilmektedir:

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

## Kullanım alanları

Metin yerleştirmeleri, aşağıdakiler gibi çeşitli yaygın yapay zeka kullanım alanları için çok önemlidir:

- **Veriyle artırılmış üretim (RAG):** Gömme, alakalı bilgileri alıp bir modelin bağlamına dahil ederek oluşturulan metnin kalitesini artırır.
- **Bilgi alma:** Giriş metni verildiğinde, semantik olarak en benzer metni veya belgeleri arayın.

  [Belge arama eğitimitask](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **Aramada yeniden sıralama**: İlk sonuçları sorguya göre anlamsal olarak puanlayarak en alakalı öğelere öncelik verin.

  [Arama sonuçlarını yeniden sıralama eğitimitask](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **Anormallik algılama:** Yerleştirme gruplarını karşılaştırmak, gizli trendleri veya aykırı değerleri belirlemeye yardımcı olabilir.

  [Anormallik algılama eğitimibubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **Sınıflandırma:** Metni içeriğine göre otomatik olarak kategorilere ayırın (ör. duygu analizi veya spam algılama).

  [Sınıflandırma eğitimitoken](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **Kümeleme:** Yerleştirmelerinizin kümelerini ve görselleştirmelerini oluşturarak karmaşık ilişkileri etkili bir şekilde kavrayın.

  [Kümeleme görselleştirme eğitimibubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## Yerleştirilmiş öğeleri depolama

Yerleştirmeleri üretime alırken yüksek boyutlu yerleştirmeleri verimli bir şekilde depolamak, dizine eklemek ve almak için **vektör veritabanlarını** kullanmak yaygın bir uygulamadır. Google Cloud, bu amaçla kullanılabilecek yönetilen veri hizmetleri sunar. Bu hizmetler arasında [Gemini Enterprise Agent Platform Vector Search 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/BUILD/vector-search-2?hl=tr), [BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=tr), [AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=tr) ve [Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=tr) yer alır.

Aşağıdaki eğitimlerde, Gemini Embedding ile diğer üçüncü taraf vektör veritabanlarının nasıl kullanılacağı gösterilmektedir.

- [ChromaDB eğitimleribolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [QDrant eğitimleribolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [Weaviate eğitimleribolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [Pinecone eğitimleribolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## Model sürümleri

### Gemini Embedding 2

| Mülk | Açıklama |
| --- | --- |
| id\_cardModel kodu | **Gemini API**  `gemini-embedding-2` |
| saveDesteklenen veri türleri | **Giriş**  Metin, resim, video, ses, PDF  **Çıkış**  Metin yerleştirmeleri |
| token\_autoJeton sınırları[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) | **Giriş jetonu sınırı**  8.192  **Çıkış boyutu**  Esnek, desteklenen boyutlar: 128 - 3072, Önerilen boyutlar: 768, 1536, 3072 |
| 123Sürümleri | Daha fazla bilgi için [model sürümü kalıplarını](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#model-versions) okuyun.  - Kararlı: `gemini-embedding-2` |
| calendar\_monthSon güncelleme | Nisan 2026 |

### Gemini Embedding

| Mülk | Açıklama |
| --- | --- |
| id\_cardModel kodu | **Gemini API**  `gemini-embedding-001` |
| saveDesteklenen veri türleri | **Giriş**  Metin  **Çıkış**  Metin yerleştirmeleri |
| token\_autoJeton sınırları[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) | **Giriş jetonu sınırı**  2.048  **Çıkış boyutu**  Esnek, desteklenen boyutlar: 128 - 3072, Önerilen boyutlar: 768, 1536, 3072 |
| 123Sürümleri | Daha fazla bilgi için [model sürümü kalıplarını](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#model-versions) okuyun.  - Kararlı: `gemini-embedding-001` |
| calendar\_monthSon güncelleme | Haziran 2025 |

Desteği sonlandırılan Embeddings modelleri için [Desteği Sonlandırılanlar](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr) sayfasını ziyaret edin.

## gemini-embedding-001'den taşıma

`gemini-embedding-001` ile `gemini-embedding-2` arasındaki yerleştirme alanları **uyumlu değildir**. Bu nedenle, bir model tarafından oluşturulan yerleştirmeleri doğrudan diğer model tarafından oluşturulan yerleştirmelerle karşılaştıramazsınız. `gemini-embedding-2` sürümüne yükseltiyorsanız mevcut verilerinizin tamamını yeniden yerleştirmeniz gerekir.

Uyumsuzluğun yanı sıra iki model arasında dikkat çekici başka farklılıklar da vardır:

- **Görev türü belirtimi:** `gemini-embedding-001` ile `task_type` parametresini kullanarak görev türünü belirtirsiniz (ör. `SEMANTIC_SIMILARITY`, `RETRIEVAL_DOCUMENT`). `gemini-embedding-2` ile `task_type` parametresi desteklenmez. Bunun yerine, yalnızca metin içeren görevler için görev talimatlarını doğrudan isteme eklemelisiniz. Farklı kullanım alanları için istemleri nasıl biçimlendireceğinizle ilgili ayrıntılar için [Embeddings 2 ile görev türleri](#task-types-embeddings-2) başlıklı makaleyi inceleyin.
- **Yerleştirme toplama:** `gemini-embedding-001`, giriş listesindeki her dize için ayrı yerleştirmeler oluşturur. Buna karşılık,
  `gemini-embedding-2` birden fazla giriş (ör. metin ve resimler) doğrudan tek bir istekte sağlandığında tek bir toplu yerleştirme oluşturur. Ayrı girişler için ayrı yerleştirmeler oluşturmak üzere her girişi bir `Content` nesnesine sarmalayın veya [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr#batch-embedding)'yi kullanın. Daha fazla bilgi için [Yerleştirme toplama](#embedding-aggregation) bölümüne bakın.
- **Normalleştirme:** 3.072'den az boyutlu yerleştirmeler istemek için `output_dimensionality` kullanırsanız `gemini-embedding-2`, bu kısaltılmış yerleştirmeleri otomatik olarak normalleştirir. `gemini-embedding-001` ile 3072 dışında kalan boyutlar için manuel normalleştirme yapmanız gerekir. Ayrıntılar için [Daha küçük boyutlarda kaliteyi sağlama](#quality-for-smaller-dimensions) başlıklı makaleyi inceleyin.

## Toplu yerleştirmeler

Gecikme sorun değilse Gemini Embeddings modellerini [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr#batch-embedding) ile kullanmayı deneyin. Bu sayede, varsayılan yerleştirme fiyatının% 50'siyle çok daha yüksek işleme hızı elde edilebilir.
Başlangıçla ilgili örnekleri [Toplu API yemek kitabında](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb) bulabilirsiniz.

## Sorumlu kullanım bildirimi

Yeni içerikler oluşturan üretken yapay zeka modellerinin aksine, Gemini Embedding modeli yalnızca giriş verilerinizin biçimini sayısal bir gösterime dönüştürmek için tasarlanmıştır. Google, giriş verilerinizin biçimini istenen sayısal biçime dönüştüren bir yerleştirme modeli sağlamaktan sorumlu olsa da kullanıcılar, girdikleri veriler ve ortaya çıkan yerleştirmelerle ilgili tüm sorumluluğu üstlenir. Gemini Embedding modelini kullanarak, yüklediğiniz tüm içeriklerle ilgili gerekli haklara sahip olduğunuzu onaylarsınız. Başkalarının fikri mülkiyet veya gizlilik haklarını ihlal eden içerikler üretmeyin. Bu hizmeti kullanımınız [Yasaklanan Kullanım Politikamıza](https://policies.google.com/terms/generative-ai/use-policy?hl=tr) ve [Google'ın Hizmet Şartları](https://ai.google.dev/gemini-api/terms?hl=tr)'na tabidir.

## Yerleştirmelerle geliştirmeye başlama

Model özelliklerini keşfetmek ve yerleştirmelerinizi nasıl özelleştirip görselleştireceğinizi öğrenmek için [yerleştirme hızlı başlangıç not defterine](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb) göz atın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-29 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-29 UTC."],[],[]]
