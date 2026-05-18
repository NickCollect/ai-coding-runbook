---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=pt-BR
fetched_at: 2026-05-18T05:18:50.556476+00:00
title: "Get started with Gemini Live API using the Google GenAI SDK \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Get started with Gemini Live API using the Google GenAI SDK

A API Gemini Live permite a interação bidirecional em tempo real com os modelos do Gemini, oferecendo suporte a entradas de áudio, vídeo e texto, além de saídas de áudio nativas. Neste guia, explicamos como fazer a integração com a API usando o SDK da GenAI do Google no seu servidor.

[Testar a API Live no Google AI Studiomic](https://aistudio.google.com/live?hl=pt-br)
[Clonar o app de exemplo do GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-genai-python-sdk)
[Usar as habilidades do agente de programaçãoterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=pt-br)

## Visão geral

A API Gemini Live usa WebSockets para comunicação em tempo real. O SDK do `google-genai` oferece uma interface assíncrona de alto nível para gerenciar essas conexões.

Principais conceitos:

- **Sessão**: uma conexão persistente com o modelo.
- **Config**: configuração de modalidades (áudio/texto), voz e instruções do sistema.
- **Entrada em tempo real**: envio de frames de áudio e vídeo como blobs.

## Como se conectar à API Live

Inicie uma sessão da API Live com uma chave de API:

### Python

```
import asyncio
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

model = "gemini-3.1-flash-live-preview"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY"});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        console.debug(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  console.debug("Session started");
  // Send content...

  session.close();
}

main();
```

## Enviando texto

O texto pode ser enviado usando `send_realtime_input` (Python) ou `sendRealtimeInput` (JavaScript).

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### JavaScript

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

## Enviando áudio

O áudio precisa ser enviado como dados PCM brutos (áudio PCM bruto de 16 bits, 16 kHz, little endian).

### Python

```
# Assuming 'chunk' is your raw PCM audio bytes
await session.send_realtime_input(
    audio=types.Blob(
        data=chunk,
        mime_type="audio/pcm;rate=16000"
    )
)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

Para um exemplo de como receber o áudio do dispositivo cliente (por exemplo, o navegador),
consulte o exemplo completo no [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L31-L70).

## Enviando vídeo

Os frames de vídeo são enviados como imagens individuais (por exemplo, JPEG ou PNG) em uma taxa de frames específica (máximo de 1 frame por segundo).

### Python

```
# Assuming 'frame' is your JPEG-encoded image bytes
await session.send_realtime_input(
    video=types.Blob(
        data=frame,
        mime_type="image/jpeg"
    )
)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

Para ver um exemplo de como extrair o vídeo do dispositivo cliente (por exemplo, o navegador),
consulte o exemplo completo no [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L84-L120).

## Recebendo áudio

As respostas de áudio do modelo são recebidas como blocos de dados.

### Python

```
async for response in session.receive():
    if response.server_content and response.server_content.model_turn:
        for part in response.server_content.model_turn.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                # Process or play the audio data
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data;
      // Process or play audioData (base64 encoded string)
    }
  }
}
```

Consulte o app de exemplo no GitHub para saber como [receber o áudio no seu servidor](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/gemini_live.py#L86-L98) e [reproduzi-lo no navegador](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L145-L174).

## Recebendo texto

As transcrições da entrada do usuário e da saída do modelo estão disponíveis no conteúdo do servidor.

### Python

```
async for response in session.receive():
    content = response.server_content
    if content:
        if content.input_transcription:
            print(f"User: {content.input_transcription.text}")
        if content.output_transcription:
            print(f"Gemini: {content.output_transcription.text}")
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.inputTranscription) {
  console.log('User:', content.inputTranscription.text);
}
if (content?.outputTranscription) {
  console.log('Gemini:', content.outputTranscription.text);
}
```

## Como processar chamadas de ferramentas

A API é compatível com a chamada de ferramentas (chamada de função). Quando o modelo solicita uma chamada de ferramenta, você precisa executar a função e enviar a resposta de volta.

### Python

```
async for response in session.receive():
    if response.tool_call:
        function_responses = []
        for fc in response.tool_call.function_calls:
            # 1. Execute the function locally
            result = my_tool_function(**fc.args)

            # 2. Prepare the response
            function_responses.append(types.FunctionResponse(
                name=fc.name,
                id=fc.id,
                response={"result": result}
            ))

        # 3. Send the tool response back to the session
        await session.send_tool_response(function_responses=function_responses)
```

### JavaScript

```
// Inside the onmessage callback
if (response.toolCall) {
  const functionResponses = [];
  for (const fc of response.toolCall.functionCalls) {
    const result = myToolFunction(fc.args);
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }
  session.sendToolResponse({ functionResponses });
}
```

## A seguir

- Leia o guia completo de [Recursos](https://ai.google.dev/gemini-api/docs/live-guide?hl=pt-br) da API Live para conhecer os principais recursos e configurações, incluindo detecção de atividade de voz e recursos de áudio nativos.
- Leia o guia [Uso de ferramentas](https://ai.google.dev/gemini-api/docs/live-tools?hl=pt-br) para saber como integrar a API Live com ferramentas e chamadas de função.
- Leia o guia [Gerenciamento de sessões](https://ai.google.dev/gemini-api/docs/live-session?hl=pt-br) para gerenciar conversas longas.
- Leia o guia [Tokens efêmeros](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=pt-br) para autenticação segura em aplicativos [cliente-servidor](#implementation-approach).
- Para mais informações sobre a API WebSockets subjacente, consulte a [referência da API WebSockets](https://ai.google.dev/api/live?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-13 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-13 UTC."],[],[]]
