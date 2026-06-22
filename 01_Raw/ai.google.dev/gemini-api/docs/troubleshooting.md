---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=he
fetched_at: 2026-06-22T06:33:15.533804+00:00
title: "\u05de\u05d3\u05e8\u05d9\u05da \u05dc\u05e4\u05ea\u05e8\u05d5\u05df \u05d1\u05e2\u05d9\u05d5\u05ea \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# מדריך לפתרון בעיות

המדריך הזה יעזור לכם לאבחן ולפתור בעיות נפוצות שמתעוררות כשקוראים ל-Gemini API. יכול להיות שתיתקלו בבעיות בשירות הקצה העורפי של Gemini API או בערכות ה-SDK של הלקוח. ערכות ה-SDK ללקוחות שלנו מבוססות על קוד פתוח במאגרים הבאים:

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

אם נתקלתם בבעיות במפתח API, ודאו שהגדרתם אותו בצורה נכונה לפי [מדריך ההגדרה של מפתח API](https://ai.google.dev/gemini-api/docs/api-key?hl=he).

## קודי שגיאה של שירות הקצה העורפי של Gemini API

בטבלה הבאה מפורטים קודי שגיאה נפוצים של ה-Backend שאולי תיתקלו בהם, יחד עם הסברים לגבי הסיבות להם ושלבים לפתרון בעיות:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **קוד HTTP** | **סטטוס** | **תיאור** | **דוגמה** | **המוצר** |
| 400 | INVALID\_ARGUMENT | גוף הבקשה לא תקין. | יש שגיאת הקלדה או שדה חובה חסר בבקשה. | כדאי לעיין ב[הפניית ה-API](https://ai.google.dev/api?hl=he) כדי לראות את פורמט הבקשה, דוגמאות וגרסאות נתמכות. שימוש בתכונות מגרסת API חדשה יותר עם נקודת קצה ישנה יותר עלול לגרום לשגיאות. |
| 400 | FAILED\_PRECONDITION | התוכנית בחינם של Gemini API לא זמינה במדינה שלך. צריך להפעיל את החיוב בפרויקט ב-Google AI Studio. | אתם שולחים בקשה באזור שבו לא נתמך מסלול חינמי, ולא הפעלתם חיוב בפרויקט שלכם ב-Google AI Studio. | כדי להשתמש ב-Gemini API, תצטרכו להגדיר תוכנית בתשלום באמצעות [Google AI Studio](https://aistudio.google.com/apikey?hl=he). |
| 403 | PERMISSION\_DENIED | למפתח ה-API שלכם אין את ההרשאות הנדרשות. | אתם משתמשים במפתח API שגוי. אתם מנסים להשתמש במודל שעבר התאמה בלי לעבור [אימות תקין](https://ai.google.dev/gemini-api/docs/model-tuning?hl=he). | צריך לוודא שמפתח ה-API מוגדר ושיש לו את הגישה הנכונה, וגם לוודא שאתם עוברים אימות תקין כדי להשתמש במודלים מכווננים. |
| 404 | NOT\_FOUND | המשאב המבוקש לא נמצא. | לא נמצא קובץ תמונה, אודיו או וידאו שההפניה אליו מופיעה בבקשה. | צריך לבדוק אם כל [הפרמטרים בבקשה תקפים](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=he#check-api) לגרסת ה-API שלכם. |
| 429 | RESOURCE\_EXHAUSTED | חרגת ממגבלת הקצב. | אתם שולחים יותר מדי בקשות לדקה באמצעות Gemini API בתוכנית בחינם. | מוודאים שלא חרגתם מ[מגבלת הקצב](https://ai.google.dev/gemini-api/docs/rate-limits?hl=he) של המודל. אם צריך, [מבקשים להגדיל את המכסה](https://ai.google.dev/gemini-api/docs/rate-limits?hl=he#request-rate-limit-increase). |
| 499 | בוטלה | הפעולה בוטלה, בדרך כלל על ידי המתקשר. | הלקוח סגר את החיבור לפני שה-API סיים להגיב. | בודקים אם הלקוח או תשתית הרשת סוגרים את החיבור לפני הזמן (למשל, בגלל זמן קצוב לתפוגה בצד הלקוח). |
| 500 | פנימי | קרתה שגיאה לא צפויה בצד של Google. | הקשר של הקלט ארוך מדי. | כדאי לבדוק את [דף הסטטוס של Gemini API](https://aistudio.google.com/status?hl=he) כדי לראות אם יש תקריות שמתרחשות כרגע. כדאי לצמצם את הקשר של הקלט או לעבור באופן זמני למודל אחר (למשל מ-Gemini 2.5 Pro ל-Gemini 2.5 Flash) ולבדוק אם זה עוזר. אפשר גם להמתין קצת ולנסות שוב לשלוח את הבקשה. אם הבעיה נמשכת אחרי שמנסים שוב, אפשר לדווח עליה באמצעות הכפתור **שליחת משוב** ב-Google AI Studio. |
| 503 | UNAVAILABLE | יכול להיות שהשירות עמוס מדי או מושבת באופן זמני. | השירות לא זמין כרגע בגלל עומס. | כדאי לבדוק את [דף הסטטוס של Gemini API](https://aistudio.google.com/status?hl=he) כדי לראות אם יש תקריות שמתרחשות כרגע. עוברים באופן זמני למודל אחר (למשל מ-Gemini 2.5 Pro ל-Gemini 2.5 Flash) ובודקים אם זה עובד. אפשר גם להמתין קצת ולנסות שוב לשלוח את הבקשה. אם הבעיה נמשכת אחרי שמנסים שוב, אפשר לדווח עליה באמצעות הכפתור **שליחת משוב** ב-Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | השירות לא יכול לסיים את העיבוד עד למועד האחרון. | ההנחיה (או ההקשר) גדולה מדי לעיבוד בזמן. | כדי להימנע מהשגיאה הזו, צריך להגדיר ערך גבוה יותר של 'זמן קצוב לתפוגה' בבקשת הלקוח. |

## בדיקה של שגיאות בפרמטרים של המודל בקריאות ל-API

מוודאים שהפרמטרים של המודל נמצאים בטווח הערכים הבא:

|  |  |
| --- | --- |
| **פרמטר של מודל** | **ערכים (טווח)** |
| מספר המועמדים | ‫1-8 (מספר שלם) |
| טמפרטורה | ‫0.0-1.0 |
| מספר מקסימלי של טוקנים בפלט | אפשר להיעזר ב[דף המודלים](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he) כדי לקבוע את המספר המקסימלי של טוקנים למודל שבו אתם משתמשים. |
| TopP | ‫0.0-1.0 |

בנוסף לבדיקת ערכי הפרמטרים, חשוב לוודא שאתם משתמשים ב[גרסת ה-API](https://ai.google.dev/gemini-api/docs/api-versions?hl=he) הנכונה (למשל, `/v1` או `/v1beta`) ובמודל שתומך בתכונות שאתם צריכים. לדוגמה, אם תכונה מסוימת נמצאת בגרסת בטא, היא תהיה זמינה רק בגרסת API‏ `/v1beta`.

## בדיקה אם יש לכם את הדגם הנכון

ודאו שאתם משתמשים במודל נתמך שמופיע ב[דף המודלים](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he).

## זמן אחזור ארוך יותר או שימוש גבוה יותר בטוקנים עם מודלים 2.5

אם אתם רואים שהחביון או השימוש באסימונים גבוהים יותר במודלים 2.5 Flash ו-Pro, יכול להיות שהסיבה לכך היא ש**החשיבה מופעלת כברירת מחדל** כדי לשפר את האיכות. אם אתם רוצים לתת עדיפות למהירות או לצמצם עלויות, אתם יכולים לשנות את ההגדרות של החשיבה או להשבית אותה.

ב[דף החשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he#set-budget) אפשר למצוא הנחיות וקוד לדוגמה.

## בעיות בטיחות

אם מופיעה הודעה שהנחיה נחסמה בגלל הגדרת בטיחות בקריאה ל-API, צריך לבדוק את ההנחיה בהתאם למסננים שהגדרתם בקריאה ל-API.

אם מופיע הסמל `BlockedReason.OTHER`, יכול להיות שהשאילתה או התשובה מפרות את [התנאים וההגבלות](https://ai.google.dev/terms?hl=he) או שהן לא נתמכות.

## בעיה בהקראה

אם המודל מפסיק ליצור פלט בגלל הסיבה RECITATION, המשמעות היא שהפלט מהמודל עשוי להיות דומה לנתונים מסוימים. כדי לפתור את הבעיה, כדאי לנסות להפוך את ההנחיה או ההקשר לייחודיים ככל האפשר ולהשתמש ברמת אקראיות גבוהה יותר.

## בעיה של טוקנים חוזרים

אם אתם רואים טוקנים של פלט שחוזרים על עצמם, נסו את ההצעות הבאות כדי לצמצם או לבטל אותם.

| תיאור | סיבה | הצעה לפתרון עקיף |
| --- | --- | --- |
| מקפים חוזרים בטבלאות Markdown | זה יכול לקרות כשהתוכן בטבלה ארוך, כי המודל מנסה ליצור טבלת Markdown עם יישור חזותי. עם זאת, היישור ב-Markdown לא נחוץ כדי שהעיבוד יהיה תקין. | כדי לתת למודל הנחיות ספציפיות ליצירת טבלאות בפורמט Markdown, צריך להוסיף הוראות בהנחיה. לספק דוגמאות שפועלות לפי ההנחיות האלה. אפשר גם לנסות לשנות את הטמפרטורה. כדי ליצור קוד או פלט מובנה מאוד כמו טבלאות Markdown, עדיף להשתמש ברמת אקראיות גבוהה (‎>= 0.8).  זו דוגמה להנחיות שאפשר להוסיף להנחיה כדי למנוע את הבעיה הזו:     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| טוקנים חוזרים בטבלאות Markdown | בדומה למקפים החוזרים, זה קורה כשהמודל מנסה ליישר חזותית את התוכן של הטבלה. ההזחה ב-Markdown לא נדרשת כדי שהעיבוד יהיה תקין. | - נסו להוסיף להנחיית המערכת הוראות כמו אלה:      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - כדאי לנסות לשנות את הטמפרטורה. טמפרטורות גבוהות יותר (>= 0.8)   עוזרות בדרך כלל למנוע חזרות או כפילויות בתוצאה. |
| שורה חדשה חוזרת (`\n`) בפלט מובנה | אם קלט המודל מכיל רצפי Unicode או רצפי escape כמו `\u` או `\t`, יכול להיות שיופיעו שורות חדשות חוזרות. | - בודקים אם יש רצפי escape אסורים ומחליפים אותם בתווי UTF-8 בהנחיה. לדוגמה, אם בדוגמאות של JSON יש רצף escape של `\u`   , המודל עלול להשתמש בו גם בפלט שלו. - לתת למודל הוראות לגבי יציאות מותרות. מוסיפים הוראה למערכת כמו זו:      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| טקסט שחוזר על עצמו בשימוש בפלט מובנה | אם הפלט של המודל כולל את השדות בסדר שונה מזה של הסכימה המובנית שהוגדרה, הדבר עלול להוביל לחזרה על טקסט. | - אל תציינו את סדר השדות בהנחיה. - הופכים את כל שדות הפלט לשדות חובה. |
| קריאות חוזרות לכלי | זה יכול לקרות אם המודל מאבד את ההקשר של מחשבות קודמות או אם הוא קורא לנקודת קצה לא זמינה שהוא נאלץ לקרוא לה. | להנחות את המודל לשמור על מצב בתוך תהליך החשיבה שלו. מוסיפים את ההוראה הזו לסוף ההוראות למערכת:    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| טקסט חוזר שלא מהווה חלק מפלט מובנה | זה יכול לקרות אם המודל נתקע בבקשה שהוא לא יכול לפתור. | - אם התכונה 'חשיבה' מופעלת, אל תתנו הוראות מפורשות לגבי אופן החשיבה על פתרון בעיה. פשוט מבקשים את הפלט הסופי. - נסו טמפרטורה גבוהה יותר >= 0.8. - מוסיפים הוראות כמו "תמציתיות", "לא לחזור על עצמך" או "לספק את התשובה פעם אחת". |

## מפתחות API חסומים או לא תקינים

בקטע הזה מוסבר איך לבדוק אם מפתח Gemini API שלכם חסום ומה אפשר לעשות כדי לפתור את הבעיה.

### למה מפתחות נחסמים

זיהינו פרצת אבטחה שבה חלק ממפתחות ה-API נחשפו באופן ציבורי. כדי להגן על הנתונים שלכם ולמנוע גישה לא מורשית, חסמנו באופן יזום את הגישה ל-Gemini API של מפתחות ידועים שדלפו.

### איך בודקים אם המפתחות מושפעים

אם ידוע שמפתח נחשף, אי אפשר יותר להשתמש בו עם Gemini API. אתם יכולים להשתמש ב-[Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=he) כדי לבדוק אם יש מפתחות API שחסימתם מונעת מהם לבצע קריאות ל-Gemini API, וליצור מפתחות חדשים. יכול להיות שתוצג גם השגיאה הבאה כשמנסים להשתמש במפתחות האלה:

```
Your API key was reported as leaked. Please use another API key.
```

### פעולה למפתחות API חסומים

מומלץ ליצור מפתחות API חדשים לשילובים של Gemini API באמצעות [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=he). מומלץ מאוד לבדוק את שיטות הניהול של מפתחות ה-API כדי לוודא שהמפתחות החדשים מאובטחים ולא נחשפים לציבור.

### חיובים לא צפויים בגלל פגיעות

[שליחת פנייה בנושא חיוב](https://console.cloud.google.com/support/chat?hl=he). צוות החיוב שלנו מטפל בבעיה הזו, ונעדכן אותך בהקדם האפשרי.

### אמצעי האבטחה של Google למפתחות שנחשפו

**איך Google תעזור לי לאבטח את החשבון מפני חריגה מהתקציב ושימוש לרעה אם מפתחות ה-API שלי ידלפו?**

- אנחנו עוברים למצב שבו כשמבקשים מפתח חדש באמצעות [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=he), המערכת מנפיקה מפתחות API שמוגבלים כברירת מחדל לשימוש ב-Google AI Studio בלבד, ולא מקבלת מפתחות משירותים אחרים.
  כך תוכלו למנוע שימוש לא מכוון במפתחות שונים.
- כברירת מחדל, אנחנו חוסמים מפתחות API שדלפו ונעשה בהם שימוש ב-Gemini API, כדי למנוע שימוש לרעה בעלויות ובנתוני האפליקציה.
- תוכלו לראות את הסטטוס של מפתחות ה-API ב-[Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=he). אם נזהה שמפתחות ה-API שלכם נחשפו, נעדכן אתכם באופן יזום כדי שתוכלו לפעול באופן מיידי.

## שיפור הפלט של המודל

כדי לקבל פלט איכותי יותר מהמודל, כדאי לנסות לכתוב הנחיות מובנות יותר. בדף [מדריך להנדסת הנחיות](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=he) מוסברים כמה מושגים בסיסיים, אסטרטגיות ושיטות מומלצות שיעזרו לכם להתחיל.

## הסבר על מגבלות הטוקנים

כדאי לעיין ב[מדריך האסימונים](https://ai.google.dev/gemini-api/docs/tokens?hl=he) כדי להבין טוב יותר איך לספור אסימונים ומהן המגבלות שלהם.

## בעיות מוכרות

- ה-API תומך רק במספר שפות נבחרות. אם תשלחו הנחיות בשפות שלא נתמכות, יכול להיות שתקבלו תשובות לא צפויות או שהתשובות ייחסמו. [כאן](https://ai.google.dev/gemini-api/docs/models?hl=he#supported-languages) אפשר לראות את השפות שזמינות לעדכונים.

## דיווח על באג

אם יש לכם שאלות, אתם יכולים להצטרף לדיון ב[פורום המפתחים של Google AI](https://discuss.ai.google.dev?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-06-10 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-06-10 (שעון UTC)."],[],[]]
