---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=he
fetched_at: 2026-07-27T04:34:02.259592+00:00
title: "\u05d4\u05e1\u05d1\u05e8 \u05e2\u05dc \u05d0\u05e1\u05d9\u05de\u05d5\u05e0\u05d9\u05dd \u05d5\u05e1\u05e4\u05d9\u05e8\u05d4 \u05e9\u05dc\u05d4\u05dd \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# הסבר על אסימונים וספירה שלהם

‫Gemini ומודלים אחרים של AI גנרטיבי מעבדים קלט ופלט ברמת פירוט שנקראת *טוקן*.

**במודלים של Gemini, טוקן שווה בערך ל-4 תווים.
‫100 טוקנים שווים לכ-60-80 מילים באנגלית.**

## מידע על טוקנים

אסימונים יכולים להיות תווים בודדים כמו `z` או מילים שלמות כמו `cat`. מילים ארוכות
מפוצלות לכמה טוקנים. קבוצת כל האסימונים שבהם נעשה שימוש במודל נקראת אוצר מילים, והתהליך של פיצול טקסט לאסימונים נקרא *טוקניזציה*.

כשמופעל חיוב, [העלות של קריאה ל-Gemini API](https://ai.google.dev/pricing?hl=he) נקבעת בין היתר לפי מספר האסימונים של הקלט והפלט, ולכן כדאי לדעת איך לספור אסימונים.

## ספירת טוקנים

כל הקלט והפלט של Gemini API עוברים טוקניזציה, כולל טקסט, קובצי תמונות וסוגים אחרים של נתונים שאינם טקסט.

אפשר לספור טוקנים בדרכים הבאות:

- **מתקשרים אל `count_tokens` ומזינים את הבקשה.** הפונקציה מחזירה את המספר הכולל של הטוקנים *בקלט בלבד*. כדאי לבצע את השיחה הזו לפני שליחת קלט כדי לבדוק את גודל הבקשות.
- **משתמשים בלחצן `usage` בתגובה לאינטראקציה.** מחזירה את מספר הטוקנים של הקלט (`total_input_tokens`), הפלט (`total_output_tokens`), החשיבה (`total_thought_tokens`), התוכן שנשמר במטמון (`total_cached_tokens`), השימוש בכלי (`total_tool_use_tokens`) והסך הכולל (`total_tokens`).

### ספירת טוקנים של טקסט

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

# Count tokens before sending
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=prompt
)
print("total_tokens:", total_tokens.total_tokens)

# Get usage from interaction
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
const countResponse = await client.models.countTokens({
    model: "gemini-3.5-flash",
    contents: prompt,
});
console.log(countResponse.totalTokens);

// Get usage from interaction
const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: prompt,
});
console.log(interaction.usage);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:countTokens" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "The quick brown fox."}]}]}'
```

### ספירת טוקנים של שיחות רציפות

כדי לספור את הטוקנים בהיסטוריית השיחות, משתמשים ב-`previous_interaction_id`:

### Python

```
# This will only work for SDK newer than 2.0.0
# First interaction
interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="Hi, my name is Bob"
)

# Second interaction continues the conversation
interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    input="What's my name?",
    previous_interaction_id=interaction1.id
)

# Usage includes tokens from both turns
print(f"Input tokens: {interaction2.usage.total_input_tokens}")
print(f"Output tokens: {interaction2.usage.total_output_tokens}")
print(f"Total tokens: {interaction2.usage.total_tokens}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
// First interaction
const interaction1 = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Hi, my name is Bob"
});

// Second interaction continues the conversation
const interaction2 = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "What's my name?",
    previous_interaction_id: interaction1.id
});

console.log(`Input tokens: ${interaction2.usage.total_input_tokens}`);
console.log(`Output tokens: ${interaction2.usage.total_output_tokens}`);
```

### ספירת טוקנים מולטי-מודאליים

כל הקלט ל-Gemini API עובר טוקניזציה, כולל תמונות, סרטונים ואודיו.
נקודות חשובות לגבי יצירת טוקנים:

- **תמונות**: תמונות בגודל של ‎384 פיקסלים או פחות בשני הממדים נחשבות כ-258 טוקנים. תמונות גדולות יותר מחולקות למשבצות של 768x768 פיקסלים, וכל משבצת נחשבת כ-258 טוקנים.
- **וידאו**: 263 טוקנים לשנייה
- **אודיו**: 32 טוקנים לשנייה

#### טוקנים של תמונות

### Python

```
# This will only work for SDK newer than 2.0.0
uploaded_file = client.files.upload(file="path/to/image.jpg")

