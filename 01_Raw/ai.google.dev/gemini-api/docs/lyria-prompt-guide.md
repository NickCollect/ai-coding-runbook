---
source_url: https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=pt-BR
fetched_at: 2026-10-26T05:58:56.301389+00:00
title: "Guia de comandos do Lyria \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Guia de comandos do Lyria

A API Gemini oferece duas maneiras de gerar músicas com o Lyria:

- **Lyria 3.5 e Lyria 3 Clip**: geração sem streaming de clipes de 30 segundos ou músicas completas com letras e vocais. Consulte [Gerar músicas com o Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=pt-br).
- **Lyria RealTime**: streaming de música interativo em tempo real e controle ao vivo por WebSockets. Confira [Geração de músicas em tempo real com o Lyria RealTime](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=pt-br).

Os dois modelos respondem a comandos de texto descritivos, terminologia musical e instruções estruturais. Este guia mostra como escrever comandos eficazes para geração em lote e direcionamento em tempo real.

## Conceitos básicos de comandos

Seu comando pode ser uma frase curta:

```
A folk song about cute cats avoiding puddles, female vocals, acoustic guitar, sound of rain
```

Ou uma descrição estruturada e detalhada:

```
A 1980s-style synth-pop track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. The song should have a retro-futuristic feel with modern production polish. Upbeat tempo around 120 BPM, clear verse-chorus structure, and a memorable instrumental hook. The lyrics describe getting ready for a party.
```

Comandos curtos e detalhados geram bons resultados. Use as estratégias a seguir para guiar o modelo em direção ao som exato que você quer.

## Gênero e estilo

Comece o comando com o gênero principal. Você pode combinar gêneros para criar híbridos exclusivos:

- Uma fusão de metal e hip-hop
- Death metal combinado com vocais de ópera
- Música de câmara clássica com elementos eletrônicos sombrios
- Música eletrônica moderna (EDM) misturada com Europop

Você também pode especificar uma era musical ou variante regional:

- Boom-bap hip-hop do início dos anos 90
- Pop yé-yé francês dos anos 60
- Pós-punk e new wave dos anos 1980
- R&B mainstream dos anos 2000
- Tecno minimalista de Berlim ou hyphy da Bay Area

### Palavras-chave de gênero

Use estes termos de gênero reconhecidos nos seus comandos para o Lyria 3.5 e o Lyria RealTime:

- **Música eletrônica e dance**: `Acid House, Breakbeat, Chillout, Chiptune, Deep House, Drum & Bass, Dubstep, EDM, Electro Swing, Glitch Hop, Hyperpop, Minimal Techno, Moombahton, Psytrance, Synthpop, Techno, Trance, Trip Hop, Vaporwave`
- **Hip-hop e R&B**: `808 Hip Hop, Boom-Bap, Contemporary R&B, G-funk, Grime, Lo-Fi Hip Hop, Neo-Soul, New Jack Swing, Trap Beat`
- **Rock e alternativa**: `Alternative Country, Blues Rock, Classic Rock, Funk Metal, Garage Rock, Indie Folk, Indie Pop, Post-Punk, 60s Psychedelic Rock, Shoegaze, Surf Rock`
- **Jazz, soul e funk**: `Acid Jazz, Afrobeat, Bossa Nova, Disco Funk, Funk, Jazz Fusion, Latin Jazz`
- **Música folclórica e tradicional**: `Bengal Baul, Bhangra, Bluegrass, Celtic Folk, Cumbia, Indian Classical, Irish Folk, Merengue, Polka, Reggae, Reggaeton, Renaissance Music, Salsa`
- **Clássica e acústica**: `Baroque, Orchestral Score, Piano Ballad`

## Instrumentos e texturas

A Lyria seleciona automaticamente a instrumentação adequada para o gênero solicitado. Se você quiser instrumentos específicos ou combinações incomuns, declare-os explicitamente:

```
A dance track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. A saxophone solo enters during the bridge.
```

Descreva como os instrumentos soam e interagem para definir o clima e a textura:

- Uma linha de baixo 303 distorcida atravessando hi-hats nítidos e firmes
- Pads de sintetizador analógico quentes crescendo sob um violão acústico seco e intimista
- Uma parede de som construída com várias camadas de guitarra fuzz, com vocais distantes e cheios de reverb

### Palavras-chave de instrumento

