---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=he
fetched_at: 2026-09-28T06:25:42.127448+00:00
title: "\u05e9\u05de\u05d9\u05e8\u05d4 \u05d1\u05de\u05d8\u05de\u05d5\u05df \u05e9\u05dc \u05d4\u05e7\u05e9\u05e8 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=he)

שליחת משוב

# שמירה במטמון של הקשר

בתהליך עבודה טיפוסי של AI, יכול להיות שתעבירו את אותם אסימוני קלט שוב ושוב למודל. ‫Gemini API מציע שני מנגנוני שמירת נתונים במטמון:

- שמירה במטמון באופן מרומז (מופעלת אוטומטית ב-Gemini 2.5 ובמודלים חדשים יותר, ללא הבטחה לחיסכון בעלויות)
- שמירה במטמון באופן מפורש (אפשר להפעיל אותה באופן ידני ברוב המודלים, מובטח חיסכון בעלויות)

שמירת נתונים במטמון באופן מפורש שימושית במקרים שבהם רוצים להבטיח חיסכון בעלויות, אבל צריך להשקיע קצת יותר עבודה בפיתוח.

## שמירה מרומזת במטמון

האפשרות 'שמירת נתונים במטמון באופן מרומז' מופעלת כברירת מחדל בכל המודלים של Gemini 2.5 ומעלה. אם הבקשה שלכם מגיעה למטמון, אנחנו מעבירים את החיסכון בעלויות באופן אוטומטי. לא צריך לעשות שום דבר כדי להפעיל את התכונה הזו. בטבלה הבאה מפורטת כמות הטוקנים המינימלית של הקלט לשמירת הקשר במטמון לכל מודל:

| מודל | מגבלת טוקנים מינימלית |
| --- | --- |
| Gemini 3.8 Flash | ‫4,096 |
| Gemini 3.7 Flash | ‫4,096 |
| Gemini 3.6 Flash | ‫4,096 |
| Gemini 3.5 Flash | ‫4,096 |
| ‫Gemini 3.1 Pro Preview | ‫4,096 |
| Gemini ‎2.5 Flash | 2,048 |
| Gemini ‎2.5 Pro | 2,048 |

כדי להגדיל את הסיכוי לפגיעה במטמון משתמע:

- כדאי לנסות להוסיף בתחילת ההנחיה תוכן גדול ונפוץ
- ניסיון לשלוח בקשות עם קידומת דומה בפרק זמן קצר

אפשר לראות את מספר הטוקנים שהיו פגיעות במטמון בשדה `usage_metadata` של אובייקט התגובה.

## שמירה מפורשת במטמון

באמצעות התכונה של Gemini API לשמירה במטמון, אתם יכולים להעביר תוכן מסוים למודל פעם אחת, לשמור במטמון את טוקני הקלט ואז להפנות לטוקנים שנשמרו במטמון בבקשות הבאות. בנפחים מסוימים, העלות של שימוש בטוקנים שנשמרו במטמון נמוכה יותר מהעלות של העברה חוזרת של אותה קבוצת טוקנים.

כשמטמנים במטמון קבוצה של טוקנים, אפשר לבחור כמה זמן המטמון יתקיים לפני שהטוקנים יימחקו אוטומטית. משך השמירה במטמון נקרא *אורך חיים* (TTL). אם לא מגדירים את ה-TTL, ברירת המחדל היא שעה אחת. העלות של שמירת נתונים במטמון תלויה בגודל של טוקן הקלט ובמשך הזמן שבו רוצים שהטוקנים יישמרו.

בקטע הזה מניחים שהתקנתם Gemini SDK (או שהתקנתם curl) והגדרתם מפתח API, כמו שמוסבר ב[מדריך לתחילת העבודה](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=he).

### יצירת תוכן באמצעות מטמון

### Python

בדוגמה הבאה מוצג תהליך יצירת תוכן באמצעות הוראה במערכת וקובץ וידאו שנשמרו במטמון.

### סרטונים

```
import os
import pathlib
import requests
import time

from google import genai
from google.genai import types

client = genai.Client()

# Download a test video file and save it locally
url = 'https://storage.googleapis.com/generativeai-downloads/data/SherlockJr._10min.mp4'
path_to_video_file = pathlib.Path('SherlockJr._10min.mp4')
if not path_to_video_file.exists():
    path_to_video_file.write_bytes(requests.get(url).content)

# Upload the video using the Files API
video_file = client.files.upload(file=path_to_video_file)

# Wait for the file to finish processing
while video_file.state.name == 'PROCESSING':
    time.sleep(2.5)
    video_file = client.files.get(name=video_file.name)

print(f'Video processing complete: {video_file.uri}')

model='models/gemini-3.8-flash'

# Create a cache with a 5 minute TTL (300 seconds)
cache = client.caches.create(
    model=model,
    config=types.CreateCachedContentConfig(
        display_name='sherlock jr movie', # used to identify the cache
        system_instruction=(
            'You are an expert video analyzer, and your job is to answer '
            'the user\'s query based on the video file you have access to.'
        ),
        contents=[video_file],
        ttl="300s",
    )
)

response = client.models.generate_content(
    model = model,
    contents= (
    'Introduce different characters in the movie by describing '
    'their personality, looks, and names. Also list the timestamps '
    'they were introduced for the first time.'),
    config=types.GenerateContentConfig(cached_content=cache.name)
)

print(response.usage_metadata)

print(response.text)
```

