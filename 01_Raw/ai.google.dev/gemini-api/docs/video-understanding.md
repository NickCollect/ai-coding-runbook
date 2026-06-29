---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=he
fetched_at: 2026-06-29T05:38:15.823479+00:00
title: "\u05d4\u05d1\u05e0\u05ea \u05e1\u05e8\u05d8\u05d5\u05e0\u05d9\u05dd \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# הבנת סרטונים

> מידע על יצירת סרטונים זמין במדריך [Veo](https://ai.google.dev/gemini-api/docs/video?hl=he).

מודלים של Gemini יכולים לעבד סרטונים, וכך לאפשר למפתחים להשתמש בהם בתרחישי שימוש רבים ומתקדמים, שבדרך כלל נדרשים להם מודלים ספציפיים לתחום.
חלק מהיכולות של Gemini בתחום הראייה כוללות את האפשרות: לתאר, לפלח ולחלץ מידע מסרטונים, לענות על שאלות לגבי תוכן של סרטונים ולהתייחס לחותמות זמן ספציפיות בסרטון.

יש כמה דרכים להזין סרטונים כקלט ל-Gemini:

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
import base64
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.output_text);
}

await main();
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
      "model": "gemini-3.5-flash",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

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
    model='gemini-3.5-flash',
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
  model: "gemini-3.5-flash",
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
      "model": "gemini-3.5-flash",
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
    model='gemini-3.5-flash',
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
  model: "gemini-3.5-flash",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.5-flash",
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
- אפשר להעלות רק סרטונים שגלויים לכולם (לא סרטונים פרטיים או לא רשומים).

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

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## חילוץ תובנות מפורטות מסרטון

מודלים של Gemini מציעים יכולות מתקדמות להבנת תוכן וידאו על ידי עיבוד מידע מזרמי **האודיו והווידאו**. התכונה הזו מאפשרת לחלץ מגוון רחב של פרטים, כולל יצירת תיאורים של מה שקורה בסרטון ומענה לשאלות לגבי התוכן שלו.

לתיאורים חזותיים, המודל דוגם את הסרטון בקצב של **1 פריימים לשנייה** (FPS). שיעור הדגימה הזה מתאים לרוב סוגי התוכן, אבל חשוב לזכור שהוא עלול לפספס פרטים בסרטונים עם תנועה מהירה או שינויי סצנה מהירים.

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
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

- **מודלים נתמכים והקשר**: כל ממשקי Gemini יכולים לעבד נתוני וידאו.
  - מודלים עם חלון קשר של מיליון טוקנים יכולים לעבד סרטונים באורך של עד שעה ברזולוציית מדיה רגילה או באורך של עד 3 שעות ברזולוציית מדיה נמוכה.
- **עיבוד באמצעות File API**: כשמשתמשים ב-File API, הסרטונים מאוחסנים ב-1 פריימים לשנייה (FPS) והשמע מעובד ב-1Kbps (ערוץ יחיד).
  חותמות הזמן מתווספות כל שנייה.
  - המחירים האלה עשויים להשתנות בעתיד בעקבות שיפורים בהסקת המסקנות.
- **חישוב הטוקנים**: כל שנייה של סרטון עוברת טוקניזציה באופן הבא:
  - פריימים בודדים (נדגמים ב-1 FPS):
    - אם הערך של `media_resolution` מוגדר ל-low, הפריימים עוברים טוקניזציה בשיעור של 66 טוקנים לכל פרים.
    - אחרת, כל פריים עובר טוקניזציה ל-258 טוקנים.
  - אודיו: 32 טוקנים לשנייה.
  - המטא-נתונים כלולים גם הם.
  - סך הכול: כ-300 טוקנים לשנייה של וידאו ברזולוציית מדיה שמוגדרת כברירת מחדל, או 100 טוקנים לשנייה של וידאו ברזולוציית מדיה נמוכה.
- **רזולוציה בינונית**: ב-Gemini 3 יש שליטה מדויקת בעיבוד של ראייה מולטימודאלית באמצעות הפרמטר `media_resolution`. הפרמטר `media_resolution` קובע את **המספר המקסימלי של טוקנים שמוקצים לכל תמונה או פריים של סרטון קלט.**
  רזולוציות גבוהות יותר משפרות את היכולת של המודל לקרוא טקסט קטן או לזהות פרטים קטנים, אבל מגדילות את השימוש בטוקנים ואת זמן האחזור.

  פרטים נוספים על חישוב אסימונים זמינים במדריך בנושא [אסימונים](https://ai.google.dev/gemini-api/docs/tokens?hl=he).
- **פורמט חותמת הזמן**: כשמתייחסים לרגעים ספציפיים בסרטון בהנחיה, צריך להשתמש בפורמט `MM:SS` (למשל, `01:15` לציון דקה ו-15 שניות).
- **שיטות מומלצות:**

  - כדי לקבל תוצאות אופטימליות, מומלץ להשתמש רק בסרטון אחד בכל בקשת הנחיה.
  - אם משלבים טקסט וסרטון אחד, צריך למקם את הנחיית הטקסט *אחרי* החלק של הסרטון במערך `input`.
  - חשוב לדעת שרצפי פעולות מהירים עלולים לאבד פרטים בגלל קצב הדגימה של 1 FPS. במקרה הצורך, אפשר להאט את הקליפים האלה.

## המאמרים הבאים

במדריך הזה מוסבר איך להעלות קובצי וידאו וליצור פלט טקסט מקלט וידאו. מידע נוסף זמין במקורות המידע הבאים:

- [System instructions](https://ai.google.dev/gemini-api/docs/text-generation?hl=he#system-instructions):
  הוראות מערכת מאפשרות לכם לכוון את התנהגות המודל בהתאם לצרכים הספציפיים ולתרחישי השימוש שלכם.
- ‫[Files API](https://ai.google.dev/gemini-api/docs/files?hl=he): מידע נוסף על העלאה וניהול של קבצים לשימוש עם Gemini.
- [אסטרטגיות לכתיבת הנחיות לקבצים](https://ai.google.dev/gemini-api/docs/files?hl=he#prompt-guide): Gemini API תומך בכתיבת הנחיות עם נתוני טקסט, תמונה, אודיו ווידאו, שנקראות גם כתיבת הנחיות מולטי-מודאליות.
- [הנחיות בטיחות](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=he): לפעמים מודלים של AI גנרטיבי יוצרים תוצאות לא צפויות, כמו תוצאות לא מדויקות, מוטות או פוגעניות. כדי לצמצם את הסיכון לנזק שעלול להיגרם מהתוצאות האלה, חשוב לבצע עיבוד לאחר יצירת התוכן והערכה אנושית.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-06-22 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-06-22 (שעון UTC)."],[],[]]
