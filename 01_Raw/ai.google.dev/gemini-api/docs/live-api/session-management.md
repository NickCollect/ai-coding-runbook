---
source_url: https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=vi
fetched_at: 2026-05-05T20:00:31.054373+00:00
title: "Session management with Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Session management with Live API

Trong Live API, phiên là một kết nối liên tục, trong đó dữ liệu đầu vào và đầu ra được truyền trực tuyến liên tục qua cùng một kết nối (đọc thêm về [cách hoạt động](https://ai.google.dev/gemini-api/docs/live?hl=vi)).
Thiết kế phiên duy nhất này cho phép độ trễ thấp và hỗ trợ các tính năng duy nhất, nhưng cũng có thể gây ra các thách thức, chẳng hạn như giới hạn thời gian phiên và việc chấm dứt sớm.
Hướng dẫn này đề cập đến các chiến lược để khắc phục những thách thức về việc quản lý phiên có thể phát sinh khi sử dụng Live API.

## Thời gian tồn tại của phiên

Nếu không nén, các phiên chỉ có âm thanh sẽ bị giới hạn ở 15 phút và các phiên có cả âm thanh và video sẽ bị giới hạn ở 2 phút. Nếu vượt quá các giới hạn này, phiên sẽ kết thúc (và do đó, kết nối cũng kết thúc), nhưng bạn có thể sử dụng [tính năng nén cửa sổ ngữ cảnh](#context-window-compression) để kéo dài phiên đến một khoảng thời gian không giới hạn.

Thời gian tồn tại của một kết nối cũng bị giới hạn, khoảng 10 phút. Khi kết nối chấm dứt, phiên cũng sẽ chấm dứt. Trong trường hợp này, bạn có thể định cấu hình một phiên duy nhất để duy trì hoạt động trên nhiều kết nối bằng cách sử dụng [tính năng tiếp tục phiên](#session-resumption).
Bạn cũng sẽ nhận được [thông báo GoAway](#goaway-message) trước khi kết thúc kết nối, cho phép bạn thực hiện các hành động khác.

## Nén cửa sổ ngữ cảnh

Để cho phép các phiên dài hơn và tránh tình trạng kết nối bị chấm dứt đột ngột, bạn có thể bật tính năng nén cửa sổ ngữ cảnh bằng cách đặt trường [contextWindowCompression](https://ai.google.dev/api/live?hl=vi#BidiGenerateContentSetup.FIELDS.ContextWindowCompressionConfig.BidiGenerateContentSetup.context_window_compression) trong cấu hình phiên.

Trong [ContextWindowCompressionConfig](https://ai.google.dev/api/live?hl=vi#contextwindowcompressionconfig), bạn có thể định cấu hình [cơ chế cửa sổ trượt](https://ai.google.dev/api/live?hl=vi#ContextWindowCompressionConfig.FIELDS.ContextWindowCompressionConfig.SlidingWindow.ContextWindowCompressionConfig.sliding_window) và [số lượng mã thông báo](https://ai.google.dev/api/live?hl=vi#ContextWindowCompressionConfig.FIELDS.int64.ContextWindowCompressionConfig.trigger_tokens) kích hoạt tính năng nén.

### Python

```
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    context_window_compression=(
        # Configures compression with default parameters.
        types.ContextWindowCompressionConfig(
            sliding_window=types.SlidingWindow(),
        )
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  contextWindowCompression: { slidingWindow: {} }
};
```

## Tiếp tục phiên

Để ngăn chặn việc kết thúc phiên khi máy chủ định kỳ đặt lại kết nối WebSocket, hãy định cấu hình trường [sessionResumption](https://ai.google.dev/api/live?hl=vi#BidiGenerateContentSetup.FIELDS.SessionResumptionConfig.BidiGenerateContentSetup.session_resumption) trong [cấu hình thiết lập](https://ai.google.dev/api/live?hl=vi#BidiGenerateContentSetup).

Việc truyền cấu hình này khiến máy chủ gửi thông báo [SessionResumptionUpdate](https://ai.google.dev/api/live?hl=vi#SessionResumptionUpdate). Bạn có thể dùng thông báo này để tiếp tục phiên bằng cách truyền mã thông báo tiếp tục gần đây nhất làm [`SessionResumptionConfig.handle`](https://ai.google.dev/api/live?hl=vi#SessionResumptionConfig.FIELDS.string.SessionResumptionConfig.handle) của kết nối tiếp theo.

Mã thông báo tiếp tục có hiệu lực trong 2 giờ sau khi phiên gần nhất kết thúc.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

async def main():
    print(f"Connecting to the service with handle {previous_session_handle}...")
    async with client.aio.live.connect(
        model=model,
        config=types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            session_resumption=types.SessionResumptionConfig(
                # The handle of the session to resume is passed here,
                # or else None to start a new session.
                handle=previous_session_handle
            ),
        ),
    ) as session:
        while True:
            await session.send_client_content(
                turns=types.Content(
                    role="user", parts=[types.Part(text="Hello world!")]
                )
            )
            async for message in session.receive():
                # Periodically, the server will send update messages that may
                # contain a handle for the current state of the session.
                if message.session_resumption_update:
                    update = message.session_resumption_update
                    if update.resumable and update.new_handle:
                        # The handle should be retained and linked to the session.
                        return update.new_handle

                # For the purposes of this example, placeholder input is continually fed
                # to the model. In non-sample code, the model inputs would come from
                # the user.
                if message.server_content and message.server_content.turn_complete:
                    break

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

console.debug('Connecting to the service with handle %s...', previousSessionHandle)
const session = await ai.live.connect({
  model: model,
  callbacks: {
    onopen: function () {
      console.debug('Opened');
    },
    onmessage: function (message) {
      responseQueue.push(message);
    },
    onerror: function (e) {
      console.debug('Error:', e.message);
    },
    onclose: function (e) {
      console.debug('Close:', e.reason);
    },
  },
  config: {
    responseModalities: [Modality.AUDIO],
    sessionResumption: { handle: previousSessionHandle }
    // The handle of the session to resume is passed here, or else null to start a new session.
  }
});

const inputTurns = 'Hello how are you?';
session.sendClientContent({ turns: inputTurns });

const turns = await handleTurn();
for (const turn of turns) {
  if (turn.sessionResumptionUpdate) {
    if (turn.sessionResumptionUpdate.resumable && turn.sessionResumptionUpdate.newHandle) {
      let newHandle = turn.sessionResumptionUpdate.newHandle
      // ...Store newHandle and start new session with this handle here
    }
  }
}

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

## Nhận được thông báo trước khi phiên kết nối bị ngắt

Máy chủ gửi thông báo [GoAway](https://ai.google.dev/api/live?hl=vi#GoAway) cho biết rằng kết nối hiện tại sẽ sớm bị chấm dứt. Thông báo này bao gồm [timeLeft](https://ai.google.dev/api/live?hl=vi#GoAway.FIELDS.google.protobuf.Duration.GoAway.time_left), cho biết thời gian còn lại và cho phép bạn thực hiện thêm hành động trước khi kết nối bị chấm dứt ở trạng thái ABORTED.

### Python

```
async for response in session.receive():
    if response.go_away is not None:
        # The connection will soon be terminated
        print(response.go_away.time_left)
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.goAway) {
    console.debug('Time left: %s\n', turn.goAway.timeLeft);
  }
}
```

## Nhận thông báo khi quá trình tạo hoàn tất

Máy chủ gửi thông báo [generationComplete](https://ai.google.dev/api/live?hl=vi#BidiGenerateContentServerContent.FIELDS.bool.BidiGenerateContentServerContent.generation_complete) cho biết mô hình đã hoàn tất việc tạo phản hồi.

### Python

```
async for response in session.receive():
    if response.server_content.generation_complete is True:
        # The generation is complete
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.generationComplete) {
    // The generation is complete
  }
}
```

## Bước tiếp theo

Khám phá thêm các cách sử dụng Live API trong hướng dẫn đầy đủ về [Các chức năng](https://ai.google.dev/gemini-api/docs/live?hl=vi), trang [Cách sử dụng công cụ](https://ai.google.dev/gemini-api/docs/live-tools?hl=vi) hoặc [Sổ tay Live API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
