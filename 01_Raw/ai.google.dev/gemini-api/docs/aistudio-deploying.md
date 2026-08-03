---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=he
fetched_at: 2026-08-03T04:30:15.275500+00:00
title: "\u05e4\u05e8\u05d9\u05e1\u05d4 \u05de-Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# פריסה מ-Google AI Studio

‫Google AI Studio מאפשר לכם לפרוס את אפליקציות הפול סטאק שלכם ישירות ממצב בנייה. כך אפשר לעבור במהירות מאב טיפוס לסביבת ייצור מנוהלת וניתנת להרחבה.

## אפשרויות פריסה

כדי לפרוס את האפליקציה ממצב Build ב-AI Studio, הדרישות משתנות בהתאם לרמה שבה אתם משתמשים:

- ‫[**Google Cloud Starter Tier**](https://docs.cloud.google.com/docs/starter-tier?hl=he):
  מאפשר לכם לפרסם עד 2 אפליקציות full-stack בלי להגדיר פרויקט ב-Google Cloud או חשבון לחיוב.
- **פריסה רגילה**: נדרש פרויקט ב-Google Cloud שמקושר לחשבון שלכם ב-AI Studio, והחיוב צריך להיות מופעל בפרויקט הזה.

## מידע על התוכנית למתחילים

מסלול Starter של Google Cloud מספק דרך פשוטה לפריסת אפליקציות ב-Google Cloud ישירות מ-Google AI Studio, בלי להגדיר סביבת Google Cloud מלאה או חשבון לחיוב.

כל פריסה של Google AI Studio יוצרת שירות תואם ב-Cloud Run. ההגבלות הבאות חלות על שירותים שנפרסו ב-Google AI Studio עם חבילת Starter:

- אפשר לפרוס עד שני שירותים.
- השירותים שלכם נפרסים ב[אזור יחיד של Cloud Run](https://docs.cloud.google.com/run/docs/locations?hl=he).

## שלבי הפריסה של תוכנית למתחילים

אחרי שמעצבים את האפליקציה במצב Build (בנייה), פורסים אותה באמצעות חבילת Starter:

1. לוחצים על הלחצן **פרסום** בפינה השמאלית העליונה.
2. לוחצים על **שנתחיל?**.
3. לוחצים על **פרסום האפליקציה**.

אחרי שהפריסה מסתיימת, AI Studio מספק כתובת URL של Cloud Run שדרכה אפשר לגשת לאפליקציה הפעילה.

## כתובות URL מותאמות אישית ל-AI Studio

כשמפרסמים אפליקציה מ-Google AI Studio, אפשר להגדיר תת-דומיין מותאם אישית וקל לזכירה בקטע `ai.studio` (לדוגמה, `https://your-app-name.ai.studio`).

‫Google AI Studio דורש ששמות של תת-דומיינים יהיו ייחודיים באופן גלובלי בכל הפרויקטים,
ומקצה אותם לפי סדר קבלת הבקשות. אם פרויקט אחר כבר משתמש בשם, AI Studio יבקש מכם לבחור שם אחר. אם מבטלים את הפרסום של אפליקציה או מוחקים אותה, כתובת ה-URL המותאמת אישית שלה מתפנה ומשתמשים אחרים יכולים להשתמש בה.

### הגדרת כתובת URL מותאמת אישית

כדי להגדיר או לעדכן כתובת URL מותאמת אישית לאפליקציה:

1. פותחים את האפליקציה ב-Google AI Studio במצב **Build**.
2. לוחצים על **פרסום** בפינה השמאלית העליונה.
3. בהגדרת הפריסה, מזינים את תת-הדומיין המועדף בשדה **כתובת URL מותאמת אישית** או מאשרים את כתובת ה-URL המוצעת.
4. לוחצים על **פרסום האפליקציה**.

כדי להעביר כתובת URL מותאמת אישית קיימת לאפליקציה אחרת, קודם צריך לבטל את הפרסום של האפליקציה שהוקצתה לה כתובת ה-URL המותאמת אישית או למחוק אותה, ואז לפרסם את האפליקציה החדשה באמצעות תת הדומיין שנבחר.

### דיווח על בעיות שקשורות לסימנים מסחריים או לזכויות יוצרים

דומיינים משנה מותאמים אישית צריכים לעמוד [בתנאים ובהגבלות של Google](https://policies.google.com/terms?hl=he). אם נתקלתם בכתובת URL בהתאמה אישית שמפרה סימן מסחרי או משתמשת בשם שמוגן בזכויות יוצרים ללא אישור, אתם יכולים לדווח על כך באמצעות [פותר הבעיות המשפטיות של Google](https://support.google.com/legal/troubleshooter/1114905?hl=he).

## פריסה רגילה

כשהאפליקציות מתפתחות, יכול להיות שתצטרכו יכולות שמעבר לרמת Starter, כמו מכסות גבוהות יותר, משאבי מחשוב מוגדלים או מוצרים אחרים של Google Cloud שלא זמינים ברמת Starter. כדי לקבל גישה ליכולות האלה, אתם יכולים להמיר את הפרויקט שלכם ברמת Starter המנוהל באופן מלא לפרויקט רגיל ב-Google Cloud.

כך תוכלו להרחיב את הפעילות בצורה חלקה בלי לאבד את ההתקדמות. פועלים לפי השלבים ל[יצירת חשבון לחיוב ב-Cloud](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=he#create-new-billing-account), מאשרים באופן רשמי את התנאים וההגבלות הרגילים של Google Cloud ו[משדרגים לפרויקט רגיל ב-Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=he#upgradee).
מידע נוסף זמין במאמר בנושא [הגדרה של חשבונות בתשלום](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=he#paid-setup).

מידע נוסף על רמות חיוב זמין במאמר [חיוב](https://ai.google.dev/gemini-api/docs/billing?hl=he).

## מחיקת הבקשה

אם אין לכם יותר צורך באפליקציה, אתם יכולים למחוק אותה ב-Google AI Studio לפי ההוראות הבאות:

1. ב-Google AI Studio, עוברים אל [דף האפליקציות](https://aistudio.google.com/app/apps?hl=he).
2. בתפריט הימני, לוחצים על **אפליקציות**.
3. מעבירים את הסמן מעל האפליקציה שרוצים למחוק.
4. כדי למחוק את האפליקציה, לוחצים על סמל פח האשפה בצד שמאל של השורה.

## המאמרים הבאים

- [מידע נוסף על רמת ההתחלה ב-Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=he)
- מידע נוסף על [חיוב](https://ai.google.dev/gemini-api/docs/billing?hl=he) ב-Gemini API

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-10 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-10 (שעון UTC)."],[],[]]
