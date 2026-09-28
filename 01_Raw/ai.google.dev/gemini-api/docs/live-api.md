---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=he
fetched_at: 2026-09-28T06:30:25.259903+00:00
title: "\u05e1\u05e7\u05d9\u05e8\u05d4 \u05db\u05dc\u05dc\u05d9\u05ea \u05e2\u05dc Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# סקירה כללית על Gemini Live API

‫Live API מאפשר אינטראקציות קוליות וויזואליות בזמן אמת עם Gemini, עם זמן טעינה נמוך. היא מעבדת זרמים רציפים של אודיו, תמונות וטקסט כדי לספק תשובות מיידיות בדיבור שנשמע טבעי, וכך ליצור חוויה שיחתית טבעית למשתמשים.

![סקירה כללית על Live API](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=he)

[אפשר לנסות את Live API ב-Google AI Studiomic](https://aistudio.google.com/live?hl=he)
[שיבוט של אפליקציות לדוגמה מ-GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[שימוש במיומנויות של סוכן תכנותterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=he)

## תרחישים לדוגמה

אפשר להשתמש ב-Live API כדי ליצור סוכנים קוליים בזמן אמת למגוון תעשיות, כולל:

- **מסחר אלקטרוני וקמעונאות:** עוזרים לקניות שמציעים המלצות מותאמות אישית וסוכני תמיכה שפותרים בעיות של לקוחות.
- **גיימינג:** דמויות אינטראקטיביות שאי אפשר לשחק איתן (NPC), עזרה במשחק, ותרגום בזמן אמת של תוכן במשחק.
- **ממשקי דור הבא:** חוויות מבוססות קול ווידאו ברובוטיקה, במשקפיים חכמים ובכלי רכב.
- **שירותי בריאות:** עוזרים בתחום הבריאות לתמיכה בחולים ולחינוך שלהם.
- **שירותים פיננסיים:** יועצים מבוססי-AI לניהול הון וייעוץ בנושא השקעות.
- **חינוך:** מנטורים מבוססי-AI ועוזרי למידה שמספקים הדרכה ומשוב בהתאמה אישית.
- **תרגום ולוקליזציה:** תרגום בזמן אמת של שיחות בדיבור עם זמן אחזור נמוך, שמאפשר תקשורת חלקה בשפות שונות.
- **תמלול וכתוביות בזמן אמת:** המרת דיבור לטקסט (STT) בזמן אמת ליצירת כתוביות בזמן אמת, תמלול פגישות, הכתבה קולית ורישום שיחות עם לקוחות.

## תכונות עיקריות

ממשק API בזמן אמת מציע קבוצה מקיפה של תכונות לבניית סוכני קוליים חזקים:

- [**תמיכה רב-לשונית**](https://ai.google.dev/gemini-api/docs/live-guide?hl=he#supported-languages):
  אפשר לנהל שיחות ב-70 שפות נתמכות.
- [**התפרצות לשיחה**](https://ai.google.dev/gemini-api/docs/live-guide?hl=he#interruptions):
  המשתמשים יכולים להפריע למודל בכל שלב כדי לנהל אינטראקציות דינמיות.
- [**שימוש בכלים**](https://ai.google.dev/gemini-api/docs/live-tools?hl=he):
  משלב כלים כמו קריאה לפונקציות וחיפוש Google כדי ליצור אינטראקציות דינמיות.
- [**תמלולי אודיו**](https://ai.google.dev/gemini-api/docs/live-guide?hl=he#audio-transcription):
  מספק תמלילי טקסט של קלט של משתמשים והפלט מהמודל.
- [**אודיו פרואקטיבי**](https://ai.google.dev/gemini-api/docs/live-guide?hl=he#proactive-audio):
  מאפשר לכם לשלוט מתי המודל מגיב ובאילו הקשרים.
- [**שיחה מותאמת-רגש**](https://ai.google.dev/gemini-api/docs/live-guide?hl=he#affective-dialog):
  התאמת סגנון ותוכן התגובה בהתאם לביטוי הקלט של המשתמש.
- [**תמלול בזמן אמת**](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=he):
  סטרימינג רציף של דיבור לטקסט בזמן אמת עם זיהוי שפה אוטומטי ומילון מותאם אישית.
- [**תרגום בזמן אמת**](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=he):
  תרגום קולי בזמן אמת ביותר מ-70 שפות.

## מפרטים טכניים

בטבלה הבאה מפורטות המפרטים הטכניים של Live API:

| קטגוריה | פרטים |
| --- | --- |
| אופני קלט | אודיו (אודיו PCM גולמי של 16 ביט, 16kHz, little-endian), תמונות (JPEG <= 1FPS), טקסט |
| אופנויות פלט | אודיו (אודיו PCM גולמי של 16 ביט, 24kHz, little-endian) |
| פרוטוקול | חיבור WebSocket עם שמירת מצב (WSS) |

## בחירת גישת הטמעה

כשמשלבים את Live API, צריך לבחור באחת מגישות ההטמעה הבאות:

- **שרת לשרת**: הקצה העורפי מתחבר ל-Live API באמצעות [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). בדרך כלל, הלקוח שולח נתוני שידור (אודיו, וידאו, טקסט) לשרת, והשרת מעביר אותם ל-Live API.
- **לקוח לשרת**: קוד הקצה הקדמי מתחבר ישירות ל-Live API באמצעות [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) כדי להזרים נתונים, בלי לעבור דרך הקצה העורפי.

## שנתחיל?

בוחרים את המדריך שמתאים לסביבת הפיתוח:

Server-to-server

### [מדריך ל-GenAI SDK](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=he)

מתחברים ל-Gemini Live API באמצעות GenAI SDK כדי ליצור אפליקציה מולטי-מודאלית בזמן אמת עם קצה עורפי של Python.

Client-to-server

### [WebSocket tutorial](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=he)

אפשר להתחבר ל-Gemini Live API באמצעות WebSockets כדי ליצור אפליקציה מולטי-מודאלית בזמן אמת עם חזית קצה (frontend) ב-JavaScript וטוקנים זמניים.

Agent development kit

### [מדריך ל-ADK](https://google.github.io/adk-docs/streaming/)

יצירת סוכן ושימוש בסטרימינג של ערכת פיתוח סוכנים (ADK) כדי להפעיל תקשורת קולית ווידאו.

## שילובים עם שותפים

כדי לייעל את הפיתוח של אפליקציות אודיו ווידאו בזמן אמת, אפשר להשתמש בשילוב של צד שלישי שתומך ב-Gemini Live API באמצעות WebRTC או WebSockets.

[LiveKit

איך משתמשים ב-Gemini Live API עם סוכני LiveKit.](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat by Daily

איך יוצרים צ'אט בוט מבוסס-AI בזמן אמת באמצעות Gemini Live ו-Pipecat.](https://docs.pipecat.ai/guides/features/gemini-live)
[Fishjam by Software Mansion

יצירת אפליקציות לסטרימינג של אודיו ווידאו בשידור חי באמצעות Fishjam.](https://docs.fishjam.io/tutorials/gemini-live-integration)
[סוכני Vision לפי זרם

פיתוח אפליקציות AI של קול ווידאו בזמן אמת באמצעות סוכני Vision.](https://visionagents.ai/integrations/gemini)
[Voximplant

אפשר לחבר שיחות נכנסות ויוצאות ל-Live API באמצעות Voximplant.](https://voximplant.com/products/gemini-client)
[Agora

פיתוח אפליקציות AI בממשק שיחה בזמן אמת באמצעות Agora.](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

מתחילים להשתמש ב-Gemini Live API באמצעות Firebase AI Logic.](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=he)

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-17 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-17 (שעון UTC)."],[],[]]
