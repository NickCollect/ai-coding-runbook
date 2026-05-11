---
source_url: https://ai.google.dev/gemini-api/docs/temporal-example?hl=id
fetched_at: 2026-05-11T05:09:59.552389+00:00
title: "Agen AI yang andal dengan Gemini dan Temporal \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Agen AI yang andal dengan Gemini dan Temporal

Tutorial ini memandu Anda membangun loop agentik
[gaya ReAct](https://arxiv.org/abs/2210.03629) yang menggunakan
Gemini API untuk penalaran dan [Temporal](https://temporal.io/) untuk ketahanan.
Kode sumber lengkap untuk tutorial ini tersedia di
[GitHub](https://github.com/temporal-community/durable-react-agent-gemini).

Agen dapat memanggil alat, seperti mencari tahu peringatan cuaca atau melakukan geolokasi alamat IP, dan akan melakukan loop hingga memiliki informasi yang cukup untuk merespons.

Yang membedakan demo ini dengan demo agen biasa adalah **daya tahan**. Setiap panggilan LLM, setiap pemanggilan alat, dan setiap langkah loop agentik dipertahankan oleh Temporal. Jika proses mengalami error, jaringan terputus, atau API mengalami waktu tunggu habis, Temporal akan otomatis mencoba lagi dan melanjutkan dari langkah terakhir yang selesai. Tidak ada histori percakapan yang hilang, dan tidak ada panggilan alat yang diulang secara tidak benar.

## Arsitektur

Arsitektur ini terdiri dari tiga bagian:

- **Alur kerja:** Loop agentic yang mengatur logika eksekusi.
- **Aktivitas:** Unit tugas individual (panggilan LLM, panggilan alat) yang
  dibuat Temporal menjadi tahan lama.
- **Worker:** Proses yang menjalankan alur kerja dan aktivitas.

Dalam contoh ini, Anda akan menempatkan ketiga bagian ini dalam satu file
(`durable_agent_worker.py`). Dalam penerapan di dunia nyata, Anda akan memisahkannya
untuk memungkinkan berbagai keuntungan deployment dan skalabilitas. Anda akan menempatkan
kode yang memberikan perintah ke agen dalam file kedua
(`start_workflow.py`).

## Prasyarat

Untuk menyelesaikan panduan ini, Anda memerlukan:

- Kunci Gemini API. Anda dapat membuatnya secara gratis di
  [Google AI Studio](https://aistudio.google.com/apikey?hl=id).
- [Python](https://www.python.org/downloads/) versi 3.10 atau yang lebih baru.
- [Temporal CLI](https://docs.temporal.io/cli) untuk menjalankan server pengembangan lokal.

## Penyiapan

Sebelum memulai, pastikan Anda memiliki
[server pengembangan Temporal](https://docs.temporal.io/cli#start-dev-server)
yang berjalan secara lokal:

```
temporal server start-dev
```

Selanjutnya, instal dependensi yang diperlukan:

```
pip install temporalio google-genai httpx pydantic python-dotenv
```

Buat file `.env` di direktori project Anda dengan kunci Gemini API Anda. Anda
dapat memperoleh kunci API dari
[Google AI Studio](https://aistudio.google.com/apikey?hl=id).

```
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

## Penerapan

Bagian selanjutnya dari tutorial ini akan membahas `durable_agent_worker.py` dari atas ke
bawah, dengan membangun bagian agen selangkah demi selangkah. Buat file dan ikuti langkah-langkahnya.

### Penyiapan impor dan sandbox

Mulailah dengan impor yang harus ditentukan di awal. Blok
`workflow.unsafe.imports_passed_through()` memberi tahu sandbox alur kerja Temporal untuk mengizinkan modul tertentu melewati tanpa batasan. Hal ini
diperlukan karena beberapa library (terutama `httpx`, yang merupakan subclass
`urllib.request.Request`) menggunakan pola yang akan diblokir oleh sandbox.

```
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    import pydantic_core  # noqa: F401
    import annotated_types  # noqa: F401

    import httpx
    from pydantic import BaseModel, Field
    from google import genai
    from google.genai import types
```

### Petunjuk sistem

Selanjutnya, tentukan kepribadian agen. Petunjuk sistem memberi tahu model cara
berperilaku. Agen ini diinstruksikan untuk merespons dalam bentuk haiku jika tidak ada alat yang diperlukan.

```
SYSTEM_INSTRUCTIONS = """
You are a helpful agent that can use tools to help the user.
You will be given an input from the user and a list of tools to use.
You may or may not need to use the tools to satisfy the user ask.
If no tools are needed, respond in haikus.
"""
```

### Definisi alat

Sekarang tentukan alat yang dapat digunakan agen. Setiap alat adalah fungsi asinkron dengan
docstring deskriptif. Alat yang menggunakan parameter menggunakan model Pydantic sebagai
satu-satunya argumennya. Ini adalah praktik terbaik Temporal yang menjaga tanda tangan aktivitas tetap stabil saat Anda menambahkan kolom opsional dari waktu ke waktu.

```
import json

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

class GetWeatherAlertsRequest(BaseModel):
    """Request model for getting weather alerts."""

    state: str = Field(description="Two-letter US state code (e.g. CA, NY)")

async def get_weather_alerts(request: GetWeatherAlertsRequest) -> str:
    """Get weather alerts for a US state.

    Args:
        request: The request object containing:
            - state: Two-letter US state code (e.g. CA, NY)
    """
    headers = {"User-Agent": USER_AGENT, "Accept": "application/geo+json"}
    url = f"{NWS_API_BASE}/alerts/active/area/{request.state}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=5.0)
        response.raise_for_status()
        return json.dumps(response.json())
```

Selanjutnya, tentukan alat untuk geolokasi alamat IP:

```
class GetLocationRequest(BaseModel):
    """Request model for getting location info from an IP address."""

    ipaddress: str = Field(description="An IP address")

async def get_ip_address() -> str:
    """Get the public IP address of the current machine."""
    async with httpx.AsyncClient() as client:
        response = await client.get("https://icanhazip.com")
        response.raise_for_status()
        return response.text.strip()

async def get_location_info(request: GetLocationRequest) -> str:
    """Get the location information for an IP address including city, state, and country.

    Args:
        request: The request object containing:
            - ipaddress: An IP address to look up
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://ip-api.com/json/{request.ipaddress}")
        response.raise_for_status()
        result = response.json()
        return f"{result['city']}, {result['regionName']}, {result['country']}"
```

### Registri alat

Selanjutnya, buat registry yang memetakan nama alat ke fungsi pengendali. Fungsi
`get_tools()` menghasilkan objek `FunctionDeclaration` yang kompatibel dengan Gemini
dari yang dapat dipanggil menggunakan `FunctionDeclaration.from_callable_with_api_option()`.

```
from typing import Any, Awaitable, Callable

ToolHandler = Callable[..., Awaitable[Any]]

def get_handler(tool_name: str) -> ToolHandler:
    """Get the handler function for a given tool name."""
    if tool_name == "get_location_info":
        return get_location_info
    if tool_name == "get_ip_address":
        return get_ip_address
    if tool_name == "get_weather_alerts":
        return get_weather_alerts
    raise ValueError(f"Unknown tool name: {tool_name}")

def get_tools() -> types.Tool:
    """Get the Tool object containing all available function declarations.

    Uses FunctionDeclaration.from_callable_with_api_option() from the Google GenAI SDK
    to generate tool definitions from the handler functions.
    """
    return types.Tool(
        function_declarations=[
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_weather_alerts, api_option="GEMINI_API"
            ),
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_location_info, api_option="GEMINI_API"
            ),
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_ip_address, api_option="GEMINI_API"
            ),
        ]
    )
```

### Aktivitas LLM

Sekarang, tentukan aktivitas yang memanggil Gemini API. Class data `GeminiChatRequest` dan
`GeminiChatResponse` menentukan kontrak.

Anda akan menonaktifkan panggilan fungsi otomatis sehingga pemanggilan LLM dan
pemanggilan alat ditangani sebagai tugas terpisah, sehingga meningkatkan ketahanan agen
Anda. Anda juga akan menonaktifkan percobaan ulang bawaan SDK (`attempts=1`) karena Temporal menangani percobaan ulang secara andal.

```
import os
from dataclasses import dataclass

from temporalio import activity

@dataclass
class GeminiChatRequest:
    """Request parameters for a Gemini chat completion."""

    model: str
    system_instruction: str
    contents: list[types.Content]
    tools: list[types.Tool]

@dataclass
class GeminiChatResponse:
    """Response from a Gemini chat completion."""

    text: str | None
    function_calls: list[dict[str, Any]]
    raw_parts: list[types.Part]

@activity.defn
async def generate_content(request: GeminiChatRequest) -> GeminiChatResponse:
    """Execute a Gemini chat completion with tool support."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is not set")
    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(
            retry_options=types.HttpRetryOptions(attempts=1),
        ),
    )

    config = types.GenerateContentConfig(
        system_instruction=request.system_instruction,
        tools=request.tools,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
    )

    response = await client.aio.models.generate_content(
        model=request.model,
        contents=request.contents,
        config=config,
    )

    function_calls = []
    raw_parts = []
    text_parts = []

    if response.candidates and response.candidates[0].content:
        for part in response.candidates[0].content.parts:
            raw_parts.append(part)
            if part.function_call:
                function_calls.append(
                    {
                        "name": part.function_call.name,
                        "args": dict(part.function_call.args) if part.function_call.args else {},
                    }
                )
            elif part.text:
                text_parts.append(part.text)

    text = "".join(text_parts) if text_parts and not function_calls else None

    return GeminiChatResponse(
        text=text,
        function_calls=function_calls,
        raw_parts=raw_parts,
    )
```

### Aktivitas alat dinamis

Selanjutnya, tentukan aktivitas yang menjalankan alat. Hal ini menggunakan fitur aktivitas dinamis Temporal: pengendali alat (dapat dipanggil) diperoleh dari registry alat melalui fungsi `get_handler`. Hal ini memungkinkan berbagai agen ditentukan hanya dengan menyediakan serangkaian alat dan petunjuk sistem yang berbeda; alur kerja yang menerapkan loop agen tidak memerlukan perubahan.

Aktivitas memeriksa tanda tangan handler untuk menentukan cara meneruskan
argumen. Jika handler mengharapkan model Pydantic, handler akan menangani format output bertingkat
yang dihasilkan Gemini (misalnya, `{"request": {"state": "CA"}}`, bukan
`{"state": "CA"}` datar).

```
import inspect
from collections.abc import Sequence

from temporalio.common import RawValue

@activity.defn(dynamic=True)
async def dynamic_tool_activity(args: Sequence[RawValue]) -> dict:
    """Execute a tool dynamically based on the activity name."""
    tool_name = activity.info().activity_type
    tool_args = activity.payload_converter().from_payload(args[0].payload, dict)
    activity.logger.info(f"Running dynamic tool '{tool_name}' with args: {tool_args}")

    handler = get_handler(tool_name)

    if not inspect.iscoroutinefunction(handler):
        raise TypeError("Tool handler must be async (awaitable).")

    sig = inspect.signature(handler)
    params = list(sig.parameters.values())

    if len(params) == 0:
        result = await handler()
    else:
        param = params[0]
        param_name = param.name
        ann = param.annotation

        if isinstance(ann, type) and issubclass(ann, BaseModel):
            nested_args = tool_args.get(param_name, tool_args)
            result = await handler(ann(**nested_args))
        else:
            result = await handler(**tool_args)

    activity.logger.info(f"Tool '{tool_name}' result: {result}")
    return result
```

### Alur kerja agentic loop

Sekarang Anda memiliki semua bagian untuk menyelesaikan pembuatan agen. Class `AgentWorkflow`
menerapkan alur kerja yang berisi loop agen. Dalam loop tersebut, LLM
dipanggil melalui aktivitas (sehingga tahan lama), output diperiksa, dan jika
alat telah dipilih oleh LLM, alat tersebut dipanggil melalui `dynamic_tool_activity`.

Dalam agen gaya ReAct sederhana ini, setelah LLM memilih untuk tidak menggunakan alat, loop dianggap selesai dan hasil LLM akhir akan ditampilkan.

```
from datetime import timedelta

@workflow.defn
class AgentWorkflow:
    """Agentic loop workflow that uses Gemini for LLM calls and executes tools."""

    @workflow.run
    async def run(self, input: str) -> str:
        contents: list[types.Content] = [
            types.Content(role="user", parts=[types.Part.from_text(text=input)])
        ]

        tools = [get_tools()]

        while True:
            result = await workflow.execute_activity(
                generate_content,
                GeminiChatRequest(
                    model="gemini-3-flash-preview",
                    system_instruction=SYSTEM_INSTRUCTIONS,
                    contents=contents,
                    tools=tools,
                ),
                start_to_close_timeout=timedelta(seconds=60),
            )

            if result.function_calls:
                # Sending the complete raw_parts here ensures Gemini 3 thought
                # signatures are propagated correctly.
                contents.append(types.Content(role="model", parts=result.raw_parts))

                for function_call in result.function_calls:
                    tool_result = await self._handle_function_call(function_call)

                    contents.append(
                        types.Content(
                            role="user",
                            parts=[
                                types.Part.from_function_response(
                                    name=function_call["name"],
                                    response={"result": tool_result},
                                )
                            ],
                        )
                    )
            else:
                return result.text
            # Leave this in place. You will un-comment it during a durability
            # test later on.
            # await asyncio.sleep(10)

    async def _handle_function_call(self, function_call: dict) -> str:
        """Execute a tool via dynamic activity and return the result."""
        tool_name = function_call["name"]
        tool_args = function_call.get("args", {})

        result = await workflow.execute_activity(
            tool_name,
            tool_args,
            start_to_close_timeout=timedelta(seconds=30),
        )

        return result
```

Loop agentik sepenuhnya tahan lama. Jika pekerja agen mengalami error setelah beberapa iterasi melalui loop, Temporal akan melanjutkan tepat dari tempat terakhir tanpa perlu memanggil kembali pemanggilan LLM atau pemanggilan alat yang sudah dieksekusi.

### Startup pekerja

Terakhir, hubungkan semuanya. Meskipun kode mengimplementasikan logika bisnis yang diperlukan dengan cara yang membuatnya tampak berjalan dalam satu proses, penggunaan Temporal menjadikannya sistem berbasis peristiwa (khususnya, berbasis sumber peristiwa) yang komunikasi antara alur kerja dan aktivitasnya terjadi melalui pesan yang disediakan oleh Temporal.

Worker Temporal terhubung ke layanan Temporal dan bertindak sebagai penjadwal untuk
tugas alur kerja dan aktivitas. Worker mendaftarkan alur kerja dan kedua aktivitas, lalu mulai memproses tugas.

```
import asyncio
from concurrent.futures import ThreadPoolExecutor

from dotenv import load_dotenv
from temporalio.client import Client
from temporalio.contrib.pydantic import pydantic_data_converter
from temporalio.envconfig import ClientConfig
from temporalio.worker import Worker

async def main():
    config = ClientConfig.load_client_connect_config()
    config.setdefault("target_host", "localhost:7233")
    client = await Client.connect(
        **config,
        data_converter=pydantic_data_converter,
    )

    worker = Worker(
        client,
        task_queue="gemini-agent-python-task-queue",
        workflows=[
            AgentWorkflow,
        ],
        activities=[
            generate_content,
            dynamic_tool_activity,
        ],
        activity_executor=ThreadPoolExecutor(max_workers=10),
    )
    await worker.run()

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
```

## Skrip klien

Buat skrip klien (`start_workflow.py`). Skrip ini mengirimkan kueri dan menunggu
hasilnya. Perhatikan bahwa skrip ini terhubung ke antrean tugas yang sama yang dirujuk di pekerja
agen—skrip `start_workflow` mengirimkan tugas alur kerja dengan perintah
pengguna ke antrean tugas tersebut, sehingga memulai eksekusi agen.

```
import asyncio
import sys
import uuid

from temporalio.client import Client
from temporalio.contrib.pydantic import pydantic_data_converter

async def main():
    client = await Client.connect(
        "localhost:7233",
        data_converter=pydantic_data_converter,
    )

    query = sys.argv[1] if len(sys.argv) > 1 else "Tell me about recursion"

    result = await client.execute_workflow(
        "AgentWorkflow",
        query,
        id=f"gemini-agent-id-{uuid.uuid4()}",
        task_queue="gemini-agent-python-task-queue",
    )
    print(f"\nResult:\n{result}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Menjalankan agen

Jika Anda belum melakukannya, mulai server pengembangan Temporal:

```
temporal server start-dev
```

Di jendela terminal baru, mulai pekerja agen:

```
python -m durable_agent_worker
```

Di jendela terminal ketiga, kirimkan kueri ke agen Anda:

```
python -m start_workflow "are there any weather alerts for where I am?"
```

Perhatikan output di terminal `durable_agent_worker` yang menunjukkan
tindakan yang terjadi di setiap iterasi loop agentik. LLM dapat
memenuhi permintaan pengguna dengan memanggil serangkaian alat yang tersedia. Anda dapat
melihat langkah-langkah yang dijalankan melalui UI Temporal di
`http://localhost:8233/namespaces/default/workflows`.

Coba beberapa perintah berbeda untuk melihat alasan agen dan alat panggilan:

```
python -m start_workflow "are there any weather alerts for New York?"
python -m start_workflow "where am I?"
python -m start_workflow "what is my ip address?"
python -m start_workflow "tell me a joke"
```

Perintah terakhir tidak memerlukan alat apa pun, jadi agen merespons dalam bentuk haiku berdasarkan `SYSTEM_INSTRUCTIONS`.

## Menguji daya tahan (Opsional)

Membangun di Temporal memastikan agen Anda dapat mengatasi kegagalan dengan lancar. Anda dapat
mengujinya menggunakan dua eksperimen yang berbeda.

### Menyimulasikan pemadaman jaringan

Dalam pengujian ini, Anda akan menonaktifkan koneksi internet komputer Anda untuk sementara, mengirimkan alur kerja, melihat Temporal mencoba lagi secara otomatis, lalu memulihkan jaringan untuk melihat pemulihannya.

1. Putuskan koneksi komputer Anda dari internet (misalnya, nonaktifkan Wi-Fi Anda).
2. Mengirimkan alur kerja:

   ```
   python -m start_workflow "tell me a joke"
   ```
3. Periksa UI Temporal (`http://localhost:8233`). Anda akan melihat aktivitas LLM gagal dan Temporal secara otomatis mengelola percobaan ulang di latar belakang.
4. Hubungkan kembali ke internet.
5. Percobaan ulang otomatis berikutnya akan berhasil menjangkau Gemini API, dan terminal Anda akan mencetak hasil akhir.

### Bertahan dari error worker

Dalam pengujian ini, Anda akan menghentikan pekerja di tengah eksekusi dan memulainya kembali. Pemutaran ulang temporal
memutar ulang histori alur kerja (sumber peristiwa) dan melanjutkan dari aktivitas
terakhir yang diselesaikan—pemanggilan LLM dan panggilan alat yang sudah diselesaikan tidak diulang.

1. Untuk memberi diri Anda waktu untuk menghentikan pekerja, buka `durable_agent_worker.py` dan
   hapus sementara komentar `await asyncio.sleep(10)` di dalam loop `AgentWorkflow`
   `run`.
2. Mulai ulang pekerja:

   ```
   python -m durable_agent_worker
   ```
3. Mengirimkan kueri yang memicu beberapa alat:

   ```
   python -m start_workflow "are there any weather alerts where I am?"
   ```
4. Hentikan proses pekerja kapan saja sebelum selesai (`Ctrl-C` di terminal pekerja, atau menggunakan `kill %1` jika berjalan di latar belakang).
5. Mulai ulang pekerja:

   ```
   python -m durable_agent_worker
   ```

Temporal memutar ulang histori alur kerja. Panggilan LLM dan pemanggilan alat yang telah selesai **tidak** dieksekusi ulang—hasilnya langsung diputar ulang dari histori (log peristiwa). Alur kerja berhasil diselesaikan.

## Aset lainnya

- [Dokumentasi temporal](https://docs.temporal.io/)
- [Temporal Python SDK](https://docs.temporal.io/develop/python)
- [Google GenAI SDK](https://googleapis.github.io/python-genai/)
- [Kode sumber untuk tutorial ini](https://github.com/temporal-community/durable-react-agent-gemini)

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-04-29 UTC."],[],[]]
