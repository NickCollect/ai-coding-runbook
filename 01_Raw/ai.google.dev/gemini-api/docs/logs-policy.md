---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=it
fetched_at: 2026-09-28T06:19:21.768061+00:00
title: "Registrazione e condivisione dei dati \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Registrazione e condivisione dei dati

Questa pagina descrive l'archiviazione e la gestione dei
[log dell'API Gemini](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=it), che sono dati API di proprietà dello sviluppatore
provenienti da chiamate API Gemini supportate per i progetti con la fatturazione abilitata. I log comprendono l'intero processo, dalla richiesta di un utente alla risposta del modello.
Questi log, che sono privati per il tuo progetto Google Cloud, sono separati da tutti i
log conservati esclusivamente per [scopi di monitoraggio degli abusi](https://ai.google.dev/gemini-api/docs/usage-policies?hl=it).

## Dati che possono essere condivisi

In qualità di proprietario del progetto, puoi scegliere di attivare la registrazione delle chiamate API Gemini per uso personale o per fornire feedback e condividerli con Google per aiutarci a migliorare continuamente i nostri modelli.

Se attivi la registrazione, puoi aiutarci a creare sistemi di AI che continuano a essere utili per gli sviluppatori in vari campi e casi d'uso scegliendo di contribuire con i seguenti dati per i miglioramenti del prodotto e l'addestramento del modello:

- **Set di dati:** utilizza l'interfaccia Log e set di dati di Google AI Studio per scegliere i log (richieste, risposte, metadati e così via) di interesse dalle chiamate API Gemini supportate; i dati vengono forniti tramite l'inclusione nei set di dati, con la possibilità di disattivare questa opzione durante la creazione del set di dati.
- **Feedback:** quando esamini i log, puoi fornire feedback, inclusi i punteggi con i pollici in su e in giù e tutti i commenti scritti che fornisci.

Quando condividi un set di dati con Google, i log in quel set di dati, incluse
richieste e risposte, verranno trattati in conformità con i nostri
[Termini](https://developers.google.com/terms?hl=it) per
"[Servizi non a pagamento](https://ai.google.dev/gemini-api/terms?hl=it#data-use-unpaid),"
il che significa che il set di dati può essere utilizzato per sviluppare e migliorare i
prodotti, i servizi e le tecnologie di machine learning di Google, inclusi il miglioramento e
l'addestramento dei nostri modelli. **Non includere informazioni personali, sensibili o riservate.**

## Come utilizziamo i tuoi dati

I log vengono conservati per un periodo massimo predefinito di 55 giorni. Trascorso questo periodo, i log vengono contrassegnati automaticamente per l'eliminazione. La finestra di conservazione dell'archiviazione per un progetto può essere aggiornata in AI Studio per contrassegnare automaticamente i log per l'eliminazione dopo 7, 14, 28 o 55 giorni.

[È possibile creare](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=it)set di dati per conservare i log di
interesse oltre il periodo di conservazione impostato per i casi d'uso downstream e il
contributo facoltativo ai miglioramenti del modello. I log archiviati nei set di dati non hanno periodi di conservazione impostati.

Per impostazione predefinita, poiché la registrazione è disponibile solo per i progetti con la fatturazione abilitata,
i prompt e le risposte nei log non vengono utilizzati per il miglioramento o lo
sviluppo del prodotto, in conformità con i nostri [Termini](https://developers.google.com/terms?hl=it)
sull'utilizzo dei dati.

Se scegli di condividere i set di dati dei tuoi log con Google, questi set di dati verranno utilizzati come dati dimostrativi reali per comprendere meglio la diversità di domini e contesti in cui vengono utilizzati i sistemi e le applicazioni di AI. Questi dati possono essere utilizzati per migliorare la qualità del modello e per informare l'addestramento e la valutazione di modelli e servizi futuri. Questi dati vengono trattati in conformità con i nostri termini di utilizzo dei dati
per i [servizi non a pagamento](https://ai.google.dev/gemini-api/terms?hl=it#data-use-unpaid).

Di conseguenza, i revisori umani potrebbero leggere, annotare ed elaborare gli input e gli output delle API che condividi. Prima che i dati vengano utilizzati per il miglioramento del modello, Google adotta misure volte a proteggere la privacy degli utenti nell'ambito di questa procedura. Ciò include la disconnessione di questi dati dal tuo Account Google, dalla chiave API e dal progetto Cloud prima che i revisori li vedano o li annotino.

## Autorizzazioni dati

Se scegli di contribuire con i dati API, confermi di disporre delle autorizzazioni necessarie affinché Google possa trattare e utilizzare i dati come descritto in questa documentazione. **Non contribuire con log contenenti informazioni sensibili, riservate o proprietarie ottenute tramite il servizio a pagamento**.
La licenza che concedi a Google ai sensi della sezione "[Invio di contenuti](https://developers.google.com/terms?hl=it#b_submission_of_content)"
dei Termini per le API si estende anche, nella misura in cui ciò è richiesto dalle leggi applicabili
per il nostro utilizzo, a qualsiasi contenuto (ad es. prompt, incluse le istruzioni di sistema associate,
i contenuti memorizzati nella cache e i file come immagini, video o documenti)
che invii ai Servizi e a qualsiasi risposta generata.

## Condivisione dei dati e feedback

Puoi aiutarci a far progredire la ricerca sull'AI, l'API Gemini e Google AI Studio scegliendo di condividere i tuoi dati come esempi, consentendoci di migliorare continuamente i nostri modelli in vari contesti e di creare sistemi di AI che continuano a essere utili per gli sviluppatori in vari campi e casi d'uso.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-08 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-08 UTC."],[],[]]
