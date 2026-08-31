---
source_url: https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=pt-BR
fetched_at: 2026-08-31T06:35:51.613043+00:00
title: "Guia de recursos da API Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Guia de recursos da API Live

Este é um guia abrangente que aborda os recursos e as configurações
disponíveis com a API Live.
Consulte a página [Começar a usar a API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br) para ter uma visão geral e exemplos de código para casos de uso comuns.

## Antes de começar

- **Conheça os conceitos básicos**:se ainda não fez isso, leia primeiro a página [Começar a usar a API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br) .
  Assim, você vai conhecer os princípios fundamentais da API Live, como ela funciona e as diferentes [abordagens de implementação](https://ai.google.dev/gemini-api/docs/live?hl=pt-br#implementation-approach).
- **Teste a API Live no AI Studio**:talvez seja útil testar a
  API Live no [Google AI Studio](https://aistudio.google.com/app/live?hl=pt-br) antes de começar a criar. Para usar a
  API Live no Google AI Studio, selecione **Transmissão**.

## Comparação de modelos

A tabela a seguir resume as principais diferenças entre os modelos [Prévia dinâmica do Gemini 3.1 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=pt-br) e [Prévia dinâmica do Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025?hl=pt-br):

| Recurso | Pré-lançamento do Gemini 3.1 Flash Live | Pré-lançamento do Gemini 2.5 Flash Live |
| --- | --- | --- |
| **[Raciocínio](#native-audio-output-thinking)** | Usa `thinkingLevel` para controlar a profundidade do pensamento com configurações como `minimal`, `low`, `medium` e `high`. O padrão é `minimal` para otimizar a menor latência. Consulte [Níveis de pensamento e orçamentos](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br#levels-budgets). | Usa `thinkingBudget` para definir o número de tokens de raciocínio. O pensamento dinâmico é ativado por padrão. Defina `thinkingBudget` como `0` para desativar. Consulte [Níveis de pensamento e orçamentos](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br#levels-budgets). |
| **[Recebendo resposta](https://ai.google.dev/api/live?hl=pt-br#bidigeneratecontentservercontent)** | Um único evento do servidor pode conter várias partes de conteúdo simultaneamente (por exemplo, `inlineData` e transcrição). Verifique se o código processa todas as partes em cada evento para evitar a perda de conteúdo. | Cada evento do servidor contém apenas uma parte do conteúdo. As partes são entregues em eventos separados. |
| **[Conteúdo do cliente](#incremental-updates)** | O `send_client_content` só é compatível com o seeding do histórico de contexto inicial (requer a definição de `initial_history_in_client_content` na configuração da sessão). Para enviar atualizações de texto durante a conversa, use `send_realtime_input`. | O `send_client_content` é compatível com toda a conversa para enviar atualizações incrementais de conteúdo e estabelecer contexto. |
| **[Cobertura de turno](https://ai.google.dev/api/live?hl=pt-br#turncoverage)** | O valor padrão é `TURN_INCLUDES_AUDIO_ACTIVITY_AND_ALL_VIDEO`. O turno do modelo inclui a atividade de áudio detectada e todos os frames de vídeo. | O valor padrão é `TURN_INCLUDES_ONLY_ACTIVITY`. A vez do modelo inclui apenas a atividade detectada. |
| **[VAD personalizado](#disable-automatic-vad)** (`activity_start`/`activity_end`) | Compatível. Desative a VAD automática e envie mensagens `activityStart` e `activityEnd` manualmente para controlar os limites de turno. | Compatível. Desative a VAD automática e envie mensagens `activityStart` e `activityEnd` manualmente para controlar os limites de turno. |
| **[Configuração automática de VAD](#configure-automatic-vad)** | Compatível. Configure parâmetros como `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms` e `silence_duration_ms`. | Compatível. Configure parâmetros como `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms` e `silence_duration_ms`. |
| **[Chamada de função assíncrona](https://ai.google.dev/gemini-api/docs/live-tools?hl=pt-br#async-function-calling)** (`behavior: NON_BLOCKING`) | Indisponível. A chamada de função é apenas sequencial. O modelo só vai começar a responder depois que você enviar a resposta da ferramenta. | Compatível. Defina `behavior` como `NON_BLOCKING` em uma declaração de função para permitir que o modelo continue interagindo enquanto a função é executada. Controle como o modelo lida com as respostas usando o parâmetro `scheduling` (`INTERRUPT`, `WHEN_IDLE` ou `SILENT`). |
| **[Áudio proativo](#proactive-audio)** | incompatível | Compatível. Quando ativado, o modelo pode decidir não responder se o conteúdo da entrada não for relevante. Defina `proactive_audio` como `true` na configuração `proactivity` (requer `v1beta`). |
| **[Computação afetiva](#affective-dialog)** | incompatível | Compatível. O modelo adapta o estilo da resposta para corresponder à expressão e ao tom da entrada. Defina `enable_affective_dialog` como `true` na configuração da sessão (requer `v1beta`). |

Para migrar do Gemini 2.5 Flash Live para o Gemini 3.1 Flash Live, consulte o [guia de migração](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=pt-br#migrating).

## Como estabelecer uma conexão

O exemplo a seguir mostra como criar uma conexão com uma chave de API:

### Python

```
import asyncio
from google import genai

client = genai.Client()

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

const ai = new GoogleGenAI({});
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

## Modalidades de interação

As seções a seguir fornecem exemplos e contexto de suporte para as diferentes modalidades de entrada e saída disponíveis na API Live.

### Enviando áudio

O áudio precisa ser enviado como dados PCM brutos (áudio PCM bruto de 16 bits, 16 kHz, little-endian).

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

### Formatos de áudio

Os dados de áudio na API Live são sempre brutos, little-endian,
PCM de 16 bits. A saída de áudio sempre usa uma taxa de amostragem de 24 kHz. O áudio de entrada é nativamente de 16 kHz, mas a API Live faz uma nova amostragem, se necessário. Portanto, qualquer taxa de amostragem pode ser enviada. Para transmitir a taxa de amostragem do áudio de entrada, defina o tipo MIME de cada [Blob](https://ai.google.dev/api/caching?hl=pt-br#Blob) que contém áudio como um valor como `audio/pcm;rate=16000`.

### Recebendo áudio

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

### Enviando texto

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

### Enviando vídeo

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

#### Atualizações incrementais de conteúdo

Use atualizações incrementais para enviar entrada de texto, estabelecer ou restaurar o contexto da sessão. Para contextos curtos, você pode enviar interações de navegação guiada para representar a sequência exata de eventos:

### Python

```
turns = [
    {"role": "user", "parts": [{"text": "What is the capital of France?"}]},
    {"role": "model", "parts": [{"text": "Paris"}]},
]

await session.send_client_content(turns=turns, turn_complete=False)

turns = [{"role": "user", "parts": [{"text": "What is the capital of Germany?"}]}]

await session.send_client_content(turns=turns, turn_complete=True)
```

### JavaScript

```
let inputTurns = [
  { "role": "user", "parts": [{ "text": "What is the capital of France?" }] },
  { "role": "model", "parts": [{ "text": "Paris" }] },
]

session.sendClientContent({ turns: inputTurns, turnComplete: false })

inputTurns = [{ "role": "user", "parts": [{ "text": "What is the capital of Germany?" }] }]

session.sendClientContent({ turns: inputTurns, turnComplete: true })
```

Para contextos mais longos, é recomendável fornecer um único resumo da mensagem para liberar a janela de contexto para interações subsequentes. Consulte [Retomada de sessão](https://ai.google.dev/gemini-api/docs/live-session?hl=pt-br#session-resumption) para outro método de
carregar o contexto da sessão.

### Transcrições de áudio

Além da resposta do modelo, você também pode receber transcrições da saída e da entrada de áudio.

Para ativar a transcrição da saída de áudio do modelo, envie
`output_audio_transcription` na configuração de configuração. O idioma da transcrição é inferido da resposta do modelo.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "output_audio_transcription": {}
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        message = "Hello? Gemini are you there?"

        await session.send_client_content(
            turns={"role": "user", "parts": [{"text": message}]}, turn_complete=True
        )

        async for response in session.receive():
            if response.server_content.model_turn:
                print("Model turn:", response.server_content.model_turn)
            if response.server_content.output_transcription:
                print("Transcript:", response.server_content.output_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  outputAudioTranscription: {}
};

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
    config: config,
  });

  const inputTurns = 'Hello how are you?';
  session.sendClientContent({ turns: inputTurns });

  const turns = await handleTurn();

  for (const turn of turns) {
    if (turn.serverContent && turn.serverContent.outputTranscription) {
      console.debug('Received output transcription: %s\n', turn.serverContent.outputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

Para ativar a transcrição da entrada de áudio do modelo, envie
`input_audio_transcription` na configuração de configuração.

### Python

```
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "input_audio_transcription": {},
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_data = Path("16000.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_data, mime_type='audio/pcm;rate=16000')
        )

        async for msg in session.receive():
            if msg.server_content.input_transcription:
                print('Transcript:', msg.server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  inputAudioTranscription: {}
};

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
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("16000.wav");

  // Ensure audio conforms to API requirements (16-bit PCM, 16kHz, mono)
  const wav = new WaveFile();
  wav.fromBuffer(fileBuffer);
  wav.toSampleRate(16000);
  wav.toBitDepth("16");
  const base64Audio = wav.toBase64();

  // If already in correct format, you can use this:
  // const fileBuffer = fs.readFileSync("sample.pcm");
  // const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }
  );

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
    else if (turn.serverContent && turn.serverContent.inputTranscription) {
      console.debug('Received input transcription: %s\n', turn.serverContent.inputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

### Mudar a voz e o idioma

Os modelos de [saída de áudio nativa](#native-audio-output) são compatíveis com qualquer uma das vozes disponíveis para nossos modelos de [conversão de texto em voz (TTS)](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pt-br#voices). Você pode ouvir todas as vozes no [AI Studio](https://aistudio.google.com/app/live?hl=pt-br).

Para especificar uma voz, defina o nome dela no objeto `speechConfig` como parte
da configuração da sessão:

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "speech_config": {
        "voice_config": {"prebuilt_voice_config": {"voice_name": "Kore"}}
    },
}
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: "Kore" } } }
};
```

A API Live é compatível com [vários idiomas](#supported-languages).
Os modelos de [saída de áudio nativa](#native-audio-output) escolhem automaticamente o idioma apropriado e não permitem definir explicitamente o código de idioma.

## Recursos de áudio nativos

Nossos modelos mais recentes têm [saída de áudio nativa](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=pt-br), que oferece uma fala natural e realista, além de melhorar o desempenho em vários idiomas.

### Pensando

Os modelos do Gemini 3.1 usam `thinkingLevel` para controlar a profundidade do pensamento, com configurações como `minimal`, `low`, `medium` e `high`. O padrão é `minimal` para otimizar a menor latência. Os modelos do Gemini 2.5 usam `thinkingBudget` para definir o número de tokens de raciocínio. Para mais detalhes
sobre níveis e orçamentos, consulte
[Níveis e orçamentos de pensamento](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br#levels-budgets).

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
    )
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Send audio input and receive audio
```

### JavaScript

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
  },
};

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: ...,
  });

  // Send audio input and receive audio

  session.close();
}

main();
```

Além disso, é possível ativar os resumos de ideias definindo `includeThoughts` como
`true` na sua configuração. Consulte [resumos de ideias](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br#summaries) para mais informações:

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
        include_thoughts=True
    )
)
```

### JavaScript

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
    includeThoughts: true,
  },
};
```

### Computação afetiva

Com esse recurso, o Gemini adapta o estilo da resposta à expressão e ao tom da solicitação.

Para usar a computação afetiva, defina a versão da API como `v1beta` e `enable_affective_dialog` como `true` na mensagem de configuração:

### Python

```
client = genai.Client(http_options={"api_version": "v1beta"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    enable_affective_dialog=True
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1beta"} });

const config = {
  responseModalities: [Modality.AUDIO],
  enableAffectiveDialog: true
};
```

### Áudio proativo

Quando esse recurso está ativado, o Gemini pode decidir não responder se o conteúdo não for relevante.

Para usar, defina a versão da API como `v1beta`, configure o campo `proactivity` na mensagem de configuração e defina `proactive_audio` como `true`:

### Python

```
client = genai.Client(http_options={"api_version": "v1beta"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    proactivity={'proactive_audio': True}
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1beta"} });

const config = {
  responseModalities: [Modality.AUDIO],
  proactivity: { proactiveAudio: true }
}
```

## Tradução em tempo real

A API Live oferece suporte à tradução em tempo real e com baixa latência de conversas faladas. Com esse recurso, é possível criar aplicativos de tradução de voz para voz em tempo real.

Para mais informações e exemplos, consulte o [guia de tradução simultânea](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=pt-br).

## Detecção de atividade de voz (VAD)

A detecção de atividade de voz (VAD, na sigla em inglês) permite que o modelo reconheça quando uma pessoa está falando. Isso é essencial para criar conversas naturais, já que permite que um usuário interrompa o modelo a qualquer momento.

Quando a VAD detecta uma interrupção, a geração em andamento é cancelada e descartada. Apenas as informações já enviadas ao cliente são mantidas no histórico da sessão. Em seguida, o servidor envia uma mensagem [`BidiGenerateContentServerContent`](https://ai.google.dev/api/live?hl=pt-br#bidigeneratecontentservercontent) para informar sobre a interrupção.

Em seguida, o servidor do Gemini descarta todas as chamadas de função pendentes e envia uma mensagem `BidiGenerateContentServerContent` com os IDs das chamadas canceladas.

### Python

```
async for response in session.receive():
    if response.server_content.interrupted is True:
        # The generation was interrupted

        # If realtime playback is implemented in your application,
        # you should stop playing audio and clear queued playback here.
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.interrupted) {
    // The generation was interrupted

    // If realtime playback is implemented in your application,
    // you should stop playing audio and clear queued playback here.
  }
}
```

### VAD automática

Por padrão, o modelo realiza automaticamente a VAD em um fluxo contínuo de entrada de áudio. A VAD pode ser configurada com o campo
[`realtimeInputConfig.automaticActivityDetection`](https://ai.google.dev/api/live?hl=pt-br#RealtimeInputConfig.AutomaticActivityDetection)
da [configuração de configuração](https://ai.google.dev/api/live?hl=pt-br#BidiGenerateContentSetup).

Quando o fluxo de áudio é pausado por mais de um segundo (por exemplo, porque o usuário desligou o microfone), um evento [`audioStreamEnd`](https://ai.google.dev/api/live?hl=pt-br#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end) precisa ser enviado para limpar o áudio em cache. O cliente pode retomar o envio de dados de áudio a qualquer momento.

### Python

```
# example audio file to try:
# URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
# !wget -q $URL -O sample.pcm
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_bytes = Path("sample.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
        )

        # if stream gets paused, send:
        # await session.send_realtime_input(audio_stream_end=True)

        async for response in session.receive():
            if response.text is not None:
                print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
// example audio file to try:
// URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
// !wget -q $URL -O sample.pcm
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

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
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("sample.pcm");
  const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }

  );

  // if stream gets paused, send:
  // session.sendRealtimeInput({ audioStreamEnd: true })

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

Com o `send_realtime_input`, a API responde ao áudio automaticamente com base na VAD. Enquanto `send_client_content` adiciona mensagens ao contexto do modelo em ordem, `send_realtime_input` é otimizado para capacidade de resposta às custas da ordenação determinística.

### Configuração automática de VAD

Para ter mais controle sobre a atividade de VAD, configure os seguintes
parâmetros. Consulte a [referência da API](https://ai.google.dev/api/live?hl=pt-br#automaticactivitydetection) para mais informações.

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {
        "automatic_activity_detection": {
            "disabled": False, # default
            "start_of_speech_sensitivity": types.StartSensitivity.START_SENSITIVITY_LOW,
            "end_of_speech_sensitivity": types.EndSensitivity.END_SENSITIVITY_LOW,
            "prefix_padding_ms": 20,
            "silence_duration_ms": 100,
        }
    }
}
```

### JavaScript

```
import { GoogleGenAI, Modality, StartSensitivity, EndSensitivity } from '@google/genai';

const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: false, // default
      startOfSpeechSensitivity: StartSensitivity.START_SENSITIVITY_LOW,
      endOfSpeechSensitivity: EndSensitivity.END_SENSITIVITY_LOW,
      prefixPaddingMs: 20,
      silenceDurationMs: 100,
    }
  }
};
```

### Desativar a detecção automática de atividade de voz

Como alternativa, a VAD automática pode ser desativada definindo
`realtimeInputConfig.automaticActivityDetection.disabled` como `true` na mensagem
de configuração. Nessa configuração, o cliente é responsável por detectar a fala do usuário e enviar mensagens
[`activityStart`](https://ai.google.dev/api/live?hl=pt-br#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityStart.BidiGenerateContentRealtimeInput.activity_start)
e [`activityEnd`](https://ai.google.dev/api/live?hl=pt-br#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityEnd.BidiGenerateContentRealtimeInput.activity_end)
nos momentos adequados. Um `audioStreamEnd` não é enviado nessa configuração. Em vez disso, qualquer interrupção do stream é marcada por
uma mensagem `activityEnd`.

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {"automatic_activity_detection": {"disabled": True}},
}

async with client.aio.live.connect(model=model, config=config) as session:
    # ...
    await session.send_realtime_input(activity_start=types.ActivityStart())
    await session.send_realtime_input(
        audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
    )
    await session.send_realtime_input(activity_end=types.ActivityEnd())
    # ...
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    }
  }
};

session.sendRealtimeInput({ activityStart: {} })

session.sendRealtimeInput(
  {
    audio: {
      data: base64Audio,
      mimeType: "audio/pcm;rate=16000"
    }
  }

);

session.sendRealtimeInput({ activityEnd: {} })
```

