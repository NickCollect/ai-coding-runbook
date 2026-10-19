---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi
fetched_at: 2026-10-19T05:44:17.117652+00:00
title: "Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Interactions API

Interactions API là cách tốt nhất để xây dựng bằng các mô hình và tác nhân Gemini. Kể từ tháng 6 năm 2026, API này sẽ được cung cấp rộng rãi và được đề xuất cho tất cả các dự án mới. Mặc dù hiện được coi là API cũ, nhưng API
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=vi)
vẫn được hỗ trợ đầy đủ.

## Tại sao bạn nên sử dụng Interactions API?

- **Giao diện chung cho tất cả ứng dụng**: Được thiết kế làm giao diện tiêu chuẩn
  cho mọi trường hợp sử dụng, bao gồm tạo văn bản một lượt,
  hiểu nhiều phương thức, đầu ra có cấu trúc, điều phối công cụ và
  quy trình công việc theo tác nhân.
- **Một API cho các mô hình và tác nhân**: Một điểm cuối và mẫu hợp nhất để
  gọi trực tiếp các mô hình Gemini tiêu chuẩn cũng như các tác nhân chuyên biệt (chẳng hạn
  như Deep Research và các tác nhân được quản lý tuỳ chỉnh).
- **Các tính năng mới ngay khi dùng**: Các tính năng như trạng thái cuộc trò chuyện không bắt buộc ở phía máy chủ
  bằng cách sử dụng `previous_interaction_id`, các bước thực thi có thể quan sát được
  để gỡ lỗi và kết xuất giao diện người dùng, cũng như thực thi ở chế độ [nền](https://ai.google.dev/gemini-api/docs/background-execution?hl=vi) cho các tác vụ chạy trong thời gian dài
  bằng cách sử dụng `background=true`.
- **Chi phí thấp hơn với tỷ lệ kết quả tìm kiếm trong bộ nhớ cache cao hơn**: Khi sử dụng các cuộc trò chuyện nhiều lượt, tính năng quản lý trạng thái không bắt buộc ở phía máy chủ cho phép lưu vào bộ nhớ đệm ngữ cảnh hiệu quả hơn trên các lượt, giúp giảm chi phí token.
- **Nơi ra mắt các tính năng mới**: Trong tương lai, tất cả các mô hình mới, tính năng nhiều phương thức
  , công cụ và tính năng theo tác nhân sẽ ra mắt trên Interactions
  API.

Theo mặc định, Interactions API sẽ lưu trữ các yêu cầu để bạn có thể tận dụng các tính năng quản lý trạng thái ở phía máy chủ bằng cách sử dụng `previous_interaction_id`. Bạn có thể chọn hành vi không trạng thái bằng cách đặt `store=false`. Hãy xem phần [giữ lại dữ liệu](#data-storage-retention) để biết thông tin chi tiết.

## Bắt đầu

- **Thiết lập tác nhân lập trình**: Kết nối với **Gemini Docs MCP** và cài đặt
  kỹ năng `gemini-api-dev` để cấp cho trợ lý của bạn quyền truy cập trực tiếp vào
  tài liệu mới nhất dành cho nhà phát triển và các phương pháp hay nhất. Để biết các bước chi tiết, hãy xem
  [hướng dẫn Thiết lập tác nhân lập trình](https://ai.google.dev/gemini-api/docs/coding-agents?hl=vi)
- **Di chuyển từ `generateContent`**: Nếu bạn đã tích hợp,
  hãy làm theo [Hướng dẫn di chuyển](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=vi) để
  chuyển sang Interactions API.
- **Bắt đầu**: Làm theo các bước trong hướng dẫn [Bắt đầu sử dụng Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=vi).

### Hướng dẫn về tính năng

Khám phá các tính năng cụ thể của Interactions API thông qua các hướng dẫn này. Bạn có thể sử dụng nút bật/tắt trên các trang này để chuyển đổi giữa generateContent và Interactions API:

- [Tạo văn bản](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi)
- [Tạo hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi)
- [Hiểu hình ảnh](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi)
- [Hiểu âm thanh](https://ai.google.dev/gemini-api/docs/audio?hl=vi)
- [Hiểu video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=vi)
- [Xử lý tài liệu](https://ai.google.dev/gemini-api/docs/document-processing?hl=vi)
- [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi)
- [Đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/structured-output?hl=vi)
- [Tác nhân Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi)
- [Suy luận linh hoạt](https://ai.google.dev/gemini-api/docs/flex-inference?hl=vi)
- [Suy luận theo mức độ ưu tiên](https://ai.google.dev/gemini-api/docs/priority-inference?hl=vi)

## Cách thức hoạt động của Interactions API

Interactions API tập trung vào một tài nguyên cốt lõi: [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=vi#Resource:Interaction). `Interaction` đại diện cho một lượt hoàn chỉnh trong cuộc trò chuyện hoặc tác vụ. Đối tượng này hoạt động như một bản ghi phiên, chứa toàn bộ nhật ký tương tác dưới dạng một chuỗi **các bước thực thi** theo trình tự thời gian. Các bước này bao gồm ý tưởng của mô hình, lệnh gọi và kết quả của công cụ ở phía máy chủ hoặc phía máy khách (chẳng hạn như `function_call` và `function_result`) và `model_output` cuối cùng. Tài nguyên được lưu trữ (truy xuất thông qua `interactions.get`) cũng bao gồm các bước `user_input` cho toàn bộ bối cảnh, mặc dù phản hồi `interactions.create` chỉ trả về các bước do mô hình tạo.

Khi bạn gọi
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=vi#CreateInteraction), bạn đang
tạo một tài nguyên `Interaction` mới:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me a short story about a time-traveling lighthouse."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Tell me a short story about a time-traveling lighthouse.",
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Tell me a short story about a time-traveling lighthouse."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Tell me a short story about a time-traveling lighthouse."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Tell me a short story about a time-traveling lighthouse."
  }'
```

### Quản lý trạng thái ở phía máy chủ

Bạn có thể sử dụng `id` của một lượt tương tác đã hoàn tất trong lệnh gọi tiếp theo bằng cách sử dụng
`previous_interaction_id` để tiếp tục cuộc trò chuyện. Máy chủ sử dụng mã nhận dạng này để truy xuất nhật ký trò chuyện, giúp bạn không phải gửi lại toàn bộ nhật ký trò chuyện:

### Python

```
from google import genai

client = genai.Client()

# 1. First turn
turn1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hi, my name is Phil."
)

# 2. Second turn (chained using previous_interaction_id)
turn2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is my name?",
    previous_interaction_id=turn1.id
)

print(turn2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

// 1. First turn
const turn1 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Hi, my name is Phil.",
});

// 2. Second turn (chained using previous_interaction_id)
const turn2 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "What is my name?",
  previous_interaction_id: turn1.id,
});

console.log(turn2.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

// 1. First turn
Interaction turn1 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("Hi, my name is Phil."))
                    .build()))
        .interaction()
        .get();

