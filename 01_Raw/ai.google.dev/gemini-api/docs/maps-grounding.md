---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he
fetched_at: 2026-07-20T04:34:29.326635+00:00
title: "\u05e2\u05d9\u05d2\u05d5\u05df \u05d1\u05e2\u05d6\u05e8\u05ea \u05de\u05e4\u05d5\u05ea Google \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# עיגון בעזרת מפות Google

העיגון באמצעות מפות Google מחבר את היכולות הגנרטיביות של Gemini לנתונים העשירים, העובדתיים והעדכניים של מפות Google. התכונה הזו מאפשרת למפתחים לשלב בקלות באפליקציות שלהם פונקציונליות שמבוססת על מיקום. כששאילתת משתמש מכילה הקשר שקשור לנתוני מפות, מודל Gemini משתמש במפות Google כדי לספק תשובות מדויקות מבחינה עובדתית ועדכניות שרלוונטיות למיקום הספציפי או לאזור הכללי שהמשתמש ציין.

- **תשובות מדויקות שמודעות למיקום:** שימוש בנתונים המקיפים והעדכניים של מפות Google לשאילתות ספציפיות מבחינה גיאוגרפית.
- **התאמה אישית משופרת:** התאמת ההמלצות והמידע על סמך המיקומים שהמשתמשים סיפקו.

## שנתחיל?

בדוגמה הזו אפשר לראות איך לשלב את התכונה Grounding עם מפות Google באפליקציה כדי לספק תשובות מדויקות לשאילתות של משתמשים, בהתאם למיקום שלהם. ההנחיה מבקשת המלצות מקומיות עם מיקום משתמש אופציונלי, ומאפשרת למודל Gemini להשתמש בנתונים של מפות Google.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## איך עיגון בעזרת מפות Google פועל

עיגון בעזרת מפות Google משלב את Gemini API עם המערכת האקולוגית של Google Geo באמצעות Maps API כמקור לעיגון. כששאילתה של משתמש מכילה הקשר גיאוגרפי, מודל Gemini יכול להפעיל את הכלי Grounding עם מפות Google. לאחר מכן המודל יכול ליצור תשובות שמבוססות על נתונים ממפות Google שרלוונטיים למיקום שצוין.

בדרך כלל התהליך כולל:

1. **שאילתת משתמש:** משתמש שולח שאילתה לאפליקציה שלכם, שיכולה לכלול הקשר גיאוגרפי (לדוגמה, "בתי קפה בקרבתי", "מוזיאונים בסן פרנסיסקו").
2. **הפעלת כלי:** מודל Gemini, שמזהה את הכוונה הגיאוגרפית, מפעיל את כלי ה-Grounding עם מפות Google. אפשר לספק לכלי הזה את `latitude` ו-`longitude` של המשתמש. הכלי הוא כלי לחיפוש טקסטואלי, והוא פועל באופן דומה לחיפוש במפות Google. כלומר, בשאילתות מקומיות ("בקרבתי") נעשה שימוש בקואורדינטות, בעוד שבשאילתות ספציפיות או לא מקומיות, לא סביר שהמיקום המפורש ישפיע על התוצאות.
3. **אחזור נתונים:** שירות ה-Grounding עם מפות Google שולח שאילתות למפות Google כדי לקבל מידע רלוונטי (לדוגמה, מקומות, ביקורות, תמונות, כתובות, שעות פתיחה).
4. **יצירה מבוססת-קרקע:** נתוני המפות שאוחזרו משמשים כדי לספק מידע לתשובה של מודל Gemini, וכך לוודא שהיא מדויקת ועניינית.
5. **תשובה והערות:** המודל מחזיר תשובה טקסטואלית עם הערות מוטבעות שמקשרות למקורות במפות Google, ומאפשרות למפתחים להציג ציטוטים.

## למה ומתי כדאי להשתמש בעיגון בעזרת מפות Google