# Count tokens for image + text
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=["Tell me about this image", uploaded_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with image
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Tell me about this image"},
        {"type": "image", "uri": uploaded_file.uri, "mime_type": uploaded_file.mime_type}
    ]
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const uploadedFile = await client.files.upload({
    file: "path/to/image.jpg",
    config: { mimeType: "image/jpeg" }
});

// Count tokens
const countResponse = await client.models.countTokens({
    model: "gemini-3.5-flash",
    contents: [
        { text: "Tell me about this image" },
        { fileData: { fileUri: uploadedFile.uri, mimeType: uploadedFile.mimeType } }
    ]
});
console.log(countResponse.totalTokens);
```

**דוגמה לנתונים מוטבעים:**

### Python

```
# This will only work for SDK newer than 2.0.0
import base64

with open('image.jpg', 'rb') as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this image"},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.usage)
```

#### טוקנים של סרטונים

### Python

```
# This will only work for SDK newer than 2.0.0
import time

video_file = client.files.upload(file="path/to/video.mp4")

while not video_file.state or video_file.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    video_file = client.files.get(name=video_file.name)

# A 60-second video is approximately 263 * 60 = 15,780 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=["Summarize this video", video_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with video
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Summarize this video"},
        {"type": "video", "uri": video_file.uri, "mime_type": video_file.mime_type}
    ]
)
print(interaction.usage)
```

#### טוקנים של אודיו

### Python

```
# This will only work for SDK newer than 2.0.0
audio_file = client.files.upload(file="path/to/audio.mp3")

# A 60-second audio clip is approximately 32 * 60 = 1,920 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=["Transcribe this audio", audio_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with audio
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Transcribe this audio"},
        {"type": "audio", "uri": audio_file.uri, "mime_type": audio_file.mime_type}
    ]
)
print(interaction.usage)
```

### ספירת טוקנים של הוראות למערכת

ההוראות למערכת נספרות כחלק מאסימוני הקלט:

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Hello!",
    system_instruction="You are a helpful assistant who speaks like a pirate."
)

# system_instruction tokens included in total_input_tokens
print(f"Input tokens: {interaction.usage.total_input_tokens}")
```

### ספירת טוקנים בכלי

גם כלים (פונקציות, הפעלת קוד, חיפוש Google) נספרים:

### Python

```
# This will only work for SDK newer than 2.0.0
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            }
        }
    }
]

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What's the weather in Tokyo?",
    tools=tools
)

print(f"Input tokens: {interaction.usage.total_input_tokens}")
print(f"Tool use tokens: {interaction.usage.total_tool_use_tokens}")
```

## חלון ההקשר

לכל מודל Gemini יש מספר מקסימלי של טוקנים שהוא יכול לטפל בהם. חלון ההקשר מגדיר את המגבלה המשולבת של טוקנים של קלט ופלט.

### קבלת גודל חלון ההקשר באופן פרוגרמטי

### Python

```
# This will only work for SDK newer than 2.0.0
model_info = client.models.get(model="gemini-3.5-flash")
print(f"Input token limit: {model_info.input_token_limit}")
print(f"Output token limit: {model_info.output_token_limit}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const modelInfo = await client.models.get({ model: "gemini-3.5-flash" });
console.log(`Input token limit: ${modelInfo.inputTokenLimit}`);
console.log(`Output token limit: ${modelInfo.outputTokenLimit}`);
```

אפשר לראות את גודל חלון ההקשר בדף [מודלים](https://ai.google.dev/gemini-api/docs/models?hl=he).

## המאמרים הבאים

- [יצירת טקסט](https://ai.google.dev/gemini-api/docs/text-generation?hl=he): יסודות היצירה
- [שמירה במטמון](https://ai.google.dev/gemini-api/docs/caching?hl=he): הפחתת עלויות באמצעות שמירה במטמון
- [תמחור](https://ai.google.dev/gemini-api/docs/pricing?hl=he): הסבר על העלויות

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-06 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-06 (שעון UTC)."],[],[]]
