---
source_url: https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=it
fetched_at: 2026-11-02T07:11:45.142530+00:00
title: "Guida ai prompt di Lyria \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Guida ai prompt di Lyria

L'API Gemini offre due modi per generare musica con Lyria:

- **Lyria 3.5 e Lyria 3 Clip**: generazione non in streaming di clip di 30 secondi o brani di lunga durata con testi e voci. Consulta [Generare musica con Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=it).
- **Lyria RealTime**: streaming musicale interattivo in tempo reale e controllo in tempo reale tramite WebSocket. Consulta [Generazione di musica in tempo reale con Lyria RealTime](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=it).

Entrambi i modelli rispondono a prompt di testo descrittivi, terminologia musicale e indicazioni strutturali. Questa guida spiega come scrivere prompt efficaci sia per la generazione batch sia per la guida in tempo reale.

## Nozioni di base sui prompt

Il prompt può essere una breve frase:

```
A folk song about cute cats avoiding puddles, female vocals, acoustic guitar, sound of rain
```

Oppure una descrizione strutturata e dettagliata:

```
A 1980s-style synth-pop track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. The song should have a retro-futuristic feel with modern production polish. Upbeat tempo around 120 BPM, clear verse-chorus structure, and a memorable instrumental hook. The lyrics describe getting ready for a party.
```

Sia i prompt brevi che quelli dettagliati producono risultati efficaci. Utilizza le seguenti strategie per indirizzare il modello verso il suono esatto che desideri.

## Genere e stile

Inizia il prompt con il genere principale. Puoi combinare i generi per creare ibridi unici:

- Una fusione di metal e hip hop
- Death metal combinato con voci liriche
- Musica da camera classica con elementi elettronici cupi
- Musica dance elettronica (EDM) moderna mixata con Europop

Puoi anche specificare un'epoca musicale o una variante regionale:

- Hip hop boom-bap dei primi anni '90
- Pop yé-yé francese degli anni '60
- Post-punk e new wave degli anni '80
- R&B mainstream degli anni 2000
- Techno minimal di Berlino o hyphy della Bay Area

### Parole chiave di genere

Utilizza questi termini di genere riconosciuti nei prompt per Lyria 3.5 e Lyria RealTime:

- **Dance ed elettronica**: `Acid House, Breakbeat, Chillout, Chiptune, Deep House, Drum & Bass, Dubstep, EDM, Electro Swing, Glitch Hop, Hyperpop, Minimal Techno, Moombahton, Psytrance, Synthpop, Techno, Trance, Trip Hop, Vaporwave`
- **Hip hop e R&B**: `808 Hip Hop, Boom-Bap, Contemporary R&B, G-funk, Grime, Lo-Fi Hip Hop, Neo-Soul, New Jack Swing, Trap Beat`
- **Rock e alternative**: `Alternative Country, Blues Rock, Classic Rock, Funk Metal, Garage Rock, Indie Folk, Indie Pop, Post-Punk, 60s Psychedelic Rock, Shoegaze, Surf Rock`
- **Jazz, soul e funk**: `Acid Jazz, Afrobeat, Bossa Nova, Disco Funk, Funk, Jazz Fusion, Latin Jazz`
- **Folk e tradizionale**: `Bengal Baul, Bhangra, Bluegrass, Celtic Folk, Cumbia, Indian Classical, Irish Folk, Merengue, Polka, Reggae, Reggaeton, Renaissance Music, Salsa`
- **Classical & Acoustic**: `Baroque, Orchestral Score, Piano Ballad`

## Strumenti e texture

Lyria seleziona automaticamente gli strumenti appropriati per il genere richiesto. Se vuoi strumenti specifici o combinazioni insolite, dichiarali esplicitamente:

```
A dance track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. A saxophone solo enters during the bridge.
```

Descrivi il suono e l'interazione degli strumenti per creare l'atmosfera e la trama:

- Una linea di basso 303 distorta che si fa strada tra hi-hat nitidi e compatti
- Pad di sintetizzatore analogico caldi che si gonfiano sotto una chitarra acustica pulita e intima
- Un muro di suono costruito da più strati di chitarra fuzz, con voci lontane e piene di riverbero

