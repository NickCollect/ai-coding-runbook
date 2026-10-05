---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he
fetched_at: 2026-10-05T06:48:27.873601+00:00
title: "Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# Interactions API

‫Interactions API הוא הדרך הכי טובה לבנות באמצעות מודלים וסוכנים של Gemini. החל מיוני 2026, הוא זמין לכלל המשתמשים ומומלץ לכל הפרויקטים החדשים. למרות שהוא נחשב עכשיו לגרסה קודמת, ה-API המקורי [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=he) עדיין נתמך באופן מלא.

## למה כדאי להשתמש ב-Interactions API?

- **ממשק אוניברסלי לכל האפליקציות**: ממשק שנועד להיות הממשק הסטנדרטי לכל תרחישי השימוש, כולל יצירת טקסט בשיחה אחת, הבנה מולטי-מודאלית, פלט מובנה, תיאום בין כלים ותהליכי עבודה מבוססי-סוכנים.
- **ממשק API יחיד למודלים ולסוכנים**: נקודת קצה ודפוס מאוחדים לקריאה ישירה למודלים רגילים של Gemini ולסוכנים מיוחדים (כמו Deep Research וסוכנים מנוהלים בהתאמה אישית).
- **יכולות חדשות שזמינות מחוץ לקופסה**: תכונות כמו מצב שיחה אופציונלי בצד השרת באמצעות `previous_interaction_id`, שלבי ביצוע שניתנים לצפייה לצורך ניפוי באגים ועיבוד ממשק משתמש, ו[ביצוע ברקע](https://ai.google.dev/gemini-api/docs/background-execution?hl=he) של משימות ארוכות טווח באמצעות `background=true`.
- **עלות נמוכה יותר עם שיעורי פגיעה גבוהים יותר במטמון**: כשמשתמשים בשיחות מרובות תורות, ניהול מצב אופציונלי בצד השרת מאפשר שמירה יעילה יותר של הקשר במטמון בין התורות, וכך מצמצם את עלויות האסימונים.
- **איפה יושקו תכונות חדשות**: בעתיד, כל המודלים החדשים, היכולות הרב-מודאליות, הכלים והתכונות המבוססות על סוכנים יושקו ב-Interactions API.

כברירת מחדל, Interactions API שומר בקשות כדי שתוכלו להשתמש בתכונות של ניהול מצב בצד השרת באמצעות `previous_interaction_id`. כדי להפעיל התנהגות בלי שמירת מצב, צריך להגדיר את
`store=false`. פרטים נוספים זמינים בקטע [שמירת נתונים](#data-storage-retention).

## שנתחיל?

- **הגדרת סוכן התכנות**: מתחברים ל-**Gemini Docs MCP** ומתקינים את מיומנות `gemini-api-dev` כדי לתת לעוזר הדיגיטלי גישה ישירה למסמכי העזרה העדכניים למפתחים ולשיטות המומלצות. שלבים מפורטים מופיעים במאמר בנושא [הגדרת סוכן תכנות](https://ai.google.dev/gemini-api/docs/coding-agents?hl=he).
- **מעבר מ-`generateContent`**: אם יש לכם שילוב קיים, כדאי לעיין [במדריך למעבר](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=he) כדי לעבור ל-Interactions API.
- **איך מתחילים**: פועלים לפי השלבים שב[מדריך למתחילים בנושא Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=he).

### מדריכים לתכונות

במדריכים האלה מוסבר על היכולות הספציפיות של Interactions API. אפשר להשתמש במתג בדפים האלה כדי לעבור בין generateContent לבין Interactions API:

- [יצירת טקסט](https://ai.google.dev/gemini-api/docs/text-generation?hl=he)
- [יצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he)
- [הבנת תמונות](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he)
- [הבנת אודיו](https://ai.google.dev/gemini-api/docs/audio?hl=he)
- [הבנת סרטונים](https://ai.google.dev/gemini-api/docs/video-understanding?hl=he)
- [עיבוד מסמכים](https://ai.google.dev/gemini-api/docs/document-processing?hl=he)
- [בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)
- [פלט מובנה](https://ai.google.dev/gemini-api/docs/structured-output?hl=he)
- [Deep Research agent](https://ai.google.dev/gemini-api/docs/deep-research?hl=he)
- [היקש ברמת Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=he)
- [היקש בעדיפות גבוהה](https://ai.google.dev/gemini-api/docs/priority-inference?hl=he)

## איך Interactions API פועל

ה-API של אינטראקציות מתמקד במשאב ליבה: [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=he#Resource:Interaction). `Interaction` מייצג תור שלם בשיחה או במשימה. הוא משמש כתיעוד של סשן, ומכיל את ההיסטוריה המלאה של אינטראקציה כרצף כרונולוגי של **שלבי ביצוע**. השלבים האלה כוללים את המחשבות של המודל, קריאות לכלים ותוצאות בצד השרת או בצד הלקוח (כמו `function_call` ו-`function_result`) ואת `model_output` הסופי. המשאב המאוחסן (שאוחזר באמצעות `interactions.get`) כולל גם `user_input` שלבים להקשר מלא, אבל התשובה `interactions.create` מחזירה רק שלבים שנוצרו על ידי המודל.

כשמתקשרים אל [`interactions.create`](https://ai.google.dev/api/interactions-api?hl=he#CreateInteraction), יוצרים משאב חדש מסוג `Interaction`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me a short story about a time-traveling lighthouse."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Tell me a short story about a time-traveling lighthouse.",
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Tell me a short story about a time-traveling lighthouse."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Tell me a short story about a time-traveling lighthouse."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Tell me a short story about a time-traveling lighthouse."
  }'
```

### ניהול מצב בצד השרת

אפשר להשתמש ב-`id` של אינטראקציה שהסתיימה בקריאה הבאה באמצעות הפרמטר `previous_interaction_id` כדי להמשיך את השיחה. השרת משתמש במזהה הזה כדי לאחזר את היסטוריית השיחות, וכך לא צריך לשלוח מחדש את כל היסטוריית הצ'אט:

### Python

```
from google import genai

client = genai.Client()

# 1. First turn
turn1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hi, my name is Phil."
)

# 2. Second turn (chained using previous_interaction_id)
turn2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is my name?",
    previous_interaction_id=turn1.id
)

print(turn2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

// 1. First turn
const turn1 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Hi, my name is Phil.",
});

// 2. Second turn (chained using previous_interaction_id)
const turn2 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "What is my name?",
  previous_interaction_id: turn1.id,
});

console.log(turn2.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

// 1. First turn
Interaction turn1 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("Hi, my name is Phil."))
                    .build()))
        .interaction()
        .get();

// 2. Second turn (chained using previousInteractionId)
Interaction turn2 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("What is my name?"))
                    .previousInteractionId(turn1.id().get())
                    .build()))
        .interaction()
        .get();

System.out.println(turn2.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // 1. First turn
    turn1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Hi, my name is Phil."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // 2. Second turn (chained using PreviousInteractionID)
    turn2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-flash"),
            Input:                 interactions.NewInteractionsInput("What is my name?"),
            PreviousInteractionID: turn1.Interaction.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if turn2.Interaction.OutputText != nil {
        fmt.Println(*turn2.Interaction.OutputText)
    }
}
```

### REST

```
# Replace PREVIOUS_INTERACTION_ID with the id returned from the first turn
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is my name?",
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID"
  }'
