---
source_url: https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=he
fetched_at: 2026-05-11T05:08:45.383436+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# הרצת קוד

‫Gemini API כולל כלי להרצת קוד שמאפשר למודל ליצור ולהריץ קוד Python. לאחר מכן המודל יכול ללמוד באופן איטרטיבי מתוצאות הביצוע של הקוד עד שהוא מגיע לפלט סופי. אתם יכולים להשתמש בהרצת קוד כדי ליצור אפליקציות שמרוויחות מחשיבה רציונלית מבוססת קוד. לדוגמה, אפשר להשתמש בהרצת קוד כדי לפתור משוואות או לעבד טקסט. אפשר גם להשתמש ב[ספריות](#supported-libraries) שכלולות בסביבת ההפעלה של הקוד כדי לבצע משימות ספציפיות יותר.

‫Gemini יכול להריץ קוד ב-Python בלבד. עדיין אפשר לבקש מ-Gemini ליצור קוד בשפה אחרת, אבל המודל לא יכול להשתמש בכלי להרצת קוד כדי להריץ אותו.

## הפעלת ביצוע קוד

כדי להפעיל את הרצת הקוד, צריך להגדיר את כלי הרצת הקוד במודל. כך המודל יכול ליצור ולהריץ קוד.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the sum of the first 50 prime numbers? "
          "Generate and run code for the calculation, and make sure you get all 50.",
    tools=[{"type": "code_execution"}]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
    elif step.type == "code_execution_call":
        print(step.arguments.code)
    elif step.type == "code_execution_result":
        print(step.result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "What is the sum of the first 50 prime numbers? " +
           "Generate and run code for the calculation, and make sure you get all 50.",
    tools: [{ type: "code_execution" }]
});

for (const step of interaction.steps) {
    if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log(contentBlock.text);
            }
        }
    } else if (step.type === "code_execution_call") {
        console.log(step.arguments.code);
    } else if (step.type === "code_execution_result") {
        console.log(step.result);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50.",
    "tools": [{"type": "code_execution"}]
}'
```

הפלט יכול להיראות כך, אחרי שעיצבנו אותו כדי שיהיה קל לקריאה:

```
Okay, I need to calculate the sum of the first 50 prime numbers. Here's how I'll
approach this:

1.  **Generate Prime Numbers:** I'll use an iterative method to find prime
    numbers. I'll start with 2 and check if each subsequent number is divisible
    by any number between 2 and its square root. If not, it's a prime.
2.  **Store Primes:** I'll store the prime numbers in a list until I have 50 of
    them.
3.  **Calculate the Sum:**  Finally, I'll sum the prime numbers in the list.

Here's the Python code to do this:

def is_prime(n):
  """Efficiently checks if a number is prime."""
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

primes = []
num = 2
while len(primes) < 50:
  if is_prime(num):
    primes.append(num)
  num += 1

sum_of_primes = sum(primes)
print(f'{primes=}')
print(f'{sum_of_primes=}')

primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
sum_of_primes=5117

The sum of the first 50 prime numbers is 5117.
```

הפלט הזה משלב כמה חלקי תוכן שהמודל מחזיר כשמשתמשים בהרצת קוד:

- ‫`text`: טקסט מוטבע שנוצר על ידי המודל
- ‫`code_execution_call`: קוד שנוצר על ידי המודל ומיועד להרצה
- `code_execution_result`: התוצאה של קוד ההפעלה

## הפעלת קוד עם תמונות (Gemini 3)

מודל Gemini 3 Flash יכול עכשיו לכתוב ולהריץ קוד Python כדי לבצע מניפולציות פעילות בתמונות ולבדוק אותן.

**תרחישים לדוגמה**

- **זום ובדיקה**: המודל מזהה באופן מובנה מתי הפרטים קטנים מדי (למשל, קריאת מד מרחק) וכותב קוד לחיתוך ולבדיקה מחדש של האזור ברזולוציה גבוהה יותר.
- **מתמטיקה ויזואלית**: המודל יכול לבצע חישובים מרובי-שלבים באמצעות קוד (למשל, סיכום פריטים בקבלה).
- **הערות לתמונות**: המודל יכול להוסיף הערות לתמונות כדי לענות על שאלות, למשל לצייר חצים כדי להראות קשרים.

## הפעלת ביצוע קוד באמצעות תמונות

החל מ-Gemini 3 Flash, יש תמיכה רשמית בהרצת קוד עם תמונות. כדי להפעיל את ההתנהגות הזו, צריך להפעיל את ההגדרה 'הפעלת קוד ככלי' ואת ההגדרה 'חשיבה'.

### Python

```
from google import genai
import requests
import base64
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "image", "data": base64.b64encode(image_bytes).decode('utf-8'), "mime_type": "image/jpeg"},
        {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
    ],
    tools=[{"type": "code_execution"}]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                # Display generated image
                display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.arguments.code)
    elif step.type == "code_execution_result":
        print(step.result)
