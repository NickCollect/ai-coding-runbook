---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=he
fetched_at: 2026-05-11T05:01:36.165519+00:00
title: "\u05d4\u05d8\u05de\u05e2\u05d5\u05ea \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# הטמעות

‫Gemini API מציע מודלים להטמעה כדי ליצור הטמעות לטקסט, לתמונות, לסרטונים ולתוכן אחר. אפשר להשתמש בהטמעות שמתקבלות למשימות כמו חיפוש סמנטי, סיווג ואשכול, כדי לקבל תוצאות מדויקות יותר שמתחשבות בהקשר, בהשוואה לגישות שמבוססות על מילות מפתח.

המודל העדכני ביותר, `gemini-embedding-2`, הוא מודל ההטמעה המולטי-מודאלי הראשון ב-Gemini API. הוא ממפה טקסט, תמונות, סרטונים, אודיו ומסמכים למרחב הטמעה מאוחד, ומאפשר חיפוש, סיווג וקיבוץ חוצי-אופנים ביותר מ-100 שפות. מידע נוסף זמין [בקטע בנושא הטמעות מולטימודאליות](#multimodal). לתרחישי שימוש שמבוססים על טקסט בלבד, `gemini-embedding-001` עדיין זמין.

יצירת מערכות Retrieval Augmented Generation (יצירה משולבת-אחזור, RAG) היא תרחיש שימוש נפוץ במוצרי AI. הטמעות ממלאות תפקיד מרכזי בשיפור משמעותי של התפוקות של המודל, עם דיוק עובדתי משופר, קוהרנטיות ועושר הקשרי. אם אתם מעדיפים להשתמש בפתרון RAG מנוהל, יצרנו את הכלי [חיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he), שמקל על ניהול RAG ומוזיל את העלויות.

## יצירת הטמעות

משתמשים ב-method‏ `embedContent` כדי ליצור הטמעות טקסט:

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

## ציון סוג המשימה לשיפור הביצועים

אפשר להשתמש בהטמעות למגוון רחב של משימות, מסיווג ועד לחיפוש מסמכים. ציון סוג המשימה הנכון עוזר לבצע אופטימיזציה של ההטמעות כדי להשיג את הקשרים הרצויים, וכך למקסם את הדיוק והיעילות.

### סוגי משימות עם Embeddings 2

במשימות שמבוססות על טקסט בלבד עם `gemini-embedding-2`, מומלץ מאוד להוסיף את הוראות המשימה בהנחיה. כדי לעשות את זה, צריך לעצב את השאילתה ואת המסמך עם קידומת המשימה הנכונה.

בטבלאות הבאות מוצגות דוגמאות לפורמט של שאילתות ומסמכים לתרחישי שימוש סימטריים ואסימטריים באמצעות מודל `gemini-embedding-2`.

**תרחישים לדוגמה לאחזור (פורמט אסימטרי)**

בתרחישי שימוש אסימטריים, מוסיפים את קידומת המשימה לשאילתה ומחילים את מבנה המסמך על התוכן שרוצים להטמיע ולאחזר.

| תרחיש שימוש | מבנה השאילתה | מבנה המסמך |
| --- | --- | --- |
| שאילתת חיפוש | `task: search result | query: {content}` | `title: {title} | text: {content}` אם אין כותרת, משתמשים בערך `title: none`. |
| מענה לשאלות | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| בדיקת עובדות | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| אחזור קוד | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**דוגמה לשימוש**

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

**תרחישי שימוש עם קלט יחיד (פורמט סימטרי)**

בתרחישי שימוש סימטריים, כשמבצעים את אותה משימה, צריך להשתמש באותו פורמט לשאילתה ולמסמך.

| תרחיש שימוש | מבנה הקלט |
| --- | --- |
| סיווג | `task: classification | query: {content}` |
| סידור באשכול | `task: clustering | query: {content}` |
| דמיון סמנטי | `task: sentence similarity | query: {content}` אין להשתמש בזה לחיפוש או לאחזור. הוא מיועד לדמיון סמנטי בין טקסטים. |

**דוגמה לשימוש**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

חשוב להשתמש במשימה באופן עקבי. לדוגמה, אם מסמכים מוטמעים באמצעות `f'task: classification | query: {content}'`, השאילתה צריכה להיות מוטמעת גם היא לפי פורמט המשימה הזה.

### סוגי משימות עם הטמעות 1

במקרה של `gemini-embedding-001`, אפשר לציין את `task_type` בשיטה `embedContent`. רשימה מלאה של סוגי המשימות הנתמכים זמינה בטבלה [סוגי המשימות הנתמכים](#supported-task-types).

בדוגמה הבאה אפשר לראות איך משתמשים ב-`SEMANTIC_SIMILARITY` כדי לבדוק עד כמה מחרוזות טקסט דומות מבחינת המשמעות.

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

קטעי הקוד יראו עד כמה חלקי הטקסט השונים דומים זה לזה כשהם יופעלו.

#### סוגי המשימות הנתמכים

סוגי המשימות הנתמכים ב-`gemini-embedding-001`:

| סוג המשימה | תיאור | דוגמאות |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | הטמעות שעברו אופטימיזציה להערכת הדמיון בין טקסטים. | מערכות המלצות, זיהוי כפילויות |
| **CLASSIFICATION** | הטמעה שעברה אופטימיזציה לסיווג טקסטים לפי תוויות מוגדרות מראש. | ניתוח סנטימנטים, זיהוי ספאם |
| **CLUSTERING** | הטמעה שעברה אופטימיזציה כדי לאגד טקסטים על סמך הדמיון ביניהם. | ארגון מסמכים, מחקר שוק, זיהוי אנומליות |
| **RETRIEVAL\_DOCUMENT** | הטמעות שעברו אופטימיזציה לחיפוש מסמכים. | יצירת אינדקס של מאמרים, ספרים או דפי אינטרנט לחיפוש. |
| **RETRIEVAL\_QUERY** | הטמעות שעברו אופטימיזציה לשאילתות חיפוש כלליות. משתמשים ב-`RETRIEVAL_QUERY` לשאילתות וב-`RETRIEVAL_DOCUMENT` למסמכים לאחזור. | חיפוש בהתאמה אישית |
| **CODE\_RETRIEVAL\_QUERY** | הטמעות שעברו אופטימיזציה לאחזור של בלוקים של קוד על סמך שאילתות בשפה טבעית. משתמשים ב-`CODE_RETRIEVAL_QUERY` לחיפושים וב-`RETRIEVAL_DOCUMENT` לבלוקים של קוד שאותם רוצים לאחזר. | הצעות קוד וחיפוש |
| **QUESTION\_ANSWERING** | הטמעות לשאלות במערכת למתן תשובות לשאלות, שעברו אופטימיזציה למציאת מסמכים שכוללים תשובה לשאלה. משתמשים ב-`QUESTION_ANSWERING` לשאלות וב-`RETRIEVAL_DOCUMENT` למסמכים שרוצים לאחזר. | תיבת צ'אט |
| **FACT\_VERIFICATION** | הטמעה של הצהרות שצריך לאמת, עם אופטימיזציה לאחזור מסמכים שמכילים הוכחות שתומכות בהצהרה או מפריכות אותה. משתמשים ב-`FACT_VERIFICATION` לטקסט היעד וב-`RETRIEVAL_DOCUMENT` למסמכים שאותם רוצים לאחזר | מערכות אוטומטיות לבדיקת עובדות |

## שליטה בגודל ההטמעה

המודלים `gemini-embedding-001` ו-`gemini-embedding-2` מאומנים באמצעות טכניקת Matryoshka Representation Learning ‏ (MRL), שמלמדת מודל ללמוד הטמעות רב-ממדיות עם פלחים ראשוניים (או קידומות) שגם הם שימושיים, וגרסאות פשוטות יותר של אותם נתונים.

משתמשים בפרמטר `output_dimensionality` כדי לשלוט בגודל של וקטור ההטמעה של הפלט. בחירה של ממד פלט קטן יותר יכולה לחסוך מקום באחסון ולשפר את יעילות החישוב עבור אפליקציות במורד הזרם, בלי לפגוע באיכות. כברירת מחדל, שני המודלים יוצרים הטמעה תלת-ממדית בגודל 3,072, אבל אפשר לקצץ אותה לגודל קטן יותר בלי לפגוע באיכות כדי לחסוך במקום באחסון. מומלץ להשתמש בממדי פלט של 768,‏ 1,536 או 3,072.

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

פלט לדוגמה מקטע הקוד:

```
Length of embedding: 768
```

## שמירה על האיכות במאפיינים קטנים יותר

בעוד שהטמעות של 3,072 מימדים שמוגדרות כברירת מחדל תמיד עוברות נורמליזציה, גם הטמעות של Gemini Embedding 2 עם מימדים קטומים (למשל, 768,‏ 1,536) עוברות נורמליזציה אוטומטית. כך מובטח שדמיון סמנטי יחושב באמצעות כיוון וקטורי ולא באמצעות גודל, ויתקבלו תוצאות מדויקות יותר מראש.

**מודלים ישנים יותר**: אם אתם משתמשים ב-`gemini-embedding-001`, אתם צריכים לבצע נורמליזציה ידנית של מימדים שאינם 3072 באופן הבא:

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

פלט לדוגמה מקטע הקוד הזה:

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

בטבלה הבאה מוצגים ציוני MTEB, מדד נפוץ להשוואה בין הטמעות, עבור ממדים שונים. חשוב לציין שהתוצאה מראה שהביצועים לא קשורים באופן ישיר לגודל של ממד ההטמעה, וממדים נמוכים יותר השיגו ציונים שדומים לאלה של הממדים הגבוהים יותר.

| מאפיין MRL | ציון MTEB‏ (Gemini Embedding 001) |
| --- | --- |
| 2048 | 68.16 |
| 1536 | 68.17 |
| 768 | ‪67.99 |
| 512 | 67.55 |
| 256 | 66.19 |
| 128 | 63.31 |

## הטמעות מולטי-מודאליות

מודל `gemini-embedding-2` תומך בקלט מולטי-מודאלי, כך שאפשר להטמיע תמונות, סרטונים, אודיו ותוכן מסמכים לצד טקסט. כל המודאליות ממופות לאותו מרחב הטמעה, מה שמאפשר חיפוש והשוואה בין מודאליות שונות.

### מגבלות וסוגי נתונים נתמכים

המגבלה הכוללת על מספר האסימונים בקלט היא 8,192 אסימונים.

| אופן הפעולה | מפרטים ומגבלות |
| --- | --- |
| **טקסט** | תמיכה בעד 8,192 טוקנים. |
| **תמונה** | אפשר להוסיף עד 6 תמונות לכל בקשה. פורמטים נתמכים: PNG, ‏ JPEG. |
| **אודיו** | משך הזמן המקסימלי הוא 180 שניות. פורמטים נתמכים: MP3, ‏ WAV. |
| **סרטון** | משך הזמן המקסימלי הוא 120 שניות. הפורמטים הנתמכים: MP4, ‏ MOV. קודקים נתמכים: H264, ‏ H265, ‏ AV1, ‏ VP9.  המערכת מעבדת עד 32 פריימים לכל סרטון: סרטונים קצרים (עד 32 שניות) נדגמים בקצב של פרים אחד לשנייה, ואילו סרטונים ארוכים יותר נדגמים באופן אחיד עד 32 פריימים. לא מתבצע עיבוד של טראקים של אודיו בקובצי וידאו. |
| **מסמכים (PDF)** | עד 6 עמודים. |

### הטמעת תמונות

בדוגמה הבאה אפשר לראות איך מטמיעים תמונה באמצעות `gemini-embedding-2`.

אפשר לספק תמונות כנתונים מוטבעים או כקבצים שהועלו דרך [Files API](https://ai.google.dev/gemini-api/docs/files?hl=he).

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

### צבירה של הטמעות

כשעובדים עם תוכן מולטימודאלי, מבנה הקלט משפיע על פלט ההטמעה:

- **כמה חלקים (מצטברים):** אם מוסיפים כמה קלטים ישירות לפרמטר `contents`, נוצרת הטמעה מצטברת אחת לכל הקלטים.
- **כמה אובייקטים של `Content` (נפרדים):** אם עוטפים כל קלט באובייקט `Content` ומעבירים אותם בפרמטר `contents`, המערכת מחזירה הטבעות נפרדות לכל רשומה.
- **ייצוג ברמת הפוסט:** לאובייקטים מורכבים כמו פוסטים ברשתות החברתיות עם כמה פריטי מדיה, מומלץ לצבור הטבעות נפרדות (למשל, על ידי חישוב ממוצע) כדי ליצור ייצוג קוהרנטי ברמת הפוסט.

בדוגמה הבאה מוצג איך ליצור הטמעה מצטברת אחת עבור קלט של טקסט ותמונה. פשוט מוסיפים כמה ערכים לפרמטר `contents`:

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

לעומת זאת, אם משתמשים באובייקטים `Content` בתוך הפרמטר `contents`, הפונקציה מחזירה הטבעות נפרדות. בדוגמה הזו נוצרות כמה הטמעות בקריאה אחת להטמעה:

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

### הטמעת אודיו

בדוגמה הבאה אפשר לראות איך מטמיעים קובץ אודיו באמצעות `gemini-embedding-2`.

אפשר לספק קובצי אודיו כנתונים מוטבעים או כקבצים שהועלו דרך [Files API](https://ai.google.dev/gemini-api/docs/files?hl=he).

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

### הטמעה של סרטון

בדוגמה הבאה אפשר לראות איך מטמיעים סרטון באמצעות `gemini-embedding-2`.

אפשר לספק סרטונים כנתונים מוטבעים או כקבצים שהועלו דרך [Files API](https://ai.google.dev/gemini-api/docs/files?hl=he).

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

אם אתם צריכים להטמיע סרטונים באורך של יותר מ-120 שניות, אתם יכולים לחלק את הסרטון לקטעים חופפים ולהטמיע כל קטע בנפרד.

### הטמעת מסמכים

אפשר להטמיע מסמכים בפורמט PDF ישירות. המודל מעבד את התוכן החזותי והטקסטואלי של כל דף.

אפשר לספק קובצי PDF כנתונים מוטבעים או כקבצים שהועלו דרך [Files API](https://ai.google.dev/gemini-api/docs/files?hl=he).

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

## תרחישים לדוגמה

הטמעות טקסט חיוניות למגוון תרחישי שימוש נפוצים ב-AI, כמו:

- **יצירה משולבת-אחזור (RAG):** הטמעות משפרות את האיכות של הטקסט שנוצר על ידי אחזור ושילוב של מידע רלוונטי בהקשר של מודל.
- **אחזור מידע:** חיפוש הטקסט או המסמכים הכי דומים מבחינה סמנטית בהינתן קטע טקסט כקלט.

  [הדרכה לחיפוש מסמכיםtask](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **דירוג מחדש של תוצאות החיפוש**: מתן עדיפות לפריטים הרלוונטיים ביותר על ידי ניתוח סמנטי של התוצאות הראשוניות בהשוואה לשאילתה.

  [מדריך לדירוג מחדש של תוצאות חיפושtask](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **זיהוי אנומליות:** השוואה בין קבוצות של הטמעות יכולה לעזור לזהות מגמות נסתרות או חריגות.

  [הדרכה בנושא זיהוי אנומליותbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **סיווג:** סיווג אוטומטי של טקסט על סמך התוכן שלו, כמו ניתוח סנטימנטים או זיהוי ספאם

  [מדריך לסיווגtoken](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **אשכולות:** כדי להבין ביעילות קשרים מורכבים, אפשר ליצור אשכולות והדמיות של ההטמעות.

  [מדריך לתצוגה חזותית של אשכולותbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## אחסון הטמעות

כשמעבירים הטמעות לייצור, נהוג להשתמש ב**מסדי נתונים וקטוריים** כדי לאחסן, ליצור אינדקס ולאחזר הטמעות רב-ממדיות בצורה יעילה. ‫Google Cloud מציע שירותי נתונים מנוהלים שאפשר להשתמש בהם למטרה הזו, כולל [Gemini Enterprise Agent Platform Vector Search 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/BUILD/vector-search-2?hl=he),‏ [BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=he), ‏ [AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=he) ו-[Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=he).

במדריכים הבאים מוסבר איך להשתמש במסדי נתונים אחרים של וקטורים של צד שלישי עם Gemini Embedding.

- [ChromaDB tutorialsbolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [מדריכים ל-QDrantbolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [מדריכים ל-Weaviatebolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [מדריכים של Pineconebolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## גרסאות המודלים

### Gemini Embedding 2

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | ‫**Gemini API**  `gemini-embedding-2` |
| saveסוגי נתונים נתמכים | **קלט**  טקסט, תמונה, סרטון, אודיו, PDF  **פלט**  הטמעות של טקסט |
| ‫token\_autoמגבלות על טוקנים[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=he) | **מגבלת טוקנים של קלט**  ‫8,192  **גודל מאפיין הפלט**  גמיש, תומך בערכים: 128 עד 3072, מומלץ: 768, ‏ 1536, ‏ 3072 |
| גרסאות 123 | פרטים נוספים זמינים במאמר בנושא [דפוסי גרסאות של מודלים](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#model-versions).  - יציב: `gemini-embedding-2` |
| calendar\_monthהעדכון האחרון | אפריל 2026 |

### Gemini Embedding

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | ‫**Gemini API**  `gemini-embedding-001` |
| saveסוגי נתונים נתמכים | **קלט**  טקסט  **פלט**  הטמעות של טקסט |
| ‫token\_autoמגבלות על טוקנים[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=he) | **מגבלת טוקנים של קלט**  2,048  **גודל מאפיין הפלט**  גמיש, תומך בערכים: 128 עד 3072, מומלץ: 768, ‏ 1536, ‏ 3072 |
| גרסאות 123 | פרטים נוספים זמינים במאמר בנושא [דפוסי גרסאות של מודלים](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#model-versions).  - יציב: `gemini-embedding-001` |
| calendar\_monthהעדכון האחרון | יוני 2025 |

למידע על מודלים של הטמעות שהוצאו משימוש, אפשר לעבור לדף [הוצאות משימוש](https://ai.google.dev/gemini-api/docs/deprecations?hl=he).

## העברה מ-gemini-embedding-001

הרווחים להטמעה בין `gemini-embedding-001` ל-`gemini-embedding-2` **לא תואמים**. כלומר, אי אפשר להשוות ישירות בין הטמעות שנוצרו על ידי מודל אחד לבין הטמעות שנוצרו על ידי המודל השני. אם אתם משדרגים ל-`gemini-embedding-2`, אתם צריכים להטמיע מחדש את כל הנתונים הקיימים.

בנוסף לחוסר התאימות, יש עוד כמה הבדלים חשובים בין שני המודלים:

- **ציון סוג המשימה:** ב-`gemini-embedding-001`, מציינים את סוג המשימה באמצעות הפרמטר `task_type` (למשל, `SEMANTIC_SIMILARITY`,‏ `RETRIEVAL_DOCUMENT`). ב-`gemini-embedding-2`, הפרמטר `task_type` לא נתמך. במקום זאת, צריך לכלול את הוראות המשימה ישירות בהנחיה למשימות של טקסט בלבד. במאמר [סוגי משימות עם Embeddings 2](#task-types-embeddings-2) מוסבר איך לנסח הנחיות לתרחישי שימוש שונים.
- **Embedding aggregation:** `gemini-embedding-001` generates individual
  embeddings for each string in a list of inputs. לעומת זאת,
  ‫`gemini-embedding-2` יוצר הטמעה אחת מצטברת כשמספקים כמה קלטים (כמו טקסט ותמונות) ישירות בבקשה אחת. כדי ליצור הטמעות נפרדות לכל קלט, צריך לעטוף כל קלט באובייקט `Content` או להשתמש ב-[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he#batch-embedding). מידע נוסף זמין במאמר בנושא [Embedding aggregation](#embedding-aggregation).
- **נרמול:** אם משתמשים ב-`output_dimensionality` כדי לבקש הטמעות עם פחות מ-3,072 ממדים, `gemini-embedding-2` מנרמל אוטומטית את ההטמעות החתוכות האלה. ב-`gemini-embedding-001`, צריך לבצע נרמול ידני למאפיינים שאינם 3072. פרטים נוספים זמינים במאמר בנושא [איך לשמור על איכות התמונות כשמשנים את המידות שלהן](#quality-for-smaller-dimensions).

## הטמעות באצווה

אם זמן האחזור לא חשוב לכם, נסו להשתמש במודלים של Gemini Embeddings עם [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he#batch-embedding). השינוי הזה מאפשר תפוקה גבוהה בהרבה ב-50% ממחיר ברירת המחדל של Embedding.
אפשר למצוא דוגמאות לתחילת העבודה ב[מדריך לשימוש ב-Batch API](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb).

## הודעה על שימוש אחראי

בניגוד למודלים של AI גנרטיבי שיוצרים תוכן חדש, מודל ההטמעה של Gemini נועד רק להמיר את הפורמט של נתוני הקלט לייצוג מספרי. ‫Google אחראית לספק מודל הטמעה שממיר את הפורמט של נתוני הקלט לפורמט המספרי המבוקש, אבל המשתמשים אחראים באופן מלא לנתונים שהם מזינים ולהטמעות שמתקבלות. השימוש במודל Gemini Embedding מבטא את האישור שלכם לכך שיש לכם את הזכויות הנדרשות על התוכן שאתם מעלים. אסור ליצור תוכן שמפר את זכויות הקניין הרוחני או זכויות הפרטיות של אחרים. השימוש בשירות הזה כפוף [למדיניות שלנו בנושא שימוש אסור](https://policies.google.com/terms/generative-ai/use-policy?hl=he) ו[לתנאים ולהגבלות של Google](https://ai.google.dev/gemini-api/terms?hl=he).

## איך מתחילים ליצור הטמעות

כדאי לעיין [במדריך למתחילים בנושא הטמעות](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb) כדי להכיר את היכולות של המודל וללמוד איך להתאים אישית את ההטמעות ולהציג אותן בצורה ויזואלית.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-07 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-07 (שעון UTC)."],[],[]]
