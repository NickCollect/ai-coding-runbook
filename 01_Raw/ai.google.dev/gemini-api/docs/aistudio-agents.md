---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=it
fetched_at: 2026-06-29T05:39:22.677592+00:00
title: "Agent in AI Studio Playground \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Agent in AI Studio Playground

Google AI Studio Playground fornisce un'interfaccia visiva per creare prototipi e imparare a creare agenti gestiti senza dover creare e scrivere chiamate API.

Per iniziare, vai alla scheda **Playground** nel pannello di navigazione di Google AI Studio e attiva/disattiva l'opzione **Agenti**.

## Modelli predefiniti

La scheda **Agenti** contiene una serie di modelli che preconfigurano l'agente Antigravity di base impostando le configurazioni di strumenti e ambiente. Tutti i modelli sono open source e pubblicati nel
repository [google-gemini/gemini-managed-agents-templates](https://github.com/google-gemini/gemini-managed-agents-templates/). Esplorare questi modelli è un ottimo modo per imparare a creare e strutturare il tuo agente gestito.

Ad esempio, quando scegli il modello AI Radio, vengono abilitati tutti gli strumenti consentiti e viene collegato un file `AGENTS.md` specializzato e le competenze per la produzione di programmi radiofonici. Puoi visualizzare queste impostazioni nell'interfaccia utente di Playground nella sezione **Ambiente** facendo clic sul pulsante **Origini**.

## Configurazione dello strumento

Nelle impostazioni dell'agente in Playground, puoi attivare/disattivare l'accesso ai seguenti strumenti integrati:

- **Ricerca Google**:accedi al web aperto per informazioni in tempo reale.
- **Contesto URL**:recupera e analizza il contenuto testuale di URL di pagine web specifiche.
- **Esecuzione del codice**:esegui comandi Bash e Python direttamente nell'ambiente sandbox isolato.
- **Strumenti del file system**:leggi, scrivi, elenca ed elimina i file all'interno dell'area di lavoro.

## Configurazione dell'ambiente

Gli agenti gestiti vengono eseguiti in una sandbox Linux effimera e sicura (l'ambiente) che fornisce l'area di lavoro e gli strumenti necessari per il loro funzionamento. Per saperne di più, consulta la guida all'ambiente degli agenti gestiti [managed agent environment](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it).

### Controllo del comportamento dell'agente

Il comportamento, la personalità e le funzionalità dell'agente sono determinati principalmente dai file presenti nel suo ambiente. L'agente rileva e carica automaticamente le configurazioni da una cartella `.agents` speciale:

- **`AGENTS.md`**: precaricato nel contesto dell'agente per definire le istruzioni di sistema e la personalità.
- **`SKILL.md`**: si trova nelle rispettive cartelle delle competenze (ad es. `.agents/skills/my-skill/SKILL.md`) per definire funzionalità e workflow specifici.

### Provisioning dell'ambiente

Puoi configurare l'ambiente da utilizzare dall'agente montando i file nell'ambiente prima di avviare una sessione. Puoi creare un nuovo ambiente montando le origini o ripristinarne uno precedente:

- **Per creare un nuovo ambiente**, fai clic su **Aggiungi origini** nel riquadro delle impostazioni dell'ambiente e scegli tra i seguenti tipi di origine:

| Tipo di origine | Descrizione | Percorso di montaggio |
| --- | --- | --- |
| **File in linea** | Scrivi o incolla file di configurazione, set di dati simulati o script di utilità (fino a 100 KB) direttamente nell'interfaccia utente di Playground. | Percorso di destinazione definito dall'utente (ad es. `/workspace/scripts/parser.py`). |
| **Google Cloud Storage** | Monta un bucket Cloud Storage pubblico o privato.  I bucket privati richiedono un token di supporto OAuth 2.0 standard. Per saperne di più, consulta [Origini private](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it#private-sources). | Mappa un percorso del bucket GCS (ad es. `gs://your-bucket-name/data/`) a una directory dell'area di lavoro (ad es. `/workspace/data/`). |
| **Repository GitHub** | Clona codebase pubblici o privati.  I repository privati richiedono l'autenticazione di base con il token di accesso personale (PAT) di GitHub. Per saperne di più, consulta [Origini private](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it#private-sources). | Clonato direttamente in `/workspace/` (in genere in `/workspace/<repo-name>`). |

- **Per ripristinare un ambiente precedente**, puoi [riutilizzare un ID ambiente esistente](#reusing-an-existing-environment-id) per clonare e creare una copia esatta del suo stato.

### Riutilizzo di un ID ambiente esistente

Se hai già dedicato del tempo alla configurazione di un ambiente sandbox, non devi ricominciare da zero. Per utilizzare un ambiente esistente:

1. Vai al riquadro Ambienti in AI Studio e imposta **Tipo** su **Esistente**.
2. Inserisci l'**ID ambiente** (ad es. `env_abc123`)

Per saperne di più, consulta [Configurare un ambiente](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it#configure-an-environment). Puoi anche recuperare l'ID ambiente della sessione corrente dalla scheda Ambiente nell'interfaccia utente.

Una volta inviato il primo messaggio all'agente, la configurazione dell'ambiente diventa fissa per quella sessione. Non puoi montare nuove origini o modificare la lista consentita di rete mentre l'interazione è in esecuzione.

## Scarica l'ambiente

Una volta creato un ambiente, puoi scaricare lo snapshot dell'ambiente in qualsiasi momento utilizzando il pulsante **Scarica** nelle impostazioni dell'ambiente di AI Studio Playground per recuperare i file dell'ambiente come file tar.

## Sicurezza e gestione dei costi

### Gestione del consumo di token

A differenza di una richiesta di chat standard che produce un singolo output, l'agente Antigravity esegue un workflow autonomo. Pianifica, esegue il codice, osserva i risultati e itera. Ciò significa che un singolo prompt può comportare un consumo illimitato di token.

Per gestire i costi, **fornisci criteri di terminazione chiari nei prompt e limita le attività dell'agente**. Un buon esempio potrebbe essere un prompt come *Esamina la richiesta di pull e interrompi l'operazione dopo aver generato il riepilogo in Markdown.
Non tentare di scrivere la correzione da solo*.

### Costi aggiuntivi

Per impostazione predefinita, tutti i modelli di agenti in Playground hanno accesso al servizio API Gemini e possono effettuare chiamate API dall'ambiente per soddisfare le richieste. Questi potrebbero comportare costi aggiuntivi che non verranno visualizzati nel consumo di token.

Allo stesso modo, se aggiungi altri servizi esterni, l'agente potrebbe comportare costi aggiuntivi chiamando questi servizi per tuo conto.

### Lista consentita di rete

Per impostazione predefinita, in AI Studio tutte le richieste di rete in uscita dall'ambiente sandbox dell'agente sono strettamente controllate e limitate per garantire la sicurezza. Per concedere all'agente la possibilità di raggiungere API esterne, servizi web o gestori di pacchetti, devi dichiararli esplicitamente:

1. Vai al riquadro Ambienti in AI Studio.
2. Seleziona il pulsante **Regole** accanto a **Rete**.
3. Nel riquadro **Configurazione di rete**, fai clic su **Aggiungi alla lista consentita** e inserisci i dettagli pertinenti:
   - **Limitazione del dominio**:solo i domini specifici o i pattern con caratteri jolly aggiunti all'elenco possono essere accessibili dalla macchina virtuale dell'agente. Ad esempio, puoi inserire domini esatti come `api.github.com` o pattern ampi come `*.googleapis.com`.
   - **Aggiungi intestazione HTTP e inserimento di token**:utilizza l'opzione **Aggiungi intestazione HTTP** per inserire in modo sicuro le credenziali richieste (ad esempio un token API) per un dominio specifico. Queste credenziali vengono trasmesse in modo sicuro tramite un proxy di uscita e non vengono mai esposte direttamente come testo non elaborato all'interno della sandbox dell'agente.

Presta sempre attenzione quando aggiungi domini alla lista consentita. Concedere all'agente l'accesso ai servizi autenticati significa che può agire per tuo conto, il che potrebbe comportare azioni indesiderate se non viene monitorato attentamente.

### Best practice per le credenziali

Se il tuo workflow richiede che l'agente si autentichi con servizi esterni, è tua responsabilità eseguire il provisioning e definire l'ambito di queste credenziali. Segui queste linee guida per ridurre i rischi:

- **Utilizza credenziali con privilegi minimi**:crea account di servizio o chiavi API con solo le autorizzazioni di cui ha bisogno l'agente. Evita di passare credenziali con accesso amministrativo o ampio.
- **Preferisci i token di breve durata**:ove possibile, utilizza credenziali o token a tempo limitato che scadono anziché chiavi API di lunga durata.
- **Supponi l'accesso completo**:l'agente può utilizzare qualsiasi credenziale a cui ha accesso per completare l'attività che gli hai assegnato. Fornisci solo le credenziali di cui sei disposto a concedere l'ambito di accesso completo.
- **Ruota regolarmente le credenziali**:tratta le credenziali condivise con l'agente allo stesso modo di qualsiasi credenziale programmatica; ruotale a intervalli regolari.

### Connessione di strumenti e API esterni

Puoi connettere strumenti e API esterni (come i server Model Context Protocol / MCP) per estendere le funzionalità dell'agente. Quando lo fai:

- Collega solo gli strumenti provenienti da origini attendibili. Uno strumento dannoso o scritto male potrebbe esporre i dati o eseguire azioni indesiderate.
- Configura gli strumenti con le autorizzazioni minime richieste per il tuo caso d'uso. Se uno strumento supporta la modalità di sola lettura, preferiscila a meno che le scritture non siano strettamente necessarie.
- Prima di connettere uno strumento a un'origine dati di produzione, testalo con dati di esempio o sintetici per verificare che l'agente lo utilizzi come previsto.

### Supervisione umana

Gli agenti possono ragionare, pianificare ed eseguire workflow in più passaggi con un elevato grado di autonomia. Sebbene questa funzionalità sia potente, è necessario applicare una supervisione adeguata, soprattutto per le attività che modificano i dati o interagiscono con sistemi esterni.

Verifica sempre gli output critici, come il codice generato, le trasformazioni dei dati o le modifiche alla configurazione, prima di eseguirne il deployment.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-20 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-20 UTC."],[],[]]