### Entender os parâmetros de VAD e o impacto deles na qualidade

Ao usar a VAD automática, dois parâmetros principais controlam como o áudio é segmentado em turnos de fala antes de ser enviado ao modelo:

- **`prefixPaddingMs`**: a quantidade de áudio a ser incluída *antes* da detecção
  da fala. Esse "retrospecto" garante que o modelo capture o início completo da fala, incluindo a primeira sílaba, que pode começar antes que o VAD seja acionado. Um valor de `0` pode fazer com que o início das palavras seja cortado.
- **`silenceDurationMs`**: por quanto tempo o servidor aguarda o silêncio
  antes de encerrar um turno de fala. Isso determina a tolerância do sistema a pausas naturais no meio da frase (por exemplo, para pensar, respirar ou limites de cláusulas).

#### Impacto de `silenceDurationMs` na qualidade do áudio

O valor de `silenceDurationMs` afeta diretamente o tamanho e a integridade dos trechos de áudio que o modelo recebe para processamento:

- **Recomendado (500 ms a 800 ms)**: oferece um bom equilíbrio. O modelo recebe partes de áudio completas e contextualmente ricas, mantendo a latência razoável. O padrão interno do servidor é de aproximadamente 800 ms.
- **Muito baixo (por exemplo, 100 ms a 200 ms)**: o sistema encerra os turnos de fala durante pausas naturais, dividindo uma única expressão em vários pequenos fragmentos de áudio. O modelo recebe esses fragmentos individualmente, perdendo o contexto entre eles e resultando em uma qualidade inferior de transcrição e resposta.
- **Muito alto (por exemplo, mais de 2.000 ms)**: o sistema espera muito tempo depois que o usuário para de falar, aumentando a latência percebida antes que o modelo responda.

