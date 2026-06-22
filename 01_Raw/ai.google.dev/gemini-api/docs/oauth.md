---
source_url: https://ai.google.dev/gemini-api/docs/oauth?hl=it
fetched_at: 2026-06-22T06:32:59.304593+00:00
title: "Guida rapida all'autenticazione con OAuth \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Guida rapida all'autenticazione con OAuth

Il modo più semplice per autenticare l'API Gemini è configurare una chiave API, come
descritto nella [guida rapida dell'API Gemini](https://ai.google.dev/gemini-api/docs/quickstart?hl=it). Se hai bisogno di controlli di accesso più rigorosi, puoi utilizzare OAuth. Questa guida ti aiuterà a configurare l'autenticazione con OAuth.

Questa guida utilizza un approccio di autenticazione semplificato, adatto a un ambiente di test. Per un ambiente di produzione, scopri di più
sull'
[autenticazione e sull'autorizzazione](https://developers.google.com/workspace/guides/auth-overview?hl=it)
prima
[di scegliere le credenziali di accesso](https://developers.google.com/workspace/guides/create-credentials?hl=it#choose_the_access_credential_that_is_right_for_you)
appropriate per la tua app.

## Obiettivi

- Configurare il progetto cloud per OAuth
- Configurare le credenziali predefinite dell'applicazione
- Gestire le credenziali nel programma anziché utilizzare `gcloud auth`

## Prerequisiti

Per eseguire questa guida rapida, devi disporre di:

- [Un progetto cloud di Google](https://developers.google.com/workspace/guides/create-project?hl=it)
- [Un'installazione locale di gcloud CLI](https://cloud.google.com/sdk/docs/install?hl=it)

## Configurare il progetto cloud

Per completare questa guida rapida, devi prima configurare il progetto cloud.

### 1. Abilita l'API

Prima di utilizzare le API di Google, devi attivarle in un progetto Google Cloud.

- Nella console Google Cloud, abilita l'API Generative Language di Google.

  [Abilita l'API](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=it)

### 2. Configura la schermata per il consenso OAuth

Poi configura la schermata per il consenso OAuth del progetto e aggiungiti come utente di test. Se hai già completato questo passaggio per il tuo progetto cloud, vai alla sezione successiva.

1. Nella console Google Cloud, vai a **Menu** > **Piattaforma di autenticazione Google** > **Panoramica**.

   [Vai alla piattaforma di autenticazione Google](https://console.developers.google.com/auth/overview?hl=it)
2. Compila il modulo di configurazione del progetto e imposta il tipo di utente su **Esterno** nella sezione **Pubblico**.
3. Compila la parte restante del modulo, accetta i termini delle Norme relative ai dati utente e poi fai clic su **Crea**.
4. Per il momento, puoi saltare l'aggiunta di ambiti e fare clic su **Salva e continua**. In futuro, quando crei un'app da utilizzare al di fuori della tua organizzazione Google Workspace, devi aggiungere e verificare gli ambiti di autorizzazione richiesti dalla tua app.
5. Aggiungi utenti di test:

   1. Vai alla
      [pagina Pubblico](https://console.developers.google.com/auth/audience?hl=it) della
      piattaforma di autenticazione Google.
   2. In **Utenti di test**, fai clic su **Aggiungi utenti**.
   3. Inserisci il tuo indirizzo email e gli indirizzi email di eventuali altri utenti di test autorizzati, quindi fai clic su **Salva**.

### 3. Autorizza le credenziali per un'applicazione desktop

Per eseguire l'autenticazione come utente finale e accedere ai dati utente nella tua app, devi creare uno o più ID client OAuth 2.0. L'ID client viene utilizzato per identificare una singola app nei server OAuth di Google. Se l'app viene eseguita su più piattaforme, devi creare un ID client separato per ogni piattaforma.

1. Nella console Google Cloud, vai a **Menu** > **Piattaforma di autenticazione Google** > **Client**.

   [Vai a credenziali](https://console.developers.google.com/auth/clients?hl=it)
2. Fai clic su **Crea client**.
3. Fai clic su **Tipo di applicazione** > **App desktop**.
4. Nel campo **Nome**, digita un nome per la credenziale. Questo nome viene visualizzato solo nella console Google Cloud.
5. Fai clic su **Crea**. Viene visualizzata la schermata Client OAuth creato, che mostra il nuovo ID client e il nuovo client secret.
6. Fai clic su **OK**. La credenziale appena creata viene visualizzata in **ID client OAuth 2.0**.
7. Fai clic sul pulsante di download per salvare il file JSON. Verrà salvato come
   `client_secret_<identifier>.json`, rinominalo in `client_secret.json`
   e spostalo nella directory di lavoro.

## Configurare le credenziali predefinite dell'applicazione

Per convertire il file `client_secret.json` in credenziali utilizzabili, passa la sua posizione all'argomento `--client-id-file` del comando `gcloud auth application-default login`.

```
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
```

La configurazione semplificata del progetto in questo tutorial attiva una finestra di dialogo **"Google non ha
verificato questa app"**. È normale, scegli **"Continua"**.

In questo modo, il token risultante viene inserito in una posizione nota, in modo che possa essere accessibile da `gcloud` o dalle librerie client.

```` ```
gcloud auth application-default login   

    --no-browser
    --client-id-file=client_secret.json   

    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
``` ````

Una volta configurate le credenziali predefinite dell'applicazione (ADC), le librerie client nella maggior parte delle lingue non hanno bisogno di aiuto per trovarle.

### Curl

Il modo più rapido per verificare che funzioni è utilizzarlo per accedere all'API REST utilizzando curl:

```
access_token=$(gcloud auth application-default print-access-token)
project_id=<MY PROJECT ID>
curl -X GET https://generativelanguage.googleapis.com/v1/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep '"name"'
```

### Python

In Python, le librerie client dovrebbero trovarle automaticamente:

```
pip install google-genai
```

Uno script minimo per testarlo potrebbe essere:

```
from google import genai

client = genai.Client()
print('Available base models:', [m.name for m in client.models.list()])
```

## Passaggi successivi

Se funziona, puoi provare
[il recupero semantico sui dati di testo](https://ai.google.dev/docs/semantic_retriever?hl=it).

## Gestire le credenziali autonomamente [Python]

In molti casi, il comando `gcloud` non sarà disponibile per creare il token di accesso dall'ID client (`client_secret.json`). Google fornisce librerie in molte lingue per consentirti di gestire questo processo all'interno della tua app. Questa sezione illustra la procedura in Python. Nella documentazione dell'API Drive sono disponibili esempi equivalenti di questo tipo
di procedura per altre lingue.

### 1. Installa le librerie necessarie

Installa la libreria client di Google per Python e la libreria client Gemini.

```
pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-genai
```

### 2. Scrivi il gestore delle credenziali

Per ridurre al minimo il numero di volte in cui devi fare clic sulle schermate di autorizzazione, crea un file denominato `load_creds.py` nella directory di lavoro per memorizzare nella cache un file `token.json` che può essere riutilizzato in un secondo momento o aggiornato se scade.

Inizia con il seguente codice per convertire il file `client_secret.json` in un token utilizzabile con `genai.configure`:

```
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/generative-language.retriever']

def load_creds():
    """Converts `client_secret.json` to a credential object.

    This function caches the generated tokens to minimize the use of the
    consent screen.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds
```

### 3. Scrivi il programma

Ora crea `script.py`:

```
import pprint
from google import genai
from load_creds import load_creds

creds = load_creds()

client = genai.Client(credentials=creds)

print()
print('Available base models:', [m.name for m in client.models.list()])
```

### 4. Esegui il programma

Nella directory di lavoro, esegui l'esempio:

```
python script.py
```

La prima volta che esegui lo script, si apre una finestra del browser e ti viene chiesto di autorizzare l'accesso.

1. Se non hai ancora eseguito l'accesso al tuo Account Google, ti verrà chiesto di farlo. Se hai eseguito l'accesso a più account, **assicurati di selezionare l'account che hai impostato come "Account di test" durante la configurazione del progetto**.
2. Le informazioni di autorizzazione vengono archiviate nel file system, quindi la volta successiva che esegui il codice campione non ti verrà richiesta l'autorizzazione.

Hai configurato correttamente l'autenticazione.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-06-19 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-06-19 UTC."],[],[]]
