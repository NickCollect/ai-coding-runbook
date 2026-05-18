---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=he
fetched_at: 2026-05-18T05:18:45.626376+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)

# מגלים תובנות מהר יותר עם Gemini for Research

[קבלת מפתח Gemini API](https://aistudio.google.com/apikey?hl=he)

אפשר להשתמש במודלים של Gemini כדי לקדם מחקר בסיסי במגוון תחומים.
כך אפשר להשתמש ב-Gemini כדי לבצע מחקר:

- **ניתוח של פלט המודל ובקרה עליו**: כדי לבצע ניתוח נוסף, אתם יכולים לבדוק תשובה פוטנציאלית שנוצרה על ידי המודל באמצעות כלים כמו `CitationMetadata`. אפשר גם להגדיר אפשרויות ליצירת מודלים ולפלט, כמו `responseSchema`, `topP` ו-`topK`. [מידע נוסף](https://ai.google.dev/api/generate-content?hl=he)
- **קלט מולטי-מודאלי**: Gemini יכול לעבד תמונות, אודיו וסרטונים, מה שמאפשר מגוון רחב של כיווני מחקר מעניינים. [מידע נוסף](https://ai.google.dev/gemini-api/docs/vision?hl=he)
- **יכולות של הקשר ארוך**: מודלי Gemini 3.0 Flash ו-Pro מגיעים עם חלון הקשר של מיליון טוקנים. [מידע נוסף](https://ai.google.dev/gemini-api/docs/long-context?hl=he)
- **הסדנה הדיגיטלית של Google**: גישה מהירה למודלים של Gemini דרך ה-API ו-Google AI Studio לתרחישי שימוש בייצור. אם אתם מחפשים פלטפורמה מבוססת Google Cloud, פלטפורמת הסוכנים של Gemini Enterprise יכולה לספק תשתית תומכת נוספת.

כדי לתמוך במחקר אקדמי ולקדם מחקר מתקדם, Google מספקת גישה לקרדיטים של Gemini API למדענים ולחוקרים אקדמיים באמצעות [תוכנית Gemini Academic](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=he#gemini-academic-program).

## מתחילים לעבוד עם Gemini

‫Gemini API ו-Google AI Studio עוזרים לכם להתחיל לעבוד עם המודלים העדכניים ביותר של Google ולהפוך את הרעיונות שלכם לאפליקציות שניתנות להרחבה.

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="How large is the universe?",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "How large is the universe?"}]
    }]
   }'
```

## אנשי אקדמיה מומלצים

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=he)

"במחקר שלנו אנחנו בודקים את Gemini כמודל שפה חזותי (VLM) ואת ההתנהגויות שלו בסביבות מגוונות מנקודות מבט של חוסן ובטיחות. עד עכשיו, בדקנו את העמידות של Gemini בפני הסחות דעת כמו חלונות קופצים כשסוכני VLM מבצעים משימות במחשב, והשתמשנו ב-Gemini כדי לנתח אינטראקציות חברתיות, אירועים זמניים וגורמי סיכון על סמך קלט וידאו".

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=he)

‫Gemini Pro ו-Flash, עם חלון ההקשר הארוך שלהם, עוזרים לנו ב-OK-Robot, פרויקט המניפולציה שלנו בנייד עם אוצר מילים פתוח. ‫Gemini מאפשר לשלוח שאילתות ופקודות מורכבות בשפה טבעית לזיכרון של הרובוט: במקרה הזה, תצפיות קודמות שהרובוט ביצע במהלך פעולה ארוכה. גם אני ומאהי שפיאוללה משתמשים ב-Gemini כדי לפרק משימות לקוד שהרובוט יכול לבצע בעולם האמיתי".

## Gemini Academic Program

חוקרים אקדמיים שעומדים בדרישות (כמו חברי סגל, עובדים וסטודנטים לתואר שלישי) ב[מדינות נתמכות](https://ai.google.dev/gemini-api/docs/available-regions?hl=he) יכולים להגיש בקשה לקבלת קרדיטים ל-Gemini API ומגבלות שימוש גבוהות יותר לפרויקטים מחקריים. התמיכה הזו מאפשרת תפוקה גבוהה יותר בניסויים מדעיים ומקדמת את המחקר.

אנחנו מתעניינים במיוחד בתחומי המחקר שמפורטים בקטע הבא, אבל נשמח לקבל בקשות מתחומים מדעיים מגוונים:

- **הערכות ובנצ'מרקים**: שיטות הערכה שאושרו על ידי הקהילה ויכולות לספק אות חזק של ביצועים בתחומים כמו עובדתיות, בטיחות, ביצוע הוראות, חשיבה רציונלית ותכנון.
- **קידום גילויים מדעיים לטובת האנושות**: יישומים פוטנציאליים של AI במחקר מדעי רב-תחומי, כולל בתחומים כמו מחלות נדירות ומוזנחות, ביולוגיה ניסויית, מדע חומרים וקיימות.
- **התגלמות ואינטראקציות**: שימוש במודלים גדולים של שפה כדי לחקור אינטראקציות חדשות בתחומים של AI מבוסס-גוף, אינטראקציות סביבתיות, רובוטיקה ואינטראקציית אדם-מחשב.
- **יכולות מתפתחות**: בחינת יכולות של AI אקטיבי חדשות שנדרשות לשיפור חשיבה רציונלית ותכנון, ואיך אפשר להרחיב את היכולות במהלך היקש (למשל, באמצעות Gemini Flash).
- **אינטראקציה והבנה מולטי-מודאליות**: זיהוי פערים והזדמנויות במודלים בסיסיים מולטי-מודאליים לניתוח, להסקת מסקנות ולתכנון במגוון משימות.

הזכאות: רק אנשים פרטיים (חברי סגל, חוקרים או אנשים בתפקיד מקביל) שמשויכים למוסד אקדמי תקף או לארגון מחקר אקדמי יכולים להגיש בקשה. הערה: Google תעניק ותסיר גישה ל-API וקרדיטים לפי שיקול דעתה. אנחנו בודקים את הבקשות פעם בחודש.

### איך מתחילים לחקור באמצעות Gemini API

[להגשת בקשה](https://forms.gle/HMviQstU8PxC5iCt5)

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-13 (שעון UTC).

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-13 (שעון UTC)."],[],[]]
