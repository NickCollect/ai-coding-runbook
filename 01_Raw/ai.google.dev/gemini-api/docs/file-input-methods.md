---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=he
fetched_at: 2026-08-17T02:22:39.685411+00:00
title: "\u05e9\u05d9\u05d8\u05d5\u05ea \u05e7\u05dc\u05d8 \u05e9\u05dc \u05e7\u05d1\u05e6\u05d9\u05dd \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# שיטות קלט של קבצים

במדריך הזה מוסברות הדרכים השונות שבהן אפשר לכלול קובצי מדיה כמו תמונות, אודיו, וידאו ומסמכים כששולחים בקשות ל-Gemini API.
השיטות החדשות נתמכות בכל נקודות הקצה (endpoints) של Gemini API, כולל Batch, ‏ Interactions ו-Live API.
השיטה המתאימה תלויה בגודל הקובץ, במיקום שבו הנתונים מאוחסנים ובתדירות שבה אתם מתכננים להשתמש בקובץ.

הדרך הכי פשוטה לכלול קובץ כקלט היא לקרוא קובץ מקומי ולכלול אותו בהנחיה. בדוגמה הבאה אפשר לראות איך קוראים קובץ PDF מקומי. בשיטה הזו, קובצי PDF מוגבלים ל-50MB. רשימה מלאה של סוגי קבצים ומגבלות מופיעה [בטבלת ההשוואה של שיטות הקלט](#method-comparison).

### Python

```
from google import genai
import pathlib
import base64

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "data": base64.b64encode(filepath.read_bytes()).decode('utf-8'), "mime_type": "application/pdf"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = 'my_local_file.pdf';

    const interaction = await client.interactions.create({
        model: "gemini-3.6-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: fs.readFileSync(filePath).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Summarize this document"},
      {
        "type": "document",
        "data": "'${B64_CONTENT}'",
        "mime_type": "application/pdf"
      }
    ]
  }'
```

## השוואה בין שיטות קלט

בטבלה הבאה מוצגת השוואה בין כל שיטות הקלט, עם מגבלות הקבצים והתרחישים המומלצים לשימוש. שימו לב שמגבלת גודל הקובץ עשויה להשתנות בהתאם לסוג הקובץ ולמודל או לטוקנייזר שמשמשים לעיבוד הקובץ.

| שיטה | הכי טוב עבור | גודל קובץ מקסימלי | התמדה |
| --- | --- | --- | --- |
| **נתונים מוטבעים** | בדיקה מהירה, קבצים קטנים, אפליקציות בזמן אמת. | ‫100MB לכל בקשה או מטען ייעודי   (**50MB לקובצי PDF**) | ללא (נשלח עם כל בקשה) |
| **העלאה דרך File API** | קבצים גדולים, קבצים שנעשה בהם שימוש כמה פעמים. | ‫2GB לכל קובץ,   עד 20GB לכל פרויקט | ‫48 שעות |
| **רישום של URI של GCS ב-File API** | קבצים גדולים שכבר נמצאים ב-Google Cloud Storage, קבצים שנמצאים בשימוש כמה פעמים. | ‫2GB לכל קובץ, ללא מגבלות אחסון כוללות | ללא (מאוחזר לכל בקשה). רישום חד-פעמי יכול להעניק גישה למשך 30 ימים לכל היותר. |
| **כתובות URL חיצוניות** | נתונים ציבוריים או נתונים בדליים בענן (AWS, ‏ Azure, ‏ GCS) בלי להעלות אותם מחדש. | ‫100MB לכל בקשה או מטען ייעודי (payload) | ללא (מאוחזר לפי בקשה) |

## נתונים מוטבעים

בקובצי PDF או בקבצים קטנים יותר (עד 100MB, או עד 50MB לקובצי PDF), אפשר להעביר את הנתונים ישירות במטען הייעודי (payload) של הבקשה. זו השיטה הפשוטה ביותר לבדיקות מהירות או לאפליקציות שמטפלות בנתונים זמניים בזמן אמת. אפשר לספק נתונים כמחרוזות מקודדות ב-Base64 או על ידי קריאה ישירה של קבצים מקומיים.

דוגמה לקריאה מקובץ מקומי מופיעה בתחילת הדף הזה.

### אחזור מכתובת URL

אפשר גם לאחזר קובץ מכתובת URL, להמיר אותו לבייטים ולכלול אותו בקלט.

### Python

```
from google import genai
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "document", "data": base64.b64encode(doc_data).decode('utf-8'), "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl)
      .then((response) => response.arrayBuffer());

    const interaction = await client.interactions.create({
        model: "gemini-3.6-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: Buffer.from(pdfResp).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### REST

```
DOC_URL="https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
PROMPT="Summarize this document"
DISPLAY_NAME="base64_pdf"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

# Check for FreeBSD base64 and set flags accordingly
if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

# Base64 encode the PDF
ENCODED_PDF=$(base64 $B64FLAGS "${DISPLAY_NAME}.pdf")

# Create JSON payload file
cat <<EOF > payload.json
{
"model": "gemini-3.6-flash",
"input": [
{"type": "document", "data": "${ENCODED_PDF}", "mime_type": "application/pdf"},
{"type": "text", "text": "${PROMPT}"}
]
}
EOF

# Generate content using interactions
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## Gemini File API

ממשק File API מיועד לקבצים גדולים יותר (עד 2GB) או לקבצים שרוצים להשתמש בהם בכמה בקשות.

### העלאה רגילה של קבצים

העלאת קובץ מקומי ל-Gemini API. קבצים שמועלים בדרך הזו מאוחסנים באופן זמני (למשך 48 שעות) ומעובדים כדי שהמודל יוכל לאחזר אותם ביעילות.

### Python

```
from google import genai

client = genai.Client()

doc_file = client.files.upload(file="path/to/your/sample.pdf")
prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "uri": doc_file.uri, "mime_type": doc_file.mime_type}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
  const filePath = "path/to/your/sample.pdf";

  const myfile = await client.files.upload({
    file: filePath,
    config: { mime_type: "application/pdf" },
  });

  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: [
        { type: "text", text: prompt },
        { type: "document", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
FILE_PATH="path/to/sample.pdf"
MIME_TYPE=$(file -b --mime-type "${FILE_PATH}")
NUM_BYTES=$(wc -c < "${FILE_PATH}")
DISPLAY_NAME=DOCUMENT

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -D "${tmp_header_file}" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
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
  --data-binary "@${FILE_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)

# Now use in an interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.6-flash",
      "input": [
        {"type": "text", "text": "Summarize this document"},
        {"type": "document", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }'
```

### רישום קבצים ב-Google Cloud Storage

אם הנתונים שלכם כבר נמצאים ב-Google Cloud Storage, אתם לא צריכים להוריד אותם ולהעלות אותם מחדש. אפשר לרשום אותו ישירות באמצעות File API.

1. הענקת גישה לכל קטגוריה ל**סוכן השירות**

   1. מפעילים את Gemini API בפרויקט בענן ב-Google Cloud.
   2. יוצרים את סוכן השירות:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **נותנים לסוכן השירות של Gemini API הרשאות** לקריאה של קטגוריות האחסון.

      המשתמש צריך להקצות את `Storage Object Viewer`
      [תפקיד ה-IAM](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=he#storage.objectViewer) לסוכן השירות הזה בקטגוריות האחסון הספציפיות שהוא מתכוון להשתמש בהן.

   הגישה הזו לא פגה כברירת מחדל, אבל אפשר לשנות את זה בכל שלב. אפשר גם להשתמש בפקודות של [Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=he) כדי להעניק הרשאות.
2. אימות השירות

   **דרישות מוקדמות**

   - הפעלת ה-API
   - יוצרים חשבון שירות או סוכן עם ההרשאות המתאימות.

   קודם צריך לבצע אימות בתור השירות שיש לו הרשאות צפייה באובייקט אחסון. אופן הגבייה תלוי בסביבה שבה יפעל קוד ניהול הקבצים.

   **מחוץ ל-Google Cloud**

   אם הקוד שלכם מורץ מחוץ ל-Google Cloud, למשל מהמחשב, אתם יכולים להוריד את פרטי הכניסה לחשבון מ-Google Cloud Console באמצעות השלבים הבאים:

   1. עוברים אל [מסוף חשבון השירות](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=he).
   2. בוחרים את חשבון השירות הרלוונטי.
   3. בוחרים בכרטיסייה **Keys** ואז באפשרות **Add key, Create new key**.
   4. בוחרים את סוג המפתח **JSON** ורושמים את המיקום במחשב שאליו הקובץ הורד.

   פרטים נוספים זמינים במאמרי העזרה הרשמיים של Google Cloud בנושא [ניהול מפתחות של חשבונות שירות](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=he).

   אחר כך משתמשים בפקודות הבאות כדי לבצע אימות. הפקודות האלה מניחות שקובץ חשבון השירות נמצא בספרייה הנוכחית, ושמו `service-account.json`.

   ### Python

   ```
   from google.oauth2.service_account import Credentials

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   SERVICE_ACCOUNT_FILE = 'service-account.json'

   credentials = Credentials.from_service_account_file(
       SERVICE_ACCOUNT_FILE,
       scopes=GCS_READ_SCOPES
   )
   ```

   ### JavaScript

   ```
   const { GoogleAuth } = require('google-auth-library');

   const GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ];

   const SERVICE_ACCOUNT_FILE = 'service-account.json';

   const auth = new GoogleAuth({
     keyFile: SERVICE_ACCOUNT_FILE,
     scopes: GCS_READ_SCOPES
   });
   ```

   ### CLI

   ```
   gcloud auth application-default login \
     --client-id-file=service-account.json \
     --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only'
   ```

   **ב-Google Cloud**

   אם אתם מריצים את האפליקציה ישירות ב-Google Cloud, למשל באמצעות [פונקציות של Cloud Run](https://cloud.google.com/functions?hl=he) או [מכונה של Compute Engine](https://cloud.google.com/products/compute?hl=he), יהיו לכם פרטי כניסה מרומזים, אבל תצטרכו לבצע אימות מחדש כדי להעניק את ההיקפים המתאימים.

   ### Python

   הקוד הזה מניח שהשירות פועל בסביבה שבה אפשר לקבל [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=he) באופן אוטומטי, כמו Cloud Run או Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   הקוד הזה מניח שהשירות פועל בסביבה שבה אפשר לקבל [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=he) באופן אוטומטי, כמו Cloud Run או Compute Engine.

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

   ### CLI

   זוהי פקודה אינטראקטיבית. בשירותים כמו Compute Engine, אפשר לצרף היקפי הרשאות לשירות הפועל ברמת ההגדרה. דוגמה מופיעה ב[מסמכי חשבון השירות שמנוהל על ידי משתמש](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=he#using).

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. רישום קבצים (Files API)

   משתמשים ב-Files API כדי לרשום קבצים וליצור נתיב Files API שאפשר להשתמש בו ישירות ב-Gemini API.

   ### Python

   ```
   from google import genai

   client = genai.Client(credentials=credentials)

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
   )
   prompt = "Summarize this file."

   for f in registered_gcs_files.files:
     print(f.name)
     interaction = client.interactions.create(
       model="gemini-3.6-flash",
       input=[
         {"type": "text", "text": prompt},
         {"type": "document", "uri": f.uri, "mime_type": f.mime_type}
       ],
     )
     print(interaction.output_text)
   ```

   ### JavaScript

   ```
   import { GoogleGenAI } from "@google/genai";

   const ai = new GoogleGenAI({ auth: auth });

   async function main() {
       const registeredGcsFiles = await ai.files.registerFiles({
           uris: ["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
       });

       const prompt = "Summarize this file.";

       for (const file of registeredGcsFiles.files) {
           console.log(file.name);
           const interaction = await ai.interactions.create({
               model: "gemini-3.6-flash",
               input: [
                   { type: "text", text: prompt },
                   { type: "document", uri: file.uri, mime_type: file.mimeType }
               ]
           });

           console.log(interaction.output_text);
       }
   }

   main();
   ```

   ### CLI

   ```
   access_token=$(gcloud auth application-default print-access-token)
   project_id=$(gcloud config get-value project)
   curl -X POST https://generativelanguage.googleapis.com/v1beta/files:register \
       -H 'Content-Type: application/json' \
       -H "Authorization: Bearer ${access_token}" \
       -H "x-goog-user-project: ${project_id}" \
       -d '{"uris": ["gs://bucket/object1", "gs://bucket/object2"]}'
   ```

## כתובות URL חיצוניות מסוג HTTP / כתובות URL חתומות

אפשר להעביר כתובות URL מסוג HTTPS שנגישות לכולם או כתובות URL חתומות מראש ישירות בבקשה. ‫Gemini API יאחזר את התוכן באופן מאובטח במהלך העיבוד.
האפשרות הזו מתאימה לקבצים בגודל של עד 100MB שאתם לא רוצים להעלות מחדש.

### Python

```
from google import genai

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "document", "uri": uri, "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: [
      { type: "document", uri: uri, mime_type: "application/pdf" },
      { type: "text", text: "summarize this file" }
    ]
  });

  console.log(interaction.output_text);
}

main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "model": "gemini-3.6-flash",
          "input": [
            {"type": "text", "text": "Summarize this pdf"},
            {
              "type": "document",
              "uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf",
              "mime_type": "application/pdf"
            }
          ]
        }'
```

### נגישות

מוודאים שכתובות ה-URL שציינתם לא מובילות לדפים שנדרשת בהם התחברות או לדפים שמוגנים על ידי חומת תשלום. במסדי נתונים פרטיים, חשוב לוודא שאתם יוצרים כתובת URL חתומה עם הרשאות הגישה הנכונות ותאריך התפוגה הנכון.

### בדיקות אבטחה

המערכת מבצעת בדיקה של ניהול התוכן בכתובת ה-URL כדי לוודא שהיא עומדת בסטנדרטים של בטיחות ומדיניות. אם כתובת ה-URL תיכשל בבדיקה הזו, תקבלו הודעה
`url_retrieval_status` של `URL_RETRIEVAL_STATUS_UNSAFE`.

### סוגי התוכן הנתמכים

הרשימה הזו של סוגי קבצים נתמכים ומגבלות נועדה לספק הנחיות ראשוניות, והיא לא מקיפה. קבוצת הסוגים הנתמכים בפועל עשויה להשתנות, והיא תלויה במודל הספציפי ובגרסת הטוקנייזר שנמצאים בשימוש. סוגים שלא נתמכים יגרמו לשגיאה.
בנוסף, אחזור תוכן עבור סוגי הקבצים האלה תומך רק בכתובות URL שזמינות לכל.

#### סוגים של קובצי טקסט

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### סוגי קבצים של אפליקציות

- `application/json`
- `application/pdf`

#### סוגים של קובצי תמונות

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### סוגים של קובצי וידאו

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## שיטות מומלצות

- **בחירת השיטה הנכונה:** משתמשים בנתונים מוטבעים לקבצים קטנים וזמניים.
  כדאי להשתמש ב-File API לקבצים גדולים או לקבצים שמשתמשים בהם לעיתים קרובות. שימוש בכתובות URL חיצוניות לנתונים שכבר מתארחים באינטרנט.
- **צריך לציין סוגי MIME:** חשוב לספק תמיד את סוג ה-MIME הנכון של נתוני הקובץ כדי להבטיח עיבוד תקין.
- **טיפול בשגיאות:** כדאי להטמיע טיפול בשגיאות בקוד כדי לנהל בעיות פוטנציאליות כמו כשלים ברשת, בעיות בגישה לקבצים או שגיאות ב-API.

## מגבלות

- מגבלות גודל הקובץ משתנות בהתאם לשיטה (ראו [טבלת השוואה](#method-comparison)) וסוג הקובץ.
- נתונים מוטמעים מגדילים את גודל המטען הייעודי (payload) של הבקשה.
- ההעלאות באמצעות File API הן זמניות והתוקף שלהן פג אחרי 48 שעות.
- הגודל של מטען ייעודי (payload) שמתקבל מכתובת URL חיצונית מוגבל ל-100MB, ויש תמיכה בסוגי תוכן ספציפיים.

## המאמרים הבאים

- אתם יכולים לנסות לכתוב פרומפטים מולטימודאליים משלכם באמצעות [Google AI Studio](http://aistudio.google.com/?hl=he).
- מידע על הוספת קבצים להנחיות זמין במדריכים בנושא [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=he), [אודיו](https://ai.google.dev/gemini-api/docs/audio?hl=he) ו[עיבוד מסמכים](https://ai.google.dev/gemini-api/docs/document-processing?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-30 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-30 (שעון UTC)."],[],[]]
