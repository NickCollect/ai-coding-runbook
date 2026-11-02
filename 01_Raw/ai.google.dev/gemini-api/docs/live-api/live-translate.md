---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=pt-BR
fetched_at: 2026-11-02T07:22:30.560408+00:00
title: "Tradu\u00e7\u00e3o instant\u00e2nea com a API Gemini Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Tradução instantânea com a API Gemini Live

A API Gemini Live oferece suporte à tradução de fala para fala em tempo real e de baixa latência entre mais de 70 idiomas usando o modelo [`gemini-3.5-live-translate-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-live-translate-preview?hl=pt-br). Ao configurar a API Live com as configurações de tradução, você pode transmitir áudio em um idioma e receber a saída de áudio traduzida em outro, permitindo uma tradução de voz para voz em tempo real.

[Testar a Tradução instantânea no Google AI Studiomic](https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview&hl=pt-br)
[Clonar o app de exemplo do GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[Usar habilidades de agente de programaçãoterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=pt-br#gemini-live-api-dev)

## Atendente x Tradução Instantânea

Embora os dois usem a API Live, o modelo mental da tradução simultânea é diferente das interações de agentes em tempo real.

| Agente em tempo real | Tradução instantânea |
| --- | --- |
| **O modelo age como um assistente.** Ele ouve, raciocina e realiza ações em seu nome. | **O modelo atua como um intérprete.** Ele funciona como um pipeline de tradução em tempo real. |
| **Usa interações baseadas em turnos.** Depende de pausas, detecção de intenção e lida com interrupções. | **Usa o processamento de stream contínuo.** Traduz enquanto o falante fala, sem esperar a vez. |
| **Compatível com ferramentas e agentes.** Suporte nativo para chamada de função, Pesquisa Google e instruções. | **Oferece suporte apenas à tradução.** Tradução pura de baixa latência, sem suporte para ferramentas ou instruções. |
| **Totalmente multimodal**. Aceita entradas de texto, áudio, vídeo e imagem. | **Áudio restrito.** A entrada é limitada ao áudio para garantir limites de latência em tempo real. |
| **Configuração granular**. Usa geração, fala, ferramentas e instruções do sistema. | **Configuração simplificada**. Defina `target_language_code` e alternâncias como `echo_target_language`. |

## Primeiros passos

Os exemplos a seguir demonstram como inicializar um cliente e se conectar à API Live com uma configuração de tradução.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.5-live-translate-preview"
config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
    output_audio_transcription=types.AudioTranscriptionConfig(),
    translation_config=types.TranslationConfig(
        target_language_code="pl",
        echo_target_language=True
    )
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started with translation")
        # Start receiving the translated audio stream
        async for response in session.receive():
            if response.server_content:
                if response.server_content.input_transcription:
                    print(f"Input transcript: {response.server_content.input_transcription.text}")
                if response.server_content.output_transcription:
                    print(f"Output transcript: {response.server_content.output_transcription.text}")
                if response.server_content.model_turn:
                    for part in response.server_content.model_turn.parts:
                        if part.inline_data:
                            audio_data = part.inline_data.data
                            # Play or process the translated audio chunk
                            print(f"Received audio chunk ({len(audio_data)} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-live-translate-preview';
const config = {
    responseModalities: [Modality.AUDIO],
    inputAudioTranscription: {},
    outputAudioTranscription: {},
    translationConfig: {
        targetLanguageCode: 'pl',
        echoTargetLanguage: true
    }
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.debug('Opened'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Input transcript:', content.inputTranscription.text);
        }
        if (content?.outputTranscription) {
          console.log('Output transcript:', content.outputTranscription.text);
        }
        if (content?.modelTurn?.parts) {
          for (const part of content.modelTurn.parts) {
            if (part.inlineData) {
              const audioData = part.inlineData.data;
              // Play or process the translated audio chunk (base64 encoded)
              console.debug(`Received audio chunk (${audioData.length} bytes)`);
            }
          }
        }
      },
      onerror: (e) => console.debug('Error:', e.message),
      onclose: (e) => console.debug('Close:', e.reason),
    },
  });

  console.debug("Session started with translation");
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-live-translate-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['AUDIO'],
        inputAudioTranscription: {},
        outputAudioTranscription: {},
        translationConfig: {
          targetLanguageCode: 'pl',
          echoTargetLanguage: true
        }
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  if (response.serverContent) {
    const content = response.serverContent;
    if (content.inputTranscription) {
      console.log('Input transcript:', content.inputTranscription.text, `(${content.inputTranscription.languageCode})`);
    }
    if (content.outputTranscription) {
      console.log('Output transcript:', content.outputTranscription.text, `(${content.outputTranscription.languageCode})`);
    }
    if (content.modelTurn?.parts) {
      for (const part of content.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data;
          // Play or process the translated audio chunk (base64 encoded)
          console.debug(`Received audio chunk (${audioData.length} bytes)`);
        }
      }
    }
  }
};
```

## Enviando áudio

Para transmitir entradas de voz para tradução, envie áudio PCM bruto, little-endian e de 16 bits.

- **Formato de áudio de entrada**: PCM bruto de 16 bits a 16 kHz (mono, little-endian).
- **Formato de áudio de saída**: PCM bruto de 16 bits a 24 kHz (mono, little endian).
- **Tamanho do bloco e latência**: envie áudio em blocos de 100 ms.

Os exemplos a seguir mostram como enviar partes de áudio para a sessão.

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

### WebSockets

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
  }
}
```

## Configuração

Para ativar a tradução, especifique o `translationConfig` no `generationConfig` durante a configuração da sessão.

### Configurar mensagens

O `generationConfig` é compatível com os seguintes campos para ativar as transcrições:

- **`inputAudioTranscription`**: um objeto que, quando presente, permite que o modelo envie transcrições de texto do áudio de entrada.
- **`outputAudioTranscription`**: um objeto que, quando presente, permite que o modelo envie transcrições de texto do áudio de saída (traduzido).

O `translationConfig` é compatível com os seguintes campos:

- **`targetLanguageCode`**: o [código de idioma BCP-47](#supported-languages) do idioma para o qual você quer que o modelo traduza (por exemplo, `"pl"` para polonês e `"es"` para espanhol). O valor padrão é `"en"`.
- **`echoTargetLanguage`**: um booleano que indica como o áudio de entrada que já está no idioma de destino deve ser processado. Se definido como `true`, o modelo vai repetir o áudio de entrada que já está no idioma de destino. Se definido como `false`, o modelo vai ficar em silêncio quando a fala de entrada já estiver no idioma de destino. O padrão é `false`.

Confira um exemplo da estrutura da mensagem de configuração:

```
"setup": {
    "model": "models/gemini-3.5-live-translate-preview",
    "generationConfig": {
      "responseModalities": [
        "AUDIO"
      ],
      "inputAudioTranscription": {},
      "outputAudioTranscription": {},
      "translationConfig": {
        "targetLanguageCode": "pl",
        "echoTargetLanguage": true
      }
    }
}
```

## Usar tokens temporários em aplicativos do lado do cliente

Para aplicativos cliente-servidor, use [tokens efêmeros](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=pt-br) (atualmente em `v1beta`) para evitar expor sua chave de API.

Ao usar tokens temporários com a Tradução Instantânea:

1. É preciso usar o endpoint `v1beta`.
2. **Configuração de bloqueio**:por padrão, especifique o `translationConfig` nas restrições de criação de token no seu servidor. Isso garante que a configuração de tradução esteja bloqueada e não possa ser adulterada pelo cliente.
3. **Configuração de desbloqueio**:se você quiser definir o `translationConfig` no lado do cliente (por exemplo, para permitir que um usuário escolha o idioma de destino), omita-o da solicitação de criação de token e defina `"lock_additional_fields": []`. Isso vai desbloquear `translationConfig` para ser definido no lado do cliente.

### Criar um token temporário restrito

Os exemplos a seguir mostram como criar um token efêmero com restrições de tradução.

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client()

token = client.auth_tokens.create(
    config = {
        'uses': 1,
        'expire_time': now + datetime.timedelta(minutes=30),
        'live_connect_constraints': {
            'model': 'gemini-3.5-live-translate-preview',
            'config': {
                'translation_config': {
                    'target_language_code': 'pl',
                    'echo_target_language': True
                }
            }
        },
    }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1,
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.5-live-translate-preview',
            config: {
                responseModalities: ['AUDIO'],
                inputAudioTranscription: {},
                outputAudioTranscription: {},
                translationConfig: {
                    targetLanguageCode: 'pl',
                    echoTargetLanguage: true
                }
            }
        },
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "liveConnectConstraints": {
      "model": "models/gemini-3.5-live-translate-preview",
      "config": {
        "responseModalities": ["AUDIO"],
        "inputAudioTranscription": {},
        "outputAudioTranscription": {},
        "translationConfig": {
          "targetLanguageCode": "pl",
          "echoTargetLanguage": true
        }
      }
    }
  }'
```