### קובצי PDF

```
from google import genai
from google.genai import types
import io
import httpx

client = genai.Client()

long_context_pdf_path = "https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf"

# Retrieve and upload the PDF using the File API
doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

document = client.files.upload(
  file=doc_io,
  config=dict(mime_type='application/pdf')
)

model_name = "gemini-3.8-flash"
system_instruction = "You are an expert analyzing transcripts."

# Create a cached content object
cache = client.caches.create(
    model=model_name,
    config=types.CreateCachedContentConfig(
      system_instruction=system_instruction,
      contents=[document],
    )
)

print(f'{cache=}')

response = client.models.generate_content(
  model=model_name,
  contents="Please summarize this transcript",
  config=types.GenerateContentConfig(
    cached_content=cache.name
  ))

print(f'{response.usage_metadata=}')

print('\n\n', response.text)
```

### JavaScript

הדוגמה הבאה מראה איך ליצור תוכן באמצעות הוראה במערכת שנשמרה במטמון וקובץ טקסט.

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {
  const doc = await ai.files.upload({
    file: "path/to/file.txt",
    config: { mimeType: "text/plain" },
  });
  console.log("Uploaded file name:", doc.name);

  const modelName = "gemini-3.8-flash";
  const cache = await ai.caches.create({
    model: modelName,
    config: {
      contents: createUserContent(createPartFromUri(doc.uri, doc.mimeType)),
      systemInstruction: "You are an expert analyzing transcripts.",
    },
  });
  console.log("Cache created:", cache);

  const response = await ai.models.generateContent({
    model: modelName,
    contents: "Please summarize this transcript",
    config: { cachedContent: cache.name },
  });
  console.log("Response text:", response.text);
}

await main();
```

### Go

בדוגמה הבאה אפשר לראות איך ליצור תוכן באמצעות מטמון.

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
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey: "GOOGLE_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    modelName := "gemini-3.8-flash"
    document, err := client.Files.UploadFromPath(
        ctx,
        "media/a11.txt",
        &genai.UploadFileConfig{
          MIMEType: "text/plain",
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    parts := []*genai.Part{
        genai.NewPartFromURI(document.URI, document.MIMEType),
    }
    contents := []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }
    cache, err := client.Caches.Create(ctx, modelName, &genai.CreateCachedContentConfig{
        Contents: contents,
        SystemInstruction: genai.NewContentFromText(
          "You are an expert analyzing transcripts.", genai.RoleUser,
        ),
    })
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("Cache created:")
    fmt.Println(cache)

    // Use the cache for generating content.
    response, err := client.Models.GenerateContent(
        ctx,
        modelName,
        genai.Text("Please summarize this transcript"),
        &genai.GenerateContentConfig{
          CachedContent: cache.Name,
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    printResponse(response) // helper for printing response parts
}
```

### REST

בדוגמה הבאה אפשר לראות איך ליצור מטמון ואז להשתמש בו כדי ליצור תוכן.

### סרטונים

```
wget https://storage.googleapis.com/generativeai-downloads/data/a11.txt
echo '{
  "model": "models/gemini-3.8-flash",
  "contents":[
    {
      "parts":[
        {
          "inline_data": {
            "mime_type":"text/plain",
            "data": "'$(base64 $B64FLAGS a11.txt)'"
          }
        }
      ],
    "role": "user"
    }
  ],
  "systemInstruction": {
    "parts": [
      {
        "text": "You are an expert at analyzing transcripts."
      }
    ]
  },
  "ttl": "300s"
}' > request.json

curl -X POST "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d @request.json \
> cache.json

CACHE_NAME=$(cat cache.json | grep '"name":' | cut -d '"' -f 4 | head -n 1)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [
        {
          "parts":[{
            "text": "Please summarize this transcript"
          }],
          "role": "user"
        },
      ],
      "cachedContent": "'$CACHE_NAME'"
    }'
```

### קובצי PDF

