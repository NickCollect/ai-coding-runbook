---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=he
fetched_at: 2026-11-02T07:18:18.866935+00:00
title: "\u05d4\u05e1\u05d1\u05e8 \u05e2\u05dc \u05d2\u05e8\u05e1\u05d0\u05d5\u05ea API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon זמין עכשיו. [רוצים לנסות?](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=he)

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [הפניית API](https://ai.google.dev/api?hl=he)

שליחת משוב

# הסבר על גרסאות API

במאמר הזה מוסברים ההבדלים העיקריים בין גרסאות `v1` ו-`v1beta` של Gemini API.

- ‫**v1**: גרסה יציבה של ה-API. התכונות בגרסה היציבה נתמכות באופן מלא לאורך כל חיי הגרסה הראשית. אם יהיו שינויי תוכנה שעלולים לגרום לכשל, ניצור גרסה ראשית חדשה של ה-API ונוציא משימוש את הגרסה הקיימת אחרי פרק זמן סביר.
  יכול להיות שיוכנסו שינויים שלא גורמים לכשל ב-API בלי לשנות את הגרסה הראשית. ‫**Interactions API** והתכונות העיקריות שלו זמינים לכלל המשתמשים ב-`v1`.
- ‫**v1beta**: הגרסה הזו כוללת תכונות ויכולות מוקדמות שנמצאות בפיתוח פעיל. התכונות ב-`v1beta` עשויות להשתנות ככל שאנחנו משפרים אותן על סמך משוב, אבל אתם יכולים לנסות יכולות חדשות לפני שהן מועברות לגרסה היציבה.

## תמיכה ביכולות ובתכונות

בטבלה הבאה מפורטת הזמינות של היכולות ב-`v1` (GA) וב-`v1beta` (בטא). הכלים והיכולות העיקריים של ה-API חלים גם על Interactions API וגם על `generateContent`, אלא אם צוין אחרת:

| תכונה | v1 | v1beta |
| --- | --- | --- |
| **יכולות ה-API העיקריות** |  |  |
| [Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=he) |  |  |
| [קריאה להפעלת פונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he) |  |  |
| [פלט מובנה](https://ai.google.dev/gemini-api/docs/structured-output?hl=he) |  |  |
| [תהליך החשיבה / הרציונל](https://ai.google.dev/gemini-api/docs/thinking?hl=he) |  |  |
| [הוראות מערכת](https://ai.google.dev/gemini-api/docs/system-instructions?hl=he) |  |  |
| [פלט אודיו (הגדרת דיבור)](https://ai.google.dev/gemini-api/docs/audio?hl=he) |  |  |
| [רמת השירות (Priority או Flex)](https://ai.google.dev/gemini-api/docs/priority-inference?hl=he) |  |  |
| **כלים** |  |  |
| [כלי להרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he) |  |  |
| [ביסוס בעזרת חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he) |  |  |
| [ביסוס עובדות במפות Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he) |  |  |
| [הכלי URL Context](https://ai.google.dev/gemini-api/docs/url-context?hl=he) |  |  |
| [כלי לחיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he) |  |  |
| [הכלי לשימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he) |  |  |
| [כלי שרתי MCP](https://ai.google.dev/gemini-api/docs/function-calling?hl=he#mcp) |  |  |
| **ממשקי API בזמן אמת** |  |  |
| [Live API (WebSockets)](https://ai.google.dev/gemini-api/docs/live-api?hl=he) |  |  |
| [Live Music API](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=he) |  |  |
| [טוקנים זמניים (Live API)](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=he) |  |  |
| **ממשקי API של הפלטפורמה** |  |  |
| [Models API](https://ai.google.dev/gemini-api/docs/models?hl=he) |  |  |
| [Files Service Route](https://ai.google.dev/gemini-api/docs/files?hl=he) |  |  |
| [מסלול החנויות בחיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he) |  |  |
| [Agents API](https://ai.google.dev/gemini-api/docs/agents?hl=he) |  |  |
| [Webhooks API](https://ai.google.dev/gemini-api/docs/webhooks?hl=he) |  |  |
| [שמירת הקשר במטמון](https://ai.google.dev/gemini-api/docs/caching?hl=he) |  |  |

- ‫ – יש תמיכה

## הגדרת גרסת API ב-SDK

ערכות ה-SDK של Gemini API מוגדרות כברירת מחדל ל-`v1beta`, אבל אתם יכולים לציין גרסאות באופן מפורש על ידי הגדרת גרסת ה-API, כמו שמוצג בדוגמת הקוד הבאה:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.HttpOptions;

Client client = Client.builder()
    .httpOptions(HttpOptions.builder().apiVersion("v1").build())
    .build();

CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.6-flash"))
    .input(InteractionsInput.of("Explain how AI works"))
    .build();
var interaction = client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
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
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        HTTPOptions: genai.HTTPOptions{
            APIVersion: "v1",
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.6-flash"),
            Input: interactions.NewInteractionsInput("Explain how AI works"),
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
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works",
  }'
```

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-10-30 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-10-30 (שעון UTC)."],[],[]]
