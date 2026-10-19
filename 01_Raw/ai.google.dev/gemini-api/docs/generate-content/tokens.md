---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=he
fetched_at: 2026-10-19T05:48:48.459968+00:00
title: "\u05d4\u05e1\u05d1\u05e8 \u05e2\u05dc \u05d0\u05e1\u05d9\u05de\u05d5\u05e0\u05d9\u05dd \u05d5\u05e1\u05e4\u05d9\u05e8\u05d4 \u05e9\u05dc\u05d4\u05dd \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon זמין עכשיו. [רוצים לנסות?](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=he)

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=he)

שליחת משוב

# הסבר על אסימונים וספירה שלהם

‫Gemini ומודלים אחרים של AI גנרטיבי מעבדים קלט ופלט ברמת פירוט שנקראת *טוקן*.

**במודלים של Gemini, טוקן שווה ערך לכ-4 תווים.
‫100 טוקנים שווים לכ-60 עד 80 מילים באנגלית.**

## מידע על טוקנים

האסימונים יכולים להיות תווים בודדים כמו `z` או מילים שלמות כמו `cat`. מילים ארוכות
מפוצלות לכמה טוקנים. קבוצת כל האסימונים שבהם המודל משתמש נקראת אוצר המילים, והתהליך של פיצול הטקסט לאסימונים נקרא *המרה לאסימונים*.

