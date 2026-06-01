---
source_url: https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=pt-BR
fetched_at: 2026-06-01T06:05:03.621745+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Geração de conversão de texto em voz (TTS)

A API Gemini pode transformar entradas de texto em áudio de um ou vários locutores usando os recursos de geração de texto em voz (TTS) do Gemini.
A geração de conversão de texto em voz (TTS) é *[controlável](#controllable)*, ou seja, você pode usar a linguagem natural para estruturar interações e orientar o *estilo*, o *sotaque*, o *ritmo* e o *tom* do áudio.

A capacidade de TTS é diferente da geração de fala fornecida pela [API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br), que foi projetada para áudio interativo e não estruturado, além de entradas e saídas multimodais. Embora a API Live seja excelente em contextos de conversação dinâmica, a TTS pela API Gemini é feita para cenários que exigem recitação exata de texto com controle refinado sobre estilo e som, como geração de podcasts ou audiolivros.

Este guia mostra como gerar áudio de um ou vários locutores com base em texto.

## Antes de começar

Use uma variante do modelo Gemini 2.5 com recursos de conversão de texto em voz (TTS) do Gemini, conforme listado na seção [Modelos compatíveis](https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=pt-br#supported-models). Para ter os melhores resultados, considere qual modelo se adapta melhor ao seu caso de uso específico.

Talvez seja útil [testar os modelos TTS do Gemini 2.5 no AI Studio]

## TTS com uma única voz

Para converter texto em áudio de um único falante, defina a modalidade de resposta como "audio" e transmita um objeto `speech_config` com um nome de voz.
Escolha um nome de voz nas [vozes de saída](#voices) pré-criadas.

Este exemplo salva o áudio de saída do modelo em um arquivo wave:

### Python

```
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_modalities=["audio"],
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)

wave_file('out.wav', base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: "Say cheerfully: Have a wonderful day!",
      response_modalities: ['audio'],
      generation_config: {
         speech_config: [
            { voice: 'Kore' }
         ]
      },
    });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');

   await saveWaveFile('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_modalities": ["audio"],
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

É possível recuperar os dados de áudio gerados usando a propriedade `interaction.output_audio`, que retorna o último bloco de áudio gerado. Para mais detalhes sobre
propriedades de conveniência, consulte a
[Visão geral das interações](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br#convenience-properties).

## TTS com vários locutores

Para áudio com vários alto-falantes, você precisa de um objeto `multi_speaker_voice_config` com
cada alto-falante (até dois) configurado como um `speaker_voice_config`.
Você precisa definir cada `speaker` com os mesmos nomes usados no
[comando](#controllable):

### Python

```
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

prompt = """TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?"""

 interaction = client.interactions.create(
     model="gemini-3.1-flash-tts-preview",
     input=prompt,
     response_modalities=["audio"],
     generation_config={
         "speech_config": [
             {"speaker": "Joe", "voice": "Kore"},
             {"speaker": "Jane", "voice": "Puck"}
         ]
     }
 )

wave_file('out.wav', base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const client = new GoogleGenAI({});

   const prompt = `TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?`;

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: prompt,
      response_modalities: ['audio'],
      generation_config: {
         speech_config: [
            { speaker: 'Joe', voice: 'Kore' },
            { speaker: 'Jane', voice: 'Puck' }
         ]
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');

   await saveWaveFile('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
  "model": "gemini-3.1-flash-tts-preview",
  "input": "TTS the following conversation between Joe and Jane: Joe: Hows it going today Jane? Jane: Not too bad, how about you?",
  "response_modalities": ["audio"],
  "generation_config": {
    "speech_config": [
      { "speaker": "Joe", "voice": "Kore" },
      { "speaker": "Jane", "voice": "Puck" }
    ]
  }
}'
```

## Controlar o estilo de fala com comandos

Você pode controlar o estilo, o tom, o sotaque e o ritmo usando comandos em linguagem natural para TTS de um ou vários locutores.
Por exemplo, em um comando com um único falante, você pode dizer:

```
Say in an spooky whisper:
"By the pricking of my thumbs...
Something wicked this way comes"
```

Em um comando com vários falantes, forneça ao modelo o nome de cada um e a transcrição correspondente. Você também pode dar orientações para cada pessoa
individualmente:

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... what's on the agenda today?
Speaker2: You're never going to guess!
```

Use uma [opção de voz](#voices) que corresponda ao estilo ou à emoção que você quer transmitir para enfatizar ainda mais. No comando anterior, por exemplo, a voz ofegante de *Encélado* pode enfatizar "cansado" e "entediado", enquanto o tom alegre de *Puck* pode complementar "animado" e "feliz".

## Gerar um comando para converter em áudio

Os modelos de TTS só geram áudio, mas você pode usar [outros modelos](https://ai.google.dev/gemini-api/docs/models?hl=pt-br) para gerar uma transcrição primeiro e depois passar essa transcrição para o modelo de TTS ler em voz alta.

### Python

```
from google import genai

client = genai.Client()

transcript_interaction = client.interactions.create(
   model="gemini-3.5-flash",
   input="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam."""
)
transcript = transcript_interaction.output_text

tts_interaction = client.interactions.create(
   model="gemini-3.1-flash-tts-preview",
   input=transcript,
   response_modalities=["audio"],
   generation_config={
      "speech_config": [
         {"speaker": "Dr. Anya", "voice": "Kore"},
         {"speaker": "Liam", "voice": "Puck"}
      ]
   }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {

const transcriptInteraction = await client.interactions.create({
   model: "gemini-3.5-flash",
   input: "Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam.",
   })

const ttsInteraction = await client.interactions.create({
   model: "gemini-3.1-flash-tts-preview",
   input: transcriptInteraction.output_text,
   response_modalities: ['audio'],
   generation_config: {
      speech_config: [
         { speaker: "Dr. Anya", voice: "Kore" },
         { speaker: "Liam", voice: "Puck" }
      ]
   }
  });
}

await main();
```

## Opções de voz

Os modelos de TTS são compatíveis com as seguintes 30 opções de voz no campo `voice_name`:

|  |  |  |
| --- | --- | --- |
| **Zephyr**: *Bright* | **Puck**: *Upbeat* | **Charon**: *informativa* |
| **Kore**: *Firme* | **Fenrir**: *Excitável* | **Leda**: *Juventude* |
| **Orus**: *Firm* | **Aoede**: *Breezy* | **Callirrhoe** -- *Tranquila* |
| **Autonoe**: *Bright* | **Enceladus**: *Breathy* | **Iapetus**: *Limpar* |
| **Umbriel**: *tranquilo* | **Algieba**: *Smooth* | **Despina**: *Smooth* |
| **Erinome**: *Limpar* | **Algenib**: *Gravelly* | **Rasalgethi**: *informativa* |
| **Laomedeia**: *Upbeat* | **Achernar**: *suave* | **Alnilam**: *Firme* |
| **Schedar**: *Even* | **Gacrux**: *Adulto* | **Pulcherrima**: *projetada* |
| **Achird**: *Amigável* | **Zubenelgenubi**: *Casual* | **Vindemiatrix**: *Gentil* |
| **Sadachbia**: *Lively* | **Sadaltager**: *Conhecedor* | **Sulafat**: *quente* |

Você pode ouvir todas as opções de voz em

## Idiomas compatíveis

Os modelos de TTS detectam automaticamente o idioma de entrada. Os seguintes idiomas são aceitos:

| Idioma | Código BCP-47 | Idioma | Código BCP-47 |
| --- | --- | --- | --- |
| Árabe | ar | Filipino | fil |
| Bengali | bn | Finlandês | fi |
| Holandês | nl | Galego | gl |
| Inglês | en | Georgiano | ka |
| Francês | fr | Grego | el |
| Alemão | de | Gujarati | gu |
| Hindi | hi | Crioulo haitiano | ht |
| Indonésio | ID | Hebraico | ele |
| Italiano | it | Húngaro | hu |
| Japonês | ja | Islandês | é |
| Coreano | ko | Javanês | jv |
| Marati | mr | Canarês | kn |
| Polonês | pl | Concani | kok |
| Português | pt | Laosiano | lo |
| Romeno | ro | Latim | la |
| Russo | ru | Letão | lv |
| Espanhol | es | Lituano | lt |
| Tâmil | ta | Luxemburguês | lb |
| Télugo | te | Macedônio | mk |
| Tailandês | th | Maithili | mai |
| Turco | tr | Malgaxe | mg |
| Ucraniano | uk | Malaio | ms |
| Vietnamita | vi | Malaiala | ml |
| Africâner | af | Mongol | mn |
| Albanês | sq | Nepalês | ne |
| Amárico | sou | Norueguês (bokmål) | nb |
| Armênio | hy | Norueguês (Nynorsk) | nn |
| Azerbaijano | az | Oriá | ou |
| Basco | eu | Pashto | ps |
| Bielorrusso | be | Persa | fa |
| Búlgaro | bg | Punjabi | pa |
| Birmanês | my | Sérvio | sr |
| Catalão | ca | Sindi | sd |
| Cebuano | ceb | Cingalês | si |
| Chinês, mandarim | cmn | Eslovaco | sk |
| Croata | h | Esloveno | sl |
| Tcheco | cs | Suaíli | sw |
| Dinamarquês | da | Sueco | sv |
| Estoniano | et | Urdu | ur |

## Modelos compatíveis

| Modelo | Falante único | Vários falantes |
| --- | --- | --- |
| [Pré-lançamento do Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=pt-br) | ✔️ | ✔️ |
| [Pré-lançamento do Gemini 2.5 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=pt-br) | ✔️ | ✔️ |
| [Pré-lançamento da TTS do Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=pt-br) | ✔️ | ✔️ |

## Guia de comandos

O modelo **Gemini Native Audio Generation Text-to-Speech (TTS)** se diferencia dos modelos convencionais de TTS por usar um modelo de linguagem grande que sabe ***não apenas o que dizer, mas também como dizer***.

Pense em um comando avançado como uma instrução do sistema para o modelo seguir. É uma maneira de dar ao modelo mais contexto e controle sobre o desempenho.

Para aproveitar esse recurso, os usuários podem se imaginar como diretores definindo uma cena para um talento de voz virtual. Para criar um comando, recomendamos considerar os seguintes componentes: um **perfil de áudio** que define a identidade e o arquétipo principais do personagem; uma **descrição da cena** que estabelece o ambiente físico e a "vibe" emocional; e **observações do diretor** que oferecem orientações de performance mais precisas sobre estilo, sotaque e controle de ritmo.

Ao fornecer instruções sutis, como um sotaque regional preciso, recursos paralinguísticos específicos (por exemplo, respiração) ou ritmo, os usuários podem aproveitar a capacidade de reconhecimento de contexto do modelo para gerar performances de áudio altamente dinâmicas, naturais e expressivas. Para uma performance ideal, recomendamos que a **transcrição** e os comandos de direção estejam alinhados, *para que "quem está dizendo"* corresponda a *"o que está sendo dito"* e *"como está sendo dito"*.

O objetivo deste guia é oferecer orientação fundamental e gerar ideias ao desenvolver experiências de áudio usando a geração de áudio do Gemini TTS. Estamos ansiosos para ver o que você vai criar!

### Tags de áudio

As tags são modificadores inline, como `[whispers]` ou `[laughs]`, que oferecem controle granular sobre a veiculação. Use-os para mudar o tom, o ritmo e a
vibe emocional de uma linha ou seção da transcrição. Você também pode usar esses recursos para
adicionar interjeições e alguns outros sons não verbais à performance, como
`[cough]`, `[sighs]` ou `[gasp]`.

Não há uma lista exaustiva do que funciona ou não. Recomendamos testar diferentes emoções e expressões para ver como a saída muda.

Se a transcrição não estiver em inglês, recomendamos que você use tags de áudio em inglês para ter os melhores resultados.

**Use a criatividade com as tags de áudio**

Para mostrar o tipo de variabilidade que você pode ter com as tags de áudio, aqui estão alguns exemplos que dizem a mesma coisa, mas a entrega muda com base nas tags usadas.

Você pode mudar a ênfase da entrega adicionando tags no início de uma
linha para deixar o alto-falante animado, entediado ou relutante:

- `[excitedly]` Olá! Sou um novo modelo de conversão de texto em voz e posso dizer as coisas de várias maneiras diferentes. Como posso ajudar?
- `[bored]` Olá, sou um novo modelo de conversão de texto em voz…
- `[reluctantly]` Olá, sou um novo modelo de conversão de texto em voz…

As tags também podem ser usadas para mudar o ritmo da entrega ou combinar ritmo com ênfase:

- `[very fast]` Olá, sou um novo modelo de conversão de texto em voz…
- `[very slow]` Olá, sou um novo modelo de conversão de texto em voz…
- `[sarcastically, one painfully slow word at a time]` Olá, sou um novo modelo de conversão de texto em voz…

Você também tem controle preciso sobre seções específicas, o que significa que pode sussurrar
uma parte e gritar outra.

- `[whispers]` Olá, sou um novo modelo de conversão de texto em voz, `[shouting]` e posso
  dizer as coisas de várias maneiras diferentes. `[whispers]` Como posso ajudar?

Você também pode testar qualquer ideia criativa:

- `[like a cartoon dog]` Olá, sou um novo modelo de conversão de texto em voz…
- `[like dracula]` Olá, sou um novo modelo de conversão de texto em voz…

As tags usadas com frequência incluem:

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

As tags oferecem controle rápido sobre a entrega da transcrição. Para ter ainda mais controle, combine-as com um comando de contexto para definir o tom e a atmosfera geral da performance.

### Estrutura do comando

Um comando robusto inclui os seguintes elementos que se unem para criar uma ótima performance:

- **Perfil de áudio**: estabelece uma persona para a voz, definindo uma identidade, um arquétipo e outras características, como idade, histórico etc.
- **Cena**: define o cenário. Descreve o ambiente físico e a "vibe".
- **Observações do diretor**: orientações de performance em que você pode detalhar quais instruções são importantes para o talento virtual. Exemplos são estilo, respiração, ritmo, articulação e sotaque.
- **Contexto de exemplo**: dá ao modelo um ponto de partida contextual para que seu
  ator virtual entre na cena que você configurou de forma natural.
- **Transcrição**: o texto que o modelo vai falar. Para ter o melhor desempenho, lembre-se de que o tema e o estilo de escrita da transcrição precisam estar relacionados às instruções que você está.
- **Tags de áudio**: modificadores que podem ser inseridos em uma transcrição para mudar a forma como essa parte do texto é entregue, como `[whispers]` ou `[shouting]`.

Exemplo de comando completo:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"

## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to wake
up an entire nation.

### DIRECTOR'S NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
* Dynamics: High projection without shouting. Punchy consonants and elongated
vowels on excitement words (e.g., "Beauuutiful morning").

Pace: Speaks at an energetic pace, keeping up with the fast music.  Speaks
with A "bouncing" cadence. High-speed delivery with fluid transitions - no dead
air, no gaps.

Accent: Jaz is from Brixton, London

### SAMPLE CONTEXT
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

#### TRANSCRIPT
Yes, massive vibes in the studio! You are locked in and it is absolutely
popping off in London right now. If you're stuck on the tube, or just sat
there pretending to work... stop it. Seriously, I see you. Turn this up!
We've got the project roadmap landing in three, two... let's go!
```

### Estratégias detalhadas de comandos

Analise cada elemento do comando da seguinte maneira:

#### Perfil de áudio

Descreva brevemente a personalidade do personagem.

- **Nome.** Dar um nome ao personagem ajuda a fundamentar o modelo e a melhorar a performance. Refira-se ao personagem pelo nome ao definir a cena e o contexto.
- **Papel**. Identidade principal e arquétipo do personagem que está atuando na cena, por exemplo, DJ de rádio, podcaster, repórter de notícias etc.

Exemplos:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### Cenário

Defina o contexto da cena, incluindo local, clima e detalhes ambientais que estabelecem o tom e a atmosfera. Descreva o que está acontecendo ao redor do personagem e como isso o afeta. A cena fornece o contexto ambiental para toda a interação e orienta a atuação de maneira sutil e orgânica.

Exemplos:

```
## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to
wake up an entire nation.
```

```
## THE SCENE: Homegrown Studio
A meticulously sound-treated bedroom in a suburban home. The space is
deadened by plush velvet curtains and a heavy rug, but there is a
distinct "proximity effect."
```

#### Observações do diretor

Esta seção essencial inclui orientações específicas sobre performance. Você pode pular todos os outros elementos, mas recomendamos que inclua este.

Defina apenas o que é importante para a performance, tomando cuidado para não especificar demais. Muitas regras restritas limitam a criatividade dos modelos e podem resultar em uma performance pior. Equilibre a descrição da função e da cena com as regras específicas de performance.

As instruções mais comuns são **Estilo, ritmo e sotaque**, mas o modelo não se limita a elas nem as exige. Inclua instruções personalizadas para abordar outros detalhes importantes para sua performance e forneça o máximo ou o mínimo de detalhes necessário.

Exemplo:

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**Estilo**:

Define o tom e o estilo da fala gerada. Inclua palavras como "animado",
"enérgico", "relaxado", "entediado" etc. para orientar a performance. Seja descritivo e forneça o máximo de detalhes possível: *"Entusiasmo contagiante. O ouvinte precisa sentir que faz parte de um evento comunitário enorme e emocionante".* funciona melhor do que dizer *"enérgico e entusiasmado".*

Você pode até tentar termos populares no setor de narração, como "sorriso vocal". Você pode adicionar quantas características de estilo quiser.

Exemplos:

Emoção simples

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

Mais profundidade

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

Complexo

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**Sotaque:**

Descreva o sotaque selecionado. Quanto mais específico for o comando, melhores serão os resultados. Por exemplo, use "*Sotaque inglês britânico como ouvido em Croydon, Inglaterra*" em vez de "*Sotaque britânico*".

Exemplos:

```
### DIRECTORS NOTES
...
Accent: Southern california valley girl from Laguna Beach
...
```

```
### DIRECTORS NOTES
...
Accent: Jaz is a from Brixton, London
...
```

**Ritmo**:

Ritmo geral e variação de ritmo ao longo da matéria.

Exemplos:

Simples

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

Mais profundidade

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

Complexo

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

**Experimente**

Teste alguns desses exemplos no [app TTS](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=pt-br) e deixe o Gemini assumir a direção. Confira algumas dicas para fazer ótimas performances vocais:

- Não se esqueça de manter todo o comando coerente. O roteiro e a direção trabalham juntos para criar uma ótima performance.
- Não é necessário descrever tudo. Às vezes, dar espaço para o modelo preencher as lacunas ajuda a manter a naturalidade. (Assim como um ator talentoso)
- Se você estiver com dificuldades, peça ajuda ao Gemini para criar seu roteiro ou apresentação.

## Limitações

- Os modelos de TTS só podem receber entradas de texto e gerar saídas de áudio.
- Uma sessão de TTS tem um limite de [janela de contexto](https://ai.google.dev/gemini-api/docs/long-context?hl=pt-br) de 32 mil tokens.
- Consulte a seção [Idiomas](https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=pt-br#languages) para saber quais idiomas são aceitos.
- A TTS não oferece suporte a streaming.

As restrições a seguir se aplicam especificamente ao usar o modelo de pré-lançamento da TTS do Gemini 3.1 Flash para geração de fala:

- **Inconsistência de voz com as instruções do comando**:a saída do modelo nem sempre corresponde ao falante selecionado, fazendo com que o áudio soe diferente do esperado. Para evitar tons incompatíveis (como uma voz masculina grave tentando falar como uma menina), verifique se o tom e o contexto da sua solicitação escrita estão alinhados naturalmente com o perfil do locutor selecionado.
- **Qualidade de saídas mais longas**:a qualidade e a consistência da fala podem começar a variar com saídas geradas que duram mais do que alguns minutos. Recomendamos dividir as transcrições em partes menores.
- **Retornos ocasionais de tokens de texto**:o modelo às vezes retorna tokens de texto em vez de tokens de áudio, fazendo com que o servidor falhe na solicitação com um erro `500`. Como isso ocorre aleatoriamente em uma porcentagem muito pequena de solicitações, implemente uma lógica de nova tentativa automatizada no aplicativo para lidar com elas.
- **Rejeições falsas do classificador de comandos**:comandos vagos podem não acionar o classificador de síntese de voz, resultando em uma solicitação rejeitada (`PROHIBITED_CONTENT`) ou fazendo com que o modelo leia em voz alta as instruções de estilo e as observações do diretor. Valide seus comandos adicionando um preâmbulo claro
  instruindo o modelo a sintetizar a fala e rotule explicitamente onde a
  transcrição falada real começa.

## A seguir

- A [API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br) do Gemini oferece opções interativas de geração de áudio que podem ser intercaladas com outras modalidades.
- Para trabalhar com *entradas* de áudio, consulte o guia [Compreensão de áudio](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-28 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-28 UTC."],[],[]]
