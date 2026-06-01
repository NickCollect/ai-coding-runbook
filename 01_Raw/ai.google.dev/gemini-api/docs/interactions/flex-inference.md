---
source_url: https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=vi
fetched_at: 2026-06-01T06:01:24.415056+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Suy luận linh hoạt

Gemini Flex API là một cấp suy luận giúp giảm 50% chi phí so với mức giá tiêu chuẩn, đổi lại độ trễ thay đổi và khả năng cung cấp tốt nhất có thể. API này được thiết kế cho các khối lượng công việc có độ trễ cao, yêu cầu xử lý đồng bộ nhưng không cần hiệu suất theo thời gian thực của API tiêu chuẩn.

## Cách sử dụng cấp linh hoạt

Để sử dụng cấp linh hoạt, hãy chỉ định `service_tier` là `flex` trong yêu cầu của bạn. Theo mặc định, các yêu cầu sẽ sử dụng cấp tiêu chuẩn nếu bạn bỏ qua trường này.

### Python

```
from google import genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="Analyze this dataset for trends...",
        service_tier='flex'
    )
    print(interaction.output_text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    try {
        const interaction = await client.interactions.create({
            model: 'gemini-3.5-flash',
            input: 'Analyze this dataset for trends...',
            service_tier: 'flex'
        });
        console.log(interaction.output_text);
    } catch (e) {
        console.log(`Flex request failed: ${e}`);
    }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## Cách hoạt động của suy luận linh hoạt

Suy luận linh hoạt của Gemini giúp thu hẹp khoảng cách giữa API tiêu chuẩn và thời gian xử lý 24 giờ
của [API theo nhóm](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi). API này tận dụng công suất tính toán "có thể giảm" ngoài giờ cao điểm để cung cấp một giải pháp tiết kiệm chi phí cho các tác vụ trong nền và quy trình làm việc tuần tự.

| Tính năng | Linh hoạt | Mức độ ưu tiên | Tiêu chuẩn | Theo nhóm |
| --- | --- | --- | --- | --- |
| **Định giá** | Chiết khấu 50% | Cao hơn 75 – 100% so với cấp tiêu chuẩn | Giá đầy đủ | Chiết khấu 50% |
| **Độ trễ** | Phút (mục tiêu 1 – 15 phút) | Thấp (giây) | Giây đến phút | Tối đa 24 giờ |
| **Độ tin cậy** | Tốt nhất có thể (có thể giảm) | Cao (không thể giảm) | Cao / Trung bình cao | Cao (đối với thông lượng) |
| **Giao diện** | Đồng bộ | Đồng bộ | Đồng bộ | Không đồng bộ |

### Lợi ích chính

- **Tiết kiệm chi phí**: Tiết kiệm đáng kể cho các hoạt động đánh giá không chính thức, tác nhân trong nền và làm phong phú dữ liệu.
- **Dễ dàng**: Chỉ cần thêm một tham số vào các yêu cầu hiện có.
- **Quy trình làm việc đồng bộ**: Lý tưởng cho các chuỗi API tuần tự, trong đó yêu cầu tiếp theo phụ thuộc vào kết quả của yêu cầu trước đó, giúp quy trình này linh hoạt hơn so với quy trình theo nhóm đối với các quy trình làm việc theo tác nhân.

### Trường hợp sử dụng

- **Đánh giá ngoại tuyến**: Chạy các bài kiểm thử hồi quy hoặc bảng xếp hạng "LLM-as-a-judge".
- **Tác nhân trong nền**: Các tác vụ tuần tự như cập nhật CRM, xây dựng hồ sơ hoặc kiểm duyệt nội dung, trong đó có thể chấp nhận độ trễ vài phút.
- **Nghiên cứu ràng buộc ngân sách**: Các thí nghiệm học thuật yêu cầu số lượng token lớn trong một ngân sách hạn chế.

### Giới hạn số lượng yêu cầu

Lưu lượng truy cập suy luận linh hoạt được tính vào [giới hạn số lượng yêu cầu](https://aistudio.google.com/rate-limit?hl=vi) chung; API này không
cung cấp giới hạn số lượng yêu cầu mở rộng như [API theo nhóm](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi).

### Công suất có thể giảm

Lưu lượng truy cập linh hoạt được xử lý với mức độ ưu tiên thấp hơn. Nếu lưu lượng truy cập tiêu chuẩn tăng đột biến, các yêu cầu linh hoạt có thể bị ưu tiên hoặc bị loại bỏ để đảm bảo công suất cho người dùng có mức độ ưu tiên cao. Nếu bạn đang tìm kiếm suy luận có mức độ ưu tiên cao, hãy xem phần
[Suy luận có mức độ ưu tiên cao](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=vi)

### Mã lỗi

Khi không có công suất linh hoạt hoặc hệ thống bị tắc nghẽn, API sẽ trả về mã lỗi tiêu chuẩn:

- **503 Không có dịch vụ**: Hệ thống hiện đang hoạt động hết công suất.
- **429 Quá nhiều yêu cầu**: Giới hạn số lượng yêu cầu hoặc hết tài nguyên.

### Trách nhiệm của ứng dụng

- **Không có phương án dự phòng phía máy chủ**: Để tránh các khoản phí không mong muốn, hệ thống sẽ không
  tự động nâng cấp yêu cầu linh hoạt lên cấp tiêu chuẩn nếu công suất linh hoạt đã
  đầy.
- **Thử lại**: Bạn phải triển khai logic thử lại phía máy khách của riêng mình với
  thuật toán đợi luỹ tuyến.
- **Thời gian chờ**: Vì các yêu cầu linh hoạt có thể nằm trong hàng đợi, bạn nên tăng thời gian chờ phía máy khách lên 10 phút trở lên để tránh đóng kết nối sớm.

## Điều chỉnh khoảng thời gian chờ

Bạn có thể định cấu hình thời gian chờ cho từng yêu cầu đối với API REST và thư viện ứng dụng.
Luôn đảm bảo thời gian chờ phía máy khách bao gồm khoảng thời gian chờ dự kiến của máy chủ (ví dụ: 600 giây trở lên đối với hàng đợi chờ linh hoạt). SDK dự kiến các giá trị thời gian chờ tính bằng mili giây.

### Thời gian chờ cho từng yêu cầu

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="why is the sky blue?",
        service_tier="flex",
    )
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    try {
        const interaction = await client.interactions.create({
            model: "gemini-3.5-flash",
            input: "why is the sky blue?",
            service_tier: "flex",
        }, {timeout: 900000});
    } catch (e) {
        console.log(`Flex request failed: ${e}`);
    }
}

await main();
```

## Triển khai tính năng thử lại

Vì cấp linh hoạt có thể giảm và gặp lỗi 503, nên bạn có thể triển khai logic thử lại để tiếp tục với các yêu cầu không thành công:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.5-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.5-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.5-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.5-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

## Định giá

Suy luận linh hoạt được định giá bằng 50% [API tiêu chuẩn](https://ai.google.dev/gemini-api/docs/pricing?hl=vi)
và được tính phí theo mã thông báo.

## Mô hình được hỗ trợ

Các mô hình sau đây hỗ trợ suy luận linh hoạt:

| Mô hình | Suy luận linh hoạt |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=vi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=vi) | ✔️ |
| [Gemini 3.1 Pro (Bản dùng thử)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=vi) | ✔️ |
| [Gemini 3 Flash (Bản dùng thử)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=vi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=vi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=vi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=vi) | ✔️ |

## Bước tiếp theo

- [Suy luận có mức độ ưu tiên](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=vi) để có độ trễ thấp nhất.
- [Mã thông báo](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=vi): Tìm hiểu về mã thông báo.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-28 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-28 UTC."],[],[]]
