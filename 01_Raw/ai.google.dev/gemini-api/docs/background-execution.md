---
source_url: https://ai.google.dev/gemini-api/docs/background-execution?hl=he
fetched_at: 2026-07-06T05:16:13.473006+00:00
title: "\u05d1\u05d9\u05e6\u05d5\u05e2 \u05d1\u05e8\u05e7\u05e2 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# ביצוע ברקע

במשימות ארוכות כמו Deep Research, חשיבה רציונלית מורכבת או הרצות של סוכנים מרובי-שלבים, זמן קצוב לתפוגה לחיבור עלול להפריע לבקשות HTTP רגילות (שבדרך כלל נסגרות אחרי 60 שניות). [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) מספק **background execution** כדי להריץ את המשימות האלה באופן אסינכרוני.

כדי לאפשר לאינטראקציה לפעול עד שהיא משלימה את המשימה בשרת, מגדירים את `"background": true` כשיוצרים את האינטראקציה. ה-API מחזיר באופן מיידי מזהה אינטראקציה, שאפליקציות לקוח יכולות להשתמש בו כדי לבדוק את הסטטוס, את התקדמות הסטרימינג או להתחבר מחדש לסטרימינג שהחיבור שלו נותק.

הביצוע ברקע נתמך במודלים רגילים של Gemini (כמו `gemini-3.5-flash` ו-`gemini-3.1-pro-preview`) ובסוכנים מנוהלים (כמו `antigravity-preview-05-2026`).

## יצירת אינטראקציה ברקע

