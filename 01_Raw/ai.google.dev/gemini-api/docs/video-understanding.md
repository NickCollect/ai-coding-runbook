---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=he
fetched_at: 2026-09-14T05:37:05.192924+00:00
title: "\u05d4\u05d1\u05e0\u05ea \u05e1\u05e8\u05d8\u05d5\u05e0\u05d9\u05dd \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# הבנת סרטונים

> מידע נוסף על יצירת סרטונים זמין במדריך [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=he).

מודלים של Gemini יכולים לעבד סרטונים, וכך לאפשר למפתחים להשתמש בהם בתרחישי שימוש רבים ומתקדמים, שבדרך כלל נדרשים להם מודלים ספציפיים לתחום.
חלק מהיכולות של Gemini בתחום הראייה כוללות את האפשרות: לתאר, לפלח ולחלץ מידע מסרטונים, לענות על שאלות לגבי תוכן של סרטונים ולהתייחס לחותמות זמן ספציפיות בסרטון.

יש כמה דרכים לספק סרטונים כקלט ל-Gemini:

| שיטת קלט | גודל מקסימלי | תרחיש שימוש מומלץ |
| --- | --- | --- |
| [File API](#upload-video) | ‫20GB (בתשלום) / 2GB (בחינם) | קבצים גדולים (100MB ומעלה), סרטונים ארוכים (10 דקות ומעלה), קבצים שאפשר לעשות בהם שימוש חוזר. |
| [הרשמה ל-Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=he#registration) | ‫2GB (לכל קובץ, ללא מגבלות אחסון) | קבצים גדולים (100MB ומעלה), סרטונים ארוכים (10 דקות ומעלה), קבצים קבועים שאפשר לעשות בהם שימוש חוזר. |
| [נתונים מוטבעים](#inline-video) | < 100MB | קבצים קטנים (פחות מ-100MB), משך קצר (פחות מדקה), קלט חד-פעמי. |
| [כתובות URL ב-YouTube](#youtube) | לא רלוונטי | סרטונים ציבוריים ב-YouTube. |

> **הערה:** מומלץ להשתמש ב-[File API](#upload-video) ברוב תרחישי השימוש, במיוחד בקבצים שגודלם גדול מ-100MB או כשרוצים לעשות שימוש חוזר בקובץ בכמה בקשות.

מידע על שיטות אחרות להזנת קבצים, כמו שימוש בכתובות URL חיצוניות או בקבצים שמאוחסנים ב-Google Cloud, מופיע במדריך [שיטות להזנת קבצים](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=he).

### העלאת קובץ של סרטון

הקוד הבא מוריד סרטון לאימון המודל, מעלה אותו באמצעות [Files API](https://ai.google.dev/gemini-api/docs/files?hl=he), מחכה לסיום העיבוד שלו ואז משתמש בהפניה לקובץ שהועלה כדי לסכם את הסרטון.

### Python

```
from google import genai
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "video", "uri": myfile.uri, "mime_type": myfile.mime_type},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  let getFile = await ai.files.get({ name: myfile.name });
  while (getFile.state === 'PROCESSING') {
      getFile = await ai.files.get({ name: myfile.name });
      console.log(`current file status: ${getFile.state}`);
      console.log('File is still processing, retrying in 5 seconds');

      await new Promise((resolve) => {
          setTimeout(resolve, 5000);
      });
  }
  if (getFile.state === 'FAILED') {
      throw new Error('File processing failed.');
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Summarize the key events in this video.").build();
Content videoContent =
    VideoContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/video/pixel8.mp4")
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
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
file_name=$(jq -r ".file.name" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# Polling loop
echo "Waiting for file to be processed..."
while true; do
  curl -s "https://generativelanguage.googleapis.com/v1beta/${file_name}" \
    -H "x-goog-api-key: $GEMINI_API_KEY" > file_status.json
  state=$(jq -r ".state" file_status.json)
  echo "Current state: $state"
  if [ "$state" == "ACTIVE" ]; then
    break
  elif [ "$state" == "FAILED" ]; then
    echo "File processing failed."
    exit 1
  fi
  sleep 5
done

echo "Generating content from video..."
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

כדי לייעל את היעילות והביצועים של הטוקנים, מומלץ להשתמש ב[עיבוד סרטונים באמצעות סוכנים](#agentic-video-understanding).

תמיד צריך להשתמש ב-Files API אם הגודל הכולל של הבקשה (כולל הקובץ, הנחיית הטקסט, הוראות המערכת וכו') גדול מ-20MB, אם משך הסרטון משמעותי או אם מתכוונים להשתמש באותו סרטון בכמה הנחיות.
‫File API מקבל ישירות פורמטים של קובצי וידאו.

מידע נוסף על עבודה עם קובצי מדיה זמין במאמר בנושא [Files API](https://ai.google.dev/gemini-api/docs/files?hl=he).

### העברת נתוני סרטונים בתוך התג

במקום להעלות קובץ וידאו באמצעות File API, אפשר להעביר סרטונים קצרים יותר ישירות בבקשה. האפשרות הזו מתאימה לסרטונים קצרים יותר, שגודל הבקשה הכולל שלהם הוא פחות מ-20MB.

דוגמה לאספקת נתוני וידאו מוטמעים:

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "data": base64.b64encode(video_bytes).decode('utf-8'),
            "mime_type": "video/mp4"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      data: base64VideoFile,
      mime_type: "video/mp4",
    }
  ],
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Summarize the key events in this video.").build();
Content videoContent =
    VideoContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/video/pixel8.mp4")
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'",
          "mime_type": "video/mp4"
        }
      ]
    }' 2> /dev/null
```

### העברת כתובות URL ב-YouTube

אתם יכולים להעביר כתובות URL של YouTube ישירות אל Gemini API כחלק מהבקשה שלכם, באופן הבא:

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      uri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    }
  ],
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Summarize the key events in this video.").build();
Content videoContent =
    VideoContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/video/pixel8.mp4")
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**מגבלות:**

- בתוכנית החינמית, אי אפשר להעלות יותר מ-8 שעות של סרטוני YouTube ביום.
- במינוי בתשלום, אין מכסה על אורך הסרטון.
- במודלים שקודמים ל-Gemini 2.5, אפשר להעלות רק סרטון אחד לכל בקשה. במודלים Gemini 2.5 ואילך, אפשר להעלות עד 10 סרטונים לכל בקשה.
- אפשר להעלות רק סרטונים שגלויים לכולם (ולא סרטונים פרטיים או לא רשומים).

## הבנת סרטונים על ידי סוכן

כברירת מחדל, קבצים של קלט וידאו עוברים עיבוד סטטי (חילוץ פריימים בקצב של 1 FPS).
מודלים של Gemini 3.8 Flash,‏ 3.7 Flash,‏ 3.6 Flash ו-3.5 Flash Lite תומכים גם ב**הבנת סרטונים באמצעות סוכנים**. במודל הזה, המודל בוחן באופן דינמי את ציר הזמן של הסרטון, בודק באופן סלקטיבי תמלילים ומתאים באופן אדפטיבי את קצב הפריימים והרזולוציה תוך כדי תנועה על סמך ההנחיה.

| **המצב** | **תיאור** | **דגמים נתמכים** |
| --- | --- | --- |
| **סטטי** (ברירת מחדל) | הכלי מחלץ פריימים בקצב קבוע (1 FPS) ומציב אותם בהקשר במעבר יחיד. מתאים לקטעי וידאו קצרים. | כל המודלים של Gemini |
| **Agentic** | המודל מנווט באופן דינמי בציר הזמן של הסרטון, וטוען רק את התוכן שהוא צריך על סמך ההנחיה. עד 88% יותר יעילות בשימוש בטוקנים ואיכות גבוהה יותר בכ-7% בתכנים ארוכים. | ‫Gemini 3.8 Flash, ‏ Gemini 3.7 Flash, ‏ Gemini 3.6 Flash, ‏ Gemini 3.5 Flash Lite |

### בחירת מצב עיבוד

ככלל, מומלץ להתחיל במצב **agentic**, במיוחד כשמבצעים אופטימיזציה לאיכות התשובה או ליעילות השימוש באסימונים.

- **סוכן:** סרטונים ארוכים או שאילתות שמטרגטות רגעים ספציפיים. המודל עובר באופן דינמי בציר הזמן כדי למקד מידע רלוונטי להקשר בלי למלא את חלון ההקשר.
- **סטטי:** שאילתות שרגישות לזמן האחזור בקליפים קצרים (עד 5 דקות), או במקרים שבהם נדרשת רמת דיוק של פריים בכל הקליפ.

> **הערה:** בסרטונים ארוכים או בהנחיות מורכבות שבהן העיבוד על ידי הסוכן לוקח יותר זמן, כדאי להשתמש בסטרימינג (`stream=True`) או בהרצת הרקע (`background=True`). כך החיבור יישאר פעיל, שלבי הנימוק הביניים יוצגו ולא יתרחשו פסק זמן בחיבור או באימות.

### הגדרת מצב העיבוד

### Python

```
import time
from google import genai

client = genai.Client()

# Upload a long video
video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

# Use agentic processing
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": "agentic"
        },
        {"type": "text", "text": "What are the three main arguments presented?"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Upload a long video
let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" }
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

// Use agentic processing
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: "agentic"
    },
    { type: "text", text: "What are the three main arguments presented?" }
  ]
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {"type": "text", "text": "What are the three main arguments presented?"}
    ]
  }' 2> /dev/null
```

> **הערה:** כדי לוודא שהיה שימוש בעיבוד מבוסס-סוכן, בודקים את `interaction.steps`. הנוכחות של התגים `processing_call` ו-`processing_result` מציינת שהמודל ניווט בסרטון באופן דינמי.

### שלבי התגובה

עיבוד אקטיבי מוסיף שני סוגים חדשים של שלבים למערך `steps`:

- ‫`processing_call`: המודל ביקש קטע וידאו או תמליל אודיו, שמזוהים על ידי `id`.
- ‫`processing_result`: התוצאה של הטעינה הזו, שמקושרת באמצעות `call_id`.

הן מופיעות לסירוגין עם `thought` שלבים (כשהסיכומים מופעלים) ולפני השלב הסופי `model_output`. אפשר להשתמש בהם כדי להציג את התקדמות התהליך בממשק המשתמש, אבל לא צריך להגיב עליהם.

בדוגמה הבאה מוצג מטען הייעודי (payload) של התגובה עם שלבי עיבוד משולבים:

```
{
  "steps": [
    {
      "type": "thought",
      "signature": "sig_thought_1",
      "summary": [
        {
          "type": "text",
          "text": "Inspecting transcript for key discussion topics..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_01",
      "signature": "sig_call_01"
    },
    {
      "type": "processing_result",
      "call_id": "call_01",
      "signature": "sig_result_01"
    },
    {
      "type": "thought",
      "signature": "sig_thought_2",
      "summary": [
        {
          "type": "text",
          "text": "Loading visual frames to verify slide content..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_02",
      "signature": "sig_call_02"
    },
    {
      "type": "processing_result",
      "call_id": "call_02",
      "signature": "sig_result_02"
    },
    {
      "type": "thought",
      "signature": "sig_thought_3",
      "summary": [
        {
          "type": "text",
          "text": "Synthesizing answer from gathered evidence..."
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The three main arguments presented in the lecture are..."
        }
      ]
    }
  ]
}
```

### שימוש במצבי עיבוד שונים בסרטונים שונים

אפשר להגדיר מצבי עיבוד שונים לכל סרטון באותה בקשה:

### Python

```
from google import genai

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": lecture.uri,
            "mime_type": lecture.mime_type,
            "processing": "agentic"  # Use agentic video understanding
        },
        {
            "type": "video",
            "uri": experiment.uri,
            "mime_type": experiment.mime_type,
            "processing": "static"  # Use static processing
        },
        {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" }
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" }
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: lecture.uri,
      mime_type: lecture.mimeType,
      processing: "agentic" // Use agentic video understanding
    },
    {
      type: "video",
      uri: experiment.uri,
      mime_type: experiment.mimeType,
      processing: "static" // Use static processing
    },
    { type: "text", text: "Compare the lecture content with the experiment results." }
  ]
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${lecture_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {
        "type": "video",
        "uri": "'${experiment_uri}'",
        "mime_type": "video/mp4",
        "processing": "static"
      },
      {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ]
  }' 2> /dev/null
```

### שיחות וידאו רב-שלביות

ההקשר של הסרטון נשמר לאורך כל התורות בשיחה. כשמשתמשים בעיבוד מבוסס-סוכן:

- **מצב Stateful** (שימוש ב-`previous_interaction_id`): השרת שומר את ההקשר של הסרטון. אין צורך בטיפול נוסף.
- **מצב בלי שמירת מצב** (באמצעות `step_list`): במצב בלי שמירת מצב, התגובה כוללת את השלבים `processing_call` ו-`processing_result` שמקודדים את ההקשר של הסרטון. כדי לשמור על ההקשר של הסרטון, צריך לכלול את כל השלבים מהתשובה בבקשה הבאה שלך `step_list`. למרות שכרגע השמטה שלהם לא מחזירה שגיאת API, ההקשר של הסרטון אובד, ואיכות התשובות לשאלות המשך יורדת באופן משמעותי. שימו לב שהשלבים שמוחזרים ונשלחים בבקשות הבאות נכללים בספירת האסימונים של הקלט.

## הפניה לחותמות זמן בתוכן

אתם יכולים לשאול שאלות על נקודות זמן ספציפיות בסרטון באמצעות חותמות זמן בתבנית `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Summarize the key events in this video.").build();
Content videoContent =
    VideoContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/video/pixel8.mp4")
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## חילוץ תובנות מפורטות מסרטון

מודלים של Gemini מציעים יכולות מתקדמות להבנת תוכן וידאו על ידי עיבוד מידע מזרמי **האודיו והווידאו**. התכונה הזו מאפשרת לחלץ מגוון רחב של פרטים, כולל יצירת תיאורים של מה שקורה בסרטון ומענה לשאלות לגבי התוכן שלו.

בתיאורים חזותיים, המודל דוגם את הסרטון בקצב של **פרים אחד לשנייה** (FPS). קצב הדגימה הזה מתאים לרוב התוכן, אבל חשוב לזכור שהוא עלול לפספס פרטים בסרטונים עם תנועה מהירה או שינויי סצנה מהירים.

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Summarize the key events in this video.").build();
Content videoContent =
    VideoContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/video/pixel8.mp4")
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## התאמה אישית של עיבוד הסרטון

אתם יכולים להתאים אישית את עיבוד הסרטון ב-Gemini API על ידי הגדרת מרווחי חיתוך או על ידי מתן דגימה מותאמת אישית של קצב הפריימים. אפשרויות ההתאמה האישית האלה נתמכות רק כשמעבדים את הסרטון במצב `"static"`.

### הגדרת מרווחי זמן לחיתוך

כדי לחתוך סרטון, מציינים את `start_offset` ואת `end_offset` באובייקט ההגדרה `processing`.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "start_offset": 1200,
                "end_offset": 1500,
            },
        },
        {"type": "text", "text": "Summarize this section of the video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        start_offset: 1200,
        end_offset: 1500,
      },
    },
    { type: "text", text: "Summarize this section of the video." },
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "start_offset": 1200,
          "end_offset": 1500
        }
      },
      {"type": "text", "text": "Summarize this section of the video."}
    ]
  }' 2> /dev/null
```

### הגדרת קצב פריימים בהתאמה אישית

כדי להגדיר דגימה של קצב פריימים בהתאמה אישית, מעבירים ארגומנט `fps` באובייקט ההגדרות `processing`.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "fps": 0.5,  # Sample 1 frame every 2 seconds
            },
        },
        {"type": "text", "text": "Describe the scene changes in this video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        fps: 0.5, // Sample 1 frame every 2 seconds
      },
    },
    { type: "text", text: "Describe the scene changes in this video." },
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "fps": 0.5
        }
      },
      {"type": "text", "text": "Describe the scene changes in this video."}
    ]
  }' 2> /dev/null
