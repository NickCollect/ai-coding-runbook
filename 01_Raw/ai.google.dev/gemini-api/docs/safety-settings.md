---
source_url: https://ai.google.dev/gemini-api/docs/safety-settings?hl=vi
fetched_at: 2026-11-02T07:27:52.949815+00:00
title: "C\u00e0i \u0111\u1eb7t an to\u00e0n \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Cài đặt an toàn

Gemini API cung cấp các chế độ cài đặt an toàn mà bạn có thể điều chỉnh trong giai đoạn tạo mẫu để xác định xem ứng dụng của bạn có cần cấu hình an toàn hạn chế hơn hay ít hạn chế hơn hay không. Bạn có thể điều chỉnh các chế độ cài đặt này trên các danh mục bộ lọc để hạn chế hoặc cho phép một số loại nội dung.

Hướng dẫn này trình bày cách thiết lập chế độ cài đặt an toàn cho một lượt tương tác, điều gì sẽ xảy ra khi nội dung bị chặn, cũng như những danh mục và ngưỡng mà bạn có thể sử dụng.

## Thiết lập chế độ cài đặt an toàn

Truyền một danh sách `safety_settings` khi bạn tạo một lượt tương tác. Mỗi chế độ cài đặt sẽ ghép một danh mục gây hại (`type`) với một ngưỡng chặn (`threshold`).