כדי להתחיל אינטראקציה ברקע, מגדירים את הפרמטר `background` לערך `true` כשיוצרים את המשאב.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Write a guide on space exploration.",
    background=True,
)
print(f"Created background interaction ID: {interaction.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Write a guide on space exploration.",
    background: true,
});
console.log(`Created background interaction ID: ${interaction.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Write a guide on space exploration.",
    "background": true
  }'
```

## איך הרצה ברקע פועלת

כשיוצרים אינטראקציה ברקע, המשימה פועלת באופן אסינכרוני בשרת. האינטראקציה עוברת בין מצבי ביצוע שונים:

- ‫`in_progress`: השרת מבצע באופן פעיל את האינטראקציה (למשל, מריץ קוד או מבצע מחקר).
- ‫`requires_action`: האינטראקציה מושהית וממתינה לקלט מהלקוח (למשל, אישור הפעלת כלי או מענה על שאלה).
- ‫`completed`: האינטראקציה הסתיימה בהצלחה והפלט זמין.
- ‫`failed`: אירעה שגיאה במהלך הביצוע (למשל, כשל בכלי או הגבלות קצב).
- ‫`cancelled`: בקשה של לקוח עצרה את הביצוע.

### תרחישים לדוגמה

שימוש בביצוע ברקע עבור:

- **הרצת סוכנים:** משימות שדורשות הרצת קוד, גלישה באינטרנט או תיאום בין סוכנים משניים (כמו `antigravity-preview-05-2026`).
- **Deep Research:** פועל באמצעות `deep-research-preview-04-2026` או `deep-research-max-preview-04-2026`, והתהליך נמשך כמה דקות.
- **הסקה ארוכה:** משימות שבהן שלבי החשיבה של המודל חורגים מהמגבלות הרגילות של חיבור HTTP.

## אחזור תוצאות

אפשר לקבל תוצאות של אינטראקציות ברקע באמצעות **polling** או **סטרימינג**.

### תבנית דגימה (לא חוסמת)

התשאול בודק את סטטוס האינטראקציה באופן תקופתי באמצעות בקשות GET לא חוסמות, עד שהוא מגיע למצב סופי.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.get(id="YOUR_INTERACTION_ID")

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

let interaction = await client.interactions.get("YOUR_INTERACTION_ID");

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

if (interaction.status === "completed") {
    console.log(interaction.output_text);
} else {
    console.log(`Finished with status: ${interaction.status}`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

### תבנית סטרימינג

אם השידור מתנתק בגלל הפרעה ברשת, אפשר להמשיך את השידור מהאירוע האחרון שהתקבל. כל דלתא מכילה `event_id` ייחודי במטען הייעודי שלה. העברת המזהה הזה כ-`last_event_id` מפעילה מחדש את הזרם מהאירוע הזה.

### Python

```
import time
from google import genai

client = genai.Client()
interaction_id = "YOUR_INTERACTION_ID"

def stream_with_reconnect(interaction_id: str):
    last_event_id = None
    while True:
        try:
            # Retrieve the stream. If resuming, pass last_event_id
            stream = client.interactions.get(
                id=interaction_id,
                stream=True,
                last_event_id=last_event_id
            )

            for event in stream:
                # Log event updates and capture event_id if present
                if event.event_id:
                    last_event_id = event.event_id

                if event.event_type == "step.delta" and event.delta.type == "text":
                    print(event.delta.text, end="", flush=True)

                if event.event_type == "interaction.completed":
                    return

        except Exception as e:
            print(f"\n[Connection lost: {e}. Reconnecting in 3s...]")
            time.sleep(3)

stream_with_reconnect(interaction_id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const interactionId = "YOUR_INTERACTION_ID";

async function streamWithReconnect(id) {
    let lastEventId = undefined;
    while (true) {
        try {
            // Retrieve the stream. If resuming, pass last_event_id in options
            const stream = await client.interactions.get(id, {
                stream: true,
                last_event_id: lastEventId
            });

            for await (const event of stream) {
                // Capture event_id if present
                const idVal = event.event_id || event.id;
                if (idVal) {
                    lastEventId = idVal;
                }

                if (event.event_type === "step.delta" && event.delta?.type === "text") {
                    process.stdout.write(event.delta.text);
                }

                if (event.event_type === "interaction.completed") {
                    return;
                }
            }
        } catch (error) {
            console.log(`\n[Connection lost: ${error.message}. Reconnecting in 3s...]`);
            await new Promise(resolve => setTimeout(resolve, 3000));
        }
    }
}

await streamWithReconnect(interactionId);
```

### REST

```
curl -N -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID?stream=true&last_event_id=YOUR_LAST_EVENT_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## שיחות רב-שלביות

אינטראקציות עוקבות יכולות להתבסס על שיחה ברקע באמצעות `previous_interaction_id`, בכפוף למגבלות הבאות:

1. **הפעלה פעילה נחסמת:** שרשור של אינטראקציה עוקבת לאינטראקציה עם סטטוס `in_progress` מחזיר שגיאה `400 Bad Request`. צריך לחכות שהאינטראקציה תגיע למצב `completed` לפני שמתחילים את האינטראקציה הבאה.
2. **פרמטר סביבה לסוכנים מנוהלים:** כשמשרשרים אינטראקציות לסוכנים מנוהלים (כמו `antigravity-preview-05-2026`), הבקשות צריכות לכלול את הפרמטרים `previous_interaction_id` ו-`environment`.

בדוגמאות הבאות אפשר לראות איך יוצרים שרשור של אינטראקציות:

### Python

```
import time
from google import genai

client = genai.Client()
agent_model = "antigravity-preview-05-2026"

# First interaction: Provision sandbox environment and execute first instruction
interaction1 = client.interactions.create(
    model=agent_model,
    input="Create a folder named project/ and write hello.py inside.",
    environment="remote",
    background=True
)

# Wait for completion
while True:
    check = client.interactions.get(id=interaction1.id)
    if check.status != "in_progress":
        break
    time.sleep(2)

# Second interaction: Chain using previous_interaction_id and environment
interaction2 = client.interactions.create(
    model=agent_model,
    input="List all files in the project/ directory.",
    previous_interaction_id=interaction1.id,
    environment="remote",
    background=True
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const agentModel = "antigravity-preview-05-2026";

// First interaction: Provision sandbox environment and execute first instruction
const interaction1 = await client.interactions.create({
    model: agentModel,
    input: "Create a folder named project/ and write hello.py inside.",
    environment: "remote",
    background: true
});

// Wait for completion
while (true) {
    const check = await client.interactions.get(interaction1.id);
    if (check.status !== "in_progress") {
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 2000));
}

// Second interaction: Chain using previous_interaction_id and environment
const interaction2 = await client.interactions.create({
    model: agentModel,
    input: "List all files in the project/ directory.",
    previous_interaction_id: interaction1.id,
    environment: "remote",
    background: true
});
```

### REST

```
# Chain second interaction (Make sure FIRST_INTERACTION_ID has status 'completed')
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "antigravity-preview-05-2026",
    "input": "List all files in the project/ directory.",
    "previous_interaction_id": "FIRST_INTERACTION_ID",
    "environment": "remote",
    "background": true
  }'
```

## ביטול ומחיקה

שליטה בהרצות פעולות וניהול האחסון באמצעות בקשות ביטול ומחיקה:

- **ביטול (`POST /interactions/{id}/cancel`):** מפסיק את המשימה הפעילה. הסטטוס משתנה ל`cancelled`. פעולות ניקוי בשרת יכולות לגרום לעיכוב קל לפני שהסטטוס מתעדכן בבקשות GET.
- **מחיקה (`DELETE /interactions/{id}`):** רשומות האינטראקציה יוסרו מהשרת. בקשות GET הבאות מחזירות שגיאה `404 Not Found`.

### Python

```
from google import genai

client = genai.Client()

# Cancel a running interaction
client.interactions.cancel(id="YOUR_INTERACTION_ID")

# Delete the interaction record entirely
client.interactions.delete(id="YOUR_INTERACTION_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Cancel a running interaction
await client.interactions.cancel("YOUR_INTERACTION_ID");

// Delete the interaction record entirely
await client.interactions.delete("YOUR_INTERACTION_ID");
```

### REST

```
# Cancel the interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID/cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"

# Delete the interaction
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## השלבים הבאים

- במאמר [סקירה כללית על Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) מוסבר על ניהול סשנים ומצבים.
- פרטים נוספים על עדכונים בזמן אמת של אירועים זמינים במדריך בנושא [אינטראקציות בסטרימינג](https://ai.google.dev/gemini-api/docs/streaming?hl=he).
- כדי ליצור סוכנים עם שמירת מצב שמנהלים כמה אינטראקציות רב-שלביות, אפשר לעיין ב[מדריך למתחילים בנושא סוכנים מנוהלים](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-06-26 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-06-26 (שעון UTC)."],[],[]]
