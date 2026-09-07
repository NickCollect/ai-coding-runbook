---
source_url: https://ai.google.dev/gemini-api/docs/llama-index?hl=tr
fetched_at: 2026-09-07T05:34:53.483937+00:00
title: "Gemini ve LlamaIndex ile ara\u015ft\u0131rma temsilcisi \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini ve LlamaIndex ile araştırma temsilcisi

LlamaIndex, verilerinize bağlı LLM'leri kullanarak bilgi aracıları oluşturmaya yönelik bir çerçevedir. Bu örnekte, bir Araştırma Ajanı için çoklu ajan iş akışının nasıl oluşturulacağı gösterilmektedir. LlamaIndex'te [`Workflows`](https://docs.llamaindex.ai/en/stable/module_guides/workflow/), temsilci ve çoklu temsilci sistemlerinin yapı taşlarıdır.

Gemini API anahtarına ihtiyacınız vardır. Henüz bir hesabınız yoksa [Google AI Studio'da hesap oluşturabilirsiniz](https://aistudio.google.com/apikey?hl=tr).
Öncelikle, gerekli tüm LlamaIndex kitaplıklarını yükleyin. LlamaIndex, arka planda `google-genai` paketini kullanır.

```
pip install llama-index llama-index-utils-workflow llama-index-llms-google-genai llama-index-tools-google
```

## LlamaIndex'te Gemini'ı kurma

Herhangi bir LlamaIndex aracının motoru, akıl yürütme ve metin işlemeyi gerçekleştiren bir LLM'dir. Bu örnekte Gemini 3 Flash kullanılmaktadır. [API anahtarınızı ortam değişkeni olarak ayarladığınızdan](https://ai.google.dev/gemini-api/docs/api-key?hl=tr) emin olun.

```
import os
from llama_index.llms.google_genai import GoogleGenAI

# Set your API key in the environment elsewhere, or with os.environ['GEMINI_API_KEY'] = '...'
assert 'GEMINI_API_KEY' in os.environ

llm = GoogleGenAI(model="gemini-3.5-flash")
```

## Derleme araçları

Aracı, web'de arama yapmak veya bilgi depolamak gibi dış dünyayla etkileşim kurmak için araçları kullanır. [LlamaIndex'teki araçlar](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/)
normal Python işlevleri olabilir veya önceden var olan `ToolSpecs`'dan içe aktarılabilir.
Gemini, Google Arama'yı kullanmak için yerleşik bir araçla birlikte gelir. Burada bu araç kullanılır.

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

Şimdi LLM örneğini arama gerektiren bir sorguyla test edin. Bu kılavuzda, çalışan bir etkinlik döngüsü (ör. `python -m asyncio` veya Google Colab) olduğu varsayılır.

```
response = await llm_with_search.acomplete("What's the weather like today in Biarritz?")
print(response)
```

Araştırma Aracısı, Python işlevlerini araç olarak kullanır. Bu görevi gerçekleştirecek bir sistem oluşturmanın birçok yolu vardır. Bu örnekte aşağıdakileri kullanacaksınız:

1. `search_web`, verilen konuyla ilgili bilgileri web'de aramak için Google Arama ile Gemini'ı kullanır.
2. `record_notes`, web'de bulunan araştırmaları diğer araçların kullanabilmesi için duruma kaydeder.
3. `write_report`, `ResearchAgent` tarafından bulunan bilgileri kullanarak raporu yazar.
4. `review_report` raporu inceler ve geri bildirim sağlar.

`Context` sınıfı, durumları aracılar/araçlar arasında aktarır ve her aracı, sistemin mevcut durumuna erişebilir.

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

## Birden çok temsilcinin yer aldığı bir asistan oluşturma

Çoklu temsilci sistemi oluşturmak için temsilcileri ve etkileşimlerini tanımlarsınız.
Sisteminizde üç temsilci bulunur:

1. `ResearchAgent`, verilen konuyla ilgili bilgi için web'de arama yapar.
2. `WriteAgent`, `ResearchAgent` tarafından bulunan bilgileri kullanarak raporu yazar.
3. Bir `ReviewAgent` raporu inceler ve geri bildirim sağlar.

Bu örnekte, `AgentWorkflow` sınıfı kullanılarak bu aracıları sırayla yürütecek çok aracılı bir sistem oluşturuluyor. Her aracı, ne yapması gerektiğini söyleyen ve diğer aracılarla nasıl çalışılacağını öneren bir `system_prompt` alır.

İsteğe bağlı olarak, `can_handoff_to` kullanarak çoklu aracı sisteminizin hangi diğer aracılarla konuşabileceğini belirterek sisteminize yardımcı olabilirsiniz (Aksi takdirde, sistem bunu kendi başına bulmaya çalışır).

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

Aracıları tanımladığınıza göre artık `AgentWorkflow` oluşturup uygulayabilirsiniz.

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

İş akışı yürütülürken etkinlikleri, araç çağrılarını ve güncellemeleri konsola aktarabilirsiniz.

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

İş akışı tamamlandıktan sonra raporun nihai çıktısını ve inceleme aracısının nihai inceleme durumunu yazdırabilirsiniz.

```
state = await handler.ctx.store.get("state")
print("Report Content:\n", state["report_content"])
print("\n------------\nFinal Review:\n", state["review"])
```

## Özel iş akışlarıyla daha fazlasını yapın

`AgentWorkflow`, çoklu aracı sistemlerini kullanmaya başlamak için harika bir yöntemdir. Ancak daha fazla kontrole ihtiyacınız varsa ne yapmalısınız? Sıfırdan bir iş akışı oluşturabilirsiniz. Kendi iş akışınızı oluşturmak isteyebileceğiniz bazı nedenler şunlardır:

- **Süreç üzerinde daha fazla kontrol**: Temsilcilerinizin izleyeceği yolu tam olarak belirleyebilirsiniz. Buna döngüler oluşturma, belirli noktalarda kararlar alma veya temsilcilerin farklı görevler üzerinde paralel olarak çalışmasını sağlama dahildir.
- **Karmaşık veriler kullanın**: Düz metnin ötesine geçin. Özel iş akışları, giriş ve çıkışlarınız için JSON nesneleri veya özel sınıflar gibi daha fazla yapılandırılmış veri kullanmanıza olanak tanır.
- **Farklı medya türleriyle çalışma**: Yalnızca metni değil, resimleri, sesleri ve videoları da anlayıp işleyebilen aracılar oluşturun.
- **Daha akıllı planlama**: Temsilciler çalışmaya başlamadan önce ayrıntılı bir plan oluşturan bir iş akışı tasarlayabilirsiniz. Bu özellik, birden fazla adım gerektiren karmaşık görevler için yararlıdır.
- **Kendi kendini düzeltme özelliğini etkinleştirme**: Kendi çalışmalarını inceleyebilen aracılar oluşturun. Çıkış yeterince iyi değilse aracı tekrar deneyebilir ve sonuç mükemmel olana kadar iyileştirme döngüsü oluşturabilir.

LlamaIndex Workflows hakkında daha fazla bilgi edinmek için [LlamaIndex Workflows Belgeleri](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)'ne bakın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-10 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-10 UTC."],[],[]]
