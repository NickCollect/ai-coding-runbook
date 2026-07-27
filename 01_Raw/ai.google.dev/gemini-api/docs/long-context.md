---
source_url: https://ai.google.dev/gemini-api/docs/long-context?hl=it
fetched_at: 2026-07-27T04:39:52.716260+00:00
title: "Contesto lungo \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Contesto lungo

Molti modelli Gemini sono dotati di finestre contestuali di grandi dimensioni, con 1 milione o più token.
Storicamente, i modelli linguistici di grandi dimensioni (LLM) erano notevolmente limitati dalla quantità di testo (o token) che poteva essere passata al modello contemporaneamente.
La finestra contestuale lunga di Gemini sblocca molti nuovi casi d'uso e paradigmi per gli sviluppatori.

Il codice che utilizzi già per casi come la [generazione](https://ai.google.dev/gemini-api/docs/text-generation?hl=it) di
testo
o gli [input](https://ai.google.dev/gemini-api/docs/vision?hl=it)
multimodali
funzionerà senza modifiche con il contesto lungo.

Questo documento fornisce una panoramica di ciò che puoi ottenere utilizzando modelli con finestre contestuali di 1 milione o più token. La pagina fornisce una breve panoramica di una finestra contestuale ed esplora il modo in cui gli sviluppatori dovrebbero pensare al contesto lungo, a vari casi d'uso reali per il contesto lungo e ai modi per ottimizzare l'utilizzo del contesto lungo.

Per le dimensioni della finestra contestuale di modelli specifici, consulta la
[pagina Modelli](https://ai.google.dev/gemini-api/docs/models?hl=it).

## Cos'è una finestra contestuale?

Il modo di base in cui utilizzi i modelli Gemini consiste nel passare informazioni (contesto) al modello, che successivamente genererà una risposta. Una finestra contestuale è analoga alla memoria a breve termine. La quantità di informazioni che può essere memorizzata nella memoria a breve termine di una persona è limitata, così come per i modelli generativi.

Puoi scoprire di più sul funzionamento dei modelli nel nostro [documento sui modelli generativi
guide](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=it#under-the-hood).

## Inizia a utilizzare il contesto lungo

Le versioni precedenti dei modelli generativi erano in grado di elaborare solo 8000 token alla volta. I modelli più recenti hanno spinto questo limite accettando 32.000 o persino 128.000 token. Gemini è il primo modello in grado di accettare 1 milione di token.

In pratica, 1 milione di token sarebbero:

- 50.000 righe di codice (con gli 80 caratteri standard per riga)
- Tutti gli SMS che hai inviato negli ultimi 5 anni
- 8 romanzi in inglese di lunghezza media
- Trascrizioni di oltre 200 puntate di podcast di lunghezza media

Le finestre contestuali più limitate comuni in molti altri modelli spesso richiedono strategie come l'eliminazione arbitraria di messaggi precedenti, il riepilogo dei contenuti, l'utilizzo di RAG con database vettoriali o il filtraggio dei prompt per salvare i token.

Sebbene queste tecniche rimangano preziose in scenari specifici, la finestra contestuale estesa di Gemini invita a un approccio più diretto: fornire in anticipo tutte le informazioni pertinenti. Poiché i modelli Gemini sono stati creati appositamente con funzionalità di contesto massicce, dimostrano un potente apprendimento in-context. Ad
esempio, utilizzando solo materiali didattici in-context (una grammatica di riferimento di 500 pagine,
un dizionario e circa 400 frasi parallele), Gemini
[ha imparato a tradurre](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf)
dall'inglese al kalamang, una lingua papuana con
meno di 200 parlanti, con una qualità simile a quella di uno studente umano che utilizza gli stessi
materiali. Questo illustra il cambio di paradigma reso possibile dal contesto lungo di Gemini, che offre nuove possibilità grazie a un solido apprendimento in-context.

## Casi d'uso del contesto lungo

Sebbene il caso d'uso standard per la maggior parte dei modelli generativi sia ancora l'input di testo, la famiglia di modelli Gemini consente un nuovo paradigma di casi d'uso multimodali. Questi modelli possono comprendere in modo nativo testo, video, audio e immagini. Sono
accompagnati dall'[API Gemini che accetta tipi di file multimodali
per
comodità.](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=it)

### Testo in formato lungo

Il testo si è dimostrato il livello di intelligence alla base di gran parte dello slancio intorno agli LLM. Come accennato in precedenza, gran parte della limitazione pratica degli LLM era dovuta al fatto di non avere una finestra contestuale sufficientemente grande per eseguire determinate attività. Ciò ha portato alla rapida adozione della generazione RAG (Retrieval Augmented Generation) e di altre tecniche che forniscono dinamicamente al modello informazioni contestuali pertinenti. Ora, con finestre contestuali sempre più grandi, sono disponibili nuove tecniche che sbloccano nuovi casi d'uso.

Alcuni casi d'uso emergenti e standard per il contesto lungo basato su testo includono:

- Riassunto di grandi corpus di testo
  - Le opzioni di riepilogo precedenti con modelli di contesto più piccoli richiederebbero una finestra scorrevole o un'altra tecnica per mantenere lo stato delle sezioni precedenti man mano che nuovi token vengono passati al modello
- Domande e risposte
  - Storicamente, ciò era possibile solo con RAG, data la quantità limitata di contesto e il richiamo fattuale dei modelli era basso
- Workflow agentici
  - Il testo è alla base del modo in cui gli agenti mantengono lo stato di ciò che hanno fatto e di ciò che devono fare; non avere informazioni sufficienti sul mondo e sull'obiettivo dell'agente è una limitazione dell'affidabilità degli agenti

[L'apprendimento in-context many-shot](https://arxiv.org/pdf/2404.11018) è una delle
funzionalità più esclusive sbloccate dai modelli di contesto lungo. La ricerca ha dimostrato che l'adozione del paradigma di esempio comune "single shot" o "multi-shot", in cui al modello vengono presentati uno o pochi esempi di un'attività, e il suo aumento a centinaia, migliaia o persino centinaia di migliaia di esempi, può portare a nuove funzionalità del modello. È stato inoltre dimostrato che questo approccio many-shot ha un rendimento simile a quello dei modelli ottimizzati per un'attività specifica. Per i casi d'uso in cui il rendimento di un modello Gemini non è ancora sufficiente per un lancio in produzione, puoi provare l'approccio many-shot. Come potresti esplorare più avanti nella sezione sull'ottimizzazione del contesto lungo, la memorizzazione nella cache del contesto rende questo tipo di workload con token di input elevati molto più fattibile dal punto di vista economico e persino con una latenza inferiore in alcuni casi.

### Video in formato lungo

L'utilità dei contenuti video è stata a lungo limitata dalla mancanza di accessibilità del mezzo stesso. Era difficile sfogliare i contenuti, le trascrizioni spesso non riuscivano a cogliere le sfumature di un video e la maggior parte degli strumenti non elabora immagini, testo e audio insieme. Con Gemini, le funzionalità di testo in contesto lungo si traducono nella capacità di ragionare e rispondere a domande su input multimodali con un rendimento costante.

Alcuni casi d'uso emergenti e standard per il contesto lungo dei video includono:

- Domande e risposte sui video
- Memoria video, come mostrato con [il progetto Astra di Google](https://deepmind.google/technologies/gemini/project-astra/?hl=it)
- Sottotitolaggio video
- Sistemi di consigli sui video, arricchendo i metadati esistenti con una nuova comprensione multimodale
- Personalizzazione dei video, esaminando un corpus di dati e i metadati video associati e poi rimuovendo le parti dei video non pertinenti per lo spettatore
- Moderazione dei contenuti video
- Elaborazione video in tempo reale

Quando lavori con i video, è importante considerare come i [video vengono
elaborati in token](https://ai.google.dev/gemini-api/docs/tokens?hl=it#media-token), il che influisce sulla
fatturazione e sui limiti di utilizzo. Puoi scoprire di più sui prompt con i file video in
la [guida ai prompt](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=it#prompting-with-videos).

### Audio in formato lungo

I modelli Gemini sono stati i primi modelli linguistici di grandi dimensioni nativamente multimodali in grado di comprendere l'audio. Storicamente, il workflow tipico degli sviluppatori prevedeva l'unione di più modelli specifici del dominio, come un modello di conversione della voce in testo e un modello da testo a testo, per elaborare l'audio. Ciò ha comportato una latenza aggiuntiva richiesta dall'esecuzione di più richieste di andata e ritorno e una riduzione del rendimento solitamente attribuita alle architetture disconnesse della configurazione di più modelli.

Alcuni casi d'uso emergenti e standard per il contesto audio includono:

- Trascrizione e traduzione in tempo reale
- Domande e risposte su podcast / video
- Trascrizione e riepilogo delle riunioni
- Assistenti vocali

Puoi scoprire di più sui prompt con i file audio nella [guida
ai prompt](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=it#prompting-with-videos).

## Ottimizzazioni del contesto lungo

L'ottimizzazione principale quando lavori con il contesto lungo e i modelli Gemini
è l'utilizzo della memorizzazione nella cache del [contesto](https://ai.google.dev/gemini-api/docs/caching?hl=it). Oltre alla precedente impossibilità di elaborare molti token in una singola richiesta, l'altro vincolo principale era il costo. Se hai un'app "Chatta con i tuoi dati" in cui un utente carica 10 PDF, un video e alcuni documenti di lavoro, in passato avresti dovuto lavorare con uno strumento/framework di generazione RAG (Retrieval Augmented Generation) più complesso per elaborare queste richieste e pagare un importo significativo per i token spostati nella finestra contestuale. Ora puoi memorizzare nella cache i file caricati dall'utente e pagare per archiviarli su base oraria. Il costo di input / output per richiesta con Gemini Flash, ad esempio, è circa 4 volte inferiore al costo di input / output standard, quindi se l'utente chatta abbastanza con i suoi dati, diventa un enorme risparmio sui costi per te come sviluppatore.

## Limitazioni del contesto lungo

In varie sezioni di questa guida, abbiamo parlato di come i modelli Gemini raggiungono un rendimento elevato in varie valutazioni di recupero di un ago in un pagliaio. Questi test considerano la configurazione più semplice, in cui hai un singolo ago che stai cercando. Nei casi in cui potresti avere più "aghi" o informazioni specifiche che stai cercando, il modello non funziona con la stessa precisione. Il rendimento può variare notevolmente a seconda del contesto. È importante tenerlo presente perché esiste un compromesso intrinseco tra il recupero delle informazioni corrette e il costo. Puoi ottenere circa il 99% su una singola query, ma devi pagare il costo del token di input ogni volta che invii la query. Quindi, per recuperare 100 informazioni, se hai bisogno di un rendimento del 99%, probabilmente dovrai inviare 100 richieste. Questo è un buon esempio di dove la memorizzazione nella cache del contesto può ridurre significativamente il costo associato all'utilizzo dei modelli Gemini mantenendo un rendimento elevato.

## Domande frequenti

### Qual è il posto migliore per inserire la query nella finestra contestuale?

Nella maggior parte dei casi, soprattutto se il contesto totale è lungo, il rendimento del modello sarà migliore se inserisci la query / domanda alla fine del prompt (dopo tutto l'altro contesto).

### Perdo il rendimento del modello quando aggiungo altri token a una query?

In genere, se non hai bisogno che i token vengano passati al modello, è meglio evitarlo. Tuttavia, se hai un blocco di token di grandi dimensioni con alcune informazioni e vuoi porre domande su queste informazioni, il modello è in grado di estrarre queste informazioni (fino al 99% di accuratezza in molti casi).

### Come posso ridurre i costi con le query di contesto lungo?

[Se hai un insieme simile di token / contesto che vuoi riutilizzare più volte, la memorizzazione nella cache del contesto può aiutarti a ridurre i costi associati alla richiesta di informazioni su queste informazioni.](https://ai.google.dev/gemini-api/docs/caching?hl=it)

### La finestra contestuale influisce sulla latenza del modello?

Esiste una quantità fissa di latenza in qualsiasi richiesta, indipendentemente dalle dimensioni, ma in genere le query più lunghe avranno una latenza maggiore (tempo al primo token).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-06-22 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-06-22 UTC."],[],[]]
