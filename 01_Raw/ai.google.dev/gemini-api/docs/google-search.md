---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=he
fetched_at: 2026-05-05T19:44:28.801953+00:00
title: "\u05e2\u05d9\u05d2\u05d5\u05df \u05d1\u05d0\u05de\u05e6\u05e2\u05d5\u05ea \u05d7\u05d9\u05e4\u05d5\u05e9 Google \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# עיגון באמצעות חיפוש Google

עיגון באמצעות חיפוש Google מחבר את מודל Gemini לתוכן אינטרנט בזמן אמת, והוא פועל בכל השפות הזמינות. כך Gemini יכול לספק תשובות מדויקות יותר ולצטט מקורות שאפשר לאמת אותם, גם אם הם פורסמו אחרי תאריך סף הידע שלו.

ההארקה עוזרת לכם ליצור אפליקציות שיכולות:

- **שיפור הדיוק העובדתי:** כדי לצמצם את ההזיות של המודל, התשובות מבוססות על מידע מהעולם האמיתי.
- **גישה למידע בזמן אמת:** אפשר לקבל תשובות לשאלות על אירועים ונושאים עדכניים.
- **לספק ציטוטים:** כדי לבנות את אמון המשתמשים, כדאי להציג את המקורות של הטענות של המודל.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Who won the euro 2024?",
    config=config,
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const groundingTool = {
  googleSearch: {},
};

const config = {
  tools: [groundingTool],
};

