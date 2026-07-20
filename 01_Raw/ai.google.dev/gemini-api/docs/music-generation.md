---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=vi
fetched_at: 2026-07-20T04:39:45.696817+00:00
title: "T\u1ea1o nh\u1ea1c b\u1eb1ng Lyria 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tạo nhạc bằng Lyria 3

Lyria 3 là nhóm mô hình tạo nhạc của Google, có sẵn thông qua Gemini API. Với Lyria 3, bạn có thể tạo âm thanh nổi chất lượng cao ở tần số 44, 1 kHz từ câu lệnh bằng văn bản hoặc từ hình ảnh. Các mô hình này mang đến sự nhất quán về cấu trúc, bao gồm cả giọng hát, lời bài hát có dấu thời gian và bản phối nhạc cụ hoàn chỉnh.

Nhóm mô hình Lyria 3 bao gồm 2 mô hình:

| Mô hình | Mã kiểu máy | Phù hợp nhất cho | Thời lượng | Đầu ra |
| --- | --- | --- | --- | --- |
| **Đoạn video Lyria 3** | `lyria-3-clip-preview` | Đoạn video ngắn, video lặp lại, bản xem trước | 30 giây | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | Bài hát có thời lượng đầy đủ, có đoạn thơ, điệp khúc và đoạn chuyển | Vài phút (có thể kiểm soát bằng câu lệnh) | MP3 |

Bạn có thể dùng cả hai mô hình bằng [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) mới, hỗ trợ đầu vào đa phương thức (văn bản và hình ảnh) và tạo ra âm thanh **nổi có độ trung thực cao 44,1 kHz**.

## Tạo đoạn nhạc

Mô hình Lyria 3 Clip luôn tạo một đoạn video dài **30 giây**. Để tạo một đoạn video, hãy gọi phương thức `interactions.create` bằng một câu lệnh văn bản. Phản hồi luôn bao gồm lời bài hát và cấu trúc bài hát được tạo cùng với âm thanh trong giản đồ `steps`.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A short instrumental acoustic guitar piece.",
)