ההארקה באמצעות מפות Google מתאימה במיוחד לאפליקציות שנדרש בהן מידע מדויק, עדכני וספציפי למיקום. הוא משפר את חוויית המשתמש באמצעות תוכן רלוונטי ומותאם אישית שמבוסס על מסד הנתונים הנרחב של מפות Google, שכולל יותר מ-250 מיליון מקומות ברחבי העולם.

כדאי להשתמש ב-Grounding עם מפות Google כשהאפליקציה צריכה:

- חשוב לענות על השאלות בצורה מקיפה ומדויקת.
- פיתוח כלים לשיחה לתכנון טיולים ומדריכים מקומיים.
- המלצה על נקודות עניין על סמך מיקום והעדפות משתמשים, כמו מסעדות או חנויות.
- ליצור חוויות מבוססות-מיקום לשירותים חברתיים, קמעונאיים או למשלוחי מזון.

ההארקה באמצעות מפות Google מצטיינת בתרחישי שימוש שבהם נתונים עובדתיים עדכניים וקרבה הם קריטיים, כמו חיפוש של "בית הקפה הכי טוב בסביבה שלי" או קבלת הוראות הגעה.

## תרחישים לדוגמה

העיגון בעזרת מפות Google תומך במגוון תרחישים לדוגמה שמתבססים על מיקום.

### איך עונים על שאלות ספציפיות לגבי מקום

אתם יכולים לשאול שאלות מפורטות על מקום ספציפי ולקבל תשובות שמבוססות על ביקורות של משתמשים ב-Google ועל נתונים אחרים במפות Google.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### התאמה אישית לפי מיקום

לקבל המלצות שמותאמות להעדפות של משתמש ולאזור גיאוגרפי ספציפי.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### עזרה בתכנון מסלול

יצירת תוכניות לכמה ימים עם הוראות הגעה ומידע על מיקומים שונים, מושלם לאפליקציות נסיעות.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## דרישות לשימוש בשירות

בקטע הזה מתוארות דרישות השימוש בשירות Grounding with Google Maps.

### לעדכן את המשתמש לגבי השימוש במקורות של מפות Google

לכל תוצאה במפות Google שנוצרה על ידי Gemini, תקבלו הערות על המקורות בבלוקי התוכן של שלב `model_output` שתומכים בכל תשובה. המטא-נתונים הבאים מוחזרים:

- כתובת אתר המקור
- שם

כשמציגים תוצאות של Grounding עם מפות Google, צריך לציין את המקורות המשויכים במפות Google ולעדכן את המשתמשים לגבי הדברים הבאים:

- המקורות של מפות Google צריכים להופיע מיד אחרי התוכן שנוצר ושנתמך על ידי המקורות. התוכן שנוצר נקרא גם תוצאה מבוססת-קרקע ב-Google Maps.
- מקורות המידע במפות Google צריכים להיות גלויים באינטראקציה אחת של המשתמש.

### הצגת מקורות של מפות Google עם קישורים למפות Google

לכל הערה למקור, צריך ליצור תצוגה מקדימה של קישור בהתאם לדרישות הבאות:

