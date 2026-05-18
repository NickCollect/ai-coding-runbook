---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=it
fetched_at: 2026-05-18T05:13:40.088320+00:00
title: "Utilizzo delle chiavi API Gemini \u00a0|\u00a0 Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Utilizzo delle chiavi API Gemini

Per utilizzare l'API Gemini, devi avere una chiave API. Questa pagina descrive come creare e gestire le chiavi in Google AI Studio, nonché come configurare l'ambiente per utilizzarle nel codice.

[Creare o visualizzare una chiave API Gemini](https://aistudio.google.com/app/apikey?hl=it)

## Chiavi API

Puoi creare e gestire tutte le chiavi API Gemini dalla
[pagina Google AI Studio](https://aistudio.google.com/app/apikey?hl=it) **Chiavi API**.

Una volta ottenuta una chiave API, hai le seguenti opzioni per connetterti all'API Gemini:

- [Impostare la chiave API come variabile di ambiente](#set-api-env-var)
- [Fornire la chiave API in modo esplicito](#provide-api-key-explicitly)

Per i test iniziali, puoi codificare in modo rigido una chiave API, ma questa operazione deve essere solo temporanea perché non è sicura. Puoi trovare esempi di codifica rigida della chiave API
in [Fornire la chiave API in modo esplicito](#provide-api-key-explicitly) sezione.

## Progetti Google Cloud

[I progetti Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=it)
sono fondamentali per utilizzare i servizi Google Cloud (come l'API Gemini),
gestire la fatturazione e controllare collaboratori e autorizzazioni. Google AI Studio fornisce un'interfaccia leggera per i tuoi progetti Google Cloud.

Se non hai ancora creato progetti, devi crearne uno nuovo o importarne uno da Google Cloud in Google AI Studio. La pagina **Progetti** in Google AI Studio mostra tutte le chiavi che dispongono di autorizzazioni sufficienti per utilizzare l'API Gemini. Per istruzioni, consulta la sezione [Importare progetti](#import-projects).

### Progetto predefinito

Per i nuovi utenti, dopo aver accettato i Termini di servizio, Google AI Studio crea un progetto Google Cloud e una chiave API predefiniti per facilità d'uso. Puoi rinominare questo
progetto in Google AI Studio andando alla visualizzazione **Progetti** nella
**Dashboard**, facendo clic sul pulsante delle impostazioni con i tre puntini accanto a un progetto e
scegliendo **Rinomina progetto**. Gli utenti esistenti o gli utenti che hanno già Account Google Cloud non avranno un progetto predefinito creato.

## Importare progetti

Ogni chiave API Gemini è associata a un progetto cloud Google. Per impostazione predefinita, Google AI Studio non mostra tutti i tuoi progetti cloud. Devi importare i progetti che vuoi cercando il nome o l'ID progetto nella finestra di dialogo **Importa progetti**. Per visualizzare un elenco completo dei progetti a cui hai accesso, visita la console Cloud.

Se non hai ancora importato progetti cloud, segui questi passaggi per importare un progetto Google Cloud e creare una chiave:

1. Vai a [Google AI Studio](https://aistudio.google.com?hl=it).
2. Apri la **Dashboard** dal riquadro laterale sinistro.
3. Seleziona **Progetti**.
4. Seleziona il pulsante **Importa progetti** nella pagina **Progetti**.
5. Cerca e seleziona il progetto Google Cloud che vuoi importare e seleziona il pulsante **Importa**.

Una volta importato un progetto, vai alla pagina **Chiavi API** dal menu **Dashboard** e crea una chiave API nel progetto appena importato.

## Limitazioni

Di seguito sono riportate le limitazioni della gestione delle chiavi API e dei progetti Google Cloud in Google AI Studio.

- Puoi creare un massimo di 10 progetti alla volta dalla pagina **Progetti** di Google AI Studio.
- Puoi assegnare un nome e rinominare progetti e chiavi.
- Le pagine **Chiavi API** e **Progetti** mostrano un massimo di 100 chiavi e 50 progetti.
- Vengono visualizzate solo le chiavi API senza limitazioni o limitate all'API Generative Language.

Per un accesso di gestione aggiuntivo ai tuoi progetti, inclusa la modifica e la limitazione delle chiavi API, visita la
[pagina delle credenziali della console Google Cloud](https://console.cloud.google.com/apis/credentials?hl=it).
In Cloud Console, puoi selezionare il tuo progetto, fare clic su una chiave API esistente e poi limitarla all'**API Generative Language**.

## Impostare la chiave API come variabile di ambiente

Se imposti la variabile di ambiente `GEMINI_API_KEY` o `GOOGLE_API_KEY`, la
chiave API verrà selezionata automaticamente dal client quando utilizzi una delle
[librerie dell'API Gemini](https://ai.google.dev/gemini-api/docs/libraries?hl=it). Ti consigliamo di impostare solo una di queste variabili, ma se sono impostate entrambe, `GOOGLE_API_KEY` ha la precedenza.

Se utilizzi l'API REST o JavaScript nel browser, dovrai fornire la chiave API in modo esplicito.

Ecco come impostare la chiave API localmente come variabile di ambiente `GEMINI_API_KEY` con diversi sistemi operativi.

### Linux/macOS - Bash

Bash è una configurazione comune del terminale Linux e macOS. Puoi verificare se hai un file di configurazione eseguendo il seguente comando:

```
~/.bashrc
```

Se la risposta è "No such file or directory", dovrai creare questo file e aprirlo eseguendo i seguenti comandi oppure utilizzare `zsh`:

```
touch ~/.bashrc
open ~/.bashrc
```

Il prossimo passo è impostare la chiave API aggiungendo il seguente comando di esportazione:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Dopo aver salvato il file, applica le modifiche eseguendo:

```
source ~/.bashrc
```

### macOS - Zsh

Zsh è una configurazione comune del terminale Linux e macOS. Puoi verificare se hai un file di configurazione eseguendo il seguente comando:

```
~/.zshrc
```

Se la risposta è "No such file or directory", dovrai creare questo file e aprirlo eseguendo i seguenti comandi oppure utilizzare `bash`:

```
touch ~/.zshrc
open ~/.zshrc
```

Il prossimo passo è impostare la chiave API aggiungendo il seguente comando di esportazione:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Dopo aver salvato il file, applica le modifiche eseguendo:

```
source ~/.zshrc
```

### Windows

1. Cerca "Variabili di ambiente" nella barra di ricerca.
2. Scegli di modificare le **Impostazioni di sistema**. Potresti dover confermare di voler eseguire questa operazione.
3. Nella finestra di dialogo delle impostazioni di sistema, fai clic sul pulsante **Variabili di ambiente**.
4. In **Variabili utente** (per l'utente corrente) o **Variabili di sistema** (si applica a tutti gli utenti che utilizzano la macchina), fai clic su **Nuova…**
5. Specifica il nome della variabile come `GEMINI_API_KEY`. Specifica la chiave API Gemini come valore della variabile.
6. Fai clic su **Ok** per applicare le modifiche.
7. Apri una nuova sessione del terminale (cmd o PowerShell) per ottenere la nuova variabile.

## Fornire la chiave API in modo esplicito

In alcuni casi, potresti voler fornire una chiave API in modo esplicito. Ad esempio:

- Stai eseguendo una semplice chiamata API e preferisci codificare in modo rigido la chiave API.
- Vuoi un controllo esplicito senza dover fare affidamento sulla rilevazione automatica delle variabili di ambiente da parte delle librerie dell'API Gemini.
- Stai utilizzando un ambiente in cui le variabili di ambiente non sono supportate (ad es.web) o stai effettuando chiamate REST.

Di seguito sono riportati esempi di come fornire una chiave API in modo esplicito:

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Vai

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  "YOUR_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## Proteggere la chiave API

Tratta la chiave API Gemini come una password. Se viene compromessa, altri utenti possono utilizzare la quota del tuo progetto, addebitare costi (se la fatturazione è abilitata) e accedere ai tuoi dati privati, ad esempio ai file.

### Regole di sicurezza critiche

- **Mantieni riservate le chiavi**: le chiavi API per Gemini potrebbero accedere a dati sensibili da cui dipende la tua
  applicazione.

  - **Non eseguire mai il commit delle chiavi API nel controllo del codice sorgente.** Non eseguire il check-in della chiave API nei sistemi di controllo della versione come Git.
  - **Non esporre mai le chiavi API lato client.** Non utilizzare la chiave API direttamente nelle app web o mobile in produzione. Le chiavi nel codice lato client (incluse le nostre librerie JavaScript/TypeScript e le chiamate REST) possono essere estratte.
- **Limita l'accesso**: limita l'utilizzo della chiave API a indirizzi IP, referrer HTTP
  o app Android/iOS specifici, ove possibile.
- **Limita l'utilizzo**: abilita solo le API necessarie per ogni chiave.
- **Esegui audit regolari**: esegui regolarmente l'audit delle chiavi API e ruotale
  periodicamente.

### Best practice

- **Utilizza chiamate lato server con le chiavi API** Il modo più sicuro per utilizzare la chiave API è chiamare l'API Gemini da un'applicazione lato server in cui la chiave può essere mantenuta riservata.
- **Utilizza token effimeri per l'accesso lato client (solo API Live):** per l'accesso diretto lato client all'API Live, puoi utilizzare token effimeri. Comportano rischi per la sicurezza inferiori e possono essere adatti all'utilizzo in produzione. Per saperne di più, consulta la guida ai
  [token effimeri](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=it).
- **Valuta la possibilità di aggiungere limitazioni alla chiave:** puoi limitare le autorizzazioni di una chiave
  aggiungendo [limitazioni alle chiavi API](https://cloud.google.com/api-keys/docs/add-restrictions-api-keys?hl=it#add-api-restrictions).
  In questo modo si riducono al minimo i potenziali danni in caso di perdita della chiave.

Per alcune best practice generali, puoi anche consultare questo
[articolo di assistenza](https://support.google.com/googleapi/answer/6310037?hl=it).

## Proteggere le chiavi API senza limitazioni

Le chiavi API senza limitazioni sono vulnerabili ad attori malintenzionati e a un utilizzo non autorizzato. A partire dal 19 giugno 2026, per migliorare la sicurezza, l'API Gemini non supporterà più le chiavi di traffico senza limitazioni.

**Ciò significa che le richieste dell'API Gemini non andranno a buon fine se non intraprendi alcuna azione.**

Per continuare a utilizzare l'API Gemini senza interruzioni, proteggi le chiavi di traffico
aggiungendo limitazioni in
[AI Studio](https://aistudio.google.com/api-keys?hl=it).

In [aistudio.google.com/api-keys](https://aistudio.google.com/api-keys?hl=it), vedrai un banner che ti avviserà quando le chiavi API non sono soggette a limitazioni. Puoi vedere quali chiavi non sono soggette a limitazioni e l'utilizzo del servizio negli ultimi 90 giorni.

Per le chiavi senza limitazioni, devi scegliere una delle seguenti opzioni:

- Utilizzare la chiave solo per l'API Gemini.
- Utilizzare la chiave per l'utilizzo di API non Gemini.

### Limitare la chiave solo all'API Gemini

Se vuoi limitare la chiave solo all'API Gemini, proteggila in
[AI Studio](https://aistudio.google.com/api-keys?hl=it) facendo clic sul pulsante
**Limita all'API Gemini**.

### Limitare la chiave per l'utilizzo di API non Gemini

Se vuoi limitare la chiave per l'utilizzo di API non Gemini:

1. Visita la
   [pagina delle credenziali della console Google Cloud](https://console.cloud.google.com/apis/credentials?hl=it).
2. Assicurati che il progetto sia selezionato correttamente.
3. Seleziona una chiave API.
4. Espandi il menu a discesa **Limitazioni API** e applica le limitazioni del servizio alla chiave API.

Se vuoi modificare le chiavi con limitazioni esistenti o appena aggiunte, visita
the
[console Google Cloud](https://console.cloud.google.com/apis/credentials?hl=it).

## Chiavi bloccate

A partire dal 7 maggio 2026, l'API Gemini bloccherà le chiavi API senza limitazioni che sono inattive da un periodo di tempo prolungato. Questi utenti vedranno un tag
**Bloccato** per la loro chiave su
[aistudio.google.com/api-keys](https://aistudio.google.com/api-keys?hl=it) e
dovranno generare una nuova chiave o utilizzare una chiave limitata alternativa per continuare a utilizzare l'API Gemini.

## Risoluzione dei problemi relativi alla creazione della chiave API

In Google AI Studio, il pulsante **Crea chiave API** potrebbe non essere disponibile e visualizzare
il messaggio: "*Non hai l'autorizzazione per creare una chiave in questo progetto*".

Questo problema si verifica quando non disponi delle autorizzazioni necessarie all'interno del progetto per generare una nuova chiave:

- **`resourcemanager.projects.get`**: consente ad AI Studio di verificare l'esistenza del progetto.
- **`apikeys.keys.create`**: consente la generazione della chiave API stessa.
- **`serviceusage.services.enable`**: è necessario per assicurarsi che l'API Gemini sia attiva nel progetto.

Per correggere le autorizzazioni, chiedi all'amministratore del progetto o all'amministratore dell'organizzazione, se il progetto appartiene a un'[organizzazione](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access?hl=it), di assegnarti un ruolo con le autorizzazioni elencate sopra (ad esempio Editor progetto o un ruolo personalizzato).

Se non disponi dell'accesso amministrativo a un progetto, puoi creare un nuovo progetto non associato a un'organizzazione per generare le chiavi.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-12 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-12 UTC."],[],[]]