### Parole chiave dello strumento

- **Tastiere e sintetizzatori**: `Buchla Synths, Clavichord, Dirty Synths, Harpsichord, Mellotron, Moog Oscillations, Ragtime Piano, Rhodes Piano, Smooth Pianos, Spacey Synths, Synth Pads`
- **Basso e batteria**: `303 Acid Bass, 808 Hip Hop Beat, Boomy Bass, Conga Drums, Drumline, Funk Drums, Precision Bass, Tabla, TR-909 Drum Machine`
- **Chitarre e corde**: `Banjo, Balalaika, Bouzouki, Cello, Charango, Dulcimer, Fiddle, Flamenco Guitar, Guitar, Harp, Koto, Lyre, Mandolin, Pipa, Shamisen, Shredding Guitar, Sitar, Slide Guitar, Viola Ensemble, Warm Acoustic Guitar`
- **Fiati**: `Alto Saxophone, Bagpipes, Bass Clarinet, Didgeridoo, Harmonica, Ocarina, Trumpet, Tuba, Woodwinds`
- **Percussioni**: `Bongos, Djembe, Glockenspiel, Hang Drum, Kalimba, Maracas, Marimba, Mbira, Steel Drum, Vibraphone`

## Struttura e tempistica del brano

Per Lyria 3.5, definisci la progressione del brano utilizzando tag o frecce:

- `[Intro] -> [Verse 1] -> [Chorus] -> [Verse 2] -> [Chorus] -> [Bridge] -> [Outro]`
- Inizia con un'introduzione di pianoforte tranquilla, passa a una strofa energica, fermati per un momento di silenzio, poi esplodi nel ritornello.

Puoi dirigere le dinamiche e le transizioni energetiche:

- Crea tensione con il pre-chorus, poi passa al silenzio prima di un ritornello esplosivo
- Crescendo graduale durante il brano, con l'aggiunta di uno strumento per sezione
- Un'interruzione improvvisa dopo il ponte, seguita da un coro a cappella

Puoi anche richiedere indicatori di tempo specifici:

- Crea un crescendo fino al beat drop a 12 secondi
- Il sample vocale si ripete ogni 4 battute
- Il ritornello inizia a 22 secondi

## Testi e parti vocali

Lyria 3.5 genera tracce vocali con testi per impostazione predefinita. Puoi fornire i tuoi testi, chiedere al modello di generarli o richiedere una traccia strumentale.

### Utilizzo dei propri testi

Includi il testo direttamente nel prompt sotto un'intestazione `Lyrics:`. Tagga ogni sezione per guidare la dizione:

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

Utilizza le parentesi per le voci di accompagnamento, gli echi o le improvvisazioni, ad esempio `(moving on)`.

### Indicazioni per i testi generati

Quando chiedi a Lyria 3.5 di scrivere un testo, delinea la narrazione, l'emozione o le frasi chiave:

```
The lyrics describe driving down the Pacific Coast Highway at sunset. The mood is nostalgic and reflective. Include an uplifting, anthemic chorus about second chances and starting over.
```

Per i generi elettronici e dance, richiedi brevi hook vocali ripetuti:

```
An upbeat dance-pop track with a repetitive, high-energy vocal hook: "Feel the rhythm all night long."
```

### Prestazione vocale e profili dei cantanti

Specifica il genere, la gamma vocale e il timbro per una resa precisa:

- **Soprano femminile**: timbro cristallino e agile, con un'esecuzione che si eleva. Tono brillante in grado di creare trame ariose e leggere.
- **Contralto femminile**: gamma bassa ricca, calda e rauca. Timbro fumoso con una voce di petto profonda e piena di sentimento.
- **Tenore maschile**: brillante, penetrante ed energico. Timbro giovanile con una potenza vocale elevata che si fa sentire anche nei mix più densi.
- **Baritono maschile**: voce di petto profonda e vellutata con un tono caldo, rilassante e melodioso.
- **Weathered Rocker**: timbro rauco e grintoso che ricorda l'alternative rock degli anni '90. Intensità emotiva grezza con note acute tese.

