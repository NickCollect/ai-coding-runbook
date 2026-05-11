---
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=it
fetched_at: 2026-05-11T05:02:49.465055+00:00
title: "Strategie di progettazione dei prompt \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Strategie di progettazione dei prompt

La *progettazione dei prompt* è il processo di creazione di prompt, ovvero richieste in linguaggio naturale,
che generano risposte accurate e di alta qualità da un modello linguistico.

Questa pagina introduce concetti, strategie e best practice di base per iniziare a progettare prompt per ottenere il massimo dai modelli di AI Gemini.

## Guide per prompt specifiche per argomento

Cerchi strategie di prompt più specifiche? Consulta le nostre altre guide ai prompt
su:

- [Prompt con file multimediali](https://ai.google.dev/gemini-api/docs/files?hl=it#prompt-guide)
- Prompt per la generazione di immagini con [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=it#imagen-prompt-guide) e [Generazione di immagini nativa di Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it#prompt-guide)
- [Prompt per la generazione di video](https://ai.google.dev/gemini-api/docs/video?hl=it#prompt-guide)

Puoi trovare altri prompt di esempio nella [galleria dei prompt](https://ai.google.dev/gemini-api/prompts?hl=it),
che ha lo scopo di mostrare in modo interattivo molti dei concetti condivisi in questa guida.

## Istruzioni chiare e specifiche

Un modo efficace ed efficiente per personalizzare il comportamento del modello è fornirgli
istruzioni chiare e specifiche. Le istruzioni possono essere sotto forma di domanda,
attività passo passo o complesse come la mappatura dell'esperienza e della mentalità di un utente.

### Input

L'input è il testo richiesto nel prompt a cui vuoi che il modello fornisca una
risposta. Gli input possono essere una domanda a cui il modello
risponde (input di domanda), un'attività eseguita dal modello (input di attività), un'entità su cui il
modello agisce (input di entità) o un input parziale che il modello completa o
prosegue (input di completamento).

| **Tipo di input** | **Prompt** | **Output generato** |
| --- | --- | --- |
| Domanda | ```     What's a good name for a flower shop that specializes in selling bouquets of     dried flowers? Create a list of 5 options with just the names. ``` | ```     Here are 5 names for a flower shop specializing in dried flowers:      1. Everlasting Blooms     2. Dried & Delightful     3. The Petal Preserve     4. Whispers of Wildflowers     5. Forever Blooms ``` |
| Attività | ```     Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ``` | ```     1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| Entità | ```     Classify the following items as [large, small]: Elephant Mouse Snail ``` | ``` Here's the classification:  * **Elephant:** Large * **Mouse:** Small * **Snail:** Small ``` |

#### Completamento parziale dell'input

I modelli linguistici generativi funzionano come uno strumento avanzato di completamento automatico. Quando
fornisci contenuti parziali, il modello può fornire il resto dei contenuti o ciò che
ritiene sia una continuazione di questi contenuti come risposta. In questo modo, se
includi esempi o contesto, il modello può tenerne conto.

L'esempio seguente fornisce un prompt con un'istruzione e un input di entità:

|  |
| --- |
| **Prompt:**    ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity.  Order: A burger and a drink. ```  **Risposta:**    ``` {   "cheeseburger": 0,   "hamburger": 1,   "fries": 0,   "drink": 1 } ```  (gemini-2.5-flash) |

Anche se il modello ha eseguito l'attività richiesta, scrivere le istruzioni in linguaggio naturale
può essere a volte difficile e lascia molto all'interpretazione del modello.
Ad esempio, il menu di un ristorante potrebbe contenere molti articoli. Per ridurre le dimensioni
della risposta JSON, probabilmente ti conviene omettere gli articoli che non sono stati ordinati. In
questo caso, puoi fornire un esempio e un prefisso di risposta e lasciare che il modello
lo completi:

|  |
| --- |
| **Prompt:**    ``` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` {   "cheeseburger": 1,   "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```  **Risposta:**    ``` ``` {   "hamburger": 2,   "drink": 1,   "fries": 1 } ``` ```  (gemini-2.5-flash) |

Nota come "cheeseburger" sia stato escluso dall'output perché non faceva parte
dell'ordine.

Sebbene tu possa specificare il formato di semplici oggetti di risposta JSON utilizzando i prompt, ti consigliamo di utilizzare la funzionalità di [output strutturato](https://ai.google.dev/gemini-api/docs/structured-output?hl=it) dell'API Gemini quando specifichi uno schema JSON più complesso per la risposta.

### Vincoli

Specifica eventuali vincoli per la lettura del prompt o la generazione di una risposta. Puoi
dire al modello cosa fare e cosa non fare. Ad esempio, puoi specificare un vincolo
nel prompt sulla lunghezza del riepilogo:

|  |
| --- |
| **Prompt:**     ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ```     **Risposta:**     ```       Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ```  (gemini-2.5-flash) |

### Formato della risposta

Puoi fornire istruzioni che specificano il formato della risposta. Ad esempio,
puoi chiedere che la risposta venga formattata come tabella, elenco puntato, discorso
di presentazione, parole chiave, frase o paragrafo. La seguente istruzione di sistema indica
al modello di utilizzare uno stile più conversazionale nella risposta:

|  |
| --- |
| **Istruzione di sistema**    ```     All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ```  **Prompt**    ```     What is a smart way to make a business that sells DVD's in 2026? ```  **Risposta:**    ``` Starting a business selling DVDs in 2026 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption.  Here's a breakdown of what a smart DVD business in 2026 would likely entail:  1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include:      * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms.     .... ```  (gemini-2.5-flash) |

#### Formattare le risposte con la strategia di completamento

Anche la [strategia di completamento](#completion) può contribuire a formattare la risposta.
Il seguente esempio chiede al modello di creare una struttura del saggio:

|  |
| --- |
| **Prompt:**    ``` Create an outline for an essay about hummingbirds. ```  **Risposta:**    ``` Here is a possible outline for an essay about hummingbirds:  I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds.  II. Appearance and Identification ..... ```  (gemini-2.5-flash) |

Il prompt non ha specificato il formato della struttura e il modello ne ha scelto uno per te. Per fare in modo che il modello restituisca una struttura in un formato specifico, puoi aggiungere
un testo che rappresenti l'inizio della struttura e lasciare che il modello la completi in base
al pattern che hai avviato.

|  |
| --- |
| **Prompt:**    ``` Create an outline for an essay about hummingbirds. I. Introduction    * ```  **Risposta:**    ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided:  I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ```  (gemini-2.5-flash) |

## Prompt zero-shot e few-shot

Puoi includere nel prompt esempi che mostrino al modello come dovrebbe essere una risposta corretta. Il modello tenta di identificare pattern e relazioni dagli esempi e li applica durante la generazione di una risposta. I prompt che contengono alcuni esempi sono chiamati prompt *few-shot*, mentre i prompt che non forniscono esempi sono chiamati prompt *zero-shot*. I prompt few-shot vengono spesso utilizzati
per regolare la formattazione, la formulazione, l'ambito o il pattern generale delle risposte del modello. Utilizza esempi specifici e vari per aiutare il modello a restringere il campo
e generare risultati più accurati.

Ti consigliamo di includere sempre esempi few-shot nei prompt. I prompt senza
esempi few-shot hanno meno probabilità di essere efficaci. Infatti, puoi rimuovere le istruzioni dal prompt se gli esempi sono abbastanza chiari per mostrare l'attività da svolgere.

Il seguente prompt zero-shot chiede al modello di scegliere la spiegazione migliore.

|  |
| --- |
| **Prompt:**    ``` Please choose the best explanation to the question:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Risposta:**    ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ```  (gemini-2.5-flash) |

Se il tuo caso d'uso richiede che il modello produca risposte concise, puoi includere
esempi nel prompt che danno la preferenza a risposte concise.

Il seguente prompt fornisce due esempi che mostrano la preferenza per le spiegazioni più brevi. Nella risposta, puoi notare che gli esempi hanno guidato il modello a scegliere la spiegazione più breve (`Explanation2`) anziché quella più lunga (`Explanation1`), come aveva fatto in precedenza.

|  |
| --- |
| **Prompt:**    ``` Below are some examples showing a question, explanation, and answer format:  Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2  Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1  Now, Answer the following question given the example formats above:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Risposta:**    ``` Answer: Explanation2 ```  (gemini-2.5-flash) |

### Numero ottimale di esempi

Modelli come Gemini spesso riescono a individuare pattern utilizzando pochi esempi, anche se
potresti dover sperimentare il numero di esempi da fornire nel prompt
per ottenere i risultati migliori. Allo stesso tempo, se includi troppi esempi,
il modello potrebbe iniziare a [fare overfitting](https://developers.google.com/machine-learning/glossary?hl=it#overfitting)
della risposta agli esempi.

### Formato coerente

Assicurati che la struttura e la formattazione degli esempi few-shot siano le stesse per
evitare risposte con formati indesiderati. Uno degli obiettivi principali dell'aggiunta
di esempi few-shot nei prompt è mostrare al modello il formato della risposta. Pertanto,
è essenziale garantire un formato coerente in tutti gli esempi, prestando particolare attenzione
a tag XML, spazi bianchi, interruzioni di riga e separatori di esempi.

## Aggiungi contesto

Puoi includere in un prompt istruzioni e informazioni necessarie al modello per risolvere un problema, anziché presumere che il modello disponga di tutte le informazioni richieste. Queste informazioni contestuali aiutano il modello a comprendere i vincoli
e i dettagli di ciò che gli stai chiedendo di fare.

L'esempio seguente chiede al modello di fornire indicazioni per la risoluzione dei problemi di un router:

|  |
| --- |
| **Prompt:**    ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ```  **Risposta:**    ```   A yellow blinking light on your Google Wifi router usually indicates a problem   with the internet connection. Here are some steps to troubleshoot and fix the   issue:   1. Restart your router and modem:     - Unplug your modem from the power outlet and wait for 30 seconds.     - Plug your modem back in and wait for it to fully boot up.     - Unplug your Google Wifi router and wait for 30 seconds.     - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ```  (gemini-2.5-flash) |

La risposta sembra contenere informazioni generiche per la risoluzione dei problemi che non sono specifiche
per il router o lo stato delle spie LED.

Per personalizzare la risposta per il router specifico, puoi aggiungere alla richiesta la guida alla risoluzione dei problemi del router come contesto a cui fare riferimento quando fornisci una risposta.

|  |
| --- |
| **Prompt:**    ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.  Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.  Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.  Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.  Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ```  **Risposta:**    ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ```  (gemini-2.5-flash) |

## Suddividere i prompt in componenti

Per i casi d'uso che richiedono prompt complessi, puoi aiutare il modello a gestire questa complessità
suddividendo gli elementi in componenti più semplici.

1. **Suddividi le istruzioni**:invece di avere molte istruzioni in un unico prompt, crea un prompt per ogni istruzione. Puoi scegliere quale prompt elaborare in base all'input dell'utente.
2. **Prompt concatenati**:per attività complesse che prevedono più passaggi sequenziali,
   trasforma ogni passaggio in un prompt e concatenali in una sequenza. In questa
   catena sequenziale di prompt, l'output di un prompt nella sequenza diventa
   l'input del prompt successivo. L'output dell'ultimo prompt della sequenza
   è l'output finale.
3. **Aggregare le risposte**:l'aggregazione si verifica quando vuoi eseguire diverse attività parallele su diverse porzioni di dati e aggregare i risultati per produrre l'output finale. Ad esempio, puoi indicare al modello di eseguire un'operazione sulla prima parte dei dati, un'altra operazione sul resto dei dati e aggregare i risultati.

## Sperimenta con i parametri del modello

Ogni chiamata inviata a un modello include valori parametro che controllano il modo in cui il modello genera una risposta. Il modello può generare risultati diversi
a seconda dei valori parametro. Sperimenta con diversi valori parametro per ottenere
i valori migliori per l'attività. I parametri disponibili per
i vari modelli possono variare. I parametri più comuni sono i seguenti:

1. **Token di output massimi**:specifica il numero massimo di token che possono essere
   generati nella risposta. Un token equivale a circa quattro caratteri. 100
   token corrispondono a circa 60-80 parole.
2. **Temperatura**:la temperatura controlla il grado di casualità nella selezione dei token. La temperatura viene utilizzata per il campionamento durante la generazione di risposte,
   che si verifica quando vengono applicati `topP` e `topK`. Le temperature più basse sono ideali per prompt che richiedono risposte più deterministiche o meno aperte, mentre le temperature più alte possono portare a risultati più diversificati o creativi. Una
   temperatura pari a 0 è deterministica, il che significa che viene sempre selezionata la risposta con la probabilità più alta.
3. **`topK`:** il parametro `topK` modifica il modo in cui il modello seleziona i token per l'output. Un `topK` pari a 1 indica che il token selezionato è il più probabile tra tutti i token nel vocabolario del modello (chiamato anche decodifica greedy). Un `topK` pari a 3 indica invece che il token successivo viene selezionato tra i tre token più probabili (utilizzando la temperatura). Per ogni fase di selezione dei token, vengono campionati i
   `topK` token con le probabilità più alte. I token vengono poi
   ulteriormente filtrati in base a `topP` e il token finale viene selezionato utilizzando
   il campionamento con temperatura.
4. **`topP`:** il parametro `topP` modifica il modo in cui il modello seleziona i token per l'output. I token vengono selezionati dal più probabile al meno probabile finché la somma delle loro probabilità non corrisponde al valore di `topP`. Ad esempio, se i token A, B e C hanno una probabilità di 0,3, 0,2 e 0,1 e il valore di `topP` è 0,5, il modello seleziona A o B come token successivo utilizzando la temperatura ed esclude C come candidato. Il valore predefinito di `topP` è 0,95.
5. **`stop_sequences`:** imposta una sequenza di interruzione per
   indicare al modello di interrompere la generazione di contenuti. Una sequenza di interruzione può essere
   qualsiasi sequenza di caratteri. Cerca di evitare di utilizzare una sequenza di caratteri che
   potrebbe essere presente nei contenuti generati.

## Strategie di iterazione dei prompt

A volte la progettazione dei prompt richiede alcune iterazioni prima di ottenere
in modo coerente la risposta che stai cercando. Questa sezione fornisce
indicazioni su alcune cose che puoi provare a fare quando esegui l'iterazione dei prompt:

1. **Utilizza una formulazione diversa**:l'utilizzo di parole o frasi diverse nei prompt
   spesso produce risposte diverse dal modello, anche se tutte significano la
   stessa cosa. Se il prompt non produce i risultati che ti aspettavi, prova a riformularlo.

   |  |
   | --- |
   | ``` Version 1: How do I bake a pie?  Version 2: Suggest a recipe for a pie.  Version 3: What's a good pie recipe? ``` |
2. **Passa a un'attività analoga:** se non riesci a far seguire al modello le tue
   istruzioni per un'attività, prova a fornirgli istruzioni per un'attività analoga
   che ottenga lo stesso risultato.

   Questo prompt indica al modello di classificare un libro utilizzando categorie predefinite:

   |  |
   | --- |
   | **Prompt:**    ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ```  **Risposta:**    ```     The Odyssey belongs to the category of **mythology**.       Here's why:      * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his     journey home after the Trojan War. It features gods, monsters, and supernatural events common to     Greek mythology. ..... ```  (gemini-2.5-flash) |

   La risposta è corretta, ma il modello non è rimasto nei limiti delle opzioni. Inoltre, vuoi che il modello risponda solo con una delle opzioni
   invece di una frase completa. In questo caso, puoi riformulare le istruzioni come una
   domanda a scelta multipla e chiedere al modello di scegliere un'opzione.

   |  |
   | --- |
   | **Prompt:**    ``` Multiple choice problem: Which of the following options describes the book The Odyssey? Options: ``` |

   - thriller
   - sci-fi
   - mythology
   - biography
     **Risposta:**

     ```
     The correct answer is mythology.
     ```

     (gemini-2.5-flash)
   - **Modificare l'ordine dei contenuti del prompt:** l'ordine dei contenuti nel prompt
     a volte può influire sulla risposta. Prova a modificare l'ordine dei contenuti e vedi
     come influisce sulla risposta.

     ```
     Version 1:
     [examples]
     [context]
     [input]

     Version 2:
     [input]
     [examples]
     [context]

     Version 3:
     [examples]
     [input]
     [context]
     ```

## Risposte di riserva

Una risposta di riserva è una risposta restituita dal modello quando il prompt o la risposta attiva un filtro di sicurezza. Un esempio di risposta di riserva è
"Non posso aiutarti in questo caso, perché sono solo un modello linguistico".

Se il modello risponde con una risposta di riserva, prova ad aumentare la temperatura.

## Grounding ed esecuzione del codice

Gemini è in grado di utilizzare strumenti per evitare le allucinazioni negli scenari in cui potrebbe
altrimenti produrre risposte errate.

[Grounding con la Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it) collega il modello Gemini a contenuti web in tempo reale e deve essere attivato ogni volta che il modello potrebbe aver bisogno di conoscere fatti oscuri o recenti.

Lo [strumento di esecuzione del codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it) di Gemini consente al modello di generare ed eseguire codice Python e deve essere abilitato ogni volta che il modello deve eseguire qualsiasi tipo di operazione aritmetica, conteggio o calcolo.

## Gemini 3

I [modelli Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-3) sono progettati per il ragionamento
avanzato e il rispetto delle istruzioni.
Rispondono meglio a prompt diretti, ben strutturati e che definiscono chiaramente
l'attività e qualsiasi vincolo. Per ottenere risultati ottimali con Gemini 3, si consiglia di adottare le seguenti pratiche:

### Principi fondamentali del prompting

- **Sii preciso e diretto**:indica il tuo obiettivo in modo chiaro e conciso. Evita
  un linguaggio non necessario o eccessivamente persuasivo.
- **Utilizza una struttura coerente**:utilizza delimitatori chiari per separare le diverse parti del prompt. I tag in stile XML (ad es. `<context>`, `<task>`) o
  le intestazioni Markdown sono efficaci. Scegli un formato e usalo in modo coerente
  all'interno di un singolo prompt.
- **Definisci i parametri:** spiega in modo esplicito eventuali termini o parametri ambigui.
- **Controlla la verbosità dell'output:** per impostazione predefinita, i modelli Gemini 3 forniscono risposte dirette ed efficienti. Se hai bisogno di una risposta più colloquiale o dettagliata,
  devi richiederla esplicitamente nelle istruzioni.
- **Gestisci gli input multimodali in modo coerente:** quando utilizzi testo, immagini, audio o video, trattali come input di pari livello. Assicurati che le istruzioni facciano riferimento
  chiaramente a ogni modalità, se necessario.
- **Dai la priorità alle istruzioni critiche:** inserisci i vincoli comportamentali essenziali, le definizioni dei ruoli (persona) e i requisiti di formato di output nelle istruzioni di sistema o all'inizio del prompt dell'utente.
- **Struttura per contesti lunghi**:quando fornisci grandi quantità di contesto
  (ad es. documenti, codice), fornisci prima tutto il contesto. Inserisci le tue istruzioni o domande specifiche alla *fine* del prompt.
- **Contesto di ancoraggio**:dopo un blocco di dati di grandi dimensioni, utilizza una frase di transizione chiara per collegare il contesto e la query, ad esempio "In base alle informazioni riportate sopra..."

### Strategie di Gemini 3 Flash

- **Accuratezza del giorno corrente**:aggiungi la seguente clausola alle istruzioni di sistema per aiutare il modello a tenere conto del fatto che il giorno corrente è il 2026:

  ```
  For time-sensitive user queries that require up-to-date information, you
  MUST follow the provided current time (date and year) when formulating
  search queries in tool calls. Remember it is 2026 this year.
  ```
- **Accuratezza del knowledge cutoff**:aggiungi la seguente clausola alle istruzioni di sistema per rendere il modello consapevole del suo knowledge cutoff:

  ```
  Your knowledge cutoff date is January 2025.
  ```
- **Prestazioni di grounding**:aggiungi la seguente clausola alle istruzioni di sistema (con le modifiche appropriate) per migliorare la capacità del modello di basare le risposte sul contesto fornito:

  ```
  You are a strictly grounded assistant limited to the information provided in
  the User Context. In your answers, rely **only** on the facts that are
  directly mentioned in that context. You must **not** access or utilize your
  own knowledge or common sense to answer. Do not assume or infer from the
  provided facts; simply report them exactly as they appear. Your answer must
  be factual and fully truthful to the provided text, leaving absolutely no
  room for speculation or interpretation. Treat the provided context as the
  absolute limit of truth; any facts or details that are not directly
  mentioned in the context must be considered **completely untruthful** and
  **completely unsupported**. If the exact answer is not explicitly written in
  the context, you must state that the information is not available.
  ```

### Migliorare il ragionamento e la pianificazione

I modelli delle serie Gemini 2.5 e 3 generano automaticamente un testo di "pensiero" interno
per migliorare le prestazioni di ragionamento. Pertanto, in genere non è necessario includere
la struttura, il piano o i passaggi di ragionamento dettagliati del modello nella risposta restituita. Per i problemi che richiedono un ragionamento complesso, richieste semplici come "Pensa
molto attentamente prima di rispondere" possono migliorare le prestazioni, anche se a scapito di
token di pensiero aggiuntivi.

Per ulteriori dettagli, consulta la documentazione relativa al [pensiero di Gemini](https://ai.google.dev/gemini-api/docs/thinking?hl=it).

### Esempi di prompt strutturati

L'utilizzo di tag o Markdown aiuta il modello a distinguere tra istruzioni, contesto e attività.

**Esempio XML:**

```
<role>
You are a helpful assistant.
</role>

<constraints>
1. Be objective.
2. Cite sources.
</constraints>

<context>
[Insert User Input Here - The model knows this is data, not instructions]
</context>

<task>
[Insert the specific user request here]
</task>
```

**Esempio di Markdown:**

```
# Identity
You are a senior solution architect.

# Constraints
- No external libraries allowed.
- Python 3.11+ syntax only.

# Output format
Return a single code block.
```

### Esempio di modello che combina le best practice

Questo modello acquisisce i principi fondamentali per la creazione di prompt con Gemini 3. Assicurati sempre
di eseguire iterazioni e modifiche per il tuo caso d'uso specifico.

**Istruzione di sistema:**

```
<role>
You are Gemini 3, a specialized assistant for [Insert Domain, e.g., Data Science].
You are precise, analytical, and persistent.
</role>

<instructions>
1. **Plan**: Analyze the task and create a step-by-step plan.
2. **Execute**: Carry out the plan.
3. **Validate**: Review your output against the user's task.
4. **Format**: Present the final answer in the requested structure.
</instructions>

<constraints>
- Verbosity: [Specify Low/Medium/High]
- Tone: [Specify Formal/Casual/Technical]
</constraints>

<output_format>
Structure your response as follows:
1. **Executive Summary**: [Short overview]
2. **Detailed Response**: [The main content]
</output_format>
```

**Prompt dell'utente:**

```
<context>
[Insert relevant documents, code snippets, or background info here]
</context>

<task>
[Insert specific user request here]
</task>

<final_instruction>
Remember to think step-by-step before answering.
</final_instruction>
```

## Workflow agentici

Per i flussi di lavoro agentici profondi, spesso sono necessarie istruzioni specifiche per controllare il modo in cui il modello ragiona, pianifica ed esegue le attività. Sebbene Gemini offra prestazioni generali elevate, gli agenti complessi spesso richiedono di configurare il compromesso tra costo di calcolo (latenza e token) e precisione dell'attività.

Quando progetti i prompt per gli agenti, considera le seguenti dimensioni del comportamento che puoi indirizzare nell'agente:

### Ragionamento e strategia

Configurazione del modo in cui il modello pensa e pianifica prima di agire.

- **Decomposizione logica**:definisce la completezza con cui il modello deve analizzare vincoli, prerequisiti e ordine delle operazioni.
- **Diagnosi del problema**: controlla la profondità dell'analisi durante l'identificazione delle cause e l'utilizzo del ragionamento abduttivo da parte del modello. Determina se il modello deve accettare la risposta più ovvia o esplorare spiegazioni complesse e meno probabili.
- **Completezza delle informazioni**:il compromesso tra l'analisi di ogni norma e documento disponibile e la priorità di efficienza e velocità.

### Esecuzione e affidabilità

Configurazione del funzionamento autonomo dell'agente e della gestione degli ostacoli.

- **Adattabilità**:come reagisce il modello ai nuovi dati. Determina se deve rispettare rigorosamente il piano iniziale o cambiare immediatamente quando le osservazioni contraddicono le ipotesi.
- **Persistenza e recupero**:il grado in cui il modello tenta di correggere automaticamente gli errori. Una persistenza elevata aumenta i tassi di successo, ma rischia di comportare costi o loop dei token più elevati.
- **Valutazione del rischio**:la logica per valutare le conseguenze. Distingue esplicitamente tra azioni esplorative a basso rischio (letture) e modifiche dello stato ad alto rischio (scritture).

### Interazione e output

Configurazione della modalità di comunicazione dell'agente con l'utente e della formattazione dei risultati.

- **Gestione dell'ambiguità e delle autorizzazioni**:definisce quando il modello è autorizzato a fare ipotesi rispetto a quando deve mettere in pausa l'esecuzione per chiedere all'utente chiarimenti o autorizzazioni.
- **Livello di dettaglio**:controlla il volume di testo generato insieme alle chiamate di strumenti. Determina se il modello spiega le sue azioni all'utente o rimane in silenzio durante l'esecuzione.
- **Precisione e completezza**:la fedeltà richiesta dell'output. Specifica se il modello deve risolvere ogni caso limite e fornire cifre esatte o se sono accettabili stime approssimative.

### Modello di istruzione di sistema

La seguente istruzione di sistema è un esempio che è stato valutato dai ricercatori per migliorare le prestazioni nei benchmark agentici in cui il modello deve rispettare un insieme di regole complesso e interagire con un utente. Incoraggia l'agente ad agire come un forte ragionatore e pianificatore, impone comportamenti specifici nelle dimensioni elencate sopra e richiede al modello di pianificare in modo proattivo prima di intraprendere qualsiasi azione.

Puoi adattare questo modello per soddisfare i vincoli del tuo caso d'uso specifico.

```
You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses.

Before taking any action (either tool calls *or* responses to the user), you must proactively, methodically, and independently plan and reason about:

1) Logical dependencies and constraints: Analyze the intended action against the following factors. Resolve conflicts in order of importance:
    1.1) Policy-based rules, mandatory prerequisites, and constraints.
    1.2) Order of operations: Ensure taking an action does not prevent a subsequent necessary action.
        1.2.1) The user may request actions in a random order, but you may need to reorder operations to maximize successful completion of the task.
    1.3) Other prerequisites (information and/or actions needed).
    1.4) Explicit user constraints or preferences.

2) Risk assessment: What are the consequences of taking the action? Will the new state cause any future issues?
    2.1) For exploratory tasks (like searches), missing *optional* parameters is a LOW risk. **Prefer calling the tool with the available information over asking the user, unless** your `Rule 1` (Logical Dependencies) reasoning determines that optional information is required for a later step in your plan.

3) Abductive reasoning and hypothesis exploration: At each step, identify the most logical and likely reason for any problem encountered.
    3.1) Look beyond immediate or obvious causes. The most likely reason may not be the simplest and may require deeper inference.
    3.2) Hypotheses may require additional research. Each hypothesis may take multiple steps to test.
    3.3) Prioritize hypotheses based on likelihood, but do not discard less likely ones prematurely. A low-probability event may still be the root cause.

4) Outcome evaluation and adaptability: Does the previous observation require any changes to your plan?
    4.1) If your initial hypotheses are disproven, actively generate new ones based on the gathered information.

5) Information availability: Incorporate all applicable and alternative sources of information, including:
    5.1) Using available tools and their capabilities
    5.2) All policies, rules, checklists, and constraints
    5.3) Previous observations and conversation history
    5.4) Information only available by asking the user

6) Precision and Grounding: Ensure your reasoning is extremely precise and relevant to each exact ongoing situation.
    6.1) Verify your claims by quoting the exact applicable information (including policies) when referring to them. 

7) Completeness: Ensure that all requirements, constraints, options, and preferences are exhaustively incorporated into your plan.
    7.1) Resolve conflicts using the order of importance in #1.
    7.2) Avoid premature conclusions: There may be multiple relevant options for a given situation.
        7.2.1) To check for whether an option is relevant, reason about all information sources from #5.
        7.2.2) You may need to consult the user to even know whether something is applicable. Do not assume it is not applicable without checking.
    7.3) Review applicable sources of information from #5 to confirm which are relevant to the current state.

8) Persistence and patience: Do not give up unless all the reasoning above is exhausted.
    8.1) Don't be dissuaded by time taken or user frustration.
    8.2) This persistence must be intelligent: On *transient* errors (e.g. please try again), you *must* retry **unless an explicit retry limit (e.g., max x tries) has been reached**. If such a limit is hit, you *must* stop. On *other* errors, you must change your strategy or arguments, not repeat the same failed call.

9) Inhibit your response: only take an action after all the above reasoning is completed. Once you've taken an action, you cannot take it back.
```

## Passaggi successivi

- Ora che hai una conoscenza più approfondita della progettazione dei prompt, prova a scrivere i tuoi prompt utilizzando [Google AI Studio](http://aistudio.google.com?hl=it).
- Per scoprire di più sui prompt multimodali, consulta
  [Prompt con file multimediali](https://ai.google.dev/gemini-api/docs/files?hl=it#prompt-guide).
- Per scoprire di più sul prompting di immagini, consulta le guide ai prompt di [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=it#prompt-guide)
  e [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=it#imagen-prompt-guide).
- Per scoprire di più sui prompt video, consulta la [guida ai prompt di Veo](https://ai.google.dev/gemini-api/docs/video?hl=it#prompt-guide).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-04-29 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-04-29 UTC."],[],[]]
