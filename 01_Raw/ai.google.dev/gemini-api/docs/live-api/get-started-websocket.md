---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=pt-BR
fetched_at: 2026-05-18T05:11:21.669268+00:00
title: "Get started with Gemini Live API using WebSockets \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Get started with Gemini Live API using WebSockets

A API Gemini Live permite a interação bidirecional em tempo real com os modelos do Gemini, oferecendo suporte a entradas de áudio, vídeo e texto e saídas de áudio nativas. Este guia explica como fazer a integração diretamente com a API usando WebSockets brutos.

[Testar a API Live no Google AI Studiomic](https://aistudio.google.com/live?hl=pt-br)
[Clonar o app de exemplo do GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-ephemeral-tokens-websocket)
[Usar habilidades do agente de codificaçãoterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=pt-br)

## Visão geral

A API Gemini Live usa WebSockets para comunicação em tempo real. Ao contrário do uso de um SDK, essa abordagem envolve o gerenciamento direto da conexão WebSocket e o envio/recebimento de mensagens em um formato JSON específico definido pela API.

Principais conceitos:

- **Endpoint do WebSocket**: o URL específico para conexão.
- **Formato da mensagem**: toda a comunicação é feita por mensagens JSON em conformidade com as estruturas [`BidiGenerateContentClientMessage`](https://ai.google.dev/api/live?hl=pt-br#bidigeneratecontentclientmessage) e [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=pt-br#bidigeneratecontentservermessage).
- **Gerenciamento de sessões**: você é responsável por manter a conexão WebSocket.

## Autenticação

A autenticação é processada incluindo sua chave de API como um parâmetro de consulta no URL do WebSocket.

O formato do endpoint é:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY
```

Substitua `YOUR_API_KEY` pela sua chave de API.

## Autenticação com tokens efêmeros

Se você estiver usando [tokens efêmeros](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=pt-br), precisará se conectar ao endpoint `v1alpha`.
O token efêmero precisa ser transmitido como um parâmetro de consulta `access_token`.

O formato do endpoint para chaves efêmeras é:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

Substitua `{short-lived-token}` pelo token efêmero real.

## Como se conectar à API Live

Para iniciar uma sessão ao vivo, estabeleça uma conexão WebSocket com o endpoint autenticado.
A primeira mensagem enviada pelo WebSocket precisa ser um [`BidiGenerateContentSetup`](https://ai.google.dev/api/live?hl=pt-br#bidigeneratecontentsetup) contendo a `config`.
Para conferir as opções de configuração completas, consulte a [referência da API Live - WebSockets](https://ai.google.dev/api/live?hl=pt-br).

### Python

```
import asyncio
import websockets
import json

API_KEY = "YOUR_API_KEY"
MODEL_NAME = "gemini-3.1-flash-live-preview"
WS_URL = f"wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key={API_KEY}"

async def connect_and_configure():
    async with websockets.connect(WS_URL) as websocket:
        print("WebSocket Connected")

        # 1. Send the initial configuration
        config_message = {
            "config": {
                "model": f"models/{MODEL_NAME}",
                "responseModalities": ["AUDIO"],
                "systemInstruction": {
                    "parts": [{"text": "You are a helpful assistant."}]
                }
            }
        }
        await websocket.send(json.dumps(config_message))
        print("Configuration sent")

        # Keep the session alive for further interactions
        await asyncio.sleep(3600) # Example: keep open for an hour

async def main():
    await connect_and_configure()

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.1-flash-live-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  // 1. Send the initial configuration
  const configMessage = {
    config: {
      model: `models/${MODEL_NAME}`,
      responseModalities: ['AUDIO'],
      systemInstruction: {
        parts: [{ text: 'You are a helpful assistant.' }]
      }
    }
  };
  websocket.send(JSON.stringify(configMessage));
  console.log('Configuration sent');
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  console.log('Received:', response);
  // Handle different types of responses here
};

websocket.onerror = (error) => {
  console.error('WebSocket Error:', error);
};

websocket.onclose = () => {
  console.log('WebSocket Closed');
};
```

## Enviando texto

Para enviar a entrada de texto, crie uma [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=pt-br#bidigeneratecontentrealtimeinput) mensagem com o `text` campo.

### Python

```
# Inside the websocket context
async def send_text(websocket, text):
    text_message = {
        "realtimeInput": {
            "text": text
        }
    }
    await websocket.send(json.dumps(text_message))
    print(f"Sent text: {text}")

# Example usage: await send_text(websocket, "Hello, how are you?")
```

### JavaScript

```
function sendTextMessage(text) {
  if (websocket.readyState === WebSocket.OPEN) {
    const textMessage = {
      realtimeInput: {
        text: text
      }
    };
    websocket.send(JSON.stringify(textMessage));
    console.log('Text message sent:', text);
  } else {
    console.warn('WebSocket not open.');
  }
}

// Example usage:
sendTextMessage("Hello, how are you?");
```

## Enviando áudio

O áudio precisa ser enviado como dados PCM brutos (áudio PCM bruto de 16 bits, 16 kHz, little-endian). Crie uma [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=pt-br#bidigeneratecontentrealtimeinput) mensagem com os dados de áudio. O `mimeType` é essencial.

### Python

```
# Inside the websocket context
async def send_audio_chunk(websocket, chunk_bytes):
    import base64
    encoded_data = base64.b64encode(chunk_bytes).decode('utf-8')
    audio_message = {
        "realtimeInput": {
            "audio": {
                "data": encoded_data,
                "mimeType": "audio/pcm;rate=16000"
            }
        }
    }
    await websocket.send(json.dumps(audio_message))
    # print("Sent audio chunk") # Avoid excessive logging

# Assuming 'chunk' is your raw PCM audio bytes
# await send_audio_chunk(websocket, chunk)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
function sendAudioChunk(chunk) {
  if (websocket.readyState === WebSocket.OPEN) {
    const audioMessage = {
      realtimeInput: {
        audio: {
          data: chunk.toString('base64'),
          mimeType: 'audio/pcm;rate=16000'
        }
      }
    };
    websocket.send(JSON.stringify(audioMessage));
    // console.log('Sent audio chunk');
  }
}
// Example usage: sendAudioChunk(audioBuffer);
```

Para conferir um exemplo de como receber o áudio do dispositivo cliente (por exemplo, o navegador),
consulte o exemplo completo no [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L38-L74).

## Enviando vídeo

Os frames de vídeo são enviados como imagens individuais (por exemplo, JPEG ou PNG). Assim como o áudio, use `realtimeInput` com um `Blob`, especificando o `mimeType` correto.

### Python

```
# Inside the websocket context
async def send_video_frame(websocket, frame_bytes, mime_type="image/jpeg"):
    import base64
    encoded_data = base64.b64encode(frame_bytes).decode('utf-8')
    video_message = {
        "realtimeInput": {
            "video": {
                "data": encoded_data,
                "mimeType": mime_type
            }
        }
    }
    await websocket.send(json.dumps(video_message))
    # print("Sent video frame")

# Assuming 'frame' is your JPEG-encoded image bytes
# await send_video_frame(websocket, frame)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
function sendVideoFrame(frame, mimeType = 'image/jpeg') {
  if (websocket.readyState === WebSocket.OPEN) {
    const videoMessage = {
      realtimeInput: {
        video: {
          data: frame.toString('base64'),
          mimeType: mimeType
        }
      }
    };
    websocket.send(JSON.stringify(videoMessage));
    // console.log('Sent video frame');
  }
}
// Example usage: sendVideoFrame(jpegBuffer);
```

Para conferir um exemplo de como receber o vídeo do dispositivo cliente (por exemplo, o navegador),
consulte o exemplo completo no [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L185-L222).

## Recebimento das respostas

O WebSocket vai enviar [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=pt-br#bidigeneratecontentservermessage) mensagens. Você precisa analisar essas mensagens JSON e processar diferentes tipos de conteúdo.

### Python

```
# Inside the websocket context, in a receive loop
async def receive_loop(websocket):
    async for message in websocket:
        response = json.loads(message)
        print("Received:", response)

        if "serverContent" in response:
            server_content = response["serverContent"]
            # Receiving Audio
            if "modelTurn" in server_content and "parts" in server_content["modelTurn"]:
                for part in server_content["modelTurn"]["parts"]:
                    if "inlineData" in part:
                        audio_data_b64 = part["inlineData"]["data"]
                        # Process or play the base64 encoded audio data
                        # audio_data = base64.b64decode(audio_data_b64)
                        print(f"Received audio data (base64 len: {len(audio_data_b64)})")

            # Receiving Text Transcriptions
            if "inputTranscription" in server_content:
                print(f"User: {server_content['inputTranscription']['text']}")
            if "outputTranscription" in server_content:
                print(f"Gemini: {server_content['outputTranscription']['text']}")

        # Handling Tool Calls
        if "toolCall" in response:
            await handle_tool_call(websocket, response["toolCall"])

# Example usage: await receive_loop(websocket)
```

### JavaScript

```
websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  console.log('Received:', response);

  if (response.serverContent) {
    const serverContent = response.serverContent;
    // Receiving Audio
    if (serverContent.modelTurn?.parts) {
      for (const part of serverContent.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data; // Base64 encoded string
          // Process or play audioData
          console.log(`Received audio data (base64 len: ${audioData.length})`);
        }
      }
    }

    // Receiving Text Transcriptions
    if (serverContent.inputTranscription) {
      console.log('User:', serverContent.inputTranscription.text);
    }
    if (serverContent.outputTranscription) {
      console.log('Gemini:', serverContent.outputTranscription.text);
    }
  }

  // Handling Tool Calls
  if (response.toolCall) {
    handleToolCall(response.toolCall);
  }
};
```

Para conferir um exemplo de como processar a resposta, consulte o exemplo completo no [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/geminilive.js#L22-L75).

## Como processar chamadas de ferramentas

Quando o modelo solicita uma chamada de ferramenta, o [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=pt-br#bidigeneratecontentservermessage) contém um campo `toolCall`. Você precisa executar a função localmente e enviar o resultado de volta ao WebSocket usando uma [`BidiGenerateContentToolResponse`](https://ai.google.dev/api/live?hl=pt-br#bidigeneratecontenttoolresponse) mensagem.

### Python

```
# Placeholder for your tool function
def my_tool_function(args):
    print(f"Executing tool with args: {args}")
    # Implement your tool logic here
    return {"status": "success", "data": "some result"}

