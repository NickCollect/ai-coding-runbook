---
source_url: https://ai.google.dev/gemini-api/docs/temporal-example?hl=tr
fetched_at: 2026-05-05T20:48:10.823752+00:00
title: "Gemini ve Temporal ile dayan\u0131kl\u0131 yapay zeka temsilcisi \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini ve Temporal ile dayanıklı yapay zeka temsilcisi

Bu eğitimde, akıl yürütme için Gemini API'yi ve dayanıklılık için [Temporal](https://temporal.io/)'ı kullanan bir [ReAct tarzı](https://arxiv.org/abs/2210.03629) agentic döngü oluşturma süreci adım adım açıklanmaktadır.
Bu eğitimin tam kaynak kodunu [GitHub](https://github.com/temporal-community/durable-react-agent-gemini)'da bulabilirsiniz.

Aracı, hava durumu uyarılarını arama veya IP adresinin coğrafi konumunu belirleme gibi araçları çağırabilir ve yanıt vermek için yeterli bilgiye sahip olana kadar döngüye girer.

Bu demoyu tipik bir ajan demosundan farklı kılan özellik **dayanıklılıktır**. Her LLM çağrısı, her araç çağırma ve her aracı döngüsü adımı Temporal tarafından kalıcı hale getirilir. İşlem çökerse, ağ düşerse veya API zaman aşımına uğrarsa Temporal otomatik olarak yeniden dener ve son tamamlanan adımdan devam eder. Sohbet geçmişi kaybolmaz ve araç çağrıları yanlışlıkla tekrarlanmaz.

## Mimari

Mimari üç bölümden oluşur:

- **İş akışı:** Yürütme mantığını düzenleyen ajan tabanlı döngü.
- **Etkinlikler:** Temporal'ın kalıcı hale getirdiği ayrı iş birimleri (LLM çağrıları, araç çağrıları).
- **Çalışan:** İş akışlarını ve etkinlikleri yürüten süreç.

Bu örnekte, bu üç parçanın tamamını tek bir dosyaya (`durable_agent_worker.py`) yerleştirirsiniz. Gerçek dünyadaki bir uygulamada, çeşitli dağıtım ve ölçeklenebilirlik avantajlarından yararlanmak için bunları ayırırsınız. Aracıya istem sağlayan kodu ikinci bir dosyaya (`start_workflow.py`) yerleştirirsiniz.

## Ön koşullar

Bu kılavuzu tamamlamak için ihtiyacınız olanlar:

- Gemini API anahtarı. [Google AI Studio](https://aistudio.google.com/apikey?hl=tr)'da ücretsiz olarak oluşturabilirsiniz.
- [Python](https://www.python.org/downloads/) 3.10 veya sonraki sürümler.
- Yerel geliştirme sunucusu çalıştırmak için [Temporal CLI](https://docs.temporal.io/cli).

## Kurulum

Başlamadan önce, yerel olarak çalışan bir [Temporal geliştirme sunucunuzun](https://docs.temporal.io/cli#start-dev-server) olduğundan emin olun:

```
temporal server start-dev
```

Ardından, gerekli bağımlılıkları yükleyin:

```
pip install temporalio google-genai httpx pydantic python-dotenv
```

Proje dizininizde Gemini API anahtarınızla bir `.env` dosyası oluşturun. [Google AI Studio](https://aistudio.google.com/apikey?hl=tr)'dan API anahtarı alabilirsiniz.

```
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

## Uygulama

Bu eğitimin geri kalanında, `durable_agent_worker.py` yukarıdan aşağıya doğru adım adım oluşturularak açıklanmaktadır. Dosyayı oluşturun ve adımları uygulayın.

### İçe aktarma işlemleri ve korumalı alan kurulumu

Önceden tanımlanması gereken içe aktarma işlemleriyle başlayın. `workflow.unsafe.imports_passed_through()` bloğu, Temporal'ın iş akışı sanal alanına belirli modüllerin kısıtlama olmadan geçmesine izin vermesini söyler. Çeşitli kitaplıklar (özellikle `httpx`, `urllib.request.Request`'in alt sınıfıdır) korumalı alanın aksi takdirde engelleyeceği kalıplar kullandığından bu gereklidir.

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

### Sistem talimatları

Ardından, temsilcinin kişiliğini tanımlayın. Sistem talimatları, modele nasıl davranması gerektiğini söyler. Bu temsilci, araç gerekmediğinde haiku tarzında yanıt vermesi için talimatlandırıldı.

```
SYSTEM_INSTRUCTIONS = """
You are a helpful agent that can use tools to help the user.
You will be given an input from the user and a list of tools to use.
You may or may not need to use the tools to satisfy the user ask.
If no tools are needed, respond in haikus.
"""
```

### Araç tanımları

Şimdi temsilcinin kullanabileceği araçları tanımlayın. Her araç, açıklayıcı bir doküman dizesi içeren bir eşzamansız işlevdir. Parametre alan araçlar, tek bağımsız değişken olarak Pydantic modeli kullanır. Bu, zaman içinde isteğe bağlı alanlar eklerken etkinlik imzalarını sabit tutan bir Temporal en iyi uygulamasıdır.

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

Ardından, IP adresi coğrafi konumu için araçları tanımlayın:

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

### Araç kayıt defteri

Ardından, araç adlarını işleyici işlevleriyle eşleyen bir kayıt oluşturun. `get_tools()` işlevi, `FunctionDeclaration.from_callable_with_api_option()` kullanarak çağrılabilir öğelerden Gemini ile uyumlu `FunctionDeclaration` nesneler oluşturur.

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

### LLM etkinliği

Şimdi Gemini API'yi çağıran etkinliği tanımlayın. Sözleşme, `GeminiChatRequest` ve `GeminiChatResponse` veri sınıflarıyla tanımlanır.

LLM çağırma ve araç çağırma işlemlerinin ayrı görevler olarak ele alınması için otomatik işlev çağırmayı devre dışı bırakarak aracınızın daha dayanıklı olmasını sağlayacaksınız. Ayrıca, Temporal, yeniden denemeleri kalıcı olarak işlediğinden SDK'nın yerleşik yeniden denemelerini de devre dışı bırakırsınız (`attempts=1`).

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

### Dinamik araç etkinliği

Ardından, araçları yürüten etkinliği tanımlayın. Bu işlemde Temporal'ın dinamik etkinlik özelliği kullanılır: Araç işleyici (çağrılabilir) `get_handler` işlevi aracılığıyla araç kayıt defterinden alınır. Bu sayede, farklı araçlar ve sistem talimatları sağlanarak farklı aracıların tanımlanması kolaylaşır. Aracı döngüsünü uygulayan iş akışında herhangi bir değişiklik yapılması gerekmez.

Etkinlik, bağımsız değişkenlerin nasıl iletileceğini belirlemek için işleyicinin imzasını inceler. İşleyici bir Pydantic modeli bekliyorsa Gemini'ın ürettiği iç içe yerleştirilmiş çıkış biçimini (örneğin, düz `{"state": "CA"}` yerine `{"request": {"state": "CA"}}`) işler.

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

### Temsilci döngüsü iş akışı

Artık aracıyı oluşturmayı tamamlamak için gereken tüm parçalara sahipsiniz. `AgentWorkflow`
sınıfı, aracı döngüsünü içeren bir iş akışını uygular. Bu döngüde, LLM etkinlik aracılığıyla çağrılır (bu da onu dayanıklı hale getirir), çıkış incelenir ve LLM tarafından bir araç seçilmişse bu araç `dynamic_tool_activity` aracılığıyla çağrılır.

Bu basit ReAct tarzı aracıda, LLM bir aracı kullanmamayı seçtiğinde döngü tamamlanmış kabul edilir ve nihai LLM sonucu döndürülür.

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

The agentic loop is fully durable. Aracının çalışanı döngüde birkaç yinelemeden sonra kilitlenirse Temporal, yürütülen LLM çağrılarını veya araç çağrılarını yeniden çağırmaya gerek kalmadan tam olarak kaldığı yerden devam eder.

### Çalışan başlatma

Son olarak, her şeyi birbirine bağlayın. Kod, gerekli iş mantığını tek bir süreçte çalışıyormuş gibi görünecek şekilde uygularken Temporal'ın kullanılması, iş akışı ile etkinlikler arasındaki iletişimin Temporal tarafından sağlanan mesajlaşma yoluyla gerçekleştiği, olaya dayalı (özellikle de olay kaynaklı) bir sistem oluşturur.

Temporal Worker, Temporal hizmetine bağlanır ve iş akışı ile etkinlik görevleri için planlayıcı görevi görür. Çalışan, iş akışını ve her iki etkinliği de kaydeder, ardından görevleri dinlemeye başlar.

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

## İstemci komut dosyası

İstemci komut dosyasını (`start_workflow.py`) oluşturun. Bu komut dosyası bir sorgu gönderir ve sonucu bekler. Bu komutun, agent worker'da referans verilen görev sırasına bağlandığını unutmayın. `start_workflow` komut dosyası, kullanıcı istemiyle birlikte bir iş akışı görevini bu görev sırasına göndererek aracının yürütülmesini başlatır.

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

## Temsilciyi çalıştırma

Henüz yapmadıysanız Temporal geliştirme sunucusunu başlatın:

```
temporal server start-dev
```

Yeni bir terminal penceresinde aracı çalışanını başlatın:

```
python -m durable_agent_worker
```

Üçüncü bir terminal penceresinde, aracınıza bir sorgu gönderin:

```
python -m start_workflow "are there any weather alerts for where I am?"
```

`durable_agent_worker` terminalindeki çıkışa dikkat edin. Bu çıkış, aracılı döngünün her yinelemesinde gerçekleşen işlemleri gösterir. LLM, elindeki bir dizi aracı kullanarak kullanıcı isteğini karşılayabilir. Temporal kullanıcı arayüzü üzerinden yürütülen adımları `http://localhost:8233/namespaces/default/workflows` adresinden görebilirsiniz.

Temsilci nedenini ve görüşme araçlarını görmek için birkaç farklı istem deneyin:

```
python -m start_workflow "are there any weather alerts for New York?"
python -m start_workflow "where am I?"
python -m start_workflow "what is my ip address?"
python -m start_workflow "tell me a joke"
```

Son istem için herhangi bir araç gerekmediğinden aracı, `SYSTEM_INSTRUCTIONS` temel alınarak haiku tarzında yanıt veriyor.

## Dayanıklılığı test etme (isteğe bağlı)

Temporal'ı temel almak, temsilcinizin hatalardan sorunsuz bir şekilde kurtulmasını sağlar. Bunu iki ayrı deneme kullanarak test edebilirsiniz.

### Ağ kesintisini simüle etme

Bu testte, bilgisayarınızın internet bağlantısını geçici olarak devre dışı bırakacak, bir iş akışı gönderecek, Temporal'ın otomatik olarak yeniden denemesini izleyecek ve ardından ağın kurtarıldığını görmek için ağı geri yükleyeceksiniz.

1. Makinenizin internet bağlantısını kesin (örneğin, kablosuz ağınızı kapatın).
2. İş akışı gönderme:

   ```
   python -m start_workflow "tell me a joke"
   ```
3. Temporal kullanıcı arayüzünü (`http://localhost:8233`) kontrol edin. LLM etkinliğinin başarısız olduğunu ve Temporal'ın yeniden denemeleri arka planda otomatik olarak yönettiğini görürsünüz.
4. İnternete tekrar bağlanın.
5. Bir sonraki otomatik yeniden deneme, Gemini API'ye başarıyla ulaşacak ve terminaliniz nihai sonucu yazdıracaktır.

### Çalışan kilitlenmesinden kurtulma

Bu testte, çalışan yürütülürken sonlandırılır ve yeniden başlatılır. Temporal, iş akışı geçmişini (olay kaynağı) yeniden oynatır ve son tamamlanan etkinlikten devam eder. Önceden tamamlanmış LLM çağrıları ve araç çağrıları tekrarlanmaz.

1. Çalışanı sonlandırmak için kendinize zaman tanımak istiyorsanız `durable_agent_worker.py` dosyasını açın ve `AgentWorkflow`
   `run` döngüsünde `await asyncio.sleep(10)` yorumunu geçici olarak kaldırın.
2. Çalışanı yeniden başlatın:

   ```
   python -m durable_agent_worker
   ```
3. Birden fazla aracı tetikleyen bir sorgu gönderin:

   ```
   python -m start_workflow "are there any weather alerts where I am?"
   ```
4. Çalışan işlemini tamamlanmadan önce istediğiniz zaman sonlandırın (çalışan terminalinde `Ctrl-C` veya arka planda çalışıyorsa `kill %1` kullanılarak).
5. Çalışanı yeniden başlatın:

   ```
   python -m durable_agent_worker
   ```

Temporal, iş akışı geçmişini yeniden oynatır. Daha önce tamamlanmış olan LLM çağrıları ve araç çağırmaları **yeniden** yürütülmez. Sonuçları, geçmişten (olay günlüğü) anında yeniden oynatılır. İş akışı başarıyla tamamlanır.

## Diğer kaynaklar

- [Temporal dokümanları](https://docs.temporal.io/)
- [Temporal Python SDK](https://docs.temporal.io/develop/python)
- [Google GenAI SDK'sı](https://googleapis.github.io/python-genai/)
- [Bu eğitim için kaynak kodu](https://github.com/temporal-community/durable-react-agent-gemini)

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-04-29 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-04-29 UTC."],[],[]]