### Effetti vocali non lirici

Puoi anche richiedere dialoghi parlati, tagli vocali ed effetti di campionamento:

- Una voce di trasmissione radiofonica vintage introduce la canzone prima che inizi la base
- Una voce sussurra poco prima del drop, seguita da sintetizzatori carichi di energia
- Loop di campioni vocali tagliati e con intonazione modificata come elemento ritmico strumentale

## Parametri musicali

Perfeziona il prompt con le proprietà musicali standard:

- **Tempo (BPM)**: imposta il tempo direttamente (ad es. `120 BPM`, `slow tempo around 72 BPM`, `fast 160 BPM`).
- **Tonalità e scala**: specifica la tonalità e la scala di base (ad es. `in G major`, `in D minor`, `in C pentatonic`).
- **Stato d'animo e atmosfera**: utilizza aggettivi emotivi descrittivi:
  `Ambient, Bright, Chill, Dark, Dreamy, Emotional, Ethereal, Euphoric, Funky, Groovy, Melancholic, Nostalgic, Ominous, Psychedelic, Relaxed, Soulful, Triumphant, Upbeat, Whimsical`

## Prompt di Lyria RealTime

Lyria RealTime utilizza **prompt ponderati** anziché una singola stringa di prompt monolitica. In questo modo puoi combinare dinamicamente più influenze musicali e controllare la musica in modo continuo tramite una connessione WebSocket.

### Struttura del prompt ponderato

Ogni prompt ponderato è composto da una frase di testo descrittiva e da un peso in rappresentazione in virgola mobile:

```
prompts = [
    types.WeightedPrompt(text="minimal techno", weight=1.0),
    types.WeightedPrompt(text="deep sub bass", weight=0.6),
    types.WeightedPrompt(text="shimmering hi-hats", weight=0.4),
]
```

### Strategie di sterzata in tempo reale

- **Combinazione di generi**: combina stili distinti assegnando pesi bilanciati:
  - `ambient synth pads (weight: 0.8)` + `lo-fi hip-hop drums (weight: 0.6)`
  - `flamenco guitar (weight: 0.7)` + `deep house groove (weight: 0.5)`
- **Transizioni dinamiche**: per una transizione musicale fluida, regola i pesi dei prompt nel tempo:
  1. Inizia con `chill jazz piano (weight: 1.0)`.
  2. Aggiungi gradualmente `electronic breakbeat (weight: 0.3)`.
  3. Aumenta `electronic breakbeat` fino a `0.8` e riduci `chill jazz piano` fino a `0.3`.
- **Elementi a livelli**: mantieni separati i tag degli strumenti e dell'umore in modo da poterli regolare in modo indipendente:
  - Prompt 1: `bossa nova guitar (weight: 0.9)`
  - Prompt 2: `warm acoustic bass (weight: 0.7)`
  - Prompt 3: `subtle vinyl crackle (weight: 0.3)`

## Prompt di esempio

### Esempi di Lyria 3.5

- **Lo-Fi Study Beat**:
  `none
  A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes piano chords, a relaxed boom-bap drum groove at 82 BPM, and a warm upright bassline. Instrumental only.`
- **Pop Anthem**:
  `none
  An upbeat, feel-good indie-pop song in G major at 122 BPM. Bright acoustic guitar strumming, driving kick drum, handclaps, and warm female vocal harmonies. The lyrics describe an unforgettable summer road trip with friends.`
- **Cinematic Cyberpunk**:
  `none
  Dark, cinematic cyberpunk synthwave at 110 BPM in D minor. Heavy distorted bass, ominous arpeggiated analog synthesizers, distant metallic percussion, and an ethereal female vocalise swelling during the climax.`

### Set di sterzo Lyria RealTime

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

## Passaggi successivi

- [Genera musica con Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=it): genera brani completi e clip di 30 secondi utilizzando l'API Interactions.
- [Generazione di musica in tempo reale con Lyria RealTime](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=it): crea applicazioni di streaming musicale interattive in tempo reale tramite WebSockets.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-18 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-18 UTC."],[],[]]
