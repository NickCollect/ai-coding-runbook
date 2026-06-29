---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=he
fetched_at: 2026-06-29T05:33:04.804859+00:00
title: "\u05e0\u05ea\u05d5\u05e0\u05d9 \u05d2\u05e8\u05e1\u05d4 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# נתוני גרסה

בדף הזה מפורטים עדכונים ל-Gemini API.

## ‫24 ביוני 2026

- **שימוש במחשב**: השקנו גרסת טרום-השקה ציבורית של התמיכה בכלי [שימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he) ב-Gemini 3.5 Flash. הגרסה הזו כוללת פעולות פשוטות יותר עם כוונות, תמיכה מובנית בסביבות דפדפן, נייד ושולחן עבודה, מדיניות בטיחות שניתנת להגדרה וזיהוי מתקדם של הזרקת הנחיות.

## ‫17 ביוני 2026

- **תמיכה בסטרימינג ליצירת דיבור**: מעכשיו יש תמיכה בסטרימינג דרך `streamGenerateContent` (ו-`stream: true` ב-Interactions API) במודל `gemini-3.1-flash-tts-preview`. מידע נוסף זמין במדריך בנושא [המרת טקסט לדיבור](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he#streaming).

## ‫15 ביוני 2026

- **הודעה על הוצאה משימוש**: המודלים הבאים ליצירת תמונות יוצאים משימוש ו[יושבתו](https://ai.google.dev/gemini-api/docs/deprecations?hl=he) ב-**17 באוגוסט 2026**:

  - ‫**Imagen 4 ומודלי התמונות של Gemini 3**:

    - `imagen-4.0-generate-001`
    - `imagen-4.0-ultra-generate-001`
    - `imagen-4.0-fast-generate-001`

    כדי להעביר את הקוד לנקודות קצה (endpoints) חדשות יותר ויציבות או לנקודות קצה בגרסת טרום-השקה, אפשר לעיין בדף [הוצאה משימוש של Gemini](https://ai.google.dev/gemini-api/docs/deprecations?hl=he#imagen-models).
- **הודעה על הוצאה משימוש**: המודלים הבאים ליצירת סרטונים יוצאים משימוש ו[יושבתו](https://ai.google.dev/gemini-api/docs/deprecations?hl=he) ב-**30 ביוני 2026**:

  - **מודלים של Veo**:

    - `veo-2.0-generate-001`
    - `veo-3.0-generate-001`
    - `veo-3.0-fast-generate-001`

    כדי למנוע שיבושים בשירות, צריך לעדכן את השילוב כך שישתמש במזהי מודלים של גרסת טרום-השקה של Veo 3.1
    (`veo-3.1-generate-preview`,‏ `veo-3.1-fast-generate-preview`) או במודלים של גרסת 3.1 GA שזמינים דרך [פלטפורמת הסוכנים של Gemini Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=he).
- **הודעה על הפסקת תמיכה**: כלי התצוגה מותאמת מיקום הניסיוני של GMP (ממשק קבוע לעיגון בעזרת מפות Google) [יושבת](https://ai.google.dev/gemini-api/docs/deprecations?hl=he) ב-**15 ביוני 2026**:

## ‫1 ביוני 2026

- המודלים הבאים של Gemini 2.0 [הושבתו](https://ai.google.dev/gemini-api/docs/deprecations?hl=he):

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

  במקום זאת, השתמשו ב-[`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=he) או ב-[`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=he).

## ‫28 במאי 2026

- השקנו את `gemini-3.1-flash-image` (Nano Banana 2) ואת `gemini-3-pro-image`
  (Nano Banana Pro), הגרסאות הזמינות לקהל הרחב של המודלים הוויזואליים המקוריים שלנו, [Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=he)
  ו-[Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=he).
- **תמיכה ביצירת תמונות מסרטונים**: עכשיו אפשר להעביר קובץ סרטון (באמצעות העלאה ישירה או ככתובת URL ציבורית ב-YouTube) כהקשר מולטימודאלי לצד הנחיה טקסטואלית כדי ליצור תמונות ממוזערות באיכות גבוהה, פוסטרים קולנועיים או אינפוגרפיקות סיכום. התכונה הזו נתמכת רק בדגם `gemini-3.1-flash-image`. מידע נוסף זמין במדריך בנושא [יצירת תמונות מסרטונים](https://ai.google.dev/gemini-api/docs/image-generation?hl=he#video-to-image).
- הודעה על הוצאה משימוש: המודלים `gemini-3.1-flash-image-preview` ו-`gemini-3-pro-image-preview` הוצאו משימוש ו[יושבתו](https://ai.google.dev/gemini-api/docs/deprecations?hl=he) ב-25 ביוני 2026.

## ‫25 במאי 2026

- מודל `gemini-3.1-flash-lite-preview` [כובה](https://ai.google.dev/gemini-api/docs/deprecations?hl=he). במקום זאת, אתם צריכים להשתמש ב-[`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=he).

## ‫19 במאי 2026

- השקנו את `gemini-3.5-flash`, הגרסה הזמינה לכלל המשתמשים (GA) של [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=he), המודל הכי חכם שלנו לביצועים מתמשכים ברמה גבוהה במשימות שקשורות לסוכנים ולכתיבת קוד. זהו המודל שעומד מאחורי `gemini-flash-latest`.
- השקנו את **ניהול סוכנים ב-Gemini API** ב-Public Preview. כך מפתחים יכולים ליצור ולפרוס סוכנים אוטונומיים עם שמירת מצב שפועלים בסביבות ארגז חול מאובטחות ומבודדות של Linux שמתארחות ב-Google. מידע נוסף זמין בדף [סקירה כללית על סוכנים](https://ai.google.dev/gemini-api/docs/agents?hl=he) וב[מדריך לתחילת העבודה](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=he).
- השקנו את הסוכן המנוהל **Antigravity Agent** לשימוש כללי, גרסת Public Preview, [`antigravity-preview-05-2026`](https://ai.google.dev/gemini-api/docs/models/antigravity-preview-05-2026?hl=he).
  סוכן Antigravity יכול לתכנן, להסיק מסקנות, לכתוב ולהריץ קוד באופן אוטונומי, לנהל קבצים ולגלוש באינטרנט בתוך מאגר ארגז החול שלו. דוגמאות קוד ומפרטים זמינים במדריך בנושא [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=he).

## ‫7 במאי 2026

- השקנו את `gemini-3.1-flash-lite`, הגרסה הזמינה לכלל המשתמשים (GA) של [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=he), שעברה אופטימיזציה למהירות, למדרגיות ולחיסכון בעלויות.
- הודעה על הוצאה משימוש: המודל `gemini-3.1-flash-lite-preview` יוצא משימוש ב-11 במאי 2026 ו[יושבת](https://ai.google.dev/gemini-api/docs/deprecations?hl=he) ב-25 במאי 2026.

## ‫6 במאי 2026

- **שינוי משמעותי שיתרחש בקרוב**: בקשות [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he), סכימת התגובות (`outputs` ← `steps`) והגדרת פורמט הפלט (`response_format`) ישתנו. הסכימה החדשה תהפוך לברירת המחדל ב-**26 במאי**, והסכימה הקודמת תוסר ב-**8 ביוני**.
  פרטים נוספים זמינים ב[מדריך להעברת נתונים](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=he).

## ‫5 במאי 2026

- עדכנו את **חיפוש הקבצים** כדי לתמוך בחיפוש מרובה מצבים. מעכשיו אפשר להטמיע תמונות ולחפש אותן באופן מובנה באמצעות מודל `gemini-embedding-2`.
  המטא-נתונים של ההארקה כוללים עכשיו את התג `media_id` לציטוטים חזותיים ואת התג `page_numbers` שמציין איפה נמצא המידע. מידע נוסף זמין במדריך בנושא [חיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he).

## ‫4 במאי 2026

- השקנו תמיכה ב[Webhooks](https://ai.google.dev/gemini-api/docs/webhooks?hl=he) מבוססי-אירועים ב-Gemini API, כדי להחליף את תהליכי העבודה של סקרים (polling) ב-Batch API ובפעולות ארוכות טווח.

## ‫30 באפריל 2026

- מודל `gemini-robotics-er-1.5-preview` [כובה](https://ai.google.dev/gemini-api/docs/deprecations?hl=he). במקום זאת, אתם צריכים להשתמש ב-[`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=he).

## ‫22 באפריל 2026

- השקנו את `gemini-embedding-2` כזמין לכלל המשתמשים (GA). מידע נוסף זמין בדף [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=he).

## ‫21 באפריל 2026

- השקנו גרסאות חדשות של סוכן [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) עם תכונות של תכנון שיתופי, תמיכה בהדמיה, שילוב של שרת MCP וחיפוש קבצים:

  - ‫[`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=he): מודל שנועד לפעול במהירות וביעילות, ומתאים במיוחד להזרמה חזרה לממשק משתמש של לקוח.
  - ‫[`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=he): רמת המקיפות המקסימלית לאיסוף ולסינתזה אוטומטיים של הקשר.

## ‫15 באפריל 2026

- השקנו את [גרסת הטרום-השקה של Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=he), מודל חסכוני, רהוט וניתן להכוונה להמרת טקסט לדיבור. מידע נוסף זמין במאמרים בנושא [המרת טקסט לדיבור](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he).

## ‫14 באפריל 2026

- השקנו את `gemini-robotics-er-1.6-preview`, המודל המעודכן שלנו לרובוטיקה.
  עכשיו יש לו יכולות חדשות כמו קריאת מכשירים, יכולות משופרות של חשיבה מרחבית ופיזית. מידע נוסף זמין בדף [Gemini Robotics-ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=he) וב[בלוג](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=he).
- הודעה על הוצאה משימוש: מודל `gemini-robotics-er-1.5-preview` [יושבת](https://ai.google.dev/gemini-api/docs/deprecations?hl=he) ב-30 באפריל 2026 בשעה 9:00 לפי שעון החוף המערבי בארה"ב.

## ‫2 באפריל 2026

- השקנו את `gemma-4-26b-a4b-it` ו-`gemma-4-31b-it`, והם זמינים ב-[AI Studio](https://aistudio.google.com?hl=he) וב-Gemini API, כחלק מההשקה של [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=he).

## ‫1 באפריל 2026

- השקנו את רמות ההסקה החדשות [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=he) ו-[Priority](https://ai.google.dev/gemini-api/docs/priority-inference?hl=he), שמציעות יותר אפשרויות לאופטימיזציה של העלות או זמן האחזור.

## ‫31 במרץ 2026

- השקנו את גרסת הטרום-השקה של Veo 3.1 Lite, ‏ [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=he), המודל הכי חסכוני שלנו ל[יצירת סרטונים](https://ai.google.dev/gemini-api/docs/video?hl=he), שנועד לאפשר איטרציה מהירה ופיתוח אפליקציות עם נפח גבוה.
- מודל `gemini-2.5-flash-lite-preview-09-2025` יצא משימוש. במקום זאת, אתם צריכים להשתמש ב-[`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=he).

## ‫26 במרץ 2026

- ‫[`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=he), המודל העדכני ביותר של אודיו לאודיו (A2A) שנועד לדיאלוג בזמן אמת ולאפליקציות AI שמבוססות על קול. כדי להתחיל, אפשר לקרוא את מאמרי העזרה בנושא [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=he).

## ‫25 במרץ 2026

- השקנו את [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=he), מודלים ליצירת מוזיקה: [`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=he) (קליפים באורך 30 שניות) ו-[`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=he) (שירים באורך מלא). שני המודלים מקבלים קלט של טקסט ותמונות, ומפיקים אודיו סטריאו באיכות גבוהה של 48kHz. פרטים נוספים ודוגמאות קוד זמינים במדריך בנושא [יצירת מוזיקה](https://ai.google.dev/gemini-api/docs/music-generation?hl=he).

## ‫23 במרץ 2026

- השקנו [מינויים בתשלום מראש ובתשלום לאחר השימוש (postpay)](https://ai.google.dev/gemini-api/docs/billing?hl=he) ב-AI Studio. יכול להיות שהשינוי ישפיע על חשבונות קיימים. מידע נוסף זמין במאמרי העזרה בנושא [חיוב](https://ai.google.dev/gemini-api/docs/billing?hl=he).

## ‫18 במרץ 2026

- השקנו את התכונה החדשה [שילוב של כלים מובנים ובקשות להפעלת פונקציות](https://ai.google.dev/gemini-api/docs/tool-combination?hl=he), שמאפשרת להשתמש בכלים המובנים של Gemini לצד כלים מותאמים אישית להפעלת פונקציות בקריאה יחידה ל-API.
- [עיגון בעזרת מפות Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he#supported_models) נתמך עכשיו במודלים של Gemini 3.

## ‫16 במרץ 2026

- השקנו [רמות שימוש](https://ai.google.dev/gemini-api/docs/billing?hl=he#about-billing) משופרות ו[מגבלות הוצאות בחשבון לחיוב](https://ai.google.dev/gemini-api/docs/billing?hl=he#tier-spend-caps) כדי לשפר את חוויית המשתמש בנושא חיוב.

## ‫12 במרץ 2026

- הוספנו לחיוב ב-AI Studio [מגבלות הוצאה ברמת הפרויקט](https://ai.google.dev/gemini-api/docs/billing?hl=he#project-spend-caps).

## ‫10 במרץ 2026

- השקנו את `gemini-embedding-2-preview`, מודל ההטמעה המולטי-מודאלי הראשון שלנו.
  הוא תומך בקלט של טקסט, תמונות, סרטונים, אודיו ו-PDF, וממפה את כל הקטגוריות למרחב הטמעה מאוחד. מידע נוסף זמין במאמר בנושא [הטמעות](https://ai.google.dev/gemini-api/docs/embeddings?hl=he).
- הודעה על הוצאה משימוש: מודל `gemini-2.5-flash-lite-preview-09-2025` [יושבת](https://ai.google.dev/gemini-api/docs/deprecations?hl=he) ב-31 במרץ 2026.

## ‫9 במרץ 2026

- מודל התצוגה המקדימה Gemini 3 Pro [הושבת](https://ai.google.dev/gemini-api/docs/deprecations?hl=he). ה-`gemini-3-pro-preview` מפנה עכשיו אל [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=he).

## ‫3 במרץ 2026

- השקנו את גרסת הטרום-השקה של Gemini 3.1 Flash-Lite, המודל הראשון מסוג Flash-Lite בסדרת Gemini 3. ב[דף המודל](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=he) אפשר לקרוא על המפרטים, על עדכונים ספציפיים ועל הנחיות למפתחים.

## ‫26 בפברואר 2026

- השקנו את Nano Banana 2, ‏ [Gemini 3.1 Flash Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image-preview?hl=he), מודל יעיל במיוחד שעבר אופטימיזציה למהירות ולתרחישי שימוש עם נפח גבוה.
- הודעה על הוצאה משימוש: Gemini 3 Pro Preview‏ (`gemini-3-pro-preview`) [יושבת](https://ai.google.dev/gemini-api/docs/deprecations?hl=he) ב-9 במרץ 2026.

## ‫19 בפברואר 2026

- השקנו את [גרסת הטרום-השקה של Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=he), הגרסה הכי עדכנית בסדרת Gemini 3 החדשה.
- השקנו נקודת קצה נפרדת `gemini-3.1-pro-preview-customtools`, שמתאימה יותר לתעדוף כלים בהתאמה אישית, למשתמשים שיוצרים באמצעות שילוב של bash וכלים.

## ‫18 בפברואר 2026

- הודעה על הוצאה משימוש: המודלים הבאים [יושבתו](https://ai.google.dev/gemini-api/docs/deprecations?hl=he) ב-1 ביוני 2026:

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

## ‫17 בפברואר 2026

- הדגמים הבאים [יושבתו](https://ai.google.dev/gemini-api/docs/deprecations?hl=he):

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`

## ‫29 בינואר 2026

- השקנו תמיכה בכלי 'שימוש במחשב' ב-`gemini-3-pro-preview` וב-`gemini-3-flash-preview`.

## ‫21 בינואר 2026

- שינית את הכינויים של `latest`:

  - `gemini-pro-latest` עבר ל-`gemini-3-pro-preview`
  - `gemini-flash-latest` עבר ל-`gemini-3-flash-preview`

## ‫15 בינואר 2026

- הודעה על הוצאה משימוש: המודלים הבאים [יושבתו](https://ai.google.dev/gemini-api/docs/deprecations?hl=he) ב-17 בפברואר 2026:

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- מודל `gemini-2.5-flash-image-preview` יצא משימוש.

## ‫14 בינואר 2026

- מודל `text-embedding-004` [יצא משימוש](https://ai.google.dev/gemini-api/docs/deprecations?hl=he).

## ‫13 בינואר 2026

- הוספנו רזולוציות פלט של 4K ל-[Veo](https://ai.google.dev/gemini-api/docs/video?hl=he) ותמיכה נוספת בסרטונים לאורך בכל הרזולוציות.

## ‫12 בינואר 2026

- השקנו את התכונה 'מחזור חיים של מודל'. בדגמים מסוימים יצוינו עכשיו שלב מחזור החיים וציר הזמן של הוצאה משימוש. מידע נוסף זמין במאמרי העזרה הבאים:

  - [שלבי המודל](https://ai.google.dev/api/generate-content?hl=he#ModelStatus)

## ‫8 בינואר 2026

- השקנו תמיכה בקטגוריות של Cloud Storage ובכל כתובת URL חתומה מראש של מסד נתונים ציבורי ופרטי כמקור קלט נתונים ל-Gemini API. גם גודל הקובץ המקסימלי עלה מ-20MB ל-100MB. פרטים נוספים זמינים במאמר בנושא [שיטות להזנת קבצים](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=he).

## ‫19 בדצמבר 2025

- הוספנו שינוי שעלול לשבור את התאימות לאחור ב-API של Interactions בגרסה v1beta. שם השדה `total_reasoning_tokens` שונה ל-`total_thought_tokens` כדי להתאים יותר למושג 'מחשבות' במודלים של חשיבה.

## ‫17 בדצמבר 2025

- השקנו את גרסת הטרום-השקה של Gemini 3 Flash,‏ `gemini-3-flash-preview`, שמספקת ביצועים מהירים ברמה גבוהה, שמתחרים במודלים גדולים יותר בעלות נמוכה בהרבה. עם יכולות משודרגות של חשיבה ויזואלית ומרחבית, ותכנות אג'נטי. כדאי לקרוא את התיעוד על כמה תכונות חדשות, כולל:

  - [תשובות פונקציה מולטימודאליות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he#multimodal)
  - [הרצת קוד עם תמונות](https://ai.google.dev/gemini-api/docs/code-execution?hl=he#images)

## ‫12 בדצמבר 2025

- השקנו את `gemini-2.5-flash-native-audio-preview-12-2025`, מודל אודיו חדש של Native API לשימוש ב-Live API. העדכון הזה משפר את היכולת של המודל להתמודד עם תהליכי עבודה מורכבים. מידע נוסף זמין [במדריך לשימוש ב-Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=he) ובמאמר [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-live?hl=he).

## ‫11 בדצמבר 2025

- השקנו את Interactions API. ה-API הזה מספק ממשק מאוחד לאינטראקציה עם מודלים וסוכנים של Gemini. מידע נוסף זמין במדריך בנושא [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he).
- השקנו את Gemini Deep Research Agent בגרסת Preview. הוא יכול לתכנן, לבצע ולסכם תוצאות של משימות מחקר בכמה שלבים באופן אוטונומי. פרטים נוספים זמינים במדריך בנושא [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he).

## ‫10 בדצמבר 2025

- השקנו שיפורים ב[מודלים שלנו של טקסט לדיבור](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he), גרסת טרום-השקה של Gemini 2.5 Flash TTS (שעברה אופטימיזציה לזמן אחזור נמוך) וגרסת טרום-השקה של Gemini 2.5 Pro TTS (שעברה אופטימיזציה לאיכות), כולל שיפורים בהבעה, בקצב מדויק ובדיאלוג חלק.

## ‫9 בדצמבר 2025

- המודלים הבאים של Gemini Live API הושבתו:
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## ‫5 בדצמבר 2025

- החיוב על Gemini 3 עבור [עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he) יתחיל ב-5 בינואר 2026.

## ‫4 בדצמבר 2025

- הודעה על הוצאה משימוש: מודל `gemini-2.5-flash-image-preview` יושבת ב-15 בינואר 2026.

## ‫3 בדצמבר 2025

- הודעה על הוצאה משימוש: מודל `text-embedding-004` ייסגר ב-14 בינואר 2026.

## ‫20 בנובמבר 2025

- השקנו את Gemini 3 Pro Image Preview, ‏ `gemini-3-pro-image-preview`, הגרסה הבאה של מודל Nano Banana. מידע נוסף זמין בדף [יצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he).

## ‫18 בנובמבר 2025

- השקנו את המודל הראשון בסדרת Gemini 3, ‏ `gemini-3-pro-preview`, המודל המתקדם ביותר שלנו להסקת מסקנות ולהבנה מולטי-מודאלית עם יכולות סוכנים ותכנות חזקות.

  בנוסף לשיפורים ברמת האינטליגנציה והביצועים, גרסת הטרום-השקה של Gemini 3 Pro מציגה התנהגות חדשה בנושאים הבאים:

  - [רזולוציית המדיה](https://ai.google.dev/gemini-api/docs/media-resolution?hl=he)
  - [חתימות מחשבה](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=he)
  - [רמות ההעמקה](https://ai.google.dev/gemini-api/docs/thinking?hl=he#thinking-levels)

  ב[מדריך למפתחים של Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=he) אפשר לקרוא על העברה, תכונות חדשות ומפרטים.

## ‫11 בנובמבר 2025

- הודעה על הוצאה משימוש: המודלים הבאים יושבתו:

  - ‫12 בנובמבר:

    - `veo-3.0-fast-generate-preview`
    - `veo-3.0-generate-preview`
  - ‫14 בנובמבר:

    - `gemini-2.0-flash-exp-image-generation`
    - `gemini-2.0-flash-preview-image-generation`

## ‫10 בנובמבר 2025

- המודל הבא מושבת:

  - `imagen-3.0-generate-002`

  במקום זאת, צריך להשתמש ב-[Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=he#imagen-4). פרטים נוספים זמינים ב[טבלת ההוצאה משימוש של Gemini](https://ai.google.dev/gemini-api/docs/deprecations?hl=he).

## ‫6 בנובמבר 2025

- השקנו את File Search API בגרסת טרום-השקה ציבורית, כדי לאפשר למפתחים להשתמש בנתונים שלהם כדי להשיג תשובות. מידע נוסף זמין בדף החדש [חיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he).

## ‫4 בנובמבר 2025

- ב-[Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation?hl=he), מספר טוקני הקלט לתמונות ירד מ-1,290 ל-258, וכך עלות עריכת התמונות ירדה.
- הודעה על הוצאה משימוש: המודלים הבאים יושבתו:

  - ‫18 בנובמבר:

    - `gemini-2.5-flash-lite-preview-06-17`
    - `gemini-2.5-flash-preview-05-20`
  - ‫2 בדצמבר:

    - `gemini-2.0-flash-thinking-exp`
    - `gemini-2.0-flash-thinking-exp-01-21`
    - `gemini-2.0-flash-thinking-exp-1219`
    - `gemini-2.5-pro-preview-03-25`
    - `gemini-2.5-pro-preview-05-06`
    - `gemini-2.5-pro-preview-06-05`
  - ‫9 בדצמבר:

    - `gemini-2.0-flash-lite-preview`
    - `gemini-2.0-flash-lite-preview-02-05`
    - `gemini-2.0-flash-exp`
    - `gemini-2.0-pro-exp`
    - `gemini-2.0-pro-exp-02-05`

## ‫29 באוקטובר 2025

- השקנו את הכלי החדש [logging and datasets](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=he) ל-Gemini API.

## ‫20 באוקטובר 2025

- המודלים הבאים של Gemini Live API הושבתו:

  - `gemini-2.5-flash-preview-native-audio-dialog`
  - `gemini-2.5-flash-exp-native-audio-thinking-dialog`

  במקומה, אפשר להשתמש ב-`gemini-2.5-flash-native-audio-preview-09-2025`.
- הודעה על הוצאה משימוש: נסגור את `gemini-2.0-flash-live-001` ואת `gemini-live-2.5-flash-preview` ב-9 בדצמבר 2025.

## ‫17 באוקטובר 2025

- **עיגון בעזרת מפות Google** זמין עכשיו לכולם. מידע נוסף זמין במאמרי עזרה בנושא [עיגון בעזרת מפות Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he).

## ‫15 באוקטובר 2025

- השקנו את המודלים [Veo 3.1 ו-3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=he#veo-3.1) בגרסת טרום-השקה לציבור, עם תכונות חדשות, כולל:

  - הארכת סרטונים שנוצרו ב-Veo.
  - התייחסות לעד שלוש תמונות כדי ליצור סרטון.
  - הוספת תמונות של המסגרת הראשונה והאחרונה כדי ליצור סרטונים.

  בנוסף, השקנו אפשרויות נוספות לאורך סרטוני הפלט ב-Veo 3: ‏ 4, 6 ו-8 שניות.
- הודעה על הוצאה משימוש: נסגור את `veo-3.0-generate-preview` ואת `veo-3.0-fast-generate-preview` ב-12 בנובמבר 2025.

## ‫7 באוקטובר 2025

- השקנו את [Gemini 2.5 Computer Use Preview](https://ai.google.dev/gemini-api/docs/computer-use?hl=he)

## ‫2 באוקטובר 2025

- השקנו את Gemini 2.5 Flash Image בגרסה זמינה לכולם: [יצירת תמונות באמצעות Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=he)

## ‫29 בספטמבר 2025

- המודלים הבאים של Gemini 1.5 מושבתים עכשיו:
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## ‫25 בספטמבר 2025

- השקנו את מודל Gemini Robotics-ER 1.5 בגרסת טרום-השקה (Preview). ב[סקירה הכללית על רובוטיקה](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=he) מוסבר איך להשתמש במודל באפליקציית הרובוטיקה שלכם.
- השקנו את המודלים הבאים בגרסת טרום-השקה (Preview):

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  פרטים נוספים זמינים בדף [מודלים](https://ai.google.dev/gemini-api/docs/models?hl=he).

## ‫23 בספטמבר 2025

- השקנו ב-`gemini-2.5-flash-native-audio-preview-09-2025` מודל אודיו מקורי חדש ל-Live API עם שיפורים בבקשות להפעלת פונקציות ובטיפול בהפסקות דיבור. מידע נוסף זמין [במדריך לשימוש ב-Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=he) ובמאמר [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-2.5-flash-native-audio).

## ‫16 בספטמבר 2025

- הודעה על הוצאה משימוש: המודלים הבאים יושבתו באוקטובר 2025:

  - `embedding-001`
  - `embedding-gecko-001`
  - ‫`gemini-embedding-exp-03-07` (`gemini-embedding-exp`)

  פרטים על המודל העדכני של הטמעות זמינים בדף [הטמעות](https://ai.google.dev/gemini-api/docs/embeddings?hl=he).

## ‫10 בספטמבר 2025

- השקנו תמיכה ב[מודל Embeddings ב-Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he#batch-embedding), והוספנו את Batch API ל[ספריית התאימות של OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=he#batch) כדי להקל עוד יותר על תחילת השימוש בשאילתות אצווה.

## ‫9 בספטמבר 2025

- השקנו את Veo 3 ו-Veo 3 Fast בגרסה זמינה לכולם, עם תמחור נמוך יותר ואפשרויות חדשות ליחסי גובה-רוחב, לרזולוציה ול-seeding. מידע נוסף זמין ב[מאמרי העזרה של Veo](https://ai.google.dev/gemini-api/docs/video?hl=he#model-features).

## ‫26 באוגוסט 2025

- השקנו את [תצוגה מקדימה של תמונות ב-Gemini 2.5](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-2.5-flash-image-preview), המודל החדש שלנו ליצירת תמונות באופן מקורי.

## ‫18 באוגוסט 2025

- השקנו את [הכלי להוספת הקשר לכתובות URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he), שזמין לכולם. הכלי מאפשר לספק כתובות URL כהקשר נוסף להנחיות. התמיכה בשימוש בהקשר של כתובת URL עם מודל `gemini-2.0-flash` (זמין במהלך גרסת ניסוי) תופסק בעוד שבוע.

## ‫14 באוגוסט 2025

- השקנו את מודלי Imagen 4 Ultra, ‏ Standard ו-Fast כגרסאות שזמינות לכלל המשתמשים (GA). מידע נוסף זמין בדף [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=he).

## ‫7 באוגוסט 2025

- ההגדרה `allow_adult` ביצירת סרטונים מתמונות זמינה עכשיו באזורים מוגבלים. פרטים נוספים זמינים בדף בנושא [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=he#veo-model-parameters).

## ‫31 ביולי 2024

- השקנו את האפשרות ליצור סרטונים מתמונות במודל Veo 3 Preview.
- השקנו את מודל Veo 3 Fast Preview.
- מידע נוסף על Veo 3 זמין בדף [Veo](https://ai.google.dev/gemini-api/docs/video?hl=he).

## ‫22 ביולי 2025

- השקנו את מודל Gemini 2.5‏ `gemini-2.5-flash-lite`, מודל מהיר, זול ועם ביצועים גבוהים. מידע נוסף זמין במאמר בנושא [Gemini 2.5
  Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-2.5-flash-lite).

## July 17, 2025

- השקנו את `veo-3.0-generate-preview`, העדכון האחרון של Veo, שכולל יצירת סרטונים עם אודיו. מידע נוסף על Veo 3 זמין בדף [Veo](https://ai.google.dev/gemini-api/docs/video?hl=he).
- מכסות גבוהות יותר של יצירת בקשות ב-Imagen 4 Standard וב-Imagen 4 Ultra. פרטים נוספים זמינים בדף [מגבלות קצב](https://ai.google.dev/gemini-api/docs/rate-limits?hl=he).

## ‫14 ביולי 2025

- השקנו את `gemini-embedding-001`, הגרסה היציבה של מודל הטמעת הטקסט שלנו. מידע נוסף זמין במאמר בנושא [הטמעות](https://ai.google.dev/gemini-api/docs/embeddings?hl=he). `gemini-embedding-exp-03-07`
  המודל הזה ייצא משימוש ב-14 באוגוסט 2025.

## ‫7 ביולי 2025

- השקנו את Gemini API Batch Mode. לצרף בקשות באצווה ולשלוח אותן לעיבוד באופן אסינכרוני. מידע נוסף זמין במאמר בנושא [מצב אצווה](https://ai.google.dev/gemini-api/docs/batch-mode?hl=he).

## ‫26 ביוני 2025

- מודלי התצוגה המקדימה `gemini-2.5-pro-preview-05-06` ו-`gemini-2.5-pro-preview-03-25` מפנים עכשיו לגרסה היציבה העדכנית `gemini-2.5-pro`.
- החשבון `gemini-2.5-pro-exp-03-25` נסגר.

## ‫24 ביוני 2025

- השקנו את מודלי התצוגה המקדימה של Imagen 4 Ultra ו-Standard. מידע נוסף זמין במאמר בנושא [יצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he).

## ‫17 ביוני 2025

- השקנו את `gemini-2.5-pro`, הגרסה היציבה של המודל הכי מתקדם שלנו, עם יכולת חשיבה אדפטיבית. מידע נוסף זמין במאמרים בנושא [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-2.5-pro) ו[חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he). `gemini-2.5-pro-preview-05-06`
  יופנה אוטומטית אל `gemini-2.5-pro` ב-26 ביוני 2025.
- השקנו את `gemini-2.5-flash`, המודל היציב הראשון שלנו מסוג ‎2.5 Flash. [מידע נוסף על Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-2.5-flash)
  המאפיין `gemini-2.5-flash-preview-04-17` ייצא משימוש ב-15 ביולי 2025.
- השקנו את `gemini-2.5-flash-lite-preview-06-17`, מודל Gemini 2.5 בעלות נמוכה ועם ביצועים גבוהים. מידע נוסף זמין במאמר [Gemini 2.5 Flash-Lite בגרסת Preview](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-2.5-flash-lite).

## ‫5 ביוני 2025

- השקנו את `gemini-2.5-pro-preview-06-05`, גרסה חדשה של המודל הכי מתקדם שלנו, עם יכולת חשיבה אדפטיבית. מידע נוסף זמין במאמרים [גרסת טרום-השקה של Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-2.5-pro-preview-06-05) ו[חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he).
  תתבצע הפניה אוטומטית מ-`gemini-2.5-pro-preview-05-06` אל `gemini-2.5-pro` ב-26 ביוני 2025.

## ‫27 במאי 2025

- המודל האחרון שזמין לכוונון, Gemini 1.5 Flash 001, הושבת.
  אין יותר תמיכה בשינוי של מודלים.
  מידע נוסף זמין במאמר בנושא [כוונון עדין באמצעות Gemini API](https://ai.google.dev/gemini-api/docs/model-tuning?hl=he).

## ‫20 במאי 2025

**עדכוני API:**

- השקנו תמיכה ב[עיבוד מקדים של סרטונים בהתאמה אישית](https://ai.google.dev/gemini-api/docs/video-understanding?hl=he#customize-video-processing) באמצעות מרווחי חיתוך ודגימת קצב פריימים שניתנת להגדרה.
- השקנו את התכונה 'שימוש בכמה כלים', שמאפשרת להגדיר [הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he) ו[עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/grounding?hl=he) באותה בקשה `generateContent`.
- השקנו תמיכה ב[קריאות אסינכרוניות לפונקציות](https://ai.google.dev/gemini-api/docs/live-tools?hl=he#async-function-calling) ב-Live API.
- השקנו [כלי ניסיוני להוספת הקשר לכתובות URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he), שמאפשר לספק כתובות URL כהקשר נוסף להנחיות.

**עדכוני מודלים:**

- השקנו את `gemini-2.5-flash-preview-05-20`, מודל [בגרסת טרום-השקה](https://ai.google.dev/gemini-api/docs/models?hl=he#model-versions) של Gemini שעבר אופטימיזציה לביצועים במחיר משתלם ולחשיבה גמישה. מידע נוסף זמין במאמרים [Gemini 2.5 Flash בגרסת טרום-השקה (Preview)](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-2.5-flash-preview) ו[חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he).
- השקנו את המודלים
  [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-2.5-pro-preview-tts)
  ו-
  [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-2.5-flash-preview-tts), שיכולים [ליצור דיבור](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he) עם דובר אחד או שניים.
- השקנו את מודל `lyria-realtime-exp`, ש[יוצר מוזיקה](https://ai.google.dev/gemini-api/docs/music-generation?hl=he) בזמן אמת.
- השקנו את `gemini-2.5-flash-preview-native-audio-dialog` ו-`gemini-2.5-flash-exp-native-audio-thinking-dialog`, מודלים חדשים של Gemini ל-Live API עם יכולות מקוריות של פלט אודיו. מידע נוסף זמין [במדריך לשימוש ב-Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=he#native-audio-output) ובמאמר [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-2.5-flash-native-audio).
- השקנו גרסת טרום-השקה של [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=he), שזמינה ב-[AI Studio](https://aistudio.google.com?hl=he) ודרך Gemini API.`gemma-3n-e4b-it`

## ‫7 במאי 2025

- השקנו את `gemini-2.0-flash-preview-image-generation`, מודל בתצוגה מקדימה ליצירה ולעריכה של תמונות. מידע נוסף זמין במאמרים בנושא [יצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he) ו[יצירת תמונות בגרסת טרום-השקה (Preview) של Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-2.0-flash-preview-image-generation).

## ‫6 במאי 2025

- השקנו את `gemini-2.5-pro-preview-05-06`, גרסה חדשה של המודל הכי מתקדם שלנו, עם שיפורים בקוד ובקריאה לפונקציות. ‫`gemini-2.5-pro-preview-03-25`
  יצביע באופן אוטומטי על הגרסה החדשה של המודל.

## ‫17 באפריל 2025

- השקנו את `gemini-2.5-flash-preview-04-17`, מודל [בגרסת טרום-השקה](https://ai.google.dev/gemini-api/docs/models?hl=he#model-versions) של Gemini שעבר אופטימיזציה לביצועים במחיר משתלם ולחשיבה גמישה. מידע נוסף זמין במאמרים [Gemini 2.5 Flash בגרסת טרום-השקה (Preview)](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-2.5-flash-preview) ו[חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he).

## ‫16 באפריל 2025

- השקנו את התכונה 'שמירת מטמון של ההקשר' עבור [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-2.0-flash).

## 9 באפריל 2025

**עדכוני מודלים:**

- השקנו את `veo-2.0-generate-001`, מודל ליצירת סרטונים מטקסט ומתמונות שזמין לכלל המשתמשים (GA). המודל הזה יכול ליצור סרטונים מפורטים עם ניואנסים אומנותיים. מידע נוסף זמין ב[מאמרי העזרה של Veo](https://ai.google.dev/gemini-api/docs/video?hl=he).
- השקנו את `gemini-2.0-flash-live-001`, גרסת טרום-השקה פתוחה של מודל [Live API](https://ai.google.dev/gemini-api/docs/live?hl=he) עם חיוב מופעל.

  - **ניהול סשנים ואמינות משופרים**

    - **המשך סשן:** שמירה על סשנים פעילים גם כשחלים שיבושים זמניים ברשת. ה-API תומך עכשיו באחסון של מצב הסשן בצד השרת (למשך עד 24 שעות) ומספק נקודות אחיזה (session\_resumption) כדי להתחבר מחדש ולהמשיך מהמקום שבו הפסקתם.
    - **סשנים ארוכים יותר באמצעות דחיסת הקשר:** אפשר לנהל אינטראקציות ממושכות יותר מעבר למגבלות הזמן הקודמות. הגדרת דחיסה של חלון ההקשר באמצעות מנגנון חלון הזזה לניהול אוטומטי של אורך ההקשר, כדי למנוע סיומים פתאומיים בגלל מגבלות ההקשר.
    - **התראה על ניתוק חלק:** תקבלו הודעה משרת `GoAway` שמציינת מתי חיבור עומד להיסגר, כדי שתוכלו לטפל בניתוק בצורה חלקה לפני שהוא יסתיים.
  - **שליטה רבה יותר בדינמיקה של האינטראקציות**
  - **זיהוי פעילות קולית (VAD) שניתן להגדרה:** אפשר לבחור רמות רגישות או להשבית לחלוטין את ה-VAD האוטומטי ולהשתמש באירועי לקוח חדשים (`activityStart`, `activityEnd`) לשליטה ידנית בהפעלה.
  - **הגדרת טיפול בהפרעות:** קובעת אם קלט של משתמש צריך להפריע לתגובה של המודל.
  - **כיסוי הפעלה שניתן להגדרה:** אתם יכולים לבחור אם ה-API יעבד את כל קלט האודיו והווידאו באופן רציף, או רק יתעד אותו כשהמערכת מזהה שהמשתמש מדבר.
  - **רזולוציית מדיה שניתנת להגדרה:** אפשר לבחור את הרזולוציה של מדיה להזנה כדי לבצע אופטימיזציה לאיכות או לשימוש באסימונים.
  - **פלט ותכונות עשירים יותר**
  - **אפשרויות מורחבות של קול ושפה:** אפשר לבחור מתוך שני קולות חדשים ו-30 שפות חדשות לפלט אודיו. עכשיו אפשר להגדיר את שפת הפלט ב-`speechConfig`.
  - **הזרמת טקסט:** קבלת תשובות טקסט בהדרגה בזמן שהן נוצרות, כדי להציג אותן למשתמשים מהר יותר.
  - **דוחות על השימוש בטוקנים:** תוכלו לקבל תובנות לגבי השימוש באמצעות ספירת טוקנים מפורטת שמופיעה בשדה `usageMetadata` של הודעות השרת, עם פירוט לפי אופן השימוש ושלבי ההנחיה או התשובה.

## ‫4 באפריל 2025

- השקנו את `gemini-2.5-pro-preview-03-25`, גרסת טרום-השקה פתוחה של Gemini 2.5 Pro עם חיוב מופעל. אתם יכולים להמשיך להשתמש ב-`gemini-2.5-pro-exp-03-25` במסגרת התוכנית החינמית.

## ‫25 במרץ 2025

- השקנו את `gemini-2.5-pro-exp-03-25`, מודל Gemini ניסיוני לשימוש הציבורי, עם מצב חשיבה שמופעל תמיד כברירת מחדל.
  [מידע נוסף על Gemini 2.5 Pro (ניסיוני)](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-2.5-pro-preview-03-25)

## ‫12 במרץ 2025

**עדכוני מודלים:**

- השקנו מודל ניסיוני של [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=he#gemini) שיכול ליצור ולערוך תמונות.
- השקה של `gemma-3-27b-it`, זמין ב-[AI Studio](https://aistudio.google.com?hl=he) וב-Gemini API, כחלק מהשקת [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=he).

**עדכוני API:**

- הוספנו תמיכה ב[כתובות URL של YouTube](https://ai.google.dev/gemini-api/docs/vision?hl=he#youtube) כמקור מדיה.
- הוספנו תמיכה בהכללת [סרטון מוטבע](https://ai.google.dev/gemini-api/docs/vision?hl=he#inline-video) בגודל של פחות מ-20MB.

## ‫11 במרץ 2025

**עדכוני SDK:**

- השקנו את [Google Gen AI SDK ל-TypeScript ול-JavaScript](https://googleapis.github.io/js-genai) בגרסת טרום-השקה פתוחה.

## ‫7 במרץ 2025

**עדכוני מודלים:**

- השקנו את `gemini-embedding-exp-03-07`, מודל [ניסיוני](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=he) של הטמעות מבוססות-Gemini בתוכנית Public Preview.

## ‫28 בפברואר 2025

**עדכוני API:**

- תמיכה ב[חיפוש ככלי](https://ai.google.dev/gemini-api/docs/grounding?hl=he) נוספה ל-`gemini-2.0-pro-exp-02-05`, מודל ניסיוני שמבוסס על Gemini 2.0 Pro.

## ‫25 בפברואר 2025

**עדכוני מודלים:**

- השקנו את `gemini-2.0-flash-lite`, גרסה זמינה לכלל המשתמשים (GA) של [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#gemini-2.0-flash-lite), שעברה אופטימיזציה למהירות, להרחבה ולחיסכון בעלויות.

## ‫19 בפברואר 2025

**עדכונים ב-AI Studio:**

- תמיכה ב[אזורים נוספים](https://ai.google.dev/gemini-api/docs/available-regions?hl=he) (קוסובו, גרינלנד ואיי פארו).

**עדכוני API:**

- תמיכה ב[אזורים נוספים](https://ai.google.dev/gemini-api/docs/available-regions?hl=he) (קוסובו, גרינלנד ואיי פארו).

## ‫18 בפברואר 2025

**עדכוני מודלים:**

- ‫Gemini 1.0 Pro לא נתמך יותר. רשימת המודלים הנתמכים מופיעה במאמר בנושא [מודלים של Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he).

## ‫11 בפברואר 2025

**עדכוני API:**

- עדכונים בנושא [התאימות של ספריות OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=he).

## ‫6 בפברואר 2025

**עדכוני מודלים:**

- השקנו את `imagen-3.0-generate-002`, גרסה זמינה לכולם (GA) של [Imagen 3 ב-Gemini API](https://ai.google.dev/gemini-api/docs/imagen?hl=he).

**עדכוני SDK:**

- השקנו את [Google Gen AI SDK for Java](https://github.com/googleapis/java-genai) בגרסת Public Preview.

## ‫5 בפברואר 2025

**עדכוני מודלים:**

- השקנו ב-`gemini-2.0-flash-001` גרסה זמינה לכלל המשתמשים (GA) של [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#gemini-2.0-flash) שתומכת בפלט של טקסט בלבד.
- השקנו `gemini-2.0-pro-exp-02-05`גרסת טרום-השקה [ניסיונית](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=he) של Gemini 2.0 Pro לציבור.
- השקנו את `gemini-2.0-flash-lite-preview-02-05`, מודל ניסיוני בגרסת טרום-השקה (Preview) פתוחה לציבור  שעבר אופטימיזציה ליעילות בעלויות.

**עדכוני API:**

- נוספה תמיכה ב[קלט של קבצים ופלט של גרפים](https://ai.google.dev/gemini-api/docs/code-execution?hl=he#input-output) בהרצת קוד.

**עדכוני SDK:**

- השקנו את [Google Gen AI SDK ל-Python](https://googleapis.github.io/python-genai/) בזמינות לכולם (GA).

## ‫21 בינואר 2025

**עדכוני מודלים:**

- השקנו את `gemini-2.0-flash-thinking-exp-01-21`, הגרסה העדכנית של טרום-ההשקה של המודל שעליו מבוסס [Gemini 2.0 Flash Thinking Model](https://ai.google.dev/gemini-api/docs/thinking?hl=he).

## ‫19 בדצמבר 2024

**עדכוני מודלים:**

- השקנו את מצב Gemini 2.0 Flash Thinking בגרסת Public Preview. מצב חשיבה הוא מודל חישוב בזמן הבדיקה שמאפשר לכם לראות את תהליך החשיבה של המודל בזמן שהוא יוצר תשובה, ומייצר תשובות עם יכולות חשיבה רציונלית חזקות יותר.

  מידע נוסף על מצב חשיבה של Gemini 2.0 Flash זמין ב[דף הסקירה הכללית](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=he).

## ‫11 בדצמבר 2024

**עדכוני מודלים:**

- השקנו את [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#gemini-2.0-flash)
  בתוכנית Public Preview. רשימה חלקית של התכונות של Gemini 2.0 Flash Experimental כוללת:
  - מהיר פי שניים מ-Gemini 1.5 Pro
  - סטרימינג דו-כיווני באמצעות Live API
  - תהליך יצירת תשובות מולטי-מודאליות בצורה של טקסט, תמונות ודיבור
  - שימוש בכלים מובנים עם חשיבה רציונלית רב-שלבית כדי להשתמש בתכונות כמו הרצת קוד, חיפוש, קריאה להפעלת פונקציות ועוד

מידע נוסף על Gemini 2.0 Flash מופיע [בדף הסקירה הכללית](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=he).

## ‫21 בנובמבר 2024

**עדכוני מודלים:**

- השקנו את `gemini-exp-1121`, מודל ניסיוני של Gemini API שהוא אפילו יותר עוצמתי.

**עדכוני מודלים:**

- עדכנו את הכינויים של המודלים `gemini-1.5-flash-latest` ו-`gemini-1.5-flash` כך שישתמשו ב-`gemini-1.5-flash-002`.
  - שינוי לפרמטר `top_k`: המודל `gemini-1.5-flash-002` תומך בערכים `top_k` בין 1 ל-41 (לא כולל).
    ערכים שגדולים מ-40 ישתנו ל-40.

## ‫14 בנובמבר 2024

**עדכוני מודלים:**

- השקנו את `gemini-exp-1114`, מודל ניסיוני מתקדם של Gemini API.

## ‫8 בנובמבר 2024

**עדכוני API:**

- הוספנו [תמיכה ב-Gemini](https://ai.google.dev/gemini-api/docs/openai?hl=he) בספריות OpenAI / API בארכיטקטורת REST.

## ‫31 באוקטובר 2024

**עדכוני API:**

- הוספנו [תמיכה בעיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/grounding?hl=he).

## ‫3 באוקטובר 2024

**עדכוני מודלים:**

- השקנו את `gemini-1.5-flash-8b-001`, גרסה יציבה של מודל ה-API הקטן ביותר של Gemini.

## ‫24 בספטמבר 2024

**עדכוני מודלים:**

- השקנו את `gemini-1.5-pro-002` ו-`gemini-1.5-flash-002`, שתי גרסאות יציבות חדשות של Gemini 1.5 Pro ו-1.5 Flash, שזמינות לכלל המשתמשים.
- עדכנו את קוד המודל `gemini-1.5-pro-latest` כך שישתמש ב-`gemini-1.5-pro-002`
  ואת קוד המודל `gemini-1.5-flash-latest` כך שישתמש ב-`gemini-1.5-flash-002`.
- הגרסה `gemini-1.5-flash-8b-exp-0924` הושקה כדי להחליף את `gemini-1.5-flash-8b-exp-0827`.
- השקנו את [מסנן הבטיחות ליושרה אזרחית](https://ai.google.dev/gemini-api/docs/safety-settings?hl=he#safety-filters) ל-Gemini API ול-AI Studio.
- השקנו תמיכה בשני פרמטרים חדשים ל-Gemini 1.5 Pro ול-Gemini 1.5 Flash ב-Python וב-NodeJS:‏ [`frequencyPenalty`](https://ai.google.dev/api/generate-content?hl=he#FIELDS.frequency_penalty) ו-[`presencePenalty`](https://ai.google.dev/api/generate-content?hl=he#FIELDS.presence_penalty).

## ‫19 בספטמבר 2024

**עדכונים ב-AI Studio:**

- הוספנו כפתורי לייק ודיסלייק לתשובות של המודל, כדי לאפשר למשתמשים לשלוח משוב על איכות התשובה.

**עדכוני API:**

- הוספנו תמיכה בקרדיטים של Google Cloud, שאפשר להשתמש בהם עכשיו לשימוש ב-Gemini API.

## ‫17 בספטמבר 2024

**עדכונים ב-AI Studio:**

- הוספנו לחצן **פתיחה ב-Colab** שמייצא הנחיה – ואת הקוד להרצתה – ל-notebook של Colab. התכונה עדיין לא תומכת בהנחיות עם כלים (מצב JSON, קריאה לפונקציה או הפעלת קוד).

## ‫13 בספטמבר 2024

**עדכונים ב-AI Studio:**

- הוספנו תמיכה במצב השוואה, שמאפשר להשוות בין תשובות של מודלים והנחיות שונות כדי למצוא את האפשרות שהכי מתאימה לתרחיש השימוש שלכם.

## ‫30 באוגוסט 2024

**עדכוני מודלים:**

- מודל Gemini 1.5 Flash תומך ב[אספקת סכימת JSON באמצעות הגדרת המודל](https://ai.google.dev/gemini-api/docs/json-mode?hl=he#supply-schema-in-config).

## ‫27 באוגוסט 2024

**עדכוני מודלים:**

- השקנו את [המודלים הניסיוניים](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=he) הבאים:
  - `gemini-1.5-pro-exp-0827`
  - `gemini-1.5-flash-exp-0827`
  - `gemini-1.5-flash-8b-exp-0827`

## ‫9 באוגוסט 2024

**עדכוני API:**

- הוספנו תמיכה ב[עיבוד קובצי PDF](https://ai.google.dev/gemini-api/docs/document-processing?hl=he).

## ‫5 באוגוסט 2024

**עדכוני מודלים:**

- השקנו תמיכה ב-Fine-tuning עבור Gemini 1.5 Flash.

## ‫1 באוגוסט 2024

**עדכוני מודלים:**

- השקנו את `gemini-1.5-pro-exp-0801`, גרסה ניסיונית חדשה של [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#gemini-1.5-pro).

## ‫12 ביולי 2024

**עדכוני מודלים:**

- הוסרה התמיכה ב-Gemini 1.0 Pro Vision משירותים ומכלים של Google AI.

## ‫27 ביוני 2024

**עדכוני מודלים:**

- זמינות לכלל המשתמשים (GA) של חלון ההקשר של 2 מיליון טוקנים ב-Gemini 1.5 Pro.

**עדכוני API:**

- הוספנו תמיכה ב[הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he).

## ‫18 ביוני 2024

**עדכוני API:**

- הוספנו תמיכה ב[שמירת מטמון של הקשר](https://ai.google.dev/gemini-api/docs/caching?hl=he).

## ‫12 ביוני 2024

**עדכוני מודלים:**

- הוצאנו משימוש את Gemini 1.0 Pro Vision.

## ‫23 במאי 2024

**עדכוני מודלים:**

- ‫[Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#gemini-1.5-pro) (`gemini-1.5-pro-001`) זמין לכלל המשתמשים (GA).
- ‫[Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#gemini-1.5-flash)
  (`gemini-1.5-flash-001`) זמין לכלל המשתמשים (GA).

## ‫14 במאי 2024

**עדכוני API:**

- השקנו חלון הקשר של 2 מיליון טוקנים ל-Gemini 1.5 Pro (רשימת המתנה).
- השקנו [חיוב](https://ai.google.dev/gemini-api/docs/billing?hl=he) בתשלום לפי שימוש עבור Gemini 1.0 Pro, ובקרוב נשיק חיוב עבור Gemini 1.5 Pro ו-Gemini 1.5 Flash.
- הגדלנו את המכסות ליצירת בקשות במינוי בתשלום החדש של Gemini 1.5 Pro.
- הוספנו תמיכה מובנית בסרטונים ל-[File API](https://ai.google.dev/api/rest/v1beta/files?hl=he).
- הוספנו תמיכה בטקסט פשוט ל-[File API](https://ai.google.dev/api/rest/v1beta/files?hl=he).
- הוספנו תמיכה בהפעלת פונקציות מקבילית, שמחזירה יותר מקריאה אחת בכל פעם.

## ‫10 במאי 2024

**עדכוני מודלים:**

- השקנו את [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#gemini-1.5-flash)
  (`gemini-1.5-flash-latest`) בגרסת טרום-השקה (Preview).

## ‫9 באפריל 2024

**עדכוני מודלים:**

- השקנו את [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#gemini-1.5-pro)
  (`gemini-1.5-pro-latest`) בגרסת טרום-השקה (Preview).
- השקנו מודל חדש להטמעת טקסט, `text-embeddings-004`, שתומך בגדלים של [הטמעה גמישה](https://ai.google.dev/gemini-api/docs/embeddings?hl=he#elastic-embedding) מתחת ל-768.

**עדכוני API:**

- השקנו את [File API](https://ai.google.dev/api/rest/v1beta/files?hl=he) לאחסון זמני של קובצי מדיה לשימוש בהנחיות.
- הוספנו תמיכה בהנחיות עם נתוני טקסט, תמונה ואודיו, שנקראות גם הנחיות *מולטי-מודאליות*. מידע נוסף זמין במאמר בנושא [יצירת הנחיות עם מדיה](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=he).
- השקנו גרסת בטא של [הוראות מערכת](https://ai.google.dev/gemini-api/docs/system-instructions?hl=he).
- נוסף [מצב הפעלת פונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he#function_calling_mode), שמגדיר את התנהגות הביצוע של הפעלת פונקציות.
- נוספה תמיכה באפשרות ההגדרה `response_mime_type`, שמאפשרת לבקש תגובות ב[פורמט JSON](https://ai.google.dev/gemini-api/docs/api-overview?hl=he#json).

## ‫19 במרץ 2024

**עדכוני מודלים:**

- הוספנו תמיכה ב[כוונון של Gemini 1.0 Pro](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/) ב-Google AI Studio או באמצעות Gemini API.

## ‫13 בדצמבר 2023

**עדכוני מודלים:**

- ‫gemini-pro: מודל טקסט חדש למגוון רחב של משימות. מאזן בין יכולת ליעילות.
- ‫gemini-pro-vision: מודל מולטי-מודאלי חדש למגוון רחב של משימות.
  איזון בין יכולת ליעילות.
- ‫embedding-001: מודל הטמעות חדש.
- ‫aqa: מודל חדש שעבר כוונון מיוחד ואומן לענות על שאלות באמצעות קטעי טקסט כדי להצדיק את התשובות שנוצרו.

פרטים נוספים זמינים במאמר בנושא [מודלים של Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he).

**עדכונים בגרסת ה-API:**

- גרסה 1: ערוץ ה-API היציב.
- ‫v1beta: ערוץ בטא. בערוץ הזה יש תכונות שאולי נמצאות בפיתוח.

פרטים נוספים זמינים [בנושא גרסאות ה-API](https://ai.google.dev/gemini-api/docs/api-versions?hl=he).

**עדכוני API:**

- ‫`GenerateContent` הוא נקודת קצה מאוחדת אחת לצ'אט ולטקסט.
- סטרימינג זמין באמצעות ה-method‏ `StreamGenerateContent`.
- יכולת מולטי-מודאלית: תמונה היא מודאליות נתמכת חדשה
- תכונות חדשות בגרסת בטא:
  - [בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)
  - [Semantic Retriever](https://ai.google.dev/gemini-api/docs/semantic_retrieval?hl=he)
  - מענה לשאלות עם שיוך (AQA)
- מספר המועמדים המעודכן: מודלים של Gemini מחזירים רק מועמד אחד.
- קטגוריות שונות של הגדרות בטיחות וסיווג בטיחות. פרטים נוספים זמינים במאמר בנושא [הגדרות בטיחות](https://ai.google.dev/gemini-api/docs/safety-settings?hl=he).
- עדיין אין תמיכה בכוונון מודלים של Gemini (העבודה בעיצומה).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-06-25 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-06-25 (שעון UTC)."],[],[]]
