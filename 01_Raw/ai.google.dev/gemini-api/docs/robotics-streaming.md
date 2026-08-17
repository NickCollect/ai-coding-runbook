---
source_url: https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=pt-BR
fetched_at: 2026-08-17T02:19:32.364466+00:00
title: "Rob\u00f3tica com streaming \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Robótica com streaming

O endpoint do modelo `gemini-robotics-er-2-streaming-preview` expõe um endpoint de streaming dedicado
que se integra à API [Live](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=pt-br), permitindo a interação bidirecional em tempo real
entre o aplicativo e o robô. Isso o torna adequado para agentes que precisam de loops de feedback rápidos e respostas reativas ao ambiente.

[Testar no Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=pt-br)
[Clonar apps de exemplo do GitHub](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## Casos de uso

- **Coordenação de vários robôs**: vários robôs que comunicam o estado da tarefa
  e delegam subtarefas por uma sessão compartilhada.
- **Monitoramento contínuo**: robôs que observam uma cena e acionam ações
  quando eventos específicos ocorrem, como um contêiner atingir um nível de preenchimento.
- **Armazém e logística**: agentes de coleta e embalagem que verificam itens
  visualmente, acompanham o progresso da embalagem e se recuperam de erros.

## Especificações técnicas

A tabela a seguir descreve as especificações técnicas da API Live:

| Categoria | Detalhes |
| --- | --- |
| Modalidades de entrada | Áudio (PCM bruto de 16 bits, 16 kHz, little-endian), imagens (JPEG <= 1 FPS), texto |
| Modalidades de saída | Texto |
| Protocolo | Conexão WebSocket com estado (WSS) |

## Criar uma configuração de agente

Cada agente de robótica criado na API Live segue três etapas:

1. **Declarar os recursos do robô como ferramentas**. Cada ação que o robô pode realizar (navegar, agarrar, falar) se torna uma declaração de função com um nome, descrição e esquema de parâmetros. As ações físicas precisam usar
   `"behavior": "BLOCKING"` para que o modelo espere o robô terminar antes de
   escolher a próxima etapa.
2. **Transmitir entrada multimodal para uma sessão persistente**. Abra uma sessão `live.connect` e mantenha-a aberta durante toda a tarefa. Envie frames de vídeo, áudio ou texto à medida que eles chegam dos sensores do robô.
3. **Processar chamadas de ferramentas em um loop de recebimento**. Cada vez que o modelo seleciona uma ação, ele envia uma mensagem `tool_call`. O loop de recebimento executa a função no SDK do robô e envia um `tool_response`. A sessão permanece aberta, e o modelo escolhe a próxima ação com base no resultado.

As seções a seguir mostram como aplicar essas etapas a três padrões comuns: um loop do agente de linha de base, monitoramento proativo de cenário com um sinal de funcionamento e roteamento de fala por TTS como uma ferramenta.

## Orquestrar um robô por chamada de função

O exemplo a seguir mostra todas as três etapas conectadas em um único script Python.

A etapa 1 (definições de ferramentas) declara os recursos do robô como declarações de função. A função `navigate` usa `"behavior": "BLOCKING"` para que o
modelo espere o robô chegar ao waypoint antes de chamar outra ferramenta.
Adicione mais declarações de função na mesma lista para expor outros recursos do robô.

A etapa 2 (helpers de entrada) mostra três funções que transmitem entradas de modalidades diferentes para a sessão: `send_text` para comandos, `send_image` para frames de câmera com um comando de texto opcional e `send_audio` para áudio PCM bruto de um microfone.

A etapa 3 (o loop de recebimento) é executada simultaneamente e processa dois tipos de mensagens: mensagens `server_content` (a saída de texto do modelo) e mensagens `tool_call` (o modelo solicitando uma ação do robô). Quando uma chamada de ferramenta chega, o loop chama `execute_tool` (um stub que você substitui pelo SDK do robô real) e envia um `tool_response` para que o modelo possa selecionar a próxima ação.

```
import asyncio
from google import genai
from google.genai import types

MODEL = "gemini-robotics-er-2-streaming-preview"

# ── Tool definitions ─────────────────────────────────────────────────────────
tools = [
   {
       "function_declarations": [
           {
               "name": "navigate",
               "description": "Navigate the robot to a named waypoint.",
               "behavior": "BLOCKING",
               "parameters": {
                   "type": "OBJECT",
                   "properties": {"name": {"type": "STRING"}},
                   "required": ["name"],
               },
           },
           # Add more function definitions here
       ]
   }
]

# ── Stub tool executor (replace with real robot SDK calls) ───────────────────
def execute_tool(name: str, args: dict) -> dict:
   print(f"  [Tool] {name}({args})")
   return {"status": "success"}

# ── Input helpers ────────────────────────────────────────────────────────────
def send_text(session, text: str):
   """Send a text turn."""
   return session.send_client_content(
       turns=types.Content(role="user", parts=[types.Part(text=text)]),
       turn_complete=True,
   )

def send_image(session, image_bytes: bytes, prompt: str = ""):
   """Send a JPEG image with an optional text prompt."""
   parts = [
       types.Part(
           inline_data=types.Blob(data=image_bytes, mime_type="image/jpeg")
       )
   ]
   if prompt:
       parts.append(types.Part(text=prompt))
   return session.send_client_content(
       turns=types.Content(role="user", parts=parts),
       turn_complete=True,
   )

def send_audio(session, audio_chunk: bytes):
   """Stream a chunk of raw PCM audio (16-bit, 16 kHz, mono)."""
   return session.send_realtime_input(
       media=types.Blob(data=audio_chunk, mime_type="audio/pcm;rate=16000")
   )

# ── Receive loop ─────────────────────────────────────────────────────────────
async def receive_loop(session):
   """Print model text and handle tool calls until the session ends."""
   async for message in session.receive():
       if message.server_content:
           sc = message.server_content
           if sc.model_turn and sc.model_turn.parts:
               for part in sc.model_turn.parts:
                   if part.text:
                       print(f"Model: {part.text}", end="", flush=True)
           if sc.turn_complete:
               print("\n[Turn Complete]")
       elif message.tool_call:
           responses = []
           for call in message.tool_call.function_calls:
               print(f"\n[Tool Call] {call.name}({call.args})")
               result = execute_tool(call.name, call.args)
               responses.append(
                   types.FunctionResponse(
                       name=call.name,
                       response=result,
                       id=call.id,
                   )
               )
           await session.send_tool_response(function_responses=responses)

# ── Main ─────────────────────────────────────────────────────────────────────
async def main():
   client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
   config = types.LiveConnectConfig(
       response_modalities=["TEXT"],
       tools=tools,
       system_instruction=types.Content(
           parts=[types.Part(text="You are a robot controller. Use tools to execute commands.")]
       ),
   )
   async with client.aio.live.connect(model=MODEL, config=config) as session:
       recv_task = asyncio.create_task(receive_loop(session))
       # Connect robot perception callbacks and user inputs to the helpers above.
       recv_task.cancel()

asyncio.run(main())
```

O loop de recebimento permanece ativo após cada resposta da ferramenta. O modelo constrói e revisa um plano de longo prazo sem que você codifique toda a sequência de ações com antecedência.

## Raciocínio espacial-temporal proativo

A API Live transmite vídeo, mas os frames de vídeo sozinhos não acionam um novo turno de raciocínio. Os frames de vídeo precisam ser acompanhados por um comando de texto ou áudio para acionar uma resposta do modelo. Consulte
[os recursos da API Live](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=pt-br) para
mais detalhes.

Para ativar o raciocínio proativo, implemente um **heartbeat**: envie periodicamente o
frame de câmera mais recente seguido por um comando de texto curto que força o modelo a
inspecionar a cena e tomar uma decisão explícita. A entrada de vídeo é limitada a um frame por segundo.

Adicione essa corrotina ao loop de recebimento da seção anterior. Ela é executada como uma tarefa `asyncio` separada na mesma sessão:

```
async def heartbeat(session, camera):  # camera is your robot camera API
    while True:
        frame = await camera.latest_jpeg()
        await session.send_realtime_input(
            video=types.Blob(data=frame, mime_type="image/jpeg")
        )
        await session.send_realtime_input(
            text=(
                "[HEARTBEAT] If no task is active, call 'ack' and wait for user"
                " input. If a task is active: observe the scene. If the current"
                " step is progressing correctly, call 'ack'. If the current step"
                " is complete, call 'run_instruction' with the next step. If the"
                " overall goal is achieved, call 'reset' and inform the user."
            )
        )
        await asyncio.sleep(1)
```

Não é necessário pausar o heartbeat durante as ações do robô. Quando usado como um
**detector de sucesso implícito**, manter a execução permite que o modelo observe continuamente
a ação em andamento (rastreando se um aperto está seguro, um despejo
está no alvo ou um objeto está se acomodando corretamente) e reaja no momento em que o
resultado fica claro.

As mensagens de heartbeat atuam como turnos de usuário e interrompem a geração de modelos em andamento.
Consulte
[o guia da API Live sobre interrupções](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=pt-br#interruptions)
para entender como a API Live processa esse comportamento.

## Saída de áudio por TTS externo

O Gemini Robotics ER 2 retorna texto. O aplicativo encaminha as respostas concluídas
para um provedor de TTS separado (como
[Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pt-br)) por um callback injetado.
Isso mantém a latência de fala, a seleção de voz e o comportamento de interrupção sob seu controle e permite trocar back-ends de TTS sem mudar a lógica do agente.

Você também pode declarar o TTS como uma ferramenta para que o modelo trate "diga algo" da mesma forma que "mova o braço". Adicione a seguinte declaração de função à lista `tools` da primeira seção:

```
TOOLS = [
    {
        "name": "send_message",
        "description": (
            "Speak a message aloud via TTS, then deliver it to the"
            " specified target. Use target='user' to speak directly"
            " to the user, or a peer agent name (e.g., 'duo') to"
            " communicate with another robot."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "string",
                    "description": "Recipient: 'user' or a peer agent name.",
                },
                "message": {
                    "type": "string",
                    "description": "The message to speak and deliver.",
                },
            },
            "required": ["target", "message"],
        },
    },
]
```

Ao encapsular o TTS em uma declaração de função, o modelo processa a fala pelo mesmo caminho de chamada de ferramenta que qualquer outra ação do robô. O aplicativo atende à chamada com um callback injetado.

## Exemplos no GitHub

Para exemplos de trabalho completos, incluindo a demonstração de busca de lanches do robô Spot e o Tinybot
pan-tilt hello world, consulte
[Exemplos da API Robotics Live](https://github.com/google-gemini/robotics-samples/tree/main/live-api).

## A seguir

- [Entendimento de vídeo](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=pt-br): descoberta de momentos e classificação de progresso.
- [Orquestração de tarefas](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=pt-br): tarefas de longo prazo sem streaming.
- [Visão geral da API Live](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=pt-br): documentação completa da API Live.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-31 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-31 UTC."],[],[]]
