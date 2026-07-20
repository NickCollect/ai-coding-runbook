---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=it
fetched_at: 2026-07-20T04:47:34.565900+00:00
title: "Registrazione e condivisione dei dati \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Registrazione e condivisione dei dati

Questa pagina descrive l'archiviazione e la gestione dei [log dell'API Gemini](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=it), ovvero i dati API di proprietà degli sviluppatori provenienti da chiamate API Gemini supportate per i progetti con la fatturazione abilitata. I log
comprendono l'intero processo, dalla richiesta di un utente alla risposta del modello.
Questi log, privati per il tuo progetto Google Cloud, sono separati da tutti i log conservati esclusivamente per scopi di [monitoraggio degli abusi](https://ai.google.dev/gemini-api/docs/usage-policies?hl=it).

## Dati che possono essere condivisi

In qualità di proprietario del progetto, puoi scegliere di attivare il logging delle chiamate all'API Gemini,
per uso personale o per feedback e condivisione con Google per aiutarci a migliorare continuamente
i nostri modelli.

Se la registrazione è attivata, puoi aiutarci a creare sistemi di AI che continuino a essere
utili per gli sviluppatori in vari campi e casi d'uso scegliendo di
contribuire con i seguenti dati per il miglioramento del prodotto e l'addestramento del modello:

- **Set di dati**:utilizza l'interfaccia Log e set di dati di Google AI Studio per
  scegliere i log (richieste, risposte, metadati e così via) di interesse dalle
  chiamate API Gemini supportate; i log vengono forniti tramite l'inclusione nei set di dati, con la
  possibilità di disattivare l'inclusione durante la creazione del set di dati.
- **Feedback**:durante la revisione dei log, puoi fornire un feedback, incluse le valutazioni Mi piace e Non mi piace e qualsiasi commento scritto.

Quando condividi un set di dati con Google, i log in quel set di dati, incluse le richieste e le risposte, verranno elaborati in conformità ai nostri [Termini](https://developers.google.com/terms?hl=it) per i "[Servizi non a pagamento](https://ai.google.dev/gemini-api/terms?hl=it#data-use-unpaid)", il che significa che il set di dati potrebbe essere utilizzato per sviluppare e migliorare i prodotti, i servizi e le tecnologie di machine learning di Google, inclusi il miglioramento e l'addestramento dei nostri modelli. **Non includere informazioni personali, sensibili o riservate.**

## Come utilizziamo i tuoi dati

I log vengono conservati per un periodo massimo predefinito di 55 giorni. Trascorso questo periodo,
i log vengono contrassegnati automaticamente per l'eliminazione. La finestra di conservazione dello spazio di archiviazione per un progetto può essere aggiornata in AI Studio per contrassegnare automaticamente i log per l'eliminazione dopo 7, 14, 28 o 55 giorni.

È possibile creare [dataset](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=it) per conservare i log di
interesse oltre il periodo di conservazione impostato per i casi d'uso downstream e
il contributo facoltativo ai miglioramenti del modello. I log archiviati nei set di dati non
hanno periodi di conservazione impostati.

Per impostazione predefinita, poiché la registrazione è disponibile solo per i progetti con fatturazione abilitata,
i prompt e le risposte all'interno dei log non vengono utilizzati per il miglioramento o lo
sviluppo dei prodotti, in conformità con i nostri [Termini](https://developers.google.com/terms?hl=it)
sull'utilizzo dei dati.

Se scegli di condividere i set di dati dei tuoi log con Google, questi verranno
utilizzati come dati dimostrativi reali per comprendere meglio la diversità di
domini e contesti in cui vengono utilizzati i sistemi e le applicazioni di AI. Questi dati potrebbero essere
utilizzati per migliorare la qualità del modello e informare l'addestramento e la valutazione di futuri
modelli e servizi. Questi dati vengono trattati in conformità ai nostri termini di utilizzo dei dati per i [Servizi non a pagamento](https://ai.google.dev/gemini-api/terms?hl=it#data-use-unpaid).

Di conseguenza, i revisori umani potrebbero leggere, annotare ed elaborare gli input e gli output delle API che condividi. Prima che i dati vengano utilizzati per il miglioramento del modello, Google adotta misure
per proteggere la privacy degli utenti nell'ambito di questa procedura. Ciò include la disconnessione di questi dati dal tuo Account Google, dalla chiave API e dal progetto Cloud prima che i revisori li vedano o li annotino.

## Autorizzazioni dati

Se accetti di contribuire con i dati dell'API, confermi di disporre delle autorizzazioni necessarie per consentire a Google di trattare e utilizzare i dati come descritto in questa documentazione. **Non contribuire con log contenenti informazioni sensibili, riservate o proprietarie ottenute tramite il servizio a pagamento**.
La licenza che concedi a Google ai sensi della sezione "[Invio di contenuti](https://developers.google.com/terms?hl=it#b_submission_of_content)"
dei Termini delle API si estende anche, nella misura richiesta dalla legge
vigente per il nostro utilizzo, a qualsiasi contenuto (ad es. prompt, incluse istruzioni
di sistema associate, contenuti memorizzati nella cache e file come immagini, video o documenti)
che invii ai Servizi e a qualsiasi risposta generata.

## Condivisione dei dati e feedback

Puoi aiutarci a far progredire la ricerca sull'AI, l'API Gemini e Google AI Studio attivando la condivisione dei tuoi dati come esempi, consentendoci di migliorare continuamente i nostri modelli in vari contesti e di creare sistemi di AI che continuino a essere utili agli sviluppatori in vari campi e casi d'uso.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-09 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-09 UTC."],[],[]]