// 2. Second turn (chained using previousInteractionId)
Interaction turn2 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("What is my name?"))
                    .previousInteractionId(turn1.id().get())
                    .build()))
        .interaction()
        .get();

System.out.println(turn2.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // 1. First turn
    turn1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Hi, my name is Phil."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // 2. Second turn (chained using PreviousInteractionID)
    turn2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-flash"),
            Input:                 interactions.NewInteractionsInput("What is my name?"),
            PreviousInteractionID: turn1.Interaction.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if turn2.Interaction.OutputText != nil {
        fmt.Println(*turn2.Interaction.OutputText)
    }
}
```

### REST

```
# Replace PREVIOUS_INTERACTION_ID with the id returned from the first turn
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is my name?",
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID"
  }'
```

Tham số `previous_interaction_id` chỉ giữ lại nhật ký trò chuyện (dữ liệu đầu vào và đầu ra) bằng cách sử dụng `previous_interaction_id`. Các tham số khác là **theo phạm vi tương tác** và chỉ áp dụng cho lượt tương tác cụ thể mà bạn hiện đang tạo:

- `tools`
- `system_instruction`
- `generation_config` (bao gồm `thinking_level`, `temperature`, v.v.)

Điều này có nghĩa là bạn phải chỉ định lại các tham số này trong mỗi lượt tương tác mới nếu muốn áp dụng các tham số đó. Bạn có thể chọn quản lý trạng thái ở phía máy chủ; bạn cũng có thể hoạt động ở chế độ không trạng thái bằng cách gửi toàn bộ nhật ký trò chuyện trong mỗi yêu cầu.

### Lưu trữ và giữ lại dữ liệu

Theo mặc định, API sẽ lưu trữ tất cả đối tượng Tương tác (`store=true`) để
đơn giản hoá việc sử dụng các tính năng quản lý trạng thái ở phía máy chủ (với
`previous_interaction_id`), [thực thi ở chế độ nền](https://ai.google.dev/gemini-api/docs/background-execution?hl=vi) (sử dụng `background=true`) và
mục đích quan sát.

- **Cấp trả phí**: Hệ thống giữ lại các lượt tương tác trong **55 ngày**.
- **Cấp miễn phí**: Hệ thống giữ lại các lượt tương tác trong **1 ngày**.

Nếu không muốn điều này, bạn có thể đặt `store=false` trong yêu cầu. Chế độ kiểm soát này tách biệt với tính năng quản lý trạng thái; bạn có thể chọn không lưu trữ cho bất kỳ lượt tương tác nào. Tuy nhiên, xin lưu ý rằng
`store=false` không tương thích với [tính năng thực thi ở chế độ nền](https://ai.google.dev/gemini-api/docs/background-execution?hl=vi) và ngăn việc sử dụng
`previous_interaction_id` cho các lượt tiếp theo.

Đối với các dự án ở Cấp trả phí, bạn có thể định cấu hình khoảng thời gian giữ lại trong
[AI Studio](https://aistudio.google.com/logs?hl=vi) để tự động đánh dấu nhật ký cần
xoá khỏi bộ nhớ dự án sau 7, 14, 28 hoặc 55 ngày. Thời gian giữ lại ngắn hơn có thể ảnh hưởng đến việc truy xuất các cuộc trò chuyện trước đây.

Bạn có thể xoá các lượt tương tác đã lưu trữ bất cứ lúc nào bằng phương thức
[`delete`](https://ai.google.dev/api/interactions-api?hl=vi#deleteInteraction) theo lập trình,
phương thức này yêu cầu mã lượt tương tác. Bạn cũng có thể xem và quản lý nhật ký các lượt tương tác đã lưu trữ, bao gồm cả việc xoá khỏi bộ nhớ dự án, trong
[AI Studio](https://aistudio.google.com/logs?hl=vi).

Sau khi hết thời gian giữ lại, dữ liệu của bạn sẽ tự động bị xoá.

Các đối tượng tương tác được xử lý theo các [điều khoản](https://ai.google.dev/gemini-api/terms?hl=vi).

### Xem các lượt tương tác trong AI Studio

API lưu trữ các yêu cầu Interactions API được thực thi bằng `store=true` cho các dự án ở Cấp trả phí. Bạn có thể xem trực tiếp các yêu cầu này từ trang
[Nhật ký trong Google AI Studio](https://aistudio.google.com/logs?hl=vi). Xem hướng dẫn
[Nhật ký](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=vi) để biết thêm thông tin.

## Các phương pháp hay nhất

- **Tỷ lệ kết quả tìm kiếm trong bộ nhớ cache**: Tính năng lưu vào bộ nhớ đệm ngầm được hỗ trợ ở cả chế độ có trạng thái và
  chế độ không lưu trạng thái (xem phần
  [Bắt đầu nhanh](https://ai.google.dev/gemini-api/docs/get-started?hl=vi#4_multi-turn_conversations)). Việc sử dụng `previous_interaction_id` (có trạng thái) để tiếp tục cuộc trò chuyện cho phép hệ thống dễ dàng sử dụng tính năng lưu vào bộ nhớ đệm ngầm cho nhật ký trò chuyện, giúp cải thiện hiệu suất và giảm chi phí.
- **Kết hợp các lượt tương tác**: Bạn có thể linh hoạt kết hợp các lượt tương tác của Tác nhân và
  Mô hình trong một cuộc trò chuyện. Ví dụ: bạn có thể sử dụng một tác nhân chuyên biệt, chẳng hạn như tác nhân Deep Research, để thu thập dữ liệu ban đầu, sau đó sử dụng mô hình Gemini tiêu chuẩn cho các tác vụ tiếp theo như tóm tắt hoặc định dạng lại, liên kết các bước này với `previous_interaction_id`.

## Các mô hình và tác nhân được hỗ trợ

| Tên mô hình | Loại | Mã kiểu máy |
| --- | --- | --- |
| Gemini 4 Argon | Mô hình | `gemini-4-argon` |
| Gemini 3.8 Flash | Mô hình | `gemini-3.8-flash` |
| Gemini 3.6 Flash | Mô hình | `gemini-3.6-flash` |
| Bản xem trước Gemini 3.1 Pro | Mô hình | `gemini-3.1-pro-preview` |
| Gemini 3.5 Flash-Lite | Mô hình | `gemini-3.5-flash-lite` |
| Gemini 3.1 Flash-Lite | Mô hình | `gemini-3.1-flash-lite` |
| Bản xem trước Gemini 3 Flash | Mô hình | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | Mô hình | `gemini-2.5-pro` |
| Gemini 2.5 Flash | Mô hình | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | Mô hình | `gemini-2.5-flash-lite` |
| Hình ảnh Gemini 3 Pro | Mô hình | `gemini-3-pro-image` |
| Hình ảnh Gemini 3.1 Flash | Mô hình | `gemini-3.1-flash-image` |
| Bản xem trước Gemini 3.1 Flash TTS | Mô hình | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | Mô hình | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | Mô hình | `gemma-4-26b-a4b-it` |
| Lyria 3.5 | Mô hình | `lyria-3.5` |
| Bản xem trước Lyria 3 Clip | Mô hình | `lyria-3-clip-preview` |
| Bản xem trước Lyria 3 Pro | Mô hình | `lyria-3-pro-preview` |
| Bản xem trước Deep Research | Tác nhân | `deep-research-preview-04-2026` |
| Bản xem trước Deep Research | Tác nhân | `deep-research-max-preview-04-2026` |
| Bản xem trước Antigravity | Tác nhân | `antigravity-preview-09-2026` |

## SDK

Bạn có thể sử dụng phiên bản mới nhất của SDK Google GenAI để truy cập vào Interactions API.

- Trên Python, đây là gói `google-genai` từ phiên bản `2.3.0` trở lên.
- Trên JavaScript, đây là gói `@google/genai` từ phiên bản `2.3.0` trở lên.
- Trên Go, đây là gói `google.golang.org/genai`.
- Trên Java, đây là gói `com.google.genai:google-genai`.

Bạn có thể tìm hiểu thêm về cách cài đặt SDK trên trang
[Thư viện](https://ai.google.dev/gemini-api/docs/libraries?hl=vi).

## Các điểm hạn chế

- **MCP từ xa**: Gemini 3 không hỗ trợ MCP từ xa, tính năng này sẽ sớm ra mắt.
- **Khả năng tương thích của mô hình nhiều lượt**: Khi kết hợp các mô hình khác nhau trong một
  cuộc trò chuyện (có trạng thái hoặc không trạng thái), các mô hình tiếp theo phải hỗ trợ
  các phương thức đầu ra của các mô hình trước đó làm dữ liệu đầu vào. Ví dụ: nếu bạn tạo một hình ảnh bằng `gemini-3.1-flash-image`, bạn không thể tiếp tục cuộc trò chuyện đó với một mô hình không chấp nhận dữ liệu đầu vào là hình ảnh (chẳng hạn như mô hình chỉ có văn bản hoặc mô hình tạo nhạc như Lyria).

Các tính năng sau được API
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=vi) hỗ trợ nhưng **chưa có**trong Interactions API:

- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi)**
- **[Tự động gọi hàm (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=vi#automatic_function_calling_python_only)**
- **[Lưu vào bộ nhớ đệm rõ ràng](https://ai.google.dev/gemini-api/docs/caching?hl=vi)**: Xin lưu ý rằng tính năng lưu vào bộ nhớ đệm ngầm ở phía máy chủ có trong Interactions API
  thông qua `previous_interaction_id`.

## Phản hồi

Ý kiến phản hồi của bạn rất quan trọng đối với việc phát triển Interactions API.
Hãy chia sẻ ý kiến, báo cáo lỗi hoặc yêu cầu tính năng trên
[Diễn đàn cộng đồng nhà phát triển AI của Google](https://discuss.ai.google.dev/c/gemini-api/4?hl=vi).

## Bước tiếp theo

- Dùng thử [sổ tay bắt đầu nhanh Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=vi).
- Tìm hiểu thêm về [tác nhân Deep Research của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-15 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-15 UTC."],[],[]]
