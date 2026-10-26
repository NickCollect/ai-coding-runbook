---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=vi
fetched_at: 2026-10-26T05:52:28.788116+00:00
title: "\u0110\u1ed9 ph\u00e2n gi\u1ea3i n\u1ed9i dung nghe nh\u00ecn \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Độ phân giải nội dung nghe nhìn

Tham số `media_resolution` kiểm soát cách Gemini API xử lý dữ liệu đầu vào đa phương tiện như hình ảnh, video, âm thanh và tài liệu PDF bằng cách xác định **số lượng mã thông báo tối đa** được phân bổ cho dữ liệu đầu vào đa phương tiện, cho phép bạn cân bằng chất lượng phản hồi với độ trễ và chi phí. Mặc dù dữ liệu đầu vào bằng hình ảnh và tài liệu sẽ điều chỉnh quy mô phân bổ mã thông báo dựa trên chế độ cài đặt độ phân giải, nhưng dữ liệu đầu vào bằng âm thanh sẽ được mã hoá thành mã thông báo với tốc độ cố định mỗi giây trên tất cả các mức độ phân giải. Đối với
các chế độ cài đặt khác nhau, giá trị mặc định và cách các giá trị này tương ứng với mã thông báo, hãy xem phần
[Số lượng mã thông báo](#token-counts).

Bạn có thể định cấu hình độ phân giải đa phương tiện cho từng đối tượng đa phương tiện (mục nội dung) trong yêu cầu của mình (mô hình Gemini 4 và Gemini 3).

## Độ phân giải đa phương tiện cho từng mục nội dung (mô hình Gemini 4 và Gemini 3)

Mô hình Gemini 4 và Gemini 3 cho phép bạn đặt độ phân giải đa phương tiện cho từng đối tượng đa phương tiện trong yêu cầu của mình, giúp tối ưu hoá việc sử dụng mã thông báo một cách chi tiết. Bạn có thể kết hợp các mức độ phân giải trong một yêu cầu. Ví dụ: sử dụng độ phân giải cao cho một sơ đồ phức tạp và độ phân giải thấp cho một hình ảnh theo ngữ cảnh đơn giản.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Describe the details in this high-resolution image.").build();
Content imageContent =
    ImageContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/image/scones.jpg")
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
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

    uploadedFile, err := client.Files.UploadFromPath(ctx, "path/to/image.jpg", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Describe the details in this high-resolution image.",
                }),
                interactions.NewContent(interactions.ImageContent{
                    URI:        genai.Ptr(uploadedFile.URI),
                    MimeType:   interactions.ImageContentMimeType(uploadedFile.MIMEType).ToPointer(),
                    Resolution: interactions.MediaResolutionHigh.ToPointer(),
                }),
            }),
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
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## Các giá trị độ phân giải hiện có

Gemini API xác định các mức độ sau đây cho độ phân giải đa phương tiện:

