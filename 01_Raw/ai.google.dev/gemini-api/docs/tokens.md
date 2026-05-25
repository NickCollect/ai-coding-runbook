---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=ja
fetched_at: 2026-05-25T05:20:26.288232+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# トークンを理解してカウントする

Gemini などの生成 AI モデルは、入力と出力をトークンという粒度で処理します。

**Gemini モデルの場合、1 個のトークンは約 4 文字に相当します。100 個のトークンは、約 60 ～ 80 ワード（英語）に相当します。**

## トークンについて

トークンは、`z` などの単一の文字、`cat` などの単語全体にすることができます。長い単語は複数のトークンに分割されます。モデルで使用されるすべてのトークンのセットを語彙と呼び、テキストをトークンに分割するプロセスをトークン化と呼びます。

課金が有効になっている場合、[Gemini API の呼び出し費用](https://ai.google.dev/pricing?hl=ja)は入力トークンと出力トークンの数によって決まるため、トークンのカウント方法を知っておくと便利です。

Colab でトークン数を試すことができます。

|  |  |  |
| --- | --- | --- |
| [ai.google.dev で表示](https://ai.google.dev/gemini-api/docs/tokens?hl=ja) | [Colab ノートブックを試す](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=ja) | [GitHub でノートブックを表示](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=ja) |

## トークンのカウント

Gemini API へのすべての入力と Gemini API からのすべての出力は、テキスト、画像ファイル、テキスト以外のモダリティを含めてトークン化されます。

トークンは次の方法でカウントできます。

- **リクエストの入力を使用して [`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=ja) を呼び出します。**  
  : *入力のみ*のトークンの合計数を返します。この呼び出しは、リクエストのサイズを確認するために、入力をモデルに送信する前に行うことができます。
- **`generate_content` を呼び出した後、`response` オブジェクトの `usage_metadata` 属性を使用します。**  
  : *入力と出力の両方*のトークンの合計数 `total_token_count` を返します。  
   また、入力トークンと出力トークンの数を別々に返します。`prompt_token_count`（入力トークン）と `candidates_token_count`（出力トークン）。

  [思考モデル](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)を使用している場合、思考プロセスで使用されたトークンは `thoughts_token_count` で返されます。[コンテキスト キャッシュ保存](https://ai.google.dev/gemini-api/docs/caching?hl=ja)を使用している場合、キャッシュに保存されているトークンの数は `cached_content_token_count` になります。

### テキスト トークンをカウントする

テキストのみの入力で `count_tokens` を呼び出すと、*入力のみ*のテキストのトークン数（`total_tokens`）が返されます。この呼び出しは、`generate_content` を呼び出してリクエストのサイズを確認する前に行うことができます。

別の方法としては、`generate_content` を呼び出し、`response` オブジェクトの `usage_metadata` 属性を使用して次の情報を取得します。

- 入力（`prompt_token_count`）、キャッシュに保存されたコンテンツ（`cached_content_token_count`）、出力（`candidates_token_count`）のトークン数の内訳
- 思考プロセスのトークン数（`thoughts_token_count`）
- *入力と出力の両方*のトークンの合計数（`total_token_count`）

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

### Go

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

### マルチターン（チャット）トークンをカウントする

チャット履歴を指定して `count_tokens` を呼び出すと、チャット内の各ロールのテキストの合計トークン数（`total_tokens`）が返されます。

別の方法としては、`send_message` を呼び出し、`response` オブジェクトの `usage_metadata` 属性を使用して次の情報を取得します。

- 入力（`prompt_token_count`）、キャッシュに保存されたコンテンツ（`cached_content_token_count`）、出力（`candidates_token_count`）のトークン数の内訳
- 思考プロセスのトークン数（`thoughts_token_count`）
- *入力と出力の両方*のトークンの合計数（`total_token_count`）

次の会話のターンがどの程度の大きさになるかを把握するには、`count_tokens` を呼び出すときに、会話のターンを履歴に追加する必要があります。

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

### Go

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

### マルチモーダル トークンをカウントする

Gemini API への入力はすべてトークン化されます。これには、テキスト、画像ファイル、その他のテキスト以外のモダリティが含まれます。Gemini API による処理中のマルチモーダル入力のトークン化に関する重要なポイントは次のとおりです。

- 両方の寸法が 384 ピクセル以下の画像入力は、258 個のトークンとしてカウントされます。1 つまたは両方の寸法が大きい画像は、必要に応じて 768x768 ピクセルのタイルに切り抜かれ、スケーリングされます。各タイルは 258 個のトークンとしてカウントされます。
- 動画ファイルと音声ファイルは、次の固定レートでトークンに変換されます。動画は 1 秒あたり 263 トークン、音声は 1 秒あたり 32 トークン。

#### メディアの解像度

[Gemini 3 モデル](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-3)では、`media_resolution` パラメータを使用して、マルチモーダル ビジョン処理をきめ細かく制御できます。`media_resolution` パラメータは、**入力画像または動画フレームごとに割り当てられるトークンの最大数**を決定します。解像度が高いほど、モデルが細かいテキストを読み取ったり、小さな詳細を識別する能力が向上しますが、トークンの使用量とレイテンシが増加します。

パラメータとそのトークン計算への影響について詳しくは、[メディアの解像度](https://ai.google.dev/gemini-api/docs/media-resolution?hl=ja)ガイドをご覧ください。

#### 画像ファイル

テキストと画像の入力を使用して `count_tokens` を呼び出すと、*入力のみ*のテキストと画像のトークン数の合計（`total_tokens`）が返されます。この呼び出しは、`generate_content` を呼び出す前にリクエストのサイズを確認するために行うことができます。必要に応じて、テキストとファイルに対して `count_tokens` を個別に呼び出すこともできます。

別の方法としては、`generate_content` を呼び出し、`response` オブジェクトの `usage_metadata` 属性を使用して次の情報を取得します。

- 入力（`prompt_token_count`）、キャッシュに保存されたコンテンツ（`cached_content_token_count`）、出力（`candidates_token_count`）のトークン数の内訳
- 思考プロセスのトークン数（`thoughts_token_count`）
- *入力と出力の両方*のトークンの合計数（`total_token_count`）

File API からアップロードされた画像を使用する例:

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

画像をインライン データとして提供する例:

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

#### 動画ファイルまたは音声ファイル

音声と動画は、次の固定レートでトークンに変換されます。

- 動画: 1 秒あたり 263 トークン
- 音声: 1 秒あたり 32 トークン

テキストと動画/音声の入力を使用して `count_tokens` を呼び出すと、テキストと動画/音声ファイルの結合されたトークン数が*入力のみ*で返されます（`total_tokens`）。この呼び出しは、`generate_content` を呼び出してリクエストのサイズを確認する前に行うことができます。必要に応じて、テキストとファイルに対して個別に `count_tokens` を呼び出すこともできます。

別の方法としては、`generate_content` を呼び出し、`response` オブジェクトの `usage_metadata` 属性を使用して次の情報を取得します。

- 入力（`prompt_token_count`）、キャッシュに保存されたコンテンツ（`cached_content_token_count`）、出力（`candidates_token_count`）のトークン数の内訳
- 思考プロセスのトークン数（`thoughts_token_count`）
- *入力と出力の両方*のトークンの合計数（`total_token_count`）。

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

## コンテキスト ウィンドウ

Gemini API で使用可能なモデルには、トークンで測定されるコンテキスト ウィンドウがあります。コンテキスト ウィンドウは、提供できる入力の量と、モデルが生成できる出力の量を定義します。コンテキスト ウィンドウのサイズは、[`models.get` エンドポイント](https://ai.google.dev/api/rest/v1/models/get?hl=ja)を呼び出すか、[モデルのドキュメント](https://ai.google.dev/gemini-api/docs/models?hl=ja)で確認できます。

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

### Go

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

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-05-19 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-05-19 UTC。"],[],[]]