Ví dụ sau đây đặt danh mục lời nói hận thù (`hate_speech`) thành `block_low_and_above`, chặn mọi nội dung có xác suất thấp hoặc cao hơn là lời nói hận thù:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Some potentially unsafe prompt.",
    safety_settings=[
        {
            "type": "hate_speech",
            "threshold": "block_low_and_above",
        }
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Some potentially unsafe prompt.",
    safety_settings: [
      {
        type: "hate_speech",
        threshold: "block_low_and_above",
      },
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.HarmCategory;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.SafetySetting;
import com.google.genai.gaos.models.interactions.Threshold;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

SafetySetting hateSpeechSafety =
    SafetySetting.builder()
        .type(HarmCategory.HATE_SPEECH)
        .threshold(Threshold.BLOCK_LOW_AND_ABOVE)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Some potentially unsafe prompt."))
        .safetySettings(List.of(hateSpeechSafety))
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
            Input: interactions.NewInteractionsInput("Some potentially unsafe prompt."),
            SafetySettings: []interactions.SafetySetting{
                {
                    Type:      interactions.HarmCategoryHateSpeech,
                    Threshold: interactions.ThresholdBlockLowAndAbove,
                },
            },
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
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Some potentially unsafe prompt.",
    "safety_settings": [
      {"type": "hate_speech", "threshold": "block_low_and_above"}
    ]
  }'
```

Bạn có thể đưa vào một chế độ cài đặt cho mỗi danh mục. Các danh mục mà bạn không thiết lập sẽ sử dụng ngưỡng mặc định là **Tắt** đối với các mô hình Gemini 2.5 trở lên.

## Khi nội dung bị chặn

Nếu một bộ lọc an toàn chặn dữ liệu đầu vào hoặc phản hồi của mô hình, thì lượt tương tác sẽ không thành công và gặp lỗi HTTP `400`. Nội dung bị chặn sẽ không được trả về.

`code` lỗi cho bạn biết lý do yêu cầu bị chặn:

- `safety`: Dữ liệu đầu vào hoặc phản hồi đã bị bộ lọc an toàn chặn.
- `jailbreak`, `prohibited_content` hoặc `blocklist`: Dữ liệu đầu vào đã bị chặn vì lý do đó. `message` lỗi bắt đầu bằng `Input blocked:`.

Ví dụ:

```
{
  "error": {
    "code": "safety",
    "message": "Request blocked due to safety violations (harmful content). Please modify your input and retry."
  }
}
```

Đối với các lượt tương tác ở chế độ nền (`background=true`), `status` của lượt tương tác được
đặt thành `failed` và cùng một `code` và `message` xuất hiện trong danh sách `errors`.
Khi phát trực tuyến, lỗi sẽ xuất hiện dưới dạng sự kiện `error`.

## Bộ lọc an toàn

Các bộ lọc an toàn có thể điều chỉnh của Gemini API bao gồm các danh mục sau:

| Danh mục | Giá trị (API) | Mô tả |
| --- | --- | --- |
| Quấy rối | `harassment` | Nội dung lạm dụng, đe doạ hoặc có ý định bắt nạt, hành hạ hoặc chế giễu. |
| Lời nói hận thù | `hate_speech` | Nội dung cổ xuý bạo lực hoặc kích động hận thù đối với cá nhân hoặc nhóm dựa trên một số thuộc tính. |
| Nội dung khiêu dâm | `sexually_explicit` | Nội dung chứa tài liệu khiêu dâm. |
| Nguy hiểm | `dangerous_content` | Nội dung cổ xuý, tạo điều kiện hoặc cho phép các hoạt động nguy hiểm. |
| Jailbreak | `jailbreak` | Câu lệnh được thiết kế để bỏ qua bộ lọc an toàn. |

Bạn có thể sử dụng các bộ lọc này để điều chỉnh nội dung phù hợp với trường hợp sử dụng của mình. Ví dụ: nếu đang xây dựng đoạn hội thoại trong trò chơi điện tử, bạn có thể cho phép nhiều nội dung được xếp hạng là *Nguy hiểm* do tính chất của trò chơi.

Ngoài các bộ lọc an toàn có thể điều chỉnh, Gemini API còn có các biện pháp bảo vệ tích hợp sẵn đối với các hành vi gây hại cốt lõi, chẳng hạn như nội dung gây nguy hiểm cho sự an toàn của trẻ em.
Các loại hành vi gây hại này luôn bị chặn và không thể điều chỉnh.

## Ngưỡng chặn

Do tính an toàn vốn có của mô hình, các bộ lọc bổ sung sẽ **Tắt** theo mặc định.
Hành vi mặc định của mô hình bao gồm hầu hết các trường hợp sử dụng, vì vậy, bạn chỉ nên điều chỉnh các chế độ cài đặt này nếu ứng dụng của bạn luôn yêu cầu.

Bảng sau đây mô tả các ngưỡng mà bạn có thể thiết lập cho từng danh mục. Ví dụ: nếu bạn đặt **Lời nói hận thù** thành **Chặn một số** (`block_only_high`), thì nội dung có xác suất cao là lời nói hận thù sẽ bị chặn và mọi nội dung có xác suất thấp hơn sẽ được cho phép.

| Ngưỡng (Google AI Studio) | Ngưỡng (API) | Mô tả |
| --- | --- | --- |
| Tắt | `off` | Tắt bộ lọc an toàn |
| Chặn một số | `block_only_high` | Chặn khi có xác suất cao về nội dung không an toàn |
| Chặn một số | `block_medium_and_above` | Chặn khi có xác suất trung bình hoặc cao về nội dung không an toàn |
| Chặn hầu hết | `block_low_and_above` | Chặn khi có xác suất thấp, trung bình hoặc cao về nội dung không an toàn |

### Xác suất so với mức độ nghiêm trọng

Gemini API đánh giá xác suất nội dung không an toàn là cao, trung bình, thấp hoặc không đáng kể. API này chặn nội dung dựa trên xác suất đó, chứ không dựa trên mức độ nghiêm trọng của hành vi gây hại. Một số nội dung có thể có xác suất thấp là không an toàn mặc dù hành vi gây hại có thể nghiêm trọng. Ví dụ: hãy so sánh các câu sau:

1. Robot đã đấm tôi.
2. Robot đã chém tôi.

Câu đầu tiên có thể có xác suất cao hơn là không an toàn, nhưng bạn có thể cho rằng câu thứ hai nghiêm trọng hơn. Hãy kiểm thử cẩn thận để tìm mức chặn hỗ trợ trường hợp sử dụng của bạn đồng thời giảm thiểu tác hại cho người dùng cuối.

## Điều chỉnh chế độ cài đặt an toàn trong Google AI Studio

Nhấp vào **Chế độ cài đặt an toàn** trong phần **Chế độ cài đặt nâng cao** trên bảng điều khiển **Chạy chế độ cài đặt** để mở cửa sổ **Chạy chế độ cài đặt an toàn**. Trong cửa sổ này, bạn có thể sử dụng thanh trượt để điều chỉnh mức lọc nội dung theo từng danh mục an toàn:

![](https://ai.google.dev/static/gemini-api/docs/images/safety_settings_ui.png?hl=vi)

Khi bạn gửi yêu cầu (ví dụ: bằng cách hỏi mô hình một câu hỏi), thông báo
warning **Nội dung bị chặn** sẽ xuất hiện nếu nội dung của yêu cầu
bị chặn. Để xem thêm thông tin chi tiết, hãy di chuột qua văn bản **Nội dung bị chặn** để xem danh mục và xác suất phân loại hành vi gây hại.

## Các bước tiếp theo

- Xem tài liệu tham khảo về API [Tương tác](https://ai.google.dev/api/interactions-api?hl=vi)
  để tìm hiểu thêm về toàn bộ API.
- Xem [hướng dẫn về an toàn](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=vi) để biết tổng quan về các yếu tố cần cân nhắc về an toàn
  khi phát triển bằng mô hình ngôn ngữ lớn (LLM).
- Tìm hiểu thêm về cách đánh giá xác suất so với mức độ nghiêm trọng từ nhóm [Jigsaw](https://developers.perspectiveapi.com/s/about-the-api-score).
- Tìm hiểu thêm về các sản phẩm góp phần vào các giải pháp an toàn như
  [Perspective
  API](https://medium.com/jigsaw/reducing-toxicity-in-large-language-models-with-perspective-api-c31c39b7a4d7).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-15 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-15 UTC."],[],[]]
