---
source_url: https://ai.google.dev/gemini-api/docs/temporal-example?hl=pl
fetched_at: 2026-05-05T20:00:21.471158+00:00
title: "Trwa\u0142y agent AI z\u00a0Gemini i\u00a0Temporal \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Trwały agent AI z Gemini i Temporal

Ten samouczek przeprowadzi Cię przez proces tworzenia pętli agentowej w [stylu ReAct](https://arxiv.org/abs/2210.03629), która do rozumowania używa interfejsu Gemini API, a do trwałości – [Temporal](https://temporal.io/).
Pełny kod źródłowy tego samouczka jest dostępny na [GitHub](https://github.com/temporal-community/durable-react-agent-gemini).

Agent może wywoływać narzędzia, np. wyszukiwać alerty pogodowe lub lokalizować adres IP, i będzie to robić, dopóki nie uzyska wystarczającej ilości informacji, aby odpowiedzieć.

Od typowej wersji demonstracyjnej agenta różni się ona **trwałością**. Każde wywołanie LLM, każde wywołanie narzędzia i każdy krok pętli agenta jest utrwalany przez Temporal. Jeśli proces ulegnie awarii, sieć zostanie odłączona lub interfejs API przekroczy limit czasu, Temporal automatycznie ponowi próbę i wznowi działanie od ostatniego ukończonego kroku. Nie utracisz historii rozmów ani nie powtórzysz nieprawidłowo wywołań narzędzi.

## Architektura

Architektura składa się z 3 części:

- **Przepływ pracy:** pętla agenta, która zarządza logiką wykonywania.
- **Aktywności:** poszczególne jednostki pracy (wywołania LLM, wywołania narzędzi), które Temporal sprawia, że są trwałe.
- **Proces roboczy:** proces, który wykonuje przepływy pracy i działania.

W tym przykładzie umieścisz wszystkie 3 elementy w jednym pliku (`durable_agent_worker.py`). W rzeczywistym wdrożeniu rozdzielisz je, aby uzyskać różne korzyści związane z wdrażaniem i skalowalnością. Kod, który dostarcza prompta do agenta, umieścisz w drugim pliku (`start_workflow.py`).

## Wymagania wstępne

Aby skorzystać z tego przewodnika, potrzebujesz:

- Klucz interfejsu Gemini API. Możesz go utworzyć bezpłatnie w [Google AI Studio](https://aistudio.google.com/apikey?hl=pl).
- [Python](https://www.python.org/downloads/) w wersji 3.10 lub nowszej.
- [Temporal CLI](https://docs.temporal.io/cli) do uruchamiania lokalnego serwera programistycznego.

## Konfiguracja

Zanim zaczniesz, upewnij się, że na Twoim komputerze działa [serwer programistyczny Temporal](https://docs.temporal.io/cli#start-dev-server):

```
temporal server start-dev
```

Następnie zainstaluj wymagane zależności:

```
pip install temporalio google-genai httpx pydantic python-dotenv
```

Utwórz w katalogu projektu plik `.env` z kluczem interfejsu Gemini API. Klucz interfejsu API możesz uzyskać w [Google AI Studio](https://aistudio.google.com/apikey?hl=pl).

```
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

## Implementacja

W dalszej części tego samouczka omówimy `durable_agent_worker.py` od góry do dołu, budując agenta krok po kroku. Utwórz plik i postępuj zgodnie z instrukcjami.

### Importowanie i konfigurowanie piaskownicy

Zacznij od importów, które muszą być zdefiniowane z góry. Blok `workflow.unsafe.imports_passed_through()` informuje piaskownicę przepływu pracy Temporal, że niektóre moduły mogą przechodzić bez ograniczeń. Jest to konieczne, ponieważ kilka bibliotek (zwłaszcza `httpx`, która jest podklasą `urllib.request.Request`) używa wzorców, które w innych okolicznościach zostałyby zablokowane przez piaskownicę.

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

### Instrukcje systemowe

Następnie zdefiniuj osobowość agenta. Instrukcje systemowe informują model, jak ma się zachowywać. Ten agent ma odpowiadać w formie haiku, gdy nie są potrzebne żadne narzędzia.

```
SYSTEM_INSTRUCTIONS = """
You are a helpful agent that can use tools to help the user.
You will be given an input from the user and a list of tools to use.
You may or may not need to use the tools to satisfy the user ask.
If no tools are needed, respond in haikus.
"""
```

### Definicje narzędzi

Teraz zdefiniuj narzędzia, z których może korzystać agent. Każde narzędzie to funkcja asynchroniczna z opisowym ciągiem dokumentacyjnym. Narzędzia, które przyjmują parametry, używają modelu Pydantic jako pojedynczego argumentu. Jest to sprawdzona metoda Temporal, która zapewnia stabilność sygnatur aktywności w miarę dodawania pól opcjonalnych.

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

Następnie zdefiniuj narzędzia do geolokalizacji adresów IP:

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

### Rejestr narzędzi

Następnie utwórz rejestr, który mapuje nazwy narzędzi na funkcje obsługi. Funkcja
`get_tools()` generuje obiekty `FunctionDeclaration` zgodne z Gemini z obiektów wywoływalnych za pomocą `FunctionDeclaration.from_callable_with_api_option()`.

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

### Aktywność LLM

Teraz zdefiniuj aktywność, która wywołuje interfejs Gemini API. `GeminiChatRequest` i `GeminiChatResponse` definiują umowę.

Wyłączysz automatyczne wywoływanie funkcji, aby wywołanie modelu LLM i wywołanie narzędzia były traktowane jako oddzielne zadania, co zwiększy trwałość agenta. Wyłączysz też wbudowane ponawianie prób w pakiecie SDK (`attempts=1`), ponieważ Temporal trwale obsługuje ponawianie prób.

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

### Aktywność narzędzia dynamicznego

Następnie zdefiniuj aktywność, która wykonuje narzędzia. Korzysta z funkcji dynamicznej aktywności Temporal: moduł obsługi narzędzia (funkcja wywoływalna) jest pobierany z rejestru narzędzi za pomocą funkcji `get_handler`. Dzięki temu można definiować różne rodzaje agentów, podając po prostu inny zestaw narzędzi i instrukcji systemowych. W przypadku przepływu pracy implementującego pętlę agenta nie trzeba wprowadzać żadnych zmian.

Działanie sprawdza sygnaturę modułu obsługi, aby określić sposób przekazywania argumentów. Jeśli moduł obsługi oczekuje modelu Pydantic, obsługuje zagnieżdżony format danych wyjściowych generowany przez Gemini (np. `{"request": {"state": "CA"}}` zamiast płaskiego `{"state": "CA"}`).

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

### Przepływ pracy w pętli agentowej

Masz już wszystkie elementy potrzebne do ukończenia tworzenia agenta. Klasa `AgentWorkflow`
implementuje przepływ pracy zawierający pętlę agenta. W tej pętli model LLM jest wywoływany za pomocą działania (co sprawia, że jest trwały), jego dane wyjściowe są sprawdzane, a jeśli model LLM wybrał narzędzie, jest ono wywoływane za pomocą funkcji `dynamic_tool_activity`.

W tym prostym agencie w stylu ReAct, gdy model LLM zdecyduje, że nie będzie używać narzędzia, pętla jest uznawana za zakończoną i zwracany jest ostateczny wynik modelu LLM.

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

Pętla agenta jest w pełni trwała. Jeśli po kilku iteracjach pętli proces roboczy agenta ulegnie awarii, Temporal wznowi działanie dokładnie w miejscu, w którym zostało przerwane, bez konieczności ponownego wywoływania już wykonanych wywołań LLM ani wywołań narzędzi.

### Uruchamianie instancji roboczej

Na koniec połącz wszystko przewodami. Chociaż kod implementuje niezbędną logikę biznesową w sposób, który sprawia, że wydaje się on działać w ramach jednego procesu, użycie Temporal sprawia, że jest to system oparty na zdarzeniach (a konkretnie na źródłach zdarzeń), w którym komunikacja między przepływem pracy a aktywnościami odbywa się za pomocą wiadomości dostarczanych przez Temporal.

Instancja robocza Temporal łączy się z usługą Temporal i działa jako harmonogram zadań przepływu pracy i aktywności. Proces roboczy rejestruje przepływ pracy i oba działania, a następnie zaczyna nasłuchiwać zadań.

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

## Skrypt klienta

Utwórz skrypt klienta (`start_workflow.py`). Wysyła on zapytanie i czeka na wynik. Zwróć uwagę, że łączy się on z tą samą kolejką zadań, do której odwołuje się skrypt `start_workflow` agenta. Skrypt wysyła do tej kolejki zadanie przepływu pracy z promptem użytkownika, co inicjuje wykonanie agenta.

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

## Uruchom agenta

Jeśli jeszcze tego nie zrobisz, uruchom serwer programistyczny Temporal:

```
temporal server start-dev
```

W nowym oknie terminala uruchom proces roboczy agenta:

```
python -m durable_agent_worker
```

W trzecim oknie terminala prześlij zapytanie do agenta:

```
python -m start_workflow "are there any weather alerts for where I am?"
```

Zwróć uwagę na dane wyjściowe w terminalu `durable_agent_worker`, które pokazują działania wykonywane w każdej iteracji pętli agenta. LLM może spełnić prośbę użytkownika, wywołując serię dostępnych narzędzi. Wykonane kroki możesz zobaczyć w interfejsie Temporal pod adresem `http://localhost:8233/namespaces/default/workflows`.

Wypróbuj kilka różnych promptów, aby zobaczyć uzasadnienie agenta i narzędzia do połączeń:

```
python -m start_workflow "are there any weather alerts for New York?"
python -m start_workflow "where am I?"
python -m start_workflow "what is my ip address?"
python -m start_workflow "tell me a joke"
```

Ostatni prompt nie wymaga żadnych narzędzi, więc agent odpowiada w formie haiku na podstawie `SYSTEM_INSTRUCTIONS`.

## Testowanie trwałości (opcjonalnie)

Korzystanie z Temporal zapewnia płynne działanie agenta w przypadku awarii. Możesz to sprawdzić za pomocą 2 różnych eksperymentów.

### Symulowanie awarii sieci

W tym teście tymczasowo wyłączysz połączenie komputera z internetem, prześlesz przepływ pracy, zobaczysz, jak Temporal automatycznie ponawia próbę, a następnie przywrócisz sieć, aby sprawdzić, czy wszystko wróci do normy.

1. Odłącz urządzenie od internetu (np. wyłącz Wi-Fi).
2. Prześlij przepływ pracy:

   ```
   python -m start_workflow "tell me a joke"
   ```
3. Sprawdź interfejs Temporal (`http://localhost:8233`). Zobaczysz, że aktywność LLM się nie powiodła, a Temporal automatycznie zarządza ponownymi próbami w tle.
4. Połącz się ponownie z internetem.
5. Następna automatyczna próba ponowienia zakończy się powodzeniem i uzyska dostęp do interfejsu Gemini API, a terminal wyświetli ostateczny wynik.

### Przetrwanie awarii instancji roboczej

W tym teście zabijesz instancję roboczą w trakcie wykonywania i ponownie ją uruchomisz. Temporal odtwarza historię przepływu pracy (źródło zdarzeń) i wznawia działanie od ostatniej ukończonej aktywności – wywołania LLM i wywołania narzędzi, które zostały już wykonane, nie są powtarzane.

1. Aby dać sobie czas na zakończenie działania worker, otwórz `durable_agent_worker.py` i tymczasowo usuń komentarz z wiersza `await asyncio.sleep(10)` w pętli `AgentWorkflow`
   `run`.
2. Uruchom ponownie instancję roboczą:

   ```
   python -m durable_agent_worker
   ```
3. Prześlij zapytanie, które uruchamia kilka narzędzi:

   ```
   python -m start_workflow "are there any weather alerts where I am?"
   ```
4. Zakończ proces roboczy w dowolnym momencie przed jego ukończeniem (`Ctrl-C` w terminalu roboczym lub za pomocą `kill %1`, jeśli proces jest uruchomiony w tle).
5. Uruchom ponownie instancję roboczą:

   ```
   python -m durable_agent_worker
   ```

Temporal odtwarza historię przepływu pracy. Wywołania LLM i narzędzi, które zostały już ukończone, **nie** są wykonywane ponownie – ich wyniki są natychmiast odtwarzane z historii (dziennika zdarzeń). Przepływ pracy zostanie zakończony.

## Dodatkowe zasoby

- [Dokumentacja czasowa](https://docs.temporal.io/)
- [Temporal Python SDK](https://docs.temporal.io/develop/python)
- [Pakiet SDK Google GenAI](https://googleapis.github.io/python-genai/)
- [Kod źródłowy tego samouczka](https://github.com/temporal-community/durable-react-agent-gemini)

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-04-29 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-04-29 UTC."],[],[]]
