---
source_url: https://ai.google.dev/gemini-api/docs/langgraph-example?hl=id
fetched_at: 2026-06-08T05:36:07.587882+00:00
title: "Agen ReAct dari awal dengan Gemini dan LangGraph \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Agen ReAct dari awal dengan Gemini dan LangGraph

LangGraph adalah framework untuk membangun aplikasi LLM stateful, sehingga menjadi pilihan yang baik untuk membuat Agen ReAct (Reasoning and Acting).

Agen ReAct menggabungkan penalaran LLM dengan eksekusi tindakan. Agen ini berpikir secara berulang, menggunakan alat, dan bertindak berdasarkan pengamatan untuk mencapai sasaran pengguna, serta menyesuaikan pendekatan secara dinamis. Diperkenalkan dalam ["ReAct: Synergizing Reasoning and Acting
in Language Models"](https://arxiv.org/abs/2210.03629) (2023), pola ini
mencoba meniru pemecahan masalah yang fleksibel dan mirip manusia melalui alur kerja yang kaku.

LangGraph menawarkan agen ReAct bawaan ([`create_react_agent`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)),
yang sangat berguna saat Anda memerlukan lebih banyak kontrol dan penyesuaian untuk penerapan ReAct. Panduan ini akan menunjukkan versi yang disederhanakan.

Agen model LangGraph sebagai grafik menggunakan tiga komponen utama:

- `State`: Struktur data bersama (biasanya `TypedDict` atau `Pydantic BaseModel`) yang mewakili snapshot saat ini dari aplikasi.
- `Nodes`: Mengenkode logika agen Anda. Agen ini menerima Status saat ini sebagai input, melakukan beberapa komputasi atau efek samping, dan menampilkan Status yang diperbarui, seperti panggilan LLM atau panggilan alat.
- `Edges`: Menentukan `Node` berikutnya yang akan dieksekusi berdasarkan `State` saat ini, sehingga memungkinkan logika kondisional dan transisi tetap.

Jika belum memiliki Kunci API, Anda bisa mendapatkannya dari [Google AI
Studio](https://aistudio.google.com/app/apikey?hl=id).

```
pip install langgraph langchain-google-genai geopy requests
```

Tetapkan kunci API Anda dalam variabel lingkungan `GEMINI_API_KEY`.

```
import os

# Read your API key from the environment variable or set it manually
api_key = os.getenv("GEMINI_API_KEY")
```

Untuk lebih memahami cara menerapkan agen ReAct menggunakan LangGraph, panduan ini akan membahas contoh praktis. Anda akan membuat agen yang tujuannya adalah menggunakan alat untuk menemukan cuaca saat ini untuk lokasi tertentu.

Untuk agen cuaca ini, `State` akan mempertahankan histori percakapan yang sedang berlangsung (sebagai daftar pesan) dan penghitung (sebagai bilangan bulat) untuk jumlah langkah yang diambil, untuk tujuan ilustrasi.

LangGraph menyediakan fungsi helper, `add_messages`, untuk memperbarui daftar pesan status. Fungsi ini berfungsi sebagai [peredam](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers),
mengambil daftar saat ini, ditambah pesan baru, dan menampilkan daftar gabungan. Fungsi ini menangani pembaruan berdasarkan ID pesan dan secara default menggunakan perilaku "hanya tambahkan" untuk pesan baru yang belum dilihat.

```
from typing import Annotated,Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages  # helper function to add messages to the state

class AgentState(TypedDict):
    """The state of the agent."""
    messages: Annotated[Sequence[BaseMessage], add_messages]
    number_of_steps: int
```

Selanjutnya, tentukan alat cuaca Anda.

```
from langchain_core.tools import tool
from geopy.geocoders import Nominatim
from pydantic import BaseModel, Field
import requests

geolocator = Nominatim(user_agent="weather-app")

class SearchInput(BaseModel):
    location:str = Field(description="The city and state, e.g., San Francisco")
    date:str = Field(description="the forecasting date for when to get the weather format (yyyy-mm-dd)")

@tool("get_weather_forecast", args_schema=SearchInput, return_direct=True)
def get_weather_forecast(location: str, date: str):
    """Retrieves the weather using Open-Meteo API.

    Takes a given location (city) and a date (yyyy-mm-dd).

    Returns:
        A dict with the time and temperature for each hour.
    """
    # Note that Colab may experience rate limiting on this service. If this
    # happens, use a machine to which you have exclusive access.
    location = geolocator.geocode(location)
    if location:
        try:
            response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&hourly=temperature_2m&start_date={date}&end_date={date}")
            data = response.json()
            return dict(zip(data["hourly"]["time"], data["hourly"]["temperature_2m"]))
        except Exception as e:
            return {"error": str(e)}
    else:
        return {"error": "Location not found"}

tools = [get_weather_forecast]
```

Sekarang, inisialisasi model dan ikat alat ke model.

```
from datetime import datetime
from langchain_google_genai import ChatGoogleGenerativeAI

# Create LLM class
llm = ChatGoogleGenerativeAI(
    model= "gemini-3.5-flash",
    temperature=1.0,
    max_retries=2,
    google_api_key=api_key,
)

# Bind tools to the model
model = llm.bind_tools([get_weather_forecast])

# Test the model with tools
res=model.invoke(f"What is the weather in Berlin on {datetime.today()}?")

print(res)
```

Langkah terakhir sebelum Anda dapat menjalankan agen adalah menentukan node dan edge.
Dalam contoh ini, Anda memiliki dua node dan satu edge.

- Node `call_tool` yang menjalankan metode alat Anda. LangGraph memiliki node bawaan
  untuk ini yang disebut
  [ToolNode](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/).
- Node `call_model` yang menggunakan `model_with_tools` untuk memanggil model.
- Edge `should_continue` yang menentukan apakah akan memanggil alat atau model.

Jumlah node dan edge tidak tetap. Anda dapat menambahkan node dan edge sebanyak yang Anda inginkan ke grafik. Misalnya, Anda dapat menambahkan node untuk menambahkan output terstruktur atau node verifikasi/refleksi mandiri untuk memeriksa output model sebelum memanggil alat atau model.

```
from langchain_core.messages import ToolMessage
from langchain_core.runnables import RunnableConfig

tools_by_name = {tool.name: tool for tool in tools}

# Define our tool node
def call_tool(state: AgentState):
    outputs = []
    # Iterate over the tool calls in the last message
    for tool_call in state["messages"][-1].tool_calls:
        # Get the tool by name
        tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
        outputs.append(
            ToolMessage(
                content=tool_result,
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )
    return {"messages": outputs}

def call_model(
    state: AgentState,
    config: RunnableConfig,
):
    # Invoke the model with the system prompt and the messages
    response = model.invoke(state["messages"], config)
    # This returns a list, which combines with the existing messages state
    # using the add_messages reducer.
    return {"messages": [response]}

# Define the conditional edge that determines whether to continue or not
def should_continue(state: AgentState):
    messages = state["messages"]
    # If the last message is not a tool call, then finish
    if not messages[-1].tool_calls:
        return "end"
    # default to continue
    return "continue"
```

Dengan semua komponen agen siap, Anda kini dapat merakitnya.

```
from langgraph.graph import StateGraph, END

# Define a new graph with our state
workflow = StateGraph(AgentState)

# 1. Add the nodes
workflow.add_node("llm", call_model)
workflow.add_node("tools",  call_tool)
# 2. Set the entrypoint as `agent`, this is the first node called
workflow.set_entry_point("llm")
# 3. Add a conditional edge after the `llm` node is called.
workflow.add_conditional_edges(
    # Edge is used after the `llm` node is called.
    "llm",
    # The function that will determine which node is called next.
    should_continue,
    # Mapping for where to go next, keys are strings from the function return,
    # and the values are other nodes.
    # END is a special node marking that the graph is finish.
    {
        # If `tools`, then we call the tool node.
        "continue": "tools",
        # Otherwise we finish.
        "end": END,
    },
)
# 4. Add a normal edge after `tools` is called, `llm` node is called next.
workflow.add_edge("tools", "llm")

# Now we can compile and visualize our graph
graph = workflow.compile()
```

Anda dapat memvisualisasikan grafik menggunakan metode `draw_mermaid_png`.

```
from IPython.display import Image, display

display(Image(graph.get_graph().draw_mermaid_png()))
```

![png](https://ai.google.dev/static/gemini-api/docs/images/langgraph-react-agent_16_0.png?hl=id)

Sekarang jalankan agen.

```
from datetime import datetime
# Create our initial message dictionary
inputs = {"messages": [("user", f"What is the weather in Berlin on {datetime.today()}?")]}

# call our graph with streaming to see the steps
for state in graph.stream(inputs, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
```

Anda kini dapat melanjutkan percakapan, meminta cuaca di kota lain, atau meminta perbandingan.

```
state["messages"].append(("user", "Would it be warmer in Munich?"))

for state in graph.stream(state, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
```

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-19 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-19 UTC."],[],[]]
