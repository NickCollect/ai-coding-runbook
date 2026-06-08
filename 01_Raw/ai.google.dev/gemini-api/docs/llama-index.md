---
source_url: https://ai.google.dev/gemini-api/docs/llama-index?hl=vi
fetched_at: 2026-06-08T05:39:32.298659+00:00
title: "T\u00e1c nh\u00e2n nghi\u00ean c\u1ee9u b\u1eb1ng Gemini v\u00e0 LlamaIndex \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tác nhân nghiên cứu bằng Gemini và LlamaIndex

LlamaIndex là một khung để xây dựng các tác nhân tri thức bằng cách sử dụng các mô hình ngôn ngữ lớn (LLM) được kết nối với dữ liệu của bạn. Ví dụ này cho bạn thấy cách xây dựng quy trình công việc nhiều tác nhân cho Tác nhân nghiên cứu. Trong LlamaIndex, [`Workflows`](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)
là các khối xây dựng của hệ thống tác nhân và nhiều tác nhân.

Bạn cần có khoá Gemini API. Nếu chưa có, bạn có thể
[lấy khoá này trong Google AI Studio](https://aistudio.google.com/app/apikey?hl=vi).
Trước tiên, hãy cài đặt tất cả các thư viện LlamaIndex cần thiết. LlamaIndex sử dụng gói `google-genai` nâng cao.

```
pip install llama-index llama-index-utils-workflow llama-index-llms-google-genai llama-index-tools-google
```

## Thiết lập Gemini trong LlamaIndex

Công cụ của bất kỳ tác nhân LlamaIndex nào cũng là một LLM (mô hình ngôn ngữ lớn) xử lý quá trình suy luận và xử lý văn bản. Ví dụ này sử dụng Gemini 3 Flash. Hãy nhớ [đặt khoá API làm
biến môi trường](https://ai.google.dev/gemini-api/docs/api-key?hl=vi).

```
import os
from llama_index.llms.google_genai import GoogleGenAI

# Set your API key in the environment elsewhere, or with os.environ['GEMINI_API_KEY'] = '...'
assert 'GEMINI_API_KEY' in os.environ

llm = GoogleGenAI(model="gemini-3.5-flash")
```

## Công cụ xây dựng

Các tác nhân sử dụng công cụ để tương tác với thế giới bên ngoài, chẳng hạn như tìm kiếm trên web hoặc lưu trữ thông tin. [Các công cụ trong LlamaIndex](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/)
có thể là các hàm Python thông thường hoặc được nhập từ `ToolSpecs`.
Gemini đi kèm với một công cụ tích hợp để sử dụng Google Tìm kiếm, được sử dụng ở đây.

```
from google.genai import types

google_search_tool = types.Tool(
    google_search=types.GoogleSearch()
)

llm_with_search = GoogleGenAI(
    model="gemini-3.5-flash",
    generation_config=types.GenerateContentConfig(tools=[google_search_tool])
)
```

Bây giờ, hãy kiểm thử thực thể LLM bằng một truy vấn yêu cầu tìm kiếm. Hướng dẫn này giả định một vòng lặp sự kiện đang chạy (chẳng hạn như `python -m asyncio` hoặc Google Colab).

```
response = await llm_with_search.acomplete("What's the weather like today in Biarritz?")
print(response)
```

Tác nhân nghiên cứu sẽ sử dụng các hàm Python làm công cụ. Có rất nhiều cách để bạn xây dựng một hệ thống thực hiện tác vụ này. Trong ví dụ này, bạn sẽ sử dụng những nội dung sau:

1. `search_web` sử dụng Gemini với Google Tìm kiếm để tìm kiếm thông tin trên web về chủ đề đã cho.
2. `record_notes` lưu kết quả nghiên cứu tìm thấy trên web vào trạng thái để các công cụ khác có thể sử dụng.
3. `write_report` viết báo cáo bằng thông tin do `ResearchAgent` tìm thấy
4. `review_report` xem xét báo cáo và đưa ra ý kiến phản hồi.

Lớp `Context` chuyển trạng thái giữa các tác nhân/công cụ và mỗi tác nhân sẽ có quyền truy cập vào trạng thái hiện tại của hệ thống.

```
from llama_index.core.workflow import Context

async def search_web(ctx: Context, query: str) -> str:
    """Useful for searching the web about a specific query or topic"""
    response = await llm_with_search.acomplete(f"""Please research given this query or topic,
    and return the result\n<query_or_topic>{query}</query_or_topic>""")
    return response

async def record_notes(ctx: Context, notes: str, notes_title: str) -> str:
    """Useful for recording notes on a given topic."""
    current_state = await ctx.store.get("state")
    if "research_notes" not in current_state:
        current_state["research_notes"] = {}
    current_state["research_notes"][notes_title] = notes
    await ctx.store.set("state", current_state)
    return "Notes recorded."

async def write_report(ctx: Context, report_content: str) -> str:
    """Useful for writing a report on a given topic."""
    current_state = await ctx.store.get("state")
    current_state["report_content"] = report_content
    await ctx.store.set("state", current_state)
    return "Report written."

async def review_report(ctx: Context, review: str) -> str:
    """Useful for reviewing a report and providing feedback."""
    current_state = await ctx.store.get("state")
    current_state["review"] = review
    await ctx.store.set("state", current_state)
    return "Report reviewed."
```

## Xây dựng trợ lý nhiều tác nhân

Để xây dựng hệ thống nhiều tác nhân, bạn hãy xác định các tác nhân và tương tác của chúng.
Hệ thống của bạn sẽ có 3 tác nhân:

1. `ResearchAgent` tìm kiếm thông tin trên web về chủ đề đã cho.
2. `WriteAgent` viết báo cáo bằng thông tin do `ResearchAgent` tìm thấy.
3. `ReviewAgent` xem xét báo cáo và đưa ra ý kiến phản hồi.

Ví dụ này sử dụng lớp `AgentWorkflow` để tạo một hệ thống nhiều tác nhân sẽ thực thi các tác nhân này theo thứ tự. Mỗi tác nhân lấy một `system_prompt` cho biết tác nhân đó nên làm gì và đề xuất cách làm việc với các tác nhân khác.

Bạn có thể tuỳ ý hỗ trợ hệ thống nhiều tác nhân bằng cách chỉ định những tác nhân khác mà hệ thống có thể trao đổi bằng `can_handoff_to` (nếu không, hệ thống sẽ tự tìm hiểu).

```
from llama_index.core.agent.workflow import (
    AgentInput,
    AgentOutput,
    ToolCall,
    ToolCallResult,
    AgentStream,
)
from llama_index.core.agent.workflow import FunctionAgent, ReActAgent

research_agent = FunctionAgent(
    name="ResearchAgent",
    description="Useful for searching the web for information on a given topic and recording notes on the topic.",
    system_prompt=(
        "You are the ResearchAgent that can search the web for information on a given topic and record notes on the topic. "
        "Once notes are recorded and you are satisfied, you should hand off control to the WriteAgent to write a report on the topic."
    ),
    llm=llm,
    tools=[search_web, record_notes],
    can_handoff_to=["WriteAgent"],
)

write_agent = FunctionAgent(
    name="WriteAgent",
    description="Useful for writing a report on a given topic.",
    system_prompt=(
        "You are the WriteAgent that can write a report on a given topic. "
        "Your report should be in a markdown format. The content should be grounded in the research notes. "
        "Once the report is written, you should get feedback at least once from the ReviewAgent."
    ),
    llm=llm,
    tools=[write_report],
    can_handoff_to=["ReviewAgent", "ResearchAgent"],
)

review_agent = FunctionAgent(
    name="ReviewAgent",
    description="Useful for reviewing a report and providing feedback.",
    system_prompt=(
        "You are the ReviewAgent that can review a report and provide feedback. "
        "Your feedback should either approve the current report or request changes for the WriteAgent to implement."
    ),
    llm=llm,
    tools=[review_report],
    can_handoff_to=["ResearchAgent","WriteAgent"],
)
```

Các tác nhân đã được xác định, giờ đây bạn có thể tạo `AgentWorkflow` và kích hoạt.

```
from llama_index.core.agent.workflow import AgentWorkflow

agent_workflow = AgentWorkflow(
    agents=[research_agent, write_agent, review_agent],
    root_agent=research_agent.name,
    initial_state={
        "research_notes": {},
        "report_content": "Not written yet.",
        "review": "Review required.",
    },
)
```

Trong quá trình thực thi quy trình công việc, bạn có thể truyền trực tuyến các sự kiện, lệnh gọi công cụ và bản cập nhật vào bảng điều khiển.

```
from llama_index.core.agent.workflow import (
    AgentInput,
    AgentOutput,
    ToolCall,
    ToolCallResult,
    AgentStream,
)

research_topic = """Write me a report on the history of the web.
Briefly describe the history of the world wide web, including
the development of the internet and the development of the web,
including 21st century developments"""

handler = agent_workflow.run(
    user_msg=research_topic
)

current_agent = None
current_tool_calls = ""
async for event in handler.stream_events():
    if (
        hasattr(event, "current_agent_name")
        and event.current_agent_name != current_agent
    ):
        current_agent = event.current_agent_name
        print(f"\n{'='*50}")
        print(f"🤖 Agent: {current_agent}")
        print(f"{'='*50}\n")
    elif isinstance(event, AgentOutput):
        if event.response.content:
            print("📤 Output:", event.response.content)
        if event.tool_calls:
            print(
                "🛠️  Planning to use tools:",
                [call.tool_name for call in event.tool_calls],
            )
    elif isinstance(event, ToolCallResult):
        print(f"🔧 Tool Result ({event.tool_name}):")
        print(f"  Arguments: {event.tool_kwargs}")
        print(f"  Output: {event.tool_output}")
    elif isinstance(event, ToolCall):
        print(f"🔨 Calling Tool: {event.tool_name}")
        print(f"  With arguments: {event.tool_kwargs}")
```

Sau khi quy trình công việc hoàn tất, bạn có thể in kết quả cuối cùng của báo cáo, cũng như trạng thái xem xét cuối cùng của tác nhân xem xét.

```
state = await handler.ctx.store.get("state")
print("Report Content:\n", state["report_content"])
print("\n------------\nFinal Review:\n", state["review"])
```

## Tiến xa hơn với quy trình công việc tuỳ chỉnh

`AgentWorkflow` là một cách tuyệt vời để bắt đầu với hệ thống nhiều tác nhân. Nhưng nếu bạn cần kiểm soát nhiều hơn thì sao? Bạn có thể xây dựng quy trình công việc từ đầu. Dưới đây là một số lý do bạn nên xây dựng quy trình làm việc của riêng mình:

- **Kiểm soát nhiều hơn đối với quy trình**: Bạn có thể quyết định chính xác đường dẫn mà các tác nhân của bạn
  sẽ thực hiện. Điều này bao gồm việc tạo vòng lặp, đưa ra quyết định tại một số điểm nhất định hoặc để các tác nhân làm việc song song trên các tác vụ khác nhau.
- **Sử dụng dữ liệu phức tạp**: Vượt ra ngoài văn bản thuần tuý. Quy trình công việc tuỳ chỉnh cho phép bạn sử dụng dữ liệu có cấu trúc hơn, chẳng hạn như đối tượng JSON hoặc lớp tuỳ chỉnh, cho dữ liệu đầu vào và đầu ra.
- **Làm việc với nhiều loại nội dung đa phương tiện**: Xây dựng các tác nhân có thể hiểu và xử lý
  không chỉ văn bản mà còn cả hình ảnh, âm thanh và video.
- **Lập kế hoạch thông minh hơn**: Bạn có thể thiết kế một quy trình công việc trước tiên tạo một
  kế hoạch chi tiết trước khi các tác nhân bắt đầu làm việc. Điều này hữu ích cho các tác vụ phức tạp đòi hỏi nhiều bước.
- **Cho phép tự sửa lỗi**: Tạo các tác nhân có thể xem xét công việc của chính mình. Nếu kết quả đầu ra không đủ tốt, tác nhân có thể thử lại, tạo một vòng lặp cải thiện cho đến khi kết quả hoàn hảo.

Để tìm hiểu thêm về Quy trình công việc của LlamaIndex, hãy xem [Tài liệu
về quy trình công việc của LlamaIndex](https://docs.llamaindex.ai/en/stable/module_guides/workflow/).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-19 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-19 UTC."],[],[]]