- **Teclados e sintetizadores**: `Buchla Synths, Clavichord, Dirty Synths, Harpsichord, Mellotron, Moog Oscillations, Ragtime Piano, Rhodes Piano, Smooth Pianos, Spacey Synths, Synth Pads`
- **Baixo e bateria**: `303 Acid Bass, 808 Hip Hop Beat, Boomy Bass, Conga Drums, Drumline, Funk Drums, Precision Bass, Tabla, TR-909 Drum Machine`
- **Guitarras e cordas**: `Banjo, Balalaika, Bouzouki, Cello, Charango, Dulcimer, Fiddle, Flamenco Guitar, Guitar, Harp, Koto, Lyre, Mandolin, Pipa, Shamisen, Shredding Guitar, Sitar, Slide Guitar, Viola Ensemble, Warm Acoustic Guitar`
- **Sopros e metais**: `Alto Saxophone, Bagpipes, Bass Clarinet, Didgeridoo, Harmonica, Ocarina, Trumpet, Tuba, Woodwinds`
- **Percussão**: `Bongos, Djembe, Glockenspiel, Hang Drum, Kalimba, Maracas, Marimba, Mbira, Steel Drum, Vibraphone`

## Estrutura e tempo da música

Para o Lyria 3.5, defina a progressão da música usando tags ou setas:

- `[Intro] -> [Verse 1] -> [Chorus] -> [Verse 2] -> [Chorus] -> [Bridge] -> [Outro]`
- Comece com uma introdução de piano suave, crie um verso energético, faça uma pausa para um momento de silêncio e depois exploda no refrão.

É possível direcionar a dinâmica e as transições de energia:

- Crie tensão no pré-refrão e depois faça uma pausa antes de um refrão explosivo
- Crescendo gradual ao longo da música, adicionando um instrumento por seção
- Uma parada repentina após a ponte, seguida de um refrão a cappella

Você também pode solicitar marcadores de tempo específicos:

- Crie uma batida aos 12 segundos
- A amostra vocal se repete a cada quatro compassos
- O refrão começa aos 22 segundos

## Letras e vocais

O Lyria 3.5 gera faixas vocais com letras por padrão. Você pode fornecer sua própria letra, pedir que o modelo gere uma ou solicitar uma música instrumental.

### Usar suas próprias letras

Inclua a letra diretamente no comando abaixo de um cabeçalho `Lyrics:`. Marque cada seção para orientar a entrega vocal:

```
Lyrics:

[Intro]
Ooooh, yeah

[Verse 1]
Early morning rain on the window pane
City lights wash away the pain
Walking down this empty street again

[Chorus]
We keep moving on (moving on)
Until the morning light
Everything will be alright
```

Use parênteses para vocais de apoio, ecos ou improvisos, como `(moving on)`.

### Direcionar letras geradas

Ao pedir para o Lyria 3.5 escrever letras, descreva a narrativa, a emoção ou as frases principais:

```
The lyrics describe driving down the Pacific Coast Highway at sunset. The mood is nostalgic and reflective. Include an uplifting, anthemic chorus about second chances and starting over.
```

Para gêneros eletrônicos e de dança, peça refrões vocais curtos e repetidos:

```
An upbeat dance-pop track with a repetitive, high-energy vocal hook: "Feel the rhythm all night long."
```

### Entrega vocal e perfis de cantores

Especifique o gênero, a extensão vocal e o timbre para uma interpretação precisa:

- **Soprano feminino**: timbre claro e cristalino com uma entrega ágil e crescente. Tom brilhante capaz de criar texturas leves e suaves.
- **Contralto feminino**: alcance mais baixo rico, quente e rouco. Timbre esfumaçado com uma voz de peito ressonante e cheia de alma.
- **Tenor masculino**: brilhante, penetrante e energético. Timbre jovem com grande potência de canto que se destaca em mixagens densas.
- **Barítono masculino**: voz grave e aveludada com um tom quente, suave e melodioso.
- **Rocker desgastado**: timbre áspero e forte que lembra o rock alternativo dos anos 1990. Intensidade emocional bruta com notas agudas tensas.

### Efeitos vocais não líricos

Você também pode pedir diálogos falados, cortes vocais e efeitos de amostragem:

