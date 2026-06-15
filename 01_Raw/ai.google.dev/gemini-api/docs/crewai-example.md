---
source_url: https://ai.google.dev/gemini-api/docs/crewai-example?hl=vi
fetched_at: 2026-06-15T06:31:17.779767+00:00
title: "Ph\u00e2n t\u00edch d\u1ecbch v\u1ee5 h\u1ed7 tr\u1ee3 kh\u00e1ch h\u00e0ng b\u1eb1ng Gemini v\u00e0 CrewAI \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Phân tích dịch vụ hỗ trợ khách hàng bằng Gemini và CrewAI

[CrewAI](https://docs.crewai.com/introduction) là một khung để điều phối các tác nhân AI tự quản cộng tác nhằm đạt được các mục tiêu phức tạp. Nó cho phép bạn xác định các tác nhân bằng cách chỉ định vai trò, mục tiêu và bối cảnh, sau đó xác định các nhiệm vụ cho các tác nhân đó.

Ví dụ này minh hoạ cách xây dựng một hệ thống đa tác nhân để phân tích dữ liệu hỗ trợ khách hàng nhằm xác định vấn đề và đề xuất các điểm cải tiến quy trình bằng Gemini 3 Flash, tạo một báo cáo dành cho Giám đốc vận hành (COO).

Hướng dẫn này sẽ hướng dẫn bạn cách tạo một "nhóm" gồm các tác nhân AI có thể thực hiện những việc sau:

1. Tìm nạp và phân tích dữ liệu hỗ trợ khách hàng (mô phỏng trong ví dụ này).
2. Xác định các vấn đề tái diễn và nút thắt cổ chai trong quy trình.
3. Đề xuất các điểm cải thiện có thể thực hiện.
4. Tổng hợp các phát hiện thành một báo cáo ngắn gọn phù hợp với COO.

Bạn cần có khoá Gemini API. Nếu chưa có, bạn có thể [tạo một khoá API trong Google AI Studio](https://aistudio.google.com/apikey?hl=vi).

```
pip install "crewai[tools]"
```

Đặt khoá Gemini API làm biến môi trường có tên là `GEMINI_API_KEY`, sau đó định cấu hình CrewAI để sử dụng mô hình Gemini.

```
import os
from crewai import LLM

gemini_api_key = os.getenv("GEMINI_API_KEY")

gemini_llm = LLM(
    model='gemini/gemini-3.5-flash',
    api_key=gemini_api_key,
    temperature=1.0  # Use the Gemini 3 recommended temperature
)
```

## Xác định các thành phần

Xây dựng các ứng dụng CrewAI bằng **Công cụ**, **Tác nhân**, **Nhiệm vụ** và chính **Nhóm**. Các phần sau đây sẽ giải thích từng thành phần này.

### Công cụ

Công cụ là những chức năng mà các đặc vụ có thể dùng để tương tác với thế giới bên ngoài hoặc thực hiện các hành động cụ thể. Tại đây, bạn xác định một công cụ giữ chỗ để mô phỏng việc tìm nạp dữ liệu hỗ trợ khách hàng. Trong một ứng dụng thực tế, bạn sẽ kết nối với cơ sở dữ liệu, API hoặc hệ thống tệp. Để biết thêm thông tin về các công cụ, hãy xem [hướng dẫn về các công cụ CrewAI](https://docs.crewai.com/concepts/tools).

```
from crewai.tools import BaseTool

# Placeholder tool for fetching customer support data
class CustomerSupportDataTool(BaseTool):
    name: str = "Customer Support Data Fetcher"
    description: str = (
      "Fetches recent customer support interactions, tickets, and feedback. "
      "Returns a summary string.")

    def _run(self, argument: str) -> str:
        # In a real scenario, this would query a database or API.
        # For this example, return simulated data.
        print(f"--- Fetching data for query: {argument} ---")
        return (
            """Recent Support Data Summary:
- 50 tickets related to 'login issues'. High resolution time (avg 48h).
- 30 tickets about 'billing discrepancies'. Mostly resolved within 12h.
- 20 tickets on 'feature requests'. Often closed without resolution.
- Frequent feedback mentions 'confusing user interface' for password reset.
- High volume of calls related to 'account verification process'.
- Sentiment analysis shows growing frustration with 'login issues' resolution time.
- Support agent notes indicate difficulty reproducing 'login issues'."""
        )

support_data_tool = CustomerSupportDataTool()
```

### Nhân viên hỗ trợ

Tác nhân là những nhân viên AI riêng lẻ trong nhóm của bạn. Mỗi tác nhân có một `role`, `goal`, `backstory` cụ thể, được chỉ định `llm` và `tools` không bắt buộc. Để biết thêm thông tin về trợ lý ảo, hãy xem [hướng dẫn về trợ lý ảo CrewAI](https://docs.crewai.com/concepts/agents).

```
from crewai import Agent

# Agent 1: Data analyst
data_analyst = Agent(
    role='Customer Support Data Analyst',
    goal='Analyze customer support data to identify trends, recurring issues, and key pain points.',
    backstory=(
        """You are an expert data analyst specializing in customer support operations.
        Your strength lies in identifying patterns and quantifying problems from raw support data."""
    ),
    verbose=True,
    allow_delegation=False,  # This agent focuses on its specific task
    tools=[support_data_tool],  # Assign the data fetching tool
    llm=gemini_llm  # Use the configured Gemini LLM
)

# Agent 2: Process optimizer
process_optimizer = Agent(
    role='Process Optimization Specialist',
    goal='Identify bottlenecks and inefficiencies in current support processes based on the data analysis. Propose actionable improvements.',
    backstory=(
        """You are a specialist in optimizing business processes, particularly in customer support.
        You excel at pinpointing root causes of delays and inefficiencies and suggesting concrete solutions."""
    ),
    verbose=True,
    allow_delegation=False,
    # No tools needed, this agent relies on the context provided by data_analyst.
    llm=gemini_llm
)

# Agent 3: Report writer
report_writer = Agent(
    role='Executive Report Writer',
    goal='Compile the analysis and improvement suggestions into a concise, clear, and actionable report for the COO.',
    backstory=(
        """You are a skilled writer adept at creating executive summaries and reports.
        You focus on clarity, conciseness, and highlighting the most critical information and recommendations for senior leadership."""
    ),
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm
)
```

### Tasks

Các nhiệm vụ xác định những việc cụ thể được giao cho nhân viên hỗ trợ. Mỗi việc cần làm đều có `description`, `expected_output` và được giao cho một `agent`. Theo mặc định, các tác vụ được chạy tuần tự và bao gồm cả bối cảnh của tác vụ trước đó. Để biết thêm thông tin về các tác vụ, hãy xem [hướng dẫn về các tác vụ của CrewAI](https://docs.crewai.com/concepts/tasks).

```
from crewai import Task

# Task 1: Analyze data
analysis_task = Task(
    description=(
        """Fetch and analyze the latest customer support interaction data (tickets, feedback, call logs)
        focusing on the last quarter. Identify the top 3-5 recurring issues, quantify their frequency
        and impact (e.g., resolution time, customer sentiment). Use the Customer Support Data Fetcher tool."""
    ),
    expected_output=(
        """A summary report detailing the key findings from the customer support data analysis, including:
- Top 3-5 recurring issues with frequency.
- Average resolution times for these issues.
- Key customer pain points mentioned in feedback.
- Any notable trends in sentiment or support agent observations."""
    ),
    agent=data_analyst  # Assign task to the data_analyst agent
)

# Task 2: Identify bottlenecks and suggest improvements
optimization_task = Task(
    description=(
        """Based on the data analysis report provided by the Data Analyst, identify the primary bottlenecks
        in the support processes contributing to the identified issues (especially the top recurring ones).
        Propose 2-3 concrete, actionable process improvements to address these bottlenecks.
        Consider potential impact and ease of implementation."""
    ),
    expected_output=(
        """A concise list identifying the main process bottlenecks (e.g., lack of documentation for agents,
        complex escalation path, UI issues) linked to the key problems.
A list of 2-3 specific, actionable recommendations for process improvement
(e.g., update agent knowledge base, simplify password reset UI, implement proactive monitoring)."""
    ),
    agent=process_optimizer  # Assign task to the process_optimizer agent
    # This task implicitly uses the output of analysis_task as context
)

# Task 3: Compile COO report
report_task = Task(
    description=(
        """Compile the findings from the Data Analyst and the recommendations from the Process Optimization Specialist
        into a single, concise executive report for the COO. The report should clearly state:
1. The most critical customer support issues identified (with brief data points).
2. The key process bottlenecks causing these issues.
3. The recommended process improvements.
Ensure the report is easy to understand, focuses on actionable insights, and is formatted professionally."""
    ),
    expected_output=(
        """A well-structured executive report (max 1 page) summarizing the critical support issues,
        underlying process bottlenecks, and clear, actionable recommendations for the COO.
        Use clear headings and bullet points."""
    ),
    agent=report_writer  # Assign task to the report_writer agent
)
```

### Nhóm sản xuất

`Crew` kết hợp các tác nhân và tác vụ, xác định quy trình công việc (chẳng hạn như "tuần tự").

```
from crewai import Crew, Process

support_analysis_crew = Crew(
    agents=[data_analyst, process_optimizer, report_writer],
    tasks=[analysis_task, optimization_task, report_task],
    process=Process.sequential,  # Tasks will run sequentially in the order defined
    verbose=True
)
```

## Run the crew

Cuối cùng, hãy bắt đầu thực thi nhóm bằng mọi thông tin đầu vào cần thiết.

```
# Start the crew's work
print("--- Starting Customer Support Analysis Crew ---")
# The 'inputs' dictionary provides initial context if needed by the first task.
# In this case, the tool simulates data fetching regardless of the input.
result = support_analysis_crew.kickoff(inputs={'data_query': 'last quarter support data'})

print("--- Crew Execution Finished ---")
print("--- Final Report for COO ---")
print(result)
```

Tập lệnh sẽ thực thi. `Data Analyst` sẽ sử dụng công cụ này, `Process
Optimizer` sẽ phân tích các kết quả và `Report Writer` sẽ biên soạn báo cáo cuối cùng, sau đó báo cáo này sẽ được in ra bảng điều khiển. Chế độ cài đặt `verbose=True` sẽ cho thấy quy trình suy nghĩ và hành động chi tiết của từng tác nhân.

Để tìm hiểu thêm về CrewAI, hãy xem [giới thiệu về CrewAI](https://docs.crewai.com/introduction).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-10 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-10 UTC."],[],[]]
