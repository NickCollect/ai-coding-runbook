---
source_url: https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=vi
fetched_at: 2026-10-05T06:33:49.414064+00:00
title: "Hi\u1ec3u video \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Hiểu video

Gemini Robotics ER 2 có thể theo dõi tiến trình thực hiện nhiệm vụ từ nguồn cấp dữ liệu video liên tục bằng 2 tính năng:

- Tìm khoảnh khắc: xác định dấu thời gian chính xác khi một sự kiện quan trọng xảy ra.
- Phân loại tiến trình: chỉ định mỗi video vào một trong năm nhóm hoàn thành (0–20%, 20–40%, 40–60%, 60–80%, 80–100%).

## Tìm khoảnh khắc

Tính năng tìm khoảnh khắc xác định chính xác khung hình video nơi một sự kiện quan trọng xảy ra, chẳng hạn như khi cốc đầy hoặc khi nút thắt được thắt. Robot sử dụng thông tin này để xác minh thành công, các bước theo trình tự và kích hoạt các bước điều chỉnh.

Câu lệnh ví dụ sau đây yêu cầu mô hình xác định thời điểm hoàn thành một nhiệm vụ nhất định trong video:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

Sau đây là các khung hình mẫu trong một video tìm khoảnh khắc, trong đó mô hình xác định dấu thời gian hoàn thành nhiệm vụ:

![Ví dụ về các khung hình video cho thấy kết quả tìm kiếm khoảnh khắc kèm theo lớp phủ dấu thời gian](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=vi)

## Phân loại tiến độ

Phân loại tiến trình sẽ chỉ định một video vào một trong năm khoảng hoàn thành: 0–20%, 20–40%, 40–60%, 60–80% hoặc 80–100%. Điều này giúp robot nhận biết tình huống theo thời gian thực để chúng có thể điều chỉnh hành động hoặc thử lại các bước không thành công mà không cần khởi động lại toàn bộ quy trình làm việc.

Câu lệnh ví dụ sau đây yêu cầu mô hình phân loại cấp độ tiến trình hiện tại trong một video:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

Sau đây là các khung hình mẫu trong một video phân loại tiến trình, trong đó mô hình chỉ định một khoảng tiến trình:

![Ví dụ về các khung hình video cho thấy kết quả phân loại tiến trình có nhãn dấu ngoặc tiến trình](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=vi)

## Ví dụ

Để xem các ví dụ đầy đủ có thể chạy, bao gồm cả tính năng theo dõi tác vụ nhiều bước, hãy xem [Sổ tay về robot học](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Bước tiếp theo

- [Live API cho robot](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=vi) – truyền trực tuyến hai chiều theo thời gian thực.
- [Điều phối công việc](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=vi) – công việc dài hạn có khả năng suy luận không gian.
- [Tổng quan về Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=vi) – so sánh mô hình và các chức năng.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-09-08 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-09-08 UTC."],[],[]]