- Uma voz de transmissão de rádio vintage apresenta a música antes de a batida começar.
- Uma voz sussurra logo antes da queda, seguida de sintetizadores de alta energia.
- Amostras vocais cortadas e com mudança de tom em loop como um elemento de ritmo instrumental.

## Parâmetros musicais

Refine o comando com propriedades musicais padrão:

- **Tempo (BPM)**: defina o tempo diretamente (por exemplo, `120 BPM`, `slow tempo around 72 BPM`, `fast 160 BPM`).
- **Tonalidade e escala**: especifique a tonalidade e a nota fundamental (por exemplo, `in G major`, `in D minor`, `in C pentatonic`).
- **Humor e atmosfera**: use adjetivos descritivos de emoções:
  `Ambient, Bright, Chill, Dark, Dreamy, Emotional, Ethereal, Euphoric, Funky, Groovy, Melancholic, Nostalgic, Ominous, Psychedelic, Relaxed, Soulful, Triumphant, Upbeat, Whimsical`

## Comandos do Lyria RealTime

O Lyria RealTime usa **comandos ponderados** em vez de uma única string de comando monolítica. Isso permite combinar várias influências musicais de forma dinâmica e direcionar a música continuamente por uma conexão WebSocket.

### Estrutura de comando ponderada

Cada comando ponderado consiste em uma frase de texto descritiva e uma ponderação de ponto flutuante:

```
prompts = [
    types.WeightedPrompt(text="minimal techno", weight=1.0),
    types.WeightedPrompt(text="deep sub bass", weight=0.6),
    types.WeightedPrompt(text="shimmering hi-hats", weight=0.4),
]
```

### Estratégias de direção em tempo real

- **Combinar gêneros**: combine estilos distintos atribuindo ponderações equilibradas:
  - `ambient synth pads (weight: 0.8)` + `lo-fi hip-hop drums (weight: 0.6)`
  - `flamenco guitar (weight: 0.7)` + `deep house groove (weight: 0.5)`
- **Transições dinâmicas**: para fazer uma transição suave da música, ajuste as ponderações de comando ao longo do tempo:
  1. Comece com `chill jazz piano (weight: 1.0)`.
  2. Adicione `electronic breakbeat (weight: 0.3)` gradualmente.
  3. Aumente `electronic breakbeat` para `0.8` e diminua `chill jazz piano` para `0.3`.
- **Camadas de elementos**: mantenha as tags de instrumento e de clima separadas para poder ajustá-las de forma independente:
  - Comando 1: `bossa nova guitar (weight: 0.9)`
  - Comando 2: `warm acoustic bass (weight: 0.7)`
  - Comando 3: `subtle vinyl crackle (weight: 0.3)`

## Exemplos de comandos

### Exemplos do Lyria 3.5

- **Lo-Fi Study Beat**:
  `none
  A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes piano chords, a relaxed boom-bap drum groove at 82 BPM, and a warm upright bassline. Instrumental only.`
- **Hino pop**:
  `none
  An upbeat, feel-good indie-pop song in G major at 122 BPM. Bright acoustic guitar strumming, driving kick drum, handclaps, and warm female vocal harmonies. The lyrics describe an unforgettable summer road trip with friends.`
- **Cyberpunk cinematográfico**:
  `none
  Dark, cinematic cyberpunk synthwave at 110 BPM in D minor. Heavy distorted bass, ominous arpeggiated analog synthesizers, distant metallic percussion, and an ethereal female vocalise swelling during the climax.`

### Conjunto de direção do Lyria RealTime

```
# Initial high-energy groove
await session.set_weighted_prompts(
    prompts=[
        types.WeightedPrompt(text="techno groove", weight=1.0),
        types.WeightedPrompt(text="acid 303 bass", weight=0.8),
    ]
)

# Transition to a melodic breakdown
await session.set_weighted_prompts(
    prompts=[
        types.WeightedPrompt(text="ambient synth pads", weight=1.0),
        types.WeightedPrompt(text="subtle reverberant piano", weight=0.7),
        types.WeightedPrompt(text="techno groove", weight=0.2),
    ]
)
```

## A seguir

- [Gerar música com o Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=pt-br): crie músicas completas e clipes de 30 segundos usando a API Interactions.
- [Geração de música em tempo real com o Lyria RealTime](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=pt-br): crie aplicativos interativos de streaming de música em tempo real com WebSockets.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-18 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-18 UTC."],[],[]]
