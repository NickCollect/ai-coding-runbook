---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=he
fetched_at: 2026-08-10T03:12:28.858595+00:00
title: "\u05d4\u05d1\u05e0\u05ea \u05e1\u05e8\u05d8\u05d5\u05e0\u05d9\u05dd \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# הבנת סרטונים

‫Gemini Robotics ER 2 יכול לעקוב אחרי התקדמות המשימה מפידים רציפים של סרטונים באמצעות שתי יכולות:

- זיהוי רגעים: זיהוי חותמת הזמן המדויקת שבה מתרחש אירוע מרכזי.
- סיווג ההתקדמות: כל סרטון משויך לאחת מ-5 קבוצות של שיעורי צפייה (0-20%, ‏ 20-40%, ‏ 40-60%, ‏ 60-80%, ‏ 80-100%).

## חיפוש רגעים

התכונה 'איתור רגעים' מזהה את הפריים המדויק בסרטון שבו מתרחש אירוע חשוב – לדוגמה, מתי מתמלאת או מתי קושרים קשר. הרובוטים משתמשים בזה כדי לוודא שהפעולה הצליחה, כדי להגדיר את רצף השלבים וכדי להפעיל תיקונים.

ההנחיה הבאה מבקשת מהמודל לזהות את רגע ההשלמה של משימה מסוימת בסרטון:

```
from google import genai
from google.genai import types

client = genai.Client()

with open("task_video.mp4", "rb") as f:
    video_bytes = f.read()

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(data=video_bytes, mime_type="video/mp4"),
        prompt,
    ],
)

print(response.text)
```

בדוגמה הבאה מוצגים פריימים מסרטון שבו המודל מזהה רגעים, והמודל מזהה את חותמת הזמן של השלמת המשימה:

![פריים לדוגמה מסרטון שמציג את הפלט של חיפוש הרגע עם שכבת-על של חותמת זמן](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=he)

## סיווג התקדמות

סיווג ההתקדמות מקצה סרטון לאחת מחמש קבוצות של שיעורי השלמה:
0-20%,‏ 20-40%,‏ 40-60%,‏ 60-80% או 80-100%. כך הרובוטים מקבלים מידע על המצב בזמן אמת, ויכולים לשנות את הפעולות או לנסות שוב שלבים שנכשלו בלי להפעיל מחדש את כל תהליך העבודה.

הפרומפט הבא מבקש מהמודל לסווג את רמת ההתקדמות הנוכחית בסרטון:

```
from google import genai
from google.genai import types

client = genai.Client()

with open("task_video.mp4", "rb") as f:
    video_bytes = f.read()

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(data=video_bytes, mime_type="video/mp4"),
        prompt,
    ],
)

print(response.text)
```

בדוגמה הבאה מוצגים פריימים מסרטון של סיווג התקדמות, עם סוגריים של התקדמות שהוקצו על ידי המודל:

![דוגמה למסגרות של סרטון שבהן מוצג פלט סיווג ההתקדמות עם תווית של סוגר התקדמות](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=he)

## דוגמאות

דוגמאות מלאות להרצה, כולל מעקב אחרי משימות מרובות שלבים, זמינות ב[אוסף הפתרונות בנושא רובוטיקה](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## המאמרים הבאים

- ‫[Live API for robotics](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=he) – סטרימינג דו-כיווני בזמן אמת.
- [תיאום משימות](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=he) – משימות ארוכות טווח עם נימוקים מרחביים.
- [סקירה כללית של Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=he) – השוואה בין מודלים ויכולות.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-30 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-30 (שעון UTC)."],[],[]]