- `unspecified`: Chế độ cài đặt mặc định. Số lượng mã thông báo cho mức độ này khác nhau đáng kể giữa Gemini 4/3 và các mô hình Gemini trước đó.
- `low`: Số lượng mã thông báo thấp hơn, giúp xử lý nhanh hơn và chi phí thấp hơn, nhưng ít chi tiết hơn.
- `medium`: Cân bằng giữa chi tiết, chi phí và độ trễ.
- `high`: Số lượng mã thông báo cao hơn, cung cấp nhiều chi tiết hơn để mô hình hoạt động, nhưng độ trễ và chi phí sẽ tăng lên.
- `ultra_high` (Chỉ áp dụng cho từng mục nội dung): Số lượng mã thông báo cao nhất, cần thiết cho các trường hợp sử dụng cụ thể như [sử dụng máy tính](https://ai.google.dev/gemini-api/docs/computer-use?hl=vi).

Xin lưu ý rằng `high` mang lại hiệu suất tối ưu cho hầu hết các trường hợp sử dụng.

Số lượng mã thông báo chính xác được tạo cho từng mức độ này phụ thuộc vào cả **loại phương tiện** (Hình ảnh, Video, Âm thanh, PDF) và **phiên bản mô hình**.

## Số lượng mã thông báo

Các bảng dưới đây tóm tắt số lượng mã thông báo gần đúng cho từng giá trị `media_resolution` và loại phương tiện cho mỗi nhóm mô hình.

**Mô hình Gemini 4 và Gemini 3**

| MediaResolution | Hình ảnh | Video | Âm thanh | PDF |
| --- | --- | --- | --- | --- |
| `unspecified` (Mặc định) | 1120 | 70 | 25 (mỗi giây) | 560 |
| `low` | 280 | 70 | 25 (mỗi giây) | 280 + Văn bản gốc |
| `medium` | 560 | 70 | 25 (mỗi giây) | 560 + Văn bản gốc |
| `high` | 1120 | 280 | 25 (mỗi giây) | 1120 + Văn bản gốc |
| `ultra_high` | 2240 | Không áp dụng | Không áp dụng | Không áp dụng |

## Chọn độ phân giải phù hợp

- **Mặc định (`unspecified`):** Bắt đầu với chế độ mặc định. Chế độ này được điều chỉnh để cân bằng chất lượng, độ trễ và chi phí cho hầu hết các trường hợp sử dụng phổ biến.
- **`low`:** Sử dụng cho các trường hợp mà chi phí và độ trễ là quan trọng nhất, còn chi tiết cụ thể thì ít quan trọng hơn.
- **`medium` / `high`:** Tăng độ phân giải khi nhiệm vụ yêu cầu hiểu các chi tiết phức tạp trong phương tiện. Điều này thường cần thiết cho việc phân tích hình ảnh phức tạp, đọc biểu đồ hoặc hiểu tài liệu dày đặc.
- **`ultra_high`** – Chỉ áp dụng cho chế độ cài đặt từng mục nội dung. Nên dùng cho các trường hợp sử dụng cụ thể như sử dụng máy tính hoặc khi thử nghiệm cho thấy có sự cải thiện rõ rệt so với `high`.
- **Kiểm soát từng mục nội dung (Gemini 4 và Gemini 3):** Tối ưu hoá việc sử dụng mã thông báo. Ví dụ: trong một câu lệnh có nhiều hình ảnh, hãy sử dụng `high` cho một sơ đồ phức tạp và `low` hoặc `medium` cho các hình ảnh theo ngữ cảnh đơn giản hơn.

**Cài đặt đề xuất**

Sau đây là danh sách các chế độ cài đặt độ phân giải đa phương tiện được đề xuất cho từng loại phương tiện được hỗ trợ.

| Loại phương tiện | Chế độ cài đặt đề xuất | Số mã thông báo tối đa | Hướng dẫn sử dụng |
| --- | --- | --- | --- |
| **Hình ảnh** | `high` | 1120 | Nên dùng cho hầu hết các nhiệm vụ phân tích hình ảnh để đảm bảo chất lượng tối đa. |
| **PDF** | `medium` | 560 | Tối ưu cho việc hiểu tài liệu; chất lượng thường đạt đến mức `medium`. Việc tăng lên `high` hiếm khi cải thiện kết quả OCR cho các tài liệu tiêu chuẩn. |
| **Video** (Chung) | `low` (hoặc `medium`) | 70 (mỗi khung hình) | **Lưu ý:** Đối với video, các chế độ cài đặt `low` và `medium` được xử lý giống nhau (70 mã thông báo) để tối ưu hoá việc sử dụng ngữ cảnh. Điều này là đủ cho hầu hết các nhiệm vụ nhận dạng và mô tả hành động. |
| **Video** (Nhiều văn bản) | `high` | 280 (mỗi khung hình) | Chỉ cần thiết khi trường hợp sử dụng liên quan đến việc đọc văn bản dày đặc (OCR) hoặc các chi tiết nhỏ trong khung hình video. |
| **Âm thanh** | `unspecified` (Mặc định) | 25 (mỗi giây) | Âm thanh được mã hoá thành mã thông báo với tốc độ cố định là 25 mã thông báo mỗi giây trên tất cả các chế độ cài đặt độ phân giải được hỗ trợ (`unspecified`, `low`, `medium` và `high`). |

Luôn thử nghiệm và đánh giá tác động của các chế độ cài đặt độ phân giải khác nhau đối với ứng dụng của bạn để tìm ra sự cân bằng tốt nhất giữa chất lượng, độ trễ và chi phí.

## Mối quan hệ với các chế độ xử lý video

Các tham số `media_resolution` và xử lý kiểm soát các khía cạnh khác nhau của dữ liệu đầu vào video:

- `media_resolution` kiểm soát **độ phân giải** của từng khung hình (số lượng mã thông báo trên mỗi khung hình).
- `processing` / `media_processing` kiểm soát **nội dung nào trong video** được tải vào ngữ cảnh.

Bạn có thể đặt cả hai tham số này trên cùng một dữ liệu đầu vào video. Ví dụ: bạn có thể sử dụng tính năng xử lý theo tác nhân với độ phân giải đa phương tiện thấp để giảm thiểu tổng số mã thông báo sử dụng cho một video dài.

Để biết thông tin chi tiết về các chế độ xử lý video, hãy xem hướng dẫn về tính năng hiểu video theo tác nhân .

## Tóm tắt về khả năng tương thích với phiên bản

- **Các mô hình Gemini 4 và Gemini 3 hỗ trợ** việc đặt `resolution` trên từng mục nội dung.

## Các bước tiếp theo

- Tìm hiểu thêm về các tính năng đa phương thức của Gemini API trong các hướng dẫn về
  [tính năng hiểu hình ảnh](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi),
  [hiểu video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=vi), [hiểu âm thanh](https://ai.google.dev/gemini-api/docs/audio?hl=vi),
  và [hiểu tài liệu](https://ai.google.dev/gemini-api/docs/document-processing?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-13 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-13 UTC."],[],[]]