כשהחיוב מופעל, [העלות של קריאה ל-Gemini API](https://ai.google.dev/pricing?hl=he) נקבעת בין היתר לפי מספר הטוקנים של הקלט והפלט, ולכן כדאי לדעת איך לספור טוקנים.

אתם יכולים לנסות לספור טוקנים ב-Colab שלנו.

|  |  |  |
| --- | --- | --- |
| [לצפייה באתר ai.google.dev](https://ai.google.dev/gemini-api/docs/tokens?hl=he) | [התנסות בנוטבוק של Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=he) | [הצגת ה-notebook ב-GitHub](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=he) |

## ספירת טוקנים

כל הקלט והפלט של Gemini API עוברים המרה לאסימונים, כולל טקסט, קובצי תמונות ומודלים אחרים שהם לא טקסט.

אפשר לספור טוקנים בדרכים הבאות:

- **קוראים ל-[`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=he) עם הקלט של הבקשה.**‫  
   הפונקציה מחזירה את המספר הכולל של הטוקנים ב*קלט בלבד*. אפשר לבצע את הקריאה הזו לפני ששולחים את הקלט למודל כדי לבדוק את גודל הבקשות.
- **משתמשים במאפיין `usage_metadata` באובייקט `response` אחרי הקריאה ל-`generate_content`.**  
   הפונקציה מחזירה את המספר הכולל של הטוקנים *גם בקלט וגם בפלט*: `total_token_count`.  
   הפונקציה גם מחזירה את ספירת הטוקנים של הקלט והפלט בנפרד: `prompt_token_count` (טוקנים של קלט) ו-`candidates_token_count` (טוקנים של פלט).

  אם אתם משתמשים ב[מודל חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he), הטוקנים שנעשה בהם שימוש במהלך תהליך החשיבה מוחזרים ב-`thoughts_token_count`. אם אתם משתמשים ב[שמירת הקשר במטמון](https://ai.google.dev/gemini-api/docs/caching?hl=he), כמות הטוקנים שנשמרו במטמון תופיע ב-`cached_content_token_count`.

### ספירת טוקנים של טקסט

אם מתקשרים אל `count_tokens` עם קלט טקסט בלבד, הפונקציה מחזירה את מספר הטוקנים של
הטקסט *בקלט בלבד* (`total_tokens`). אפשר להתקשר אל לפני
שמתקשרים אל `generate_content` כדי לבדוק את גודל הבקשות.

אפשרות נוספת היא להפעיל את `generate_content` ואז להשתמש במאפיין `usage_metadata` באובייקט `response` כדי לקבל את הפרטים הבאים:

- מספר הטוקנים הנפרד של הקלט (`prompt_token_count`), התוכן שנשמר במטמון (`cached_content_token_count`) והפלט (`candidates_token_count`)
- כמות הטוקנים של תהליך החשיבה (`thoughts_token_count`)
- המספר הכולל של הטוקנים *בקלט ובפלט* (`total_token_count`)

### Python

```
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash", contents=prompt
)
print("total_tokens: ", total_tokens)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=prompt
)

print(response.usage_metadata)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

async function main() {
  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.8-flash",
    contents: prompt,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: prompt,
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

// Convert prompt to a slice of *genai.Content using the helper.
contents := []*genai.Content{
  genai.NewContentFromText(prompt, genai.RoleUser),
}
countResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  return err
}
fmt.Println("total_tokens:", countResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
    ```
```

### ספירת טוקנים בשיחה עם זיכרון (צ'אט)

אם מתקשרים אל `count_tokens` עם היסטוריית הצ'אט, הפונקציה מחזירה את המספר הכולל של הטוקנים בטקסט מכל תפקיד בצ'אט (`total_tokens`).

אפשרות נוספת היא להפעיל את `send_message` ואז להשתמש במאפיין `usage_metadata` באובייקט `response` כדי לקבל את הפרטים הבאים:

- מספר הטוקנים הנפרדים של הקלט (`prompt_token_count`), התוכן שנשמר במטמון (`cached_content_token_count`) והפלט (`candidates_token_count`)
- כמות הטוקנים של תהליך החשיבה (`thoughts_token_count`)
- המספר הכולל של הטוקנים *בקלט ובפלט* (`total_token_count`)

כדי להבין מה יהיה גודל התור הבא של השיחה, צריך לצרף אותו להיסטוריה כשמתקשרים אל `count_tokens`.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.8-flash",
    history=[
        types.Content(
            role="user", parts=[types.Part(text="Hi my name is Bob")]
        ),
        types.Content(role="model", parts=[types.Part(text="Hi Bob!")]),
    ],
)

print(
    client.models.count_tokens(
        model="gemini-3.8-flash", contents=chat.get_history()
    )
)

response = chat.send_message(
    message="In one sentence, explain how a computer works to a young child."
)
print(response.usage_metadata)

extra = types.UserContent(
    parts=[
        types.Part(
            text="What is the meaning of life?",
        )
    ]
)
history = [*chat.get_history(), extra]
print(client.models.count_tokens(model="gemini-3.8-flash", contents=history))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  const history = [
    { role: "user", parts: [{ text: "Hi my name is Bob" }] },
    { role: "model", parts: [{ text: "Hi Bob!" }] },
  ];
  const chat = ai.chats.create({
    model: "gemini-3.8-flash",
    history: history,
  });

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.8-flash",
    contents: chat.getHistory(),
  });
  console.log(countTokensResponse.totalTokens);

  const chatResponse = await chat.sendMessage({
    message: "In one sentence, explain how a computer works to a young child.",
  });
  console.log(chatResponse.usageMetadata);

  const extraMessage = {
    role: "user",
    parts: [{ text: "What is the meaning of life?" }],
  };
  const combinedHistory = [...chat.getHistory(), extraMessage];
  const combinedCountTokensResponse = await ai.models.countTokens({
    model: "gemini-3.8-flash",
    contents: combinedHistory,
  });
  console.log(
    "Combined history token count:",
    combinedCountTokensResponse.totalTokens,
  );
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

history := []*genai.Content{
  {Role: genai.RoleUser, Parts: []*genai.Part({Text: "Hi my name is Bob"})},
  {Role: genai.RoleModel, Parts: []*genai.Part({Text: "Hi Bob!"})},
}
chat, err := client.Chats.Create(ctx, "gemini-3.8-flash", nil, history)
if err != nil {
  log.Fatal(err)
}

firstTokenResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", chat.History(false), nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println(firstTokenResp.TotalTokens)

resp, err := chat.SendMessage(ctx, genai.NewPartFromText("In one sentence, explain how a computer works to a young child."))
if err != nil {
  log.Fatal(err)
}
fmt.Printf("%#v\n", resp.UsageMetadata)

extra := genai.NewContentFromText("What is the meaning of life?", genai.RoleUser)
hist := chat.History(false)
hist = append(hist, extra)

secondTokenResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", hist, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println(secondTokenResp.TotalTokens)
```

### ספירת טוקנים מולטי-מודאליים

כל הקלט ל-Gemini API עובר טוקניזציה, כולל טקסט, קובצי תמונות וסוגים אחרים של נתונים שאינם טקסט. חשוב לשים לב לנקודות העיקריות הבאות לגבי טוקניזציה של קלט מולטימודלי במהלך העיבוד על ידי Gemini API:

- תמונות קלט ששני הממדים שלהן קטנים מ-384 פיקסלים או שווים ל-384 פיקסלים נספרות כ-258 אסימונים. תמונות שגדולות יותר באחד מהממדים או בשניהם נחתכות ומשתנות בהתאם לצורך למשבצות של 768x768 פיקסלים, וכל אחת מהן נספרת כ-258 אסימונים.
- קובצי וידאו ואודיו מומרים לטוקנים בשיעורים הקבועים הבאים:
  וידאו ב-263 טוקנים לשנייה ואודיו ב-32 טוקנים לשנייה. התעריף הזה חל על עיבוד סטטי (ברירת המחדל). במקרה של עיבוד באמצעות סוכנים, השימוש באסימונים משתנה. [כאן אפשר לראות את השימוש באסימוני וידאו לפי מצב עיבוד](#video-token-usage).

#### רזולוציות של מדיה

[במודלים של Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-3) יש שליטה מפורטת על עיבוד הראייה המולטימודלי באמצעות הפרמטר `media_resolution`. הפרמטר `media_resolution` קובע את **המספר המקסימלי של אסימונים שמוקצים לכל תמונה או פריים של סרטון בקלט.**
רזולוציות גבוהות יותר משפרות את היכולת של המודל לקרוא טקסט קטן או לזהות פרטים קטנים, אבל מגדילות את השימוש בטוקנים ואת זמן הטעינה.

למידע נוסף על הפרמטר ועל האופן שבו הוא יכול להשפיע על חישובי הטוקנים, עיינו במדריך בנושא [רזולוציית מדיה](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=he).

#### קובצי תמונות

אם קוראים ל-`count_tokens` עם קלט של טקסט ותמונה, הפונקציה מחזירה את מספר הטוקנים המשולב של הטקסט והתמונה *בקלט בלבד* (`total_tokens`). אפשר לבצע את הקריאה הזו לפני שקוראים ל-`generate_content` כדי לבדוק את גודל הבקשות. אפשר גם להפעיל את `count_tokens` על הטקסט ועל הקובץ בנפרד.

אפשרות נוספת היא להתקשר אל `generate_content` ואז להשתמש במאפיין `usage_metadata`
באובייקט `response` כדי לקבל את הפרטים הבאים:

- מספר הטוקנים הנפרד של הקלט (`prompt_token_count`), התוכן שנשמר במטמון (`cached_content_token_count`) והפלט (`candidates_token_count`)
- כמות הטוקנים של תהליך החשיבה (`thoughts_token_count`)
- המספר הכולל של הטוקנים *גם בקלט וגם בפלט*
  (`total_token_count`)

דוגמה לשימוש בתמונה שהועלתה מ-File API:

### Python

```
from google import genai

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = client.files.upload(file=media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3.8-flash", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[prompt, your_image_file]
)
print(response.usage_metadata)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});
const prompt = "Tell me about this image";

async function main() {
  const organ = await ai.files.upload({
    file: path.join(media, "organ.jpg"),
    config: { mimeType: "image/jpeg" },
  });

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(organ.uri, organ.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(organ.uri, organ.mimeType),
    ]),
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

file, err := client.Files.UploadFromPath(
  ctx, 
  filepath.Join(getMedia(), "organ.jpg"), 
  &genai.UploadFileConfig{
    MIMEType : "image/jpeg",
  },
)
if err != nil {
  log.Fatal(err)
}
parts := []*genai.Part{
  genai.NewPartFromText("Tell me about this image"),
  genai.NewPartFromURI(file.URI, file.MIMEType),
}
contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

דוגמה שבה התמונה מסופקת כנתונים מוטבעים:

### Python

