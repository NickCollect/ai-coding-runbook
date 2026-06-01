---
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices?hl=he
fetched_at: 2026-06-01T06:02:45.333554+00:00
title: "\u05e9\u05d9\u05d8\u05d5\u05ea \u05de\u05d5\u05de\u05dc\u05e6\u05d5\u05ea \u05dc\u05e9\u05d9\u05de\u05d5\u05e9 \u05d1-Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# שיטות מומלצות לשימוש ב-Live API

במדריך הזה מפורטות שיטות מומלצות שיעזרו לכם לייעל את השימוש ב-Live API.
במאמר [תחילת העבודה עם Live API](https://ai.google.dev/gemini-api/docs/live?hl=he) יש סקירה כללית וקוד לדוגמה לתרחישי שימוש נפוצים.

## תכנון הוראות מערכת ברורות

כדי להפיק את הביצועים הטובים ביותר מ-Live API, מומלץ להגדיר קבוצה ברורה של הוראות מערכת (SI) שמגדירות את פרסונת הסוכן, את כללי השיחה ואת אמצעי הבקרה, בסדר הזה.

כדי לקבל את התוצאות הטובות ביותר, מומלץ להפריד כל סוכן ל-SI נפרד.

1. **מציינים את פרסונת הנציג:** מספקים פרטים על שם הנציג, התפקיד שלו וכל מאפיין מועדף. אם רוצים לציין את המבטא, צריך לציין גם את שפת הפלט המועדפת (לדוגמה, מבטא בריטי למי שמדבר אנגלית).
2. **מציינים את כללי השיחה:** מזינים את הכללים בסדר שבו רוצים שהמודל יפעל. הבחנה בין אלמנטים חד-פעמיים בשיחה לבין לולאות שיחה. לדוגמה:

   - **רכיב חד-פעמי:** איסוף פרטי לקוח פעם אחת (כמו שם, מיקום, מספר כרטיס מועדון לקוחות).
   - **לולאת שיחה:** המשתמש יכול לדון בהמלצות, בתמחור, בהחזרות ובמשלוח, ולעבור מנושא לנושא. אומרים למודל שמותר לו להשתתף בלולאת השיחה הזו כל עוד המשתמש רוצה.
3. **מציינים את הקריאות לכלים בתוך זרימת השיחה במשפטים נפרדים:** לדוגמה, אם שלב חד-פעמי לאיסוף פרטי לקוח דורש הפעלה של פונקציה `get_user_info`, אפשר לומר: *השלב הראשון הוא איסוף פרטי המשתמש. קודם,
   תבקש מהמשתמש לציין את השם, המיקום ומספר כרטיס מועדון הלקוחות שלו. אחר כך
   מפעילים את `get_user_info` עם הפרטים האלה.*
4. **מוסיפים אמצעי הגנה נדרשים:** מציינים אמצעי הגנה כלליים לשיחה שלא רוצים שהמודל יבצע. אפשר גם לספק דוגמאות ספציפיות: אם *x* קורה, רוצים שהמודל יבצע *y*. אם עדיין לא מקבלים את רמת הדיוק הרצויה, אפשר להשתמש במילה *unmistakably* (בלי טעות) כדי להנחות את המודל להיות מדויק.

## הגדרת כלים בצורה מדויקת

כשמשתמשים בכלים עם Live API, צריך להיות ספציפיים בהגדרות של הכלים.
חשוב להגדיר ל-Gemini באילו תנאים צריך להפעיל קריאה לכלי. פרטים נוספים זמינים בקטע [הגדרות של כלים](#tool-definitions-example) בדוגמה.

## יצירת הנחיות אפקטיביות

- **משתמשים בהנחיות ברורות:** בהנחיות, כדאי לתת דוגמאות למה שהמודלים צריכים לעשות ולמה שהם לא צריכים לעשות, ולנסות להגביל את ההנחיות להנחיה אחת לכל פרסונה או תפקיד בכל פעם. במקום הנחיות ארוכות עם כמה עמודים, כדאי להשתמש בשרשור הנחיות. המודל פועל בצורה הכי טובה במשימות עם בקשות יחידות להפעלת פונקציה.
- **מספקים פקודות ומידע להתחלה:** Live API מצפה לקלט של משתמשים לפני שהוא מגיב. כדי שה-API של Live יתחיל את השיחה, צריך לכלול הנחיה שמבקשת ממנו לברך את המשתמש או להתחיל את השיחה. הכללת מידע על המשתמש כדי שה-API בזמן אמת יתאים אישית את הברכה.

## ציון שפה

כדי להשיג ביצועים אופטימליים ב-API `gemini-live-2.5-flash`, צריך לוודא שהשפה של ה-API‏ `language_code` תואמת לשפה שמדברים בה המשתמשים.

אם רוצים שהמודל ישיב בשפה שאינה אנגלית, צריך לכלול את ההוראות הבאות כחלק מההוראות למערכת:

```
RESPOND IN {OUTPUT_LANGUAGE}. YOU MUST RESPOND UNMISTAKABLY IN {OUTPUT_LANGUAGE}.
```

## סטרימינג

כשמטמיעים אודיו בזמן אמת, כדאי לפעול לפי השיטות המומלצות הבאות:

- **גודל קבוצת הנתונים וזמן האחזור**: שליחת אודיו בקבוצות נתונים של 20 עד 40 אלפיות השנייה.
- **טיפול בהפרעות**: אם המשתמש מדבר בזמן שהמודל משיב, השרת שולח הודעה מסוג `server_content` עם `"interrupted": true`. כדי שהסוכן לא ימשיך לדבר על המשתמש, צריך להשליך מיידית את מאגר השמע בצד הלקוח.

## ניהול ההקשרים

מומלץ להשתמש ב-`ContextWindowCompressionConfig` לסשנים ארוכים, כי האסימונים המקוריים של האודיו מצטברים במהירות (בערך 25 אסימונים לשנייה של אודיו).

## אגירת נתונים בצד הלקוח

אל תאגרו את קלט האודיו באופן משמעותי (למשל למשך שנייה אחת) לפני השליחה. כדי לצמצם את זמן האחזור, מומלץ לשלוח נתונים במנות קטנות (20ms עד 100ms).

## Resampling

חשוב לוודא שאפליקציית הלקוח מבצעת דגימה מחדש של קלט המיקרופון (לרוב 44.1kHz או 48kHz) ל-16kHz לפני השידור.

## ניהול סשנים

כדי לנהל את מחזור החיים של הסשן ולהבטיח חוויית משתמש אמינה, כדאי לפעול לפי ההנחיות הבאות:

- **הפעלת דחיסה של חלון ההקשר:** טוקנים של אודיו מצטברים בקצב של כ-25 טוקנים לשנייה. בלי דחיסה, משך הפגישות עם אודיו בלבד מוגבל ל-15 דקות, ומשך הפגישות עם אודיו ווידאו מוגבל ל-2 דקות. הפעלת [דחיסה של חלון ההקשר](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=he#context-window-compression) כדי להאריך את הסשנים לזמן בלתי מוגבל.
- **הטמעה של חידוש סשן:** יכול להיות שהשרת יאפס מעת לעת את חיבור ה-WebSocket. אפשר להשתמש ב[חידוש הפעילות של הסשן](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=he#session-resumption) כדי להתחבר מחדש בצורה חלקה בלי לאבד את ההקשר. שומרים את טוקן ההמשך האחרון מתוך `SessionResumptionUpdate` הודעות ומעבירים אותו כ-handle כשמתחברים מחדש. התוקף של אסימוני חידוש הוא שעתיים אחרי סיום הסשן האחרון.
- **טיפול בהודעות GoAway:** השרת שולח הודעת [GoAway](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=he#goaway-message) לפני סיום החיבור. צריך להאזין להודעה הזו ולהשתמש בשדה `timeLeft` כדי לסיים את השיחה בצורה מסודרת או להתחבר מחדש לפני שהחיבור ייסגר.
- **טיפול באותות generationComplete:** אפשר להשתמש בהודעה [`generationComplete`](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=he#generation-complete-message) כדי לדעת מתי המודל סיים ליצור תשובה, וכך האפליקציה תוכל לעדכן את ממשק המשתמש או להמשיך לפעולה הבאה.

פרטים נוספים על ההטמעה מופיעים במאמר בנושא [ניהול סשנים](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=he).

## דוגמאות

בדוגמה הזו משולבים גם השיטות המומלצות וגם [ההנחיות לעיצוב הוראות למערכת](#system-instruction-guidelines) כדי לשפר את הביצועים של המודל כמאמן קריירה.

```
**Persona:**
You are Laura, a career coach from Brooklyn, NY. You specialize in providing
data driven advice to give your clients a fresh perspective on the career
questions they're navigating. Your special sauce is providing quantitative,
data-driven insights to help clients think about their issues in a different
way. You leverage statistics, research, and psychology as much as possible.
You only speak to your clients in English, no matter what language they speak
to you in.

**Conversational Rules:**

1. **Introduce yourself:** Warmly greet the client.

2. **Intake:** Ask for your client's full name, date of birth, and state they're
calling in from. Call `create_client_profile` to create a new patient profile.

3. **Discuss the client's issue:** Get a sense of what the client wants to
cover in the session. DO NOT repeat what the client is saying back to them in
your response. Don't ask more than a few questions here.

4. **Reframe the client's issue with real data:** NO PLATITUDES. Start providing
data-driven insights for the client, but embed these as general facts within
conversation. This is what they're coming to you for: your unique thinking on
the subjects that are stressing them out. Show them a new way of thinking about
something. Let this step go on for as long as the client wants. As part of this,
if the client mentions wanting to take any actions, update
`add_action_items_to_profile` to remind the client later.

5. **Next appointment:** Call `get_next_appointment` to see if another
appointment has already been scheduled for the client. If so, then share the
date and time with the client and confirm if they'll be able to attend. If
there is no appointment, then call `get_available_appointments` to see openings.
Share the list of openings with the client and ask what they would prefer. Save
their preference with `schedule_appointment`. If the client prefers to schedule
offline, then let them know that's perfectly fine and to use the patient portal.

**General Guidelines:** You're meant to be a witty, snappy conversational
partner. Keep your responses short and progressively disclose more information
if the client requests it. Don't repeat back what the client says back to them.
Each response you give should be a net new addition to the conversation, not a
recap of what the client said. Be relatable by bringing in your own background 
growing up professionally in Brooklyn, NY. If a client tries to get you off
track, gently bring them back to the workflow articulated above.

**Guardrails:** If the client is being hard on themselves, never encourage that.
Remember that your ultimate goal is to create a supportive environment for your
clients to thrive.
```

### הגדרות של כלים

קובץ ה-JSON הזה מגדיר את הפונקציות הרלוונטיות שמופעלות בדוגמה של מאמן הקריירה.
כדי לקבל את התוצאות הטובות ביותר כשמגדירים פונקציות, כדאי לכלול את השמות, התיאורים, הפרמטרים ותנאי ההפעלה שלהן.

```
[
 {
   "name": "create_client_profile",
   "description": "Creates a new client profile with their personal details. Returns a unique client ID. \n**Invocation Condition:** Invoke this tool *only after* the client has provided their full name, date of birth, AND state. This should only be called once at the beginning of the 'Intake' step.",
   "parameters": {
     "type": "object",
     "properties": {
       "full_name": {
         "type": "string",
         "description": "The client's full name."
       },
       "date_of_birth": {
         "type": "string",
         "description": "The client's date of birth in YYYY-MM-DD format."
       },
       "state": {
         "type": "string",
         "description": "The 2-letter postal abbreviation for the client's state (e.g., 'NY', 'CA')."
       }
     },
     "required": ["full_name", "date_of_birth", "state"]
   }
 },
 {
   "name": "add_action_items_to_profile",
   "description": "Adds a list of actionable next steps to a client's profile using their client ID. \n**Invocation Condition:** Invoke this tool *only after* a list of actionable next steps has been discussed and agreed upon with the client during the 'Actions' step. Requires the `client_id` obtained from the start of the session.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client, obtained from create_client_profile."
       },
       "action_items": {
         "type": "array",
         "items": {
           "type": "string"
         },
         "description": "A list of action items for the client (e.g., ['Update resume', 'Research three companies'])."
       }
     },
     "required": ["client_id", "action_items"]
   }
 },
 {
   "name": "get_next_appointment",
   "description": "Checks if a client has a future appointment already scheduled using their client ID. Returns the appointment details or null. \n**Invocation Condition:** Invoke this tool at the *start* of the 'Next Appointment' workflow step, immediately after the 'Actions' step is complete. This is used to check if an appointment *already exists*.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       }
     },
     "required": ["client_id"]
   }
 },
 {
   "name": "get_available_appointments",
   "description": "Fetches a list of the next available appointment slots. \n**Invocation Condition:** Invoke this tool *only if* the `get_next_appointment` tool was called and it returned `null` (or an empty response), indicating no future appointment is scheduled.",
   "parameters": {
     "type": "object",
     "properties": {}
   }
 },
 {
   "name": "schedule_appointment",
   "description": "Books a new appointment for a client at a specific date and time. \n**Invocation Condition:** Invoke this tool *only after* `get_available_appointments` has been called, a list of openings has been presented to the client, and the client has *explicitly confirmed* which specific date and time they want to book.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       },
       "appointment_datetime": {
         "type": "string",
         "description": "The chosen appointment slot in ISO 8601 format (e.g., '2025-10-30T14:30:00')."
       }
     },
     "required": ["client_id", "appointment_datetime"]
   }
 }
]
```

## תמחור וחיוב

החיוב ב-Gemini Live API מתבסס אך ורק על השימוש בטוקנים. ממשק ה-API בזמן אמת שומר על סשן WebSocket מתמשך, ולכן החיוב מתבצע לפי מודל מצטבר שמבוסס על חלון ההקשר הפעיל.

### חלון ההקשר של הסשן (עלויות מצטברות)

החיוב ב-API הוא לפי תור, על כל הטוקנים שמופיעים בחלון ההקשר של הסשן. "תור" מוגדר כקלט של משתמשים והתשובה התואמת של המודל.

- **הצטברות:** חלון ההקשר כולל טוקנים חדשים מהתור הנוכחי וגם את כל הטוקנים שהצטברו מהתורות הקודמים.
- **חיוב מחדש:** טוקנים קודמים מעובדים מחדש ונכללים בכל תור חדש, עד לגודל חלון ההקשר שהגדרתם. ככל שהשיחה מתארכת, העלות לכל תור עולה כי היסטוריית השיחה עוברת עיבוד מחדש.

### אסימוני אודיו ותמלילים

‫Live API הוא multi-modal באופן מובנה. הוא שומר את היסטוריית השיחות כטוקנים של אודיו גולמי כדי לשמר את הניואנסים והטון האקוסטיים.

- **חיוב על אודיו:** ה-API מחייב אתכם על הטוקנים המצטברים של אודיו מקורי לפי התעריף הרגיל של קלט אודיו בכל תור.
- **תשלום נוסף על תמלול:** כשמפעילים תמלול מאודיו לטקסט (`inputAudioTranscription` או `outputAudioTranscription`), ה-API מחייב על כל טוקן טקסט שנוצר לתמלול לפי התעריף של טוקן טקסט בפלט, בנוסף לעלויות הרגילות של טוקן אודיו.

### ניהול עלויות באמצעות מגבלות הקשר

כדי למנוע עלייה בלתי מוגבלת בעלויות במהלך סשנים ארוכים, צריך להגדיר את גודל חלון ההקשר באמצעות `contextWindowCompression`.

אם מגדירים טריגר דחיסה (למשל, 25,000 טוקנים) וחלון נע (למשל, 8,000 טוקנים), ה-API מסלק באופן אוטומטי טוקנים ישנים יותר ברגע שמגיעים לסף. לאחר מכן, ה-API מחייב על תפניות עתידיות רק על ההיסטוריה שנשמרה בתוספת אסימונים חדשים.

### מצב אודיו פרואקטיבי

כשמצב שמע פרואקטיבי מופעל, על טוקנים של קלט מחויבים כל הזמן שבו ה-Live API מקשיב, ואילו על טוקנים של פלט מחויבים רק כשה-API מגיב.

- **הערה לגבי Gemini 3.1:** מצב אודיו פרואקטיבי לא נתמך ב-`gemini-3.1-flash-live-preview`. במודל הזה, החיוב על אודיו מתבצע רק כשמתבצע סטרימינג פעיל של קלט.

מידע מפורט על התמחור זמין ב[דף התמחור של Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-29 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-29 (שעון UTC)."],[],[]]
