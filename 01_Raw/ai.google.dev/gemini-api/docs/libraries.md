---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=he
fetched_at: 2026-06-29T05:28:20.472508+00:00
title: "\u05e1\u05e4\u05e8\u05d9\u05d5\u05ea Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# ספריות Gemini API

כשמפתחים באמצעות Gemini API, מומלץ להשתמש ב-**Google GenAI SDK**.
אלה ספריות רשמיות שמוכנות לשימוש בסביבת ייצור, שאנחנו מפתחים ומתחזקים עבור השפות הפופולריות ביותר. הם נמצאים ב[זמינות כללית](https://ai.google.dev/gemini-api/docs/libraries?hl=he#new-libraries) ומשמשים בכל הדוגמאות והמסמכים הרשמיים שלנו.

אם זו הפעם הראשונה שאתם משתמשים ב-Gemini API, כדאי לעיין ב[מדריך לתחילת העבודה](https://ai.google.dev/gemini-api/docs/get-started?hl=he).

## שפות נתמכות והתקנה

‫Google GenAI SDK זמין לשפות Python, ‏ JavaScript/TypeScript, ‏ Go ו-Java. אפשר להתקין את הספרייה של כל שפה באמצעות מנהלי חבילות, או להיכנס למאגרי GitHub שלהן כדי לקבל מידע נוסף:

### Python

- ספרייה: [`google-genai`](https://pypi.org/project/google-genai)
- מאגר GitHub: ‏ [googleapis/python-genai](https://github.com/googleapis/python-genai)
- התקנה: `pip install google-genai`

### JavaScript

- ספרייה: [`@google/genai`](https://www.npmjs.com/package/@google/genai)
- מאגר GitHub: ‏ [googleapis/js-genai](https://github.com/googleapis/js-genai)
- התקנה: `npm install @google/genai`

### Go

- ספרייה: [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)
- מאגר GitHub: ‏ [googleapis/go-genai](https://github.com/googleapis/go-genai)
- התקנה: `go get google.golang.org/genai`

### Java

- ספרייה: `google-genai`
- מאגר GitHub: ‏ [googleapis/java-genai](https://github.com/googleapis/java-genai)
- התקנה: אם משתמשים ב-Maven, מוסיפים את הקוד הבא ליחסי התלות:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#‎

- ספרייה: `Google.GenAI`
- מאגר GitHub: ‏ [googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)
- התקנה: `dotnet add package Google.GenAI`

## זמינות לכלל המשתמשים (GA)

החל ממאי 2025, ערכת Google GenAI SDK זמינה לכלל המשתמשים (GA) בכל הפלטפורמות הנתמכות, והיא הספרייה המומלצת לגישה ל-Gemini API.
הן יציבות, נתמכות באופן מלא לשימוש בשלב הייצור ומתעדכנות באופן פעיל.
הם מספקים גישה לתכונות העדכניות ביותר ומציעים את הביצועים הטובים ביותר בעבודה עם Gemini.

אם אתם משתמשים באחת מהספריות מדור קודם שלנו, מומלץ מאוד לבצע מיגרציה כדי שתוכלו לגשת לתכונות העדכניות ביותר וליהנות מהביצועים הטובים ביותר בעבודה עם Gemini. מידע נוסף זמין בקטע בנושא [ספריות מדור קודם](https://ai.google.dev/gemini-api/docs/libraries?hl=he#previous-sdks).

## ספריות קודמות והעברה

אם אתם משתמשים באחת מהספריות הקודמות שלנו, מומלץ [לעבור לספריות החדשות](https://ai.google.dev/gemini-api/docs/migrate?hl=he).

הספריות מדור קודם לא מספקות גישה לתכונות חדשות (כמו [Live API](https://ai.google.dev/gemini-api/docs/live?hl=he) ו-[Veo](https://ai.google.dev/gemini-api/docs/video?hl=he)), והן יוצאו משימוש החל מ-30 בנובמבר 2025.

סטטוס התמיכה של כל ספרייה מהדור הקודם משתנה, והוא מפורט בטבלה הבאה:

| שפה | ספרייה מדור קודם | סטטוס התמיכה | ספרייה מומלצת |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | לא מתבצע תחזוקה פעילה | `google-genai` |
| ‫**JavaScript/TypeScript** | `@google/generativeai` | לא מתבצע תחזוקה פעילה | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | לא מתבצע תחזוקה פעילה | `google.golang.org/genai` |
| **Dart ו-Flutter** | `google_generative_ai` | לא מתבצע תחזוקה פעילה | משתמשים ב-[Genkit Dart](https://genkit.dev/docs/dart/get-started/) או ב-[Firebase AI Logic](https://pub.dev/packages/firebase_ai) |
| **Swift** | `generative-ai-swift` | לא מתבצע תחזוקה פעילה | שימוש ב-[Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=he) |
| **Android** | `generative-ai-android` | לא מתבצע תחזוקה פעילה | שימוש ב-[Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=he) |

**הערה למפתחי Java:** לא הייתה גרסה קודמת של Java SDK שסופקה על ידי Google ל-Gemini API, ולכן לא נדרש מעבר מספרייה קודמת של Google. אפשר להתחיל ישירות עם הספרייה החדשה בקטע [תמיכה בשפות והתקנה](#install).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-06-22 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-06-22 (שעון UTC)."],[],[]]
