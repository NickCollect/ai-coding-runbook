---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=he
fetched_at: 2026-09-21T05:56:21.930642+00:00
title: "\u05e8\u05d6\u05d5\u05dc\u05d5\u05e6\u05d9\u05d9\u05ea \u05d4\u05de\u05d3\u05d9\u05d4 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# רזולוציית המדיה

הפרמטר `media_resolution` קובע איך Gemini API מעבד קלט של מדיה, כמו תמונות, סרטונים, אודיו ומסמכי PDF, על ידי קביעת **מספר הטוקנים המקסימלי** שמוקצה לקלט של מדיה. כך אפשר לאזן בין איכות התשובה לבין זמן האחזור והעלות. בעוד שהקצאת הטוקנים בקלט של תמונות ומסמכים מותאמת להגדרת הרזולוציה, קלט של אודיו עובר טוקניזציה בקצב קבוע לשנייה בכל רמות הרזולוציה. בקטע [ספירת טוקנים](#token-counts) מפורטים ערכי ברירת המחדל של הגדרות שונות וההתאמה שלהם לטוקנים.

אתם יכולים להגדיר את רזולוציית המדיה לאובייקטים נפרדים של מדיה (פריטי תוכן) בבקשה (רק ב-Gemini 3).

## רזולוציית מדיה לכל פריט תוכן (Gemini 3 בלבד)

‫Gemini 3 מאפשר לכם להגדיר רזולוציית מדיה לאובייקטים ספציפיים של מדיה בבקשה, וכך לבצע אופטימיזציה פרטנית של השימוש בטוקנים. אפשר לשלב רמות רזולוציה שונות בבקשה אחת. לדוגמה, שימוש ברזולוציה גבוהה לתרשים מורכב וברזולוציה נמוכה לתמונה פשוטה שמוסיפה הקשר.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Describe the details in this high-resolution image.").build();
Content imageContent =
    ImageContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/image/scones.jpg")
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## ערכי הרזולוציה הזמינים

ב-Gemini API מוגדרות רמות הרזולוציה הבאות של מדיה:

- ‫`unspecified`: הגדרת ברירת המחדל. מספר הטוקנים ברמה הזו משתנה באופן משמעותי בין Gemini 3 לבין מודלים קודמים של Gemini.
- ‫`low`: מספר הטוקנים נמוך יותר, ולכן העיבוד מהיר יותר והעלות נמוכה יותר, אבל יש פחות פרטים.
- ‫`medium`: איזון בין רמת הפירוט, העלות וזמן האחזור.
- ‫`high`: מספר גבוה יותר של טוקנים, שמספק למודל יותר פרטים לעבודה, אבל על חשבון עלות גבוהה יותר וזמן אחזור ארוך יותר.
- ‫`ultra_high` (לכל פריט תוכן בלבד): כמות הטוקנים הגבוהה ביותר, נדרש לתרחישי שימוש ספציפיים כמו [שימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he).

חשוב לזכור שההגדרה `high` מספקת את הביצועים האופטימליים ברוב תרחישי השימוש.

המספר המדויק של הטוקנים שנוצרים בכל אחת מהרמות האלה תלוי ב**סוג המדיה** (תמונה, סרטון, אודיו, PDF) וב**גרסת המודל**.

## מספר הטוקנים

בטבלאות הבאות מפורטות ספירות האסימונים המשוערות לכל ערך של `media_resolution` ולכל סוג מדיה לכל משפחת מודלים.

**מודלים של Gemini 3**

| MediaResolution | תמונה | וידאו | אודיו | PDF |
| --- | --- | --- | --- | --- |
| ‫`unspecified` (ברירת מחדל) | 1120 | 70 | ‫25 (לשנייה) | 560 |
| `low` | 280 | 70 | ‫25 (לשנייה) | ‫280 + טקסט חי |
| `medium` | 560 | 70 | ‫25 (לשנייה) | ‫560 + טקסט חי |
| `high` | 1120 | 280 | ‫25 (לשנייה) | ‫1120 + טקסט חי |
| `ultra_high` | 2240 | לא רלוונטי | לא רלוונטי | לא רלוונטי |

## בחירת הרזולוציה המתאימה

- **ברירת מחדל (`unspecified`):** מתחילים עם ברירת המחדל. הוא מותאם לאיזון טוב בין איכות, זמן אחזור ועלות ברוב תרחישי השימוש הנפוצים.
- ‫**`low`:** מתאים לתרחישים שבהם העלות והחביון הם בעלי חשיבות עליונה, ופרטים מדויקים פחות קריטיים.
- ‫**`medium` / `high`:** הגדלת הרזולוציה כשנדרשת הבנה של פרטים מורכבים במדיה. היכולת הזו נדרשת לעיתים קרובות לניתוח חזותי מורכב, לקריאת תרשימים או להבנת מסמכים עמוסים במידע.
- ‫**`ultra_high`** – זמין רק להגדרה של כל פריט תוכן. מומלץ לתרחישי שימוש ספציפיים, כמו שימוש במחשב, או במקרים שבהם בדיקות מראות שיפור ברור לעומת `high`.
- **שליטה בכל פריט תוכן (Gemini 3):** אופטימיזציה של השימוש בטוקנים. לדוגמה, בהנחיה עם כמה תמונות, אפשר להשתמש ב-`high` לדיאגרמה מורכבת וב-`low` או ב-`medium` לתמונות פשוטות יותר שמוצגות בהקשר.

**הגדרות מומלצות**

ברשימה הבאה מפורטות הגדרות הרזולוציה המומלצות של המדיה לכל סוג מדיה נתמך.

| סוג מדיה | הגדרה מומלצת | מספר הטוקנים המקסימלי | הנחיות לשימוש |
| --- | --- | --- | --- |
| **תמונות** | `high` | 1120 | מומלץ לרוב משימות ניתוח התמונות כדי להבטיח איכות מקסימלית. |
| **קובצי PDF** | `medium` | 560 | אופטימלי להבנת מסמכים. האיכות מגיעה בדרך כלל לנקודת רוויה ב-`medium`. הגדלה ל-`high` משפרת לעיתים רחוקות את תוצאות ה-OCR במסמכים רגילים. |
| **סרטון** (כללי) | `low` (או `medium`) | ‫70 (לכל פריים) | **הערה:** כשמדובר בסרטונים, ההגדרות `low` ו-`medium` מטופלות באופן זהה (70 טוקנים) כדי לייעל את השימוש בהקשר. זה מספיק לרוב המשימות של זיהוי פעולות ותיאור. |
| **סרטון** (עם הרבה טקסט) | `high` | ‫280 (לכל פריים) | נדרש רק אם תרחיש השימוש כולל קריאה של טקסט צפוף (OCR) או פרטים קטנים בתוך פריים של סרטון. |
| **אודיו** | ‫`unspecified` (ברירת מחדל) | ‫25 (לשנייה) | האודיו עובר טוקניזציה בקצב קבוע של 25 טוקנים לשנייה בכל הגדרות הרזולוציה הנתמכות (`unspecified`, ‏`low`, ‏`medium` ו-`high`). |

חשוב תמיד לבדוק ולהעריך את ההשפעה של הגדרות רזולוציה שונות על האפליקציה, כדי למצוא את האיזון הטוב ביותר בין איכות, זמן אחזור ועלות.

## הקשר בין מצבי העיבוד של הסרטון

הפרמטרים של `media_resolution` ושל העיבוד שולטים בהיבטים שונים של קלט הווידאו:

- ‫`media_resolution` שולט ב**רזולוציה** של כל פריים (מספר הטוקנים לכל פריים).
- ‫`processing` / `media_processing` קובעים **איזה תוכן מהסרטון** ייטען בהקשר.

אפשר להגדיר את שניהם באותו קלט וידאו. לדוגמה, אפשר להשתמש בעיבוד מבוסס-סוכן עם רזולוציית מדיה נמוכה כדי למזער את השימוש הכולל בטוקנים בסרטון ארוך.

פרטים על מצבי עיבוד של סרטונים זמינים במדריך [הבנת סרטונים באמצעות AI](https://ai.google.dev/gemini-api/docs/video-understanding?hl=he#agentic-video-understanding).

## סיכום תאימות הגרסה

- ההגדרה `resolution` בפריטי תוכן ספציפיים **זמינה רק במודלים של Gemini 3**.

## השלבים הבאים

- במדריכים [הבנת תמונות](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he), [הבנת סרטונים](https://ai.google.dev/gemini-api/docs/video-understanding?hl=he), [הבנת אודיו](https://ai.google.dev/gemini-api/docs/audio?hl=he) ו[הבנת מסמכים](https://ai.google.dev/gemini-api/docs/document-processing?hl=he) אפשר לקרוא מידע נוסף על היכולות המולטי-מודאליות של Gemini API.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-19 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-19 (שעון UTC)."],[],[]]
