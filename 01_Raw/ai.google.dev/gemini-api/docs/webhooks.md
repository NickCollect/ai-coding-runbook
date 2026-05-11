---
source_url: https://ai.google.dev/gemini-api/docs/webhooks?hl=he
fetched_at: 2026-05-11T04:59:39.379513+00:00
title: "\u05ea\u05d2\u05d5\u05d1\u05d5\u05ea \u05dc\u05e4\u05e2\u05d5\u05dc\u05d4 \u05de\u05d0\u05ea\u05e8 \u05d0\u05d7\u05e8 (webhook) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# תגובות לפעולה מאתר אחר (webhook)

תגובות לפעולה מאתר אחר (webhook) מאפשרות ל-Gemini API לשלוח התראות בזמן אמת לשרת שלכם כשפעולות אסינכרוניות או פעולות ארוכות טווח (LRO) מסתיימות. השינוי הזה מייתר את הצורך לדגום את ה-API כדי לקבל עדכוני סטטוס, וכך מקטין את זמן הטעינה ואת התקורה.

אפשר להשתמש ב-Webhooks לפעולות כמו משימות [Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=he), [אינטראקציות](https://ai.google.dev/gemini-api/docs/interactions?hl=he) ו[יצירת סרטונים](https://ai.google.dev/gemini-api/docs/video?hl=he).

## איך זה עובד

במקום לבצע סקר `GET /operations` שוב ושוב כדי לבדוק אם משימה הסתיימה, אפשר להגדיר Webhooks של Gemini API כדי לשלוח בקשת HTTP POST לכתובת ה-URL של מאזין מיד כשמופעל אירוע.

‫Gemini API תומך בשתי דרכים להגדרת ווּבְהוּקים:

- ‫[**Static webhooks**](#static-webhooks): נקודות קצה ברמת הפרויקט שהוגדרו באמצעות [Gemini WebhookService API](https://ai.google.dev/api?hl=he). מתאים לשילובים גלובליים (לדוגמה, שליחת התראות ל-Slack, סנכרון של מסד נתונים וכו').
- [**וווב-הוקים דינמיים**](#dynamic-webhooks): שינויים ברמת הבקשה שמעבירים webhook URL במטען הייעודי (payload) של ההגדרה של קריאה ספציפית למשרות. הסוג הזה אידיאלי להפניית משימות ספציפיות לנקודות קצה ייעודיות.

## Webhooks סטטיים

הרישום של וווב-הוקים סטטיים מתבצע עבור [פרויקט](https://ai.google.dev/gemini-api/docs/api-key?hl=he#google-cloud-projects) שלם, והם מופעלים כשמתרחש אירוע תואם.

### יצירת webhook

אפשר ליצור נקודות קצה באמצעות ה-SDK או ה-REST API.

**חשוב**: כשיוצרים webhook, ה-API מחזיר **סוד חתימה**
**רק פעם אחת**. כדי לאמת חתימות בהמשך, צריך לאחסן את המפתח הזה בצורה מאובטחת (למשל, במשתני הסביבה). אם תאבדו את הסוד לחתימה, תצטרכו [לשנות](#rotate-signing-secret) אותו.

### Python

```
from google import genai

client = genai.Client()

webhook = client.webhooks.create(
    name="MyBatchWebhook",
    subscribed_events=["batch.succeeded", "batch.failed"],
    uri="https://my-api.com/gemini-callback",
)

# Store webhook.new_signing_secret securely
webhook_secret = webhook.new_signing_secret
print(f"Created webhook: {webhook.name}, {webhook.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createWebhook() {
  const webhook = await client.webhooks.create({
    name: "MyBatchWebhook",
    subscribed_events: ["batch.succeeded", "batch.failed"],
    uri: "https://my-api.com/gemini-callback",
  });

  // Store webhook.signingSecret securely
  const webhookSecret = webhook.new_signing_secret;
  console.log(`Created webhook: ${webhook.name}, ${webhook.id}`);
}

createWebhook();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/webhooks" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "name": "MyBatchWebhook",
    "uri": "https://my-api.com/gemini-callback",
    "subscribed_events": ["batch.succeeded", "batch.failed"]
  }'
```

פרטים על הגדרת השרת לקבלת נתונים מופיעים בקטע [טיפול בבקשות של webhook](#handle-webhook-requests).

### קבלת webhook

אחזור פרטים על webhook ספציפי לפי שם המשאב שלו.

### Python

```
from google import genai

client = genai.Client()

webhook = client.webhooks.get(id="<your_webhook_id>")

print(f"Webhook: {webhook.name}")
print(f"URI: {webhook.uri}")
print(f"Events: {webhook.subscribed_events}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI(); // Assumes process.env.GEMINI_API_KEY is set

async function getWebhook() {
  const webhook = await client.webhooks.get("<your_webhook_id>");

  console.log(`Webhook: ${webhook.name}`);
  console.log(`URI: ${webhook.uri}`);
  console.log(`Events: ${webhook.subscribed_events}`);
}

getWebhook();
```

### REST

```
curl -X GET \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### הצגת רשימה של webhooks

הצגת רשימה של כל ה-webhook שהוגדרו בפרויקט הנוכחי, עם אפשרות להצגה בדפים.

### Python

```
from google import genai

client = genai.Client()

webhooks = client.webhooks.list()

for wh in webhooks:
    print(f"{wh.id}: {wh.name} -> {wh.uri}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function listWebhooks() {
  const webhooks = await client.webhooks.list();

  for (const wh of webhooks) {
    console.log(`${wh.id}: ${wh.name} -> ${wh.uri}`);
  }
}

listWebhooks();
```

### REST

```
curl -X GET \
  "https://generativelanguage.googleapis.com/v1/webhooks" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### עדכון webhook

עדכון של מאפיינים של webhook קיים, כמו השם לתצוגה, ה-URI של היעד או האירועים שנרשמו.

### Python

```
from google import genai

client = genai.Client()

updated_webhook = client.webhooks.update(
    id="<your_webhook_id>",
    subscribed_events=["batch.succeeded", "batch.failed", "batch.cancelled"],
)

print(f"Updated webhook: {updated_webhook.name}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function updateWebhook() {
  const updatedWebhook = await client.webhooks.update(
    "<your_webhook_id>",
    {
      subscribed_events: ["batch.succeeded", "batch.failed", "batch.cancelled"],
    }
  );

  console.log(`Updated webhook: ${updatedWebhook.name}`);
}

updateWebhook();
```

### REST

```
curl -X PATCH \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "subscribed_events": ["batch.succeeded", "batch.failed", "batch.cancelled"]
  }'
```

### מחיקת webhook

הסרה של נקודת קצה של webhook מהפרויקט. הפעולה הזו תפסיק את העברת האירועים העתידיים לנקודת הקצה הזו.

### Python

```
from google import genai

client = genai.Client()

client.webhooks.delete(id="<your_webhook_id>")

print("Webhook deleted.")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function deleteWebhook() {
  await client.webhooks.delete("<your_webhook_id>");

  console.log("Webhook deleted.");
}

deleteWebhook();
```

### REST

```
curl -X DELETE \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### סיבוב של סוד חתימה

סיבוב של ערך ה-Secret לחתימה של webhook. אתם יכולים להגדיר אם סודות שהיו פעילים בעבר יבוטלו באופן מיידי או אחרי תקופת חסד של 24 שעות.

**חשוב**: הסוד החדש לחתימה מוחזר **רק פעם אחת** בזמן הרוטציה. חשוב לשמור אותו במקום בטוח לפני שמעדכנים את לוגיקת האימות.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.webhooks.rotate_signing_secret(
    id="<your_webhook_id>",
    revocation_behavior="REVOKE_PREVIOUS_SECRETS_AFTER_H24",
)

# Store response.secret securely, then update your server's verification config
print("New signing secret generated. Update your server configuration.")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function rotateSigningSecret() {
  const response = await client.webhooks.rotateSigningSecret(
    "<your_webhook_id>",
    {
      revocation_behavior: "REVOKE_PREVIOUS_SECRETS_AFTER_H24",
    }
  );

  // Store response.secret securely, then update your server's verification config
  console.log("New signing secret generated. Update your server configuration.");
}

rotateSigningSecret();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>/rotate_secret" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "revocation_behavior": "REVOKE_PREVIOUS_SECRETS_AFTER_H24"
  }'
```

### טיפול בבקשות webhook בשרת

כשמתרחש אירוע שנרשמתם לקבלת עדכונים לגביו, כתובת ה-URL של ה-webhook תקבל בקשת HTTP POST. נקודת הקצה צריכה להגיב עם קוד סטטוס 2xx תוך כמה שניות כדי למנוע ניסיון חוזר. כדי להבטיח את המסירה, Gemini API מבצע אוטומטית ניסיון חוזר של בקשות שנכשלו למשך 24 שעות באמצעות השהיה מעריכית לפני ניסיון חוזר (exponential backoff).

‫Gemini פועל בהתאם למפרט [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) לגבי כותרות אבטחה. מאמתים את מטען הנתונים בשרת באמצעות החתימות של הכותרת החתומה והסוד הסטטי לחתימה ששמור אצלכם. מידע על מטען הייעודי זמין בקטע [מעטפת ה-Webhook](#webhook-envelope).

דוגמה לשימוש ב-Flask בשביל מאזין HTTP:

### Python

```
# pip install flask standardwebhooks
import os
from flask import Flask, request, jsonify
# Standard verification wrapper for Standard Webhook Headers
from standardwebhooks.webhooks import Webhook, WebhookVerificationError

app = Flask(__name__)

SIGNING_SECRET = os.environ.get('WEBHOOK_SIGNING_SECRET')

@app.route('/gemini-callback', methods=['POST'])
def gemini_callback():
    payload = request.get_data(as_text=True)
    headers = request.headers

    try:
        wh = Webhook(SIGNING_SECRET)
        event = wh.verify(payload, headers)
    except WebhookVerificationError as e:
        return jsonify({"error": "Signature invalid"}), 400

    # Process thin payload contents
    if event.get("type") == "batch.succeeded":
        print(f"Batch completed! ID: {event["data"]["id"]}")
        if event["data"].get("output_file_uri"):
            # For batch jobs with input file
            print(f"Batch file: {event["data"]["output_file_uri"]}")
    elif (event.type == "video.generated"):
        print(f"Video generated! URI: {event["data"]["output_file_uri"]}")

    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(port=8000)
```

### JavaScript

```
// npm install standardwebhooks
import { Webhook } from "standardwebhooks";
import express from "express";

const app = express();
const client = new GoogleGenAI({ webhookSecret: process.env.WEBHOOK_SIGNING_SECRET });

// Don't use express.json() because signature verification needs the raw text body
app.use(express.text({ type: "application/json" }));

app.post("/gemini-callback", async (req, res) => {
  const payload = await req.text();
        const headers: Record<string, string> = {};
        req.headers.forEach((value, key) => {
            headers[key] = value;
        });

        try {
            const wh = new Webhook(process.env.WEBHOOK_SIGNING_SECRET);
            const event = wh.verify(payload, headers) as Record<string, any>;
    console.log(`Event type: ${event.type}, data: ${JSON.stringify(event.data)}`);

            // Process thin payload contents
            if (event.type === "batch.succeeded") {
                console.log(`Batch completed! ID: ${event.data.id}`);
                if (event.data.output_file_uri) {
                    // For batch jobs with input file
                    console.log(`Batch file: ${event.data.output_file_uri}`);
                }
            } else if (event.type === "video.generated") {
                console.log(`Video generated! URI: ${event.data.output_file_uri}`);
            }

            res.status(200).json({ status: "received" });
        } catch (e) {
            console.error("Webhook verification failed:", e);
            res.status(400).send("Invalid signature");
        }
});

app.listen(8000, () => {
  console.log("Webhook server is running on port 8000");
});
```

## ‫webhooks דינמיים

בעזרת וווב-הוקים דינמיים אפשר לקשר נקודת קצה של וווב-הוק ל**הגדרת בקשה ספציפית**, וזה אידיאלי לתורים של תיאום בין נציגים. ב-webhooks דינמיים נעשה שימוש בחתימות JWKS של מפתח ציבורי אסימטרי במקום בסודות סימטריים.

### שליחת בקשה דינמית

מוסיפים `webhook_config` כשמפעילים עבודה אסינכרונית (למשל, יצירת Batch).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

file_batch_job = client.batches.create(
    model="gemini-3-flash-preview",
    src="files/uploaded_file_id",
    config={
        "display_name": "My Setup",
        "webhook_config": {
            "uris": ["https://my-api.com/gemini-webhook-dynamic"],
            "user_metadata":{"job_group": "nightly-eval", "priority": "high"}
        }
    }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createBatchWithWebhook() {
  const fileBatchJob = await client.batches.create({
    model: "gemini-3-flash-preview",
    src: "files/uploaded_file_id",
    config: {
      displayName: "My Setup",
      webhookConfig: {
        uris: ["https://my-api.com/gemini-webhook-dynamic"],
        user_metadata: {"job_group": "nightly-eval", "priority": "high"}
      },
    },
  });
}
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3-flash-preview:batchCreate" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "src": "files/uploaded_file_id",
    "config": {
      "display_name": "My Setup",
      "webhook_config": {
        "uris": ["https://my-api.com/gemini-webhook-dynamic"],
        "user_metadata": {"job_group": "nightly-eval", "priority": "high"}
      }
    }
  }'
```

### אימות חתימות דינמיות (JWKS)

בקשות דינמיות של webhook פולטות חתימה של JSON Web Token‏ (JWT). המאזין צריך לחלץ את החתימה ולאמת אותה באמצעות [נקודות הקצה של האישור הציבורי של Google](https://www.googleapis.com/oauth2/v3/certs).

### Python

```
import jwt
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Google public cert list endpoint
JWKS_URI = "https://generativelanguage.googleapis.com/.well-known/jwks.json"

def load_google_public_key(kid):
    response = requests.get(JWKS_URI).json()
    for key_item in response.get('keys', []):
        if key_item.get('kid') == kid:
            # Convert JWK to Cert wrapper
            return jwt.algorithms.RSAAlgorithm.from_jwk(key_item)
    return None

@app.route('/gemini-webhook-dynamic', methods=['POST'])
def dynamic_handler():
    payload = request.get_data(as_text=True)
    headers = request.headers

    token = headers.get('Webhook-Signature')
    if not token:
        return jsonify({"error": "No signature header"}), 400

    try:
        # Extract kid from JWT header
        unverified_headers = jwt.get_unverified_header(token)
        pub_key = load_google_public_key(unverified_headers.get('kid'))

        if not pub_key:
            return jsonify({"error": "Key cert not found"}), 400

        # Verify Signature against expected audience (e.g., your project client ID)
        event = jwt.decode(
            token,
            pub_key,
            algorithms=["RS256"],
            audience="your-configured-audience"
        )
    except Exception as e:
        return jsonify({"error": "Invalid Dynamic signature", "details": str(e)}), 400

    print("Verified Dynamic payload success.")
    return jsonify({"status": "received"}), 200
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import express from "express";
import jwt from "jsonwebtoken";
import jwksClient from "jwks-rsa";

const app = express();
app.use(express.text({ type: 'application/json' }));

const client = jwksClient({
  jwksUri: "https://generativelanguage.googleapis.com/.well-known/jwks.json"
});

function getKey(header, callback) {
  client.getSigningKey(header.kid, (err, key) => {
    const signingKey = key.getPublicKey();
    callback(null, signingKey);
  });
}

app.post('/gemini-webhook-dynamic', (req, res) => {
  const token = req.headers['webhook-signature'];

  if (!token) {
    return res.status(400).json({ error: "No signature header" });
  }

  jwt.verify(
    token,
    getKey,
    {
      algorithms: ["RS256"],
      audience: "your-configured-audience"
    },
    (err, decoded) => {
      if (err) {
        return res.status(400).json({ error: "Invalid Dynamic signature", details: err.message });
      }

      console.log("Verified Dynamic payload success.");
      res.status(200).json({ status: "received" });
    }
  );
});
```

## מעטפת webhook

כדי למנוע עומס על רוחב הפס, Gemini משתמש במודל **מטען ייעודי דליל** של וווב-הוק כדי להעביר נתונים. במקום קובץ הפלט הגולמי, נשלח snapshot שמכיל פרטי סטטוס ונקודות להפניה לתוצאות.

דוגמה לפורמט של מטען ייעודי (payload):

```
{
  "type": "batch.succeeded",
  "version": "v1",
  "timestamp": "2026-01-22T12:00:00Z",
  "data": {
    "id": "batch_123456",
    "output_file_uri": "gs://my-bucket/results.jsonl"
  }
}
```

## מידע על קטלוג האירועים

האירועים הבאים מופעלים עבור משימות תומכות:

| סוג אירוע | טריגר | פריט מטען ייעודי (`data`) |
| --- | --- | --- |
| `batch.succeeded` | העיבוד הסתיים בהצלחה. | `id`, `output_file_uri` |
| `batch.cancelled` | המשתמש ביטל את הבקשה | `id` |
| `batch.expired` | העיבוד של החבילה לא הסתיים תוך 24 שעות | `id` |
| `batch.failed` | משימה באצווה נכשלה (שגיאת מערכת או שגיאת אימות). | `id`,‏ `error_code`,‏ `error_message` |
| `interaction.requires_action` | בקשה להפעלת פונקציה, המשתמש צריך לעשות משהו | `id` |
| `interaction.completed` | הפעולה LRO ב-API של האינטראקציות בוצעה בהצלחה | `id` |
| `interaction.failed` | הפעולה LRO ב-Interactions API נכשלה (שגיאת מערכת או שגיאת אימות). | `id`,‏ `error_code`,‏ `error_message` |
| `interaction.cancelled` | בוטלה פעולת LRO בממשק API של אינטראקציות | `id` |
| `video.generated` | תהליך יצירת הסרטון LRO הושלם. | `id`,‏ `output_file_uri`,‏ `file_name` |

## שיטות מומלצות

כדי להבטיח פעולה אמינה וניתנת להרחבה:

- **בדיקה קפדנית של הגנה מפני שידור חוזר**: כל הבקשות כוללות `webhook-timestamp`
  כותרת. חשוב תמיד לאמת את חותמת הזמן הזו בשכבת הגדרות השרת כדי לדחות נתוני payload שגילם יותר מ-**5 דקות** (כדי לצמצם את הסיכון למתקפות שידור חוזר).
- **עיבוד אסינכרוני**: תגובה עם `2xx OK` באופן מיידי לאחר זיהוי חתימה תקינה, והוספת פעולות הניתוח לתור באופן פנימי. זמני המתנה ארוכים של המאזינים יפעילו מחזור של ניסיונות מסירה.
- **טיפול בהסרת כפילויות**: וווב-הוקים רגילים מספקים 'לפחות פעם אחת'. כדאי להשתמש בכותרת `webhook-id` העקבית כדי לטפל בכפילויות פוטנציאליות בזרימות עם עומס גבוה יותר.

## מה השלב הבא?

- ‫[Batch API](https://ai.google.dev/gemini-api/docs/batch?hl=he): שימוש ב-webhook כדי לבצע אוטומציה של נקודות קצה עם נפח גבוה.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-08 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-08 (שעון UTC)."],[],[]]
