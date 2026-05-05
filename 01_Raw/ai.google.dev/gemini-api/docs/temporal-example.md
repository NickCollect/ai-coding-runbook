---
source_url: https://ai.google.dev/gemini-api/docs/temporal-example?hl=it
fetched_at: 2026-05-05T13:22:51.727837+00:00
title: "Agente AI durevole con Gemini e Temporal \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

- [Home page](https://ai.google.dev/gemini-api/docs/Home page)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Documenti](https://ai.google.dev/gemini-api/docs/Documenti)

Invia feedback

# Agente AI durevole con Gemini e Temporal

Questo tutorial ti guida nella creazione di un
[loop agentico in stile ReAct](https://ai.google.dev/gemini-api/docs/loop agentico in stile ReAct) che utilizza l'
API Gemini per il ragionamento e [Temporal](https://ai.google.dev/gemini-api/docs/Temporal) per la durabilità.
Il codice sorgente completo per questo tutorial è disponibile su
[GitHub](https://ai.google.dev/gemini-api/docs/GitHub).

L'agente può chiamare strumenti, ad esempio cercare avvisi meteo o geolocalizzare un indirizzo IP, e continuerà a eseguire il loop finché non avrà informazioni sufficienti per rispondere.

Ciò che lo distingue da una tipica demo di agenti è la **durabilità**. Ogni chiamata LLM, ogni chiamata di strumenti e ogni passaggio del loop agentico viene mantenuto da Temporal. Se il processo si arresta in modo anomalo, la rete si interrompe o un'API va in timeout, Temporal riprova automaticamente e riprende dall'ultimo passaggio completato. Non viene persa la cronologia delle conversazioni e le chiamate di strumenti non vengono ripetute in modo errato.

## Architettura

L'architettura è composta da tre parti:

- **Workflow**:il loop agentico che orchestra la logica di esecuzione.
- **Attività**:singole unità di lavoro (chiamate LLM, chiamate di strumenti) che Temporal rende durabili.
- **Worker**:il processo che esegue i workflow e le attività.

In questo esempio, inserirai tutti e tre questi elementi in un unico file (`durable_agent_worker.py`). In un'implementazione reale, li separeresti per consentire vari vantaggi di deployment e scalabilità. Inserirai il codice che fornisce un prompt all'agente in un secondo file (`start_workflow.py`).

## Prerequisiti

Per completare questa guida, avrai bisogno di:

- Una chiave API Gemini. Puoi crearne una senza costi in
  [Google AI Studio](https://ai.google.dev/gemini-api/docs/Google AI Studio).
- [Python](https://ai.google.dev/gemini-api/docs/Python) versione 3.10 o successive.
- La [CLI Temporal](https://ai.google.dev/gemini-api/docs/CLI Temporal) per l'esecuzione di un server di sviluppo
  locale.

## Configurazione

Prima di iniziare, assicurati di avere un
[server di sviluppo Temporal](https://ai.google.dev/gemini-api/docs/server di sviluppo Temporal)
in esecuzione localmente:

```
temporal server start-dev
```

Poi, installa le dipendenze richieste:

```
pip install temporalio google-genai httpx pydantic python-dotenv
```

Crea un file `.env` nella directory del progetto con la tua chiave API Gemini. Puoi
ottenere una chiave API da
[Google AI Studio](https://ai.google.dev/gemini-api/docs/Google AI Studio).

```
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

## Implementazione

Il resto di questo tutorial illustra il file `durable_agent_worker.py` dall'inizio alla fine, creando l'agente passo dopo passo. Crea il file e segui le istruzioni.

### Importazioni e configurazione del sandbox

Inizia con le importazioni che devono essere definite in anticipo. Il blocco `workflow.unsafe.imports_passed_through()` indica al sandbox del workflow di Temporal di consentire il passaggio di determinati moduli senza restrizioni. Questo è necessario perché diverse librerie (in particolare `httpx`, che è una sottoclasse di `urllib.request.Request`) utilizzano pattern che altrimenti il sandbox bloccherebbe.

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

### Istruzioni di sistema

Poi, definisci la personalità dell'agente. Le istruzioni di sistema indicano al modello come comportarsi. Questo agente è istruito a rispondere in haiku quando non sono necessari strumenti.

```
SYSTEM_INSTRUCTIONS = """
You are a helpful agent that can use tools to help the user.
You will be given an input from the user and a list of tools to use.
You may or may not need to use the tools to satisfy the user ask.
If no tools are needed, respond in haikus.
"""
```

### Definizioni degli strumenti

Ora definisci gli strumenti che l'agente può utilizzare. Ogni strumento è una funzione asincrona con una stringa di documentazione descrittiva. Gli strumenti che accettano parametri utilizzano un modello Pydantic come singolo argomento. Questa è una best practice di Temporal che mantiene stabili le firme delle attività man mano che aggiungi campi facoltativi nel tempo.

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

Poi, definisci gli strumenti per la geolocalizzazione degli indirizzi IP:

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

### Registro degli strumenti

Poi, crea un registro che mappa i nomi degli strumenti alle funzioni di gestione. La funzione
`get_tools()` genera oggetti `FunctionDeclaration` compatibili con Gemini
dai callable utilizzando `FunctionDeclaration.from_callable_with_api_option()`.

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

### Attività LLM

Ora definisci l'attività che chiama l'API Gemini. Le classi di dati `GeminiChatRequest` e `GeminiChatResponse` definiscono il contratto.

Disabiliterai la chiamata automatica di funzioni in modo che la chiamata LLM e la chiamata di strumenti vengano gestite come attività separate, aumentando la durabilità dell'agente. Disabiliterai anche i tentativi integrati dell'SDK (`attempts=1`) poiché Temporal gestisce i tentativi in modo duraturo.

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

### Attività di strumenti dinamici

Poi, definisci l'attività che esegue gli strumenti. Questa utilizza la funzionalità di attività dinamica di Temporal: il gestore di strumenti (un callable) viene ottenuto dal registro degli strumenti tramite la funzione `get_handler`. In questo modo è possibile definire agenti diversi semplicemente fornendo un insieme diverso di strumenti e istruzioni di sistema; il workflow che implementa il loop agentico non richiede modifiche.

L'attività esamina la firma del gestore per determinare come passare gli argomenti. Se il gestore prevede un modello Pydantic, gestisce il formato di output
nidificato prodotto da Gemini (ad esempio, `{"request": {"state": "CA"}}` anziché
un formato piatto `{"state": "CA"}`).

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

### Il workflow del loop agentico

Ora hai tutti gli elementi per completare la creazione dell'agente. La classe `AgentWorkflow` implementa un workflow contenente il loop dell'agente. All'interno di questo loop, l'LLM viene chiamato tramite l'attività (rendendolo duraturo), l'output viene esaminato e, se l'LLM ha scelto uno strumento, viene chiamato tramite `dynamic_tool_activity`.

In questo semplice agente in stile ReAct, una volta che l'LLM sceglie di non utilizzare uno strumento, il loop viene considerato completato e viene restituito il risultato finale dell'LLM.

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

Il loop agentico è completamente duraturo. Se il worker dell'agente si arresta in modo anomalo dopo diverse iterazioni del loop, Temporal riprenderà esattamente da dove si era interrotto senza dover richiamare le chiamate LLM o le chiamate di strumenti già eseguite.

### Avvio del worker

Infine, collega tutto. Sebbene il codice implementi la logica di business necessaria in modo da sembrare in esecuzione in un unico processo, l'utilizzo di Temporal lo rende un sistema basato su eventi (in particolare, basato su eventi) in cui la comunicazione tra il workflow e le attività avviene tramite la messaggistica fornita da Temporal.

Il worker Temporal si connette al servizio Temporal e funge da pianificatore per le attività di workflow e attività. Il worker registra il workflow e entrambe le attività, quindi inizia ad ascoltare le attività.

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

## Lo script client

Crea lo script client (`start_workflow.py`). Invia una query e attende il risultato. Tieni presente che si connette alla stessa coda di attività a cui fa riferimento il worker dell'agente: lo script `start_workflow` invia un'attività di workflow con il prompt dell'utente a questa coda di attività, avviando l'esecuzione dell'agente.

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

## Esegui l'agente

Se non l'hai ancora fatto, avvia il server di sviluppo Temporal:

```
temporal server start-dev
```

In una nuova finestra del terminale, avvia il worker dell'agente:

```
python -m durable_agent_worker
```

In una terza finestra del terminale, invia una query all'agente:

```
python -m start_workflow "are there any weather alerts for where I am?"
```

Nota l'output nel terminale di `durable_agent_worker` che mostra le azioni che si verificano in ogni iterazione del loop agentico. L'LLM è in grado di soddisfare la richiesta dell'utente chiamando una serie di strumenti a sua disposizione. Puoi visualizzare i passaggi eseguiti tramite l'interfaccia utente di Temporal all'indirizzo `http://localhost:8233/namespaces/default/workflows`.

Prova alcuni prompt diversi per vedere l'agente ragionare e chiamare gli strumenti:

```
python -m start_workflow "are there any weather alerts for New York?"
python -m start_workflow "where am I?"
python -m start_workflow "what is my ip address?"
python -m start_workflow "tell me a joke"
```

L'ultimo prompt non richiede strumenti, quindi l'agente risponde in un haiku basato su `SYSTEM_INSTRUCTIONS`.

## Testa la durabilità (facoltativo)

La creazione su Temporal garantisce che l'agente sopravviva senza problemi agli errori. Puoi testarlo utilizzando due esperimenti distinti.

### Simulazione di un'interruzione della rete

In questo test, disabiliterai temporaneamente la connessione a internet del computer, invierai un workflow, osserverai Temporal riprovare automaticamente e poi ripristinerai la rete per vederla recuperare.

1. Scollega la macchina da internet (ad esempio, disattiva il Wi-Fi).
2. Invia un workflow:

   ```
   python -m start_workflow "tell me a joke"
   ```
3. Controlla l'interfaccia utente di Temporal (`http://localhost:8233`). Vedrai che l'attività LLM non riesce e che Temporal gestisce automaticamente i tentativi in background.
4. Riconnettiti a internet.
5. Il successivo tentativo automatico raggiungerà correttamente l'API Gemini e il terminale stamperà il risultato finale.

### Superare un arresto anomalo del worker

In questo test, interrompi il worker a metà dell'esecuzione e lo riavvii. Temporal riproduce la cronologia del workflow (origine eventi) e riprende dall'ultima attività completata: le chiamate LLM e le chiamate di strumenti già completate non vengono ripetute.

1. Per darti il tempo di interrompere il worker, apri `durable_agent_worker.py` e rimuovi temporaneamente il commento da `await asyncio.sleep(10)` all'interno del loop `run` di `AgentWorkflow`.
2. Riavvia il worker:

   ```
   python -m durable_agent_worker
   ```
3. Invia una query che attivi diversi strumenti:

   ```
   python -m start_workflow "are there any weather alerts where I am?"
   ```
4. Interrompi il processo worker in qualsiasi momento prima del completamento (`Ctrl-C` nel terminale worker o utilizzando `kill %1` se è in esecuzione in background).
5. Riavvia il worker:

   ```
   python -m durable_agent_worker
   ```

Temporal riproduce la cronologia del workflow. Le chiamate LLM e le chiamate di strumenti già completate **non** vengono eseguite di nuovo: i risultati vengono riprodotti immediatamente dalla cronologia (il log eventi). Il workflow viene completato correttamente.

## Ulteriori risorse

- [Documentazione di Temporal](https://ai.google.dev/gemini-api/docs/Documentazione di Temporal)
- [SDK Python di Temporal](https://ai.google.dev/gemini-api/docs/SDK Python di Temporal)
- [SDK Google GenAI](https://ai.google.dev/gemini-api/docs/SDK Google GenAI)
- [Codice sorgente per questo tutorial](https://ai.google.dev/gemini-api/docs/Codice sorgente per questo tutorial)

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://ai.google.dev/gemini-api/docs/licenza Creative Commons Attribution 4.0), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://ai.google.dev/gemini-api/docs/licenza Apache 2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://ai.google.dev/gemini-api/docs/norme del sito di Google Developers). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-04-29 UTC.

Vuoi dirci altro?
