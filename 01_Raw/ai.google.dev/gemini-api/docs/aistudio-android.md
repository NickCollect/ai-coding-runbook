---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-android?hl=he
fetched_at: 2026-05-25T05:19:20.587172+00:00
title: "\u05e4\u05d9\u05ea\u05d5\u05d7 \u05d0\u05e4\u05dc\u05d9\u05e7\u05e6\u05d9\u05d5\u05ea \u05dc-Android \u05d1-Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# פיתוח אפליקציות ל-Android ב-Google AI Studio

‫Google AI Studio מאפשר לכם ליצור אפליקציות מקוריות ל-Android מהנחיה בשפה טבעית. מתארים את האפליקציה שרוצים ליצור, ו[סוכן Antigravity](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=he#antigravity-agent) יוצר פרויקט מלא של Kotlin ו-[Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=he). בדפדפן, אפשר לראות תצוגה מקדימה של האפליקציה באמולטור Android מבוסס-דפדפן, להתקין אותה במכשיר פיזי ולפרסם אותה לבדיקה.

## שנתחיל?

כדי להתחיל לפתח אפליקציה ל-Android:

1. עוברים אל [מצב בנייה](https://aistudio.google.com/apps?hl=he) ב-Google AI Studio באמצעות חלונית הניווט הימנית.
2. בוחרים באפשרות **Android** מתוך בורר הפלטפורמות.
3. כותבים הנחיה שמתארת את האפליקציה שרוצים ליצור (לדוגמה, *"צור טבלה לחלוקת משימות יומית עם אחסון מקומי"* או *"צור מחשבון פשוט"*).
4. הסוכן יוצר את הפרויקט ומפעיל אותו באמולטור Android מבוסס-דפדפן.

לאחר מכן תוכלו לבצע איטרציות באפליקציה באמצעות חלונית הצ'אט, בדיוק כמו בחוויית השימוש באינטרנט. הסוכן מנהל את כל הקבצים בפרויקט Android ומפיץ את השינויים בבסיס הקוד.

## אמולטור Android מבוסס-דפדפן

אמולטור Android פועל כולו בענן ומוזרם לדפדפן שלכם.
אין צורך להתקין את Android SDK,‏ Android Studio או אמולטור מקומי.

האמולטור מספק:

- **סימולציה של מכשיר כמו Pixel**: הקשה, גלילה ואינטראקציה עם האפליקציה בדיוק כמו במכשיר אמיתי.
- **תמיכה בסיבוב**: מעבר בין כיוון לאורך לבין כיוון לרוחב.
- **תצוגה מקדימה בזמן אמת**: כשהסוכן מבצע שינויים בקוד, האפליקציה נוצרת מחדש והאמולטור מתרענן באופן אוטומטי.

### מגבלות של אמולטורים

האמולטור מבוסס-הדפדפן לא תומך בכל תכונות החומרה. התכונות הבאות לא זמינות באמולטור:

- צילום במצלמה
- ‫NFC ו-Bluetooth
- ‫GPS (המיקום מדומה)
- ‫Google Play Services (כניסה באמצעות חשבון Google, מפות ותכונות אחרות של Play Services פועלות במכשיר אמיתי אבל לא באמולטור)

## התקנה במכשיר עם ADB

אפשר להתקין את קובץ ה-APK שנוצר ישירות במכשיר Android פיזי שמחובר למחשב באמצעות USB. הפעולה הזו מתבצעת באמצעות [WebUSB](https://developer.chrome.com/docs/capabilities/usb?hl=he) כדי ליצור תקשורת עם המכשיר דרך הדפדפן. אין צורך בהתקנת ADB מקומית.

### דרישות מוקדמות

- דפדפן Chrome או Edge שתומך ב-WebUSB.
- מכשיר Android שבו מופעלות האפשרויות [למפתחים וניפוי באגים ב-USB](https://developer.android.com/studio/debug/dev-options?hl=he).
- כבל USB שמחבר את המכשיר למחשב.

### התקנת האפליקציה במכשיר

1. בחלונית התצוגה המקדימה, לוחצים על **התקנה במכשיר**.
2. בוחרים את מכשיר Android מבורר מכשירי ה-USB בדפדפן.
3. קובץ ה-APK מועבר ומוגדר במכשיר.
4. האפליקציה תופעל אוטומטית.

## פרסום בחנות Play

אתם יכולים לפרסם את האפליקציה ל-Android במסלול הבדיקות הפנימיות של [Google Play Console](https://play.google.com/console?hl=he), שמאפשר לכם להפיץ את האפליקציה ל-100 בודקים לכל היותר.

### דרישות מוקדמות

- [חשבון פיתוח ב-Google Play](https://play.google.com/console/signup?hl=he) (כרוך בתשלום חד-פעמי של דמי רישום בסך 25$).
- פרופיל מפתח מלא ב-Play Console.

### פרסום האפליקציה

1. פותחים את **ההגדרות > פרסום** ב-Google AI Studio.
2. לוחצים על **פרסום בחנות Play**.
3. מאמתים את החשבון באמצעות חשבון הפיתוח ב-Google Play.
4. ‫AI Studio חותם על ה-APK, יוצר את דף האפליקציה בחנות (או מעלה גרסה חדשה) ומפרסם אותה במסלול הבדיקה הפנימית.
5. מקבלים קישור שאפשר לשתף עם הבודקים.

‫AI Studio מנהל את חתימת ה-APK באופן אוטומטי באמצעות מאגר מפתחות מנוהל. אפשר להתאים אישית את דף האפליקציה (סמל, צילומי מסך, תיאור) בשלב מאוחר יותר ב-Play Console.

## מה נוצר

כשמבצעים build של אפליקציית Android, הסוכן יוצר פרויקט רגיל מבוסס Gradle עם המבנה הבא:

- **תצורת ה-build**: קובצי `build.gradle.kts` (ברמת הפרויקט והאפליקציה) באמצעות Kotlin DSL.
- **שכבת ממשק המשתמש**: רכיבי [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=he) עם עיצוב [Material 3](https://m3.material.io/).
- **ארכיטקטורה**: ארכיטקטורה של פעילות יחידה עם ViewModels וסוגי נתונים.
- **משאבים**: `AndroidManifest.xml`, drawables, strings ומשאבים אחרים של Android.

הסוכן מנהל באופן אוטומטי את התלויות של Gradle, ומוסיף חבילות ממאגרי Maven ו-Google לפי הצורך.

אפשר לראות ולערוך את הקוד שנוצר באמצעות הכרטיסייה **קוד** בחלונית התצוגה המקדימה. כדי להמשיך בפיתוח ב-Android Studio, מורידים את הפרויקט כ**קובץ ZIP**.

## מגבלות

יש מגבלות על פיתוח אפליקציות ל-Android ב-AI Studio:

### מגבלות פלטפורמה

- **בצד הלקוח בלבד**: אפליקציות ל-Android לא כוללות רכיב בצד השרת.
  תכונות שדורשות זמן ריצה של שרת (ניהול סודות, משחק מרובה משתתפים, Firebase, ממשקי API של Google Workspace) לא זמינות.
- **ארכיטקטורה של פעילות יחידה**: נתמכים רק פרויקטים עם פעילות יחידה ומודול יחיד.
- **Jetpack Compose בלבד**: האפליקציות משתמשות ב-Kotlin וב-Jetpack Compose. אין תמיכה בפריסות של Java ו-XML.
- **אין NDK או קוד Native**: אין תמיכה בקוד C ו-C++‎.
- **אין Wear OS או Android TV**: יש תמיכה רק בטלפונים ובטאבלטים.

### מגבלות על ייצוא

- **הורדה כקובץ ZIP בלבד**: אפשר להוריד את הפרויקט כקובץ ZIP. ייצוא ל-GitHub
  עדיין לא זמין בפרויקטים ל-Android.

## המאמרים הבאים

- [פיתוח אפליקציות ב-Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=he)
- [פיתוח אפליקציות פול סטאק](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=he) (אינטרנט)
- אפשר לראות דוגמאות ב[גלריית האפליקציות](https://aistudio.google.com/apps?source=showcase&hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-19 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-19 (שעון UTC)."],[],[]]
