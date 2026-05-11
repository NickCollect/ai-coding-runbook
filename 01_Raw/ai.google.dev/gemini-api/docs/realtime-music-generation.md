---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=vi
fetched_at: 2026-05-11T05:04:20.789935+00:00
title: "T\u1ea1o nh\u1ea1c theo th\u1eddi gian th\u1ef1c b\u1eb1ng Lyria RealTime \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tạo nhạc theo thời gian thực bằng Lyria RealTime

Gemini API, sử dụng [Lyria RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=vi), cung cấp quyền truy cập vào một mô hình tạo nhạc trực tuyến theo thời gian thực, hiện đại. Công cụ này cho phép nhà phát triển xây dựng các ứng dụng mà người dùng có thể tương tác để tạo, điều khiển liên tục và biểu diễn nhạc cụ.

Tính năng tạo nhạc theo thời gian thực của Lyria sử dụng một kết nối truyền phát trực tiếp hai chiều, có độ trễ thấp và liên tục bằng [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API).

Để trải nghiệm những nội dung có thể tạo bằng Lyria RealTime, hãy dùng thử trên AI Studio bằng ứng dụng [Prompt DJ](https://aistudio.google.com/apps/bundled/promptdj?hl=vi) hoặc [MIDI DJ](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=vi).

## Tạo và điều khiển nhạc

Lyria RealTime hoạt động tương tự như [Live API](https://ai.google.dev/gemini-api/docs/live?hl=vi) ở chỗ sử dụng Websocket để duy trì giao tiếp theo thời gian thực với mô hình.

Đoạn mã sau đây minh hoạ cách tạo nhạc:

### Python

Ví dụ này khởi tạo phiên Lyria RealTime bằng `client.aio.live.music.connect()`, sau đó gửi một lời nhắc ban đầu bằng `session.set_weighted_prompts()` cùng với cấu hình ban đầu bằng `session.set_music_generation_config`, bắt đầu tạo nhạc bằng `session.play()` và thiết lập `receive_audio()` để xử lý các đoạn âm thanh mà nó nhận được.

```
  import asyncio
  from google import genai
  from google.genai import types

  client = genai.Client(http_options={'api_version': 'v1alpha'})

  async def main():
      async def receive_audio(session):
        """Example background task to process incoming audio."""
        while True:
          async for message in session.receive():
            audio_data = message.server_content.audio_chunks[0].data
            # Process audio...
            await asyncio.sleep(10**-12)

      async with (
        client.aio.live.music.connect(model='models/lyria-realtime-exp') as session,
        asyncio.TaskGroup() as tg,
      ):
        # Set up task to receive server messages.
        tg.create_task(receive_audio(session))

        # Send initial prompts and config
        await session.set_weighted_prompts(
          prompts=[
            types.WeightedPrompt(text='minimal techno', weight=1.0),
          ]
        )
        await session.set_music_generation_config(
          config=types.LiveMusicGenerationConfig(bpm=90, temperature=1.0)
        )

        # Start streaming music
        await session.play()
  if __name__ == "__main__":
      asyncio.run(main())
```

### JavaScript

Ví dụ này khởi tạo phiên Lyria RealTime bằng `client.live.music.connect()`, sau đó gửi một lời nhắc ban đầu bằng `session.setWeightedPrompts()` cùng với cấu hình ban đầu bằng `session.setMusicGenerationConfig`, bắt đầu tạo nhạc bằng `session.play()` và thiết lập một lệnh gọi lại `onMessage` để xử lý các đoạn âm thanh mà nó nhận được.

```
import { GoogleGenAI } from "@google/genai";
import Speaker from "speaker";
import { Buffer } from "buffer";

const client = new GoogleGenAI({
  apiKey: GEMINI_API_KEY,
    apiVersion: "v1alpha" ,
});

async function main() {
  const speaker = new Speaker({
    channels: 2,       // stereo
    bitDepth: 16,      // 16-bit PCM
    sampleRate: 44100, // 44.1 kHz
  });

  const session = await client.live.music.connect({
    model: "models/lyria-realtime-exp",
    callbacks: {
      onmessage: (message) => {
        if (message.serverContent?.audioChunks) {
          for (const chunk of message.serverContent.audioChunks) {
            const audioBuffer = Buffer.from(chunk.data, "base64");
            speaker.write(audioBuffer);
          }
        }
      },
      onerror: (error) => console.error("music session error:", error),
      onclose: () => console.log("Lyria RealTime stream closed."),
    },
  });

  await session.setWeightedPrompts({
    weightedPrompts: [
      { text: "Minimal techno with deep bass, sparse percussion, and atmospheric synths", weight: 1.0 },
    ],
  });

  await session.setMusicGenerationConfig({
    musicGenerationConfig: {
      bpm: 90,
      temperature: 1.0,
      audioFormat: "pcm16",  // important so we know format
      sampleRateHz: 44100,
    },
  });

  await session.play();
}

main().catch(console.error);
```

Sau đó, bạn có thể dùng `session.play()`, `session.pause()`, `session.stop()` và `session.reset_context()` để bắt đầu, tạm dừng, dừng hoặc đặt lại phiên.

## Điều hướng nhạc theo thời gian thực

Bạn có thể định hướng quá trình tạo nhạc theo thời gian thực bằng cách gửi câu lệnh và cập nhật các thông số tạo theo thời gian thực.

### Câu lệnh Lyria RealTime

Trong khi sự kiện phát trực tiếp đang diễn ra, bạn có thể gửi tin nhắn `WeightedPrompt` mới bất cứ lúc nào để thay đổi nhạc được tạo. Mô hình sẽ chuyển đổi mượt mà dựa trên dữ liệu đầu vào mới.

Câu lệnh cần tuân theo đúng định dạng với `text` (câu lệnh thực tế) và `weight`. `weight` có thể nhận bất kỳ giá trị nào ngoại trừ `0`. `1.0`thường là một điểm xuất phát tốt.

### Python

```
  from google.genai import types

  await session.set_weighted_prompts(
    prompts=[
      {"text": "Piano", "weight": 2.0},
      types.WeightedPrompt(text="Meditation", weight=0.5),
      types.WeightedPrompt(text="Live Performance", weight=1.0),
    ]
  )
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    weightedPrompts: [
      { text: 'Harmonica', weight: 0.3 },
      { text: 'Afrobeat', weight: 0.7 }
    ],
  });
```

Xin lưu ý rằng quá trình chuyển đổi mô hình có thể diễn ra hơi đột ngột khi bạn thay đổi lời nhắc một cách đáng kể. Vì vậy, bạn nên triển khai một số loại hiệu ứng làm mờ bằng cách gửi các giá trị trọng số trung gian đến mô hình.

### Cập nhật cấu hình

Bạn có thể điều hướng quá trình tạo nhạc bằng cách cập nhật các thông số tạo nhạc theo thời gian thực. Bạn không thể chỉ cập nhật một tham số, mà cần phải đặt toàn bộ cấu hình. Nếu không, các trường khác sẽ được đặt lại về giá trị mặc định.

Vì việc cập nhật bpm hoặc tỷ lệ là một thay đổi lớn đối với mô hình, bạn cũng cần cho mô hình biết rằng mô hình cần đặt lại ngữ cảnh bằng cách sử dụng `reset_context()` để tính đến cấu hình mới. Thao tác này sẽ không dừng luồng phát, nhưng sẽ là một quá trình chuyển đổi khó khăn. Bạn không cần làm việc này cho các tham số khác.

### Python

```
  from google.genai import types

  await session.set_music_generation_config(
    config=types.LiveMusicGenerationConfig(
      bpm=128,
      scale=types.Scale.D_MAJOR_B_MINOR,
      music_generation_mode=types.MusicGenerationMode.QUALITY
    )
  )
  await session.reset_context();
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    musicGenerationConfig: { 
      bpm: 120,
      density: 0.75,
      musicGenerationMode: MusicGenerationMode.QUALITY
    },
  });
  await session.reset_context();
```

## Hướng dẫn về câu lệnh cho Lyria RealTime

Sau đây là danh sách không đầy đủ các câu lệnh bạn có thể dùng để nhắc Lyria RealTime:

- Nhạc cụ: `303 Acid Bass, 808 Hip Hop Beat, Accordion, Alto Saxophone,
  Bagpipes, Balalaika Ensemble, Banjo, Bass Clarinet, Bongos, Boomy Bass,
  Bouzouki, Buchla Synths, Cello, Charango, Clavichord, Conga Drums,
  Didgeridoo, Dirty Synths, Djembe, Drumline, Dulcimer, Fiddle, Flamenco
  Guitar, Funk Drums, Glockenspiel, Guitar, Hang Drum, Harmonica, Harp,
  Harpsichord, Hurdy-gurdy, Kalimba, Koto, Lyre, Mandolin, Maracas, Marimba,
  Mbira, Mellotron, Metallic Twang, Moog Oscillations, Ocarina, Persian Tar,
  Pipa, Precision Bass, Ragtime Piano, Rhodes Piano, Shamisen, Shredding
  Guitar, Sitar, Slide Guitar, Smooth Pianos, Spacey Synths, Steel Drum, Synth
  Pads, Tabla, TR-909 Drum Machine, Trumpet, Tuba, Vibraphone, Viola Ensemble,
  Warm Acoustic Guitar, Woodwinds, ...`
- Thể loại nhạc: `Acid Jazz, Afrobeat, Alternative Country, Baroque, Bengal Baul,
  Bhangra, Bluegrass, Blues Rock, Bossa Nova, Breakbeat, Celtic Folk, Chillout,
  Chiptune, Classic Rock, Contemporary R&B, Cumbia, Deep House, Disco Funk,
  Drum & Bass, Dubstep, EDM, Electro Swing, Funk Metal, G-funk, Garage Rock,
  Glitch Hop, Grime, Hyperpop, Indian Classical, Indie Electronic, Indie Folk,
  Indie Pop, Irish Folk, Jam Band, Jamaican Dub, Jazz Fusion, Latin Jazz, Lo-Fi
  Hip Hop, Marching Band, Merengue, New Jack Swing, Minimal Techno, Moombahton,
  Neo-Soul, Orchestral Score, Piano Ballad, Polka, Post-Punk, 60s Psychedelic
  Rock, Psytrance, R&B, Reggae, Reggaeton, Renaissance Music, Salsa, Shoegaze,
  Ska, Surf Rock, Synthpop, Techno, Trance, Trap Beat, Trip Hop, Vaporwave,
  Witch house, ...`
- Tâm trạng/Nội dung mô tả: `Acoustic Instruments, Ambient, Bright Tones, Chill,
  Crunchy Distortion, Danceable, Dreamy, Echo, Emotional, Ethereal Ambience,
  Experimental, Fat Beats, Funky, Glitchy Effects, Huge Drop, Live Performance,
  Lo-fi, Ominous Drone, Psychedelic, Rich Orchestration, Saturated Tones,
  Subdued Melody, Sustained Chords, Swirling Phasers, Tight Groove,
  Unsettling, Upbeat, Virtuoso, Weird Noises, ...`

Đây chỉ là một số ví dụ, Lyria RealTime có thể làm được nhiều việc hơn thế. Thử nghiệm với câu lệnh của riêng bạn!

## Các phương pháp hay nhất

- Các ứng dụng khách phải triển khai tính năng đệm âm thanh mạnh mẽ để đảm bảo quá trình phát mượt mà. Điều này giúp tính đến độ trễ mạng và những thay đổi nhỏ về độ trễ tạo.
- Đưa ra câu lệnh hiệu quả:
  - Hãy cung cấp thông tin mô tả. Sử dụng tính từ mô tả tâm trạng, thể loại và nhạc cụ.
  - Lặp lại và điều chỉnh dần dần. Thay vì thay đổi hoàn toàn câu lệnh, hãy thử thêm hoặc sửa đổi các phần tử để biến đổi nhạc một cách mượt mà hơn.
  - Thử nghiệm với trọng số trên `WeightedPrompt` để tác động đến mức độ ảnh hưởng của một câu lệnh mới đối với quá trình tạo nội dung đang diễn ra.

## Chi tiết kỹ thuật

Phần này mô tả cụ thể cách sử dụng tính năng tạo nhạc theo thời gian thực của Lyria.

### Thông số kỹ thuật

- Định dạng đầu ra: Âm thanh PCM 16 bit thô
- Tốc độ lấy mẫu: 48 kHz
- Kênh: 2 (âm thanh nổi)

### Các chế độ kiểm soát

Bạn có thể ảnh hưởng đến quá trình tạo nhạc theo thời gian thực bằng cách gửi tin nhắn có chứa:

- `WeightedPrompt`: Một chuỗi văn bản mô tả ý tưởng âm nhạc, thể loại, nhạc cụ, tâm trạng hoặc đặc điểm. Bạn có thể cung cấp nhiều câu lệnh để kết hợp các yếu tố ảnh hưởng. Hãy xem [phía trên](https://ai.google.dev/gemini-api/docs/:?hl=vi#steer-music) để biết thêm thông tin chi tiết về cách đưa ra câu lệnh hiệu quả nhất cho Lyria RealTime.
- `MusicGenerationConfig`: Cấu hình cho quy trình tạo nhạc, ảnh hưởng đến các đặc điểm của âm thanh đầu ra.). Các tham số bao gồm:
  - `guidance`: (số thực có độ chính xác đơn) Phạm vi: `[0.0, 6.0]`. Mặc định: `4.0`.
    Kiểm soát mức độ tuân thủ câu lệnh của mô hình. Hướng dẫn chi tiết hơn sẽ giúp cải thiện mức độ tuân thủ lời nhắc, nhưng khiến các chuyển cảnh trở nên đột ngột hơn.
  - `bpm`: (int) Phạm vi: `[60, 200]`.
    Đặt số nhịp mỗi phút bạn muốn cho bản nhạc được tạo. Bạn cần dừng/phát hoặc đặt lại ngữ cảnh để mô hình tính đến nhịp độ mới.
  - `density`: (số thực có độ chính xác đơn) Phạm vi: `[0.0, 1.0]`.
    Kiểm soát mật độ của các nốt nhạc/âm thanh. Giá trị thấp tạo ra nhạc thưa thớt hơn; giá trị cao tạo ra nhạc "dồn dập" hơn.
  - `brightness`: (số thực có độ chính xác đơn) Phạm vi: `[0.0, 1.0]`.
    Điều chỉnh chất lượng âm sắc. Giá trị càng cao thì âm thanh càng "sáng", thường nhấn mạnh các tần số cao hơn.
  - `scale`: (Enum) Đặt thang âm nhạc (Khoá và chế độ) cho quá trình tạo. Sử dụng [các giá trị enum `Scale`](#scale-enum) do SDK cung cấp. Bạn cần dừng/phát hoặc đặt lại ngữ cảnh để mô hình tính đến tỷ lệ mới.
  - `mute_bass`: (bool) Mặc định: `False`.
    Kiểm soát xem mô hình có giảm âm trầm của đầu ra hay không.
  - `mute_drums`: (bool) Mặc định: `False`.
    Kiểm soát xem đầu ra của mô hình có giảm âm lượng trống của đầu ra hay không.
  - `only_bass_and_drums`: (bool) Mặc định: `False`.
    Điều chỉnh mô hình để chỉ xuất ra âm trầm và trống.
  - `music_generation_mode`: (Enum) Cho biết mô hình có nên tập trung vào `QUALITY` (giá trị mặc định) hay `DIVERSITY` của nhạc hay không. Bạn cũng có thể đặt thành `VOCALIZATION` để cho phép mô hình tạo ra các âm thanh như một nhạc cụ khác (thêm các âm thanh đó dưới dạng câu lệnh mới).
- `PlaybackControl`: Các lệnh điều khiển các khía cạnh phát, chẳng hạn như phát, tạm dừng, dừng hoặc đặt lại ngữ cảnh.

Đối với `bpm`, `density`, `brightness` và `scale`, nếu bạn không cung cấp giá trị nào, thì mô hình sẽ quyết định giá trị nào phù hợp nhất dựa trên câu lệnh ban đầu của bạn.

Các thông số cổ điển khác như `temperature` (0 đến 3, mặc định là 1,1), `top_k` (1 đến 1000, mặc định là 40) và `seed` (0 đến 2.147.483.647, được chọn ngẫu nhiên theo mặc định) cũng có thể tuỳ chỉnh trong `MusicGenerationConfig`.

#### Giá trị enum tỷ lệ

Sau đây là tất cả các giá trị tỷ lệ mà mô hình có thể chấp nhận:

| Giá trị enum | Gam / Khoá |
| --- | --- |
| `C_MAJOR_A_MINOR` | Đô trưởng / La thứ |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | Rê giáng trưởng / Si giáng thứ |
| `D_MAJOR_B_MINOR` | D trưởng / B thứ |
| `E_FLAT_MAJOR_C_MINOR` | Mi giáng trưởng / Đô thứ |
| `E_MAJOR_D_FLAT_MINOR` | Mi trưởng / Đô thăng/Rê giáng thứ |
| `F_MAJOR_D_MINOR` | Fa trưởng / Rê thứ |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | Sol giáng trưởng / Mi giáng thứ |
| `G_MAJOR_E_MINOR` | Sol trưởng / Mi thứ |
| `A_FLAT_MAJOR_F_MINOR` | La giáng trưởng / Fa thứ |
| `A_MAJOR_G_FLAT_MINOR` | La trưởng / Fa thăng/Sol giáng thứ |
| `B_FLAT_MAJOR_G_MINOR` | Si giáng trưởng / Sol thứ |
| `B_MAJOR_A_FLAT_MINOR` | B major / G♯/A♭ minor |
| `SCALE_UNSPECIFIED` | Mặc định / Mô hình quyết định |

Mô hình này có khả năng hướng dẫn các nốt nhạc được chơi, nhưng không phân biệt được các khoá tương đối. Do đó, mỗi enum tương ứng với cả hai khoá chính và khoá phụ tương đối. Ví dụ: `C_MAJOR_A_MINOR` sẽ tương ứng với tất cả các phím trắng của đàn piano và `F_MAJOR_D_MINOR` sẽ là tất cả các phím trắng ngoại trừ phím B giáng.

### Các điểm hạn chế

- Chỉ nhạc không lời: Mô hình chỉ tạo nhạc không lời.
- An toàn: Các bộ lọc an toàn sẽ kiểm tra câu lệnh. Các câu lệnh kích hoạt bộ lọc sẽ bị bỏ qua. Trong trường hợp đó, lời giải thích sẽ được viết trong trường `filtered_prompt` của đầu ra.
- Tạo hình mờ: Âm thanh đầu ra luôn được tạo hình mờ để nhận dạng theo các nguyên tắc [AI có trách nhiệm](https://ai.google/responsibility/principles/?hl=vi) của chúng tôi.

## Bước tiếp theo

- Tạo các bài hát hoàn chỉnh và bản nhạc có giọng hát bằng [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=vi),
- Thay vì âm nhạc, hãy tìm hiểu cách tạo cuộc trò chuyện có nhiều người nói bằng [các mô hình TTS](https://ai.google.dev/gemini-api/docs/audio-generation?hl=vi),
- Khám phá cách tạo [hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi) hoặc [video](https://ai.google.dev/gemini-api/docs/video?hl=vi),
- Thay vì tạo nhạc hoặc âm thanh, hãy tìm hiểu cách Gemini có thể [hiểu các tệp âm thanh](https://ai.google.dev/gemini-api/docs/audio?hl=vi),
- Trò chuyện theo thời gian thực với Gemini bằng [Live API](https://ai.google.dev/gemini-api/docs/live?hl=vi).

Khám phá [Sổ tay hướng dẫn](https://github.com/google-gemini/cookbook) để xem thêm các ví dụ về mã và hướng dẫn.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
