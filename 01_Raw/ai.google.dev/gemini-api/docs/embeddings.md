---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=bn
fetched_at: 2026-10-19T05:52:25.553042+00:00
title: "\u098f\u09ae\u09cd\u09ac\u09c7\u09a1\u09bf\u0982 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs?hl=bn)

মতামত জানান

# এম্বেডিং

Gemini API, টেক্সট, ছবি, ভিডিও ও অন্যান্য কন্টেন্টের জন্য এম্বেডিং জেনারেট করতে এম্বেডিং মডেল অফার করে। এইসব এম্বেডিংয়ের ফলাফলকে সেম্যান্টিক সার্চ, ক্লাসিফিকেশন ও ক্লাস্টারিংয়ের মতো
টাস্কের জন্য ব্যবহার করা যেতে পারে। এর ফলে কীওয়ার্ড-ভিত্তিক পদ্ধতির তুলনায় আরও নিখুঁত,
প্রসঙ্গ-সচেতন ফলাফল পাওয়া যায়।

লেটেস্ট মডেল, `gemini-embedding-2`, হল Gemini API-তে প্রথম মাল্টিমোডাল
এমবেডিং মডেল। এটি টেক্সট, ছবি,
ভিডিও, অডিও ও ডকুমেন্টকে একটি ইউনিফায়েড এম্বেডিং স্পেসে ম্যাপ করে, এর ফলে ১০০টিরও বেশি ভাষা জুড়ে ক্রস-মোডাল
সার্চ, শ্রেণীবিন্যাস ও ক্লাস্টারিং করা যায়। আরও জানতে
[মাল্টিমোডাল এম্বেডিং বিভাগ](#multimodal) দেখুন। শুধুমাত্র টেক্সট-ভিত্তিক
ব্যবহারের ক্ষেত্রে, `gemini-embedding-001` উপলভ্য থাকে।

AI প্রোডাক্টের জন্য রিট্রিভাল অগমেন্টেড জেনারেশন (RAG) সিস্টেম তৈরি করা হল একটি সাধারণ ব্যবহারের উদাহরণ।
উন্নত ফ্যাকচুয়াল নির্ভুলতা, সুসংবদ্ধতা ও প্রাসঙ্গিক সমৃদ্ধির সাথে
মডেল আউটপুট উল্লেখযোগ্যভাবে উন্নত করার ক্ষেত্রে এম্বেডিং গুরুত্বপূর্ণ ভূমিকা পালন করে। আপনি যদি ম্যানেজ করা RAG সলিউশন ব্যবহার করতে চান, তাহলে আমরা [ফাইল সার্চ](https://ai.google.dev/gemini-api/docs/file-search?hl=bn)
টুল তৈরি করেছি যা RAG-কে আরও সহজে ম্যানেজ করতে এবং আরও সাশ্রয়ী করে তুলতে সাহায্য করে।

## এম্বেডিং জেনারেট করা

টেক্সট এম্বেডিং জেনারেট করতে `embedContent` পদ্ধতি ব্যবহার করুন:

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

## পারফর্ম্যান্স উন্নত করতে টাস্কের ধরন নির্দিষ্ট করুন

আপনি ক্লাসিফিকেশন থেকে ডকুমেন্ট
সার্চ পর্যন্ত বিভিন্ন ধরনের টাস্কের জন্য এম্বেডিং ব্যবহার করতে পারবেন। সঠিক টাস্কের ধরন নির্দিষ্ট করলে, কাঙ্ক্ষিত সম্পর্কের জন্য এম্বেডিং অপ্টিমাইজ করতে সাহায্য করে,
যার ফলে নির্ভুলতা ও কার্যকারিতা সর্বাধিক হয়।

### Embeddings 2-এর সাথে টাস্কের ধরন

`gemini-embedding-2` সহ শুধুমাত্র টেক্সট-ভিত্তিক টাস্কের জন্য, আমরা আপনাকে
প্রম্পটে টাস্কের নির্দেশাবলী যোগ করার জন্য বিশেষভাবে সাজেস্ট করি। সঠিক টাস্ক প্রিফিক্স সহ কোয়েরি ও ডকুমেন্ট ফর্ম্যাট
করার মাধ্যমে এটি করা যেতে পারে।

[মাল্টিমোডাল ইনপুটের উপর ভিত্তি করে একটি এম্বেডিং জেনারেট করার
সময়](#embedding-aggregation), আমরা সাধারণত ইনপুটের টেক্সট
অংশে টাস্ক নির্দেশাবলী প্রিফিক্স করার সাজেশন দিই না। কিছু ক্ষেত্রে এটি পারফর্ম্যান্স উন্নত করে, কিন্তু অন্যান্য ক্ষেত্রে এটি পারফর্ম্যান্স কমিয়ে দেয়।

`gemini-embedding-2` মডেল ব্যবহার করে সিমেট্রিক ও অ্যাসিমেট্রিক ব্যবহারের ক্ষেত্রে কোয়েরি ও ডকুমেন্ট কীভাবে ফর্ম্যাট করতে হয়, তার উদাহরণ নিচে দেওয়া হল।

**রিট্রিভালের ব্যবহারিক উদাহরণ (অপ্রতিসম ফর্ম্যাট)**

অসমমিতিক ব্যবহারের ক্ষেত্রে, কোয়েরিতে টাস্ক প্রিফিক্স যোগ করুন এবং আপনি যে কন্টেন্ট এম্বেড ও রিট্রিভ করতে চান তার জন্য
ডকুমেন্ট স্ট্রাকচার প্রয়োগ করুন।

| ব্যবহারিক ক্ষেত্র | কোয়েরি স্ট্রাকচার | ডকুমেন্টের গঠন |
| --- | --- | --- |
| সার্চ কোয়েরি | `task: search result | query: {content}` | `title: {title} | text: {content}` কোনও শীর্ষক না থাকলে, `title: none` ব্যবহার করুন। |
| প্রশ্নের উত্তর দেওয়া | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| সত্যতা যাচাই করা | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| কোড ফিরিয়ে আনা | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**ব্যবহারের উদাহরণ**

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

**সিঙ্গেল-ইনপুট ব্যবহারের উদাহরণ (সিমেট্রিক ফর্ম্যাট)**

সিমেট্রিক ব্যবহারের ক্ষেত্রে, একই টাস্কের জন্য, কোয়েরি ও ডকুমেন্টের জন্য একই ফর্ম্যাটিং
ব্যবহার করুন।

| ব্যবহারিক ক্ষেত্র | ইনপুট স্ট্রাকচার |
| --- | --- |
| শ্রেণীবিভাগ | `task: classification | query: {content}` |
| ক্লাস্টারিং | `task: clustering | query: {content}` |
| শব্দের অর্থগত মিল | `task: sentence similarity | query: {content}` সার্চ বা রিট্রিভ করার জন্য এটি ব্যবহার করবেন না। এটি টেক্সটের অর্থগত মিলের জন্য তৈরি করা হয়েছে। |

**ব্যবহারের উদাহরণ**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

টাস্কটি যেন ধারাবাহিকভাবে ব্যবহার করা হয়, তা দেখা গুরুত্বপূর্ণ। যেমন, ডকুমেন্ট `f'task: classification | query: {content}'`-এর সাথে
এম্বেড করা থাকলে, কোয়েরিকেও
এই টাস্ক ফর্ম্যাট মেনে এম্বেড করতে হবে।

### এম্বেডিং ১ সহ টাস্কের ধরন

`gemini-embedding-001`-এর জন্য, আপনি `embedContent`
পদ্ধতিতে `task_type` নির্দিষ্ট করতে পারবেন। কাজ করে এমন টাস্কের ধরনের সম্পূর্ণ তালিকা দেখতে, [কাজ করে এমন টাস্কের ধরন](#supported-task-types)
টেবিল দেখুন।

নিম্নলিখিত উদাহরণ থেকে আপনি বুঝতে পারবেন যে কীভাবে `SEMANTIC_SIMILARITY` ব্যবহার করে
দুটি টেক্সট স্ট্রিংয়ের অর্থ কতটা কাছাকাছি তা চেক করা যায়।

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

কোড স্নিপেট থেকে বোঝা যাবে যে রান করার সময় টেক্সটের বিভিন্ন অংশ একে
অপরের সাথে কতটা মিলছে।

#### যে ধরনের টাস্ক কাজ করে

`gemini-embedding-001`-এর জন্য কাজ করে এমন টাস্কের ধরন:

| টাস্কের ধরন | বিবরণ | উদাহরণ |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | টেক্সটের মিল মূল্যায়ন করার জন্য অপ্টিমাইজ করা এম্বেডিং। | সাজেশন সিস্টেম, ডুপ্লিকেট কন্টেন্ট শনাক্তকরণ |
| **শ্রেণীবিভাগ** | পূর্বনির্ধারিত লেবেল অনুযায়ী টেক্সটকে শ্রেণীবদ্ধ করার জন্য অপ্টিমাইজ করা এম্বেডিং। | সেন্টিমেন্ট বিশ্লেষণ, স্প্যাম শনাক্তকরণ |
| **ক্লাস্টারিং** | টেক্সটের মিলের উপর ভিত্তি করে সেগুলিকে ক্লাস্টার করার জন্য অপ্টিমাইজ করা এম্বেডিং। | ডকুমেন্ট সাজানো, মার্কেট রিসার্চ, অসঙ্গতি শনাক্তকরণ |
| **RETRIEVAL\_DOCUMENT** | ডকুমেন্ট সার্চের জন্য অপ্টিমাইজ করা এম্বেডিং। | সার্চের জন্য নিবন্ধ, বই বা ওয়েবপেজ ইনডেক্স করা। |
| **RETRIEVAL\_QUERY** | সাধারণ সার্চ কোয়েরির জন্য অপ্টিমাইজ করা এম্বেডিং। কোয়েরির জন্য `RETRIEVAL_QUERY` ব্যবহার করুন; `RETRIEVAL_DOCUMENT` হল সেইসব ডকুমেন্ট যা খুঁজে বের করতে হবে। | কাস্টম সার্চ |
| **CODE\_RETRIEVAL\_QUERY** | ন্যাচারাল ল্যাঙ্গুয়েজ কোয়েরির উপর ভিত্তি করে কোড ব্লক রিট্রিভ করার জন্য অপ্টিমাইজ করা এম্বেডিং। কোয়েরির জন্য `CODE_RETRIEVAL_QUERY` ব্যবহার করুন; কোড ব্লক রিট্রিভ করার জন্য `RETRIEVAL_DOCUMENT` ব্যবহার করুন। | কোড সাজেশন ও সার্চ |
| **QUESTION\_ANSWERING** | প্রশ্ন-উত্তর সিস্টেমে প্রশ্নের জন্য এম্বেডিং, প্রশ্নের উত্তর দেয় এমন ডকুমেন্ট খুঁজে পাওয়ার জন্য অপ্টিমাইজ করা হয়। প্রশ্নের জন্য `QUESTION_ANSWERING` ব্যবহার করুন; `RETRIEVAL_DOCUMENT` হল সেইসব ডকুমেন্ট যা খুঁজে বের করতে হবে। | চ্যাটবক্স |
| **FACT\_VERIFICATION** | যাচাই করতে হবে এমন বিবৃতির জন্য এম্বেডিং, বিবৃতি সমর্থন বা খণ্ডন করে এমন প্রমাণ থাকা ডকুমেন্ট রিট্রিভ করার জন্য অপ্টিমাইজ করা। টার্গেট টেক্সটের জন্য `FACT_VERIFICATION` ব্যবহার করুন; যে ডকুমেন্ট পুনরুদ্ধার করতে হবে তার জন্য `RETRIEVAL_DOCUMENT` ব্যবহার করুন | অটোমেটেড তথ্য যাচাইকরণ সিস্টেম |

## এম্বেডিংয়ের সাইজ কন্ট্রোল করা

`gemini-embedding-001` ও `gemini-embedding-2`, দুটি মডেলকেই
Matryoshka Representation Learning (MRL) টেকনিক ব্যবহার করে ট্রেনিং দেওয়া হয়। এটি কোনও মডেলকে
এমন হাই-ডাইমেনশনাল এম্বেডিং শিখতে সাহায্য করে যেগুলির প্রাথমিক সেগমেন্ট (বা প্রিফিক্স) থাকে যা
একই ডেটার আরও উপযোগী, সহজ ভার্সন।

আউটপুট এম্বেডিং ভেক্টরের
সাইজ কন্ট্রোল করতে `output_dimensionality` প্যারামিটার ব্যবহার করুন। ছোট আউটপুট ডাইমেনশনালিটি বেছে নিলে স্টোরেজ স্পেস বাঁচানো যায় এবং ডাউনস্ট্রিম অ্যাপ্লিকেশনের জন্য কম্পিউটেশনাল এফিসিয়েন্সি বাড়ানো যায়,
তবে কোয়ালিটির দিক থেকে সামান্য ক্ষতি হয়। ডিফল্ট হিসেবে, দুটি মডেলই ৩০৭২-ডাইমেনশনাল এম্বেডিং আউটপুট দেয়, কিন্তু স্টোরেজ স্পেস বাঁচাতে আপনি কোয়ালিটি
নষ্ট না করেই এটিকে ছোট সাইজে ট্রাঙ্কেট করতে পারেন।
আমরা ৭৬৮, ১৫৩৬ বা ৩০৭২
আউটপুট ডাইমেনশন ব্যবহার করার সাজেশন দিই।

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

কোড স্নিপেট থেকে পাওয়া আউটপুটের উদাহরণ:

```
Length of embedding: 768
```

## ছোট আকারের ক্ষেত্রে কোয়ালিটি নিশ্চিত করা

ডিফল্ট ৩০৭২-ডাইমেনশন এম্বেডিং সবসময়ই স্বাভাবিক করা হয়, তবে Gemini
Embedding 2-ও ছোট করে দেওয়া ডাইমেনশন (যেমন, ৭৬৮, ১৫৩৬) অটোমেটিক স্বাভাবিক করে দেয়। এটি
নিশ্চিত করে যে ভেক্টর ডিরেকশনের মাধ্যমে সেম্যান্টিক মিল গণনা করা হয়, ম্যাগনিটিউডের
মাধ্যমে নয়, যা বক্সের বাইরে আরও সঠিক ফলাফল প্রদান করে।

**পুরনো মডেল**: আপনি `gemini-embedding-001` ব্যবহার করলে, আপনাকে অবশ্যই ম্যানুয়ালি
নিচের মতো করে ৩০৭২ নয় এমন ডাইমেনশনকে স্বাভাবিক করতে হবে:

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

এই কোড স্নিপেট থেকে পাওয়া আউটপুটের উদাহরণ:

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

নিচের টেবিলে MTEB স্কোর দেখানো হয়েছে, এটি হল এম্বেডিংয়ের জন্য সাধারণত ব্যবহৃত
বেঞ্চমার্ক, যা বিভিন্ন ডাইমেনশনের জন্য ব্যবহার করা হয়। বিশেষত, ফলাফল থেকে দেখা যায় যে পারফর্ম্যান্স
এমবেডিং ডাইমেনশনের সাইজের সাথে কঠোরভাবে যুক্ত নয়, কারণ কম
ডাইমেনশনগুলি তাদের বেশি ডাইমেনশন সহ সমকক্ষদের সাথে তুলনীয় স্কোর অর্জন করে।

| MRL ডাইমেনশন | MTEB স্কোর (Gemini Embedding 001) |
| --- | --- |
| 2048 | ৬৮.১৬ |
| 1536 | 68.17 |
| 768 | ৬৭.৯৯ |
| 512 | ৬৭.৫৫ |
| 256 | ৬৬.১৯ |
| 128 | ৬৩.৩১ |

## মাল্টিমোডাল এম্বেডিং

`gemini-embedding-2` মডেল মাল্টিমোডাল ইনপুট সাপোর্ট করে, এর ফলে আপনি
টেক্সটের সাথে ছবি, ভিডিও, অডিও ও ডকুমেন্ট কন্টেন্ট এম্বেড করতে পারবেন। সব মোডালিটি
একই এম্বেডিং স্পেসে ম্যাপ করা হয়, এর ফলে ক্রস-মোডাল সার্চ ও
তুলনা করা যায়।

### কাজ করে এমন মোডালিটি ও সীমা

ইনপুট টোকেনের সামগ্রিক সর্বাধিক সীমা হল ৮১৯২টি টোকেন।

| মোডালিটি | স্পেসিফিকেশন ও সীমা |
| --- | --- |
| **Text** | ৮,১৯২টি টোকেন পর্যন্ত কাজ করে। |
| **ছবি** | প্রতিটি অনুরোধে সর্বাধিক ৬টি ছবি। যেসব ফর্ম্যাট কাজ করে: PNG, JPEG. |
| **অডিও** | সর্বাধিক সময়সীমা ১৮০ সেকেন্ড। কাজ করে এমন ফর্ম্যাট: MP3, WAV. |
| **ভিডিও** | সর্বাধিক সময়সীমা ১২০ সেকেন্ড। কাজ করে এমন ফর্ম্যাট: MP4, MOV. কাজ করে এমন কোডেক: H264, H265, AV1, VP9.  সিস্টেম প্রতিটি ভিডিওতে সর্বাধিক ৩২টি ফ্রেম প্রসেস করে: ছোট ভিডিও (≤৩২ সেকেন্ড) ১ fps-এ স্যাম্পেল করা হয়, যেখানে বড় ভিডিওগুলি ৩২টি ফ্রেমে সমানভাবে স্যাম্পেল করা হয়। ভিডিও ফাইলে অডিও ট্র্যাক প্রসেস করা হয় না। |
| **ডকুমেন্ট (PDF)** | প্রতিটি অনুরোধে সর্বাধিক ১টি ফাইল, ৬টি পৃষ্ঠা পর্যন্ত। |

### ছবি এম্বেড করা

নিচের উদাহরণে দেখানো হয়েছে কীভাবে
`gemini-embedding-2` ব্যবহার করে ছবি এম্বেড করতে হয়।

[Files API](https://ai.google.dev/gemini-api/docs/files?hl=bn)-এর মাধ্যমে ইনলাইন ডেটা হিসেবে অথবা আপলোড করা ফাইল হিসেবে ছবি প্রদান করা যেতে পারে।

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

### জাভাস্ক্রিপ্ট

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

### এম্বেডিং এগ্রিগেশন

মাল্টিমোডাল কন্টেন্ট নিয়ে কাজ করার সময়, আপনার ইনপুট স্ট্রাকচার করার পদ্ধতি এম্বেডিং আউটপুটকে
প্রভাবিত করে:

- **একাধিক পার্ট (অ্যাগ্রিগেট করা):**
  `contents` প্যারামিটারে সরাসরি একাধিক ইনপুট যোগ করলে, সব ইনপুটের জন্য একটি অ্যাগ্রিগেট করা এম্বেডিং তৈরি হয়।
- **একাধিক `Content` অবজেক্ট (আলাদা):** প্রতিটি ইনপুটকে একটি
  `Content` অবজেক্টে র‍্যাপ করে `contents` প্যারামিটারে পাস করলে
  প্রতিটি এন্ট্রির জন্য আলাদা এম্বেডিং রিটার্ন করে।
- **পোস্ট-লেভেল উপস্থাপনা:** একাধিক মিডিয়া আইটেম সহ সোশ্যাল মিডিয়া পোস্টের
  মতো জটিল অবজেক্টের ক্ষেত্রে, আমরা একটি সুসংহত পোস্ট-লেভেল উপস্থাপনা তৈরি করতে আলাদা আলাদা এম্বেডিংকে
  একত্রিত করার (যেমন, গড় মান বের করার মাধ্যমে) পরামর্শ দিই।

টেক্সট ও
ইমেজ ইনপুটের জন্য কীভাবে একটি অ্যাগ্রিগেট করা এম্বেডিং তৈরি করতে হয় তা নিম্নলিখিত উদাহরণে দেখানো হয়েছে। `contents` প্যারামিটারে একাধিক ইনপুট যোগ করুন:

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

### জাভাস্ক্রিপ্ট

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

অন্যদিকে, আপনি যদি `contents` প্যারামিটারের মধ্যে `Content` অবজেক্ট ব্যবহার করেন,
তাহলে এটি আলাদা আলাদা এম্বেডিং রিটার্ন করে। এই উদাহরণে একটি এম্বেডিং কলে একাধিক এম্বেডিং
তৈরি করা হয়েছে:

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

### জাভাস্ক্রিপ্ট

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

### অডিও এম্বেড করা

নিচের উদাহরণে
`gemini-embedding-2` ব্যবহার করে কীভাবে অডিও ফাইল এম্বেড করতে হয় তা দেখানো হয়েছে।

[Files API](https://ai.google.dev/gemini-api/docs/files?hl=bn)-এর মাধ্যমে অডিও ফাইল ইনলাইন ডেটা হিসেবে অথবা আপলোড করা ফাইল হিসেবে
প্রদান করা যেতে পারে।

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

### জাভাস্ক্রিপ্ট

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

### ভিডিও এম্বেড করা

নিচের উদাহরণে দেখানো হয়েছে যে কীভাবে
`gemini-embedding-2` ব্যবহার করে ভিডিও এম্বেড করতে হয়।

ভিডিও ইনলাইন ডেটা হিসেবে বা [Files API](https://ai.google.dev/gemini-api/docs/files?hl=bn)-এর মাধ্যমে আপলোড করা ফাইল হিসেবে
প্রদান করা যেতে পারে।

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

### জাভাস্ক্রিপ্ট

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

১২০ সেকেন্ডের বেশি দৈর্ঘ্যের ভিডিও এম্বেড করতে চাইলে, ভিডিওটিকে
ওভারল্যাপ করা সেগমেন্টে ভাগ করে প্রতিটি সেগমেন্ট আলাদা আলাদা করে এম্বেড করতে পারেন।

### ডকুমেন্ট এম্বেড করা

পিডিএফ ফর্ম্যাটের ডকুমেন্ট সরাসরি এম্বেড করা যায়। মডেলটি প্রতিটি পৃষ্ঠার ভিজ্যুয়াল ও টেক্সট
কন্টেন্ট প্রসেস করে।

PDF-কে ইনলাইন ডেটা হিসেবে বা [Files API](https://ai.google.dev/gemini-api/docs/files?hl=bn)-এর মাধ্যমে আপলোড করা ফাইল হিসেবে
প্রদান করা যেতে পারে।

#### মডেল কীভাবে পিডিএফ প্রসেস করে

আপনি কোনও PDF এম্বেড করলে, মডেলটি ভিজ্যুয়াল ও টেক্সট ফিচার, দুটিই ব্যবহার করে ডকুমেন্ট প্রসেস করে:

- **ভিজ্যুয়াল উপস্থাপনা:** মডেল প্রতিটি পৃষ্ঠা একটি ছবি হিসেবে রেন্ডার করে, যার ফলে প্রতি পৃষ্ঠায় **২৫৮টি টোকেন** খরচ হয়।
- **টেক্সট এক্সট্র্যাকশন:** মডেলটি ডকুমেন্ট থেকে টেক্সট এক্সট্র্যাক্ট করে। **নেটিভ পিডিএফ** (যেগুলিতে ডিজিটাল টেক্সট থাকে) থেকে মডেল সরাসরি টেক্সট এক্সট্র্যাক্ট করে। **স্ক্যান করা পিডিএফের** (যেগুলিতে টেক্সটের ছবি থাকে) ক্ষেত্রে, টেক্সট এক্সট্র্যাক্ট করার জন্য মডেল অটোমেটিক অপটিক্যাল অক্ষর স্বীকৃতি (OCR) চালায়।

কোনও পিডিএফের মোট টোকেন সংখ্যা গণনা করতে, টেক্সট টোকেনের সাথে ভিজ্যুয়াল টোকেন (প্রতি পৃষ্ঠায় ২৫৮) যোগ করুন। আপনার ইনপুটকে মডেলের **৮,১৯২ টোকেন সীমার** (সব মোডালিটি জুড়ে শেয়ার করা) মধ্যে থাকতে হবে। এই সীমা অতিক্রম করলে সিস্টেম কোনও বিজ্ঞপ্তি না দিয়েই ইনপুট কেটে দেয়।

#### PDF সংক্রান্ত সীমা

- **প্রতিটি অনুরোধে ফাইল:** আপনি সর্বাধিক ১টি পিডিএফ ফাইল জমা দিতে পারবেন।
- **পৃষ্ঠার সীমা:** আপনি প্রতি ফাইলে সর্বাধিক ৬টি পৃষ্ঠা জমা দিতে পারবেন। সবচেয়ে ভাল কোয়ালিটির জন্য, আমরা প্রতিটি PDF-এর জন্য ১টি করে পৃষ্ঠা ব্যবহার করার সাজেশন দিই।

`gemini-embedding-2` ব্যবহার করে কীভাবে পিডিএফ এম্বেড করতে হয় তা নিম্নলিখিত উদাহরণ থেকে দেখুন:

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

### জাভাস্ক্রিপ্ট

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

## যেসব ক্ষেত্রে ব্যবহার করা যাবে

টেক্সট এম্বেডিং বিভিন্ন ধরনের সাধারণ AI ব্যবহারের ক্ষেত্রে অত্যন্ত গুরুত্বপূর্ণ, যেমন:

- **রিট্রিভাল-অগমেন্টেড জেনারেশন (RAG):** কোনও মডেলের কনটেক্সটে প্রাসঙ্গিক তথ্য
  রিট্রিভ ও ইনকর্পোরেট করার মাধ্যমে এম্বেডিং, জেনারেটেড টেক্সটের কোয়ালিটি
  উন্নত করে।
- **তথ্য রিট্রিভ করা:** ইনপুট টেক্সটের একটি অংশ দেওয়া হলে, সবচেয়ে বেশি শব্দার্থগতভাবে একই রকম টেক্সট বা
  ডকুমেন্ট সার্চ করা।

  [ডকুমেন্ট সার্চ টিউটোরিয়ালtask](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **সার্চ আবার র‍্যাঙ্ক করা**: কোয়েরির সাথে প্রাথমিক ফলাফলের শব্দার্থগত
  স্কোর তুলনা করে সবচেয়ে প্রাসঙ্গিক আইটেমকে অগ্রাধিকার দিন।

  [সার্চ রির‍্যাঙ্কিং টিউটোরিয়ালtask](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **অসঙ্গতি শনাক্তকরণ:** এম্বেডিংয়ের গ্রুপ তুলনা করলে লুকানো ট্রেন্ড বা আউটলায়ার
  শনাক্ত করতে সাহায্য পাওয়া যায়।

  [অসঙ্গতি শনাক্তকরণ টিউটোরিয়ালbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **শ্রেণীবিভাগ:** কন্টেন্টের উপর ভিত্তি করে টেক্সটকে অটোমেটিক ক্যাটেগরাইজ করা, যেমন
  সেন্টিমেন্ট বিশ্লেষণ বা স্প্যাম শনাক্তকরণ

  [শ্রেণীবিভাগ টিউটোরিয়ালtoken](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **ক্লাস্টারিং:** আপনার এম্বেডিংয়ের ক্লাস্টার
  ও ভিজ্যুয়ালাইজেশন তৈরি করে জটিল সম্পর্ককে কার্যকরভাবে বুঝুন।

  [ক্লাস্টারিং ভিজ্যুয়ালাইজেশন টিউটোরিয়ালbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## এম্বেডিং স্টোর করা

প্রোডাকশনে এম্বেডিং ব্যবহার করার সময়, হাই-ডাইমেনশনাল এম্বেডিং
দক্ষতার সাথে স্টোর, ইন্ডেক্স ও রিট্রিভ করতে **ভেক্টর ডেটাবেস** ব্যবহার করা
সাধারণ ব্যাপার। Google Cloud ম্যানেজ করা ডেটা পরিষেবা প্রদান করে যা
এই উদ্দেশ্যে ব্যবহার করা যেতে পারে, এর মধ্যে
[Gemini Enterprise Agent Platform Vector Search 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/overview?hl=bn),
[BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=bn), [AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=bn) এবং
[Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=bn) অন্তর্ভুক্ত।

Gemini Embedding-এর সাথে কীভাবে অন্যান্য থার্ড-পার্টি ভেক্টর ডেটাবেস
ব্যবহার করতে হয় তা নিম্নলিখিত টিউটোরিয়াল থেকে জানুন।

- [ChromaDB টিউটোরিয়ালbolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [QDrant টিউটোরিয়ালbolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [Weaviate টিউটোরিয়ালbolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [Pinecone টিউটোরিয়ালbolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## মডেলের ভার্সন

### Gemini Embedding 2

| প্রপার্টি | বিবরণ |
| --- | --- |
| id\_cardমডেল কোড | **Gemini API**  `gemini-embedding-2` |
| সেভ করাডেটার ধরন | **ইনপুট**  টেক্সট, ছবি, ভিডিও, অডিও, পিডিএফ  **আউটপুট**  টেক্সট এম্বেডিং |
| token\_autoটোকেন সীমা[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=bn) | **ইনপুট টোকেনের সীমা**  ৮,১৯২  **আউটপুট ডাইমেনশনের সাইজ**  ফ্লেক্সিবল, এগুলির সাথে কাজ করে: ১২৮ - ৩০৭২, সাজেস্ট করা: ৭৬৮, ১৫৩৬, ৩০৭২ |
| 123ভার্সন | আরও বিবরণের জন্য [মডেল ভার্সন প্যাটার্ন](https://ai.google.dev/gemini-api/docs/models/gemini?hl=bn#model-versions) পড়ুন।  - স্থিতিশীল: `gemini-embedding-2` |
| calendar\_monthলেটেস্ট আপডেট | এপ্রিল ২০২৬ |

### Gemini Embedding

| প্রপার্টি | বিবরণ |
| --- | --- |
| id\_cardমডেল কোড | **Gemini API**  `gemini-embedding-001` |
| সেভ করাডেটার ধরন | **ইনপুট**  টেক্সট  **আউটপুট**  টেক্সট এম্বেডিং |
| token\_autoটোকেন সীমা[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=bn) | **ইনপুট টোকেনের সীমা**  ২,০৪৮  **আউটপুট ডাইমেনশনের সাইজ**  ফ্লেক্সিবল, এগুলির সাথে কাজ করে: ১২৮ - ৩০৭২, সাজেস্ট করা: ৭৬৮, ১৫৩৬, ৩০৭২ |
| 123ভার্সন | আরও বিবরণের জন্য [মডেল ভার্সন প্যাটার্ন](https://ai.google.dev/gemini-api/docs/models/gemini?hl=bn#model-versions) পড়ুন।  - স্থিতিশীল: `gemini-embedding-001` |
| calendar\_monthলেটেস্ট আপডেট | জুন ২০২৫ |

বন্ধ হয়ে যাওয়া এম্বেডিং মডেলের জন্য, এই
[বন্ধ হয়ে যাওয়া](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn) পৃষ্ঠা দেখুন

## gemini-embedding-001 থেকে মাইগ্রেশন

`gemini-embedding-001` ও
`gemini-embedding-2`-এর মধ্যে এম্বেডিং স্পেস **অসঙ্গত**। এর অর্থ হল, আপনি একটি মডেলের জেনারেট করা এম্বেডিংয়ের সাথে অন্য মডেলের
জেনারেট করা এম্বেডিং সরাসরি তুলনা করতে পারবেন না।
আপনি `gemini-embedding-2`-এ আপগ্রেড করলে, আপনাকে অবশ্যই
আগে থেকে থাকা সব ডেটা আবার এম্বেড করতে হবে।

অসামঞ্জস্যতা ছাড়াও, দুটি মডেলের মধ্যে আরও বেশ কিছু উল্লেখযোগ্য পার্থক্য রয়েছে:

- **টাস্কের ধরন সংক্রান্ত স্পেসিফিকেশন:** `gemini-embedding-001`-এর মাধ্যমে, আপনি `task_type` প্যারামিটার (যেমন, `SEMANTIC_SIMILARITY`,
  `RETRIEVAL_DOCUMENT`) ব্যবহার করে টাস্কের
  ধরন নির্দিষ্ট করেন। `gemini-embedding-2`-এর মাধ্যমে, `task_type`
  প্যারামিটার কাজ করে না। এর পরিবর্তে, আপনাকে শুধু টেক্সট-ভিত্তিক টাস্কের জন্য
  সরাসরি প্রম্পটে টাস্কের নির্দেশাবলী যোগ করতে হবে। বিভিন্ন ব্যবহারের ক্ষেত্রে কীভাবে
  প্রম্পট ফর্ম্যাট করতে হয় সেই বিষয়ে বিস্তারিত জানতে,
  [এম্বেডিং ২ সহ টাস্কের ধরন](#task-types-embeddings-2) দেখুন।
- **এম্বেডিং এগ্রিগেশন:** `gemini-embedding-001` ইনপুটের তালিকায় থাকা প্রতিটি স্ট্রিংয়ের জন্য
  আলাদা এম্বেডিং জেনারেট করে। অন্যদিকে,
  `gemini-embedding-2` একাধিক ইনপুট (যেমন, টেক্সট ও ছবি) সরাসরি একটি অনুরোধে দেওয়া হলে,
  একটিই অ্যাগ্রিগেট করা এম্বেডিং তৈরি করে। আলাদা আলাদা ইনপুটের জন্য আলাদা আলাদা এম্বেডিং জেনারেট করতে, প্রতিটি ইনপুটকে
  `Content` অবজেক্টে র‍্যাপ করুন অথবা
  [ব্যাচ API](https://ai.google.dev/gemini-api/docs/batch-api?hl=bn#batch-embedding) ব্যবহার করুন। আরও তথ্যের জন্য
  [এম্বেডিং অ্যাগ্রিগেশন](#embedding-aggregation) দেখুন।
- **নর্মালাইজেশন:** আপনি যদি `output_dimensionality` ব্যবহার করে ৩০৭২-এর কম ডাইমেনশন সহ এম্বেডিংয়ের
  অনুরোধ করেন, তাহলে `gemini-embedding-2` অটোমেটিক
  এইসব সংক্ষিপ্ত এম্বেডিংকে নর্মালাইজ করে। `gemini-embedding-001`-এর সাহায্যে, আপনাকে
  ৩০৭২ ছাড়া অন্যান্য ডাইমেনশনের জন্য ম্যানুয়াল নরমালাইজেশন করতে হবে। বিবরণের জন্য
  [ছোট আকারের ক্ষেত্রে কোয়ালিটি নিশ্চিত করা](#quality-for-smaller-dimensions)
  দেখুন।

## ব্যাচ এম্বেডিং

লেটেন্সি নিয়ে কোনও সমস্যা না থাকলে, Gemini Embeddings মডেলের সাথে
[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=bn#batch-embedding) ব্যবহার করে দেখুন। এর ফলে
ডিফল্ট এম্বেডিং দামের ৫০% খরচে অনেক বেশি থ্রুপুট পাওয়া যায়।
কীভাবে শুরু করতে হয় তার উদাহরণ
[ব্যাচ API কুকবুকে](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb) দেখুন।

## দায়িত্ব সহকারে ব্যবহার সংক্রান্ত বিজ্ঞপ্তি

নতুন কন্টেন্ট তৈরি করা জেনারেটিভ AI মডেলের বিপরীতে, Gemini Embedding মডেল
শুধুমাত্র আপনার ইনপুট ডেটার ফর্ম্যাটকে সংখ্যাগত
প্রতিনিধিত্বে পরিবর্তন করার উদ্দেশ্যে তৈরি করা হয়েছে। Google একটি এম্বেডিং মডেল প্রদান করার জন্য দায়ী
যা আপনার ইনপুট ডেটার ফর্ম্যাটকে অনুরোধ করা সংখ্যাসূচক-ফর্ম্যাটে রূপান্তরিত করে,
ব্যবহারকারীরা তাদের ইনপুট করা ডেটা এবং এর ফলে প্রাপ্ত
এম্বেডিংয়ের জন্য সম্পূর্ণ দায়বদ্ধ থাকে। Gemini Embedding মডেল ব্যবহার করার মাধ্যমে, আপনি কনফার্ম করছেন যে আপলোড করা যেকোনও কন্টেন্টে আপনার
প্রয়োজনীয় অধিকার রয়েছে। এমন কন্টেন্ট তৈরি করবেন না যা
অন্যদের মেধা সম্পত্তি বা গোপনীয়তা অধিকার লঙ্ঘন করে। এই
পরিষেবা ব্যবহারের ক্ষেত্রে আমাদের [নিষিদ্ধ ব্যবহার
সংক্রান্ত নীতি](https://policies.google.com/terms/generative-ai/use-policy?hl=bn) এবং
[Google-এর পরিষেবার শর্তাবলী](https://ai.google.dev/gemini-api/terms?hl=bn) প্রযোজ্য।

## এম্বেডিং ব্যবহার করে তৈরি করা শুরু করুন

মডেলের ক্ষমতা এক্সপ্লোর করতে এবং কীভাবে আপনার
এম্বেডিং কাস্টমাইজ ও ভিজ্যুয়ালাইজ করতে হয় তা জানতে [এম্বেডিং কুইকস্টার্ট
নোটবুক](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb)
দেখুন।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-09 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-09 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