```

הפרמטר `previous_interaction_id` שומר רק את היסטוריית השיחות (קלט ופלט) באמצעות `previous_interaction_id`. הפרמטרים האחרים הם **במסגרת האינטראקציה** והם חלים רק על האינטראקציה הספציפית שאתם יוצרים כרגע:

- `tools`
- `system_instruction`
- ‫`generation_config` (כולל `thinking_level`,‏ `temperature` וכו')

כלומר, אם רוצים שהפרמטרים האלה יחולו, צריך לציין אותם מחדש בכל אינטראקציה חדשה. ניהול המצב בצד השרת הוא אופציונלי. אפשר גם לפעול במצב חסר מצב על ידי שליחת היסטוריית השיחות המלאה בכל בקשה.

### אחסון נתונים ושמירתם

כברירת מחדל, ה-API שומר את כל אובייקטי האינטראקציה (`store=true`) כדי לפשט את השימוש בתכונות של ניהול מצב בצד השרת (עם `previous_interaction_id`), [הפעלה ברקע](https://ai.google.dev/gemini-api/docs/background-execution?hl=he) (באמצעות `background=true`) ולמטרות ניטור.

- **רמה בתשלום**: המערכת שומרת את האינטראקציות למשך **55 ימים**.
- **רמת שירות בחינם**: המערכת שומרת את האינטראקציות למשך **יום אחד**.

אם אתם לא רוצים את זה, אתם יכולים להגדיר `store=false` בבקשה. הפקד הזה נפרד מניהול המצב, ואפשר להשבית את האחסון בכל אינטראקציה. עם זאת, חשוב לזכור ש-`store=false` לא תואם ל[הרצה ברקע](https://ai.google.dev/gemini-api/docs/background-execution?hl=he) ומונע את השימוש ב-`previous_interaction_id` בתורות הבאות.

בפרויקטים במינוי בתשלום, אפשר להגדיר את חלון השמירה ב-[AI Studio](https://aistudio.google.com/logs?hl=he) כדי לסמן באופן אוטומטי יומנים למחיקה מאחסון הפרויקט אחרי 7, 14, 28 או 55 ימים. תקופת שמירה קצרה יותר עשויה להשפיע על אחזור שיחות קודמות.

אתם יכולים למחוק אינטראקציות שמורות בכל שלב באמצעות השיטה [`delete`](https://ai.google.dev/api/interactions-api?hl=he#deleteInteraction) באופן פרוגרמטי, שדורשת את מזהה האינטראקציה. בנוסף, אתם יכולים לראות ולנהל את יומני האינטראקציות המאוחסנים, כולל מחיקה מאחסון הפרויקט, ב-[AI Studio](https://aistudio.google.com/logs?hl=he).

אחרי שתקופת השמירה תסתיים, הנתונים יימחקו באופן אוטומטי.

אובייקטים של אינטראקציות מעובדים בהתאם [לתנאים](https://ai.google.dev/gemini-api/terms?hl=he).

### צפייה באינטראקציות ב-AI Studio

ממשק ה-API שומר בקשות של Interactions API שמופעלות באמצעות `store=true` עבור פרויקטים ברמה בתשלום. אפשר לראות אותם ישירות ב[דף היומנים ב-Google AI Studio](https://aistudio.google.com/logs?hl=he). מידע נוסף זמין [במדריך ליומנים](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=he).

## שיטות מומלצות

- **שיעור מציאות במטמון**: שמירה במטמון מרומזת נתמכת במצב עם שמירת מצב ובמצב בלי שמירת מצב (ראו [מדריך למתחילים](https://ai.google.dev/gemini-api/docs/get-started?hl=he#4_multi-turn_conversations)). השימוש ב-`previous_interaction_id` (עם שמירת מצב) כדי להמשיך שיחות מאפשר למערכת להשתמש בקלות רבה יותר במטמון מרומז להיסטוריית השיחות, וכך לשפר את הביצועים ולהפחית את העלויות.
- **שילוב אינטראקציות**: אתם יכולים לשלב בין אינטראקציות עם נציג ועם מודל במהלך שיחה. לדוגמה, אפשר להשתמש בסוכן מיוחד, כמו סוכן Deep Research, לאיסוף נתונים ראשוני, ואז להשתמש במודל Gemini רגיל למשימות המשך כמו סיכום או עיצוב מחדש, ולקשר בין השלבים האלה באמצעות `previous_interaction_id`.

## מודלים וסוכנים נתמכים

| שם דגם | סוג | מזהה דגם |
| --- | --- | --- |
| Gemini 3.8 Flash | מודל | `gemini-3.8-flash` |
| Gemini 3.7 Flash | מודל | `gemini-3.7-flash` |
| Gemini 3.6 Flash | מודל | `gemini-3.6-flash` |
| Gemini 3.5 Flash | מודל | `gemini-3.5-flash` |
| ‫Gemini 3.1 Pro Preview | מודל | `gemini-3.1-pro-preview` |
| Gemini 3.5 Flash-Lite | מודל | `gemini-3.5-flash-lite` |
| Gemini 3.1 Flash-Lite | מודל | `gemini-3.1-flash-lite` |
| ‫Gemini 3 Flash Preview | מודל | `gemini-3-flash-preview` |
| Gemini ‎2.5 Pro | מודל | `gemini-2.5-pro` |
| Gemini ‎2.5 Flash | מודל | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | מודל | `gemini-2.5-flash-lite` |
| ‫Gemini 3 Pro Image | מודל | `gemini-3-pro-image` |
| תמונה של Gemini 3.1 Flash | מודל | `gemini-3.1-flash-image` |
| ‫Gemini 3.1 Flash TTS (גרסת טרום-השקה) | מודל | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | מודל | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | מודל | `gemma-4-26b-a4b-it` |
| Lyria 3.5 | מודל | `lyria-3.5` |
| תצוגה מקדימה של קטע ב-Lyria 3 | מודל | `lyria-3-clip-preview` |
| גרסת טרום-השקה של Lyria 3 Pro | מודל | `lyria-3-pro-preview` |
| גרסת טרום-השקה (Preview) של Deep Research | סוכן | `deep-research-preview-04-2026` |
| גרסת טרום-השקה (Preview) של Deep Research | סוכן | `deep-research-max-preview-04-2026` |
| גרסת טרום-השקה של Antigravity | סוכן | `antigravity-preview-09-2026` |

## ערכות SDK

אתם יכולים להשתמש בגרסה העדכנית של Google GenAI SDK כדי לגשת אל Interactions API.

- ב-Python, זו חבילת `google-genai` החל מגרסה `2.3.0`.
- ב-JavaScript, מדובר בחבילה `@google/genai` מגרסה `2.3.0` ואילך.
- ב-Go, זו חבילת `google.golang.org/genai`.
- ב-Java, זה חבילת `com.google.genai:google-genai`.

מידע נוסף על התקנת ערכות ה-SDK זמין בדף [Libraries](https://ai.google.dev/gemini-api/docs/libraries?hl=he).

## מגבלות

- **MCP מרחוק**: Gemini 3 לא תומך ב-MCP מרחוק, אבל התמיכה הזו תגיע בקרוב.
- **תאימות של מודלים רב-שלביים**: כשמשלבים בין מודלים שונים בשיחה (עם שמירת מצב או בלי שמירת מצב), המודלים הבאים צריכים לתמוך בשיטות הפלט של המודלים הקודמים כקלט. לדוגמה, אם יוצרים תמונה באמצעות `gemini-3.1-flash-image`, אי אפשר להמשיך את השיחה עם מודל שלא מקבל קלט של תמונות (כמו מודל שמקבל רק טקסט או מודל ליצירת מוזיקה כמו Lyria).

התכונות הבאות נתמכות על ידי [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=he) API, אבל **עדיין לא זמינות** ב-Interactions API:

- ‫**[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he)**
- **[הפעלת פונקציות אוטומטית (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=he#automatic_function_calling_python_only)**
- **[שמירה במטמון באופן מפורש](https://ai.google.dev/gemini-api/docs/caching?hl=he)**: שימו לב ששמירה במטמון באופן מרומז בצד השרת זמינה ב-Interactions API באמצעות `previous_interaction_id`.
- **[הגדרות בטיחות](https://ai.google.dev/gemini-api/docs/safety-settings?hl=he)**: הגדרות בטיחות מותאמות אישית לא אפשריות ב-Interactions API.

## משוב

המשוב שלכם חשוב לנו מאוד לפיתוח של Interactions API.
אתם יכולים לשתף את המחשבות שלכם, לדווח על באגים או לבקש תכונות ב[פורום קהילת המפתחים של Google AI](https://discuss.ai.google.dev/c/gemini-api/4?hl=he).

## המאמרים הבאים

- אפשר לנסות את [המדריך המהיר לשימוש ב-Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=he).
- [מידע נוסף על סוכן Deep Research ב-Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=he)

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-10-01 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-10-01 (שעון UTC)."],[],[]]