#### Práticas recomendadas para VAD manual (do lado do cliente)

Quando você desativa a VAD automática e gerencia os sinais `activityStart`/`activityEnd` da sua própria detecção de voz do lado do cliente, os mecanismos de buffer de áudio integrados do servidor são ignorados. Isso significa que:

1. **Sem buffer de pré-fala**:o servidor não adiciona mais áudio antes do início da fala detectada. O cliente precisa incluir contexto de áudio suficiente antes de enviar `activityStart`.
2. **Sem tolerância a silêncio**:o servidor age imediatamente no seu indicador
   `activityEnd` sem espera adicional. Se a VAD do lado do cliente usar um limite agressivo de fim de fala (por exemplo, 200 ms de silêncio), a fala poderá ser cortada no meio da frase durante pausas naturais.

Para preservar a qualidade do áudio com VAD manual, use um limite de silêncio de fim de fala de pelo menos **500 ms** no detector de atividade de voz do cliente.
Limiares abaixo desse valor geralmente causam áudio fragmentado que prejudica a qualidade da transcrição e da resposta do modelo.

## Contagem de tokens

Você pode encontrar o número total de tokens consumidos no campo [usageMetadata](https://ai.google.dev/api/live?hl=pt-br#usagemetadata) da mensagem retornada do servidor.

### Python

```
async for message in session.receive():
    # The server will periodically send messages that include UsageMetadata.
    if message.usage_metadata:
        usage = message.usage_metadata
        print(
            f"Used {usage.total_token_count} tokens in total. Response token breakdown:"
        )
        for detail in usage.response_tokens_details:
            match detail:
                case types.ModalityTokenCount(modality=modality, token_count=count):
                    print(f"{modality}: {count}")
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.usageMetadata) {
    console.debug('Used %s tokens in total. Response token breakdown:\n', turn.usageMetadata.totalTokenCount);

    for (const detail of turn.usageMetadata.responseTokensDetails) {
      console.debug('%s\n', detail);
    }
  }
}
```

## Resolução de mídia

Você pode especificar a resolução da mídia de entrada definindo o campo
`mediaResolution` como parte da configuração da sessão:

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "media_resolution": types.MediaResolution.MEDIA_RESOLUTION_LOW,
}
```

### JavaScript

```
import { GoogleGenAI, Modality, MediaResolution } from '@google/genai';

