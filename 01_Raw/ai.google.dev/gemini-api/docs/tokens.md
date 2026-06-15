---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=hi
fetched_at: 2026-06-15T06:22:42.440490+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# टोकन को समझना और उनकी गिनती करना

Gemini और जनरेटिव एआई के अन्य मॉडल, इनपुट और आउटपुट को *टोकन* नाम की ग्रैनुलैरिटी पर प्रोसेस करते हैं.

**Gemini मॉडल के लिए, एक टोकन करीब चार वर्णों के बराबर होता है.
100 टोकन, अंग्रेज़ी के करीब 60 से 80 शब्दों के बराबर होते हैं.**

## टोकन के बारे में जानकारी

टोकन, `z` जैसे सिंगल वर्ण या `cat` जैसे पूरे शब्द हो सकते हैं. लंबे शब्दों को कई टोकन में बांटा जाता है. मॉडल के इस्तेमाल किए जाने वाले सभी टोकन के सेट को शब्दावली कहा जाता है. साथ ही, टेक्स्ट को टोकन में बांटने की प्रोसेस को *टोकनाइज़ेशन* कहा जाता है.

बिलिंग की सुविधा चालू होने पर, [Gemini API को कॉल करने की लागत](https://ai.google.dev/pricing?hl=hi) इनपुट और आउटपुट टोकन की संख्या के हिसाब से तय की जाती है. इसलिए, टोकन की गिनती करने का तरीका जानना मददगार साबित हो सकता है.

हमारे Colab में, टोकन की गिनती करने की सुविधा आज़माई जा सकती है.

|  |  |  |
| --- | --- | --- |
| [ai.google.dev पर देखें](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) | [Colab notebook आज़माएं](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=hi) | [GitHub पर notebook देखें](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=hi) |

## टोकन की गिनती करना

Gemini API के सभी इनपुट और आउटपुट को टोकनाइज़ किया जाता है. इनमें टेक्स्ट, इमेज फ़ाइलें, और टेक्स्ट के अलावा अन्य फ़ॉर्मैट शामिल हैं.

टोकन की गिनती इन तरीकों से की जा सकती है:

- **अनुरोध के इनपुट
  के साथ [`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=hi) को कॉल करें.**  
   इससे, *सिर्फ़ इनपुट* में मौजूद टोकन की कुल संख्या मिलती है. अनुरोधों का साइज़ देखने के लिए, मॉडल को इनपुट भेजने से पहले यह कॉल किया जा सकता है.
- **`generate_content` को कॉल करने के बाद, `response` ऑब्जेक्ट पर मौजूद `usage_metadata` एट्रिब्यूट का इस्तेमाल करें.**  
   इससे, *इनपुट और आउटपुट*, दोनों में मौजूद टोकन की कुल संख्या मिलती है: `total_token_count`.  
   इससे, इनपुट और आउटपुट के टोकन की संख्या अलग-अलग भी मिलती है: `prompt_token_count` (इनपुट टोकन) और `candidates_token_count` (आउटपुट टोकन).

  अगर किसी ऐसे मॉडल का इस्तेमाल किया जा रहा है जो [सोच-समझकर
  जवाब](https://ai.google.dev/gemini-api/docs/thinking?hl=hi) देता है, तो सोचने की
  प्रोसेस के दौरान इस्तेमाल किए गए टोकन, `thoughts_token_count` में दिखते हैं. साथ ही, अगर
  [कॉन्टेक्स्ट कैशिंग](https://ai.google.dev/gemini-api/docs/caching?hl=hi) का इस्तेमाल किया जा रहा है, तो कैश मेमोरी में सेव किए गए टोकन
  की संख्या, `cached_content_token_count` में दिखेगी.

### टेक्स्ट टोकन की गिनती करना

अगर सिर्फ़ टेक्स्ट वाले इनपुट के साथ `count_tokens` को कॉल किया जाता है, तो इससे *सिर्फ़ इनपुट* में मौजूद टेक्स्ट के टोकन की संख्या (`total_tokens`) मिलती है. अनुरोधों का साइज़ देखने के लिए, `generate_content` को कॉल करने से पहले यह कॉल किया जा सकता है.

`generate_content` को कॉल करने और फिर `response` ऑब्जेक्ट पर मौजूद `usage_metadata` एट्रिब्यूट का इस्तेमाल करके, ये जानकारी भी पाई जा सकती है:

- इनपुट (`prompt_token_count`), कैश मेमोरी में सेव किए गए कॉन्टेंट (`cached_content_token_count`), और आउटपुट (`candidates_token_count`) के टोकन की संख्या
- सोचने की प्रोसेस के लिए टोकन की संख्या (`thoughts_token_count`)
- *इनपुट और आउटपुट* , दोनों में मौजूद टोकन की कुल संख्या (`total_token_count`)

### Python

```
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash", contents=prompt
)
print("total_tokens: ", total_tokens)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=prompt
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
    model: "gemini-3.5-flash",
    contents: prompt,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: prompt,
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### ऐप पर जाएं

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

// Convert prompt to a slice of *genai.Content using the helper.
contents := []*genai.Content{
  genai.NewContentFromText(prompt, genai.RoleUser),
}
countResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  return err
}
fmt.Println("total_tokens:", countResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", contents, nil)
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

### मल्टी-टर्न (चैट) टोकन की गिनती करना

अगर चैट के इतिहास के साथ `count_tokens` को कॉल किया जाता है, तो इससे चैट में हर रोल के टेक्स्ट के टोकन की कुल संख्या (`total_tokens`) मिलती है.

`send_message` को कॉल करने और फिर `response` ऑब्जेक्ट पर मौजूद `usage_metadata` एट्रिब्यूट का इस्तेमाल करके, ये जानकारी भी पाई जा सकती है:

- इनपुट (`prompt_token_count`), कैश मेमोरी में सेव किए गए कॉन्टेंट (`cached_content_token_count`), और आउटपुट (`candidates_token_count`) के टोकन की संख्या
- सोचने की प्रोसेस के लिए टोकन की संख्या (`thoughts_token_count`)
- *इनपुट और आउटपुट* , दोनों में मौजूद टोकन की कुल संख्या (`total_token_count`)

बातचीत के अगले टर्न का साइज़ समझने के लिए, `count_tokens` को कॉल करते समय, आपको इसे इतिहास में जोड़ना होगा.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.5-flash",
    history=[
        types.Content(
            role="user", parts=[types.Part(text="Hi my name is Bob")]
        ),
        types.Content(role="model", parts=[types.Part(text="Hi Bob!")]),
    ],
)

