---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=tr
fetched_at: 2026-08-24T02:28:54.744165+00:00
title: "Jetonlar\u0131 anlama ve sayma \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Jetonları anlama ve sayma

Gemini ve diğer üretken yapay zeka modelleri, giriş ve çıkışı *token* adı verilen bir ayrıntı düzeyinde işler.

**Gemini modellerinde bir jeton yaklaşık 4 karaktere eşittir.
100 jeton yaklaşık 60-80 İngilizce kelimeye eşittir.**

## Jetonlar hakkında

Jetonlar, `z` gibi tek karakterler veya `cat` gibi tam kelimeler olabilir. Uzun kelimeler
birkaç jetona ayrılır. Model tarafından kullanılan tüm jetonlar kümesine kelime hazinesi, metni jetonlara bölme işlemine ise *jetonlaştırma* adı verilir.

Faturalandırma etkinleştirildiğinde [Gemini API'ye yapılan bir çağrının maliyeti](https://ai.google.dev/pricing?hl=tr) kısmen giriş ve çıkış jetonlarının sayısına göre belirlenir. Bu nedenle, jetonları nasıl sayacağınızı bilmek faydalı olabilir.

Colab'imizde jeton saymayı deneyebilirsiniz.

|  |  |  |
| --- | --- | --- |
| [ai.google.dev adresinde görüntüle](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) | [Colab not defterini deneyin](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=tr) | [Not defterini GitHub'da görüntüleyin](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=tr) |

## Parça sayma

Metin, resim dosyaları ve metin dışı diğer formatlar da dahil olmak üzere Gemini API'ye yapılan tüm girişler ve API'den alınan tüm çıkışlar jetonlaştırılır.

Jetonları aşağıdaki şekillerde sayabilirsiniz:

- **İsteğin girişiyle [`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=tr) işlevini çağırın.**  
   Bu işlev, *yalnızca giriş* bölümündeki toplam jeton sayısını döndürür. Bu aramayı, isteklerinizin boyutunu kontrol etmek için girişi modele göndermeden önce yapabilirsiniz.
- **`generate_content` işlevi çağrıldıktan sonra `response` nesnesinde `usage_metadata` özelliğini kullanın.**  
   Bu işlev, *hem girişte hem de çıkışta* toplam jeton sayısını döndürür: `total_token_count`.  
   Ayrıca giriş ve çıkışın jeton sayılarını ayrı ayrı döndürür: `prompt_token_count` (giriş jetonları) ve `candidates_token_count` (çıkış jetonları).

  [Düşünen modeli](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) kullanıyorsanız düşünme süreci sırasında kullanılan jetonlar `thoughts_token_count` içinde döndürülür. [Bağlamı önbelleğe alma](https://ai.google.dev/gemini-api/docs/caching?hl=tr) özelliğini kullanıyorsanız önbelleğe alınan jeton sayısı `cached_content_token_count` içinde gösterilir.

### Metin jetonlarını sayma

`count_tokens` işlevini yalnızca metin içeren bir girişle çağırırsanız *yalnızca girişteki* metnin jeton sayısını (`total_tokens`) döndürür. İsteklerinizin boyutunu kontrol etmek için `generate_content` işlevini çağırmadan önce bu çağrıyı yapabilirsiniz.

Diğer bir seçenek ise `generate_content` işlevini çağırmak ve ardından `usage_metadata` özelliğini `response` nesnesinde kullanarak aşağıdakileri elde etmektir:

- Giriş (`prompt_token_count`), önbelleğe alınmış içerik (`cached_content_token_count`) ve çıkışın (`candidates_token_count`) ayrı jeton sayıları
- Düşünme süreci için jeton sayısı (`thoughts_token_count`)
- *Hem girişte hem de çıkışta* toplam jeton sayısı (`total_token_count`)

### Python

```
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash", contents=prompt
)
print("total_tokens: ", total_tokens)

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=prompt
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
    model: "gemini-3.6-flash",
    contents: prompt,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.6-flash",
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
countResp, err := client.Models.CountTokens(ctx, "gemini-3.6-flash", contents, nil)
if err != nil {
  return err
}
fmt.Println("total_tokens:", countResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.6-flash", contents, nil)
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

### Çok aşamalı etkileşim (sohbet) jetonlarını sayma

Sohbet geçmişiyle birlikte `count_tokens` işlevini çağırırsanız sohbetteki her rolden gelen metnin toplam jeton sayısını (`total_tokens`) döndürür.

Diğer bir seçenek ise `send_message` işlevini çağırmak ve ardından `usage_metadata` özelliğini `response` nesnesinde kullanarak aşağıdakileri elde etmektir:

- Giriş (`prompt_token_count`), önbelleğe alınmış içerik (`cached_content_token_count`) ve çıkışın (`candidates_token_count`) ayrı jeton sayıları
- Düşünme süreci için jeton sayısı (`thoughts_token_count`)
- *Hem girişte hem de çıkışta* toplam jeton sayısı (`total_token_count`)

Bir sonraki etkileşiminizin ne kadar büyük olacağını anlamak için `count_tokens` işlevini çağırdığınızda bunu geçmişe eklemeniz gerekir.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.6-flash",
    history=[
        types.Content(
            role="user", parts=[types.Part(text="Hi my name is Bob")]
        ),
        types.Content(role="model", parts=[types.Part(text="Hi Bob!")]),
    ],
)

print(
    client.models.count_tokens(
        model="gemini-3.6-flash", contents=chat.get_history()
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
print(client.models.count_tokens(model="gemini-3.6-flash", contents=history))
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
    model: "gemini-3.6-flash",
    history: history,
  });

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
chat, err := client.Chats.Create(ctx, "gemini-3.6-flash", nil, history)
if err != nil {
  log.Fatal(err)
}

firstTokenResp, err := client.Models.CountTokens(ctx, "gemini-3.6-flash", chat.History(false), nil)
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

secondTokenResp, err := client.Models.CountTokens(ctx, "gemini-3.6-flash", hist, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println(secondTokenResp.TotalTokens)
```

### Çok formatlı jetonları sayma

Gemini API'ye yapılan tüm girişler (metin, resim dosyaları ve diğer metin dışı biçimler dahil) jetonlaştırılır. Gemini API tarafından işleme sırasında çok formatlı girişin jetonlaştırılmasıyla ilgili aşağıdaki üst düzey önemli noktaları unutmayın:

- Her iki boyutu da <=384 piksel olan resim girişleri 258 jeton olarak sayılır. Bir veya iki boyutta daha büyük olan resimler, gerektiğinde 768x768 piksellik parçalar halinde kırpılıp ölçeklendirilir ve her biri 258 jeton olarak sayılır.
- Video ve ses dosyaları, aşağıdaki sabit oranlarda jetonlara dönüştürülür:
  Video: Saniyede 263 jeton, ses: saniyede 32 jeton.

#### Medya çözünürlükleri

[Gemini 3 modelleri](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-3), `media_resolution` parametresiyle çok formatlı görüntü işleme üzerinde ayrıntılı kontrol sağlar. `media_resolution` parametresi, **giriş resim veya video karesi başına ayrılan maksimum jeton sayısını** belirler.
Daha yüksek çözünürlükler, modelin küçük metinleri okuma veya küçük ayrıntıları tanımlama becerisini artırır ancak jeton kullanımını ve gecikmeyi de artırır.

Parametre ve jeton hesaplamalarını nasıl etkileyebileceği hakkında daha fazla bilgi için [medya çözünürlüğü](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=tr) kılavuzuna bakın.

#### Resim dosyaları

`count_tokens` işlevini metin ve resim girişiyle çağırırsanız *yalnızca girişteki* (`total_tokens`) metin ve resmin birleştirilmiş jeton sayısını döndürür. İsteklerinizin boyutunu kontrol etmek için `generate_content` işlevini çağırmadan önce bu işlevi çağırabilirsiniz. İsteğe bağlı olarak metin ve dosya üzerinde ayrı ayrı `count_tokens` işlevini de çağırabilirsiniz.

Diğer bir seçenek ise `generate_content` işlevini çağırmak ve ardından `usage_metadata` özelliğini `response` nesnesinde kullanarak aşağıdakileri elde etmektir:

- Giriş (`prompt_token_count`), önbelleğe alınmış içerik (`cached_content_token_count`) ve çıkışın (`candidates_token_count`) ayrı jeton sayıları
- Düşünme süreci için jeton sayısı (`thoughts_token_count`)
- *Hem girişte hem de çıkışta* toplam jeton sayısı (`total_token_count`)

File API'den yüklenen bir görüntünün kullanıldığı örnek:

### Python

```
from google import genai

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = client.files.upload(file=media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3.6-flash", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=[prompt, your_image_file]
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
    model: "gemini-3.6-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(organ.uri, organ.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.6-flash",
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
  filepath.Join(getMedia(), "organ.jpg&q&uot;), 
  genai.UploadFileConfig{
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

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.6-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.6-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

Resmi satır içi veri olarak sağlayan örnek:

### Python

```
from google import genai
import PIL.Image

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = PIL.Image.open(media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3.6-flash", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=[prompt, your_image_file]
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
    model: "gemini-3.6-flash",
    contents: contents,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.6-flash",
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
  genai.NewPartFromText("Tell me about this image&qu&ot;),
  {
        InlineData: genai.Blob{
              MIMEType: "image/jpeg",
              Data:     imageBytes,
        },
  },
}
contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.6-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.6-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "&quot;, "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

#### Video veya ses dosyaları

Ses ve video, aşağıdaki sabit oranlarda jetonlara dönüştürülür:

- Video: Saniyede 263 jeton
- Ses: Saniyede 32 jeton

`count_tokens` işlevini metin ve video/ses girişiyle çağırırsanız *yalnızca girişteki* metin ve video/ses dosyasının birleştirilmiş jeton sayısını döndürür (`total_tokens`). İsteklerinizin boyutunu kontrol etmek için `generate_content` işlevini çağırmadan önce bu çağrıyı yapabilirsiniz. İsterseniz metni ve dosyayı ayrı ayrı `count_tokens` çağırabilirsiniz.

Diğer bir seçenek ise `generate_content` işlevini çağırmak ve ardından `usage_metadata` özelliğini `response` nesnesinde kullanarak aşağıdakileri elde etmektir:

- Giriş (`prompt_token_count`), önbelleğe alınmış içerik (`cached_content_token_count`) ve çıkışın (`candidates_token_count`) ayrı jeton sayıları
- Düşünme süreci için jeton sayısı (`thoughts_token_count`)
- *Hem girişte hem de çıkışta* toplam jeton sayısıdır (`total_token_count`).

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
        model="gemini-3.6-flash", contents=[prompt, your_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=[prompt, your_file]
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
    model: "gemini-3.6-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(videoFile.uri, videoFile.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.6-flash",
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
  filepath.Join(getMedia(), "Big_Buck_Bunny.mp4&&quot;),
  genai.UploadFileConfig{
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

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.6-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal video/audio token count:", tokenResp.TotalTokens)
response, err := client.Models.GenerateContent(ctx, "gemini-3.6-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

### Düşünce parçalarını sayma

Düşünme özelliğini etkinleştirdiğinizde yanıt fiyatı, çıkış jetonları ile düşünme jetonlarının toplamı olur. Oluşturulan düşünce jetonlarının toplam sayısını `thoughtsTokenCount` alanından (veya SDK eşdeğeri) alabilirsiniz.

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

Düşünme modelleri, nihai yanıtın kalitesini artırmak için tam düşünceler üretir ve ardından düşünce süreci hakkında bilgi vermek için [özetler](https://ai.google.dev/gemini-api/docs/thinking?hl=tr#summaries) oluşturur. Bu nedenle, API yalnızca özeti çıkış olarak verse de fiyatlandırma, modelin özet oluşturmak için ürettiği tüm düşünce jetonlarına göre yapılır.

Düşünme özelliğini nasıl yapılandıracağınız hakkında daha fazla bilgiyi [Gemini düşünme](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) kılavuzunda bulabilirsiniz.

## Bağlam pencereleri

Gemini API aracılığıyla kullanılabilen modellerin bağlam pencereleri jetonlarla ölçülür. Bağlam penceresi, ne kadar giriş sağlayabileceğinizi ve modelin ne kadar çıkış üretebileceğini tanımlar. Bağlam penceresinin boyutunu [`models.get` uç noktasını](https://ai.google.dev/api/rest/v1/models/get?hl=tr) çağırarak veya [modeller belgelerine](https://ai.google.dev/gemini-api/docs/models?hl=tr) bakarak belirleyebilirsiniz.

### Python

```
from google import genai

client = genai.Client()
model_info = client.models.get(model="gemini-3.6-flash")
print(f"{model_info.input_token_limit=}")
print(f"{model_info.output_token_limit=}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  const modelInfo = await ai.models.get({model: 'gemini-3.6-flash'});
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
modelInfo, err := client.ModelInfo(ctx, "models/gemini-3.6-flash")
if err != nil {
  log.Fatal(err)
}
fmt.Println("input token limit:", modelInfo.InputTokenLimit)
fmt.Println("output token limit:", modelInfo.OutputTokenLimit)
```

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-30 UTC."],[],[]]
