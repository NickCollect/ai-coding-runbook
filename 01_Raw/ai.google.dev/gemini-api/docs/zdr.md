---
source_url: https://ai.google.dev/gemini-api/docs/zdr?hl=it
fetched_at: 2026-09-28T06:19:56.144587+00:00
title: "Nessuna conservazione dei dati nell'API Gemini Developer \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Nessuna conservazione dei dati nell'API Gemini Developer

Questa pagina descrive in dettaglio ciò che viene comunemente definito "zero data retention"
nell'API Gemini Developer.

## Limitazione all'addestramento

Come indicato nei [Termini di servizio dell'API Gemini](https://ai.google.dev/gemini-api/terms?hl=it), quando utilizzi i servizi a pagamento, Google non utilizza i tuoi prompt (incluse le istruzioni di sistema associate, i contenuti memorizzati nella cache e i file come immagini, video o documenti) o le risposte per migliorare i propri prodotti. I Servizi a pagamento sono definiti
[qui](https://ai.google.dev/gemini-api/terms?hl=it#paid-services).

## Conservazione dei dati dei clienti e raggiungimento della conservazione zero dei dati

I dati dei clienti vengono in genere conservati per periodi di tempo limitati nei seguenti
scenari e condizioni. Per ottenere la conservazione zero dei dati, i clienti devono intraprendere azioni specifiche o evitare funzionalità specifiche in ciascuna di queste aree:

- **Registrazione dei prompt per il monitoraggio degli abusi**: come indicato nei [Termini di servizio aggiuntivi dell'API Gemini](https://ai.google.dev/gemini-api/terms?hl=it), per i Servizi a pagamento, Google registra i prompt e le risposte per un periodo di tempo limitato esclusivamente per rilevare violazioni delle [Norme relative all'uso vietato](https://policies.google.com/terms/generative-ai/use-policy?hl=it). Se il tuo
  carico di lavoro richiede la garanzia di zero conservazione dei dati o contratti di trattamento dei dati aziendali, utilizza Vertex AI. Per maggiori dettagli, vedi
  [Gemini Enterprise Agent Platform e conservazione dei dati pari a zero](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention?hl=it).
- **Grounding con la Ricerca Google**: come indicato nei [Termini di servizio aggiuntivi dell'API Gemini](https://ai.google.dev/gemini-api/terms?hl=it#grounding-with-google-search), Google memorizza prompt, informazioni contestuali e output generati per trenta (30) giorni allo scopo di creare risultati fondati e suggerimenti di ricerca.
  Queste informazioni archiviate possono essere utilizzate per il debug e il test dei sistemi
  che supportano la messa a terra. **Non è possibile disattivare l'archiviazione di queste
  informazioni se utilizzi Grounding con la Ricerca Google.**
- **Grounding con Google Maps**: come descritto nei [Termini di servizio aggiuntivi dell'API Gemini](https://ai.google.dev/gemini-api/terms?hl=it), Google memorizza prompt, informazioni contestuali e output generati per trenta (30) giorni allo scopo di creare risultati fondati. Queste informazioni memorizzate possono essere utilizzate solo per
  l'ingegneria dell'affidabilità, ad esempio il debug in caso di problemi con il servizio.
  **Non è possibile disattivare l'archiviazione di queste informazioni se utilizzi
  Grounding con Google Maps.**
- **API Interactions**: l'API Interactions gestisce lo stato attivo di una conversazione per consentire turni multi-turno. **Per impostazione predefinita, l'API Interactions
  consente l'archiviazione dello stato**. Per garantire un'impronta di dati pari a zero, devi
  impostare esplicitamente il parametro `store` su `false` nelle richieste API per disattivare
  la conservazione dello stato predefinita.
- **API Live**: questa API stateful consente la riconnessione in tempo reale memorizzando
  lo stato della conversazione. Per ottenere una conservazione dei dati pari a zero, **non configurare
  SessionResumptionConfig**. Se viene generato un handle di sessione, lo stato della conversazione (inclusi testo, audio e video) viene conservato per un massimo di 24 ore.
- **Archiviazione API File**: l'API File consente agli utenti di caricare asset di grandi dimensioni.
  I file vengono archiviati inattivi finché non vengono eliminati dall'utente o finché non scadono.
  L'utilizzo dell'API File è indipendente dalla registrazione ZDR; gli utenti devono eliminare manualmente i file per garantire un'impronta zero di dati.
- **Memorizzazione nella cache del contesto esplicito**: gli utenti possono memorizzare manualmente nella cache set di dati di grandi dimensioni (ad es.
  video lunghi o librerie di documenti) utilizzando il campo `cached_content`. Anche se
  i log di queste richieste seguono le norme di eliminazione ZDR, il contesto memorizzato nella cache
  viene archiviato con un `ttl` o un `expire_time` definito dall'utente. Per ottenere un'impronta
  di dati assolutamente nulla, non utilizzare la funzionalità cached\_content.
- **Memorizzazione nella cache in memoria implicita**: per impostazione predefinita, i modelli Gemini memorizzano nella cache i dati
  in memoria per ridurre la latenza e i costi per gli sviluppatori. Questi dati sono rigorosamente
  nella RAM (non at-rest), isolati a livello di progetto e hanno un TTL di 24 ore.
  **Ciò non viola la conservazione zero dei dati.**

## Passaggi successivi

- Scopri di più sulle [Norme relative all'uso vietato dell'AI generativa](https://policies.google.com/terms/generative-ai/use-policy?hl=it).
- Consulta i [Termini di servizio aggiuntivi dell'API Gemini](https://ai.google.dev/gemini-api/terms?hl=it).
- Se hai bisogno di controlli ZDR self-service di livello enterprise, consulta la [guida alla zero data retention
  di Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-16 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-16 UTC."],[],[]]