generated_audio = interaction.output_audio
if generated_audio:
    with open("music.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A short instrumental acoustic guitar piece.',
});

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
  fs.writeFileSync('music.mp3', Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
  console.log(`Lyrics:\n${lyrics}`);
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

Bạn có thể truy xuất dữ liệu nhạc đã tạo bằng cách sử dụng thuộc tính `interaction.output_audio`. Thuộc tính này trả về khối âm thanh được tạo gần đây nhất. Bạn cũng có thể truy xuất lời bài hát và cấu trúc của bài hát bằng cách sử dụng thuộc tính `interaction.output_text`. Để biết thông tin chi tiết về các thuộc tính tiện lợi, hãy xem phần [Tổng quan về các hoạt động tương tác](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi#convenience-properties).

## Tạo bài hát có thời lượng đầy đủ

Sử dụng mô hình `lyria-3-pro-preview` để tạo các bài hát dài từ một đến hai phút. Mô hình Pro hiểu cấu trúc âm nhạc và có thể tạo ra các bản nhạc có các đoạn, điệp khúc và cầu nối riêng biệt. Bạn có thể điều chỉnh thời lượng bằng cách chỉ định thời lượng trong câu lệnh (ví dụ: "tạo một bài hát dài 2 phút") hoặc bằng cách sử dụng [dấu thời gian](#timing) để xác định cấu trúc.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody."
}'
```

## Chọn định dạng đầu ra

Theo mặc định, các mô hình Lyria 3 tạo âm thanh ở định dạng **MP3**. Đối với Lyria 3 Pro, bạn cũng có thể yêu cầu đầu ra ở định dạng **WAV** bằng cách đặt `response_format`.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="A beautiful piano melody.",
    response_format={"type": "audio"},
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
    response_format: {
        type: 'audio',
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## Phân tích cú pháp phản hồi

Phản hồi từ Lyria 3 chứa nhiều khối nội dung trong giản đồ `steps`.
Các lượt tương tác trả về một chuỗi các bước, trong đó các bước `model_output` chứa nội dung được tạo.
Các khối nội dung văn bản chứa lời bài hát được tạo hoặc nội dung mô tả JSON về cấu trúc bài hát.
Các khối nội dung có loại `audio` chứa dữ liệu âm thanh được mã hoá base64.

### Python

```
lyrics = []
audio_data = None

generated_audio = interaction.output_audio
if generated_audio:
    with open("output.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
const lyrics = [];
let audioData = null;

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
    fs.writeFileSync("output.mp3", Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
    console.log("Lyrics:\n" + lyrics);
}
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

#### Lời bài hát và nhạc xen kẽ

Vì đầu ra của Lyria 3 rất phức tạp (chứa các bước và khối riêng biệt cho lời bài hát (văn bản) được tạo và bản thân bài hát (âm thanh)), nên các thuộc tính tiện lợi sẽ cung cấp một lối tắt nhanh chóng và được đề xuất.

Tuy nhiên, nếu muốn kiểm soát hoàn toàn, theo cách lập trình đối với dòng thời gian thô của các bước do máy chủ trả về (chẳng hạn như ghi nhật ký các khối nội dung riêng lẻ khi chúng được nhận), bạn có thể lặp lại `steps` theo cách thủ công:

### Python

```
lyrics = []
audio_data = None

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "audio":
                audio_data = base64.b64decode(content_block.data)
            elif content_block.type == "text":
                lyrics.append(content_block.text)

if lyrics:
    print("Lyrics:\n" + "\n".join(lyrics))

if audio_data:
    with open("output.mp3", "wb") as f:
        f.write(audio_data)
```

### JavaScript

```
const lyrics = [];
let audioData = null;

for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        for (const contentBlock of step.content) {
            if (contentBlock.type === 'audio') {
                audioData = Buffer.from(contentBlock.data, 'base64');
            } else if (contentBlock.type === 'text') {
                lyrics.push(contentBlock.text);
            }
        }
    }
}

if (lyrics.length) {
    console.log("Lyrics:\n" + lyrics.join("\n"));
}

if (audioData) {
    fs.writeFileSync("output.mp3", audioData);
}
```

## Tạo nhạc từ hình ảnh

Lyria 3 hỗ trợ nhiều phương thức nhập dữ liệu – bạn có thể cung cấp tối đa **10 hình ảnh** cùng với câu lệnh văn bản trong danh sách `input` và mô hình sẽ sáng tác nhạc dựa trên nội dung trực quan.

### Python

```
import base64

with open("desert_sunset.jpg", "rb") as f:
    image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

response = client.interactions.create(
    model="lyria-3-pro-preview",
    input=[
        {
            "type": "text",
            "text": "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_b64,
        },
    ],
)
```

### JavaScript

```
import * as fs from "fs";

const imageBytes = fs.readFileSync("desert_sunset.jpg").toString("base64");

const interaction = await client.interactions.create({
    model: "lyria-3-pro-preview",
    input: [
        {
            type: "text",
            text: "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            type: "image",
            mime_type: "image/jpeg",
            data: imageBytes,
        },
    ],
});
```

### REST

```
# Pass base64 encoded image data directly:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

## Cung cấp lời bài hát tuỳ chỉnh

Bạn có thể tự viết lời bài hát và đưa lời bài hát đó vào câu lệnh. Sử dụng các thẻ phần như `[Verse]`, `[Chorus]` và `[Bridge]` để giúp mô hình hiểu cấu trúc bài hát:

### Python

```
prompt = """
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## Kiểm soát thời gian và cấu trúc

Bạn có thể chỉ định chính xác những gì xảy ra tại các thời điểm cụ thể trong bài hát bằng cách sử dụng dấu thời gian. Việc này rất hữu ích để kiểm soát thời điểm nhạc cụ bắt đầu, thời điểm lời bài hát được chuyển và cách bài hát tiến triển:

### Python

```
prompt = """
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## Tạo bản nhạc không lời

Đối với nhạc nền, nhạc trong trò chơi hoặc bất kỳ trường hợp sử dụng nào không yêu cầu giọng hát, bạn có thể yêu cầu mô hình tạo ra các bản nhạc chỉ có nhạc cụ:

### Python

```
interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## Tạo nhạc bằng nhiều ngôn ngữ

Lyria 3 tạo lời bài hát bằng ngôn ngữ trong câu lệnh của bạn. Để tạo một bài hát có lời bằng tiếng Pháp, hãy viết câu lệnh bằng tiếng Pháp. Mô hình này điều chỉnh phong cách giọng nói và cách phát âm cho phù hợp với ngôn ngữ.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## Trí tuệ của mô hình

Lyria 3 phân tích quy trình tạo câu lệnh của bạn, trong đó mô hình suy luận thông qua cấu trúc âm nhạc (đoạn mở đầu, đoạn thơ, điệp khúc, đoạn chuyển, v.v.) dựa trên câu lệnh của bạn.
Việc này diễn ra trước khi âm thanh được tạo và đảm bảo tính nhất quán về cấu trúc cũng như tính nhạc.

## Hướng dẫn đặt câu lệnh

Câu lệnh càng cụ thể thì kết quả càng tốt. Sau đây là những nội dung bạn có thể đưa vào để hướng dẫn quá trình tạo:

- **Thể loại**: Chỉ định một thể loại hoặc sự kết hợp của các thể loại (ví dụ: "lo-fi hip hop", "jazz fusion", "cinematic orchestral").
- **Nhạc cụ**: Nêu tên nhạc cụ cụ thể (ví dụ: "đàn piano Fender Rhodes", "đàn guitar slide", "máy đánh trống TR-808").
- **BPM**: Đặt nhịp độ (ví dụ: "120 BPM", "nhịp độ chậm khoảng 70 BPM").
- **Khoá/Gam**: Nêu rõ một khoá nhạc (ví dụ: "trong khoá Sol trưởng", "trong khoá Rê thứ").
- **Tâm trạng và bầu không khí**: Sử dụng tính từ mô tả (ví dụ: "hoài niệm", "mạnh mẽ", "siêu thực", "mơ màng").
- **Cấu trúc**: Sử dụng các thẻ như `[Verse]`, `[Chorus]`, `[Bridge]`, `[Intro]`, `[Outro]` hoặc dấu thời gian để kiểm soát tiến trình của bài hát.
- **Thời lượng**: Mô hình Đoạn trích luôn tạo ra các đoạn trích dài 30 giây. Đối với mô hình Pro, hãy chỉ định độ dài dự kiến trong câu lệnh (ví dụ: "tạo một bài hát dài 2 phút") hoặc dùng dấu thời gian để kiểm soát thời lượng.

### Câu lệnh mẫu

Sau đây là một số ví dụ về câu lệnh hiệu quả:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## Các phương pháp hay nhất

- **Lặp lại với Clip trước.** Sử dụng mô hình `lyria-3-clip-preview` nhanh hơn để thử nghiệm các câu lệnh trước khi tạo một hình ảnh/video dài bằng `lyria-3-pro-preview`.
- **Mô tả cụ thể.** Câu lệnh mơ hồ sẽ tạo ra kết quả chung chung. Đề cập đến nhạc cụ, số nhịp/phút, khoá nhạc, tâm trạng và cấu trúc để có kết quả tốt nhất.
- **Ngôn ngữ phải phù hợp.** Đưa ra câu lệnh bằng ngôn ngữ mà bạn muốn có lời bài hát.
- **Sử dụng thẻ phần.** Thẻ `[Verse]`, `[Chorus]`, `[Bridge]` giúp mô hình có cấu trúc rõ ràng để tuân theo.
- **Tách lời bài hát khỏi hướng dẫn.** Khi cung cấp lời bài hát tuỳ chỉnh, hãy tách riêng lời bài hát với hướng dẫn về chỉ dẫn âm nhạc.

## Các điểm hạn chế

- **An toàn**: Tất cả câu lệnh đều được bộ lọc an toàn kiểm tra. Những câu lệnh kích hoạt bộ lọc sẽ bị chặn. Điều này bao gồm cả những câu lệnh yêu cầu giọng nói của một nghệ sĩ cụ thể hoặc việc tạo ra lời bài hát có bản quyền.
- **Tạo hình mờ**: Tất cả âm thanh được tạo đều có [thuỷ vân âm thanh SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=vi) để nhận dạng. Hình mờ này không thể nghe thấy bằng tai thường và không ảnh hưởng đến trải nghiệm nghe.
- **Chỉnh sửa nhiều lượt**: Tạo nhạc là một quy trình chỉ diễn ra một lượt.
  Phiên bản Lyria 3 hiện tại không được hỗ trợ chỉnh sửa lặp lại hoặc tinh chỉnh một đoạn video được tạo thông qua nhiều câu lệnh.
- **Độ dài**: Mô hình Đoạn trích luôn tạo ra các đoạn trích dài 30 giây. Mô hình Pro tạo ra những bài hát có thời lượng vài phút; thời lượng chính xác có thể bị ảnh hưởng bởi câu lệnh của bạn.
- **Tính xác định**: Kết quả có thể khác nhau giữa các lệnh gọi, ngay cả khi dùng cùng một câu lệnh.

## Bước tiếp theo

- Xem [giá](https://ai.google.dev/gemini-api/docs/pricing?hl=vi) của các mô hình Lyria 3.
- Thử [tạo nhạc trực tuyến theo thời gian thực](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=vi) bằng Lyria RealTime.
- Tạo các cuộc trò chuyện có nhiều người nói bằng [các mô hình TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi).
- Khám phá cách tạo [hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi) hoặc [video](https://ai.google.dev/gemini-api/docs/video?hl=vi).
- Tìm hiểu cách Gemini có thể [hiểu tệp âm thanh](https://ai.google.dev/gemini-api/docs/audio?hl=vi).
- Trò chuyện theo thời gian thực với Gemini bằng [Live API](https://ai.google.dev/gemini-api/docs/live?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-16 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-16 UTC."],[],[]]