```
from google import genai
import PIL.Image

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = PIL.Image.open(media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3.8-flash", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[prompt, your_image_file]
)
print(response.usage_metadata)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});
const prompt = "Tell me about this image";
const imageBuffer = fs.readFileSync(path.join(media, "organ.jpg"));

const imageBase64 = imageBuffer.toString("base64");

const contents = createUserContent([
  prompt,
  createPartFromBase64(imageBase64, "image/jpeg"),
]);

async function main() {
  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.8-flash",
    contents: contents,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: contents,
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

imageBytes, err := os.ReadFile("organ.jpg")
if err != nil {
    log.Fatalf("Failed to read image file: %v", err)
}
parts := []*genai.Part{
  genai.NewPartFromText("Tell me about this image"),
  {
        InlineData: &genai.Blob{
              MIMEType: "image/jpeg",
              Data:     imageBytes,
        },
  },
}
contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

#### קובצי וידאו או אודיו

אודיו ווידאו מומרים לטוקנים לפי התעריפים הקבועים הבאים:

- סרטון: 263 טוקנים לשנייה
- אודיו: 32 טוקנים לשנייה

אם מתקשרים אל `count_tokens` עם קלט של טקסט וסרטון או אודיו, הפונקציה מחזירה את מספר הטוקנים המשולב של הטקסט ושל קובץ הווידאו או האודיו *בקלט בלבד* (`total_tokens`). אפשר להתקשר אל הפונקציה הזו לפני שמתקשרים אל `generate_content` כדי לבדוק את גודל הבקשות. אפשר גם להפעיל את `count_tokens` על הטקסט ועל הקובץ בנפרד.

אפשרות נוספת היא להפעיל את `generate_content` ואז להשתמש במאפיין `usage_metadata` באובייקט `response` כדי לקבל את הפרטים הבאים:

- מספר הטוקנים הנפרד של הקלט (`prompt_token_count`), התוכן שנשמר במטמון (`cached_content_token_count`) והפלט (`candidates_token_count`)
- מספר הטוקנים של תהליך החשיבה (`thoughts_token_count`)
- המספר הכולל של הטוקנים *בקלט ובפלט* (`total_token_count`).

### Python

```
from google import genai
import time

client = genai.Client()
prompt = "Tell me about this video"
your_file = client.files.upload(file=media / "Big_Buck_Bunny.mp4")

while not your_file.state or your_file.state.name != "ACTIVE":
    print("Processing video...")
    print("File state:", your_file.state)
    time.sleep(5)
    your_file = client.files.get(name=your_file.name)

print(
    client.models.count_tokens(
        model="gemini-3.8-flash", contents=[prompt, your_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[prompt, your_file]
)
print(response.usage_metadata)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});
const prompt = "Tell me about this video";

async function main() {
  let videoFile = await ai.files.upload({
    file: path.join(media, "Big_Buck_Bunny.mp4"),
    config: { mimeType: "video/mp4" },
  });

  while (!videoFile.state || videoFile.state.toString() !== "ACTIVE") {
    console.log("Processing video...");
    console.log("File state: ", videoFile.state);
    await sleep(5000);
    videoFile = await ai.files.get({ name: videoFile.name });
  }

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(videoFile.uri, videoFile.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(videoFile.uri, videoFile.mimeType),
    ]),
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

file, err := client.Files.UploadFromPath(
  ctx,
  filepath.Join(getMedia(), "Big_Buck_Bunny.mp4"),
  &genai.UploadFileConfig{
    MIMEType : "video/mp4",
  },
)
if err != nil {
  log.Fatal(err)
}

for file.State == genai.FileStateUnspecified || file.State != genai.FileStateActive {
  fmt.Println("Processing video...")
  fmt.Println("File state:", file.State)
  time.Sleep(5 * time.Second)

  file, err = client.Files.Get(ctx, file.Name, nil)
  if err != nil {
    log.Fatal(err)
  }
}

parts := []*genai.Part{
  genai.NewPartFromText("Tell me about this video"),
  genai.NewPartFromURI(file.URI, file.MIMEType),
}
contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal video/audio token count:", tokenResp.TotalTokens)
response, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

#### שימוש באסימוני וידאו לפי מצב עיבוד

השימוש באסימונים עבור סרטון תלוי במצב העיבוד:

| **מצב עיבוד** | **חישוב טוקנים** | **שימוש אופייני** |
| --- | --- | --- |
| ‫**Static** (ברירת מחדל) | כ-100 טוקנים לשנייה כברירת מחדל (רזולוציה נמוכה) או כ-300 טוקנים לשנייה (רזולוציה גבוהה). כל הפריימים נדגמים בקצב של פריים אחד לשנייה. | צפוי, ביחס למשך נכס הווידאו. |
| **Agentic** | משתנה בהתאם למורכבות התוכן. המודל טוען רק את התמליל ו/או הפריימים ו/או האודיו שנדרשים כדי לענות על ההנחיה. | עד 88% פחות טוקנים לתוכן ארוך. |