print(
    client.models.count_tokens(
        model="gemini-3.5-flash", contents=chat.get_history()
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
print(client.models.count_tokens(model="gemini-3.5-flash", contents=history))
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
    model: "gemini-3.5-flash",
    history: history,
  });

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
    contents: combinedHistory,
  });
  console.log(
    "Combined history token count:",
    combinedCountTokensResponse.totalTokens,
  );
}

await main();
```

### ऐप पर जाएं

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

history := []*genai.Content{
  {Role: genai.RoleUser, Parts: []*genai.Part({Text: "Hi my name is Bob"})},
  {Role: genai.RoleModel, Parts: []*genai.Part({Text: "Hi Bob!"})},
}
chat, err := client.Chats.Create(ctx, "gemini-3.5-flash", nil, history)
if err != nil {
  log.Fatal(err)
}

firstTokenResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", chat.History(false), nil)
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

secondTokenResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", hist, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println(secondTokenResp.TotalTokens)
```

### मल्टीमॉडल टोकन की गिनती करना

Gemini API के सभी इनपुट को टोकनाइज़ किया जाता है. इनमें टेक्स्ट, इमेज फ़ाइलें, और टेक्स्ट के अलावा अन्य फ़ॉर्मैट शामिल हैं. Gemini API से प्रोसेस करने के दौरान, मल्टीमॉडल इनपुट के टोकनाइज़ेशन के बारे में ये मुख्य बातें ध्यान में रखें:

- दोनों डाइमेंशन में <=384 पिक्सल वाली इमेज इनपुट को 258 टोकन के तौर पर गिना जाता है. एक या दोनों डाइमेंशन में बड़ी इमेज को ज़रूरत के हिसाब से क्रॉप और स्केल करके, 768x768 पिक्सल की टाइल में बदला जाता है. हर टाइल को 258 टोकन के तौर पर गिना जाता है.
- वीडियो और ऑडियो फ़ाइलों को इन तय दरों पर टोकन में बदला जाता है: वीडियो के लिए 263 टोकन प्रति सेकंड और ऑडियो के लिए 32 टोकन प्रति सेकंड.

