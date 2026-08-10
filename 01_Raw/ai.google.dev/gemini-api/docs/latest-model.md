---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=he
fetched_at: 2026-08-10T03:21:13.968895+00:00
title: "\u05e9\u05d9\u05de\u05d5\u05e9 \u05d1\u05de\u05d5\u05d3\u05dc\u05d9\u05dd \u05d4\u05e2\u05d3\u05db\u05e0\u05d9\u05d9\u05dd \u05e9\u05dc Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# שימוש במודלים העדכניים של Gemini

[הנושאים בדף](#)
[3.5 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=he)

‫Gemini 3.6 Flash‏ (`gemini-3.6-flash`) ו-Gemini 3.5 Flash-Lite‏ (`gemini-3.5-flash-lite`) זמינים לכלל המשתמשים (GA) ומוכנים לשימוש בסביבת ייצור.

- ‫**Gemini 3.6 Flash**: ביצועים טובים יותר במשימות מורכבות של סוכנים ושל מודלים מולטי-מודאליים, תוך צמצום השימוש בטוקנים, במחיר נמוך יותר מ-3.5 Flash.
- ‫**Gemini 3.5 Flash-Lite**: המודל הכי מהיר והכי זול בסדרת 3.5. הביצועים שלו טובים יותר מהדורות הקודמים של Flash-Lite בביצוע עם תפוקה גבוהה.

במדריך הזה מוסבר מה חדש בכל מודל, אילו שינויים ב-API משפיעים על הקוד ואיך לבצע מיגרציה.

### Gemini 3.6 Flash

1. מתקינים את המיומנות:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. הפעלת המיומנות:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. מתקינים את המיומנות:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. הפעלת המיומנות:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

## מודלים חדשים

| מודל | מזהה דגם | רמת ההעמקה שמוגדרת כברירת מחדל | תמחור | תיאור |
| --- | --- | --- | --- | --- |
| Gemini 3.6 Flash | `gemini-3.6-flash` | `medium` | ‫1.50$ למיליון טוקנים של קלט ו-7.50 $למיליון טוקנים של פלט | משלב בין מהירות לבין אינטליגנציה למשימות מבוססות-סוכנים ומולטימודאליות. |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | `minimal` | ‫0.30$ למיליון טוקנים של קלט ו-2.50 $למיליון טוקנים של פלט | המודל המהיר ביותר מסוג 3.5 עם העלות הכי נמוכה לביצוע עם תפוקה גבוהה. |

שני המודלים תומכים בחלון הקשר של מיליון טוקנים, ב-64,000 טוקנים מקסימליים של פלט, בחשיבה ובחבילה המלאה של כלים מובנים, כולל [שימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he).

מפרטים מלאים זמינים בדפי הדגמים:

- [דף המודל Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=he)
- [דף המודל Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=he)

למידע מפורט על המחירים, אפשר לעיין ב[דף המחירים](https://ai.google.dev/gemini-api/docs/pricing?hl=he).

## מדריך למתחילים

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Write a three.js script that renders an interactive 3D robot."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Write a three.js script that renders an interactive 3D robot.",
  });
  console.log(interaction.outputText);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.6-flash",
    "input": {
      "parts": [{"text": "Write a three.js script that renders an interactive 3D robot."}]
    }
  }'