- צריך לשייך כל מקור למפות Google בהתאם [להנחיות לשיוך של טקסט במפות Google](#maps-attribution-guidelines).
- הצגת שם המקור שמופיע בתשובה.
- מקשרים למקור באמצעות `url` מההערה.

### הנחיות לציון מקורות במפות Google

כשמציינים את המקורות במפות Google בטקסט, חשוב לפעול לפי ההנחיות הבאות:

- אל תשנו את הטקסט 'מפות Google' בשום צורה:
  - אל תשנו את האותיות הרישיות של מפות Google.
  - אל תפצלו את כתובת מפות Google לכמה שורות.
  - אל תתאימו את מפות Google לשפה אחרת.
  - כדי למנוע מדפדפנים לתרגם את מפות Google, משתמשים בתכונת ה-HTML‏ translate="no".

מידע נוסף על חלק מספקי הנתונים של מפות Google ועל תנאי הרישיון שלהם מופיע [בהודעות המשפטיות של מפות Google ו-Google Earth](https://www.google.com/help/legalnotices_maps/?hl=he).

## שיטות מומלצות

- **ציון מיקום המשתמש:** כדי לקבל תשובות רלוונטיות ומותאמות אישית, תמיד צריך לכלול את `latitude` ו`longitude` בהגדרת הכלי `google_maps` כשמיקום המשתמש ידוע.
- **ליידע את משתמשי הקצה:** חשוב ליידע את משתמשי הקצה בצורה ברורה שהנתונים של מפות Google משמשים למענה על השאילתות שלהם, במיוחד כשהכלי מופעל.
- **השבתה כשלא צריך:** ההארקה באמצעות מפות Google מושבתת כברירת מחדל. כדי לשפר את הביצועים ולהוזיל עלויות, מפעילים את האפשרות הזו (`"tools": [{"type": "google_maps"}]`) רק כששאילתה כוללת הקשר גיאוגרפי ברור.

## מגבלות

- בשלב הזה, ההארקה באמצעות מפות Google תומכת רק בהנחיות ובתשובות באנגלית.
- יכול להיות שהכלי לא יהיה זמין בכל האזורים.
- התוצאות עשויות להשתנות בהתאם לדיוק המיקום ולנתונים הזמינים במפות Google.
- **היקף גיאוגרפי:** עיגון בעזרת מפות Google זמין בכל העולם.
- **מצב ברירת מחדל:** הכלי 'עיגון בעזרת מפות Google' מושבת כברירת מחדל.
  צריך להפעיל אותו באופן מפורש בבקשות ל-API.

## תמחור והגבלות על קצב יצירת הבקשות

התמחור של עיגון בעזרת מפות Google משתנה בהתאם לדור המודל:

- **מודלים של Gemini 3:** הפרויקט שלכם יחויב על כל **שאילתת חיפוש** שהמודל יחליט לבצע. **הנחיית חיפוש** אחת (בקשת ה-API שלכם למודל) עשויה לגרום למודל להריץ כמה שאילתות חיפוש כדי למצוא את המידע הדרוש. כל אחת מהשאילתות האלה נחשבת לשימוש בתשלום בכלי.
- ‫**Gemini 2.5 ומודלים ישנים יותר:** החיוב על הפרויקט מתבצע לפי **הנחיה לחיפוש**.
  חיוב על בקשה מתבצע רק אם ההנחיה מחזירה בהצלחה לפחות תוצאה אחת מבוססת-קרקע של מפות Google, ללא קשר למספר שאילתות החיפוש הנפרדות שהמודל ביצע באופן פנימי כדי לקבל את התוצאה הזו.

מידע מפורט על התמחור זמין ב[דף התמחור של Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=he).

## מודלים נתמכים

המודלים הבאים תומכים בעיגון בעזרת מפות Google:

| מודל | עיגון בעזרת מפות Google |
| --- | --- |
| ‫[Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=he) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=he) | ✔️ |
| ‫[Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=he) | ✔️ |
| [תצוגה מקדימה של Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=he) | ✔️ |
| ‫[Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=he) | ✔️ |

## שילובים נתמכים של כלים

מודלים של Gemini 3 תומכים בשילוב של כלים מובנים (כמו עיגון באמצעות מפות Google) עם כלים מותאמים אישית (קריאה לפונקציה). מידע נוסף זמין בדף [שילובים של כלים](https://ai.google.dev/gemini-api/docs/tool-combination?hl=he).

## המאמרים הבאים

- [מידע על כלים נוספים](https://ai.google.dev/gemini-api/docs/tools?hl=he)
- כדי לקבל מידע נוסף על שיטות מומלצות לשימוש אחראי ב-AI ועל מסנני הבטיחות של Gemini API, אפשר לעיין [במדריך להגדרות הבטיחות](https://ai.google.dev/gemini-api/docs/safety-settings?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-06 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-06 (שעון UTC)."],[],[]]
