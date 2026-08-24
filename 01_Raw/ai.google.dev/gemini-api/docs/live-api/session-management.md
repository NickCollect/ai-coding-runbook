---
source_url: https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=pt-BR
fetched_at: 2026-08-24T02:33:48.357810+00:00
title: "Gerenciamento de sess\u00f5es com a API Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Gerenciamento de sessões com a API Live

Na API Live, uma sessão se refere a uma conexão
persistente em que a entrada e a saída são transmitidas continuamente pela mesma
conexão. Leia mais sobre [como ela funciona](https://ai.google.dev/gemini-api/docs/live?hl=pt-br).
Esse design de sessão exclusivo permite baixa latência e oferece suporte a recursos exclusivos, mas
também pode apresentar desafios, como limites de tempo de sessão e encerramento antecipado.
Este guia aborda estratégias para superar os desafios de gerenciamento de sessões
que podem surgir ao usar a API Live.

## Ciclo de vida da sessão

Sem compressão, as sessões somente de áudio são limitadas a 15 minutos, e as sessões de áudio e vídeo são limitadas a 2 minutos. Exceder esses limites
encerra a sessão (e, portanto, a conexão), mas é possível usar a [compressão da janela de contexto](#context-window-compression) para estender as sessões por
um período ilimitado.

A vida útil de uma conexão também é limitada a cerca de 10 minutos. Quando a conexão termina, a sessão também é encerrada. Nesse caso, é possível
configurar uma única sessão para ficar ativa em várias conexões usando a
[retomada de sessão](#session-resumption).
Você também vai receber uma [mensagem GoAway](#goaway-message) antes do
término da conexão, permitindo que você tome outras medidas.

## Compactação da janela de contexto

Para ativar sessões mais longas e evitar o encerramento abrupto da conexão, é possível ativar a compactação da janela de contexto definindo o campo [contextWindowCompression](https://ai.google.dev/api/live?hl=pt-br#BidiGenerateContentSetup.FIELDS.ContextWindowCompressionConfig.BidiGenerateContentSetup.context_window_compression) como parte da configuração da sessão.

Em [ContextWindowCompressionConfig](https://ai.google.dev/api/live?hl=pt-br#contextwindowcompressionconfig), é possível configurar um [mecanismo de janela deslizante](https://ai.google.dev/api/live?hl=pt-br#ContextWindowCompressionConfig.FIELDS.ContextWindowCompressionConfig.SlidingWindow.ContextWindowCompressionConfig.sliding_window) e o [número de tokens](https://ai.google.dev/api/live?hl=pt-br#ContextWindowCompressionConfig.FIELDS.int64.ContextWindowCompressionConfig.trigger_tokens) que aciona a compactação.

### Python

```
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    context_window_compression=(
        # Configures compression with default parameters.
        types.ContextWindowCompressionConfig(
            sliding_window=types.SlidingWindow(),
        )
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  contextWindowCompression: { slidingWindow: {} }
};
```

## Retomada da sessão

Para evitar o encerramento da sessão quando o servidor redefine periodicamente a conexão
WebSocket, configure o campo [sessionResumption](https://ai.google.dev/api/live?hl=pt-br#BidiGenerateContentSetup.FIELDS.SessionResumptionConfig.BidiGenerateContentSetup.session_resumption)
na [configuração de configuração](https://ai.google.dev/api/live?hl=pt-br#BidiGenerateContentSetup).

Ao transmitir essa configuração, o servidor envia mensagens [SessionResumptionUpdate](https://ai.google.dev/api/live?hl=pt-br#SessionResumptionUpdate), que podem ser usadas para retomar a sessão transmitindo o último token de retomada como o [`SessionResumptionConfig.handle`](https://ai.google.dev/api/live?hl=pt-br#SessionResumptionConfig.FIELDS.string.SessionResumptionConfig.handle) da conexão subsequente.

Os tokens de retomada são válidos por duas horas após o término das últimas sessões.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

async def main():
    print(f"Connecting to the service with handle {previous_session_handle}...")
    async with client.aio.live.connect(
        model=model,
        config=types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            session_resumption=types.SessionResumptionConfig(
                # The handle of the session to resume is passed here,
                # or else None to start a new session.
                handle=previous_session_handle
            ),
        ),
    ) as session:
        while True:
            await session.send_client_content(
                turns=types.Content(
                    role="user", parts=[types.Part(text="Hello world!")]
                )
            )
            async for message in session.receive():
                # Periodically, the server will send update messages that may
                # contain a handle for the current state of the session.
                if message.session_resumption_update:
                    update = message.session_resumption_update
                    if update.resumable and update.new_handle:
                        # The handle should be retained and linked to the session.
                        return update.new_handle

                # For the purposes of this example, placeholder input is continually fed
                # to the model. In non-sample code, the model inputs would come from
                # the user.
                if message.server_content and message.server_content.turn_complete:
                    break

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

console.debug('Connecting to the service with handle %s...', previousSessionHandle)
const session = await ai.live.connect({
  model: model,
  callbacks: {
    onopen: function () {
      console.debug('Opened');
    },
    onmessage: function (message) {
      responseQueue.push(message);
    },
    onerror: function (e) {
      console.debug('Error:', e.message);
    },
    onclose: function (e) {
      console.debug('Close:', e.reason);
    },
  },
  config: {
    responseModalities: [Modality.AUDIO],
    sessionResumption: { handle: previousSessionHandle }
    // The handle of the session to resume is passed here, or else null to start a new session.
  }
});

const inputTurns = 'Hello how are you?';
session.sendClientContent({ turns: inputTurns });

const turns = await handleTurn();
for (const turn of turns) {
  if (turn.sessionResumptionUpdate) {
    if (turn.sessionResumptionUpdate.resumable && turn.sessionResumptionUpdate.newHandle) {
      let newHandle = turn.sessionResumptionUpdate.newHandle
      // ...Store newHandle and start new session with this handle here
    }
  }
}

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

## Receber uma mensagem antes de a sessão ser desconectada

O servidor envia uma mensagem [GoAway](https://ai.google.dev/api/live?hl=pt-br#GoAway) que indica que a conexão
atual será encerrada em breve. Essa mensagem inclui o [timeLeft](https://ai.google.dev/api/live?hl=pt-br#GoAway.FIELDS.google.protobuf.Duration.GoAway.time_left), que indica o tempo restante e permite que você tome outras medidas antes que a conexão seja encerrada como ABORTED.

### Python

```
async for response in session.receive():
    if response.go_away is not None:
        # The connection will soon be terminated
        print(response.go_away.time_left)
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.goAway) {
    console.debug('Time left: %s\n', turn.goAway.timeLeft);
  }
}
```

## Receber uma mensagem quando a geração for concluída

O servidor envia uma mensagem [generationComplete](https://ai.google.dev/api/live?hl=pt-br#BidiGenerateContentServerContent.FIELDS.bool.BidiGenerateContentServerContent.generation_complete)
que indica que o modelo terminou de gerar a resposta.

### Python

```
async for response in session.receive():
    if response.server_content.generation_complete is True:
        # The generation is complete
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.generationComplete) {
    // The generation is complete
  }
}
```

## A seguir

Confira mais maneiras de trabalhar com a API Live no guia completo de
[Recursos](https://ai.google.dev/gemini-api/docs/live?hl=pt-br),
na página [Uso de ferramentas](https://ai.google.dev/gemini-api/docs/live-tools?hl=pt-br) ou no
[Cookbook da API Live](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-06-01 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-06-01 UTC."],[],[]]
