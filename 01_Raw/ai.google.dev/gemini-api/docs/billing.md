---
source_url: https://ai.google.dev/gemini-api/docs/billing?hl=it
fetched_at: 2026-06-29T05:41:42.148859+00:00
title: "Fatturazione \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Fatturazione

Questa guida fornisce una panoramica delle diverse opzioni di fatturazione dell'API Gemini,
spiega come attivare la fatturazione e monitorare l'utilizzo e fornisce risposte alle
domande frequenti sulla fatturazione.

## Informazioni su fatturazione e livelli

La fatturazione per l'API Gemini si basa sulla tua cronologia dei pagamenti.

| Livello di utilizzo | Qualificazione | [Limite del livello di fatturazione](#spend-caps) |
| --- | --- | --- |
| **Nessun costo** | [Progetto attivo](https://ai.google.dev/gemini-api/docs/api-key?hl=it#google-cloud-projects) o prova senza costi | N/D |
| **Livello 1** | [Configura e collega un account di fatturazione attivo](#setup-billing) | 250 $ |
| **Livello 2** | Pagamento di 100 $+ 3 giorni dal primo pagamento riuscito | $ 2000 |
| **Livello 3** | Pagamento di 1000 $+ 30 giorni dal primo pagamento riuscito | 20.000 $-100.000+ $ |

I nuovi account iniziano con il Livello senza costi, che consente l'accesso a
[determinati modelli](https://ai.google.dev/gemini-api/docs/pricing?hl=it) nell'API Gemini e in AI Studio,
fino ai [limiti di frequenza](https://aistudio.google.com/rate-limit?hl=it) del Livello senza costi dei modelli.

Per eseguire il deployment delle applicazioni direttamente dalla modalità di creazione, puoi utilizzare il
**livello iniziale di Google Cloud**. Questo livello ti consente di pubblicare fino a due applicazioni full-stack senza configurare un progetto Google Cloud o un account di fatturazione.
Per maggiori dettagli, consulta [Deployment da Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=it) e la [documentazione di Google Cloud Starter Tier](https://docs.cloud.google.com/docs/starter-tier?hl=it).

Per accedere a limiti di frequenza più elevati, utilizzare modelli avanzati e assicurarti che i prompt e le
risposte **non** vengano utilizzati per migliorare i prodotti Google\*, puoi
[collegare un account di fatturazione](#setup-billing) e [pagare in anticipo](#prepay) per passare ai
livelli a pagamento.
Successivamente, passerai ai livelli superiori in base alla spesa cumulativa e all'età dell'account. Al livello 3, potresti avere la possibilità di passare alla fatturazione [postpagamento](#postpay).

I livelli, i limiti di frequenza e i limiti dell'account di fatturazione sono tutti determinati a livello di [account di
fatturazione](#cloud-billing).

\* *Privacy dei dati di livello aziendale: per saperne di più sull'utilizzo dei dati
per i servizi a pagamento, consulta i [Termini di servizio](https://ai.google.dev/gemini-api/terms?hl=it#data-use-paid).*

## Configurare la fatturazione per accedere al livello a pagamento

Puoi creare un progetto e configurare la fatturazione o importare un progetto esistente per eseguire l'upgrade al livello a pagamento in [Google AI Studio](https://aistudio.google.com/projects?hl=it).
L'upgrade dal Livello senza costi al Livello a pagamento prevede il collegamento di un account di fatturazione
e il [pagamento anticipato](#prepay) per aggiungere al tuo account un minimo di 10 $ (o l'equivalente in altre
valute) di crediti.

1. Vai alla pagina [Chiavi API](https://aistudio.google.com/api-keys?hl=it), alla pagina [Progetti](https://aistudio.google.com/projects?hl=it) o in qualsiasi punto in cui vedi il pulsante **Configura fatturazione** in AI Studio.
   - Per i nuovi utenti verranno creati per impostazione predefinita un [progetto e una chiave API](https://ai.google.dev/gemini-api/docs/api-key?hl=it#google-cloud-projects).
   - Se hai bisogno di una nuova chiave, fai clic su [**Crea chiave API**](https://aistudio.google.com/api-keys?hl=it)
     e segui la finestra di dialogo per aggiungere una coppia chiave-progetto alla tabella.
2. Individua il progetto Livello senza costi che vuoi eseguire l'upgrade al livello a pagamento e fai clic su
   **Configura fatturazione** nella colonna *Livello di fatturazione*.
3. Se non hai mai configurato un account Google per la fatturazione:
   - Ti verrà chiesto di selezionare il tuo paese per accettare i Termini di servizio.
   - Poi, inserisci o conferma i tuoi dati di contatto e il metodo di pagamento per continuare.
4. Se hai configurato account di fatturazione Google in passato:
   - Ti verrà chiesto di scegliere tra i tuoi account di fatturazione esistenti.
   - Se non vuoi utilizzare nessuno dei tuoi account esistenti, fai clic su **Aggiungi nuovo
     account di fatturazione** e compila o conferma i tuoi dati di contatto e il
     metodo di pagamento per continuare.
5. Successivamente, potrai:
   - Ti è stato chiesto di pagare in anticipo un minimo di 10 $per completare la configurazione della fatturazione (il tuo account viene assegnato automaticamente al piano di fatturazione [Prepagato](#prepay)).
   - Data la scelta tra i piani di fatturazione [pagamento anticipato](#prepay) e [pagamento posticipato](#postpay) per il tuo account.
   - Assegnato a un piano di fatturazione [postpagamento](#postpay) per un periodo intermedio
     fino a quando il nuovo sistema prepagato non verrà applicato a tutti gli utenti (a partire dal 23 marzo 2026).
6. Dopo aver effettuato il pagamento anticipato o selezionato il pagamento posticipato, la configurazione dell'account è completata.

### Eseguire l'upgrade al livello a pagamento successivo

Se hai già un livello a pagamento e soddisfi i [criteri](#about-billing)
per un cambio di piano, verrà eseguito automaticamente l'upgrade al livello successivo
(in base ai [tempi di elaborazione](#processing-times)).

## Verificare lo stato di fatturazione

Dopo aver [collegato un account di fatturazione](#setup-billing) al tuo progetto, puoi monitorarne lo stato nella [pagina Fatturazione di AI Studio](https://aistudio.google.com/billing?hl=it). A differenza del livello senza costi, lo stato del livello a pagamento è dinamico: mentre il livello di utilizzo è determinato dalla cronologia dell'account, l'API Gemini servirà le richieste solo se hai un saldo dei crediti [prepagati](#prepay) positivo.

Nella pagina [Progetti](https://aistudio.google.com/projects?hl=it), potrai visualizzare il livello e il piano di fatturazione del tuo progetto nella colonna *Livello di fatturazione*. Eventuali
azioni relative allo stato di fatturazione che potresti dover intraprendere per un progetto vengono visualizzate nelle colonne
*Livello di fatturazione* o *Stato*:

- "***Configura la fatturazione***" se al progetto non è collegato un account di fatturazione.
- "***Configura pagamento anticipato***" se il progetto ha un account di fatturazione collegato, ma
  deve utilizzare un piano di fatturazione con [pagamento anticipato](#prepay) che deve essere configurato.
- "***Nessun credito***" se l'account di fatturazione è tenuto ad acquistare
  crediti, ma l'account pagamenti prepagato non è configurato o il saldo
  disponibile è esaurito.

Fai clic su uno dei messaggi per procedere con le azioni necessarie.

## Monitorare l'utilizzo

Puoi monitorare l'utilizzo dell'API Gemini in
[Google AI Studio](https://aistudio.google.com/usage?hl=it) nella **dashboard** >
**Utilizzo**.

## Piani di fatturazione

I piani di fatturazione per l'API Gemini e AI Studio rientrano in due categorie che
determinano quando paghi l'utilizzo: pagamento anticipato e pagamento posticipato. Puoi controllare il piano di fatturazione assegnato e gestire i metodi di pagamento nella pagina [Fatturazione di AI Studio](https://aistudio.google.com/billing?hl=it).

### Pagamento anticipato

Nel piano di fatturazione con pagamento anticipato, acquisti crediti per il saldo del pagamento anticipato prima di utilizzare l'API Gemini e i costi di utilizzo dell'API vengono dedotti dal saldo dei crediti con pagamento anticipato [quasi in tempo reale](#processing-times).
Puoi pagare in anticipo [aggiungendo crediti](#buy-credits) al tuo account o configurando la [ricarica automatica](#auto-reload). Una volta acquistati, i crediti non utilizzati
scadono dopo 12 mesi e [non sono rimborsabili](#refunds), tranne dopo
[il passaggio a un account postpagato](#postpay).

Quando il saldo del credito prepagato dell'account di fatturazione raggiunge 0 $, tutte le chiavi API di
tutti i progetti collegati a quell'account di fatturazione smetteranno di funzionare contemporaneamente.
I crediti prepagati si applicano solo ai costi di utilizzo dell'API Gemini. Non puoi utilizzarli per pagare altri servizi Google Cloud.

Per impostazione predefinita, i nuovi utenti utilizzano il piano di fatturazione con pagamento anticipato. I progetti precedenti all'introduzione dei piani di fatturazione con pagamento anticipato e posticipato potrebbero dover [aggiornare i dettagli di fatturazione del progetto](#verify-billing) prima di continuare a utilizzare l'API Gemini.

*Tieni presente che il pagamento anticipato non è disponibile per gli account [fatturati (o offline)](https://docs.cloud.google.com/billing/docs/concepts?hl=it#billing_account_types).*

#### Acquista crediti

Puoi acquistare manualmente i crediti in anticipo rispetto all'utilizzo dell'API Gemini per caricarli
nel saldo del credito dell'account con pagamento anticipato.

Per acquistare crediti, vai alla pagina [Fatturazione di AI Studio](https://aistudio.google.com/billing?hl=it) e seleziona **Acquista crediti**.
L'acquisto minimo è di 10 $. L'importo massimo di crediti che puoi pagare in anticipo è di
5000 $.

#### Ricarica automaticamente

La ricarica automatica è una funzionalità facoltativa che ricarica automaticamente il saldo dei crediti prepagati
quando sta per esaurirsi. Ciò è utile per evitare interruzioni del servizio.

Puoi configurare la ricarica automatica e visualizzarne lo stato nella scheda *Crediti
disponibili* della pagina [Fatturazione di AI Studio](https://aistudio.google.com/billing?hl=it). Fai clic su **Configura ricarica automatica** o
**Gestisci ricarica automatica** per impostare il metodo di pagamento, l'importo di ricarica e il
saldo minimo che attiva un pagamento di ricarica.

#### Limite di addebito automatico mensile

Il limite di addebito automatico mensile è disponibile per gli utenti prepagati
e contribuisce a evitare costi imprevisti dovuti a frequenti ricariche automatiche del credito.
Utilizza questa funzionalità per impostare un limite massimo per le ricariche automatiche di crediti all'interno di un singolo ciclo di fatturazione. Una volta raggiunto questo limite, il sistema disattiva la ricarica automatica fino all'inizio del mese successivo. I pagamenti una tantum che avvii manualmente non vengono conteggiati ai fini di questo limite.

Per impostare il limite di addebito automatico mensile quando la ricarica automatica è attivata:

1. Vai alla pagina [Fatturazione di AI Studio](https://aistudio.google.com/billing?hl=it).
2. Fai clic su **Gestisci la ricarica automatica**.
3. Espandi la sezione **Limite mensile** e inserisci il limite mensile massimo per le ricariche automatiche.
4. Fai clic su **Salva**.

### Pagamento posticipato

Nel piano di fatturazione postpagamento, il tuo account di fatturazione Cloud accumula costi e ti
vengono addebitati automaticamente alla fine del mese o quando i costi raggiungono un
[limite di spesa assegnato automaticamente](#tier-spend-caps) in base al livello del tuo account.
Il pagamento viene addebitato sul metodo di pagamento collegato al tuo account
pagamenti posticipati, che puoi gestire nella pagina [Fatturazione di AI Studio](https://aistudio.google.com/billing?hl=it).

Quando soddisfi i [criteri del livello 3](#about-billing), puoi
passare manualmente dal piano prepagato a quello postpagato. Per cambiare piano, dovrai
fare clic sul pulsante **Passa al pagamento posticipato** visualizzato in alto a destra
della pagina [Fatturazione di AI Studio](https://aistudio.google.com/billing?hl=it) quando il tuo
account diventa idoneo.

Nella pagina **Fatturazione** potrai visualizzare il saldo, le date di scadenza
e i pagamenti passati, nonché effettuare pagamenti e gestire i metodi di pagamento.

Quando [configuri la fatturazione](#setup-billing) per un nuovo progetto, se hai l'idoneità per il pagamento posticipato, potrai scegliere tra pagamento anticipato e posticipato nella finestra di dialogo [configurazione di fatturazione](#setup-billing).

Dopo aver cambiato un account di fatturazione Cloud in modo che utilizzi il piano di fatturazione postpagato, tutti i progetti collegati a quell'account di fatturazione vengono spostati al piano postpagato. Non puoi ripristinare il piano di fatturazione prepagato per questo account di fatturazione. Puoi
spostare un progetto in un account di fatturazione con un piano di fatturazione diverso per modificare
il ciclo di addebito per quel progetto. Consulta la documentazione di Cloud sulla [gestione
della fatturazione per i progetti](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=it).

Per saperne di più sul ciclo di addebito postpagato, consulta la [guida alla fatturazione Cloud](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=it).

## Limiti di spesa

L'API Gemini supporta i limiti di spesa mensili sia a livello di account di fatturazione sia a livello di progetto. Questi controlli sono progettati per proteggere il tuo account da
superamenti imprevisti e l'ecosistema per garantire la disponibilità del servizio.

*Tieni presente che i limiti di spesa non sono disponibili per gli account [fatturati (o offline)](https://docs.cloud.google.com/billing/docs/concepts?hl=it#billing_account_types).*

### Limiti di spesa del progetto

Puoi impostare i tuoi limiti di spesa [a livello di progetto](https://ai.google.dev/gemini-api/docs/api-key?hl=it#google-cloud-projects) in AI Studio.
Questa funzionalità è utile se hai più progetti nello stesso account di fatturazione e vuoi assicurarti che ognuno abbia accesso a una parte sufficiente del limite di spesa cumulativo.

Gli account con i [ruoli](https://docs.cloud.google.com/iam/docs/roles-overview?hl=it) di editor, proprietario o amministratore del progetto possono impostare limiti di spesa per progetto in AI Studio nella pagina [Spesa](https://aistudio.google.com/spend?hl=it) in **Limite di spesa mensile** > **Modifica limite di spesa**.

Per informazioni dettagliate sulle autorizzazioni Cloud IAM di Google Cloud specifiche richieste per visualizzare o modificare i limiti di spesa e i dati di fatturazione in AI Studio, consulta la [guida alla risoluzione dei problemi di AI Studio](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=it#iam-permissions).

Se [sposti un progetto in un altro account di fatturazione](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=it#change_the_billing_account_for_a_project),
il limite di spesa che hai già impostato per quel progetto verrà mantenuto, ma la spesa
accumulata verrà reimpostata su 0 $per il nuovo ciclo di fatturazione.

Le attività di lunga durata come i completamenti in [modalità batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it) e le sessioni degli agenti potrebbero comportare superamenti del limite di spesa del progetto.

I tempi di elaborazione dei dati di fatturazione possono subire ritardi in AI Studio, fino a circa 10 minuti. Potresti riscontrare superamenti oltre il limite del progetto se i dati di fatturazione
non sono stati elaborati prima dell'accumulo di ulteriori addebiti.

### Limiti di spesa per livello dell'account di fatturazione

Ogni [livello](#about-billing) ha un limite di spesa mensile massimo:

| Livello di utilizzo | Limite di spesa |
| --- | --- |
| **Nessun costo** | N/D |
| **Livello 1** | 250 $ |
| **Livello 2** | $ 2000 |
| **Livello 3** | 20.000 $-100.000 $ |

I limiti di utilizzo mensili vengono applicati all'API Gemini a livello di [account di fatturazione](#cloud-billing). Anche se i limiti predefiniti sono preimpostati, puoi [richiedere un
aumento](https://docs.google.com/forms/d/e/1FAIpQLSdiP6BWJyNNN65lnwnlOr-5Kv0MOFp0jLQyqi_ixVCfddqWBw/viewform?hl=it)
per adattarli a un utilizzo maggiore. La spesa totale viene aggregata in tutti i progetti collegati in cui è abilitato il servizio API Gemini. Una volta che il totale cumulativo dell'account
raggiunge il limite del livello, il servizio viene sospeso per tutti i progetti collegati a quell'account di fatturazione fino all'inizio del ciclo di fatturazione successivo (il 1° di ogni mese).

#### Valutare la spesa dell'account di fatturazione

Per valutare la spesa mensile storica e determinare se i nuovi [limiti di spesa per livello dell'account di fatturazione](#tier-spend-caps) influiranno sui tuoi progetti in corso,
segui questi passaggi:

1. Nella console Google Cloud, visualizza la pagina [Report dell'account di fatturazione Cloud](https://console.cloud.google.com/billing/reports?hl=it).
   - Se hai più di un account di fatturazione, quando richiesto scegli l'account di fatturazione Cloud per cui vuoi visualizzare i report sui costi.
2. Per impostazione predefinita, il report è impostato su "Raggruppa per servizio" nel "Mese attuale". Vedrai **API Gemini** nella colonna **Servizio** e la spesa totale nella colonna **Costo
   utilizzo** della tabella.
3. Per visualizzare i costi granulari limitati all'utilizzo dell'API Gemini, imposta il filtro **Raggruppa per**
   in modo da raggruppare per **SKU** e il filtro **Servizi** su **API Gemini**.
4. Modifica il filtro **Intervallo di tempo per data di utilizzo** in base all'intervallo che preferisci per
   valutare la spesa storica in un periodo.

## Tempi di elaborazione

Gli indicatori e gli aggiornamenti della fatturazione non vengono sempre eseguiti in tempo reale.

- **Utilizzo del credito**: i costi di utilizzo vengono in genere detratti dal saldo
  nel giro di pochi minuti.
- **Conferma del pagamento**: anche se la maggior parte dei pagamenti con carta è immediata, alcune forme
  di pagamento (come i bonifici bancari) potrebbero richiedere diversi giorni per essere autorizzate. I servizi
  vengono ripristinati o eseguiti l'upgrade solo dopo la conferma ufficiale dell'acquisto dei crediti.
- **Upgrade di livello**: dopo un pagamento andato a buon fine o quando soddisfi i [criteri di upgrade](#about-billing), gli upgrade di livello vengono in genere visualizzati entro 10 minuti.
- **Grafici di suddivisione del costo totale**: i grafici che mostrano la suddivisione del costo totale sia nella pagina [Fatturazione](https://aistudio.google.com/billing?hl=it) sia nella pagina [Spesa](https://aistudio.google.com/spend?hl=it) possono richiedere fino a 24 ore per l'aggiornamento.

Per saperne di più sui potenziali ritardi di fatturazione, leggi le guide alla fatturazione Cloud su [ciclo di addebito](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=it#delayed-billing) e latenze delle [transazioni](https://docs.cloud.google.com/billing/docs/how-to/view-history?hl=it#missing-transactions).

## Rimborsi

I rimborsi non sono consentiti per gli account di fatturazione **prepagati**, tranne quando si cambia
il tipo di account.

**Quando un account prepagato passa al tipo di account postpagato** (dopo che hai
soddisfatto i [criteri](#about-billing) ed eseguito l'[upgrade manuale](#postpay)
dell'account), l'account prepagato viene chiuso e l'eventuale credito prepagato residuo
viene rimborsato automaticamente sul metodo di pagamento registrato.

Se [chiudi](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=it#close-a-billing-account)
il tuo account prepagato per qualsiasi motivo diverso dall'upgrade a Postpagato, i
crediti prepagati rimanenti vengono persi.

I crediti acquistati scadono dopo 1 anno. Una volta scaduti, i crediti vengono persi
e non possono essere recuperati.

Gli account **postpagamento** seguono le [norme di rimborso di Google Cloud](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=it#request_a_refund).

## Account di fatturazione Cloud

L'API Gemini utilizza [account di fatturazione Cloud](https://cloud.google.com/billing/docs/concepts?hl=it) per i servizi di fatturazione, che puoi [configurare direttamente in AI Studio](#setup-billing).
Puoi utilizzare AI Studio per monitorare la spesa, comprendere i costi ed effettuare pagamenti.

I livelli, i limiti di frequenza e i limiti dell'account di fatturazione vengono determinati a livello di account di fatturazione.

### Progetti e chiavi API

Tutti i [progetti](https://ai.google.dev/gemini-api/docs/api-key?hl=it#google-cloud-projects) collegati a un account di fatturazione Cloud ereditano il livello di utilizzo e i limiti di velocità e i limiti dell'account associati. Se [modifica un progetto](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=it#change_the_billing_account_for_a_project)
da un account di fatturazione a un altro, il suo livello e, di conseguenza, i limiti di frequenza e
i limiti dell'account, passeranno al livello del nuovo account di fatturazione.

La spesa cumulativa (per tutti i prodotti Google Cloud) e l'età dell'account in tutti i
progetti collegati a un account di fatturazione vengono conteggiati ai fini delle
[qualifiche per il livello](#about-billing) dell'account di fatturazione.

Puoi [scollegare un progetto](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=it#disable_billing_for_a_project)
dal relativo account di fatturazione per tornare al livello senza costi.

Le [chiavi API](https://ai.google.dev/gemini-api/docs/api-key?hl=it) sono credenziali generate all'interno di un progetto.
Non hanno impostazioni di fatturazione indipendenti; ereditano i limiti del livello e lo stato di fatturazione del progetto. L'utilizzo cumulativo di tutte le chiavi all'interno di un progetto viene conteggiato ai fini del limite di spesa del progetto e della spesa totale dell'account di fatturazione.

## Domande frequenti

Le seguenti sezioni forniscono le risposte alle domande frequenti.

### A che cosa si riferiscono gli addebiti che ricevo?

I prezzi dell'API Gemini si basano su quanto segue:

- Conteggio token di input
- Conteggio token di output
- Conteggio dei token memorizzati nella cache
- Durata di archiviazione dei token memorizzati nella cache

Per informazioni sui prezzi, consulta la [pagina dei prezzi](https://ai.google.dev/pricing?hl=it).

### Dove posso visualizzare la mia quota?

Puoi visualizzare la quota e i limiti di sistema in
[AI Studio](https://aistudio.google.com/usage?hl=it).

### Come faccio a passare a un livello di limite di frequenza più alto o a richiedere una quota maggiore?

Ti verrà concessa automaticamente una quota maggiore quando il tuo account raggiungerà i successivi
[requisiti del livello](https://ai.google.dev/gemini-api/docs/rate-limits?hl=it#usage-tiers).

### Posso utilizzare l'API Gemini senza costi nel SEE (inclusa l'UE), nel Regno Unito e in Svizzera?

Sì, rendiamo disponibili il livello senza costi e quello a pagamento in [molte regioni](https://ai.google.dev/gemini-api/docs/available-regions?hl=it).

### Se configuro la fatturazione con l'API Gemini, mi verrà addebitato l'utilizzo di Google AI Studio?

L'utilizzo di AI Studio rimane senza costi, a meno che gli utenti non colleghino una chiave API a pagamento per accedere alle funzionalità a pagamento.
Una volta collegata una chiave API a pagamento nell'ambito di un progetto a pagamento in AI Studio, ti verrà addebitato l'utilizzo di AI Studio per quella chiave. Puoi passare da progetti con livello a pagamento a progetti con Livello senza costi in base alle esigenze utilizzando le rispettive chiavi API collegate a ogni tipo.

### Se utilizzo il livello senza costi, come faccio a eseguire l'upgrade a livelli superiori?

Per accedere ai livelli superiori, devi configurare la fatturazione nel tuo progetto. Fai clic su [**Configura
la fatturazione**](#setup-billing) in Google AI Studio. Ti guiderà nella selezione o nella creazione di un account di fatturazione Cloud. Se devi utilizzare il modello di fatturazione prepagata, la procedura **Configura fatturazione** ti guiderà nella creazione del tuo account prepagato collegato al tuo account di fatturazione Cloud.

### Posso utilizzare 1 milione di token nel livello senza costi?

Il livello senza costi dell'API Gemini varia in base al modello selezionato. Per il momento, puoi provare la finestra contestuale da 1 milione di token nei seguenti modi:

- In Google AI Studio
- Con piani senza costi per modelli selezionati
- Con i piani con pagamento posticipato

### Posso tornare al livello senza costi dopo aver eseguito l'upgrade a livelli superiori (a pagamento)?

Per eseguire il downgrade al Livello senza costi, puoi [disattivare la fatturazione](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=it#disable_billing_for_a_project)
per ciascuno dei progetti per cui vuoi eseguire il downgrade.

### Come faccio a calcolare il numero di token che sto utilizzando?

Utilizza il metodo [`GenerativeModel.count_tokens`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=it#count_tokens)
per conteggiare il numero di token. Per saperne di più sui token, consulta la [guida ai token](https://ai.google.dev/gemini-api/docs/tokens?hl=it).

### Se mi registro per il mio primo account di fatturazione Cloud tramite AI Studio, riceverò comunque una prova senza costi di Google Cloud?

Quando ti registri per il tuo primo account di fatturazione Cloud, inizia la [prova senza costi di Google Cloud](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=it#free-trial) e ti vengono concessi 300 $di [credito di benvenuto](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=it#welcome-credits).
Tuttavia, questi crediti non possono essere utilizzati per pagare l'utilizzo di AI Studio. Puoi utilizzare il
credito di benvenuto per pagare altri servizi idonei all'interno di Google Cloud (tieni presente che
una volta consumati o scaduti (entro 90 giorni), eventuali costi di utilizzo aggiuntivi
vengono fatturati automaticamente al metodo di pagamento stabilito).

### Posso utilizzare il mio credito di benvenuto di Google Cloud con l'API Gemini?

No, il [credito di benvenuto](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=it#welcome-credits)
o il credito della prova senza costi di Google Cloud non possono essere utilizzati per l'API Gemini o AI Studio.

Se ti è stato concesso un credito di benvenuto Google Cloud prima che diventasse
non idoneo, puoi spendere i crediti rimanenti per l'API Gemini
e AI Studio fino alla scadenza dei crediti (dopo 90 giorni).

### La prova senza costi di Google Cloud si applica all'utilizzo dell'API Gemini?

No, a partire da marzo 2026, i costi di utilizzo dell'API Gemini sono specificamente esclusi dal programma [prova senza costi di Google Cloud di 300$](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=it#free-trial).

### Come funzionano i crediti Google Cloud con il pagamento anticipato?

Gli utenti prepagati devono prima [acquistare crediti prepagati](#buy-credits) prima che
possano essere applicati crediti Google Cloud idonei all'utilizzo dell'API Gemini. Una volta che hai
un saldo del credito prepagato attivo, i crediti Google Cloud idonei per l'API
Gemini vengono utilizzati prima del saldo del credito prepagato. Quando il saldo del credito prepagato nell'account di fatturazione raggiunge 0 $, i crediti Google Cloud non verranno più utilizzati.

Non tutti i crediti Google Cloud, come il
[credito di benvenuto di Google Cloud](#cloud-credits), possono essere utilizzati per l'API Gemini
e AI Studio.

### Come viene gestita la fatturazione?

La fatturazione dell'API Gemini viene gestita dal sistema di [fatturazione Cloud](https://cloud.google.com/billing/docs/concepts?hl=it). Scopri di più sulla
configurazione della fatturazione Cloud nel prodotto nella [documentazione sulla fatturazione Cloud](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=it).

### Mi vengono addebitati costi per le richieste non riuscite?

Se la richiesta non va a buon fine e viene visualizzato un errore 400 o 500, non ti verranno addebitati i token utilizzati. Tuttavia, la richiesta verrà comunque conteggiata ai fini del calcolo della quota.

### `GetTokens` è fatturato?

Le richieste all'API `GetTokens` non vengono fatturate e non vengono conteggiate ai fini della quota di inferenza.

### Come vengono gestiti i miei dati di Google AI Studio se ho un account API a pagamento?

Per informazioni dettagliate sul trattamento dei dati quando è abilitata la fatturazione Cloud, consulta i [Termini di servizio](https://ai.google.dev/gemini-api/terms?hl=it#paid-services) (vedi "In che modo Google utilizza i tuoi dati" nella sezione "Servizi a pagamento"). Tieni presente che i prompt di Google AI Studio sono
trattati ai sensi degli stessi termini dei "Servizi a pagamento" purché almeno un progetto API
abbia la fatturazione abilitata, che puoi convalidare nella
[pagina della chiave API Gemini](https://aistudio.google.com/api-keys?hl=it) se vedi
progetti contrassegnati come "A pagamento" in "Piano".

### Che cos'è la fatturazione prepagata e chi è tenuto a utilizzare il modello di fatturazione prepagata?

La fatturazione prepagata consente agli utenti dell'API Gemini in AI Studio di pre-acquistare i crediti.
A partire dal 23 marzo 2026, i nuovi utenti di AI Studio potrebbero dover utilizzare il piano di fatturazione prepagato. Durante la procedura di [configurazione della fatturazione](#setup-billing) di AI Studio, l'interfaccia utente ti guiderà nel flusso di configurazione della fatturazione e indicherà se è necessario effettuare un pagamento anticipato.

### Come faccio ad acquistare i crediti prepagati? Esiste un importo minimo o massimo?

Puoi [acquistare crediti](#buy-credits) nella pagina Fatturazione di AI Studio. Durante
la procedura di acquisto, l'interfaccia utente fornirà l'importo minimo di pre-acquisto
richiesto per la tua regione e il tuo livello, nonché un importo massimo che può
essere presente nel tuo account contemporaneamente.

### Posso configurare il mio account con pagamento anticipato in modo che acquisti automaticamente altri crediti in base alle necessità?

Sì, ti consigliamo di configurare il [ricaricamento automatico](#auto-reload) nelle impostazioni di fatturazione di AI
Studio. Specifichi un saldo del credito "trigger" (ad es. "quando il mio saldo scende al di sotto di 30 $") e un "valore di ricarica" (ad es. "aggiungi 100 $").

### Posso limitare l'importo degli addebiti per la ricarica automatica?

Sì, gli utenti prepagati possono impostare un [limite di addebito automatico mensile](#monthly-auto-charge-limit)
all'interno del widget **Ricarica automatica**. Quando l'importo totale delle ricariche automatiche in un ciclo di fatturazione raggiunge questo limite, il sistema disattiva la ricarica automatica fino al mese successivo. Gli acquisti manuali di crediti non vengono conteggiati ai fini di questo limite.

### Posso ricevere un rimborso per i miei crediti inutilizzati?

Tutti i crediti API prepagati scadono dopo 1 anno e non possono essere rimborsati. Leggi le
[norme sui rimborsi per gli account prepagati](#refunds).

### I miei crediti prepagati hanno una scadenza?

Sì, i crediti scadono 12 mesi dopo la data di acquisto.

### Che cosa succede quando il saldo del mio credito prepagato raggiunge 0 €?

Tutti i servizi dell'API Gemini in tutti i progetti pagati da quell'account di prepagamento della fatturazione Cloud verranno interrotti immediatamente per evitare ulteriori addebiti. I tuoi progetti
non vengono automaticamente sottoposti a downgrade al Livello senza costi.

Per ripristinare il servizio al tuo attuale livello di piano a pagamento, devi [acquistare
crediti aggiuntivi](#buy-credits). Dopo aver acquistato i crediti, dovresti essere in grado di utilizzare l'API Gemini. Tieni presente che potrebbe verificarsi un [ritardo](#processing-times) durante l'aggiornamento dei nostri sistemi per riflettere il saldo del credito.

Se vuoi eseguire il downgrade al Livello senza costi, puoi [disattivare la fatturazione](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=it#disable_billing_for_a_project)
per i progetti per cui vuoi eseguire il downgrade.

### Perché il mio utilizzo si è interrotto anche se il saldo del credito prepagato è superiore a 0 €?

Potresti aver raggiunto il [limite di utilizzo](#tier-spend-caps) per il tuo livello attuale.
I limiti di utilizzo aumenteranno automaticamente man mano che avanzi ai livelli superiori. L'utilizzo di API Gemini AI Studio può essere influenzato anche dallo [stato del tuo
account di fatturazione Cloud](#missed-payment).

### Perché il saldo del credito del mio account prepagato è negativo?

A causa della complessità dei nostri sistemi di fatturazione ed elaborazione, potrebbero verificarsi
[ritardi](#processing-times) nella nostra capacità di interrompere l'utilizzo dopo che hai consumato
tutti i tuoi crediti. Questo utilizzo in eccesso potrebbe essere visualizzato come saldo del credito negativo
nella dashboard di fatturazione di AI Studio. In questo caso, il servizio viene messo in pausa e il saldo negativo verrà detratto dal tuo prossimo acquisto di crediti.

Per evitare una pausa nel servizio API Gemini, ti consigliamo di configurare la
[ricarica automatica](#auto-reload) per acquistare automaticamente altri crediti quando il saldo
scende al di sotto di un valore specificato.

### Posso utilizzare i miei crediti prepagati per altri servizi Google Cloud, come Gemini Enterprise Agent Platform?

No, i crediti prepagati sono strettamente limitati all'utilizzo dell'API Gemini. Qualsiasi
altro servizio Google Cloud che utilizzi (Compute, Storage, Gemini Enterprise Agent Platform) viene fatturato utilizzando
il [ciclo di addebito di Cloud](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=it) standard.

### Posso passare a un piano di fatturazione con pagamento posticipato?

Quando stabilisci una cronologia dei pagamenti e [raggiungi un livello idoneo](#about-billing)
per il piano di fatturazione con pagamento posticipato, puoi scegliere facoltativamente di trasferire tutti i costi futuri di utilizzo dell'API Gemini a un [ciclo di addebito con pagamento posticipato](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=it#view-your-charging-cycle) standard e consolidato di Google Cloud.

### Che cosa succede ai miei crediti prepagati se passo a Postpay?

Quando esegui l'upgrade a [pagamento posticipato](#postpay), la fatturazione Cloud chiude il tuo account pagamenti anticipati, disattiva la [ricarica automatica](#auto-reload) e ti rimborsa automaticamente gli eventuali crediti prepagati inutilizzati (in base ai tempi standard di elaborazione dei rimborsi).

### Dove posso visualizzare il saldo attuale del credito prepagato e la cronologia delle transazioni?

Tutta la gestione del saldo e la cronologia delle transazioni per l'API Gemini devono essere
eseguite direttamente nella scheda Fatturazione di Google AI Studio.

### Perché visualizzo il messaggio "Il tipo di account di fatturazione è inattivo o non supportato"?

Le interazioni di pagamento nella [pagina Fatturazione di AI Studio](https://aistudio.google.com/billing?hl=it) potrebbero essere bloccate e sostituite dal messaggio "Il tipo di account di fatturazione è inattivo o non supportato" se il tipo di account di fatturazione o lo stato dell'account di fatturazione selezionato non è idoneo per il livello a pagamento in AI Studio.

Controlla la [console Google Cloud](https://console.cloud.google.com/billing/?hl=it) per visualizzare lo stato del tuo account di fatturazione. Un tipo non idoneo potrebbe essere *Account di prova senza costi*, nel qual caso puoi [attivare la fatturazione](#setup-billing) in AI Studio per diventare idoneo. Uno stato inattivo potrebbe essere *Chiuso*, nel qual caso puoi [riaprire
l'account](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=it).

### I costi di utilizzo dell'API Gemini verranno visualizzati nella console Google Cloud?

Sì, i costi dell'API Gemini, insieme a quelli associati a qualsiasi altro servizio Google Cloud pagato dal tuo account di fatturazione Cloud, sono visibili nelle [pagine di gestione dei costi](https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle?hl=it#cost-reports) della [console Cloud Billing](https://console.cloud.google.com/billing?hl=it). Nota
che puoi gestire il saldo del credito prepagato solo in AI Studio.

### Perché il mio utilizzo dell'API Gemini non viene visualizzato in Cloud Billing Console, mentre posso vederlo in AI Studio Billing, insieme al consumo dei miei crediti?

Google Cloud e AI Studio segnalano i dati di utilizzo a Cloud Billing a intervalli
variabili. A causa della complessità dei nostri sistemi di fatturazione ed elaborazione, potresti
riscontrare un ritardo tra l'utilizzo dei servizi e la visualizzazione dell'utilizzo e dei costi
in Cloud Billing. In genere, i dettagli dei costi sono disponibili
entro un giorno, ma a volte possono essere necessarie più di 24 ore.
Scopri di più sulla fatturazione posticipata nella [documentazione di Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=it#delayed-billing).

### Se utilizzo altri servizi Google Cloud con costi soggetti a un ciclo di addebito postpagato, cosa succede se non effettuo un pagamento?

Il mancato pagamento di altri servizi Google Cloud può sospendere l'accesso all'API Gemini in AI Studio, **indipendentemente dal numero di crediti prepagati disponibili**. L'utilizzo di AI Studio è alimentato da un account di fatturazione Google Cloud, che
può condividere sia la fatturazione prepagata per AI Studio sia la fatturazione postpagata per altri servizi
cloud. Un problema con il saldo Postepay interrompe tutti i servizi collegati a questo
account. L'utilizzo dell'API Gemini verrà sospeso se il tuo account di fatturazione Cloud
viene segnalato per problemi quali:

- Un saldo insoluto o scaduto
- Un pagamento rifiutato
- Un metodo di pagamento non valido o scaduto

Per ripristinare il servizio, devi [risolvere il problema dell'account postpagato](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=it#resolving-declined-payments)
nella console Google Cloud Billing. Una volta risolto il problema, riavrai
accesso ai tuoi servizi e crediti prepagati dell'API Gemini.

### Dove posso ricevere assistenza per la fatturazione?

Per ricevere assistenza in merito alla fatturazione, consulta la pagina
[Richiedi assistenza per la fatturazione Cloud](https://cloud.google.com/support/billing?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-06-23 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-06-23 UTC."],[],[]]
