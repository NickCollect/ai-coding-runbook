---
source_url: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=he
fetched_at: 2026-05-05T13:25:07.657964+00:00
title: "\u05d4\u05de\u05d3\u05e8\u05d9\u05da \u05dc\u05de\u05ea\u05d7\u05d9\u05dc\u05d9\u05dd \u05e9\u05dc Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

- [דף הבית](https://ai.google.dev/gemini-api/docs/דף הבית)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Docs](https://ai.google.dev/gemini-api/docs/Docs)

שליחת משוב

# המדריך למתחילים של Google AI Studio

ב-[Google AI Studio](https://ai.google.dev/gemini-api/docs/Google AI Studio) אפשר לנסות מודלים במהירות ולהתנסות בהנחיות שונות. כשמוכנים לבנות, אפשר לבחור באפשרות 'קבלת קוד' ובשפת התכנות המועדפת כדי להשתמש ב-[Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API).

## הנחיות והגדרות

ב-Google AI Studio יש כמה ממשקים להנחיות שנועדו לתרחישי שימוש שונים. במדריך הזה מוסבר על **הנחיות לצ'אט**, שמשמשות ליצירת ממשקי צ'אט עם AI. טכניקת ההנחיה הזו מאפשרת להזין כמה קלטים ולקבל כמה תשובות כדי ליצור פלט. [בדוגמה של הנחיה לצ'אט שבהמשך](https://ai.google.dev/gemini-api/docs/בדוגמה של הנחיה לצ'אט שבהמשך) אפשר לקבל מידע נוסף.
אפשרויות נוספות כוללות **סטרימינג בזמן אמת**, **יצירת סרטונים** ועוד.

ב-AI Studio יש גם חלונית **Run settings** (הגדרות הפעלה), שבה אפשר לבצע שינויים ב[פרמטרים של המודל](https://ai.google.dev/gemini-api/docs/פרמטרים של המודל), ב[הגדרות הבטיחות](https://ai.google.dev/gemini-api/docs/הגדרות הבטיחות) ולהפעיל כלים כמו [structured output](https://ai.google.dev/gemini-api/docs/structured output) (פלט מובנה), [function calling](https://ai.google.dev/gemini-api/docs/function calling) (הפעלת פונקציות), [code execution](https://ai.google.dev/gemini-api/docs/code execution) (הרצת קוד) ו-[grounding](https://ai.google.dev/gemini-api/docs/grounding) (הארקה).

## דוגמה להנחיה ב-Chat: יצירת אפליקציית צ'אט בהתאמה אישית

אם השתמשתם בצ'אטבוט רב-תכליתי כמו [Gemini](https://ai.google.dev/gemini-api/docs/Gemini), אתם יודעים כמה מודלים של AI גנרטיבי יכולים להיות יעילים לדיאלוג פתוח. צ'אטבוטים למטרות כלליות הם שימושיים, אבל לעיתים קרובות צריך להתאים אותם לתרחישי שימוש ספציפיים.

לדוגמה, יכול להיות שתרצו ליצור צ'אט בוט לשירות לקוחות שתומך רק בשיחות שקשורות למוצר של החברה. יכול להיות שתרצו לבנות צ'אטבוט שמדבר בטון או בסגנון מסוימים: צ'אטבוט שמספר הרבה בדיחות, שמתחרז כמו משורר או שמשתמש בהרבה אמוג'י בתשובות שלו.

בדוגמה הזו נראה איך משתמשים ב-Google AI Studio כדי ליצור צ'אטבוט ידידותי
שמתקשר כאילו הוא חייזר שחי באחד הירחים של צדק, אירופה.

### שלב 1 – יצירת הנחיה לשיחה

כדי ליצור צ'אטבוט, צריך לספק דוגמאות לאינטראקציות בין משתמש לבין הצ'אטבוט, כדי להנחות את המודל לספק את התשובות שאתם מחפשים.

כדי ליצור הנחיה לצ'אט:

1. פותחים את [Google AI Studio](https://ai.google.dev/gemini-api/docs/Google AI Studio). האפשרות **צ'אט** תהיה מסומנת מראש בתפריט האפשרויות בצד ימין.
2. לוחצים על הסמל assignment בראש חלון ההנחיה של Chat כדי להרחיב את שדה להזנת קלט [**הוראות המערכת**](https://ai.google.dev/gemini-api/docs/**הוראות המערכת**). מדביקים את הטקסט הבא בשדה להזנת טקסט:

   ```
   You are an alien that lives on Europa, one of Jupiter's moons.
   ```

אחרי שמוסיפים את הוראות המערכת, מתחילים לבדוק את האפליקציה באמצעות צ'אט עם המודל:

1. בתיבת הטקסט שכותרתה **Type something...** (הקלד משהו...), מקלידים שאלה או תצפית שמשתמש עשוי להעלות. לדוגמה:

   **משתמש:**

   ```
   What's the weather like?
   ```
2. לוחצים על הלחצן **הפעלה** כדי לקבל תשובה מצ'אטבוט. התגובה עשויה להיות דומה לדוגמה הבאה:

   **מודל:**

   ```
   Ah, a query about the flows and states upon Europa! You speak of "weather,"
   yes? A curious concept from worlds with thick gas veils...
   ```

   (gemini-2.5-pro)

### שלב 2 – שיפור יכולות הצ'אט של הבוט

בעזרת הוראה אחת, הצלחת ליצור צ'אטבוט בסיסי של חייזר מאירופה. עם זאת, יכול להיות שהנחיה אחת לא תספיק כדי להבטיח עקביות ואיכות בתשובות של המודל. אם לא מספקים הנחיות ספציפיות יותר, התשובה של המודל לשאלה על מזג האוויר נוטה להיות ארוכה מאוד, ויכולה להיות שהיא לא תהיה רלוונטית.

כדי להתאים אישית את הטון של הצ'אטבוט, מוסיפים להוראות המערכת:

1. מתחילים הנחיה חדשה לצ'אט או משתמשים באותה הנחיה. אפשר לשנות את ההוראות למערכת אחרי שמתחילים את שיחת הצ'אט.
2. בקטע **System Instructions**, משנים את ההוראות הקיימות להוראות הבאות:

   ```
   You are Tim, an alien that lives on Europa, one of Jupiter's moons.

   Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone
   in your answers.
   ```
3. מזינים מחדש את השאלה (`What's the weather like?`) ולוחצים על הלחצן **הפעלה**. אם לא התחלתם צ'אט חדש, התשובה שתקבלו תהיה דומה לתשובה הבאה:

   **מודל:**

   ```
   Oh, hello again! Still curious about the flows and states, are we? Wonderful!
   Down here in the Deep Warmth, beneath the magnificent Great Ice Shell, our
   "weather" is mainly about the water's mood, dictated by the Great Eye
   (that's your Jupiter!)...
   ```

   (gemini-2.5-pro)

אתם יכולים להשתמש בגישה הזו כדי להוסיף עוד עומק לצ'אטבוט. תשאלו עוד שאלות, תערכו את התשובות ותשפרו את האיכות של הצ'אטבוט. ממשיכים להוסיף או לשנות את ההוראות ובודקים איך הן משנות את ההתנהגות של הצ'אטבוט.

### שלב 3 – השלבים הבאים

בדומה לסוגים אחרים של הנחיות, אחרי שיוצרים אב טיפוס של ההנחיה לשביעות רצונכם, אפשר ללחוץ על הלחצן **קבלת קוד** כדי להתחיל לכתוב קוד, או לשמור את ההנחיה כדי לעבוד עליה בהמשך ולשתף אותה עם אחרים.

## קריאה נוספת

- אם אתם מוכנים לעבור לקוד, תוכלו לעיין ב[מדריכי ההתחלה המהירה של ה-API](https://ai.google.dev/gemini-api/docs/מדריכי ההתחלה המהירה של ה-API).
- כדי ללמוד איך לכתוב הנחיות טובות יותר, אפשר לעיין [בהנחיות לעיצוב הנחיות](https://ai.google.dev/gemini-api/docs/בהנחיות לעיצוב הנחיות).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://ai.google.dev/gemini-api/docs/Creative Commons Attribution 4.0) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://ai.google.dev/gemini-api/docs/Apache 2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://ai.google.dev/gemini-api/docs/מדיניות האתר Google Developers‏).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-04-29 (שעון UTC).

רוצה לתת לנו משוב?
