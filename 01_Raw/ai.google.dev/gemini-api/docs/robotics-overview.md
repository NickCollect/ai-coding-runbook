---
source_url: https://ai.google.dev/gemini-api/docs/robotics-overview?hl=he
fetched_at: 2026-08-17T02:26:17.747558+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# Gemini Robotics ER

מודלים של Gemini Robotics ER (embodied reasoning) הם מודלים של ראייה ושפה (VLM) שמאפשרים לרובוטים לתפוס את העולם הפיזי ולקיים איתו אינטראקציה. הם מפרשים נתונים חזותיים, מבצעים ניתוח מרחבי וזמני, מתכננים משימות מרובות שלבים ומתזמנים רובוטים וכלים.

## מודלים

מודל Gemini Robotics ER 2 הוא המודל העדכני ביותר ב-Gemini Robotics.
זהו מודל חשיבה רציונלית העדכני שלנו, שמאפשר לרובוטים להבין את הסביבה שלהם בצורה מדויקת. הוא מתמחה ביכולות של נימוק מגולם, כמו תזמור של רובוטים על ידי סוכנים (למשל, באמצעות VLAs), הבנת סרטוני רובוטים כולל הבנת התקדמות וזיהוי הצלחה, קריאת מכשירים, הצבעה ונימוק מרחבי.

מודל Gemini Robotics ER 2 כולל שתי נקודות קצה של מודלים:

- ‫**`gemini-robotics-er-2-preview`**: מודל ER 2 רגיל. הוא מבוסס על Gemini 3.5 Flash וכולל שיפורים ביכולות הבאות: ניתוח מרחבי, איתור רגעים בסרטונים, סיווג של התקדמות בסרטונים, תיאום בין כמה רובוטים ושימוש בכלי רב-שלבי.
- ‫**`gemini-robotics-er-2-streaming-preview`**: מותאם לסטרימינג בזמן אמת באמצעות [Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=he). אפשר להשתמש במודל הזה לסוכני רובוט עם זמן אחזור נמוך, שמבצעים עיבוד של קלט אודיו ווידאו רציף.