```

## פורמטים נתמכים של וידאו

‫Gemini תומך בסוגי ה-MIME הבאים של פורמטים של סרטונים:

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## פרטים טכניים על סרטונים

- **מודלים והקשר נתמכים**: כל המודלים של Gemini יכולים לעבד נתוני וידאו.
  - מודלים עם חלון הקשר של מיליון טוקנים יכולים לעבד סרטונים באורך של עד 3 שעות כברירת מחדל (ברזולוציית מדיה נמוכה), או באורך של עד שעה ברזולוציית מדיה גבוהה.
- **מצבי עיבוד**: מודלים של Gemini 3.8 Flash,‏ 3.7 Flash,‏ 3.6 Flash,‏ 3.5 Flash Lite ומודלים מתקדמים יותר תומכים בשני מצבי עיבוד וידאו:
  - **סטטי**: הפריימים מחולצים בקצב של 1 FPS ומוצבים בהקשר (ברירת המחדל לכל המודלים). האודיו מעובד בקצב של 1Kbps (ערוץ יחיד).
    חותמות הזמן מתווספות כל שנייה. הכי מתאים לקליפים קצרים או כשכל פריים חשוב (למשל, בדיקה של פריים אחרי פריים). שימו לב שרצפים של פעולות מהירות עלולים לאבד פרטים בגלל קצב הדגימה של 1 FPS.
  - **מבוסס-סוכן**: המודל מנווט בסרטון באופן דינמי, וטוען תמליל, פריימים או אודיו על פי דרישה. השימוש בשיטה הזו מאפשר לצמצם את מספר הטוקנים בתוכן ארוך ב-88% לפחות, אבל יכול להיות שהניווט יגרום לעלייה קלה בזמן עד לטוקן הראשון (TTFT) בקליפים קצרים (עד 5 דקות) בגלל תהליכי חשיבה פנימיים ושימוש בכלי הלוך ושוב לפני תחילת היצירה. הכי מתאים לסרטונים ארוכים (LFV) כדי לבצע אופטימיזציה של עלויות הטוקנים ואיכות התשובות.
    התכונה נתמכת ב-Gemini 3.8 Flash,‏ 3.7 Flash,‏ 3.6 Flash ו-3.5 Flash Lite.
    פרטים נוספים זמינים במאמר בנושא [הבנת סרטונים באמצעות סוכנים](#agentic-video-understanding).
- **חישוב טוקנים (מצב סטטי)**: כל שנייה של סרטון עוברת טוקניזציה באופן הבא:
  - פריימים בודדים (נדגמים ב-1 FPS):
    - אם הערך של `media_resolution` מוגדר כנמוך, הפריימים עוברים טוקניזציה בשיעור של 66 טוקנים לכל פריים.
    - אחרת, הפריימים עוברים טוקניזציה בקצב של 258 טוקנים לכל פריים.
  - אודיו: 32 טוקנים לשנייה.
  - המטא-נתונים כלולים גם הם.
  - סה"כ: כ-100 טוקנים לשנייה של וידאו ברזולוציית מדיה (נמוכה) שמוגדרת כברירת מחדל, או כ-300 טוקנים לשנייה של וידאו ברזולוציית מדיה גבוהה.
- **חישוב אסימונים (מצב סוכן):** השימוש באסימונים משתנה בהתאם למורכבות התוכן ולאסטרטגיית הניווט של המודל. טוקנים של נימוקי ניווט שנוצרים במהלך חיפוש בסרטון נספרים כ**טוקנים של מחשבה** (`total_thought_tokens`), ואילו פריימים, אודיו ותמליל שנטענים לפי דרישה נספרים כטוקנים של שימוש בכלי (`total_tool_use_tokens`). בדרך כלל, עיבוד באמצעות סוכן משתמש בעד 88% פחות טוקנים כוללים מאשר עיבוד סטטי של תוכן ארוך, כי המודל טוען רק את התמליל או הפריימים או האודיו שהוא צריך כדי לענות על ההנחיה (ראו את [המדריך לטוקנים](https://ai.google.dev/gemini-api/docs/tokens?hl=he#video-token-usage)).
- **רזולוציית מדיה**: ב-Gemini 3 יש שליטה מדויקת בעיבוד של ראייה מולטימודאלית באמצעות הפרמטר `media_resolution`. הפרמטר
  `media_resolution` קובע את **המספר המקסימלי של טוקנים
  שהוקצו לכל תמונה או פריים של סרטון קלט.** רזולוציות גבוהות יותר משפרות את היכולת של המודל לקרוא טקסט קטן או לזהות פרטים קטנים, אבל מגדילות את השימוש בטוקנים ואת זמן האחזור. הפרמטרים `media_resolution` ו-`processing` הם בלתי תלויים: אפשר להגדיר את שניהם באותו קלט וידאו.

פרטים נוספים על חישוב אסימונים זמינים במדריך בנושא [אסימונים](https://ai.google.dev/gemini-api/docs/tokens?hl=he).

- **פורמט חותמת הזמן**: כשמפנים לרגעים ספציפיים בסרטון בהנחיה, צריך להשתמש בפורמט `MM:SS` (למשל, `01:15` לציון דקה ו-15 שניות).
- **מיקום ההנחיה**: אם משלבים טקסט וסרטון אחד, צריך למקם את הנחיית הטקסט *אחרי* חלק הסרטון במערך `input`.
- **פסק זמן לבקשות ארוכות**: בסרטונים שנדרש להם זמן עיבוד ממושך או ניתוח מורכב בכמה שלבים, כדאי להשתמש בסטרימינג (`stream=True`) או בהרצה ברקע (`background=True`). בקשות סינכרוניות שאינן סטרימינג, שמתבצעים בהן ניסיונות חוזרים בעורף המערכת בביקוש גבוה, עשויות לחרוג מחלונות התוקף של החיבור או של אסימון האימות, מה שעלול להוביל לשגיאות לא צפויות מסוג `401 Unauthorized` או לשגיאות של פסק זמן.
  הסטרימינג שומר על החיבור פעיל ומציג את שלבי הביניים של החשיבה הרציונלית ואת ההתקדמות של קריאות הכלים.

## המאמרים הבאים

- [רזולוציית המדיה](https://ai.google.dev/gemini-api/docs/media-resolution?hl=he): שליטה ברזולוציה של פריימים של סרטונים כדי לאזן בין איכות לבין שימוש באסימונים.
- [טוקנים](https://ai.google.dev/gemini-api/docs/tokens?hl=he): הסבר על האופן שבו תוכן וידאו עובר טוקניזציה במצבי עיבוד סטטיים ודינמיים.
- [הוראות למערכת](https://ai.google.dev/gemini-api/docs/text-generation?hl=he#system-instructions):
  ההוראות למערכת מאפשרות לכם לכוון את התנהגות המודל בהתאם לצרכים הספציפיים ולתרחישי השימוש שלכם.
- ‫[Files API](https://ai.google.dev/gemini-api/docs/files?hl=he): מידע נוסף על העלאה וניהול של קבצים לשימוש עם Gemini.
- [אסטרטגיות להנפקת הנחיות לקבצים](https://ai.google.dev/gemini-api/docs/files?hl=he#prompt-guide): Gemini API תומך בהנפקת הנחיות עם נתוני טקסט, תמונה, אודיו ווידאו, שנקראות גם הנחיות מולטימודאליות.
- [הנחיות בנושא בטיחות](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=he): לפעמים מודלים של AI גנרטיבי יוצרים פלטים לא צפויים, כמו פלטים לא מדויקים, מוטים או פוגעניים. עיבוד תמונה (Post Processing) והערכה אנושית חיוניים כדי לצמצם את הסיכון לנזק שעלול להיגרם מהתוצאות האלה.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-12 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-12 (שעון UTC)."],[],[]]
