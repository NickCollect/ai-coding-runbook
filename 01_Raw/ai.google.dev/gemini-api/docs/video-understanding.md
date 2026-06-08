---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=he
fetched_at: 2026-06-08T05:27:27.898504+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# הבנת סרטונים

> מידע על יצירת סרטונים זמין במדריך [Veo](https://ai.google.dev/gemini-api/docs/video?hl=he).

מודלים של Gemini יכולים לעבד סרטונים, וכך לאפשר למפתחים להשתמש בהם בתרחישי שימוש רבים ומתקדמים, שבדרך כלל נדרשים להם מודלים ספציפיים לתחום.
בין היכולות של Gemini לראייה: תיאור, פילוח וחילוץ מידע מסרטונים, מענה על שאלות לגבי תוכן של סרטונים והפניה לחותמות זמן ספציפיות בסרטון.

יש כמה דרכים לספק סרטונים כקלט ל-Gemini:

| שיטת קלט | גודל מקסימלי | תרחיש שימוש מומלץ |
| --- | --- | --- |
| [File API](#upload-video) | ‫20GB (בתשלום) / 2GB (בחינם) | קבצים גדולים (100MB ומעלה), סרטונים ארוכים (10 דקות ומעלה), קבצים שאפשר לעשות בהם שימוש חוזר. |
| [Cloud Storage Registration](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=he#registration) | ‫2GB (לכל קובץ, ללא מגבלות אחסון) | קבצים גדולים (100MB ומעלה), סרטונים ארוכים (10 דקות ומעלה), קבצים קבועים שאפשר לעשות בהם שימוש חוזר. |
| [נתונים מוטבעים](#inline-video) | < 100MB | קבצים קטנים (פחות מ-100MB), משך קצר (פחות מדקה), קלט חד-פעמי. |
| [כתובות URL ב-YouTube](#youtube) | לא רלוונטי | סרטונים ציבוריים ב-YouTube. |

> **הערה:** מומלץ להשתמש ב-[File API](#upload-video) ברוב תרחישי השימוש, במיוחד כשמדובר בקבצים גדולים מ-100MB או כשרוצים לעשות שימוש חוזר בקובץ בכמה בקשות.

מידע על שיטות אחרות להזנת קבצים, כמו שימוש בכתובות URL חיצוניות או בקבצים שמאוחסנים ב-Google Cloud, מופיע במדריך [שיטות להזנת קבצים](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=he).

### העלאת קובץ של סרטון

הקוד הבא מוריד סרטון לאימון המודל, מעלה אותו באמצעות [Files API](https://ai.google.dev/gemini-api/docs/files?hl=he), מחכה לסיום העיבוד שלו ואז משתמש בהפניה לקובץ שהועלה כדי לסכם את הסרטון.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
)

print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", nil)

parts := []*genai.Part{
    genai.NewPartFromText("Summarize this video. Then create a quiz with an answer key based on the information in this video."),
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.5-flash",
    contents,
    nil,
)

fmt.Println(result.Text())
```

### REST

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# --- 3. Generate content using the uploaded video file ---
echo "Generating content from video..."
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},
          {"text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}]
        }]
      }' 2> /dev/null > response.json

jq -r ".candidates[].content.parts[].text" response.json
```

תמיד צריך להשתמש ב-Files API אם הגודל הכולל של הבקשה (כולל הקובץ, הנחיית הטקסט, הוראות המערכת וכו') גדול מ-20MB, אם משך הסרטון משמעותי או אם מתכוונים להשתמש באותו סרטון בכמה הנחיות.
‫File API מקבל ישירות פורמטים של קובצי וידאו.

מידע נוסף על עבודה עם קובצי מדיה זמין במאמר בנושא [Files API](https://ai.google.dev/gemini-api/docs/files?hl=he).

### העברת נתוני סרטונים בתוך התג

במקום להעלות קובץ וידאו באמצעות File API, אפשר להעביר סרטונים קצרים יותר ישירות בבקשה אל `generateContent`. האפשרות הזו מתאימה לסרטונים קצרים יותר, עד גודל בקשה כולל של 20MB.

דוגמה לאספקת נתוני וידאו מוטמעים:

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const contents = [
  {
    inlineData: {
      mimeType: "video/mp4",
      data: base64VideoFile,
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: contents,
});
console.log(response.text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"video/mp4",
                "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'"
              }
            },
            {"text": "Please summarize the video in 3 sentences."}
        ]
      }]
    }' 2> /dev/null
```

### העברת כתובות URL ב-YouTube

אתם יכולים להעביר כתובות URL של YouTube ישירות אל Gemini API כחלק מהבקשה שלכם, באופן הבא:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=9hE5-98ZeCg')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const contents = [
  {
    fileData: {
      fileUri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: contents,
});
console.log(response.text);
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  parts := []*genai.Part{
      genai.NewPartFromText("Please summarize the video in 3 sentences."),
      genai.NewPartFromURI("https://www.youtube.com/watch?v=9hE5-98ZeCg","video/mp4"),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.5-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Please summarize the video in 3 sentences."},
            {
              "file_data": {
                "file_uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
              }
            }
        ]
      }]
    }' 2> /dev/null
```

**מגבלות:**

- בתוכנית החינמית, אי אפשר להעלות יותר מ-8 שעות של סרטוני YouTube ביום.
- במינוי בתשלום, אין הגבלה על אורך הסרטון.
- במודלים שקודמים ל-Gemini 2.5, אפשר להעלות רק סרטון אחד לכל בקשה. במודלים Gemini 2.5 ואילך, אפשר להעלות עד 10 סרטונים לכל בקשה.
- אפשר להעלות רק סרטונים שגלויים לכולם (לא סרטונים פרטיים או לא רשומים).

## שימוש במטמון הקשר לסרטונים ארוכים

בסרטונים באורך של יותר מ-10 דקות, או כשמתכננים לשלוח כמה בקשות לאותו קובץ וידאו, מומלץ להשתמש ב[שמירת הקשר במטמון](https://ai.google.dev/gemini-api/docs/caching?hl=he) כדי להקטין את העלויות ולשפר את זמן האחזור. השימוש במטמון של ההקשר מאפשר לעבד את הסרטון פעם אחת ולעשות שימוש חוזר בטוקנים בשאילתות הבאות. לכן, הוא אידיאלי לשיחות בצ'אט או לניתוח חוזר של תוכן ארוך.

## הפניה לחותמות זמן בתוכן

אתם יכולים לשאול שאלות על נקודות זמן ספציפיות בסרטון באמצעות חותמות זמן בתבנית `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?" # Adjusted timestamps for the NASA video
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
         // Adjusted timestamps for the NASA video
        genai.NewPartFromText("What are the examples given at 00:05 and " +
            "00:10 supposed to show us?"),
    }
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## חילוץ תובנות מפורטות מסרטון

מודלים של Gemini מציעים יכולות מתקדמות להבנת תוכן וידאו באמצעות עיבוד מידע מזרמי **האודיו והווידאו**. התכונה הזו מאפשרת לכם לחלץ מגוון רחב של פרטים, כולל יצירת תיאורים של מה שקורה בסרטון ומענה על שאלות לגבי התוכן שלו.

בתיאורים חזותיים, המודל דוגם את הסרטון בקצב של **פרים אחד לשנייה** (FPS). קצב הדגימה הזה מתאים לרוב התוכן, אבל חשוב לזכור שהוא עלול לפספס פרטים בסרטונים עם תנועה מהירה או שינויי סצנה מהירים.
במקרה של תוכן עם תנועה רבה, כדאי [להגדיר קצב פריימים בהתאמה אישית](#custom-frame-rate).

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
        genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
      "Include timestamps for salient moments."),
    }
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## התאמה אישית של עיבוד הסרטון

אתם יכולים להתאים אישית את עיבוד הסרטון ב-Gemini API על ידי הגדרת מרווחי חיתוך או על ידי מתן דגימה מותאמת אישית של קצב הפריימים.

### הגדרת מרווחי חיתוך

כדי ליצור קליפ מסרטון, מציינים את `videoMetadata` עם היסטים של התחלה וסיום.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=XEzRZ35urlk'),
                video_metadata=types.VideoMetadata(
                    start_offset='1250s',
                    end_offset='1570s'
                )
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});
const model = 'gemini-3.5-flash';

async function main() {
const contents = [
  {
    role: 'user',
    parts: [
      {
        fileData: {
          fileUri: 'https://www.youtube.com/watch?v=9hE5-98ZeCg',
          mimeType: 'video/*',
        },
        videoMetadata: {
          startOffset: '40s',
          endOffset: '80s',
        }
      },
      {
        text: 'Please summarize the video in 3 sentences.',
      },
    ],
  },
];

const response = await ai.models.generateContent({
  model,
  contents,
});

console.log(response.text)

}

await main();
```

### הגדרת קצב פריימים בהתאמה אישית

אפשר להגדיר דגימה מותאמת אישית של קצב פריימים על ידי העברת ארגומנט `fps` אל
`videoMetadata`.

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(
                    data=video_bytes,
                    mime_type='video/mp4'),
                video_metadata=types.VideoMetadata(fps=5)
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

כברירת מחדל, המערכת דוגמת פריימים מהסרטון בקצב של פרים אחד לשנייה (FPS). כדאי להגדיר קצב פריימים נמוך (פחות מ-1) לסרטונים ארוכים. האפשרות הזו שימושית במיוחד לסרטונים סטטיים ברובם (למשל הרצאות). כדאי להשתמש בקצב פריימים גבוה יותר בסרטונים שנדרש בהם ניתוח זמני מפורט, כמו הבנת פעולה מהירה או מעקב תנועה במהירות גבוהה.

## פורמטים נתמכים של וידאו

‫Gemini תומך בסוגי ה-MIME הבאים של פורמטים של סרטונים:

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## פרטים טכניים על סרטונים

- **מודלים נתמכים והקשר**: כל ממשקי Gemini יכולים לעבד נתוני וידאו.
  - מודלים עם חלון הקשר של מיליון טוקנים יכולים לעבד סרטונים באורך של עד שעה ברזולוציית מדיה רגילה או באורך של עד 3 שעות ברזולוציית מדיה נמוכה.
- **עיבוד באמצעות File API**: כשמשתמשים ב-File API, הסרטונים מאוחסנים ב-1 פריימים לשנייה (FPS) והשמע מעובד ב-1Kbps (ערוץ יחיד).
  חותמות הזמן מתווספות כל שנייה.
  - המחירים האלה עשויים להשתנות בעתיד בעקבות שיפורים בהסקת המסקנות.
  - אפשר לשנות את קצב הדגימה של 1 FPS על ידי [הגדרת קצב פריימים מותאם אישית](#custom-frame-rate).
- **חישוב הטוקנים**: כל שנייה של סרטון עוברת טוקניזציה באופן הבא:
  - פריימים בודדים (נדגמים ב-1 FPS):
    - אם הערך של [`mediaResolution`](https://ai.google.dev/api/generate-content?hl=he#MediaResolution) מוגדר כנמוך, המערכת יוצרת טוקניזציה של הפריימים בשיעור של 66 טוקנים לכל פרים.
    - אחרת, הפריימים עוברים טוקניזציה בשיעור של 258 טוקנים לכל פריים.
  - אודיו: 32 טוקנים לשנייה.
  - המטא-נתונים כלולים גם הם.
  - סך הכול: כ-300 טוקנים לשנייה של וידאו ברזולוציית מדיה שמוגדרת כברירת מחדל, או 100 טוקנים לשנייה של וידאו ברזולוציית מדיה נמוכה.
- **רזולוציה בינונית**: ב-Gemini 3 יש שליטה מדויקת בעיבוד של ראייה מולטימודאלית באמצעות הפרמטר `media_resolution`. הפרמטר `media_resolution` קובע את **המספר המקסימלי של טוקנים שמוקצים לכל תמונה או פריים של סרטון קלט.**
  רזולוציות גבוהות יותר משפרות את היכולת של המודל לקרוא טקסט קטן או לזהות פרטים קטנים, אבל מגדילות את השימוש באסימונים ואת זמן האחזור.

  לפרטים נוספים על הפרמטר ועל האופן שבו הוא יכול להשפיע על חישובי האסימון, אפשר לעיין במדריך בנושא [רזולוציית מדיה](https://ai.google.dev/gemini-api/docs/media-resolution?hl=he).
- **פורמט חותמת הזמן**: כשמתייחסים לרגעים ספציפיים בסרטון בהנחיה, צריך להשתמש בפורמט `MM:SS` (למשל, `01:15` בשביל דקה ו-15 שניות).
- **שיטות מומלצות:**

  - כדי לקבל תוצאות אופטימליות, מומלץ להשתמש רק בסרטון אחד בכל בקשת הנחיה.
  - אם משלבים טקסט וסרטון אחד, צריך למקם את הנחיית הטקסט *אחרי* החלק של הסרטון במערך `contents`.
  - חשוב לדעת שרצפי פעולות מהירים עלולים לאבד פרטים בגלל קצב הדגימה של 1 FPS. במקרה הצורך, אפשר להאט את הקליפים האלה.

## המאמרים הבאים

במדריך הזה מוסבר איך להעלות קובצי וידאו וליצור פלט טקסט מקלט וידאו. מידע נוסף זמין במקורות המידע הבאים:

- [הוראות למערכת](https://ai.google.dev/gemini-api/docs/text-generation?hl=he#system-instructions):
  הוראות למערכת מאפשרות לכוון את התנהגות המודל בהתאם לצרכים הספציפיים ולתרחישי השימוש שלכם.
- ‫[Files API](https://ai.google.dev/gemini-api/docs/files?hl=he): מידע נוסף על העלאה וניהול של קבצים לשימוש עם Gemini.
- [אסטרטגיות לכתיבת הנחיות עם קבצים](https://ai.google.dev/gemini-api/docs/files?hl=he#prompt-guide): Gemini API תומך בכתיבת הנחיות עם נתוני טקסט, תמונה, אודיו ווידאו, שנקראות גם כתיבת הנחיות מולטי-מודאליות.
- [הנחיות בטיחות](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=he): לפעמים מודלים של AI גנרטיבי יוצרים תוצאות לא צפויות, כמו תוצאות לא מדויקות, מוטות או פוגעניות. כדי לצמצם את הסיכון לנזק שעלול להיגרם מהתוצאות האלה, חשוב לבצע עיבוד לאחר יצירת התוצאות והערכה אנושית.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-06-01 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-06-01 (שעון UTC)."],[],[]]
