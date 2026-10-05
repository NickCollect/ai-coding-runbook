---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=vi
fetched_at: 2026-10-05T06:51:01.331664+00:00
title: "T\u00ecm hi\u1ec3u v\u00e0 t\u00ednh m\u00e3 th\u00f4ng b\u00e1o \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs/generate-content?hl=vi)

Gửi ý kiến phản hồi

# Tìm hiểu và tính mã thông báo

Gemini và các mô hình AI tạo sinh khác xử lý dữ liệu đầu vào và đầu ra ở mức độ chi tiết được gọi là *mã thông báo*.

**Đối với các mô hình Gemini, một mã thông báo tương đương với khoảng 4 ký tự.
100 mã thông báo tương đương với khoảng 60 – 80 từ tiếng Anh.**

## Giới thiệu về mã thông báo

Mã thông báo có thể là các ký tự đơn như `z` hoặc toàn bộ từ như `cat`. Các từ dài được chia thành nhiều mã thông báo. Tập hợp tất cả mã thông báo mà mô hình sử dụng được gọi là từ vựng và quá trình chia văn bản thành mã thông báo được gọi là *phân tách thành mã thông báo*.

Khi tính năng thanh toán được bật, [chi phí của một lệnh gọi đến Gemini API](https://ai.google.dev/pricing?hl=vi) được
xác định một phần dựa trên số lượng mã thông báo đầu vào và đầu ra. Vì vậy, việc biết cách
đếm mã thông báo có thể hữu ích.

Bạn có thể thử đếm mã thông báo trong Colab của chúng tôi.

|  |  |  |
| --- | --- | --- |
| [Xem trên ai.google.dev](https://ai.google.dev/gemini-api/docs/tokens?hl=vi) | [Dùng thử sổ tay Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=vi) | [Xem sổ tay trên GitHub](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=vi) |

## Đếm mã thông báo

Tất cả dữ liệu đầu vào và đầu ra từ Gemini API đều được phân tách thành mã thông báo, bao gồm văn bản, tệp hình ảnh và các phương thức không phải văn bản khác.

Bạn có thể đếm mã thông báo theo những cách sau:

- **Gọi [`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=vi) bằng dữ liệu đầu vào
  của yêu cầu.**  
   Hàm này chỉ trả về tổng số mã thông báo trong *dữ liệu đầu vào*. Bạn có thể thực hiện lệnh gọi này trước khi gửi dữ liệu đầu vào đến mô hình để kiểm tra kích thước của yêu cầu.
- **Sử dụng thuộc tính `usage_metadata` trên đối tượng `response` sau khi
  gọi `generate_content`.**  
   Hàm này trả về tổng số
  mã thông báo trong *cả dữ liệu đầu vào và đầu ra*: `total_token_count`.  
   Hàm này cũng trả về số lượng mã thông báo của dữ liệu đầu vào và đầu ra riêng biệt: `prompt_token_count` (mã thông báo đầu vào) và `candidates_token_count` (mã thông báo đầu ra).

  Nếu bạn đang sử dụng mô hình [tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi), thì các mã thông báo được dùng trong quá trình tư duy
  sẽ được trả về trong `thoughts_token_count`. Và nếu bạn đang sử dụng
  [tính năng lưu vào bộ nhớ đệm theo Ngữ cảnh](https://ai.google.dev/gemini-api/docs/caching?hl=vi), thì số lượng mã thông báo được lưu vào bộ nhớ đệm sẽ nằm trong `cached_content_token_count`.

### Đếm mã thông báo văn bản

Nếu bạn gọi `count_tokens` bằng dữ liệu đầu vào chỉ có văn bản, thì hàm này sẽ trả về số lượng mã thông báo của văn bản trong *dữ liệu đầu vào* (`total_tokens`). Bạn có thể thực hiện lệnh gọi này trước khi gọi `generate_content` để kiểm tra kích thước của yêu cầu.

Một lựa chọn khác là gọi `generate_content`, sau đó sử dụng thuộc tính `usage_metadata` trên đối tượng `response` để nhận các giá trị sau:

- Số lượng mã thông báo riêng biệt của dữ liệu đầu vào (`prompt_token_count`), nội dung được lưu vào bộ nhớ đệm (`cached_content_token_count`) và dữ liệu đầu ra (`candidates_token_count`)
- Số lượng mã thông báo cho quá trình tư duy (`thoughts_token_count`)
- Tổng số mã thông báo trong *cả dữ liệu đầu vào và đầu ra* (`total_token_count`)

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

### Đếm mã thông báo nhiều lượt (trò chuyện)

Nếu bạn gọi `count_tokens` bằng nhật ký trò chuyện, thì hàm này sẽ trả về tổng số mã thông báo của văn bản từ từng vai trò trong cuộc trò chuyện (`total_tokens`).

Một lựa chọn khác là gọi `send_message`, sau đó sử dụng thuộc tính `usage_metadata` trên đối tượng `response` để nhận các giá trị sau:

- Số lượng mã thông báo riêng biệt của dữ liệu đầu vào (`prompt_token_count`), nội dung được lưu vào bộ nhớ đệm (`cached_content_token_count`) và dữ liệu đầu ra (`candidates_token_count`)
- Số lượng mã thông báo cho quá trình tư duy (`thoughts_token_count`)
- Tổng số mã thông báo trong *cả dữ liệu đầu vào và đầu ra* (`total_token_count`)

Để biết lượt trò chuyện tiếp theo của bạn sẽ có kích thước bao nhiêu, bạn cần thêm lượt trò chuyện đó vào nhật ký khi gọi `count_tokens`.

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

### Đếm mã thông báo đa phương thức

Tất cả dữ liệu đầu vào cho Gemini API đều được phân tách thành mã thông báo, bao gồm văn bản, tệp hình ảnh và các phương thức không phải văn bản khác. Hãy lưu ý những điểm chính cấp cao sau đây về việc phân tách thành mã thông báo của dữ liệu đầu vào đa phương thức trong quá trình xử lý bằng Gemini API:

- Dữ liệu đầu vào hình ảnh có cả hai kích thước <= 384 pixel được tính là 258 mã thông báo. Hình ảnh có một hoặc cả hai kích thước lớn hơn sẽ được cắt và điều chỉnh tỷ lệ khi cần thành các ô 768x768 pixel, mỗi ô được tính là 258 mã thông báo.
- Tệp video và âm thanh được chuyển đổi thành mã thông báo theo các tỷ lệ cố định sau: video ở mức 263 mã thông báo mỗi giây và âm thanh ở mức 32 mã thông báo mỗi giây.

#### Độ phân giải của nội dung nghe nhìn

[Các mô hình Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-3) giới thiệu khả năng kiểm soát chi tiết đối với
quá trình xử lý hình ảnh đa phương thức bằng tham số `media_resolution`. Tham số `media_resolution` xác định **số lượng mã thông báo tối đa được phân bổ cho mỗi hình ảnh đầu vào hoặc khung video.**
Độ phân giải cao hơn giúp cải thiện khả năng đọc văn bản chi tiết hoặc xác định các chi tiết nhỏ của mô hình, nhưng làm tăng mức sử dụng mã thông báo và độ trễ.

Để biết thêm thông tin chi tiết về tham số này và cách tham số này có thể ảnh hưởng đến việc tính toán mã thông báo,
hãy xem hướng dẫn về [độ phân giải của nội dung nghe nhìn](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=vi).

#### Tệp hình ảnh

Nếu bạn gọi `count_tokens` bằng dữ liệu đầu vào văn bản và hình ảnh, thì hàm này sẽ trả về số lượng mã thông báo kết hợp của văn bản và hình ảnh trong *dữ liệu đầu vào* (`total_tokens`). Bạn có thể thực hiện lệnh gọi này trước khi gọi `generate_content` để kiểm tra kích thước của yêu cầu. Bạn cũng có thể tuỳ ý gọi `count_tokens` trên văn bản và tệp riêng biệt.

Một lựa chọn khác là gọi `generate_content`, sau đó sử dụng thuộc tính `usage_metadata` trên đối tượng `response` để nhận các giá trị sau:

- Số lượng mã thông báo riêng biệt của dữ liệu đầu vào (`prompt_token_count`), nội dung được lưu vào bộ nhớ đệm (`cached_content_token_count`) và dữ liệu đầu ra (`candidates_token_count`)
- Số lượng mã thông báo cho quá trình tư duy (`thoughts_token_count`)
- Tổng số mã thông báo trong *cả dữ liệu đầu vào và đầu ra* (`total_token_count`)

Ví dụ sử dụng hình ảnh đã tải lên từ File API:

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

Ví dụ cung cấp hình ảnh dưới dạng dữ liệu nội tuyến:

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

#### Tệp video hoặc âm thanh

Âm thanh và video được chuyển đổi thành mã thông báo theo các tỷ lệ cố định sau:

- Video: 263 mã thông báo mỗi giây
- Âm thanh: 32 mã thông báo mỗi giây

Nếu bạn gọi `count_tokens` bằng dữ liệu đầu vào văn bản và video/âm thanh, thì hàm này sẽ trả về số lượng mã thông báo kết hợp của văn bản và tệp video/âm thanh trong *dữ liệu đầu vào* (`total_tokens`). Bạn có thể thực hiện lệnh gọi này trước khi gọi `generate_content` để kiểm tra kích thước của yêu cầu. Bạn cũng có thể tuỳ ý gọi `count_tokens` trên văn bản và tệp riêng biệt.

Một lựa chọn khác là gọi `generate_content`, sau đó sử dụng thuộc tính `usage_metadata` trên đối tượng `response` để nhận các giá trị sau:

- Số lượng mã thông báo riêng biệt của dữ liệu đầu vào (`prompt_token_count`), nội dung được lưu vào bộ nhớ đệm (`cached_content_token_count`) và dữ liệu đầu ra (`candidates_token_count`)
- Số lượng mã thông báo cho quá trình tư duy (`thoughts_token_count`)
- Tổng số mã thông báo trong *cả dữ liệu đầu vào và đầu ra* (`total_token_count`).

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

### Đếm mã thông báo tư duy

Khi bạn bật tính năng tư duy, giá phản hồi là tổng số mã thông báo đầu ra và mã thông báo tư duy. Bạn có thể truy xuất tổng số mã thông báo tư duy đã tạo từ trường `thoughtsTokenCount` (hoặc SDK tương đương).

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

Các mô hình tư duy tạo ra toàn bộ ý tưởng để cải thiện chất lượng của phản hồi cuối cùng, sau đó đưa ra [bản tóm tắt](https://ai.google.dev/gemini-api/docs/thinking?hl=vi#summaries) để cung cấp thông tin chi tiết về quá trình tư duy. Vì vậy, API định giá dựa trên toàn bộ mã thông báo tư duy mà mô hình tạo ra để tạo bản tóm tắt, mặc dù API chỉ đưa ra bản tóm tắt.

Bạn có thể tìm hiểu thêm về cách định cấu hình tính năng tư duy trong hướng dẫn về tính năng tư duy của [Gemini](https://ai.google.dev/gemini-api/docs/thinking?hl=vi).

## Cửa sổ ngữ cảnh

Các mô hình có sẵn thông qua Gemini API có cửa sổ ngữ cảnh được đo bằng mã thông báo. Cửa sổ ngữ cảnh xác định lượng dữ liệu đầu vào mà bạn có thể cung cấp và lượng dữ liệu đầu ra mà mô hình có thể tạo. Bạn có thể xác định kích thước của
cửa sổ ngữ cảnh bằng cách gọi điểm cuối [`models.get`](https://ai.google.dev/api/rest/v1/models/get?hl=vi)
hoặc bằng cách xem [tài liệu về mô hình](https://ai.google.dev/gemini-api/docs/models?hl=vi).

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

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-09-12 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-09-12 UTC."],[],[]]