const response = await ai.models.generateContent({
  model: "gemini-3-flash-preview",
  contents: "Who won the euro 2024?",
  config,
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

מידע נוסף זמין ב[מחברת של כלי החיפוש](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=he).

## איך עיגון באמצעות חיפוש Google פועל

כשמפעילים את הכלי `google_search`, המודל מטפל בכל תהליך העבודה של חיפוש, עיבוד וציטוט מידע באופן אוטומטי.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=he)

1. **הנחיית משתמש:** האפליקציה שולחת הנחיית משתמש אל Gemini API עם הכלי `google_search` מופעל.
2. **ניתוח ההנחיה:** המודל מנתח את ההנחיה וקובע אם חיפוש ב-Google יכול לשפר את התשובה.
3. **חיפוש Google:** אם צריך, המודל יוצר באופן אוטומטי שאילתת חיפוש אחת או יותר ומריץ אותן.
4. **עיבוד תוצאות החיפוש:** המודל מעבד את תוצאות החיפוש, מסנתז את המידע ומנסח תגובה.
5. **תשובה מבוססת:** ה-API מחזיר תשובה סופית וידידותית למשתמש שמבוססת על תוצאות החיפוש. התשובה הזו כוללת את התשובה הטקסטואלית של המודל, `groundingMetadata` עם שאילתות החיפוש, תוצאות החיפוש והציטוטים.

## הסבר על תגובת ההארקה

כשמקרקעים תשובה בהצלחה, התשובה כוללת את השדה `groundingMetadata`. הנתונים המובנים האלה חיוניים לאימות הטענות וליצירת חוויית ציטוט עשירה באפליקציה.

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

‫Gemini API מחזיר את המידע הבא עם התג `groundingMetadata`:

- ‫`webSearchQueries` : מערך של שאילתות החיפוש שנעשה בהן שימוש. המידע הזה שימושי לניפוי באגים ולהבנת תהליך החשיבה של המודל.
- ‫`searchEntryPoint` : מכיל את ה-HTML ואת ה-CSS לעיבוד הצעות החיפוש הנדרשות. דרישות השימוש המלאות מפורטות [בתנאים ובהגבלות](https://ai.google.dev/gemini-api/terms?hl=he#grounding-with-google-search).
- ‫`groundingChunks` : מערך של אובייקטים שמכילים את המקורות באינטרנט (`uri` ו-`title`).
- ‫`groundingSupports` : מערך של מקטעים לחיבור התגובה של המודל `text` למקורות ב-`groundingChunks`. כל מקטע מקשר טקסט `segment` (מוגדר על ידי `startIndex` ו-`endIndex`) ל-`groundingChunkIndices` אחד או יותר. זהו המפתח ליצירת ציטוטים בגוף הטקסט.

אפשר גם להשתמש בעיגון באמצעות חיפוש Google בשילוב עם [כלי ההקשר של כתובת ה-URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he) כדי לעגן תשובות גם על נתונים ציבוריים באינטרנט וגם על כתובות URL ספציפיות שאתם מספקים.

## שיוך מקורות באמצעות ציטוטים מוטמעים

ממשק ה-API מחזיר נתוני ציטוט מובְנים, כך שיש לכם שליטה מלאה על האופן שבו אתם מציגים מקורות בממשק המשתמש. אפשר להשתמש בשדות `groundingSupports` ו-`groundingChunks` כדי לקשר את ההצהרות של המודל ישירות למקורות שלהן. הנה דפוס נפוץ לעיבוד המטא-נתונים כדי ליצור תגובה עם ציטוטים מוטבעים שאפשר ללחוץ עליהם.

### Python

```
def add_citations(response):
    text = response.text
    supports = response.candidates[0].grounding_metadata.grounding_supports
    chunks = response.candidates[0].grounding_metadata.grounding_chunks

    # Sort supports by end_index in descending order to avoid shifting issues when inserting.
    sorted_supports = sorted(supports, key=lambda s: s.segment.end_index, reverse=True)

    for support in sorted_supports:
        end_index = support.segment.end_index
        if support.grounding_chunk_indices:
            # Create citation string like [1](link1)[2](link2)
            citation_links = []
            for i in support.grounding_chunk_indices:
                if i < len(chunks):
                    uri = chunks[i].web.uri
                    citation_links.append(f"[{i + 1}]({uri})")

            citation_string = ", ".join(citation_links)
            text = text[:end_index] + citation_string + text[end_index:]

    return text

# Assuming response with grounding metadata
text_with_citations = add_citations(response)
print(text_with_citations)
```

### JavaScript

```
function addCitations(response) {
    let text = response.text;
    const supports = response.candidates[0]?.groundingMetadata?.groundingSupports;
    const chunks = response.candidates[0]?.groundingMetadata?.groundingChunks;

    // Sort supports by end_index in descending order to avoid shifting issues when inserting.
    const sortedSupports = [...supports].sort(
        (a, b) => (b.segment?.endIndex ?? 0) - (a.segment?.endIndex ?? 0),
    );

    for (const support of sortedSupports) {
        const endIndex = support.segment?.endIndex;
        if (endIndex === undefined || !support.groundingChunkIndices?.length) {
        continue;
        }

        const citationLinks = support.groundingChunkIndices
        .map(i => {
            const uri = chunks[i]?.web?.uri;
            if (uri) {
            return `[${i + 1}](${uri})`;
            }
            return null;
        })
        .filter(Boolean);

        if (citationLinks.length > 0) {
        const citationString = citationLinks.join(", ");
        text = text.slice(0, endIndex) + citationString + text.slice(endIndex);
        }
    }

    return text;
}

const textWithCitations = addCitations(response);
console.log(textWithCitations);
```

התשובה החדשה עם ציטוטים מוטבעים תיראה כך:

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
```

## תמחור

כשמשתמשים ב-עיגון באמצעות חיפוש Google עם Gemini 3, הפרויקט מחויב על כל שאילתת חיפוש שהמודל מחליט להריץ. אם המודל מחליט להריץ כמה שאילתות חיפוש כדי לענות על הנחיה אחת (לדוגמה, חיפוש של `"UEFA Euro 2024 winner"` ושל `"Spain vs England Euro 2024 final
score"` באותה קריאה ל-API), זה נחשב כשני שימושים מחויבים בכלי עבור הבקשה הזו. לצורך חיוב, אנחנו מתעלמים משאילתות חיפוש אינטרנט ריקות כשסופרים שאילתות ייחודיות. מודל החיוב הזה רלוונטי רק למודלים של Gemini 3. כשמשתמשים בהארקה של חיפוש עם Gemini 2.5 או מודלים ישנים יותר, החיוב על הפרויקט הוא לפי הנחיה.

למידע מפורט על התמחור, אפשר לעיין ב[דף התמחור של Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=he).

## מודלים נתמכים

אפשר למצוא את כל היכולות בדף [סקירה כללית של המודל](https://ai.google.dev/gemini-api/docs/models?hl=he).

| דגם | עיגון באמצעות חיפוש Google |
| --- | --- |
| תצוגה מקדימה של תמונה ב-Gemini 3.1 Flash | ✔️ |
| ‫Gemini 3.1 Pro Preview | ✔️ |
| תצוגה מקדימה של תמונות ב-Gemini 3 Pro | ✔️ |
| ‫Gemini 3 Flash Preview | ✔️ |
| Gemini ‎2.5 Pro | ✔️ |
| Gemini ‎2.5 Flash | ✔️ |
| ‫Gemini ‎2.5 Flash-Lite | ✔️ |
| Gemini ‎2.0 Flash | ✔️ |

## שילובים נתמכים של כלים

אתם יכולים להשתמש ב-עיגון באמצעות חיפוש Google יחד עם כלים אחרים כמו [הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he) ו[הקשר של כתובת URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he) כדי להפעיל תרחישי שימוש מורכבים יותר.

מודלים של Gemini 3 תומכים בשילוב של כלים מובנים (כמו Grounding עם חיפוש Google) עם כלים מותאמים אישית (קריאה לפונקציה). מידע נוסף זמין בדף [שילובים של כלים](https://ai.google.dev/gemini-api/docs/tool-combination?hl=he).

## המאמרים הבאים

- כדאי לנסות את [המתכון לעיגון באמצעות חיפוש Google ב-Gemini API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=he).
- אפשר לקרוא על כלים זמינים אחרים, כמו [הפעלת פונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he).
- [כאן](https://ai.google.dev/gemini-api/docs/url-context?hl=he) מוסבר איך להוסיף לתיאורים כתובות URL ספציפיות באמצעות הכלי 'הקשר של כתובת URL'.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-04-29 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-04-29 (שעון UTC)."],[],[]]
