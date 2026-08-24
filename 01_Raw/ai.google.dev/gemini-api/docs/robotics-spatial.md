---
source_url: https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=he
fetched_at: 2026-08-24T02:32:19.638754+00:00
title: "\u05d7\u05e9\u05d9\u05d1\u05d4 \u05de\u05e8\u05d7\u05d1\u05d9\u05ea \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# חשיבה מרחבית

מודלים של Gemini Robotics ER יכולים להצביע על אובייקטים, לעקוב אחריהם בסרטון, לזהות אותם באמצעות תיבות תוחמות וליצור מסלולי תנועה.

קוד מלא שניתן להרצה זמין ב-[Robotics cookbook](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## הצבעה על אובייקטים

בדוגמה הבאה מוצגים אובייקטים ספציפיים בתמונה ומוחזרות הקואורדינטות המנורמלות של `[y, x]`:

### Python

```
from google import genai

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

image_response = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": PROMPT}
    ],
    generation_config={"thinking_level": "high"},
)

print(image_response.output_text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-robotics-er-2-preview",
    "input": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "image/png",
            "data": "'"${IMAGE_BASE64}"'"
          }
        },
        {
          "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
        }
      ]
    },
    "generation_config": {
      "thinking_config": {
        "thinking_level": "high"
      }
    }
  }'
```

הפלט יהיה מערך JSON שמכיל אובייקטים, שלכל אחד מהם יש `point` (קואורדינטות `[y, x]` מנורמלות) ו-`label` שמזהה את האובייקט.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

בתמונה הבאה אפשר לראות דוגמה לאופן שבו הנקודות האלה יכולות להופיע:

![דוגמה שמציגה את הנקודות של אובייקטים בתמונה](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=he)

## מעקב אחרי אובייקטים בסרטון

‫Gemini Robotics ER 2 יכול גם לנתח פריימים של סרטונים כדי לעקוב אחרי אובייקטים לאורך זמן. רשימה של פורמטים נתמכים של סרטונים זמינה במאמר בנושא [קלט של סרטונים](https://ai.google.dev/gemini-api/docs/video-understanding?hl=he#supported-formats).

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="my-video.mp4")

prompt = """
          Point to the red ball in every frame where it appears.
          The answer should follow the json format: [{"point": [y, x],
          "label": <label>}, ...]. The points are in [y, x] format
          normalized to 0-1000. Return one entry per frame that contains
          the object.
        """

image_response = client.interactions.create(
  model="gemini-robotics-er-2-preview",
  input=[
    {
        "type": "video",
        "uri": uploaded_file.uri,
        "mime_type": uploaded_file.mime_type
    },
    {"type": "text", "text": prompt}
  ],
)

print(image_response.output_text)
```

## זיהוי אובייקטים ותיבות תוחמות

בנוסף לנקודות, אפשר להנחות את המודל להחזיר תיבות תוחמות דו-ממדיות, שמספקות פרטים מרחביים נוספים לגבי אובייקטים שזוהו.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

prompt = """
          Detect all objects in this image and return bounding boxes.
          The answer should follow the JSON format:
          [{"label": <label>, "y": <y_min>, "x": <x_min>,
            "y2": <y_max>, "x2": <x_max>}, ...]
          where coordinates are normalized to 0-1000.
        """

image_response = client.interactions.create(
  model="gemini-robotics-er-2-preview",
  input=[
    {
        "type": "image",
        "uri": uploaded_file.uri,
        "mime_type": uploaded_file.mime_type
    },
    {"type": "text", "text": prompt}
  ],
)

print(image_response.output_text)
```

## מסלולים

‫Gemini Robotics ER 2 יכול ליצור רצפים של נקודות שמגדירות מסלול, שימושי להנחיית תנועת הרובוט.

בדוגמה הזו, המשתמש מבקש מסלול להזזת עט אדום למארגן, כולל הערכה של נקודות הציון הביניים. הקוד צומצם כדי להציג
רק את ההנחיה.

### Python

```
prompt = """
          Generate a trajectory for the robotic arm to pick up the red pen
          and place it in the organizer. Return a list of waypoints as JSON:
          [{"step": <int>, "point": [y, x], "action": <description>}, ...]
          where coordinates are normalized to 0-1000.
        """
```

## מפנים מקום למחשב נייד

בדוגמה הזו אפשר לראות איך Gemini Robotics ER מסיק מסקנות לגבי מרחב. ההנחיה
מבקשת מהמודל לזהות איזה אובייקט צריך להזיז כדי ליצור
מקום לפריט אחר.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/image-with-objects.jpg")

prompt = """
          Point to the object that I need to remove to make room for my laptop
          The answer should follow the JSON format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000.
        """

image_response = client.interactions.create(
  model="gemini-robotics-er-2-preview",
  input=[
    {
        "type": "image",
        "uri": uploaded_file.uri,
        "mime_type": uploaded_file.mime_type
    },
    {"type": "text", "text": prompt}
  ],
)

print(image_response.output_text)
```

התגובה מכילה קואורדינטה דו-ממדית של האובייקט שנותן מענה לשאלה של המשתמש. במקרה הזה, האובייקט שצריך להזיז כדי לפנות מקום למחשב נייד.

```
[
  {"point": [672, 301], "label": "The object that I need to remove to make room for my laptop"}
]
```

![דוגמה שמראה איזה אובייקט צריך להעביר כדי שאובייקט אחר](https://ai.google.dev/static/gemini-api/docs/images/robotics/spatial-reasoning.png?hl=he)

## אריזת ארוחת צהריים

המודל יכול גם לספק הוראות למשימות מרובות שלבים ולהצביע על אובייקטים רלוונטיים לכל שלב. בדוגמה הזו אפשר לראות איך המודל מתכנן סדרה של שלבים לאריזת ארוחת צהריים בתיק.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/image-of-lunch.jpg")

prompt = """
          Explain how to pack the lunch box and lunch bag. Point to each
          object that you refer to. Each point should be in the format:
          [{"point": [y, x], "label": }], where the coordinates are
          normalized between 0-1000.
        """

image_response = client.interactions.create(
  model="gemini-robotics-er-2-preview",
  input=[
    {
        "type": "image",
        "uri": uploaded_file.uri,
        "mime_type": uploaded_file.mime_type
    },
    {"type": "text", "text": prompt}
  ],
)

print(image_response.output_text)
```

התשובה לפרומפט הזה היא סדרה של הוראות מפורטות לאריזת תיק לארוחת צהריים על סמך קלט התמונה.

**תמונת קלט**

![תמונה של קופסת אוכל ופריטים שאפשר להכניס לתוכה](https://ai.google.dev/static/gemini-api/docs/images/robotics/packing-lunch.png?hl=he)

**פלט המודל**

```
Based on the image, here is a plan to pack the lunch box and lunch bag:

1.  **Pack the fruit into the lunch box.** Place the [apple](apple), [banana](banana), [red grapes](red grapes), and [green grapes](green grapes) into the [blue lunch box](blue lunch box).
2.  **Add the spoon to the lunch box.** Put the [blue spoon](blue spoon) inside the lunch box as well.
3.  **Close the lunch box.** Secure the lid on the [blue lunch box](blue lunch box).
4.  **Place the lunch box inside the lunch bag.** Put the closed [blue lunch box](blue lunch box) into the [brown lunch bag](brown lunch bag).
5.  **Pack the remaining items into the lunch bag.** Place the [blue snack bar](blue snack bar) and the [brown snack bar](brown snack bar) into the [brown lunch bag](brown lunch bag).

Here is the list of objects and their locations:
*   [{"point": [899, 440], "label": "apple"}]
*   [{"point": [814, 363], "label": "banana"}]
*   [{"point": [727, 470], "label": "red grapes"}]
*   [{"point": [675, 608], "label": "green grapes"}]
*   [{"point": [706, 529], "label": "blue lunch box"}]
*   [{"point": [864, 517], "label": "blue spoon"}]
*   [{"point": [499, 401], "label": "blue snack bar"}]
*   [{"point": [614, 705], "label": "brown snack bar"}]
*   [{"point": [448, 501], "label": "brown lunch bag"}]
```

## המאמרים הבאים

- [יכולות אג'נטיות](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=he) – ביצוע קוד, קריאת מכשירים, הוספת הערות לתמונות.
- [תיאום משימות](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=he) – משימות ארוכות טווח עם ממשקי API מותאמים אישית של רובוטים.
- [רובוטיקה עם סטרימינג](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=he) – סטרימינג דו-כיווני בזמן אמת (Gemini Robotics ER 2 בלבד).
- [הבנת סרטונים](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=he) – איתור רגעים וסיווג התקדמות (Gemini Robotics ER 2 בלבד).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-30 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-30 (שעון UTC)."],[],[]]
