---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=it
fetched_at: 2026-10-19T05:47:13.501065+00:00
title: "Deployment da Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Deployment da Google AI Studio

Google AI Studio ti consente di eseguire il deployment delle applicazioni full-stack direttamente
dalla modalità Build. In questo modo, il prototipo può essere trasformato rapidamente in un ambiente di produzione gestito e scalabile.

## Opzioni di deployment

Per eseguire il deployment dell'applicazione dalla modalità di creazione di AI Studio, i requisiti dipendono
dal livello che utilizzi:

- [**Livello iniziale Google Cloud**](https://docs.cloud.google.com/docs/starter-tier?hl=it):
  Consente agli account idonei di pubblicare fino a due applicazioni full-stack senza
  configurare un progetto Google Cloud o un account di fatturazione.
- **Deployment standard**: richiede un progetto Google Cloud collegato al tuo
  account AI Studio e la fatturazione abilitata per il progetto.

## Informazioni sullo Starter Tier

Il livello Starter Tier di Google Cloud offre un percorso semplificato per gli account idonei per eseguire il deployment di applicazioni su Google Cloud direttamente da Google AI Studio. Non devi
configurare un ambiente Google Cloud o un account di fatturazione completo.

Ogni deployment di Google AI Studio crea un servizio corrispondente in
Cloud Run. Per i servizi di cui è stato eseguito il deployment in Google AI Studio con il livello
Starter, si applicano le seguenti limitazioni:

- Puoi eseguire il deployment di un massimo di due servizi.
- I tuoi servizi vengono implementati in una
  [singola regione Cloud Run](https://docs.cloud.google.com/run/docs/locations?hl=it).

### Idoneità a Starter Tier

Non tutti gli account sono idonei per lo Starter Tier di Google Cloud. Il tuo account
potrebbe non essere idoneo se si verifica una delle seguenti condizioni:

- Hai eseguito l'accesso con un account Google Workspace (inclusi abbonamenti Google Workspace, Google Workspace for Education o Google per il non profit a pagamento o senza costi).
- Hai un account di fatturazione Google Cloud a pagamento attivo o precedente.
- Al momento non disponiamo di prove sufficienti dall'attività del tuo account per concedere l'accesso al livello Starter.

Il team di assistenza di Google AI Studio non può ignorare l'idoneità allo Starter Tier. Se
il tuo account non è idoneo, collega un account di fatturazione e utilizza
l'[implementazione standard](#standard-deployment) per pubblicare le app.

## Esegui il deployment con lo Starter Tier

Dopo aver progettato l'app in modalità Build, esegui il deployment con Starter Tier:

1. Fai clic sul pulsante **Pubblica** nell'angolo in alto a destra.
2. Fai clic su **Inizia**.
3. Fai clic su **Pubblica app**.

Una volta completato il deployment, AI Studio fornisce un URL Cloud Run in cui puoi
accedere alla tua applicazione live.

## URL personalizzati per AI Studio

Quando pubblichi un'applicazione da Google AI Studio, puoi impostare un sottodominio personalizzato e memorabile in `ai.studio` (ad esempio, `https://your-app-name.ai.studio`).

Google AI Studio richiede che i sottodomini siano univoci a livello globale in tutti i progetti
e li assegna in base all'ordine di arrivo. Se un altro progetto
utilizza già un nome, AI Studio ti chiede di sceglierne uno diverso. Se annulli la pubblicazione o elimini un'applicazione, il relativo URL personalizzato viene rilasciato e diventa disponibile per altri utenti.

### Impostare un URL personalizzato

Per impostare o aggiornare un URL personalizzato per la tua applicazione:

1. Apri l'applicazione in Google AI Studio in modalità **Build**.
2. Fai clic su **Pubblica** nell'angolo in alto a destra.
3. Nella configurazione del deployment, inserisci il sottodominio che preferisci nel campo
   **URL personalizzato** o accetta l'URL suggerito.
4. Fai clic su **Pubblica app**.

Per trasferire un URL personalizzato esistente a un'altra applicazione, devi prima
annullare la pubblicazione o eliminare l'applicazione a cui è assegnato l'URL personalizzato, quindi
pubblicare la nuova applicazione utilizzando il sottodominio scelto.

### Segnalare problemi relativi a marchi o copyright

I sottodomini personalizzati devono essere conformi ai
[Termini di servizio di Google](https://policies.google.com/terms?hl=it). Se noti un URL personalizzato che viola un marchio o utilizza un nome protetto da copyright senza autorizzazione, puoi segnalarlo utilizzando lo [strumento per la risoluzione dei problemi legali di Google](https://support.google.com/legal/troubleshooter/1114905?hl=it).

## Deployment standard

Man mano che le tue applicazioni si evolvono, potresti aver bisogno di funzionalità che vanno oltre lo Starter Tier, come quote più elevate o maggiori risorse di calcolo o altri prodotti Google Cloud non disponibili nello Starter Tier. Per sbloccare
queste funzionalità, puoi convertire il tuo progetto di livello base completamente gestito in
un progetto Google Cloud standard.

In questo modo, puoi scalare senza problemi senza perdere
i tuoi progressi. Segui i passaggi per
[creare un account di fatturazione Cloud](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=it#create-new-billing-account),
accettare formalmente i Termini di servizio standard di Google Cloud e
[eseguire l'upgrade a un progetto Google Cloud standard](https://docs.cloud.google.com/docs/starter-tier?hl=it#upgradee).
Per saperne di più, consulta
[Configurazione per gli account a pagamento](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=it#paid-setup).

Per saperne di più sui livelli di fatturazione, consulta [Fatturazione](https://ai.google.dev/gemini-api/docs/billing?hl=it).

## Eliminare la richiesta

Se non hai più bisogno della tua app, puoi eliminarla in Google AI Studio
seguendo queste istruzioni:

1. In Google AI Studio, vai alla
   [pagina App](https://aistudio.google.com/app/apps?hl=it).
2. Nel menu a sinistra, seleziona **App**.
3. Tieni il puntatore sopra l'app che vuoi eliminare.
4. Fai clic sull'icona del cestino sul lato destro della riga per eliminare l'app.

## Passaggi successivi

- Scopri di più sullo
  [Starter Tier di Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=it).
- Scopri di più sulla [fatturazione](https://ai.google.dev/gemini-api/docs/billing?hl=it) nell'API Gemini.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-28 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-28 UTC."],[],[]]
