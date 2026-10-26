---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=it
fetched_at: 2026-10-26T05:45:21.895653+00:00
title: "Utilizzo delle chiavi API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Utilizzo delle chiavi API Gemini

Per utilizzare l'API Gemini, devi autenticare le tue richieste. Puoi autenticarti utilizzando una chiave API standard o di autorizzazione.

[Creare o visualizzare una chiave API Gemini](https://aistudio.google.com/apikey?hl=it)

## Tipi di chiavi API: standard e autorizzazione

Le chiavi API forniscono l'accesso all'API Gemini, ma le loro caratteristiche di sicurezza
sono diverse. L'API Gemini sta passando dalle chiavi API standard alle chiavi di autorizzazione
per migliorare la sicurezza:

- **Chiavi API standard**: associa le richieste a un progetto Google Cloud ai fini di fatturazione e quota. Le chiavi standard non identificano un chiamante, il che
  limita la granularità delle autorizzazioni e del controllo dell'accesso che possono supportare.
- **Chiavi di autorizzazione**: associate direttamente a un service account Google Cloud. Quando utilizzi una chiave di autorizzazione, le tue richieste vengono elaborate
  con l'identità del service account associato, consentendo un controllo
  dell'accesso granulare. Per impostazione predefinita, le chiavi di autorizzazione sono limitate all'API Generative Language (API Gemini) e forniscono un'applicazione rapida delle chiavi compromesse che interrompe rapidamente l'utilizzo delle chiavi compromesse rilevate dai nostri sistemi.

Per garantire un utilizzo sicuro, l'API Gemini passerà dalle chiavi standard alle chiavi di autenticazione:

- **Chiavi di autenticazione predefinite**: a partire dal 28 maggio 2026, tutte le nuove chiavi API create in
  Google AI Studio vengono create automaticamente come chiavi di autenticazione.
- **Chiavi senza restrizioni rifiutate**: l'API Gemini rifiuta le richieste
  dalle **chiavi standard senza restrizioni**. Le chiavi API standard a cui sono state applicate
  restrizioni esplicite continuano a funzionare. Questa limitazione impedisce l'uso non autorizzato di chiavi che potrebbero essere condivise pubblicamente o collegate ad altri servizi.

## Gestione delle chiavi API in Google AI Studio

Puoi gestire i tuoi progetti e le tue chiavi direttamente in [Google AI Studio](https://aistudio.google.com/apikey?hl=it).

### Progetti Google Cloud

Ogni chiave API Gemini è associata a un [progetto Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=it).
I progetti Google Cloud gestiscono la fatturazione, i collaboratori e le autorizzazioni. Google AI Studio fornisce un'interfaccia leggera per accedere a questi progetti.

- **Progetto predefinito**: se sei un nuovo utente, Google AI Studio crea automaticamente
  un progetto Google Cloud e una chiave API predefiniti dopo che hai accettato i
  Termini di servizio. Puoi rinominare questo progetto andando alla visualizzazione
  **Progetti** nella dashboard.
- **Progetti esistenti**: se hai già un account Google Cloud, AI
  Studio non crea un progetto predefinito. Devi invece importare i tuoi
  progetti esistenti.

### Importazione dei progetti

Per impostazione predefinita, Google AI Studio non mostra tutti i tuoi progetti Google Cloud. Devi importare i progetti che vuoi utilizzare:

1. Vai a [Google AI Studio](https://aistudio.google.com?hl=it).
2. Apri la **dashboard** dal riquadro a sinistra e seleziona **Progetti**.
3. Fai clic sul pulsante **Importa progetti**.
4. Cerca e seleziona il progetto Google Cloud da importare, poi
   fai clic su **Importa**.
5. Una volta importato, vai alla pagina **Chiavi API** nella dashboard per
   creare una chiave nel progetto.

### Risoluzione dei problemi relativi alle autorizzazioni di creazione delle chiavi

Se il pulsante **Crea chiave API** non è disponibile e viene visualizzato il messaggio:
*"Non hai l'autorizzazione per creare una chiave in questo progetto"*, non disponi delle autorizzazioni IAM richieste.

Chiedi all'amministratore del progetto o dell'organizzazione Google Cloud di concederti un ruolo
che contenga le seguenti autorizzazioni (ad esempio Editor progetto):

- `resourcemanager.projects.get`: consente ad AI Studio di verificare il progetto.
- `apikeys.keys.create`: Consente la generazione di chiavi.
- `serviceusage.services.enable`: garantisce che l'API Generative Language sia
  abilitata.
- `iam.serviceAccounts.create`: obbligatorio per creare il service account collegato.
- `iam.serviceAccountApiKeyBindings.create`: associa il service account alla chiave API.

Se non riesci a ottenere l'accesso amministrativo, puoi creare un nuovo progetto Google Cloud
non associato a un'organizzazione per generare le chiavi.

## Creazione di chiavi nella console Google Cloud

Google AI Studio mostra solo le chiavi senza limitazioni o limitate all'API
Gemini. Se non puoi utilizzare AI Studio o vuoi gestire tutte le tue chiavi API in un unico posto, segui la documentazione di Cloud sulla [creazione di una chiave API](https://cloud.google.com/docs/authentication/api-keys?hl=it#create). La creazione di una chiave API Gemini richiede l'associazione a un [service account](https://cloud.google.com/iam/docs/service-account-overview?hl=it).

## Configurazione dell'ambiente

Una volta ottenuta una chiave, configura l'ambiente per utilizzarla in modo sicuro nelle tue
applicazioni.

### Opzione 1: utilizza le variabili di ambiente (consigliata)

Imposta la variabile di ambiente `GEMINI_API_KEY` o `GOOGLE_API_KEY`. Le librerie client dell'API Gemini rilevano e utilizzano automaticamente queste variabili. Se vengono impostati entrambi, `GOOGLE_API_KEY` ha la precedenza.

Seleziona il tuo sistema operativo per impostare la variabile:

### Linux/macOS - Bash

Verifica se hai un file di configurazione bash:

```
~/.bashrc
```

In caso contrario, creane uno e aprilo:

```
touch ~/.bashrc && open ~/.bashrc
```

Aggiungi il comando di esportazione alla fine del file:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Salva il file, poi applica le modifiche:

```
source ~/.bashrc
```

### macOS - Zsh

Verifica di avere un file di configurazione zsh:

```
~/.zshrc
```

In caso contrario, creane uno e aprilo:

```
touch ~/.zshrc && open ~/.zshrc
```

Aggiungi il comando di esportazione:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Salva il file, poi applica le modifiche:

```
source ~/.zshrc
```

### Windows

1. Cerca "Variabili di ambiente" nella barra di ricerca di Windows.
2. Fai clic su **Variabili di ambiente** nella finestra di dialogo Proprietà del sistema.
3. In **Variabili utente** o **Variabili di sistema**, fai clic su **Nuova…**.
4. Imposta il nome della variabile su `GEMINI_API_KEY` e il valore sulla tua chiave API.
5. Fai clic su **OK** per salvarlo. Apri una nuova sessione del terminale per caricare la variabile.

### Opzione 2: fornisci la chiave API in modo esplicito nel codice

Puoi passare la chiave API in modo esplicito durante l'inizializzazione del client. Esegui questa operazione
solo se non puoi utilizzare le variabili di ambiente.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.output_text);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = Client.builder().apiKey("YOUR_API_KEY").build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few sentences."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey: "YOUR_API_KEY",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Explain how AI works in a few sentences."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## Gestione della sicurezza e dei secret

Tratta la chiave API Gemini come una password. Se viene compromesso, altri possono consumare
la quota del tuo progetto, incorrere in addebiti di fatturazione imprevisti e accedere a risorse
private.

### Regole di sicurezza critiche

- **Mantieni riservate le chiavi**: non archiviare mai le chiavi API nei sistemi di controllo del codice sorgente
  come Git.
- **Non esporre mai le chiavi lato client in produzione**: non codificare le chiavi API
  direttamente nelle app web o mobile. Le chiavi compilate nel codice lato client possono essere
  estratte dagli utenti. Per proteggere le app lato client, esegui un server proxy di backend per effettuare le chiamate API effettive.

### Best practice per la gestione dei secret

- **Variabili di ambiente**: leggi le chiavi dalle variabili di ambiente anziché dai file di configurazione.
- **Secret Manager**: per la produzione, archivia le chiavi in un archivio dei secret sicuro
  come [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=it).
- **Avvisi di fatturazione**: configura gli avvisi di fatturazione nella console Google Cloud per
  ricevere una notifica in caso di picchi di utilizzo o costi.

### Elenco di controllo per la risposta alle perdite di dati

Se sospetti che la tua chiave API sia stata compromessa:

1. **Genera una nuova chiave**: crea una chiave sostitutiva in Google AI Studio o nella
   console Google Cloud.
2. **Aggiorna l'applicazione**: esegui il deployment del codice utilizzando la nuova chiave.
3. **Disattiva o elimina la chiave compromessa**: disattiva la chiave compromessa nella
   console Cloud una volta verificata la nuova chiave. Non eliminare la vecchia chiave finché
   la nuova chiave non è completamente attiva per evitare tempi di inattività dell'applicazione.
4. **Controlla l'utilizzo**: controlla i log di fatturazione e l'utilizzo delle API nella console Google Cloud per identificare attività non autorizzate.

## Limitare e proteggere le chiavi

L'aggiunta di limitazioni alle chiavi API riduce al minimo i potenziali danni in caso di compromissione di una chiave.

### Applica limitazioni all'origine della richiesta

Le limitazioni di origine limitano gli indirizzi IP, i siti web o le applicazioni che possono utilizzare la tua chiave.

1. Vai alla [pagina delle credenziali della console Google Cloud](https://console.cloud.google.com/apis/credentials?hl=it).
2. Seleziona il tuo progetto e fai clic sul nome della chiave API che vuoi limitare.
3. In **Restrizioni delle applicazioni**, seleziona **Indirizzi IP** (o il tipo di restrizione appropriato per il tuo ambiente).
4. Specifica gli indirizzi IP o gli intervalli consentiti, quindi fai clic su **Salva**.

### Protezione delle chiavi API standard senza limitazioni

Per continuare a utilizzare l'API Gemini, devi proteggere le chiavi senza limitazioni.

#### Metodo A: limita la chiave solo all'API Gemini (AI Studio)

Se utilizzi la chiave solo per l'API Gemini, proteggila direttamente in AI Studio:

1. Nella pagina **Chiavi API** di [Google AI Studio](https://aistudio.google.com/api-keys?hl=it), individua le chiavi contrassegnate con l'etichetta
   **Senza limitazioni**.
2. Passa il mouse sopra l'etichetta e fai clic su **Aggiungi limitazioni** nella finestra di dialogo.
3. Seleziona **Limita solo all'API Gemini**.
4. Fai clic su **Limita chiave** per confermare.

#### Metodo B: limita la chiave per altri servizi (console Google Cloud)

Se la chiave è condivisa con altre API di Google (non consigliato), limitane l'utilizzo nella console Cloud. **Nota: le richieste dell'API Gemini che utilizzano questa chiave non andranno a buon fine dopo l'applicazione di queste limitazioni.**

1. Visita la [pagina delle credenziali della console Google Cloud](https://console.cloud.google.com/apis/credentials?hl=it).
2. Seleziona il progetto e la chiave API.
3. In **Restrizioni delle API**, utilizza il menu a discesa **Seleziona limitazioni dell'API** per
   selezionare le API a cui vuoi che questa chiave acceda. Non selezionare l'**API
   Generative Language**.
4. Fai clic su **Salva**. Crea una chiave separata con limitazioni in AI Studio per continuare
   a utilizzare l'API Gemini.

### Chiavi inattive bloccate

A partire dal 7 maggio 2026, l'API Gemini blocca le chiavi API senza limitazioni che sono
rimaste inattive per un periodo prolungato. Queste chiavi mostrano un tag **Bloccata** in AI
Studio. Per continuare, devi generare una nuova chiave o utilizzare una chiave con limitazioni esistente.

## Esegui la migrazione a una chiave di autenticazione

Per creare una nuova chiave API di autenticazione e aggiornare le tue applicazioni:

1. Vai alla [pagina delle chiavi API di AI Studio](https://aistudio.google.com/api-keys?hl=it).
2. Controlla la colonna **Tipo di chiave** per identificare le chiavi elencate come **Standard**.
3. Fai clic su **Crea chiave API** per generare una nuova chiave. Tutte le nuove chiavi create in
   AI Studio vengono create automaticamente come chiavi di autenticazione.
4. Copia la nuova chiave API di autenticazione.
5. Aggiorna il codice dell'applicazione, le variabili di ambiente e qualsiasi configurazione di deployment
   per utilizzare la nuova chiave API di autenticazione.
6. Testa l'applicazione per verificare che funzioni correttamente con la nuova chiave.
7. Una volta verificata, elimina o revoca la vecchia chiave del traffico per evitare abusi.

## Limitazioni

Google AI Studio impone le seguenti limitazioni alla gestione di progetti e chiavi:

- Puoi creare un massimo di 10 progetti alla volta dalla pagina **Progetti** di Google AI Studio.
- Le pagine **Chiavi API** e **Progetti** mostrano un massimo di 100 chiavi e 50
  progetti.
- Vengono visualizzate solo le chiavi API senza limitazioni o limitate specificamente all'API Generative Language (API Gemini).

Per la gestione avanzata dei progetti o per modificare le chiavi con altre limitazioni, utilizza
la [pagina delle credenziali della console Google Cloud](https://console.cloud.google.com/apis/credentials?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-10-06 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-10-06 UTC."],[],[]]