```
DOC_URL="https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf"
DISPLAY_NAME="A11_Mission_Report"
SYSTEM_INSTRUCTION="You are an expert at analyzing transcripts."
PROMPT="Please summarize this transcript"
MODEL="models/gemini-3.8-flash"
TTL="300s"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

MIME_TYPE=$(file -b --mime-type "${DISPLAY_NAME}.pdf")
NUM_BYTES=$(wc -c < "${DISPLAY_NAME}.pdf")

echo "MIME_TYPE: ${MIME_TYPE}"
echo "NUM_BYTES: ${NUM_BYTES}"

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files?key=${GOOGLE_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${DISPLAY_NAME}.pdf" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo "file_uri: ${file_uri}"

# Clean up the downloaded PDF
rm "${DISPLAY_NAME}.pdf"

# Create the cached content request
echo '{
  "model": "'$MODEL'",
  "contents":[
    {
      "parts":[
        {"file_data": {"mime_type": "'$MIME_TYPE'", "file_uri": '$file_uri'}}
      ],
    "role": "user"
    }
  ],
  "system_instruction": {
    "parts": [
      {
        "text": "'$SYSTEM_INSTRUCTION'"
      }
    ],
    "role": "system"
  },
  "ttl": "'$TTL'"
}' > request.json

# Send the cached content request
curl -X POST "${BASE_URL}/v1beta/cachedContents?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d @request.json \
> cache.json

CACHE_NAME=$(cat cache.json | grep '"name":' | cut -d '"' -f 4 | head -n 1)
echo "CACHE_NAME: ${CACHE_NAME}"
# Send the generateContent request using the cached content
curl -X POST "${BASE_URL}/${MODEL}:generateContent?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [
        {
          "parts":[{
            "text": "'$PROMPT'"
          }],
          "role": "user"
        }
      ],
      "cachedContent": "'$CACHE_NAME'"
    }' > response.json

cat response.json

echo jq ".candidates[].content.parts[].text" response.json
```

### הצגת רשימה של מטמונים

אי אפשר לאחזר או להציג תוכן שנשמר במטמון, אבל אפשר לאחזר מטא-נתונים של המטמון (`name`,‏ `model`,‏ `display_name`,‏ `usage_metadata`,‏ `create_time`,‏ `update_time` ו-`expire_time`).

### Python

כדי להציג רשימה של המטא-נתונים של כל המטמונים שהועלו, משתמשים בפקודה `CachedContent.list()`:

```
for cache in client.caches.list():
  print(cache)
```

כדי לאחזר את המטא-נתונים של אובייקט אחד במטמון, אם אתם יודעים את השם שלו, משתמשים בפקודה `get`:

```
client.caches.get(name=name)
```

### JavaScript

כדי להציג רשימה של המטא-נתונים של כל המטמונים שהועלו, משתמשים בפקודה `GoogleGenAI.caches.list()`:

```
console.log("My caches:");
const pager = await ai.caches.list({ config: { pageSize: 10 } });
let page = pager.page;
while (true) {
  for (const c of page) {
    console.log("    ", c.name);
  }
  if (!pager.hasNextPage()) break;
  page = await pager.nextPage();
}
```

### Go

בדוגמה הבאה מוצגת רשימה של כל המטמונים.

```
caches, err := client.Caches.All(ctx)
if err != nil {
    log.Fatal(err)
}
fmt.Println("Listing all caches:")
for _, item := range caches {
    fmt.Println("   ", item.Name)
}
```

בדוגמה הבאה מוצגות רשימות של מטמונים עם גודל דף של 2.

```
page, err := client.Caches.List(ctx, &genai.ListCachedContentsConfig{PageSize: 2})
if err != nil {
    log.Fatal(err)
}

pageIndex := 1
for {
    fmt.Printf("Listing caches (page %d):\n", pageIndex)
    for _, item := range page.Items {
        fmt.Println("   ", item.Name)
    }
    if page.NextPageToken == "" {
        break
    }
    page, err = page.Next(ctx)
    if err == genai.ErrPageDone {
        break
    } else if err != nil {
        return err
    }
    pageIndex++
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY"
```

### עדכון מטמון

אפשר להגדיר `ttl` או `expire_time` חדשים למטמון. אין תמיכה בשינוי של פרטים אחרים במטמון.

### Python

בדוגמה הבאה אפשר לראות איך מעדכנים את `ttl` של מטמון באמצעות `client.caches.update()`.

```
from google import genai
from google.genai import types

client.caches.update(
  name = cache.name,
  config  = types.UpdateCachedContentConfig(
      ttl='300s'
  )
)
```

כדי להגדיר את זמן התפוגה, אפשר להשתמש באובייקט `datetime` או במחרוזת של תאריך ושעה בפורמט ISO ‏ (`dt.isoformat()`, כמו `2025-01-27T16:02:36.473528+00:00`). צריך לציין את אזור הזמן (`datetime.utcnow()` לא מצרף אזור זמן, `datetime.now(datetime.timezone.utc)` כן מצרף אזור זמן).

