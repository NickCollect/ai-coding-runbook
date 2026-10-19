---
source_url: https://ai.google.dev/gemini-api/docs/temporal-example?hl=pt-BR
fetched_at: 2026-10-19T05:36:44.851443+00:00
title: "Agente de IA dur\u00e1vel com Gemini e Temporal \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Agente de IA durável com Gemini e Temporal

Neste tutorial, você vai aprender a criar um loop de agente [estilo ReAct](https://arxiv.org/abs/2210.03629) que usa a API Gemini para raciocínio e o [Temporal](https://temporal.io/) para durabilidade.
O código-fonte completo deste tutorial está disponível no
[GitHub](https://github.com/temporal-community/durable-react-agent-gemini).

O agente pode chamar ferramentas, como pesquisar alertas de clima ou geolocalizar um endereço IP, e vai repetir o processo até ter informações suficientes para responder.

O que diferencia isso de uma demonstração típica de agente é a **durabilidade**. Cada chamada de LLM, cada invocação de ferramenta e cada etapa do loop do agente são mantidas pelo Temporal. Se o processo falhar, a rede cair ou uma API atingir o tempo limite,
o Temporal vai tentar novamente e retomar automaticamente da última etapa concluída. Nenhum histórico de conversas é perdido, e nenhuma chamada de ferramenta é repetida incorretamente.

## Arquitetura

A arquitetura consiste em três partes:

- **Fluxo de trabalho**:o loop agêntico que orquestra a lógica de execução.
- **Atividades**:unidades individuais de trabalho (chamadas de LLM, chamadas de ferramentas) que o Temporal torna duráveis.
- **Worker**:o processo que executa os fluxos de trabalho e as atividades.

Neste exemplo, você vai colocar todas as três partes em um único arquivo (`durable_agent_worker.py`). Em uma implementação real, você as separaria para permitir várias vantagens de implantação e escalonabilidade. Você vai colocar o código que fornece um comando ao agente em um segundo arquivo (`start_workflow.py`).

## Pré-requisitos

Para concluir este guia, você vai precisar do seguinte:

- Uma chave da API Gemini. Você pode criar uma sem custo financeiro no
  [Google AI Studio](https://aistudio.google.com/apikey?hl=pt-br).
- [Python](https://www.python.org/downloads/) versão 3.10 ou mais recente.
- A [CLI do Temporal](https://docs.temporal.io/cli) para executar um servidor de desenvolvimento local.

## Configuração

Antes de começar, verifique se você tem um
[servidor de desenvolvimento do Temporal](https://docs.temporal.io/cli#start-dev-server)
em execução localmente:

```
temporal server start-dev
```

Em seguida, instale as dependências necessárias:

```
pip install temporalio google-genai httpx pydantic python-dotenv
```

Crie um arquivo `.env` no diretório do projeto com sua chave de API Gemini. Você
pode receber uma chave de API do
[Google AI Studio](https://aistudio.google.com/apikey?hl=pt-br).

```
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

## Implementação

O restante deste tutorial explica o `durable_agent_worker.py` de cima para baixo, criando o agente parte por parte. Crie o arquivo e acompanhe.

### Importações e configuração de sandbox

Comece com as importações que precisam ser definidas antecipadamente. O bloco
`workflow.unsafe.imports_passed_through()` instrui a sandbox de fluxo de trabalho do Temporal
a permitir que determinados módulos passem sem restrições. Isso é necessário porque várias bibliotecas (principalmente `httpx`, que cria subclasses de `urllib.request.Request`) usam padrões que o sandbox bloquearia.

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

### Instruções do sistema

Em seguida, defina a personalidade do agente. As instruções do sistema informam ao modelo como
se comportar. O agente foi instruído a responder em haicais quando nenhuma ferramenta é necessária.

```
SYSTEM_INSTRUCTIONS = """
You are a helpful agent that can use tools to help the user.
You will be given an input from the user and a list of tools to use.
You may or may not need to use the tools to satisfy the user ask.
If no tools are needed, respond in haikus.
"""
```

### Definições de ferramentas

Agora, defina as ferramentas que o agente pode usar. Cada ferramenta é uma função assíncrona com uma
docstring descritiva. As ferramentas que usam parâmetros usam um modelo Pydantic como argumento único. Essa é uma prática recomendada do Temporal que mantém as assinaturas de atividade
estáveis à medida que você adiciona campos opcionais ao longo do tempo.

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

Em seguida, defina ferramentas para geolocalização de endereços IP:

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

### Registro de ferramentas

Em seguida, crie um registro que mapeie nomes de ferramentas para funções de manipulador. A função
`get_tools()` gera objetos `FunctionDeclaration` compatíveis com o Gemini
das chamadas usando `FunctionDeclaration.from_callable_with_api_option()`.

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

### Atividade do LLM

Agora defina a atividade que chama a API Gemini. As classes de dados `GeminiChatRequest` e `GeminiChatResponse` definem o contrato.

Você vai desativar a chamada de função automática para que a invocação do LLM e da ferramenta sejam tratadas como tarefas separadas, aumentando a durabilidade do seu agente. Você também vai desativar as novas tentativas integradas do SDK (`attempts=1`), já que
o Temporal processa as novas tentativas de maneira durável.

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

### Atividade da ferramenta dinâmica

Em seguida, defina a atividade que executa ferramentas. Isso usa o recurso de atividade dinâmica do Temporal: o gerenciador de ferramentas (um objeto invocável) é obtido do registro de ferramentas pela função `get_handler`. Isso permite que diferentes agentes sejam definidos apenas fornecendo um conjunto diferente de ferramentas e instruções do sistema. O fluxo de trabalho que implementa o loop de agente não requer mudanças.

A atividade inspeciona a assinatura do manipulador para determinar como transmitir
argumentos. Se o manipulador esperar um modelo Pydantic, ele vai processar o formato de saída aninhado que o Gemini produz (por exemplo, `{"request": {"state": "CA"}}` em vez de um `{"state": "CA"}` simples).

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

### O fluxo de trabalho de loop com agentes

Agora você tem tudo o que precisa para terminar de criar o agente. A classe `AgentWorkflow` implementa um fluxo de trabalho que contém o ciclo do agente. Nesse loop, o LLM
é invocado por uma atividade (tornando-o durável), a saída é inspecionada e, se uma
ferramenta foi escolhida pelo LLM, ela é invocada pelo `dynamic_tool_activity`.

Neste agente simples de estilo ReAct, quando o LLM decide não usar uma ferramenta, o
loop é considerado concluído e o resultado final do LLM é retornado.

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
                    model="gemini-3.6-flash",
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

O loop de agente é totalmente durável. Se o worker do agente falhar após várias
iterações no loop, o Temporal vai retomar exatamente de onde parou
sem precisar invocar novamente as invocações de LLM ou chamadas de ferramentas já executadas.

### Inicialização do worker

Por fim, conecte tudo. Embora o código implemente a lógica de negócios necessária de maneira que pareça estar sendo executado em um único processo, o uso do Temporal o torna um sistema orientado a eventos (especificamente, originado por eventos), em que a comunicação entre o fluxo de trabalho e as atividades acontece por mensagens fornecidas pelo Temporal.

O worker do Temporal se conecta ao serviço do Temporal e atua como um programador para
as tarefas de fluxo de trabalho e atividade. O worker registra o fluxo de trabalho e as duas
atividades e começa a detectar tarefas.

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

## O script do cliente

Crie o script do cliente (`start_workflow.py`). Ele envia uma consulta e aguarda o resultado. Ele se conecta à mesma fila de tarefas referenciada no worker do agente. O script `start_workflow` envia uma tarefa de fluxo de trabalho com o comando do usuário para essa fila, iniciando a execução do agente.

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

## Run the agent

Se ainda não tiver feito isso, inicie o servidor de desenvolvimento do Temporal:

```
temporal server start-dev
```

Em uma nova janela de terminal, inicie o worker do agente:

```
python -m durable_agent_worker
```

Em uma terceira janela de terminal, envie uma consulta ao seu agente:

```
python -m start_workflow "are there any weather alerts for where I am?"
```

Observe a saída no terminal do `durable_agent_worker`, que mostra as ações que acontecem em cada iteração do loop de agente. O LLM consegue atender à solicitação do usuário invocando uma série de ferramentas disponíveis. Você pode
conferir as etapas executadas na interface do Temporal em
`http://localhost:8233/namespaces/default/workflows`.

Teste alguns comandos diferentes para ver o raciocínio do agente e chamar ferramentas:

```
python -m start_workflow "are there any weather alerts for New York?"
python -m start_workflow "where am I?"
python -m start_workflow "what is my ip address?"
python -m start_workflow "tell me a joke"
```

O último comando não exige ferramentas, então o agente responde com um haicai
baseado no `SYSTEM_INSTRUCTIONS`.

## Testar a durabilidade (opcional)

A criação com base no Temporal garante que seu agente sobreviva a falhas sem problemas. Você pode testar isso usando dois experimentos distintos.

### Como simular uma interrupção de rede

Neste teste, você vai desativar temporariamente a conexão de Internet do computador,
enviar um fluxo de trabalho, observar o Temporal tentar novamente de forma automática e restaurar a
rede para ver a recuperação.

1. Desconecte a máquina da Internet (por exemplo, desative o Wi-Fi).
2. Envie um fluxo de trabalho:

   ```
   python -m start_workflow "tell me a joke"
   ```
3. Verifique a interface do Temporal (`http://localhost:8233`). Você vai notar que a atividade do LLM está falhando e que o Temporal está gerenciando automaticamente as novas tentativas em segundo plano.
4. Conecte-se à Internet novamente.
5. A próxima tentativa automática vai acessar a API Gemini, e seu terminal vai imprimir o resultado final.

### Como sobreviver a uma falha de worker

Neste teste, você vai encerrar o worker no meio da execução e reiniciá-lo. O Temporal reproduz o histórico do fluxo de trabalho (origem de eventos) e retoma da última atividade concluída. As invocações de LLM e as chamadas de ferramentas já concluídas não são repetidas.

1. Para ter tempo de encerrar o worker, abra `durable_agent_worker.py` e remova temporariamente o comentário de `await asyncio.sleep(10)` dentro do laço `AgentWorkflow`
   `run`.
2. Reinicie o worker:

   ```
   python -m durable_agent_worker
   ```
3. Envie uma consulta que acione várias ferramentas:

   ```
   python -m start_workflow "are there any weather alerts where I am?"
   ```
4. Encerre o processo de worker a qualquer momento antes da conclusão (`Ctrl-C` no terminal do worker ou usando `kill %1` se estiver em execução em segundo plano).
5. Reinicie o worker:

   ```
   python -m durable_agent_worker
   ```

O Temporal reproduz o histórico do fluxo de trabalho. As chamadas de LLM e as invocações de ferramentas que já foram concluídas **não** são executadas novamente. Os resultados delas são reproduzidos instantaneamente do histórico (o log de eventos). O fluxo de trabalho é concluído.

## Outros recursos

- [Documentação temporal](https://docs.temporal.io/)
- [SDK do Python do Temporal](https://docs.temporal.io/develop/python)
- [SDK da IA generativa do Google](https://googleapis.github.io/python-genai/)
- [Código-fonte deste tutorial](https://github.com/temporal-community/durable-react-agent-gemini)

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-12 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-12 UTC."],[],[]]
