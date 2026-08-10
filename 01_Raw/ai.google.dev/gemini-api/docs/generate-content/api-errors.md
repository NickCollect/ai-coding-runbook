---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-errors?hl=he
fetched_at: 2026-08-10T03:17:51.111860+00:00
title: "\u05e9\u05d2\u05d9\u05d0\u05d5\u05ea API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# שגיאות API

בדף הזה מפורטים קודי השגיאה של הבק-אנד שמוחזרים על ידי `GenerateContent` API, מוסבר פורמט התגובה של שגיאת gRPC ומפורטים שלבים לפתרון בעיות.

## קודי שגיאה של HTTP

בטבלה הבאה מפורטים קודי שגיאה נפוצים של ה-Backend, הסברים לגבי הסיבות לשגיאות ופתרונות מומלצים:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **קוד HTTP** | **סטטוס** | **תיאור** | **דוגמה** | **המוצר** |
| 400 | INVALID\_ARGUMENT | גוף הבקשה לא תקין. | יש שגיאת הקלדה או שדה חובה חסר בבקשה. | ב[הפניית ה-API](https://ai.google.dev/api?hl=he) אפשר למצוא מידע על פורמט הבקשות, דוגמאות וגרסאות נתמכות. שימוש בתכונות מגרסת API חדשה יותר עם נקודת קצה ישנה יותר עלול לגרום לשגיאות. |
| 400 | FAILED\_PRECONDITION | השימוש ב-Gemini API בחינם לא זמין במדינה שלך. צריך להפעיל את החיוב בפרויקט ב-Google AI Studio. | אתם שולחים בקשה באזור שבו לא נתמך מסלול חינמי, ולא הפעלתם חיוב בפרויקט שלכם ב-Google AI Studio. | כדי להשתמש ב-Gemini API, תצטרכו להגדיר תוכנית בתשלום באמצעות [Google AI Studio](https://aistudio.google.com/apikey?hl=he). |
| 403 | PERMISSION\_DENIED | למפתח ה-API שלכם אין את ההרשאות הנדרשות. | אתם משתמשים במפתח API שגוי. אתם מנסים להשתמש במודל שעבר התאמה בלי לעבור [אימות תקין](https://ai.google.dev/gemini-api/docs/model-tuning?hl=he). | בודקים שמפתח ה-API מוגדר ושיש לו את הגישה הנכונה. כדי להשתמש במודלים שעברו התאמה אישית, חשוב לוודא שאתם עוברים אימות תקין. |
| 404 | NOT\_FOUND | המשאב המבוקש לא נמצא. | לא נמצא קובץ תמונה, אודיו או וידאו שההפניה אליו מופיעה בבקשה. | בודקים אם כל הפרמטרים בבקשה תקפים לגרסת ה-API שלכם. |
| 429 | RESOURCE\_EXHAUSTED | חרגתם מאחת ממגבלות הקצב של ה-API (RPM,‏ TPM,‏ RPD, הוצאות וכו'). | אתם שולחים יותר מדי בקשות, משתמשים ביותר מדי טוקנים או חורגים מהמגבלות שמבוססות על הוצאות בהיסטוריית החיובים ובדרגה של החשבון. | מוודאים שאתם עומדים ב[מגבלות הקצב](https://ai.google.dev/gemini-api/docs/rate-limits?hl=he) של המודל. מחכים קצת ומנסים שוב. צריך להקטין את הקצב או את הגודל של הבקשות. במקרה הצורך, [מבקשים להגדיל את מגבלת קצב הבקשות](https://ai.google.dev/gemini-api/docs/rate-limits?hl=he#request-rate-limit-increase). |
| 499 | בוטלה | הפעולה בוטלה, בדרך כלל על ידי המתקשר. | הלקוח סגר את החיבור לפני שה-API סיים להגיב. | בודקים אם הלקוח או תשתית הרשת סוגרים את החיבור לפני הזמן (למשל, בגלל זמן קצוב לתפוגה בצד הלקוח). |
| 500 | פנימי | קרתה שגיאה לא צפויה בצד של Google. | הקשר של הקלט ארוך מדי. | כדאי לבדוק את [דף הסטטוס של Gemini API](https://aistudio.google.com/status?hl=he) כדי לראות אם יש תקריות שמתרחשות כרגע. כדאי לצמצם את הקשר של הקלט או לעבור זמנית למודל אחר (למשל מ-Gemini 2.5 Pro ל-Gemini 2.5 Flash) ולבדוק אם זה עוזר. אפשר גם להמתין קצת ולנסות שוב לשלוח את הבקשה. אם הבעיה נמשכת אחרי שמנסים שוב, אפשר לדווח עליה באמצעות הכפתור **שליחת משוב** ב-Google AI Studio. |
| 503 | UNAVAILABLE | יכול להיות שהשירות עמוס מדי או מושבת באופן זמני. | השירות לא זמין באופן זמני בגלל חוסר קיבולת. | כדאי לבדוק את [דף הסטטוס של Gemini API](https://aistudio.google.com/status?hl=he) כדי לראות אם יש תקריות שמתרחשות כרגע. עוברים באופן זמני למודל אחר (למשל מ-Gemini 2.5 Pro ל-Gemini 2.5 Flash) ובודקים אם זה עובד. אפשר גם להמתין קצת ולנסות שוב לשלוח את הבקשה. אם הבעיה נמשכת אחרי שמנסים שוב, אפשר לדווח עליה באמצעות הכפתור **שליחת משוב** ב-Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | השירות לא יכול לסיים את העיבוד עד למועד האחרון. | ההנחיה (או ההקשר) גדולה מדי לעיבוד בזמן. | כדי להימנע מהשגיאה הזו, צריך להגדיר ערך גבוה יותר של 'זמן קצוב לתפוגה' בבקשת הלקוח. |

## פורמט של תגובת שגיאה

כשבקשת `GenerateContent` נכשלת, ה-API מגדיר את קוד הסטטוס של HTTP (למשל `400 Bad Request`, `403 Forbidden` או `429 Too Many Requests`) ומחזיר גוף תגובה בפורמט JSON שמכיל פרטי סטטוס של gRPC:

```
{
  "error": {
    "code": 400,
    "message": "API key not valid. Please pass a valid API key.",
    "status": "INVALID_ARGUMENT",
    "details": [
      {
        "@type": "type.googleapis.com/google.rpc.ErrorInfo",
        "reason": "API_KEY_INVALID",
        "domain": "googleapis.com",
        "metadata": {
          "service": "generativelanguage.googleapis.com"
        }
      },
      {
        "@type": "type.googleapis.com/google.rpc.LocalizedMessage",
        "locale": "en-US",
        "message": "API key not valid. Please pass a valid API key."
      }
    ]
  }
}
```

| שדה | סוג | תיאור |
| --- | --- | --- |
| `code` | מספר שלם | קוד הסטטוס של HTTP. |
| `message` | מחרוזת | תיאור של השגיאה שכתוב בצורה שקריאה לאנשים. |
| `status` | מחרוזת | קוד הסטטוס של gRPC ב-`SCREAMING_CASE`. |
| `details` | מערך | הקשר נוסף של השגיאה, כמו `ErrorInfo` או `LocalizedMessage`. |

## המאמרים הבאים

- [פתרון בעיות ב-API](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=he): פתרון בעיות נפוצות ותרחישי שגיאה.
- [מגבלות קצב](https://ai.google.dev/gemini-api/docs/rate-limits?hl=he): מידע על מגבלות בקשות וטיפול במכסות.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-30 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-30 (שעון UTC)."],[],[]]
