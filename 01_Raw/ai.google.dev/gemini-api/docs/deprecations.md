---
source_url: https://ai.google.dev/gemini-api/docs/deprecations?hl=vi
fetched_at: 2026-11-02T07:29:16.759427+00:00
title: "C\u00e1c t\u00ednh n\u0103ng kh\u00f4ng d\u00f9ng n\u1eefa c\u1ee7a Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Các tính năng không dùng nữa của Gemini

Trang này liệt kê lịch trình ngừng sử dụng đã biết đối với các mô hình [ổn định (GA)](https://ai.google.dev/gemini-api/docs/models?hl=vi#stable) và [bản xem trước](https://ai.google.dev/gemini-api/docs/models?hl=vi#preview), cũng như đối với API tác nhân được quản lý trong Gemini. "**Ngừng cung cấp**" là thông báo rằng chúng tôi không còn hỗ trợ một mô hình nữa và mô hình đó sẽ bị "**ngừng hoạt động**" trong tương lai gần. Sau khi một mô hình "**tắt**", mô hình đó sẽ tắt hoàn toàn và điểm cuối không còn hoạt động nữa.

Thông báo ngừng hoạt động được đưa ra trên trang [Ghi chú phát hành](https://ai.google.dev/gemini-api/docs/changelog?hl=vi) và ngày ngừng hoạt động sớm nhất được thông báo sẽ được theo dõi trên trang này.
Các mô hình đã tắt sẽ có nền màu xám.

## Mô hình Gemini 3

| **Mô hình** | **Ngày phát hành** | **Ngày ngừng hoạt động** | **Thay thế được đề xuất** |
| --- | --- | --- | --- |
| `gemini-3.8-flash-tts` | Ngày 22 tháng 9 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-3.8-flash-lite-tts` | Ngày 22 tháng 9 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-3.8-live` | Ngày 15 tháng 9 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-3.8-live-extended-thinking` | Ngày 15 tháng 9 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-3.8-flash` | Ngày 2 tháng 9 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-3.7-flash` | Ngày 13 tháng 8 năm 2026 | Không áp dụng | `gemini-3.8-flash` (không thể chọn trong Google AI Studio; điểm cuối này không ngừng hoạt động và tự động định tuyến các yêu cầu API đến `gemini-3.8-flash`) |
| `gemini-3.6-flash` | 21/7/2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-3.5-flash-lite` | 21/7/2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-3.5-flash` | Ngày 19 tháng 5 năm 2026 | Không áp dụng | `gemini-3.6-flash` (không thể chọn trong Google AI Studio; điểm cuối không ngừng hoạt động và tự động định tuyến các yêu cầu API đến `gemini-3.6-flash`) |
| `gemini-3.1-flash-lite` | Ngày 7 tháng 5 năm 2026 | Ngày 7 tháng 5 năm 2027 | `gemini-3.5-flash-lite` |
| Xem trước mẫu | | | |
| `gemini-3.1-flash-tts-preview` | Ngày 26 tháng 2 năm 2026 | Ngày 17 tháng 11 năm 2026 | `gemini-3.8-flash-tts` hoặc `gemini-3.8-flash-lite-tts` |
| `gemini-3.1-pro-preview` | Ngày 19 tháng 2 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-3-flash-preview` | Ngày 17 tháng 12 năm 2025 | Chưa công bố ngày ngừng hoạt động | `gemini-3.6-flash` |
| `gemini-3-pro-preview` | Ngày 18 tháng 11 năm 2025 | Ngày 9 tháng 3 năm 2026 | `gemini-3.1-pro-preview` |
| `gemini-3.1-flash-lite-preview` | Ngày 3 tháng 3 năm 2026 | Ngày 25 tháng 5 năm 2026 | `gemini-3.1-flash-lite` |

## Các mô hình Gemini 2.5 Pro

| **Mô hình** | **Ngày phát hành** | **Ngày ngừng hoạt động** | **Sản phẩm thay thế nên dùng** |
| --- | --- | --- | --- |
| `gemini-2.5-pro` | Ngày 17 tháng 6 năm 2025 | Chưa công bố ngày ngừng hoạt động |  |
| Xem trước mẫu | | | |
| `gemini-2.5-computer-use-preview-10-2025` | Ngày 7 tháng 10 năm 2025 | Ngày 28 tháng 7 năm 2026 | `gemini-3.8-flash` |
| `gemini-2.5-pro-preview-03-25` | Ngày 3 tháng 3 năm 2025 | Ngày 2 tháng 12 năm 2025 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-05-06` | Ngày 6 tháng 5 năm 2025 | Ngày 2 tháng 12 năm 2025 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-06-05` | Ngày 5 tháng 6 năm 2025 | Ngày 2 tháng 12 năm 2025 | `gemini-3.1-pro-preview` |

## Mô hình Gemini 2.5 Flash

| **Mô hình** | **Ngày phát hành** | **Ngày ngừng hoạt động** | **Sản phẩm thay thế nên dùng** |
| --- | --- | --- | --- |
| `gemini-2.5-flash` | Ngày 17 tháng 6 năm 2025 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-2.5-flash-lite` | Ngày 22 tháng 7 năm 2025 | Chưa công bố ngày ngừng hoạt động |  |
| Xem trước mẫu | | | |
| `gemini-2.5-flash-lite-preview-09-2025` | Ngày 25 tháng 9 năm 2025 | Ngày 31 tháng 3 năm 2026 | `gemini-3.1-flash-lite` |
| `gemini-2.5-flash-preview-05-20` | Ngày 20 tháng 5 năm 2025 | Ngày 18 tháng 11 năm 2025 | `gemini-3.6-flash` |
| `gemini-2.5-flash-preview-09-25` | Ngày 25 tháng 9 năm 2025 | Ngày 17 tháng 2 năm 2026 | `gemini-3.6-flash` |

## Các mô hình Gemini 2.0

| **Mô hình** | **Ngày phát hành** | **Ngày ngừng hoạt động** | **Thay thế được đề xuất** |
| --- | --- | --- | --- |
| `gemini-2.0-flash` | Ngày 5 tháng 2 năm 2025 | Ngày 1 tháng 6 năm 2026 | `gemini-3.6-flash` |
| `gemini-2.0-flash-001` | Ngày 5 tháng 2 năm 2025 | Ngày 1 tháng 6 năm 2026 | `gemini-3.6-flash` |
| `gemini-2.0-flash-lite` | Ngày 25 tháng 2 năm 2025 | Ngày 1 tháng 6 năm 2026 | `gemini-3.1-flash-lite` |
| `gemini-2.0-flash-lite-001` | Ngày 25 tháng 2 năm 2025 | Ngày 1 tháng 6 năm 2026 | `gemini-3.1-flash-lite` |
| Xem trước mẫu | | | |
| `gemini-2.0-flash-lite-preview` | Ngày 5 tháng 2 năm 2025 | Ngày 9 tháng 12 năm 2025 | `gemini-3.1-flash-lite` |
| `gemini-2.0-flash-lite-preview-02-05` | Ngày 5 tháng 2 năm 2025 | Ngày 9 tháng 12 năm 2025 | `gemini-3.1-flash-lite` |

## Mô hình Live API

| **Mô hình** | **Ngày phát hành** | **Ngày ngừng hoạt động** | **Sản phẩm thay thế được đề xuất** |
| --- | --- | --- | --- |
| `gemini-3.8-live` | Ngày 15 tháng 9 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-3.8-live-extended-thinking` | Ngày 15 tháng 9 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-3.5-transcribe-live` | Tháng 8 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-2.0-flash-live-001` | Ngày 9 tháng 4 năm 2025 | Ngày 9 tháng 12 năm 2025 | `gemini-3.8-live` |
| Xem trước mẫu | | | |
| `gemini-3.5-live-translate-preview` | Tháng 6 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-3.1-flash-live-preview` | Ngày 11 tháng 3 năm 2026 | Ngày 17 tháng 11 năm 2026 | `gemini-3.8-live` |
| `gemini-2.5-flash-native-audio-preview-12-2025` | Ngày 12 tháng 12 năm 2025 | Ngày 17 tháng 11 năm 2026 | `gemini-3.8-live` |
| `gemini-live-2.5-flash-preview` | Ngày 17 tháng 6 năm 2025 | Ngày 9 tháng 12 năm 2025 | `gemini-3.8-live` |

## Mô hình âm thanh

| **Mô hình** | **Ngày phát hành** | **Ngày ngừng hoạt động** | **Sản phẩm thay thế được đề xuất** |
| --- | --- | --- | --- |
| `gemini-3.5-transcribe` | Tháng 8 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| Xem trước mẫu | | | |
| `gemini-2.5-flash-preview-tts` | Ngày 20 tháng 5 năm 2025 | Ngày 17 tháng 11 năm 2026 | `gemini-3.8-flash-tts` hoặc `gemini-3.8-flash-lite-tts` |
| `gemini-2.5-pro-preview-tts` | Ngày 20 tháng 5 năm 2025 | Ngày 17 tháng 11 năm 2026 | `gemini-3.8-flash-tts` hoặc `gemini-3.8-flash-lite-tts` |

## Mô hình nhúng

| **Mô hình** | **Ngày phát hành** | **Ngày ngừng hoạt động** | **Thay thế được đề xuất** |
| --- | --- | --- | --- |
| `gemini-embedding-2` | Ngày 22 tháng 4 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-embedding-001` | Ngày 14 tháng 7 năm 2025 | Ngày 14 tháng 5 năm 2028 | `gemini-embedding-2` |
| `text-embedding-004` | Ngày 9 tháng 4 năm 2024 | Ngày 14 tháng 1 năm 2026 | `gemini-embedding-2` |
| Xem trước mẫu | | | |
| `embedding-2-preview` | Ngày 10 tháng 3 năm 2026 | Ngày 10 tháng 8 năm 2026 | `gemini-embedding-2` |
| `embedding-001` | Ngày 9 tháng 4 năm 2024 | Ngày 30 tháng 10 năm 2025 | `gemini-embedding-2` |
| `embedding-gecko-001` |  | Ngày 30 tháng 10 năm 2025 | `gemini-embedding-2` |
| `gemini-embedding-exp` |  | Ngày 30 tháng 10 năm 2025 | `gemini-embedding-2` |
| `gemini-embedding-exp-03-07` |  | Ngày 30 tháng 10 năm 2025 | `gemini-embedding-2` |

## Mô hình Nano Banana

| **Mô hình** | **Ngày phát hành** | **Ngày ngừng hoạt động** | **Thay thế được đề xuất** |
| --- | --- | --- | --- |
| `gemini-nano-banana-2.1` | Ngày 6 tháng 10 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-3.1-flash-lite-image` | Ngày 30 tháng 6 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-3.1-flash-image` | Ngày 28 tháng 5 năm 2026 | Chưa công bố ngày ngừng hoạt động | `gemini-nano-banana-2.1` |
| `gemini-3-pro-image` | Ngày 28 tháng 5 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-2.5-flash-image` | Ngày 2 tháng 10 năm 2025 | Ngày 15 tháng 3 năm 2027 | `gemini-3.1-flash-lite-image` |
| Xem trước mẫu | | | |
| `gemini-3.1-flash-image-preview` | Ngày 26 tháng 2 năm 2026 | Ngày 25 tháng 6 năm 2026 | `gemini-nano-banana-2.1` |
| `gemini-3-pro-image-preview` | Ngày 20 tháng 11 năm 2025 | Ngày 25 tháng 6 năm 2026 | `gemini-3-pro-image` |
| `gemini-2.5-flash-image-preview` | Ngày 7 tháng 5 năm 2025 | Ngày 15 tháng 1 năm 2026 | `gemini-nano-banana-2.1` |
| `gemini-2.0-flash-preview-image-generation` | Ngày 7 tháng 5 năm 2025 | Ngày 14 tháng 11 năm 2025 | `gemini-nano-banana-2.1` |

## Mô hình Imagen

| **Mô hình** | **Ngày phát hành** | **Ngày ngừng hoạt động** | **Thay thế được đề xuất** |
| --- | --- | --- | --- |
| `imagen-4.0-generate-001` | Ngày 24 tháng 6 năm 2025 | Ngày 17 tháng 8 năm 2026 | `gemini-nano-banana-2.1` |
| `imagen-4.0-ultra-generate-001` | Ngày 24 tháng 6 năm 2025 | Ngày 17 tháng 8 năm 2026 | `gemini-nano-banana-2.1` |
| `imagen-4.0-fast-generate-001` | Ngày 24 tháng 6 năm 2025 | Ngày 17 tháng 8 năm 2026 | `gemini-nano-banana-2.1` |
| `imagen-3.0-generate-002` | Ngày 6 tháng 2 năm 2025 | Ngày 10 tháng 11 năm 2025 | `gemini-nano-banana-2.1` |
| Xem trước mẫu | | | |
| `imagen-4.0-generate-preview-06-06` | Ngày 24 tháng 6 năm 2025 | Ngày 17 tháng 2 năm 2026 | `gemini-nano-banana-2.1` |
| `imagen-4.0-ultra-generate-preview-06-06` | Ngày 24 tháng 6 năm 2025 | Ngày 17 tháng 2 năm 2026 | `gemini-nano-banana-2.1` |

## mô hình Veo

| **Mô hình** | **Ngày phát hành** | **Ngày ngừng hoạt động** | **Sản phẩm thay thế được đề xuất** |
| --- | --- | --- | --- |
| `veo-3.0-generate-001` | Ngày 9 tháng 9 năm 2025 | Ngày 30 tháng 6 năm 2026 | `gemini-omni-1.1-flash` hoặc các mô hình GA trên [Nền tảng tác nhân Gemini Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=vi) |
| `veo-3.0-fast-generate-001` | Ngày 9 tháng 9 năm 2025 | Ngày 30 tháng 6 năm 2026 | `gemini-omni-1.1-flash` hoặc các mô hình GA trên [Nền tảng tác nhân Gemini Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=vi) |
| `veo-2.0-generate-001` | Ngày 9 tháng 4 năm 2025 | Ngày 30 tháng 6 năm 2026 | `gemini-omni-1.1-flash` hoặc các mô hình GA trên [Nền tảng tác nhân Gemini Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=vi) |
| Xem trước mẫu | | | |
| `veo-3.1-lite-generate-preview` | Ngày 31 tháng 3 năm 2026 | Ngày 22 tháng 10 năm 2026 | `gemini-omni-1.1-flash` |
| `veo-3.1-generate-preview` | Ngày 15 tháng 10 năm 2025 | Ngày 22 tháng 10 năm 2026 | `gemini-omni-1.1-flash` |
| `veo-3.1-fast-generate-preview` | Ngày 15 tháng 10 năm 2025 | Ngày 22 tháng 10 năm 2026 | `gemini-omni-1.1-flash` |
| `veo-3.0-generate-preview` | Ngày 31 tháng 7 năm 2025 | Ngày 12 tháng 11 năm 2025 | `gemini-omni-1.1-flash` |
| `veo-3.0-fast-generate-preview` | Ngày 31 tháng 7 năm 2025 | Ngày 12 tháng 11 năm 2025 | `gemini-omni-1.1-flash` |

## Mô hình Gemini Omni Flash

| **Mô hình** | **Ngày phát hành** | **Ngày ngừng hoạt động** | **Sản phẩm thay thế được đề xuất** |
| --- | --- | --- | --- |
| `gemini-omni-1.1-flash` | Ngày 27 tháng 8 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| Xem trước mẫu | | | |
| `gemini-omni-flash-preview` | Ngày 30 tháng 6 năm 2026 | Ngày 22 tháng 10 năm 2026 | `gemini-omni-1.1-flash` |

## mô hình Lyria

| **Mô hình** | **Ngày phát hành** | **Ngày ngừng hoạt động** | **Sản phẩm thay thế được đề xuất** |
| --- | --- | --- | --- |
| `lyria-3.5` | Ngày 3 tháng 9 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| Xem trước mẫu | | | |
| `lyria-3-clip-preview` | Ngày 25 tháng 3 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `lyria-3-pro-preview` | Ngày 25 tháng 3 năm 2026 | Chưa công bố ngày ngừng hoạt động | `lyria-3.5` |
| `lyria-realtime-exp` | Ngày 20 tháng 5 năm 2025 | Chưa công bố ngày ngừng hoạt động |  |

## Mô hình người máy

| **Mô hình** | **Ngày phát hành** | **Ngày ngừng hoạt động** | **Sản phẩm thay thế nên dùng** |
| --- | --- | --- | --- |
| Xem trước mẫu | | | |
| `gemini-robotics-er-2-preview` | Ngày 30 tháng 7 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-robotics-er-2-streaming-preview` | Ngày 30 tháng 7 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `gemini-robotics-er-1.6-preview` | Ngày 14 tháng 4 năm 2026 | Ngày 31 tháng 8 năm 2026 | `gemini-robotics-er-2-preview` |
| `gemini-robotics-er-1.5-preview` | Ngày 25 tháng 9 năm 2025 | Ngày 30 tháng 4 năm 2026 | `gemini-robotics-er-2-preview` |

## Tác nhân được quản lý

| **Tác nhân** | **Ngày phát hành** | **Ngày ngừng hoạt động** | **Thay thế được đề xuất** |
| --- | --- | --- | --- |
| Xem trước tác nhân | | | |
| `antigravity-preview-09-2026` | Ngày 17 tháng 9 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `deep-research-preview-04-2026` | Ngày 21 tháng 4 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `deep-research-max-preview-04-2026` | Ngày 21 tháng 4 năm 2026 | Chưa công bố ngày ngừng hoạt động |  |
| `deep-research-pro-preview-12-2025` | Ngày 11 tháng 12 năm 2025 | Ngày 23 tháng 10 năm 2026 | `deep-research-preview-04-2026` |
| `antigravity-preview-05-2026` | Ngày 19 tháng 5 năm 2026 | Ngày 5 tháng 10 năm 2026 | `antigravity-preview-09-2026` |

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-22 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-22 UTC."],[],[]]