```

### JavaScript

```
async function main() {
  const client = new GoogleGenAI({});

  // 1. Prepare Image Data
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

  // 2. Call the API with Code Execution enabled
  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        data: base64ImageData,
        mime_type: "image/jpeg"
      },
      { type: "text", text: "Zoom into the expression pedals and tell me how many pedals are there?" }
    ],
    tools: [{ type: "code_execution" }]
  });

  // 3. Process the response (Text, Code, and Execution Results)
  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log(`\nGenerated Code:\n`, step.arguments.code);
    } else if (step.type === "code_execution_result") {
      console.log(`\nExecution Output:\n`, step.result);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

# Use jq to create the JSON payload to avoid "Argument list too long" error with large base64 strings
echo -n "$IMAGE_B64" > image_b64.txt
jq -n \
  --rawfile b64 image_b64.txt \
  --arg mime "$MIME_TYPE" \
  '{
    model: "gemini-3-flash-preview",
    input: [
      {type: "image", data: $b64, mime_type: $mime},
      {type: "text", text: "Zoom into the expression pedals and tell me how many pedals are there?"}
    ],
    tools: [{type: "code_execution"}]
  }' > payload.json

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d @payload.json
```

## שימוש בהרצת קוד באינטראקציות עוקבות

אפשר גם להשתמש בהרצת קוד כחלק משיחה מרובת תפניות באמצעות `previous_interaction_id`.

### Python

```
from google import genai

client = genai.Client()

# First turn
interaction1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="I have a math question for you.",
    tools=[{"type": "code_execution"}]
)
print(interaction1.steps[-1].content[0].text)

# Second turn - follow-up with code execution
interaction2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction1.id,
    input="What is the sum of the first 50 prime numbers? "
          "Generate and run code for the calculation, and make sure you get all 50.",
    tools=[{"type": "code_execution"}]
)

for step in interaction2.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
    elif step.type == "code_execution_call":
        print(step.arguments.code)
    elif step.type == "code_execution_result":
        print(step.result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First turn
const interaction1 = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "I have a math question for you.",
    tools: [{ type: "code_execution" }]
});
console.log(interaction1.steps.at(-1).content[0].text);

// Second turn - follow-up with code execution
const interaction2 = await client.interactions.create({
    model: "gemini-3-flash-preview",
    previous_interaction_id: interaction1.id,
    input: "What is the sum of the first 50 prime numbers? " +
           "Generate and run code for the calculation, and make sure you get all 50.",
    tools: [{ type: "code_execution" }]
});

for (const step of interaction2.steps) {
    if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log(contentBlock.text);
            }
        }
    } else if (step.type === "code_execution_call") {
        console.log(step.arguments.code);
    } else if (step.type === "code_execution_result") {
        console.log(step.result);
    }
}
```

### REST

```
# First turn
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "I have a math question for you.",
    "tools": [{"type": "code_execution"}]
}')

INTERACTION_ID=$(echo $RESPONSE1 | jq -r '.id')

