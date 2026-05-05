---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=hi
fetched_at: 2026-05-05T20:42:50.806695+00:00
title: "\u090f\u0902\u092c\u0947\u0921 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# एंबेड करना

Gemini API, एम्बेडिंग मॉडल उपलब्ध कराता है. इनका इस्तेमाल करके, टेक्स्ट, इमेज, वीडियो, और अन्य कॉन्टेंट के लिए एम्बेडिंग जनरेट की जा सकती हैं. इसके बाद, इन एम्बेडिंग का इस्तेमाल, सिमैंटिक सर्च, क्लासिफ़िकेशन, और क्लस्टरिंग जैसे कामों के लिए किया जा सकता है. इससे कीवर्ड पर आधारित तरीकों की तुलना में, ज़्यादा सटीक और कॉन्टेक्स्ट के हिसाब से नतीजे मिलते हैं.

नया मॉडल, `gemini-embedding-2`, Gemini API में पहला मल्टीमॉडल एम्बेडिंग मॉडल है. यह टेक्स्ट, इमेज, वीडियो, ऑडियो, और दस्तावेज़ों को एक ही एम्बेडिंग स्पेस में मैप करता है. इससे 100 से ज़्यादा भाषाओं में क्रॉस-मॉडल खोज, क्लासिफ़िकेशन, और क्लस्टरिंग की जा सकती है. ज़्यादा जानने के लिए, [मल्टीमॉडल एम्बेडिंग सेक्शन](#multimodal) देखें. सिर्फ़ टेक्स्ट के लिए इस्तेमाल किए जाने वाले मामलों में, `gemini-embedding-001` उपलब्ध रहेगा.

रिट्रीवल ऑगमेंटेड जनरेशन (आरएजी) सिस्टम बनाना, एआई प्रॉडक्ट के इस्तेमाल का एक सामान्य उदाहरण है. मॉडल के आउटपुट को बेहतर बनाने में एम्बेडिंग की अहम भूमिका होती है. इससे तथ्यों के सही होने की संभावना बढ़ जाती है. साथ ही, कॉन्टेंट ज़्यादा सटीक और संदर्भ के हिसाब से ज़्यादा जानकारी वाला होता है. अगर आपको मैनेज किया गया RAG समाधान इस्तेमाल करना है, तो हमने [फ़ाइलें खोजने](https://ai.google.dev/gemini-api/docs/file-search?hl=hi) का टूल बनाया है. इससे RAG को मैनेज करना आसान हो जाता है और यह ज़्यादा किफ़ायती भी होता है.

## एमबेडिंग जनरेट की जा रही हैं

टेक्स्ट एम्बेडिंग जनरेट करने के लिए, `embedContent` तरीके का इस्तेमाल करें:

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

### ऐप पर जाएं

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

## परफ़ॉर्मेंस को बेहतर बनाने के लिए टास्क का टाइप तय करना

क्लासिफ़िकेशन से लेकर दस्तावेज़ खोजने तक, कई तरह के टास्क के लिए एम्बेडिंग का इस्तेमाल किया जा सकता है. सही टास्क टाइप तय करने से, एम्बेडिंग को बेहतर तरीके से ऑप्टिमाइज़ करने में मदद मिलती है. इससे सटीक नतीजे मिलते हैं और काम भी बेहतर तरीके से होता है.

### Embeddings 2 की मदद से किए जा सकने वाले टास्क के टाइप

हमारा सुझाव है कि `gemini-embedding-2` वाले सिर्फ़ टेक्स्ट वाले टास्क के लिए, अपने प्रॉम्प्ट में टास्क से जुड़े निर्देश जोड़ें. इसके लिए, क्वेरी और दस्तावेज़ को टास्क के सही प्रीफ़िक्स के साथ फ़ॉर्मैट करें.

यहां दी गई टेबल में, `gemini-embedding-2` मॉडल का इस्तेमाल करके सिमेट्रिक और एसिमेट्रिक इस्तेमाल के उदाहरणों के लिए, क्वेरी और दस्तावेज़ों को फ़ॉर्मैट करने के उदाहरण दिए गए हैं.

**जानकारी पाने के उदाहरण (असमान फ़ॉर्मैट)**

एसिमेट्रिक इस्तेमाल के उदाहरणों में, क्वेरी में टास्क का प्रीफ़िक्स जोड़ें. साथ ही, उस कॉन्टेंट के लिए दस्तावेज़ का स्ट्रक्चर लागू करें जिसे आपको एम्बेड और वापस पाना है.

| इस्तेमाल का उदाहरण | क्वेरी का स्ट्रक्चर | दस्तावेज़ का स्ट्रक्चर |
| --- | --- | --- |
| खोज क्वेरी | `task: search result | query: {content}` | `title: {title} | text: {content}` अगर कोई टाइटल नहीं है, तो `title: none` का इस्तेमाल करें. |
| सवाल का जवाब देना | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| तथ्यों की जांच करना | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| कोड वापस पाना | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**इस्तेमाल का उदाहरण**

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

**एक इनपुट वाले इस्तेमाल के उदाहरण (सिमेट्रिक फ़ॉर्मैट)**

सिमेट्रिक इस्तेमाल के उदाहरणों में, एक ही टास्क के लिए क्वेरी और दस्तावेज़, दोनों में एक जैसा फ़ॉर्मैट इस्तेमाल करें.

| इस्तेमाल का उदाहरण | इनपुट स्ट्रक्चर |
| --- | --- |
| कैटगरी | `task: classification | query: {content}` |
| गुच्छ | `task: clustering | query: {content}` |
| मिलते-जुलते मतलब | `task: sentence similarity | query: {content}` इसका इस्तेमाल, खोजने या वापस पाने के लिए न करें. इसका इस्तेमाल, सिमेंटिक टेक्स्ट की समानता के लिए किया जाता है. |

**इस्तेमाल का उदाहरण**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

यह ज़रूरी है कि टास्क का इस्तेमाल लगातार किया जाए. उदाहरण के लिए, अगर दस्तावेज़ों में `f'task: classification | query: {content}'` एम्बेड किया गया है, तो क्वेरी में भी इस टास्क फ़ॉर्मैट के हिसाब से एम्बेड किया जाना चाहिए.

### Embeddings 1 की सुविधा वाले टास्क टाइप

`gemini-embedding-001` के लिए, `embedContent` तरीके में `task_type` की जानकारी दी जा सकती है. इस्तेमाल किए जा सकने वाले टास्क टाइप की पूरी सूची देखने के लिए, [इस्तेमाल किए जा सकने वाले टास्क टाइप](#supported-task-types) टेबल देखें.

यहां दिए गए उदाहरण में बताया गया है कि `SEMANTIC_SIMILARITY` का इस्तेमाल करके, यह कैसे पता लगाया जा सकता है कि टेक्स्ट की स्ट्रिंग का मतलब कितना मिलता-जुलता है.

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

### ऐप पर जाएं

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

कोड स्निपेट से पता चलेगा कि टेक्स्ट के अलग-अलग हिस्सों में कितनी समानता है.

#### इस्तेमाल किए जा सकने वाले टास्क टाइप

`gemini-embedding-001` के लिए, इन टास्क टाइप का इस्तेमाल किया जा सकता है:

| टास्क किस तरह का है | ब्यौरा | उदाहरण |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | टेक्स्ट की समानता का आकलन करने के लिए, ऑप्टिमाइज़ किए गए एम्बेडिंग. | सुझाव देने वाले सिस्टम, डुप्लीकेट कॉन्टेंट का पता लगाना |
| **CLASSIFICATION** | एम्बेडिंग को ऑप्टिमाइज़ किया गया है, ताकि पहले से तय किए गए लेबल के हिसाब से टेक्स्ट को कैटगरी में बांटा जा सके. | भावनाओं का विश्लेषण, स्पैम का पता लगाना |
| **क्लस्टरिंग** | ये एम्बेडिंग, टेक्स्ट को उनकी समानता के आधार पर क्लस्टर करने के लिए ऑप्टिमाइज़ की जाती हैं. | दस्तावेज़ व्यवस्थित करना, मार्केट रिसर्च, गड़बड़ी की पहचान करना |
| **RETRIEVAL\_DOCUMENT** | दस्तावेज़ खोजने के लिए ऑप्टिमाइज़ किए गए एम्बेडिंग. | खोज के लिए लेखों, किताबों या वेब पेजों को इंडेक्स करना. |
| **RETRIEVAL\_QUERY** | सामान्य खोज क्वेरी के लिए ऑप्टिमाइज़ की गई एम्बेडिंग. क्वेरी के लिए `RETRIEVAL_QUERY` और वापस लाए जाने वाले दस्तावेज़ों के लिए `RETRIEVAL_DOCUMENT` का इस्तेमाल करें. | कस्टम सर्च |
| **CODE\_RETRIEVAL\_QUERY** | नैचुरल लैंग्वेज क्वेरी के आधार पर कोड ब्लॉक को वापस पाने के लिए, ऑप्टिमाइज़ की गई एम्बेडिंग. क्वेरी के लिए `CODE_RETRIEVAL_QUERY` और कोड ब्लॉक को वापस पाने के लिए `RETRIEVAL_DOCUMENT` का इस्तेमाल करें. | कोड से जुड़े सुझाव और खोज |
| **QUESTION\_ANSWERING** | सवाल-जवाब वाले सिस्टम में सवालों के लिए एम्बेडिंग. इन्हें ऐसे दस्तावेज़ ढूंढने के लिए ऑप्टिमाइज़ किया जाता है जिनमें सवाल का जवाब दिया गया हो. सवाल पूछने के लिए `QUESTION_ANSWERING` और दस्तावेज़ों को वापस पाने के लिए `RETRIEVAL_DOCUMENT` का इस्तेमाल करें. | चैटबॉक्स |
| **FACT\_VERIFICATION** | ऐसे स्टेटमेंट के लिए एम्बेडिंग जिनकी पुष्टि करनी है. साथ ही, ऐसे दस्तावेज़ों को वापस पाने के लिए ऑप्टिमाइज़ किया गया है जिनमें स्टेटमेंट के पक्ष या विपक्ष में सबूत मौजूद हैं. टारगेट किए गए टेक्स्ट के लिए `FACT_VERIFICATION` का इस्तेमाल करें; जिन दस्तावेज़ों को वापस पाना है उनके लिए `RETRIEVAL_DOCUMENT` का इस्तेमाल करें | तथ्यों की जांच करने वाले ऑटोमेटेड सिस्टम |

## एम्बेड किए गए कॉन्टेंट के साइज़ को कंट्रोल करना

`gemini-embedding-001` और `gemini-embedding-2`, दोनों को Matryoshka Representation Learning (MRL) तकनीक का इस्तेमाल करके ट्रेन किया जाता है. यह तकनीक, मॉडल को ज़्यादा डाइमेंशन वाले एम्बेडिंग सीखने के बारे में बताती है. इन एम्बेडिंग में शुरुआती सेगमेंट (या प्रीफ़िक्स) होते हैं, जो एक ही डेटा के काम के और आसान वर्शन होते हैं.

आउटपुट एम्बेडिंग वेक्टर के साइज़ को कंट्रोल करने के लिए, `output_dimensionality` पैरामीटर का इस्तेमाल करें. आउटपुट डाइमेंशनैलिटी को कम करने से, स्टोरेज स्पेस बचाया जा सकता है. साथ ही, डाउनस्ट्रीम ऐप्लिकेशन के लिए कंप्यूटेशनल क्षमता को बढ़ाया जा सकता है. हालांकि, इससे क्वालिटी में थोड़ी कमी आ सकती है. डिफ़ॉल्ट रूप से, दोनों मॉडल 3072 डाइमेंशन वाली एम्बेडिंग का आउटपुट देते हैं. हालांकि, स्टोरेज की जगह बचाने के लिए, इसकी क्वालिटी को कम किए बिना इसे छोटे साइज़ में काटा जा सकता है. हमारा सुझाव है कि आउटपुट डाइमेंशन के लिए 768, 1536 या 3072 का इस्तेमाल करें.

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

### ऐप पर जाएं

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

कोड स्निपेट से मिले आउटपुट का उदाहरण:

```
Length of embedding: 768
```

## छोटे डाइमेंशन के लिए क्वालिटी को बेहतर बनाना

डिफ़ॉल्ट रूप से 3072 डाइमेंशन वाली एम्बेडिंग हमेशा सामान्य होती हैं. हालांकि, Gemini Embedding 2, काटे गए डाइमेंशन (जैसे कि 768, 1536) को भी अपने-आप सामान्य कर देता है. इससे यह पक्का होता है कि सिमैंटिक समानता को वेक्टर डायरेक्शन के ज़रिए कैलकुलेट किया जाता है, न कि मैग्नीट्यूड के ज़रिए. इससे आपको ज़्यादा सटीक नतीजे मिलते हैं.

**पुराने मॉडल**: अगर `gemini-embedding-001` का इस्तेमाल किया जा रहा है, तो आपको 3072 से कम डाइमेंशन को मैन्युअल तरीके से इस तरह सामान्य करना होगा:

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

इस कोड स्निपेट का उदाहरण आउटपुट:

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

यहां दी गई टेबल में, अलग-अलग डाइमेंशन के लिए MTEB स्कोर दिए गए हैं. MTEB स्कोर, एम्बेडिंग के लिए आम तौर पर इस्तेमाल किया जाने वाला बेंचमार्क है. खास तौर पर, नतीजे से पता चलता है कि परफ़ॉर्मेंस, एम्बेडिंग डाइमेंशन के साइज़ से पूरी तरह जुड़ी नहीं होती. कम डाइमेंशन वाले मॉडल, ज़्यादा डाइमेंशन वाले मॉडल के मुकाबले बेहतर स्कोर हासिल करते हैं.

| एमआरएल डाइमेंशन | एमटीईबी स्कोर (Gemini Embedding 001) |
| --- | --- |
| 2048 | 68.16 |
| 1536 | 68.17 |
| 768 | 67.99 |
| 512 | 67.55 |
| 256 | 66.19 |
| 128 | 63.31 |

## मल्टीमॉडल एम्बेडिंग

`gemini-embedding-2` मॉडल में टेक्स्ट, इमेज, वीडियो, ऑडियो, और दस्तावेज़ों के कॉन्टेंट को एक साथ इस्तेमाल किया जा सकता है. सभी मोडेलिटी को एक ही एम्बेडिंग स्पेस में मैप किया जाता है. इससे अलग-अलग मोडेलिटी में खोज करने और उनकी तुलना करने की सुविधा मिलती है.

### इस्तेमाल की जा सकने वाली सुविधाएं और सीमाएं

इनपुट के लिए, कुल 8,192 टोकन इस्तेमाल किए जा सकते हैं.

| मोडेलिटी | खासियतें और सीमाएं |
| --- | --- |
| **टेक्स्ट** | इसमें ज़्यादा से ज़्यादा 8,192 टोकन इस्तेमाल किए जा सकते हैं. |
| **इमेज** | हर अनुरोध में ज़्यादा से ज़्यादा छह इमेज शामिल की जा सकती हैं. इस्तेमाल किए जा सकने वाले फ़ॉर्मैट: PNG, JPEG. |
| **ऑडियो** | ज़्यादा से ज़्यादा 180 सेकंड का हो. इस्तेमाल किए जा सकने वाले फ़ॉर्मैट: MP3, WAV. |
| **वीडियो** | ज़्यादा से ज़्यादा 120 सेकंड का हो. इस्तेमाल किए जा सकने वाले फ़ॉर्मैट: MP4, MOV. काम करने वाले कोडेक: H264, H265, AV1, VP9.  सिस्टम, हर वीडियो के लिए ज़्यादा से ज़्यादा 32 फ़्रेम प्रोसेस करता है: 32 सेकंड या इससे कम अवधि वाले शॉर्ट वीडियो को 1 एफ़पीएस पर सैंपल किया जाता है. वहीं, लंबी अवधि वाले वीडियो को 32 फ़्रेम पर सैंपल किया जाता है. वीडियो फ़ाइलों में ऑडियो ट्रैक प्रोसेस नहीं किए जाते. |
| **दस्तावेज़ (PDF)** | ज़्यादा से ज़्यादा छह पेज. |

### इमेज एम्बेड करना

यहां दिए गए उदाहरण में, `gemini-embedding-2` का इस्तेमाल करके इमेज एम्बेड करने का तरीका बताया गया है.

इमेज को इनलाइन डेटा के तौर पर या [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi) के ज़रिए अपलोड की गई फ़ाइलों के तौर पर उपलब्ध कराया जा सकता है.

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

### एम्बेडिंग एग्रीगेशन

मल्टीमॉडल कॉन्टेंट के साथ काम करते समय, इनपुट को स्ट्रक्चर करने का तरीका, एम्बेडिंग आउटपुट पर असर डालता है:

- **कई हिस्से (एक साथ):** `contents` पैरामीटर में सीधे तौर पर कई इनपुट जोड़ने से, सभी इनपुट के लिए एक साथ एग्रीगेट की गई एम्बेडिंग जनरेट होती है.
- **एक से ज़्यादा `Content` ऑब्जेक्ट (अलग-अलग):** हर इनपुट को `Content` ऑब्जेक्ट में रैप करके, उन्हें `contents` पैरामीटर में पास करने पर, हर एंट्री के लिए अलग-अलग एम्बेडिंग मिलती हैं.
- **पोस्ट-लेवल पर जानकारी देना:** सोशल मीडिया पोस्ट जैसे जटिल ऑब्जेक्ट के लिए, जिनमें कई मीडिया आइटम शामिल होते हैं, हमारा सुझाव है कि आप अलग-अलग एम्बेडिंग को एग्रीगेट करें. उदाहरण के लिए, पोस्ट-लेवल पर एक जैसी जानकारी देने के लिए, औसत निकालकर एग्रीगेट करें.

यहां दिए गए उदाहरण में, टेक्स्ट और इमेज के इनपुट के लिए एक एग्रीगेटेड एम्बेडिंग बनाने का तरीका बताया गया है. `contents` पैरामीटर में कई इनपुट जोड़ें:

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

वहीं दूसरी ओर, अगर `Content` पैरामीटर में `Content` ऑब्जेक्ट का इस्तेमाल किया जाता है, तो यह अलग-अलग एम्बेडिंग दिखाता है.`contents` इस उदाहरण में, एंबेड करने के एक ही कॉल में कई एंबेडिंग बनाई गई हैं:

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

### ऑडियो एम्बेड करना

यहां दिए गए उदाहरण में, `gemini-embedding-2` का इस्तेमाल करके ऑडियो फ़ाइल को एम्बेड करने का तरीका बताया गया है.

ऑडियो फ़ाइलें, इनलाइन डेटा के तौर पर या [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi) के ज़रिए अपलोड की गई फ़ाइलों के तौर पर उपलब्ध कराई जा सकती हैं.

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

### वीडियो एम्बेड करना

यहां दिए गए उदाहरण में, `gemini-embedding-2` का इस्तेमाल करके वीडियो एम्बेड करने का तरीका बताया गया है.

वीडियो, इनलाइन डेटा के तौर पर या [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi) के ज़रिए अपलोड की गई फ़ाइलों के तौर पर दिए जा सकते हैं.

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

अगर आपको 120 सेकंड से ज़्यादा अवधि के वीडियो एम्बेड करने हैं, तो वीडियो को ओवरलैप होने वाले सेगमेंट में बांटें. इसके बाद, उन सेगमेंट को अलग-अलग एम्बेड करें.

### दस्तावेज़ों को एम्बेड करना

PDF फ़ॉर्मैट में मौजूद दस्तावेज़ों को सीधे तौर पर एम्बेड किया जा सकता है. यह मॉडल, हर पेज के विज़ुअल और टेक्स्ट कॉन्टेंट को प्रोसेस करता है.

पीडीएफ़ को इनलाइन डेटा के तौर पर या [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi) के ज़रिए अपलोड की गई फ़ाइलों के तौर पर उपलब्ध कराया जा सकता है.

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

## उपयोग के उदाहरण

टेक्स्ट एम्बेडिंग, एआई के कई सामान्य इस्तेमाल के उदाहरणों के लिए ज़रूरी होती हैं. जैसे:

- **रिट्रीवल ऑगमेंटेड जनरेशन (आरएजी):** एम्बेडिंग, जनरेट किए गए टेक्स्ट की क्वालिटी को बेहतर बनाती हैं. इसके लिए, वे मॉडल के कॉन्टेक्स्ट में काम की जानकारी को वापस लाती हैं और उसे शामिल करती हैं.
- **जानकारी पाना:** दिए गए इनपुट टेक्स्ट के आधार पर, मतलब के हिसाब से सबसे मिलते-जुलते टेक्स्ट या दस्तावेज़ों को खोजना.

  [दस्तावेज़ खोजने से जुड़ा ट्यूटोरियलtask](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **खोज के नतीजों को फिर से रैंक करना**: क्वेरी के हिसाब से, शुरुआती नतीजों को सेमैंटिक तौर पर स्कोर करके, सबसे काम के आइटम को प्राथमिकता दें.

  [खोज के नतीजों को फिर से रैंक करने से जुड़ा ट्यूटोरियलtask](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **गड़बड़ी की पहचान करना:** एम्बेडिंग के ग्रुप की तुलना करने से, छिपे हुए ट्रेंड या असामान्य डेटा की पहचान करने में मदद मिल सकती है.

  [गड़बड़ी की पहचान करने से जुड़ा ट्यूटोरियलbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **वर्गीकरण:** टेक्स्ट के कॉन्टेंट के आधार पर, उसे अपने-आप कैटगरी में बांटना. जैसे, भावनाओं का विश्लेषण करना या स्पैम का पता लगाना

  [क्लासिफ़िकेशन से जुड़ा ट्यूटोरियलtoken](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **क्लस्टरिंग:** अपने एम्बेडिंग के क्लस्टर और विज़ुअलाइज़ेशन बनाकर, मुश्किल संबंधों को आसानी से समझें.

  [क्लस्टरिंग विज़ुअलाइज़ेशन ट्यूटोरियलbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## एंबेड किए गए डेटा को सेव करना

एम्बेडिंग को प्रोडक्शन में ले जाते समय, **वेक्टर डेटाबेस** का इस्तेमाल करना आम बात है. इससे ज़्यादा डाइमेंशन वाली एम्बेडिंग को आसानी से सेव, इंडेक्स, और वापस पाया जा सकता है. Google Cloud, मैनेज की गई डेटा सेवाएं उपलब्ध कराता है. इनका इस्तेमाल इस काम के लिए किया जा सकता है. इनमें [Gemini Enterprise Agent Platform Vector Search 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/BUILD/vector-search-2?hl=hi), [BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=hi), [AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=hi), और [Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=hi) शामिल हैं.

यहाँ दिए गए ट्यूटोरियल में, Gemini Embedding के साथ तीसरे पक्ष के अन्य वेक्टर डेटाबेस इस्तेमाल करने का तरीका बताया गया है.

- [ChromaDB ट्यूटोरियलbolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [QDrant ट्यूटोरियलbolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [Weaviate के ट्यूटोरियलbolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [Pinecone ट्यूटोरियलbolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## मॉडल के वर्शन

### Gemini Embedding 2

| प्रॉपर्टी | ब्यौरा |
| --- | --- |
| id\_cardमॉडल कोड | **Gemini API**  `gemini-embedding-2` |
| saveइस्तेमाल किए जा सकने वाले डेटा टाइप | **इनपुट**  टेक्स्ट, इमेज, वीडियो, ऑडियो, PDF  **आउटपुट**  टेक्स्ट एम्बेडिंग |
| token\_autoटोकन की सीमाएं[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) | **इनपुट टोकन की सीमा**  8,192  **आउटपुट डाइमेंशन का साइज़**  लचीला, इन साइज़ के साथ काम करता है: 128 - 3072, सुझाया गया साइज़: 768, 1536, 3072 |
| 123वर्शन | ज़्यादा जानकारी के लिए, [मॉडल वर्शन के पैटर्न](https://ai.google.dev/gemini-api/docs/models/gemini?hl=hi#model-versions) पढ़ें.  - स्थिर: `gemini-embedding-2` |
| calendar\_monthनया अपडेट | अप्रैल 2026 |

### Gemini Embedding

| प्रॉपर्टी | ब्यौरा |
| --- | --- |
| id\_cardमॉडल कोड | **Gemini API**  `gemini-embedding-001` |
| saveइस्तेमाल किए जा सकने वाले डेटा टाइप | **इनपुट**  टेक्स्ट  **आउटपुट**  टेक्स्ट एम्बेडिंग |
| token\_autoटोकन की सीमाएं[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) | **इनपुट टोकन की सीमा**  2,048  **आउटपुट डाइमेंशन का साइज़**  लचीला, इन साइज़ के साथ काम करता है: 128 - 3072, सुझाया गया साइज़: 768, 1536, 3072 |
| 123वर्शन | ज़्यादा जानकारी के लिए, [मॉडल वर्शन के पैटर्न](https://ai.google.dev/gemini-api/docs/models/gemini?hl=hi#model-versions) पढ़ें.  - स्थिर: `gemini-embedding-001` |
| calendar\_monthनया अपडेट | जून 2025 |

काम न करने वाले Embeddings मॉडल के बारे में जानने के लिए, [Deprecations](https://ai.google.dev/gemini-api/docs/deprecations?hl=hi) पेज पर जाएं

## gemini-embedding-001 से माइग्रेट करना

`gemini-embedding-001` और `gemini-embedding-2` के बीच एम्बेडिंग स्पेस **काम नहीं करते**. इसका मतलब है कि एक मॉडल से जनरेट किए गए एम्बेडिंग की तुलना, दूसरे मॉडल से जनरेट किए गए एम्बेडिंग से सीधे तौर पर नहीं की जा सकती. `gemini-embedding-2` पर अपग्रेड करने पर, आपको अपना मौजूदा डेटा फिर से एम्बेड करना होगा.

इन दोनों मॉडल के बीच, कई अन्य अहम अंतर भी हैं. जैसे:

- **टास्क टाइप की खास जानकारी:** `gemini-embedding-001` की मदद से, `task_type` पैरामीटर का इस्तेमाल करके टास्क टाइप तय किया जाता है. जैसे, `SEMANTIC_SIMILARITY`, `RETRIEVAL_DOCUMENT`. `gemini-embedding-2` में, `task_type` पैरामीटर काम नहीं करता. इसके बजाय, आपको सिर्फ़ टेक्स्ट वाले टास्क के लिए, टास्क से जुड़े निर्देश सीधे तौर पर प्रॉम्प्ट में शामिल करने चाहिए. अलग-अलग इस्तेमाल के उदाहरणों के लिए प्रॉम्प्ट को फ़ॉर्मैट करने के तरीके के बारे में जानने के लिए, [Embeddings 2 की सुविधा के साथ काम करने वाले टास्क टाइप](#task-types-embeddings-2) देखें.
- **एंबेडिंग एग्रीगेशन:** `gemini-embedding-001` इनपुट की सूची में मौजूद हर स्ट्रिंग के लिए अलग-अलग एंबेडिंग जनरेट करता है. इसके उलट, `gemini-embedding-2` एक ही अनुरोध में सीधे तौर पर कई इनपुट (जैसे कि टेक्स्ट और इमेज) दिए जाने पर, एक एग्रीगेटेड एम्बेडिंग जनरेट करता है. अलग-अलग इनपुट के लिए अलग-अलग एम्बेडिंग जनरेट करने के लिए, हर इनपुट को `Content` ऑब्जेक्ट में रैप करें या [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi#batch-embedding) का इस्तेमाल करें. ज़्यादा जानकारी के लिए, [एग्रीगेशन को एम्बेड करना](#embedding-aggregation) लेख पढ़ें.
- **नॉर्मलाइज़ेशन:** अगर `output_dimensionality` का इस्तेमाल करके, 3072 से कम डाइमेंशन वाले एम्बेडिंग का अनुरोध किया जाता है, तो `gemini-embedding-2` अपने-आप इन छोटे किए गए एम्बेडिंग को नॉर्मलाइज़ कर देता है. `gemini-embedding-001` के साथ, आपको 3072 के अलावा अन्य डाइमेंशन के लिए मैन्युअल तरीके से नॉर्मलाइज़ेशन करना होगा. ज़्यादा जानकारी के लिए, [छोटे डाइमेंशन के लिए क्वालिटी बनाए रखना](#quality-for-smaller-dimensions) लेख पढ़ें.

## बैच एम्बेड करना

अगर आपको जवाब मिलने में देरी से कोई समस्या नहीं है, तो Gemini Embeddings मॉडल के साथ [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi#batch-embedding) का इस्तेमाल करें. इससे डिफ़ॉल्ट एम्बेडिंग की कीमत के 50% पर, ज़्यादा थ्रूपुट मिलता है.
[Batch API की कुकबुक](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb) में, इसका इस्तेमाल शुरू करने के उदाहरण देखें.

## ज़िम्मेदारी के साथ इस्तेमाल करने के बारे में सूचना

जनरेटिव एआई मॉडल नया कॉन्टेंट बनाते हैं. हालांकि, Gemini Embedding मॉडल का मकसद सिर्फ़ आपके इनपुट डेटा के फ़ॉर्मैट को संख्यात्मक रूप में बदलना है. Google, एम्बेडिंग मॉडल उपलब्ध कराने के लिए ज़िम्मेदार है. यह मॉडल, आपके इनपुट डेटा के फ़ॉर्मैट को अनुरोध किए गए संख्यात्मक फ़ॉर्मैट में बदलता है. हालांकि, उपयोगकर्ता अपने इनपुट किए गए डेटा और उससे मिलने वाली एम्बेडिंग के लिए पूरी तरह से ज़िम्मेदार होते हैं. Gemini Embedding मॉडल का इस्तेमाल करने का मतलब है कि आपने पुष्टि की है कि आपके पास अपलोड किए गए कॉन्टेंट को इस्तेमाल करने के लिए ज़रूरी अधिकार हैं. ऐसा कोई कॉन्टेंट जनरेट न करें जिससे किसी की बौद्धिक संपत्ति या निजता के अधिकारों का उल्लंघन होता हो. इस सेवा के इस्तेमाल पर, हमारी [इस्तेमाल पर पाबंदी से जुड़ी नीति](https://policies.google.com/terms/generative-ai/use-policy?hl=hi) और [Google की सेवा की शर्तें](https://ai.google.dev/gemini-api/terms?hl=hi) लागू होती हैं.

## एंबेडिंग का इस्तेमाल करके ऐप्लिकेशन बनाना

मॉडल की क्षमताओं के बारे में जानने के लिए, [एम्बेडिंग की क्विकस्टार्ट नोटबुक](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb) देखें. साथ ही, यह भी जानें कि एम्बेडिंग को अपनी पसंद के मुताबिक कैसे बनाया और विज़ुअलाइज़ किया जा सकता है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-01 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-01 (UTC) को अपडेट किया गया."],[],[]]
