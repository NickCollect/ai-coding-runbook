---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=vi
fetched_at: 2026-05-05T20:08:07.577924+00:00
title: "Suy lu\u1eadn m\u1ee9c \u0111\u1ed9 \u01b0u ti\u00ean \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Suy luận mức độ ưu tiên

Gemini Priority API là một cấp suy luận cao cấp được thiết kế cho các khối lượng công việc quan trọng đối với doanh nghiệp, đòi hỏi độ trễ thấp và độ tin cậy cao nhất với mức giá cao cấp. Lưu lượng truy cập ở cấp ưu tiên được ưu tiên hơn lưu lượng truy cập ở cấp API tiêu chuẩn và cấp linh hoạt.

Tính năng suy luận mức độ ưu tiên được cung cấp cho người dùng [Cấp 2 và Cấp 3](https://ai.google.dev/gemini-api/docs/billing?hl=vi#about-billing) trên các điểm cuối GenerateContent API và Interactions API.

## Cách sử dụng Mức độ ưu tiên

Để sử dụng Cấp ưu tiên, hãy đặt trường `service_tier` trong nội dung yêu cầu thành `priority`. Cấp mặc định là cấp tiêu chuẩn nếu bạn bỏ qua trường này.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3-flash-preview",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## Cách hoạt động của tính năng Suy luận mức độ ưu tiên

Các tuyến suy luận ưu tiên sẽ định tuyến các yêu cầu đến các hàng đợi điện toán có mức độ quan trọng cao, mang lại hiệu suất nhanh chóng và có thể dự đoán được cho các ứng dụng dành cho người dùng. Cơ chế chính của tính năng này là giảm cấp phía máy chủ một cách hợp lý xuống quy trình xử lý tiêu chuẩn cho lưu lượng truy cập vượt quá giới hạn động, đảm bảo tính ổn định của ứng dụng thay vì làm cho yêu cầu không thành công.

| Tính năng | Mức độ ưu tiên | Tiêu chuẩn | Gập | Theo nhóm |
| --- | --- | --- | --- | --- |
| **Định giá** | Cao hơn 75 – 100% so với gói Standard | Giá đầy đủ | Giảm giá 50% | Giảm giá 50% |
| **Độ trễ** | Giây | Giây sang phút | Phút (mục tiêu 1 – 15 phút) | Tối đa 24 giờ |
| **Độ tin cậy** | Cao (Không rụng lông) | Cao / Cao vừa | Nỗ lực tối đa (Có thể loại bỏ) | Cao (đối với thông lượng) |
| **Giao diện** | Đồng bộ | Đồng bộ | Đồng bộ | Không đồng bộ |

### Lợi ích chính

- **Độ trễ thấp**: Được thiết kế để có thời gian phản hồi dưới một giây cho các công cụ AI tương tác, hướng đến người dùng.
- **Độ tin cậy cao**: Lưu lượng truy cập được xử lý với mức độ quan trọng cao nhất và hoàn toàn không thể loại bỏ.
- **Xuống cấp nhẹ**: Các đợt tăng đột biến lưu lượng truy cập vượt quá hạn mức linh hoạt sẽ tự động được hạ cấp xuống cấp độ Tiêu chuẩn để xử lý thay vì thất bại, ngăn chặn tình trạng ngừng dịch vụ.
- **Ít rắc rối**: Sử dụng cùng một phương thức `generateContent` đồng bộ như các cấp tiêu chuẩn và linh hoạt.

### Trường hợp sử dụng

Xử lý ưu tiên là lựa chọn lý tưởng cho các quy trình quan trọng đối với doanh nghiệp, trong đó hiệu suất và độ tin cậy là yếu tố tối quan trọng.

- **Các ứng dụng AI tương tác**: Chatbot và trợ lý dịch vụ khách hàng mà người dùng trả phí cao và mong đợi câu trả lời nhanh chóng, nhất quán.
- **Công cụ đưa ra quyết định theo thời gian thực**: Hệ thống yêu cầu kết quả có độ tin cậy cao và độ trễ thấp, chẳng hạn như phân loại vé trực tiếp hoặc phát hiện hành vi gian lận.
- **Các tính năng dành cho khách hàng cao cấp**: Nhà phát triển cần đảm bảo mục tiêu mức độ dịch vụ (SLO) cao hơn cho khách hàng trả phí.

### Giới hạn số lượng yêu cầu

Mức sử dụng ưu tiên có giới hạn tốc độ riêng, mặc dù mức sử dụng được tính vào [giới hạn tốc độ lưu lượng truy cập tương tác tổng thể](https://aistudio.google.com/rate-limit?hl=vi). Giới hạn tốc độ mặc định cho suy luận Ưu tiên là **giới hạn tốc độ tiêu chuẩn 0,3x cho Mô hình / Cấp**

### Logic hạ cấp từng bước

Nếu vượt quá giới hạn Ưu tiên do tình trạng tắc nghẽn, thì các yêu cầu vượt quá sẽ được **tự động và hạ cấp một cách suôn sẻ** xuống mức xử lý Chuẩn thay vì gặp lỗi 503 hoặc 429. Các yêu cầu bị hạ cấp sẽ được tính phí theo mức giá tiêu chuẩn, chứ không phải mức giá ưu tiên cao cấp.

### Trách nhiệm của khách hàng

- **Giám sát phản hồi**: Nhà phát triển nên giám sát tiêu đề `x-gemini-service-tier` trong phản hồi API để phát hiện xem các yêu cầu có thường xuyên bị hạ cấp xuống `standard` hay không.
- **Thử lại**: Ứng dụng phải triển khai logic thử lại/thuật toán đợi luỹ tiến cho các lỗi tiêu chuẩn, chẳng hạn như `DEADLINE_EXCEEDED`.

## Giá

Suy luận ưu tiên có giá cao hơn 75 – 100% so với [API tiêu chuẩn](https://ai.google.dev/gemini-api/docs/pricing?hl=vi) và được tính phí theo token.

## Mô hình được hỗ trợ

Các mô hình sau đây hỗ trợ tính năng Suy luận ưu tiên:

| Mô hình | Suy luận mức độ ưu tiên |
| --- | --- |
| [Bản xem trước Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=vi) | ✔️ |
| [Bản dùng thử Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=vi) | ✔️ |
| [Bản dùng thử Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=vi) | ✔️ |
| [Bản xem trước hình ảnh của Gemini 3 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=vi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=vi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=vi) | ✔️ |
| [Hình ảnh Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=vi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=vi) | ✔️ |

## Bước tiếp theo

Đọc về các lựa chọn [suy luận và tối ưu hoá](https://ai.google.dev/gemini-api/docs/optimization?hl=vi) khác của Gemini:

- [Suy luận linh hoạt](https://ai.google.dev/gemini-api/docs/flex-inference?hl=vi) giúp giảm 50% chi phí.
- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi) để xử lý không đồng bộ trong vòng 24 giờ.
- [Lưu vào bộ nhớ đệm theo bối cảnh](https://ai.google.dev/gemini-api/docs/caching?hl=vi) để giảm chi phí mã thông báo đầu vào.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