## Limitações

- **Modalidades de entrada**: somente a entrada de áudio é compatível com a tradução. Não é possível inserir texto.
- **Replicação de voz**: a replicação de voz pode ser inconsistente. As vozes podem mudar após longas pausas, atribuir o gênero errado com base em como a fala começa ou ficar presas em uma voz durante conversas rápidas com vários falantes.
- **Detecção de idioma**: a detecção de idioma tem dificuldades com sotaques fortes, idiomas semelhantes (por exemplo, espanhol e português) ou mudanças rápidas de idioma. **Observação**:isso só afeta a transcrição de entrada. Os códigos de idioma e a tradução final ainda precisam ser precisos.
- **Áudio em segundo plano**: o modelo foi projetado para filtrar ruídos e músicas e produzir uma fala limpa, mas nem todo o áudio em segundo plano pode ser ignorado.
- **Repetir o idioma de destino**: quando `echoTargetLanguage: true`, o ruído de fundo ou a música podem introduzir artefatos no áudio traduzido quando o áudio de entrada já está no idioma de destino.

## Idiomas compatíveis

Os seguintes idiomas são compatíveis com a Tradução instantânea.

| Idioma | Código BCP-47 | Idioma | Código BCP-47 |
| --- | --- | --- | --- |
| Africâner | af | Cazaque | kk |
| Akan | ak | Khmer | km |
| Albanês | sq | Quiniaruanda | rw |
| Amárico | am | Coreano | ko |
| Árabe | ar | Laosiano | lo |
| Armênio | hy | Letão | lv |
| Azerbaijano | az | Lituano | lt |
| Basco | eu | Macedônio | mk |
| Bielorrusso | be | Malaio | ms |
| Bengali | bn | Malaiala | ml |
| Búlgaro | bg | Marati | mr |
| Birmanês (Mianmar) | my | Mongol | mn |
| Catalão | ca | Nepalês | ne |
| Chinês (simplificado) | zh-Hans | Norueguês | não, nb |
| Chinês (tradicional) | zh-Hant | Persa | fa |
| Croata | h | Polonês | pl |
| Tcheco | cs | Português (Brasil) | pt-BR |
| Dinamarquês | da | Português (Portugal) | pt-PT |
| Neerlandês | nl | Punjabi | pa |
| Inglês | en | Romeno | ro |
| Estoniano | et | Russo | ru |
| Filipino | fil | Sérvio | sr |
| Finlandês | fi | Sindi | sd |
| Francês | fr | Cingalês | si |
| Galego | gl | Eslovaco | sk |
| Georgiano | ka | Esloveno | sl |
| Alemão | de | Espanhol | es |
| Grego | el | Sundanês | su |
| Gujarati | gu | Suaíli | sw |
| Hauçá | ha | Sueco | sv |
| Hebraico | ele | Tâmil | ta |
| Hindi | hi | Télugo | te |
| Húngaro | hu | Tailandês | th |
| Islandês | is | Turco | tr |
| Indonésio | id | Ucraniano | uk |
| Italiano | it | Urdu | ur |
| Japonês | ja | Usbeque | uz |
| Javanês | jv | Vietnamita | vi |
| Canarês | kn | Zulu | zu |

## A seguir

- Leia o guia completo de [recursos](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=pt-br) da API Live.
- Leia o guia [Começar a usar o SDK](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=pt-br).
- Leia o guia [Começar a usar WebSockets](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=pt-br).
- Leia o guia [Tokens efêmeros](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=pt-br) para autenticação segura em aplicativos cliente-servidor.
- Clone os [exemplos de API ativa](https://github.com/google-gemini/gemini-live-api-examples) do GitHub.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-23 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-23 UTC."],[],[]]
