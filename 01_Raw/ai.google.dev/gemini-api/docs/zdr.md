---
source_url: https://ai.google.dev/gemini-api/docs/zdr?hl=it
fetched_at: 2026-07-20T04:41:01.110619+00:00
title: "Nessuna conservazione dei dati nell'API Gemini Developer \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Nessuna conservazione dei dati nell'API Gemini Developer

Questa pagina illustra i dettagli di ciò che viene comunemente definito "conservazione zero dei dati" nell'API Gemini Developer.

## Restrizione relativa all'addestramento

Come indicato nei [Termini di servizio dell'API Gemini](https://ai.google.dev/gemini-api/terms?hl=it), quando
utilizzi i Servizi a pagamento, Google non utilizza i tuoi prompt (incluse le istruzioni di sistema associate, i contenuti memorizzati nella cache e i file come immagini, video o documenti) o
le risposte per migliorare i nostri prodotti. I Servizi a pagamento sono definiti
[qui](https://ai.google.dev/gemini-api/terms?hl=it#paid-services).

## Conservazione dei dati dei clienti e raggiungimento della conservazione zero dei dati

In genere, i dati dei clienti vengono conservati per periodi di tempo limitati nei seguenti scenari e condizioni. Per ottenere la conservazione zero dei dati, i clienti devono intraprendere azioni specifiche o evitare funzionalità specifiche in ciascuna di queste aree:

- **Registrazione dei prompt per il monitoraggio degli abusi**: come indicato nei [Termini di servizio aggiuntivi](https://ai.google.dev/gemini-api/terms?hl=it) dell'
  API Gemini, per i Servizi a pagamento, Google
  registra i prompt e le risposte per un periodo di tempo limitato esclusivamente per rilevare
  le violazioni delle [Norme relative all'uso vietato](https://policies.google.com/terms/generative-ai/use-policy?hl=it). Quando la tua richiesta di ZDR per un determinato progetto viene approvata, tutti i contenuti dell'utente (prompt e risposte) e i metadati identificabili (come indirizzi IP e ID Account Google) vengono cancellati prima della registrazione. Il record risultante viene contrassegnato come sanificato e non contiene dati di identificazione utente, garantendo la parità con la conservazione zero dei dati di Gemini Enterprise Agent Platform.
- **Grounding con la Ricerca Google**: come indicato nei [Termini di servizio aggiuntivi dell'API Gemini](https://ai.google.dev/gemini-api/terms?hl=it#grounding-with-google-search), Google archivia i prompt, le informazioni contestuali e l'output generato per trenta (30) giorni ai fini della creazione di risultati fondati e suggerimenti di ricerca.
  Queste informazioni archiviate possono essere utilizzate per il debug e il test dei sistemi che supportano il grounding. **Non è possibile disattivare l'archiviazione di queste informazioni se utilizzi il grounding con la Ricerca Google.**
- **Grounding con Google Maps**: come indicato nei [Termini di servizio aggiuntivi dell'API
  Gemini](https://ai.google.dev/gemini-api/terms?hl=it), Google archivia i prompt, le informazioni contestuali
  e l'output generato per trenta (30) giorni ai fini della creazione di risultati
  fondati. Queste informazioni archiviate possono essere utilizzate solo per l'affidabilità, ad esempio per il debug in caso di problemi con il servizio.
  **Non è possibile disattivare l'archiviazione di queste informazioni se utilizzi il grounding con Google Maps.**
- **API Interactions**: l'API Interactions gestisce lo stato attivo di una
  conversazione per consentire turni multi-turn. **Per impostazione predefinita, l'API Interactions abilita l'archiviazione dello stato**. Per garantire un'impronta di dati pari a zero, devi impostare esplicitamente il parametro `store` su `false` nelle richieste API per disattivare la conservazione dello stato predefinita.
- **API Live**: questa API con stato consente la riconnessione in tempo reale memorizzando
  lo stato della conversazione. Per ottenere la conservazione zero dei dati, **non configurare SessionResumptionConfig**. Se viene generato un handle di sessione, lo stato della conversazione (inclusi testo, audio e video) viene conservato per un massimo di 24 ore.
- **Archiviazione dell'API File**: l'API File consente agli utenti di caricare asset di grandi dimensioni.
  I file vengono archiviati inattivi finché non vengono eliminati dall'utente o fino alla loro scadenza.
  L'utilizzo dell'API File è indipendente dalla registrazione della conservazione zero dei dati; gli utenti devono eliminare manualmente i file per garantire un'impronta di dati pari a zero.
- **Memorizzazione nella cache del contesto esplicito**: gli utenti possono memorizzare manualmente nella cache set di dati di grandi dimensioni (ad es.
  video lunghi o librerie di documenti) utilizzando il campo `cached_content`. Sebbene i log di queste richieste seguano le norme di eliminazione della conservazione zero dei dati, il contesto memorizzato nella cache viene archiviato con un valore `ttl` o `expire_time` definito dall'utente. Per ottenere un'impronta di dati pari a zero assoluta, non utilizzare la funzionalità cached\_content.
- **Memorizzazione nella cache in memoria implicita**: per impostazione predefinita, i modelli Gemini memorizzano i dati nella cache
  in memoria per ridurre la latenza e i costi per gli sviluppatori. Questi dati sono strettamente in RAM (non inattivi), isolati a livello di progetto e hanno un TTL di 24 ore.
  **Ciò non viola la conservazione zero dei dati.**

## Passaggi successivi

- Scopri di più sulle [Norme relative all'uso vietato dell'AI generativa
  Policy](https://policies.google.com/terms/generative-ai/use-policy?hl=it).
- Consulta i [Termini di servizio aggiuntivi dell'API Gemini](https://ai.google.dev/gemini-api/terms?hl=it).
- Se hai bisogno di controlli di conservazione zero dei dati self-service di livello enterprise, consulta la [guida
  Conservazione zero dei dati
  di Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-28 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-28 UTC."],[],[]]
