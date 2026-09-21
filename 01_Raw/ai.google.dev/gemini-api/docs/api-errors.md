---
source_url: https://ai.google.dev/gemini-api/docs/api-errors?hl=he
fetched_at: 2026-09-21T05:54:45.153898+00:00
title: "\u05e9\u05d2\u05d9\u05d0\u05d5\u05ea API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# שגיאות API

בדף הזה מפורטים כל קודי השגיאה של Interactions API, מתואר הפורמט של תגובת השגיאה ומוסבר איך ה-API מספק שגיאות לסוגים שונים של בקשות.

## קודי שגיאה של Standard API

קודי השגיאה הכלליים האלה ברמת הבקשה תואמים לקודי סטטוס רגילים של HTTP.
משתמשים בשדה `code` בלוגיקה של האפליקציה כדי לטפל בשגיאות באופן פרוגרמטי.

| קוד | סטטוס HTTP | תיאור | הפעולה המומלצת |
| --- | --- | --- | --- |
| `invalid_request` | ‫400 בקשה שגויה | מטען הייעודי (payload) של הבקשה לא תקין או שהוא מכיל פרמטרים לא תקינים. | כדאי לבדוק את התחביר והפרמטרים של הבקשה בהשוואה ל[מאמרי העזרה של ה-API](https://ai.google.dev/api/interactions-api?hl=he). |
| `failed_precondition` | ‫400 בקשה שגויה | אי אפשר לעבד את הבקשה כי לא מתקיימת דרישה מוקדמת (לדוגמה, חיוב מושבת). | צריך לבדוק את סטטוס החיוב של הפרויקט או את הדרישות המוקדמות של החשבון. |
| `out_of_range` | ‫‎416 Requested Range Not Satisfiable | פרמטר הבקשה חורג מהטווח התקין. | בודקים את ערכי הפרמטרים והמגבלות. |
| `parameter_unknown` | ‫400 בקשה שגויה | הבקשה מכילה פרמטר לא מוכר. | צריך להסיר את הפרמטר הלא מזוהה ולנסות שוב. |
| `authentication` | ‫401 אין הרשאה | מפתח ה-API חסר, לא תקין או שתוקפו פג. | מאמתים את [מפתח ה-API](https://ai.google.dev/gemini-api/docs/api-key?hl=he). |
| `payment_required` | ‫402 נדרש תשלום | יתרת הזיכוי בתשלום מראש אזלה. | [מוסיפים קרדיטים](https://ai.google.dev/gemini-api/docs/billing?hl=he#buy-credits) לחשבון לחיוב או מפעילים את התכונה [הוספת כסף אוטומטית](https://ai.google.dev/gemini-api/docs/billing?hl=he#auto-reload). לא כדאי לנסות שוב: הבקשה לא תצליח עד שיוספו קרדיטים. |
| `permission_denied` | ‫403 Forbidden | למפתח ה-API שלך אין הרשאה למשאב הזה. | בודקים את ההרשאות של מפתח ה-API ואת הגישה לפרויקט. |
| `not_found` | שגיאת 404 | המשאב המבוקש לא נמצא. | בודקים את נתיב המשאב והפרמטרים. |
| `model_not_found` | שגיאת 404 | המודל שצוין לא נמצא. | צריך לאמת את שם המודל או להשתמש במודל אחר. |
| `already_exists` | ‎409 Conflict | הישות שניסית ליצור כבר קיימת. | לפני שיוצרים מחדש משאב, בודקים אם הוא כבר קיים. |
| `aborted` | ‎409 Conflict | הפעולה בוטלה בגלל קונפליקט או בגלל כשל בבדיקת מקבילות. | כדאי לנסות לשלוח את הבקשה שוב ברמה גבוהה יותר של האפליקציה. |
| `rate_limit_exceeded` | ‫429 יותר מדי בקשות | חרגתם מהמגבלה של בקשות או טוקנים לדקה או לשנייה. | צריך להמתין ולנסות שוב עם השהיה מעריכית לפני ניסיון חוזר (exponential backoff). |
| `quota_exceeded` | ‫429 יותר מדי בקשות | חרגתם מהמכסה היומית. | צריך לחכות עד שהמכסה תתאפס או לבקש להגדיל את המכסה. |
| `too_many_requests` | ‫429 יותר מדי בקשות | שלחת יותר מדי בקשות בפרק זמן קצר. | צריך להמתין ולנסות שוב עם השהיה מעריכית לפני ניסיון חוזר (exponential backoff). |
| `cancelled` | ‫499 Client Closed Request | הלקוח ביטל את הבקשה לפני שהיא הושלמה. | אין צורך בפעולה נוספת. בדרך כלל זה אומר שהלקוח התנתק. |
| `api_error` | ‫‎500 Internal Server Error | קרתה שגיאה לא צפויה בשרת. | מנסים לשלוח את הבקשה שוב. אם הבעיה נמשכת, אפשר לפנות לתמיכה. |
| `unimplemented` | ‫501 Not Implemented | הפעולה או התכונה לא יושמו או לא נתמכות. | בודקים את היכולות של ה-API או עוברים לתכונה נתמכת. |
| `service_unavailable` | ‫‎503 Service Unavailable | יש כרגע עומס על השרות או שהוא מושבת. | צריך להמתין ולנסות שוב עם השהיה מעריכית לפני ניסיון חוזר (exponential backoff). |
| `deadline_exceeded` | ‫‎504 Gateway Timeout | הבקשה לא הושלמה עד המועד האחרון. | מסירים את הגדרת הזמן הקצוב לתפוגה של הלקוח או מגדילים אותה כדי להשתמש בברירת המחדל של השרת. |

## קודים שחסימת היצירה שלהם

קודי השגיאה האלה מציינים שהגבלות מדיניות, בטיחות או הגבלות תוכן חסמו את הפלט של המודל. אם מקבלים אחד מהקודים האלה, צריך לשנות את הקלט ולנסות שוב.

| קוד | תיאור |
| --- | --- |
| `safety` | הבקשה נחסמה בגלל הפרות של כללי הבטיחות (תוכן פוגעני). |
| `recitation` | הבקשה נחסמה בגלל הגבלות שקשורות לזכויות יוצרים או להקראה. |
| `language` | הבקשה נחסמה בגלל שפה שלא נתמכת. |
| `prohibited_content` | הבקשה נחסמה בגלל הנחיות לתוכן אסור. |
| `spii` | הבקשה נחסמה בגלל הגבלות על פרטים אישיים מזהים בעלי רגישות גבוהה. |
| `blocklist` | הבקשה נחסמה כי מונחים אסורים ברשימת החסימה חסמו אותה. |
| `image_safety` | הפרות של כללי הבטיחות חסמו את יצירת התמונה. |
| `image_prohibited_content` | ההנחיות בנושא תוכן אסור חסמו את יצירת התמונה. |
| `image_recitation` | הגבלות על זכויות יוצרים או על הקראה חסמו את יצירת התמונה. |
| `image_other` | יצירת התמונות נחסמה מסיבות לא מוגדרות. |
| `content_blocked` | הבקשה נחסמה בגלל סיבה שקשורה למדיניות, שלא צוינה. |

## קודי שגיאה ביצירה

קודי השגיאה האלה מציינים בעיה מבנית בפלט שנוצר על ידי המודל (למשל בקשה להפעלת פונקציה שגויה או בקשה להפעלת כלי שלא הוגדרה).

| קוד | תיאור |
| --- | --- |
| `malformed_function_call` | המודל יצר בקשה להפעלת פונקציה שלא ניתן לנתח. |
| `malformed_tool_call` | המודל יצר קריאה לכלי שלא ניתן לנתח. |
| `unexpected_tool_call` | המודל הפעיל כלי שלא הוגדר בבקשה. |
| `no_image` | המודל לא הצליח ליצור תמונה. |
| `too_many_tool_calls` | המודל יצר יותר קריאות לכלים מהמותר. |
| `missing_thought_signature` | בתגובה חסרה חתימת מחשבה נדרשת. |

## פורמט של תגובת שגיאה

כל השגיאות מ-Interactions API מחזירות אובייקט `error` שמכיל `code` ו-`message`. לדוגמה, העברת סוג כלי שלא נתמך מחזירה:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'. Supported values: 'function', 'code_execution', 'mcp_server', 'filesystem', 'google_maps', 'google_search', 'bash', 'computer_use', 'file_search', 'url_context'."
  }
}
```

| שדה | סוג | תיאור |
| --- | --- | --- |
| `code` | מחרוזת | קוד שגיאה שקריא למחשב ב`snake_case`. |
| `message` | מחרוזת | תיאור קריא לאנשים של מה שהשתבש. |

## איך השגיאות מועברות

ה-API מחזיר שגיאות בצורה שונה, בהתאם לסוג הבקשה ששולחים: בקשת HTTP רגילה או בקשת סטרימינג (SSE).

### בקשות HTTP רגילות

בבקשות רגילות (לא סטרימינג), ה-API מגדיר את קוד הסטטוס של תגובת ה-HTTP (למשל `400 Bad Request`, `401 Unauthorized` או `429 Too Many Requests`) ומחזיר אובייקט `error` בגוף תגובת ה-JSON:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'."
  }
}
```

### בקשות סטרימינג (SSE)

בבקשות סטרימינג (`stream: true`), ה-API שולח אירועי שגיאה דרך הסטרימינג של Server-Sent Events‏ (SSE) עם הערך `"error"` של `event_type`. השדה `error` מכיל את אותו מבנה של `code` ושל `message`:

```
{
  "event_type": "error",
  "error": {
    "code": "not_found",
    "message": "Failed to get completed interaction: Result not found."
  }
}
```

סכימת האירועים המלאה של SSE זמינה במאמר [Interactions API Reference](https://ai.google.dev/api/interactions-api?hl=he).

## המאמרים הבאים

- [פתרון בעיות ב-API](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=he): פתרון בעיות נפוצות ותרחישי שגיאה.
- [מגבלות קצב](https://ai.google.dev/gemini-api/docs/rate-limits?hl=he): מידע על מגבלות בקשות וניהול מכסות.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-20 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-20 (שעון UTC)."],[],[]]
