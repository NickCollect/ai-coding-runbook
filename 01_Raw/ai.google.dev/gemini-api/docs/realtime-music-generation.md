---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=pt-BR
fetched_at: 2026-06-08T05:39:25.410795+00:00
title: "Gera\u00e7\u00e3o de m\u00fasica em tempo real com o Lyria RealTime \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Geração de música em tempo real com o Lyria RealTime

A API Gemini, usando
[Lyria RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=pt-br),
oferece acesso a um modelo de geração de música de streaming em tempo real de última geração. Ele permite que os desenvolvedores criem aplicativos em que os usuários podem criar, direcionar continuamente e executar músicas instrumentais de forma interativa.

A geração de música do Lyria RealTime usa uma conexão de streaming bidirecional e persistente,
de baixa latência usando
[WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API).

Para saber o que pode ser criado usando o Lyria RealTime, teste-o no AI Studio
usando os apps [Prompt DJ](https://aistudio.google.com/apps/bundled/promptdj?hl=pt-br) ou
[MIDI DJ](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=pt-br).

## Gerar e controlar música

O Lyria RealTime funciona de maneira semelhante à [API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br)
usando WebSockets para manter a comunicação em tempo real com o modelo.

O código a seguir demonstra como gerar música:

### Python

Este exemplo inicializa a sessão do Lyria RealTime usando `client.aio.live.music.connect()`, envia um comando inicial com `session.set_weighted_prompts()` e uma configuração inicial usando `session.set_music_generation_config`, inicia a geração de música usando `session.play()` e configura `receive_audio()` para processar os blocos de áudio recebidos.

```
  import asyncio
  from google import genai
  from google.genai import types

  client = genai.Client(http_options={'api_version': 'v1alpha'})

  async def main():
      async def receive_audio(session):
        """Example background task to process incoming audio."""
        while True:
          async for message in session.receive():
            audio_data = message.server_content.audio_chunks[0].data
            # Process audio...
            await asyncio.sleep(10**-12)

      async with (
        client.aio.live.music.connect(model='models/lyria-realtime-exp') as session,
        asyncio.TaskGroup() as tg,
      ):
        # Set up task to receive server messages.
        tg.create_task(receive_audio(session))

        # Send initial prompts and config
        await session.set_weighted_prompts(
          prompts=[
            types.WeightedPrompt(text='minimal techno', weight=1.0),
          ]
        )
        await session.set_music_generation_config(
          config=types.LiveMusicGenerationConfig(bpm=90, temperature=1.0)
        )

        # Start streaming music
        await session.play()
  if __name__ == "__main__":
      asyncio.run(main())
```

### JavaScript

Este exemplo inicializa a sessão do Lyria RealTime usando `client.live.music.connect()`, envia um comando inicial com `session.setWeightedPrompts()` e uma configuração inicial usando `session.setMusicGenerationConfig`, inicia a geração de música usando `session.play()` e configura um callback `onMessage` para processar os blocos de áudio recebidos.

```
import { GoogleGenAI } from "@google/genai";
import Speaker from "speaker";
import { Buffer } from "buffer";

const client = new GoogleGenAI({
  apiKey: GEMINI_API_KEY,
    apiVersion: "v1alpha" ,
});

async function main() {
  const speaker = new Speaker({
    channels: 2,       // stereo
    bitDepth: 16,      // 16-bit PCM
    sampleRate: 44100, // 44.1 kHz
  });

  const session = await client.live.music.connect({
    model: "models/lyria-realtime-exp",
    callbacks: {
      onmessage: (message) => {
        if (message.serverContent?.audioChunks) {
          for (const chunk of message.serverContent.audioChunks) {
            const audioBuffer = Buffer.from(chunk.data, "base64");
            speaker.write(audioBuffer);
          }
        }
      },
      onerror: (error) => console.error("music session error:", error),
      onclose: () => console.log("Lyria RealTime stream closed."),
    },
  });

  await session.setWeightedPrompts({
    weightedPrompts: [
      { text: "Minimal techno with deep bass, sparse percussion, and atmospheric synths", weight: 1.0 },
    ],
  });

  await session.setMusicGenerationConfig({
    musicGenerationConfig: {
      bpm: 90,
      temperature: 1.0,
      audioFormat: "pcm16",  // important so we know format
      sampleRateHz: 44100,
    },
  });

  await session.play();
}

main().catch(console.error);
```

Em seguida, você pode usar `session.play()`, `session.pause()`, `session.stop()` e `session.reset_context()` para iniciar, pausar, interromper ou redefinir a sessão.

## Direcionar música em tempo real

É possível direcionar a geração de música em tempo real enviando comandos e atualizando os parâmetros de geração em tempo real.

### Comando do Lyria RealTime

Enquanto o stream estiver ativo, você poderá enviar novas mensagens `WeightedPrompt` a qualquer momento para alterar a música gerada. O modelo fará a transição sem problemas com base na nova entrada.

Os comandos precisam seguir o formato correto com um `text` (o comando real) e um `weight`. O `weight` pode assumir qualquer valor, exceto `0`. `1.0`
geralmente é um bom ponto de partida.

### Python

```
  from google.genai import types

  await session.set_weighted_prompts(
    prompts=[
      {"text": "Piano", "weight": 2.0},
      types.WeightedPrompt(text="Meditation", weight=0.5),
      types.WeightedPrompt(text="Live Performance", weight=1.0),
    ]
  )
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    weightedPrompts: [
      { text: 'Harmonica', weight: 0.3 },
      { text: 'Afrobeat', weight: 0.7 }
    ],
  });
```

Observe que as transições de modelo podem ser um pouco abruptas ao mudar drasticamente os comandos. Por isso, é recomendável implementar algum tipo de crossfade enviando valores de peso intermediários ao modelo.

### Atualizar a configuração

É possível direcionar a geração de música atualizando os parâmetros de geração de música em tempo real. Não é possível apenas atualizar um parâmetro. É necessário definir toda a configuração. Caso contrário, os outros campos serão redefinidos para os valores padrão.

Como a atualização do bpm ou da escala é uma mudança drástica para o modelo, você também precisa informar que ele deve redefinir o contexto usando `reset_context()` para considerar a nova configuração. Isso não vai interromper o stream, mas será uma transição difícil. Não é necessário fazer isso para os outros parâmetros.

### Python

```
  from google.genai import types

  await session.set_music_generation_config(
    config=types.LiveMusicGenerationConfig(
      bpm=128,
      scale=types.Scale.D_MAJOR_B_MINOR,
      music_generation_mode=types.MusicGenerationMode.QUALITY
    )
  )
  await session.reset_context();
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    musicGenerationConfig: { 
      bpm: 120,
      density: 0.75,
      musicGenerationMode: MusicGenerationMode.QUALITY
    },
  });
  await session.reset_context();
```

## Guia de comandos para o Lyria RealTime

Confira uma lista não exaustiva de comandos que podem ser usados para o Lyria RealTime:

- Instrumentos: `303 Acid Bass, 808 Hip Hop Beat, Accordion, Alto Saxophone,
  Bagpipes, Balalaika Ensemble, Banjo, Bass Clarinet, Bongos, Boomy Bass,
  Bouzouki, Buchla Synths, Cello, Charango, Clavichord, Conga Drums,
  Didgeridoo, Dirty Synths, Djembe, Drumline, Dulcimer, Fiddle, Flamenco
  Guitar, Funk Drums, Glockenspiel, Guitar, Hang Drum, Harmonica, Harp,
  Harpsichord, Hurdy-gurdy, Kalimba, Koto, Lyre, Mandolin, Maracas, Marimba,
  Mbira, Mellotron, Metallic Twang, Moog Oscillations, Ocarina, Persian Tar,
  Pipa, Precision Bass, Ragtime Piano, Rhodes Piano, Shamisen, Shredding
  Guitar, Sitar, Slide Guitar, Smooth Pianos, Spacey Synths, Steel Drum, Synth
  Pads, Tabla, TR-909 Drum Machine, Trumpet, Tuba, Vibraphone, Viola Ensemble,
  Warm Acoustic Guitar, Woodwinds, ...`
- Gênero musical: `Acid Jazz, Afrobeat, Alternative Country, Baroque, Bengal Baul,
  Bhangra, Bluegrass, Blues Rock, Bossa Nova, Breakbeat, Celtic Folk, Chillout,
  Chiptune, Classic Rock, Contemporary R&B, Cumbia, Deep House, Disco Funk,
  Drum & Bass, Dubstep, EDM, Electro Swing, Funk Metal, G-funk, Garage Rock,
  Glitch Hop, Grime, Hyperpop, Indian Classical, Indie Electronic, Indie Folk,
  Indie Pop, Irish Folk, Jam Band, Jamaican Dub, Jazz Fusion, Latin Jazz, Lo-Fi
  Hip Hop, Marching Band, Merengue, New Jack Swing, Minimal Techno, Moombahton,
  Neo-Soul, Orchestral Score, Piano Ballad, Polka, Post-Punk, 60s Psychedelic
  Rock, Psytrance, R&B, Reggae, Reggaeton, Renaissance Music, Salsa, Shoegaze,
  Ska, Surf Rock, Synthpop, Techno, Trance, Trap Beat, Trip Hop, Vaporwave,
  Witch house, ...`
- Humor/descrição: `Acoustic Instruments, Ambient, Bright Tones, Chill,
  Crunchy Distortion, Danceable, Dreamy, Echo, Emotional, Ethereal Ambience,
  Experimental, Fat Beats, Funky, Glitchy Effects, Huge Drop, Live Performance,
  Lo-fi, Ominous Drone, Psychedelic, Rich Orchestration, Saturated Tones,
  Subdued Melody, Sustained Chords, Swirling Phasers, Tight Groove,
  Unsettling, Upbeat, Virtuoso, Weird Noises, ...`

Estes são apenas alguns exemplos. O Lyria RealTime pode fazer muito mais. Faça testes com seus próprios comandos.

## Práticas recomendadas

- Os aplicativos cliente precisam implementar um buffer de áudio robusto para garantir uma reprodução suave. Isso ajuda a considerar a instabilidade da rede e pequenas variações na latência de geração.
- Comandos eficazes:
  - Utilize descrições. Use adjetivos que descrevam o humor, o gênero e a instrumentação.
  - Faça iterações e direcionamentos gradualmente. Em vez de mudar completamente o comando, tente adicionar ou modificar elementos para transformar a música de maneira mais suave.
  - Teste o peso em `WeightedPrompt` para influenciar a intensidade com que um novo comando afeta a geração em andamento.

## Detalhes técnicos

Esta seção descreve os detalhes de como usar a geração de música do Lyria RealTime.

### Especificações

- Formato da saída: áudio PCM bruto de 16 bits
- Taxa de amostragem: 48 kHz
- Canais: 2 (estéreo)

### Controles

A geração de música pode ser influenciada em tempo real enviando mensagens que contenham:

- `WeightedPrompt`: uma string de texto que descreve uma ideia musical, gênero, instrumento, humor ou característica. Vários comandos podem ser fornecidos para combinar influências. Consulte [acima](https://ai.google.dev/gemini-api/docs/:?hl=pt-br#steer-music) para mais detalhes sobre como usar o
  Lyria RealTime da melhor maneira.
- `MusicGenerationConfig`: configuração para o processo de geração de música, influenciando as características do áudio de saída. Os parâmetros incluem:
  - `guidance`: (float) intervalo: `[0.0, 6.0]`. Padrão: `4.0`.
    Controla a rigidez com que o modelo segue os comandos. Uma orientação maior melhora a adesão ao comando, mas torna as transições mais abruptas.
  - `bpm`: (int) intervalo: `[60, 200]`.
    Define as batidas por minuto que você quer para a música gerada. É necessário interromper/reproduzir ou redefinir o contexto para que o modelo considere o novo bpm.
  - `density`: (float) intervalo: `[0.0, 1.0]`.
    Controla a densidade de notas/sons musicais. Valores mais baixos produzem músicas mais esparsas, enquanto valores mais altos produzem músicas "mais ocupadas".
  - `brightness`: (float) intervalo: `[0.0, 1.0]`.
    Ajusta a qualidade tonal. Valores mais altos produzem áudio com som "mais brilhante", geralmente enfatizando frequências mais altas.
  - `scale`: (Enum) define a escala musical (chave e modo) para a geração. Use os
    [`Scale` valores de enum](#scale-enum) fornecidos pelo SDK. É necessário interromper/reproduzir ou redefinir o contexto para que o modelo considere a nova escala.
  - `mute_bass`: (bool) padrão: `False`.
    Controla se o modelo reduz o baixo das saídas.
  - `mute_drums`: (bool) padrão: `False`.
    Controla se o modelo reduz a bateria das saídas.
  - `only_bass_and_drums`: (bool) padrão: `False`.
    Direciona o modelo para tentar gerar apenas baixo e bateria.
  - `music_generation_mode`: (Enum) indica ao modelo se ele deve se concentrar na `QUALITY` (valor padrão) ou na `DIVERSITY` da música. Ele também pode ser definido como `VOCALIZATION` para permitir que o modelo gere vocalizações como outro instrumento (adicione-as como novos comandos).
- `PlaybackControl`: comandos para controlar aspectos de reprodução, como reproduzir, pausar, interromper ou redefinir o contexto.

Para `bpm`, `density`, `brightness` e `scale`, se nenhum valor for fornecido, o modelo vai decidir o que é melhor de acordo com os comandos iniciais.

Outros parâmetros clássicos, como `temperature` (0,0 a 3,0, padrão 1,1), `top_k` (1 a 1000, padrão 40) e `seed` (0 a 2.147.483.647, selecionado aleatoriamente por padrão), também podem ser personalizados no `MusicGenerationConfig`.

#### Valores de enum de escala

Confira todos os valores de escala que o modelo pode aceitar:

| Valor de enum | Escala / chave |
| --- | --- |
| `C_MAJOR_A_MINOR` | Dó maior / Lá menor |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | Ré♭ maior / Si♭ menor |
| `D_MAJOR_B_MINOR` | Ré maior / Si menor |
| `E_FLAT_MAJOR_C_MINOR` | Mi♭ maior / Dó menor |
| `E_MAJOR_D_FLAT_MINOR` | Mi maior / Ré♭ menor |
| `F_MAJOR_D_MINOR` | Fá maior / Ré menor |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | Sol♭ maior / Mi♭ menor |
| `G_MAJOR_E_MINOR` | Sol maior / Mi menor |
| `A_FLAT_MAJOR_F_MINOR` | Lá♭ maior / Fá menor |
| `A_MAJOR_G_FLAT_MINOR` | Lá maior / Sol♭ menor |
| `B_FLAT_MAJOR_G_MINOR` | Si♭ maior / Sol menor |
| `B_MAJOR_A_FLAT_MINOR` | Si maior / Sol♯/Lá♭ menor |
| `SCALE_UNSPECIFIED` | Padrão / O modelo decide |

O modelo é capaz de orientar as notas tocadas, mas não distingue entre chaves relativas. Assim, cada enum corresponde tanto ao maior quanto ao menor relativo. Por exemplo, `C_MAJOR_A_MINOR` corresponderia a todas as teclas brancas de um piano, e `F_MAJOR_D_MINOR` seria todas as teclas brancas, exceto o Si♭.

### Limitações

- Apenas instrumental: o modelo gera apenas música instrumental.
- Segurança: os comandos são verificados por filtros de segurança. Os comandos que acionam os filtros serão ignorados. Nesse caso, uma explicação será escrita no campo `filtered_prompt` da saída.
- Marca d'água: o áudio de saída sempre tem uma marca d'água para identificação, seguindo
  nossos [princípios de IA responsável](https://ai.google/responsibility/principles/?hl=pt-br).

## A seguir

- Gerar músicas completas e faixas vocais com o [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=pt-br),
- Em vez de música, aprenda a gerar conversas com vários locutores usando
  os [modelos TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pt-br),
- Saiba como gerar [imagens](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br) ou [vídeos](https://ai.google.dev/gemini-api/docs/video?hl=pt-br),
- Em vez de gerar música ou áudio, saiba como o Gemini pode
  [entender arquivos de áudio](https://ai.google.dev/gemini-api/docs/audio?hl=pt-br),
- Tenha uma conversa em tempo real com o Gemini usando a
  [API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br).

Confira o [Cookbook](https://github.com/google-gemini/cookbook) para mais
exemplos de código e tutoriais.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-06-01 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-06-01 UTC."],[],[]]