```

## מה חדש ב-Gemini 3.6 Flash

- **צמצום של טוקנים ותורות בדיבור:** השלמת תהליכי עבודה מרובי-שלבים עם פחות שלבי חשיבה רציונלית, תורות בדיבור וקריאות לכלים בהשוואה ל-Gemini 3.5. היא גם מפחיתה את התרחבות לולאת ההפעלה.
- **יצירת קוד משופרת:** יצירת קוד באיכות גבוהה יותר שמוכן לייצור, עם פחות עריכות לא רצויות ופחות לולאות ניפוי באגים.
- **שיפור היכולת לפעול לפי הוראות**: הפחתת שינויים לא רצויים בקבצים במהלך משימות אבחון.
- **הסקה מרחבית ורב-אופנית משופרת:** ביצועים משופרים בניתוח תרשימים, בהמרת תוכניות חזותיות וביצירת פריסות אינטרנט מרובות רכיבים.
- **בדיקה תוכניתית מראש:** Gemini 2.5 Pro מעדיף להריץ סקריפטים של קוד אבחון לפני ביצוע שינויים בתדירות גבוהה יותר מ-Gemini 3.5 Flash. השיטה הזו משפרת את הדיוק במשימות מורכבות, אבל יכולה להוסיף שלבים מיותרים של חיפוש מידע בעבודות פשוטות שקשורות לחלק הקצה הקדמי של האתר.
- **תמיכה בשימוש במחשב:** נתמכת ככלי מקורי לאוטומציה של ממשק משתמש מבוסס-סוכן.
- **העדפות לגבי סגנון ממשק המשתמש**: המודל טוב יותר ביצירת קוד פונקציונלי, אבל בודקים אנושיים העדיפו מודלים קודמים מבחינת פריסה חזותית וסגנון. כדי לצמצם את הסיכון הזה, מומלץ לספק הנחיות עיצוב ברורות.
- **מאמץ חשיבה שמוגדר כברירת מחדל (בינוני):** משתמש באותה רמת חשיבה שמוגדרת כברירת מחדל `medium` כמו Gemini 3.5 Flash.
- **תמחור מוזל**: עלויות נמוכות יותר של טוקנים של פלט (7.50$ למיליון לעומת 9.00$ למיליון ל-3.5 Flash). המחיר של טוקנים של קלט נשאר 1.50 $למיליון.

## מה חדש ב-Gemini 3.5 Flash-Lite

- **זמן האחזור של ביצוע המשימות קצר יותר:** התפוקה הכי גבוהה במשפחת 3.5 לניתוח נתונים בכמויות גדולות ולחילוץ מסמכים.
- **ביצועים משופרים של חשיבה רציונלית ומולטי-מודאליות:** נתיב מיגרציה חזק מ-Gemini 2.5 Flash, עם ציונים גבוהים יותר במשימות של חשיבה רציונלית כמו HLE‏ (18.0% לעומת 11.0%) ובמדדי ביצועים מולטי-מודאליים כמו CharXIV‏ (74.5% לעומת 63.7%).
- **ארגון של סוכנים משניים ומהימנות של כלים:** שיפור המהימנות של הפעלת כלים לביצוע קוד, לחיפוש ולתהליכי עבודה של MCP. העלאת רמת החשיבה לתכנון אוטונומי ולמשימות מורכבות של סוכני משנה.
- **הבנה משופרת של מסמכים:** שיפור הדיוק בניתוח מסמכים ובחילוץ נתונים מובְנים. אפשר להתנסות ברמות חשיבה מינימליות וגבוהות, בהתאם למורכבות המסמך.
- **קידוד אינטראקטיבי ועיבוד נתונים טבלאיים:** ביצועים טובים מאוד ב-JavaScript של חזית האתר ובעיבוד נתונים טבלאיים באמצעות תכנון דרך הרצת קוד קלה.
- **צ'אטבוט ועקביות התפקיד:** יכולת טובה יותר לעקוב אחרי הוראות רב-שלביות ולשמור על עקביות התפקיד בהשוואה ל-Gemini 3.1 Flash-Lite.
- **תמיכה בשימוש במחשב:** נתמכת ככלי מקורי לאוטומציה של ממשק משתמש מבוסס-סוכן.

## בחירת המודל המתאים של Flash או Flash-Lite

אפשר להשתמש בטבלה הזו כדי לבחור את המודל ואת נתיב ההעברה שמתאימים לעומסי העבודה שלכם.

בשני המודלים צריך להסיר פרמטרים של דגימה שהוצאו משימוש (`temperature`, `top_p`, `top_k`) ופניות למודל שמולאו מראש. פרטים נוספים זמינים במאמר בנושא [שינויים ב-API](#api-changes-and-parameter-updates).

| מודל | תרחישים עיקריים לדוגמה | יעד מומלץ להעברה |
| --- | --- | --- |
| ‫**Gemini 3.6 Flash** `gemini-3.6-flash` | יצירת קוד, חשיבה רציונלית מרחבית/מולטי-מודאלית, תהליכי עבודה מבוססי-סוכן מרובי-שלבים | ‫**Gemini 3.5 Flash**,‏ **Gemini 3 Flash (Preview)** או **Gemini 3.1 Pro** |
| ‫**Gemini 3.5 Flash-Lite** `gemini-3.5-flash-lite` | הרצה אוטונומית של סוכנים משניים, ניתוח נתונים בכמויות גדולות וחילוץ מסמכים, ניתוח של JSON מובנה | ‫**Gemini 3.1 Flash-Lite** או **Gemini 2.5 Flash** |

## סוכן Antigravity עודכן

בגלל הביצועים המשופרים שלו, Gemini 3.6 Flash הוא עכשיו מודל ברירת המחדל החדש שמפעיל את [סוכן Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=he) ב-Gemini Managed Agents. אפשר לשנות את זה על ידי הגדרת שדה חדש ב-API.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## שינויים ב-API ועדכונים בפרמטרים

החל מ-Gemini 3.6 Flash ומ-Gemini 3.5 Flash-Lite, השינויים הבאים ב-API חלים על מודלים אלה ועל כל מודלי Gemini העתידיים.

- **הוצאה משימוש של פרמטרים לדגימה**: הפרמטרים `temperature`,‏ `top_p` ו-`top_k` הוצאו משימוש. ממשק ה-API מתעלם מהפרמטרים האלה ומחזיר שגיאה בדורות עתידיים של המודל.
- **אימות של תפניות במודל עם מילוי מראש**: אין יותר תמיכה במילוי מראש של תפניות במודל. אם התור האחרון בבקשה שלא ריק הוא תור של `model`, ה-API מחזיר שגיאת `400`.

בהמשך מופיעים הסברים מפורטים ודוגמאות קוד לכל שינוי ב-API.

### 1. הוצאה משימוש של פרמטרים לדגימה (`temperature`, `top_p`, `top_k`)

התכונות `temperature`, `top_p` וגם `top_k` הוצאו משימוש ומתעלמים מהן. בדורות הבאים של המודלים, אם תספקו את הפרמטרים האלה, תוחזר שגיאת HTTP 400. **הסרת הפרמטרים האלה מכל הבקשות.**

```
# ⚠️ Remove these parameters (deprecated)
generation_config = {
     "temperature": 0.7,
     "top_p": 0.9,
     "top_k": 40,
}
```

כדי לשפר את הדטרמיניזם, צריך להגדיר הוראה למערכת עם כללים מפורשים לתרחיש השימוש הספציפי.

### 2. אימות של תורות במודל עם מילוי מראש

בקשות ל-API שמסתיימות בתפקיד מודל לא ריק אסורות, ומוחזרת **שגיאת HTTP 400**.

#### ⚠️ הימנעות

במטען ייעודי (payload) של `generateContent` מדור קודם או במטען ייעודי (payload) של REST גולמי, אסור עכשיו לסיים עם תור של תפקיד מודל:

```
/* ❌ DO NOT: End payload contents with a 'model' role turn */
{
  "contents": [
    {"role": "user", "parts": [{"text": "Translate 'Hello world' to Spanish."}]},
    {"role": "model", "parts": [{"text": "Translation:"}]}  /* ❌ Returns error */
  ]
}
```

#### ‫✅ מיגרציה מומלצת (Interactions API)

ב-Interactions API, תורות של מודלים לא מאוכלסות מראש באופן ידני. אם האפליקציה שלכם מילאה מראש תור של מודל כדי להשמיט פתיחים או לכפות עיצוב JSON, אתם צריכים להשתמש במקום זאת ב-system\_instruction או ב[פלט מובנה](https://ai.google.dev/gemini-api/docs/structured-output?hl=he).

```
# ✅ RECOMMENDED: Use system_instruction in the Interactions API to specify output format
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Translate 'Hello world' to Spanish.",
    system_instruction="Output only the translation without introductory text.",
)
```

## רשימת משימות להעברה

### Gemini 3.6 Flash

1. מתקינים את המיומנות:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. הפעלת המיומנות:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. מתקינים את המיומנות:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. הפעלת המיומנות:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

### מעבר אל gemini-3.6-flash

- **עדכון מזהה המודל:** משנים את מחרוזת מודל היעד ל-`gemini-3.6-flash`.
- **הסרת פרמטרים של דגימה שהוצאו משימוש:**
  - הסרת `temperature`,‏ `top_p` ו-`top_k` מהגדרות יצירה.
  - מחליפים את `thinking_budget` במחרוזת enum `thinking_level` שמוגדרת ל-`"medium"` או ל-`"high"`.
  - הסרת `candidate_count` (לא נתמך ב-Gemini 3.x).
- **החלת כללי אימות של תור:**
  - סטנדרטיזציה של שיחות רב-שלביות בצד השרת `previous_interaction_id`.
  - הסרת תפניות של מודל שמולאו מראש.
- **ביקורת של הפעלת פונקציות:**
  - ממקמים נכסים מולטימודאליים בתוך מטען התגובה.
  - מעצבים הוראות מוטבעות באמצעות `\n\n`.
  - אם מופיעות שגיאות `Malformed_Function_Call` שקשורות לטקסט לפני הכלי, אפשר לעיין במאמר [פתרונות עקיפים לדרישות לגבי טקסט לפני הכלי](https://ai.google.dev/gemini-api/docs/function-calling?hl=he#workarounds-for-pre-tool-text-requirements).
  - רק אם משתמשים ב-generateContent API: מוודאים שכל האובייקטים מסוג `FunctionResponse` כוללים את `call_id` ואת `name`.
- **דרישות בסיסיות ל-Gemini 3.x:** למידע על עדכוני SDK ושימור חתימת המחשבה, אפשר לעיין ב[רשימת המשימות למיגרציה של Gemini 3.5](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=he#migration).

### מעבר ל-gemini-3.5-flash-lite

- **עדכון מזהה המודל:** משנים את מחרוזת מודל היעד ל-`gemini-3.5-flash-lite`.
- **הגדרת רמת המאמץ המחשבתי:**
  - למיצוי, להעברה או לסיווג של נפחים גדולים: משאירים את הערך `thinking_level` על `"minimal"` (ברירת מחדל) כדי למקסם את קצב העברת הנתונים.
  - עבור סוכני משנה אוטונומיים עם קריאות לכלים, הפעלת קוד או נימוקים מרובי-שלבים: מגדירים את `thinking_level` לערך `"medium"` או את `"high"` לערך `"high"` כדי למנוע סיום מוקדם של הכלי.
- **הסרת פרמטרים שהוצאו משימוש ואימות של הפעלת פונקציות:** צריך להחיל את [אותם כללים כמו ב-3.6 Flash](#migrate-to-gemini-3-6-flash).
- **הדרישות הבסיסיות ל-Gemini 3.x:** אפשר לעיין ב[רשימת המשימות להעברה ל-Gemini 3.5](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=he#migration).

## השלבים הבאים

- אפשר לעיין במפרטי ה-API ב[סקירה הכללית של המודלים](https://ai.google.dev/gemini-api/docs/models?hl=he).
- מידע נוסף על תזמור של כמה סוכנים זמין [במדריך לשימוש ב-Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=he).
- בודקים ומעדנים את הפרומפטים ב-[Google AI Studio](https://aistudio.google.com/?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-30 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-30 (שעון UTC)."],[],[]]