const config = {
    responseModalities: [Modality.AUDIO],
    mediaResolution: MediaResolution.MEDIA_RESOLUTION_LOW,
};
```

## Limitações

Considere as seguintes limitações da API Live
ao planejar seu projeto.

### Modalidades de resposta

Os modelos de áudio nativos só são compatíveis com a modalidade de resposta `AUDIO`. Se você precisar da resposta do modelo como texto, use o recurso [transcrição de áudio de saída](#audio-transcription).

### Autenticação do cliente

Por padrão, a API Live só oferece autenticação de servidor para servidor. Se você estiver implementando seu aplicativo da API Live
usando uma [abordagem de cliente para servidor](https://ai.google.dev/gemini-api/docs/live?hl=pt-br#implementation-approach), use
[tokens efêmeros](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=pt-br) para reduzir os riscos
de segurança.

### Duração da sessão

As sessões somente de áudio têm duração máxima de 15 minutos, e as sessões de áudio e vídeo têm duração máxima de 2 minutos.
No entanto, é possível configurar diferentes [técnicas de gerenciamento de sessão](https://ai.google.dev/gemini-api/docs/live-session?hl=pt-br) para extensões ilimitadas na duração da sessão.

### Janela de contexto

Uma sessão tem um limite de janela de contexto de:

- 128 mil tokens para modelos de [saída de áudio nativa](#native-audio-output)
- 32 mil tokens para outros modelos de API Live

## Idiomas compatíveis

A API Live é compatível com os seguintes 97 idiomas.

| Idioma | Código BCP-47 | Idioma | Código BCP-47 |
| --- | --- | --- | --- |
| Africâner | `af` | Letão | `lv` |
| Akan | `ak` | Lituano | `lt` |
| Albanês | `sq` | Macedônio | `mk` |
| Amárico | `am` | Malaio | `ms` |
| Árabe | `ar` | Malaiala | `ml` |
| Armênio | `hy` | Maltês | `mt` |
| Assamês | `as` | Maori | `mi` |
| Azerbaijano | `az` | Marati | `mr` |
| Basco | `eu` | Mongol | `mn` |
| Bielorrusso | `be` | Nepalês | `ne` |
| Bengali | `bn` | Norueguês | `no` |
| Bósnio | `bs` | Oriá | `or` |
| Búlgaro | `bg` | Oromo | `om` |
| Birmanês | `my` | Pashto | `ps` |
| Catalão | `ca` | Persa | `fa` |
| Cebuano | `ceb` | Polonês | `pl` |
| Chinês | `zh` | Português | `pt` |
| Croata | `hr` | Punjabi | `pa` |
| Tcheco | `cs` | Quíchua | `qu` |
| Dinamarquês | `da` | Romeno | `ro` |
| Holandês | `nl` | Romanche | `rm` |
| Inglês | `en` | Russo | `ru` |
| Estoniano | `et` | Sérvio | `sr` |
| Faroês | `fo` | Sindi | `sd` |
| Filipino | `fil` | Cingalês | `si` |
| Finlandês | `fi` | Eslovaco | `sk` |
| Francês | `fr` | Esloveno | `sl` |
| Galego | `gl` | Somali | `so` |
| Georgiano | `ka` | Soto do sul | `st` |
| Alemão | `de` | Espanhol | `es` |
| Grego | `el` | Suaíli | `sw` |
| Gujarati | `gu` | Sueco | `sv` |
| Hauçá | `ha` | Tadjique | `tg` |
| Hebraico | `iw` | Tâmil | `ta` |
| Hindi | `hi` | Télugo | `te` |
| Húngaro | `hu` | Tailandês | `th` |
| Islandês | `is` | Tswana | `tn` |
| Indonésio | `id` | Turco | `tr` |
| Irlandês | `ga` | Turcomano | `tk` |
| Italiano | `it` | Ucraniano | `uk` |
| Japonês | `ja` | Urdu | `ur` |
| Canarês | `kn` | Usbeque | `uz` |
| Cazaque | `kk` | Vietnamita | `vi` |
| Khmer | `km` | Galês | `cy` |
| Quiniaruanda | `rw` | Frísio ocidental | `fy` |
| Coreano | `ko` | Wolof | `wo` |
| Curdo | `ku` | Iorubá | `yo` |
| Quirguiz | `ky` | Zulu | `zu` |
| Laosiano | `lo` |  |  |

## A seguir

- Leia os guias [Uso de ferramentas](https://ai.google.dev/gemini-api/docs/live-tools?hl=pt-br) e [Gerenciamento de sessões](https://ai.google.dev/gemini-api/docs/live-session?hl=pt-br) para informações essenciais sobre como usar a API Live de maneira eficaz.
- Teste a API Live no [Google AI Studio](https://aistudio.google.com/app/live?hl=pt-br).
- Para mais informações sobre os modelos da API Live, consulte [Áudio nativo do Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=pt-br#gemini-2.5-flash-native-audio) na página "Modelos".
- Confira mais exemplos no [manual da API Live](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=pt-br), no [manual de ferramentas da API Live](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=pt-br) e no [script de primeiros passos da API Live](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.py).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-31 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-31 UTC."],[],[]]