אם אתם משתמשים ב-Gemini Robotics ER 1.6, אתם יכולים לשדרג ל-Gemini Robotics ER 2 על ידי החלפת
`model="gemini-robotics-er-1.6-preview"` ב-
`model="gemini-robotics-er-2-preview"` או ב-
`model="gemini-robotics-er-2-streaming-preview"` בקריאות ה-API. חשוב לדעת: מודל Gemini Robotics ER 1.6 ייסגר [בסוף אוגוסט](https://ai.google.dev/gemini-api/docs/deprecations?hl=he#robotics-models).

[התנסות ב-Gemini Robotics ER 2 ב-Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=he)

## יכולות רובוטיקה

‫Gemini Robotics ER תומך במגוון יכולות של הסקת מסקנות מגוף.
כדי לקבל מידע נוסף, בוחרים יכולת:

| יכולת | תיאור | הדרכות |
| --- | --- | --- |
| חשיבה מרחבית | הפנייה לאובייקטים, מעקב אחריהם בסרטון, זיהוי באמצעות תיבות תוחמות, תכנון מסלולים. | [היגיון מרחבי](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=he) |
| ראייה באמצעות סוכנים | שימוש בהרצת קוד כדי לשפר יכולות אחרות באמצעות כלים לעריכת תמונות. | [Agentic vision](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=he) |
| תזמור משימות | שילוב של חשיבה מרחבית עם ממשקי API מותאמים אישית של רובוטים כדי להשלים משימות ארוכות טווח. | [תזמור משימות](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=he) |
| הזרמה (רק בנקודת הקצה של Gemini Robotics ER 2 Streaming) | סטרימינג דו-כיווני לסוכני רובוטים בזמן אמת עם קריאות לפונקציות בזמן אחזור נמוך. | [סטרימינג לרובוטיקה](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=he) |
| התקדמות הסרטון (Gemini Robotics ER 2 בלבד) | חיפוש רגעים וסיווג התקדמות מפידים רציפים של סרטונים. | [הבנת סרטונים](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=he) |

## תחילת העבודה

בדוגמה הבאה מוצגים אובייקטים בתמונה ומוחזרות התוויות והקואורדינטות הדו-ממדיות המנורמלות שלהם. אפשר להעביר את הפלט הזה ישירות ל-API של רובוטיקה או למודל VLA כדי ליצור פעולות של רובוט.

### Python

```
from google import genai

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

image_response = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": PROMPT}
    ],
    generation_config={"thinking_level": "high"},
)

print(image_response.output_text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-robotics-er-2-preview",
    "input": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "image/png",
            "data": "'"${IMAGE_BASE64}"'"
          }
        },
        {
          "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
        }
      ]
    },
    "generation_config": {
      "thinking_config": {
        "thinking_level": "high"
      }
    }
  }'
```

הפלט יהיה מערך JSON שמכיל אובייקטים, שלכל אחד מהם יש `point` (קואורדינטות `[y, x]` מנורמלות) ו-`label` שמזהה את האובייקט.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

בתמונה הבאה אפשר לראות דוגמה לאופן שבו הנקודות האלה יכולות להופיע:

![דוגמה שמציגה את הנקודות של אובייקטים בתמונה](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=he)

## איך זה עובד

‫Gemini Robotics ER מקבל קלט של תמונות, סרטונים או אודיו עם הנחיות בשפה טבעית. היא מזהה אובייקטים, מנתחת את ההקשר של הסצנה ואת היחסים המרחביים, ומחזירה פלט מובנה כמו קואורדינטות או תיבות תוחמות.

‫Gemini Robotics ER הוא גם סוכן: הוא מפרק משימות מורכבות למשימות משנה ומבצע אותן על ידי הפעלת פונקציות הרובוט או הפעלת קוד שנוצר. לדוגמה, המשפט "תשים את התפוח בקערה" הופך לרצף של שלבים: איתור, אחיזה והנחה.

במאמר [בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=he#how-it-works) מוסבר איך Gemini מבצע קריאות לכלים.

## בטיחות

‫Gemini Robotics ER נבנה תוך התחשבות בבטיחות, אבל האחריות לשמירה על סביבה בטוחה סביב הרובוט היא שלכם. מודלים של AI גנרטיבי עלולים לטעות, ורובוטים פיזיים עלולים לגרום נזק. מידע נוסף זמין ב[דף בנושא בטיחות רובוטים של Google DeepMind](https://deepmind.google/models/gemini-robotics/safety?hl=he).

## שיטות מומלצות

1. השתמשו בשפה פשוטה וטבעית. מתארים מה רוצים שהרובוט יעשה, כמו שמסבירים לאדם אחר. אם מונח מסוים לא עובד, נסו להשתמש במילה נרדפת נפוצה.
2. אופטימיזציה של קלט חזותי. לפני ששולחים את התמונה, כדאי לחתוך או לשנות את מרחק התצוגה של אובייקטים קטנים או לא ברורים. תאורה וניגודיות צבעים נמוכה יכולים להשפיע על הזיהוי.
3. כדאי לפצל משימות מורכבות לשלבים. כדי לשמור על המיקוד של המודל ולשפר את הדיוק, שולחים כל שלב כהנחיה נפרדת.
4. כדי לבצע משימות שדורשות דיוק גבוה, כדאי להריץ את השאילתה כמה פעמים ולחשב את ממוצע התוצאות. גישת הקונצנזוס הזו מצמצמת את השונות בתוצאות המרחביות.

## מגבלות

כשמפתחים באמצעות Gemini Robotics ER, חשוב לקחת בחשבון את המגבלות הבאות:

- **הגבלות על מפתחות API:** Gemini API לא מקבל בקשות ממפתחות API ללא הגבלות ומחזיר שגיאה `403 Forbidden`. כדי לאבטח את מפתח ה-API, מוסיפים הגבלות ב-[AI Studio](https://aistudio.google.com/api-keys?hl=he).
  פרטים נוספים זמינים במאמר בנושא [אבטחת מפתחות API ללא הגבלות](https://ai.google.dev/gemini-api/docs/api-key?hl=he#secure-unrestricted-keys).
- **זמן אחזור לעומת ביצועים:** שאילתות מורכבות, קלט ברזולוציה גבוהה או רמות חשיבה גבוהות יכולים להוביל לזמני עיבוד ארוכים יותר. לרמת החשיבה, כדאי להשתמש בערך 'בינוני' כדי ליצור איזון טוב בין זמן האחזור לביצועים.
- **הזיות:** כמו כל המודלים הגדולים של שפה, מודלים של Gemini Robotics ER יכולים מדי פעם "להזות" או לספק מידע שגוי, במיוחד בהנחיות מעורפלות או בקלט שהוא מחוץ להתפלגות.
- **תלות באיכות ההנחיה:** איכות הפלט תלויה בבהירות של ההנחיה. חשוב להשתמש בהנחיות ספציפיות ומובנות היטב.
- **עלות החישוב:** הפעלת המודל, במיוחד עם נתוני וידאו או עם `thinking_budget` גבוה, צורכת משאבי מחשוב וגוררת עלויות.
  פרטים נוספים מופיעים בדף [חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he).
- **סוגי קלט:** בקישורים הבאים מפורטות המגבלות של כל מצב.
  - [הוספת תמונות](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#technical-details-image)
  - [קלט של סרטונים](https://ai.google.dev/gemini-api/docs/video-understanding?hl=he#supported-formats)
  - [הוספת אודיו](https://ai.google.dev/gemini-api/docs/audio?hl=he#supported-formats)

## הודעת פרטיות

אתם מאשרים שהמודלים שמצוינים במסמך הזה ('מודלים של רובוטיקה') משתמשים בנתוני וידאו ואודיו כדי לפעול ולהזיז את החומרה בהתאם להוראות שלכם. לכן, יכול להיות שתפעילו את המודלים של הרובוטיקה כך שהם יאספו נתונים מאנשים שאפשר לזהות, כמו נתוני קול, תמונות ונתונים שקשורים לדמות שלהם ('מידע אישי'). אם תבחרו להפעיל את מודלי הרובוטיקה באופן שיאסוף מידע אישי, אתם מסכימים שלא תאפשרו לאנשים שניתן לזהות אותם ליצור אינטראקציה עם מודלי הרובוטיקה או להיות נוכחים באזור שמסביב להם, אלא אם כן הודעתם לאנשים שניתן לזהות אותם מראש שהמידע האישי שלהם עשוי להימסר ל-Google ולשמש אותה כפי שמפורט בתנאים והגבלות הנוספים לשירות של Gemini API שזמינים בכתובת [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=he) (התנאים), כולל בהתאם לקטע שכותרתו 'איך Google משתמשת בנתונים שלך'. תדאגו שההודעה תאפשר איסוף ושימוש במידע אישי כפי שמפורט בתנאים, ותפעלו באופן סביר מבחינה מסחרית כדי לצמצם את האיסוף וההפצה של מידע אישי באמצעות טכניקות כמו טשטוש פנים והפעלת מודלים רובוטיים באזורים שלא מכילים אנשים שניתן לזהות, במידת האפשר.

## תמחור

מידע מפורט על התמחור והאזורים הזמינים מופיע בדף [תמחור](https://ai.google.dev/gemini-api/docs/pricing?hl=he).

## נקודות קצה של מודלים

### ‫Gemini Robotics ER 2 Preview

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | `gemini-robotics-er-2-preview` |
| saveסוגי נתונים נתמכים | **קלטים**  טקסט, תמונות, סרטונים, אודיו  **פלט**  טקסט |
| ‫token\_autoמגבלות על טוקנים[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=he) | **מגבלת טוקנים של קלט**  131,072  **Output token limit**  65,536 |
| handymanיכולות | **[יצירת אודיו](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he)**  לא נתמך  **[שמירת נתונים במטמון](https://ai.google.dev/gemini-api/docs/caching?hl=he)**  נתמך  **[הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he)**  נתמך  **[שימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he)**  נתמך  **[חיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he)**  נתמך  **[בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)**  נתמך  **[עיגון בעזרת מפות Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he)**  נתמך  **[יצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he)**  לא נתמך  ‫**[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=he)**  לא נתמך  **[חיפוש עם עיגון בנתונים](https://ai.google.dev/gemini-api/docs/google-search?hl=he)**  נתמך  **[פלטים מובנים](https://ai.google.dev/gemini-api/docs/structured-output?hl=he)**  נתמך  **[חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he)**  נתמך  **[הקשר של כתובת ה-URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he)**  נתמך |
| speedאפשרויות צריכה | ‫**[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he)**  נתמך  **[הסקת מסקנות ב-Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=he)**  לא נתמך  **[הסקת עדיפות](https://ai.google.dev/gemini-api/docs/priority-inference?hl=he)**  לא נתמך |
| גרסאות 123 | פרטים נוספים זמינים במאמר בנושא [תבניות של גרסאות מודל](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#model-versions).  - תצוגה מקדימה: `gemini-robotics-er-2-preview` |
| calendar\_monthהעדכון האחרון | יולי 2026 |
| id\_cardכרטיס מודל | [כרטיס מודל](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=he) |

### ‫Gemini Robotics ER 2 Streaming Preview

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | `gemini-robotics-er-2-streaming-preview` |
| saveסוגי נתונים נתמכים | **קלטים**  טקסט, תמונות, סרטונים, אודיו  **פלט**  טקסט |
| ‫token\_autoמגבלות על טוקנים[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=he) | **מגבלת טוקנים של קלט**  131,072  **Output token limit**  65,536 |
| handymanיכולות | **[יצירת אודיו](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he)**  לא נתמך  **[שמירת נתונים במטמון](https://ai.google.dev/gemini-api/docs/caching?hl=he)**  לא נתמך  **[הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he)**  לא נתמך  **[שימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he)**  לא נתמך  **[חיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he)**  לא נתמך  **[בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)**  נתמך  **[עיגון בעזרת מפות Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he)**  לא נתמך  **[יצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he)**  לא נתמך  ‫**[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=he)**  נתמך  **[חיפוש עם עיגון בנתונים](https://ai.google.dev/gemini-api/docs/google-search?hl=he)**  נתמך  **[פלטים מובנים](https://ai.google.dev/gemini-api/docs/structured-output?hl=he)**  לא נתמך  **[חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he)**  נתמך  **[הקשר של כתובת ה-URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he)**  לא נתמך |
| speedאפשרויות צריכה | ‫**[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he)**  לא נתמך  **[הסקת מסקנות ב-Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=he)**  לא נתמך  **[הסקת עדיפות](https://ai.google.dev/gemini-api/docs/priority-inference?hl=he)**  לא נתמך |
| גרסאות 123 | פרטים נוספים זמינים במאמר בנושא [תבניות של גרסאות מודל](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#model-versions).  - תצוגה מקדימה: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthהעדכון האחרון | יולי 2026 |
| id\_cardכרטיס מודל | [כרטיס מודל](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=he) |

### ‫Gemini Robotics ER 1.6 Preview

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | `gemini-robotics-er-1.6-preview` |
| saveסוגי נתונים נתמכים | **קלטים**  טקסט, תמונות, סרטונים, אודיו  **פלט**  טקסט |
| ‫token\_autoמגבלות על טוקנים[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=he) | **מגבלת טוקנים של קלט**  131,072  **Output token limit**  65,536 |
| handymanיכולות | **[יצירת אודיו](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he)**  לא נתמך  **[שמירת נתונים במטמון](https://ai.google.dev/gemini-api/docs/caching?hl=he)**  נתמך  **[הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he)**  נתמך  **[שימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he)**  נתמך  **[חיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he)**  נתמך  **[בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)**  נתמך  **[עיגון בעזרת מפות Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he)**  נתמך  **[יצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he)**  לא נתמך  ‫**[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=he)**  לא נתמך  **[חיפוש עם עיגון בנתונים](https://ai.google.dev/gemini-api/docs/google-search?hl=he)**  נתמך  **[פלטים מובנים](https://ai.google.dev/gemini-api/docs/structured-output?hl=he)**  נתמך  **[חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he)**  נתמך  **[הקשר של כתובת ה-URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he)**  נתמך |
| speedאפשרויות צריכה | ‫**[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he)**  נתמך  **[הסקת מסקנות ב-Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=he)**  לא נתמך  **[הסקת עדיפות](https://ai.google.dev/gemini-api/docs/priority-inference?hl=he)**  לא נתמך |
| גרסאות 123 | פרטים נוספים זמינים במאמר בנושא [תבניות של גרסאות מודל](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#model-versions).  - תצוגה מקדימה: `gemini-robotics-er-1.6-preview` |
| calendar\_monthהעדכון האחרון | דצמבר 2025 |
| cognition\_2תאריך סף הידע | ינואר 2025 |

## המאמרים הבאים

- [היגיון מרחבי](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=he) – הצבעה, מעקב, תיבות תוחמות, מסלולים.
- [יכולות אג'נטיות](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=he) – ביצוע קוד, קריאת מכשירים, הוספת הערות לתמונות.
- [תיאום משימות](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=he) – משימות ארוכות טווח עם ממשקי API מותאמים אישית של רובוטים.
- [רובוטיקה עם סטרימינג](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=he) – סטרימינג דו-כיווני בזמן אמת (Gemini Robotics ER 2 בלבד).
- [הבנת סרטונים](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=he) – איתור רגעים וסיווג התקדמות (Gemini Robotics ER 2 בלבד).
- [בטיחות רובוטים של Google DeepMind](https://deepmind.google/models/gemini-robotics/safety?hl=he) – מחקר בטיחותי שמאחורי משפחת המודלים.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-30 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-30 (שעון UTC)."],[],[]]