async def handle_tool_call(websocket, tool_call):
    function_responses = []
    for fc in tool_call["functionCalls"]:
        # 1. Execute the function locally
        try:
            result = my_tool_function(fc.get("args", {}))
            response_data = {"result": result}
        except Exception as e:
            print(f"Error executing tool {fc['name']}: {e}")
            response_data = {"error": str(e)}

        # 2. Prepare the response
        function_responses.append({
            "name": fc["name"],
            "id": fc["id"],
            "response": response_data
        })

    # 3. Send the tool response back to the session
    tool_response_message = {
        "toolResponse": {
            "functionResponses": function_responses
        }
    }
    await websocket.send(json.dumps(tool_response_message))
    print("Sent tool response")

# This function is called within the receive_loop when a toolCall is detected.
```

### JavaScript

```
// Placeholder for your tool function
function myToolFunction(args) {
  console.log(`Executing tool with args:`, args);
  // Implement your tool logic here
  return { status: 'success', data: 'some result' };
}

function handleToolCall(toolCall) {
  const functionResponses = [];
  for (const fc of toolCall.functionCalls) {
    // 1. Execute the function locally
    let result;
    try {
      result = myToolFunction(fc.args || {});
    } catch (e) {
      console.error(`Error executing tool ${fc.name}:`, e);
      result = { error: e.message };
    }

    // 2. Prepare the response
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }

  // 3. Send the tool response back to the session
  if (websocket.readyState === WebSocket.OPEN) {
    const toolResponseMessage = {
      toolResponse: {
        functionResponses: functionResponses
      }
    };
    websocket.send(JSON.stringify(toolResponseMessage));
    console.log('Sent tool response');
  } else {
    console.warn('WebSocket not open to send tool response.');
  }
}
// This function is called within websocket.onmessage when a toolCall is detected.
```

## A seguir

- Leia o guia completo de [recursos](https://ai.google.dev/gemini-api/docs/live-guide?hl=pt-br) da API Live para conferir os principais recursos e configurações, incluindo a detecção de atividade de voz e recursos de áudio nativos.
- Leia o [guia de uso de ferramentas](https://ai.google.dev/gemini-api/docs/live-tools?hl=pt-br) para saber como integrar a API Live com ferramentas e chamadas de função.
- Leia o [guia de gerenciamento de sessões](https://ai.google.dev/gemini-api/docs/live-session?hl=pt-br) para gerenciar conversas longas.
- Leia o guia de [tokens efêmeros](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=pt-br) para autenticação segura em aplicativos [cliente-servidor](#implementation-approach).
- Para mais informações sobre a API WebSockets subjacente, consulte a [referência da API WebSockets](https://ai.google.dev/api/live?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-13 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-13 UTC."],[],[]]