עם עיבוד מבוסס-סוכן, הרצאה של שעה שמשתמשת ב-1.08 מיליון טוקנים במצב סטטי, יכולה להשתמש ב-108,000 טוקנים, בהתאם להנחיה ולתוכן.

כדי לבדוק את השימוש בפועל בטוקנים לבקשה, משתמשים בשדה `usage_metadata` בתשובה. בשנת `UsageMetadata`, נתוני השימוש באסימונים של סרטונים עם AI אקטיבי מדווחים בשדות הבאים:

- **הנחיה ראשונית** (סרטון לדוגמה + הנחיית משתמש): `prompt_token_count`
- **ניווט**: `thoughts_token_count`
- **תמליל, פריימים ואודיו נטענים לפי דרישה**: `tool_use_prompt_token_count`
- **תשובה סופית**: `candidates_token_count`

### ספירת טוקנים של חשיבה

כשמפעילים את מצב החשיבה, התמחור של התשובה הוא הסכום של טוקנים של פלט וטוקנים של חשיבה. אפשר לאחזר את המספר הכולל של טוקנים של חשיבה שנוצרו מהשדה `thoughtsTokenCount` (או מהשדה המקביל ב-SDK).

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

המודלים החושבים יוצרים מחשבות מלאות כדי לשפר את איכות התשובה הסופית, ואז מפיקים [סיכומים](https://ai.google.dev/gemini-api/docs/thinking?hl=he#summaries) שנותנים תובנות לגבי תהליך החשיבה. לכן, התמחור של ה-API מבוסס על האסימונים המלאים של המחשבה שהמודל יוצר כדי ליצור סיכום, למרות שה-API מוציא רק את הסיכום.

במדריך [Gemini thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=he) תוכלו לקבל מידע נוסף על הגדרת תהליך החשיבה.

## חלונות הקשר

המודלים שזמינים דרך Gemini API כוללים חלונות הקשר שנמדדים בטוקנים. חלון ההקשר מגדיר את כמות הקלט שאפשר לספק ואת כמות הפלט שהמודל יכול ליצור. כדי לקבוע את הגודל של חלון ההקשר, אתם יכולים להפעיל את נקודת הקצה [`models.get`](https://ai.google.dev/api/rest/v1/models/get?hl=he) או לעיין ב[מסמכי התיעוד של המודלים](https://ai.google.dev/gemini-api/docs/models?hl=he).

- **מודלים של Gemini 4‏ (`gemini-4-argon`):** חולקים חלון הקשר יחיד של מיליון טוקנים (`1,048,576` טוקנים) בין טוקנים של קלט, חשיבה ופלט. בקשות בודדות מוגבלות ל-`65,536` טוקנים של פלט לסטרימינג (`streamGenerateContent`) ול-`32,768` טוקנים של פלט ללא סטרימינג (`generateContent`). אפשר גם ליצור עד `1,048,576` טוקנים באמצעות [פענוח ארוך](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=he). אם טוקני הקלט שלכם בתוספת `max_output_tokens` חורגים מ-1,048,576 טוקנים, ה-API מגביל באופן אוטומטי את מגבלת הפלט למקום שנותר בחלון ההקשר (`1,048,576` פחות טוקני הקלט שלכם).
- **מודלים של Gemini 3 ו-Gemini 2.5:** משתמשים בתקציבים נפרדים לקלט (`1,048,576` טוקנים) ולפלט (`65,536` טוקנים).

### Python

```
from google import genai

client = genai.Client()
model_info = client.models.get(model="gemini-3.8-flash")
print(f"{model_info.input_token_limit=}")
print(f"{model_info.output_token_limit=}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  const modelInfo = await ai.models.get({model: 'gemini-3.8-flash'});
  console.log(modelInfo.inputTokenLimit);
  console.log(modelInfo.outputTokenLimit);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
  log.Fatal(err)
}
modelInfo, err := client.ModelInfo(ctx, "models/gemini-3.8-flash")
if err != nil {
  log.Fatal(err)
}
fmt.Println("input token limit:", modelInfo.InputTokenLimit)
fmt.Println("output token limit:", modelInfo.OutputTokenLimit)
```

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-10-13 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-10-13 (שעון UTC)."],[],[]]