# Second turn with previous_interaction_id
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "'"$INTERACTION_ID"'",
    "input": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50.",
    "tools": [{"type": "code_execution"}]
}'
```

## קלט/פלט (I/O)

החל מ-[Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#gemini-2.0-flash), ביצוע הקוד תומך בקלט של קבצים ובפלט של גרפים. באמצעות היכולות האלה של קלט ופלט, אתם יכולים להעלות קובצי CSV וקובצי טקסט, לשאול שאלות לגבי הקבצים ולקבל גרפים של [Matplotlib](https://matplotlib.org/) שנוצרים כחלק מהתשובה. קבצי הפלט מוחזרים כתמונות מוטמעות בתשובה.

### תמחור של קלט/פלט

כשמשתמשים בקלט/פלט של הרצת קוד, מחויבים על טוקנים של קלט וטוקנים של פלט:

**טוקנים של קלט:**

- הנחיה למשתמש

**טוקנים בפלט:**

- קוד שנוצר על ידי המודל
- פלט של הרצת קוד בסביבת הקוד
- טוקנים של חשיבה
- סיכום שנוצר על ידי המודל

### פרטי I/O

כשעובדים עם קלט/פלט של הרצת קוד, חשוב לשים לב לפרטים הטכניים הבאים:

- זמן הריצה המקסימלי של סביבת הקוד הוא 30 שניות.
- אם סביבת הקוד יוצרת שגיאה, יכול להיות שהמודל יחליט ליצור מחדש את פלט הקוד. המצב הזה יכול לקרות עד 5 פעמים.
- הגודל המקסימלי של קובץ קלט מוגבל על ידי חלון הטוקנים של המודל. ב-AI Studio, באמצעות Gemini Flash 2.0, הגודל המקסימלי של קובץ קלט הוא מיליון טוקנים (בערך 2MB לקובצי טקסט מסוגי הקלט הנתמכים). אם תעלו קובץ גדול מדי, לא תוכלו לשלוח אותו ב-AI Studio.
- הכי טוב להשתמש בהרצת קוד עם קובצי טקסט ו-CSV.
- אפשר להעביר את קובץ הקלט כנתונים מוטבעים או להעלות אותו באמצעות [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=he), וקובץ הפלט תמיד מוחזר כנתונים מוטבעים.

## חיוב

אין עלות נוספת על הפעלת ביצוע קוד מ-Gemini API.
תחויבו לפי התעריף הנוכחי של טוקנים של קלט ופלט, בהתאם למודל Gemini שבו אתם משתמשים.

ריכזנו כאן כמה דברים נוספים שכדאי לדעת על חיוב על הפעלת קוד:

- אתם מחויבים רק פעם אחת על טוקני הקלט שאתם מעבירים למודל, ועל טוקני הפלט הסופי שהמודל מחזיר לכם.
- טוקנים שמייצגים קוד שנוצר נספרים כטוקנים של פלט. הקוד שנוצר יכול לכלול טקסט ופלט מולטי-מודאלי כמו תמונות.
- תוצאות של הרצת קוד נספרות גם הן כאסימוני פלט.

מודל החיוב מוצג בתרשים הבא:

![מודל חיוב על הרצת קוד](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=he)

- החיוב מתבצע לפי התעריף הנוכחי של טוקנים של קלט ופלט, בהתאם למודל Gemini שבו אתם משתמשים.
- אם Gemini משתמש בהרצת קוד כדי ליצור את התשובה, ההנחיה המקורית, הקוד שנוצר והתוצאה של הקוד שהורץ מסומנים בתווית *intermediate tokens* (טוקנים ביניים) והחיוב עליהם הוא כ*input tokens* (טוקנים של קלט).
- ‫Gemini יוצר סיכום ומחזיר את הקוד שנוצר, את התוצאה של הקוד שהופעל ואת הסיכום הסופי. החיוב הוא על *אסימוני פלט*.
- תגובת ה-API של Gemini כוללת ספירה של אסימוני ביניים, כדי שתדעו למה אתם מקבלים אסימוני קלט נוספים מעבר להנחיה הראשונית.

## מגבלות

- המודל יכול רק ליצור ולהריץ קוד. הוא לא יכול להחזיר פריטים אחרים, כמו קובצי מדיה.
- במקרים מסוימים, הפעלת ביצוע קוד עלולה להוביל לרגרסיות בתחומים אחרים של פלט המודל (לדוגמה, כתיבת סיפור).
- יש הבדלים בין המודלים השונים ביכולת שלהם להשתמש בהרצת קוד בהצלחה.

## שילובים נתמכים של כלים

אפשר לשלב את הכלי להרצת קוד עם [עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=he) כדי להפעיל תרחישי שימוש מורכבים יותר.

מודלים של Gemini 3 תומכים בשילוב של כלים מובנים (כמו הפעלת קוד) עם כלים מותאמים אישית (הפעלת פונקציות).

## ספריות נתמכות

סביבת ההפעלה של הקוד כוללת את הספריות הבאות:

- attrs
- שחמט
- contourpy
- fpdf
- geopandas
- imageio
- jinja2
- joblib
- jsonschema
- jsonschema-specifications
- lxml
- matplotlib
- mpmath
- numpy
- opencv-python
- openpyxl
- מארז
- פנדות
- כרית
- protobuf
- pylatex
- pyparsing
- PyPDF2
- python-dateutil
- python-docx
- python-pptx
- reportlab
- scikit-learn
- scipy
- seaborn
- שש
- striprtf
- sympy
- לרכז בטבלה
- tensorflow
- toolz
- xlrd

אי אפשר להתקין ספריות משלכם.

## המאמרים הבאים

- אני רוצה לנסות את
- מידע על כלים אחרים של Gemini API:
  - [בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=he)
  - [עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=he)

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-09 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-09 (שעון UTC)."],[],[]]