```
from google import genai
from google.genai import types
import datetime

# You must use a time zone-aware time.
in10min = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=10)

client.caches.update(
  name = cache.name,
  config  = types.UpdateCachedContentConfig(
      expire_time=in10min
  )
)
```

### JavaScript

בדוגמה הבאה אפשר לראות איך מעדכנים את `ttl` של מטמון באמצעות `GoogleGenAI.caches.update()`.

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### Go

בדוגמה הבאה אפשר לראות איך מעדכנים את `TTL` של מטמון.

```
// Update the TTL (2 hours).
cache, err = client.Caches.Update(ctx, cache.Name, &genai.UpdateCachedContentConfig{
    TTL: 7200 * time.Second,
})
if err != nil {
    log.Fatal(err)
}
fmt.Println("After update:")
fmt.Println(cache)
```

### REST

בדוגמה הבאה אפשר לראות איך מעדכנים את `ttl` של מטמון.

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### מחיקת מטמון

שירות המטמון מספק פעולת מחיקה להסרת תוכן מהמטמון באופן ידני. בדוגמה הבאה אפשר לראות איך מוחקים מטמון:

### Python

```
client.caches.delete(cache.name)
```

### JavaScript

```
await ai.caches.delete({ name: cache.name });
```

### Go

```
_, err = client.Caches.Delete(ctx, cache.Name, &genai.DeleteCachedContentConfig{})
if err != nil {
    log.Fatal(err)
}
fmt.Println("Cache deleted:", cache.Name)
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY"
```

### שמירת נתונים במטמון באופן מפורש באמצעות ספריית OpenAI

אם אתם משתמשים ב[ספרייה של OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=he), אתם יכולים להפעיל שמירה במטמון באופן מפורש באמצעות המאפיין `cached_content` ב-[`extra_body`](https://ai.google.dev/gemini-api/docs/openai?hl=he#extra-body).

## מתי כדאי להשתמש בשמירת נתונים במטמון

שמירת נתונים במטמון לפי הקשר מתאימה במיוחד למקרים שבהם יש הקשר ראשוני משמעותי שאליו מתייחסות שוב ושוב בקשות קצרות יותר. כדאי להשתמש בשמירה במטמון של ההקשר בתרחישים כמו:

- צ'אטבוטים עם [הוראות מערכת](https://ai.google.dev/gemini-api/docs/system-instructions?hl=he) מפורטות
- ניתוח חוזר של קובצי וידאו ארוכים
- שאילתות חוזרות על קבוצות גדולות של מסמכים
- ניתוח תכוף של מאגר קוד או תיקון באגים

### איך שמירת מטמון מפורשת מפחיתה עלויות

שמירת הקשר במטמון היא תכונה בתשלום שנועדה להפחית את העלויות. החיוב מבוסס על הגורמים הבאים:

1. **מספר הטוקנים במטמון:** מספר טוקני הקלט שנשמרו במטמון. אם הם נכללים בהנחיות הבאות, הם מחויבים במחיר מופחת.
2. **משך האחסון:** משך הזמן שבו טוקנים במטמון מאוחסנים (TTL),
   החיוב מתבצע על סמך משך ה-TTL של ספירת הטוקנים במטמון. אין גבולות מינימליים או מקסימליים לערך ה-TTL.
3. **גורמים אחרים:** חלים חיובים אחרים, למשל על טוקנים של קלט ופלט שלא נשמרו במטמון.

פרטים עדכניים על התמחור זמינים [בדף התמחור](https://ai.google.dev/pricing?hl=he) של Gemini API. ב[מדריך לאסימונים](https://ai.google.dev/gemini-api/docs/tokens?hl=he) מוסבר איך לספור אסימונים.

### שיקולים נוספים

כשמשתמשים בשמירת מטמון של הקשר, חשוב לזכור את הנקודות הבאות:

- כמות הטוקנים ה*מינימלית* של הקלט לשמירת הקשר במטמון משתנה בהתאם למודל. *הערך המקסימלי* זהה לערך המקסימלי של המודל הנתון. (מידע נוסף על ספירת אסימונים זמין ב[מדריך האסימונים](https://ai.google.dev/gemini-api/docs/tokens?hl=he)).
- המודל לא מבחין בין טוקנים במטמון לבין טוקנים רגילים של קלט. התוכן שנשמר במטמון מופיע כתוספת לתחילת ההנחיה.
- אין מגבלות מיוחדות על שיעור השימוש או על שיעור הבקשות במטמון ההקשר. חלות מגבלות השיעור הרגילות של `GenerateContent`, ומגבלות האסימונים כוללות אסימונים במטמון.
- מספר האסימונים שנשמרו במטמון מוחזר ב-`usage_metadata` מפעולות היצירה, האחזור והרשימה של שירות המטמון, וגם ב-`GenerateContent` כשמשתמשים במטמון.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-16 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-16 (שעון UTC)."],[],[]]