#### मीडिया रिज़ॉल्यूशन

[Gemini 3 मॉडल](https://ai.google.dev/gemini-api/docs/models?hl=hi#gemini-3) में,
मल्टीमॉडल विज़न प्रोसेसिंग पर ज़्यादा कंट्रोल मिलता है, `media_resolution` पैरामीटर की मदद से. `media_resolution` पैरामीटर, **हर इनपुट इमेज या वीडियो फ़्रेम के लिए, तय किए गए टोकन की ज़्यादा से ज़्यादा संख्या** तय करता है.
ज़्यादा रिज़ॉल्यूशन से, मॉडल को बारीक टेक्स्ट पढ़ने या छोटी-छोटी जानकारी की पहचान करने में मदद मिलती है. हालांकि, इससे टोकन का इस्तेमाल और इंतज़ार का समय बढ़ जाता है.

पैरामीटर और इससे टोकन की गिनती पर पड़ने वाले असर के बारे में ज़्यादा जानने के लिए,
[मीडिया रिज़ॉल्यूशन](https://ai.google.dev/gemini-api/docs/media-resolution?hl=hi) की गाइड देखें.

#### इमेज फ़ाइलें

अगर टेक्स्ट और इमेज वाले इनपुट के साथ `count_tokens` को कॉल किया जाता है, तो इससे *सिर्फ़ इनपुट* में मौजूद टेक्स्ट और इमेज के टोकन की कुल संख्या (`total_tokens`) मिलती है. अनुरोधों का साइज़ देखने के लिए, `generate_content` को कॉल करने से पहले यह कॉल किया जा सकता है. इसके अलावा, टेक्स्ट और फ़ाइल के लिए अलग-अलग `count_tokens` को कॉल किया जा सकता है.

`generate_content` को कॉल करने और फिर `response` ऑब्जेक्ट पर मौजूद `usage_metadata` एट्रिब्यूट का इस्तेमाल करके, ये जानकारी भी पाई जा सकती है:

- इनपुट (`prompt_token_count`), कैश मेमोरी में सेव किए गए कॉन्टेंट (`cached_content_token_count`), और आउटपुट (`candidates_token_count`) के टोकन की संख्या
- सोचने की प्रोसेस के लिए टोकन की संख्या (`thoughts_token_count`)
- *इनपुट और आउटपुट* , दोनों में मौजूद टोकन की कुल संख्या (`total_token_count`)

File API से अपलोड की गई इमेज का इस्तेमाल करने वाला उदाहरण:

### Python

```
from google import genai

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = client.files.upload(file=media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3.5-flash", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=[prompt, your_image_file]
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
    model: "gemini-3.5-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(organ.uri, organ.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(organ.uri, organ.mimeType),
    ]),
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### ऐप पर जाएं

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

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

इनलाइन डेटा के तौर पर इमेज उपलब्ध कराने वाला उदाहरण:

### Python

```
from google import genai
import PIL.Image

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = PIL.Image.open(media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3.5-flash", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=[prompt, your_image_file]
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
    model: "gemini-3.5-flash",
    contents: contents,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: contents,
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### ऐप पर जाएं

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

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

#### वीडियो या ऑडियो फ़ाइलें

ऑडियो और वीडियो, दोनों को इन तय दरों पर टोकन में बदला जाता है:

- वीडियो: 263 टोकन प्रति सेकंड
- ऑडियो: 32 टोकन प्रति सेकंड

अगर टेक्स्ट और वीडियो/ऑडियो वाले इनपुट के साथ `count_tokens` को कॉल किया जाता है, तो इससे *सिर्फ़ इनपुट* में मौजूद टेक्स्ट और वीडियो/ऑडियो फ़ाइल के टोकन की कुल संख्या (`total_tokens`) मिलती है. अनुरोधों का साइज़ देखने के लिए, `generate_content` को कॉल करने से पहले यह कॉल किया जा सकता है. इसके अलावा, टेक्स्ट और फ़ाइल के लिए अलग-अलग `count_tokens` को कॉल किया जा सकता है.

`generate_content` को कॉल करने और फिर `response` ऑब्जेक्ट पर मौजूद `usage_metadata` एट्रिब्यूट का इस्तेमाल करके, ये जानकारी भी पाई जा सकती है:

- इनपुट (`prompt_token_count`), कैश मेमोरी में सेव किए गए कॉन्टेंट (`cached_content_token_count`), और आउटपुट (`candidates_token_count`) के टोकन की संख्या
- सोचने की प्रोसेस के लिए टोकन की संख्या (`thoughts_token_count`)
- *इनपुट और आउटपुट* , दोनों में मौजूद टोकन की कुल संख्या (`total_token_count`).

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
        model="gemini-3.5-flash", contents=[prompt, your_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=[prompt, your_file]
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
    model: "gemini-3.5-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(videoFile.uri, videoFile.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(videoFile.uri, videoFile.mimeType),
    ]),
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### ऐप पर जाएं

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

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal video/audio token count:", tokenResp.TotalTokens)
response, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

### सोच-समझकर जवाब देने वाले मॉडल के टोकन की गिनती करना

सोच-समझकर जवाब देने वाले मॉडल की सुविधा चालू करने पर, जवाब की कीमत, आउटपुट टोकन और सोच-समझकर जवाब देने वाले मॉडल के टोकन की कुल संख्या के बराबर होती है. जनरेट किए गए सोच-समझकर जवाब देने वाले मॉडल के टोकन की कुल संख्या, `thoughtsTokenCount` फ़ील्ड (या SDK के बराबर) से देखी जा सकती है.

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

### ऐप पर जाएं

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

सोच-समझकर जवाब देने वाले मॉडल, फ़ाइनल जवाब की क्वालिटी बेहतर बनाने के लिए, पूरी तरह से सोच-समझकर जवाब जनरेट करते हैं. इसके बाद, सोचने की प्रोसेस के बारे में जानकारी देने के लिए, [खास जानकारी](https://ai.google.dev/gemini-api/docs/thinking?hl=hi#summaries) आउटपुट करते हैं. इसलिए, API, कीमत तय करने के लिए, मॉडल के जनरेट किए गए सोच-समझकर जवाब देने वाले मॉडल के टोकन का इस्तेमाल करता है. भले ही, API सिर्फ़ खास जानकारी आउटपुट करता हो.

Gemini की सोच-समझकर जवाब देने वाले मॉडल की [गाइड](https://ai.google.dev/gemini-api/docs/thinking?hl=hi) में, सोच-समझकर जवाब देने वाले मॉडल को कॉन्फ़िगर करने के तरीके के बारे में ज़्यादा जानें.

## कॉन्टेक्स्ट विंडो

Gemini API के ज़रिए उपलब्ध मॉडल में, कॉन्टेक्स्ट विंडो होती हैं. इन्हें टोकन में मापा जाता है. कॉन्टेक्स्ट विंडो से यह तय होता है कि कितना इनपुट दिया जा सकता है और मॉडल कितना आउटपुट जनरेट कर सकता है. `[`models.get` एंडपॉइंट](https://ai.google.dev/api/rest/v1/models/get?hl=hi) को कॉल करके या [मॉडल के दस्तावेज़](https://ai.google.dev/gemini-api/docs/models?hl=hi) में देखकर, कॉन्टेक्स्ट विंडो का साइज़ तय किया जा सकता है.

### Python

```
from google import genai

client = genai.Client()
model_info = client.models.get(model="gemini-3.5-flash")
print(f"{model_info.input_token_limit=}")
print(f"{model_info.output_token_limit=}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  const modelInfo = await ai.models.get({model: 'gemini-3.5-flash'});
  console.log(modelInfo.inputTokenLimit);
  console.log(modelInfo.outputTokenLimit);
}

await main();
```

### ऐप पर जाएं

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
  log.Fatal(err)
}
modelInfo, err := client.ModelInfo(ctx, "models/gemini-3.5-flash")
if err != nil {
  log.Fatal(err)
}
fmt.Println("input token limit:", modelInfo.InputTokenLimit)
fmt.Println("output token limit:", modelInfo.OutputTokenLimit)
```

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-04 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-04 (UTC) को अपडेट किया गया."],[],[]]
