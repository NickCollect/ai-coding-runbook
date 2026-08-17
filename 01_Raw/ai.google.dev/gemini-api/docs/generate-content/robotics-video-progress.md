---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=it
fetched_at: 2026-08-17T02:26:43.939693+00:00
title: "Comprensione dei video \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Comprensione dei video

Gemini Robotics ER 2 può monitorare l'avanzamento delle attività dai feed video continui utilizzando due funzionalità:

- Ricerca di momenti: identifica il timestamp preciso in cui si verifica un evento chiave.
- Classificazione dell'avanzamento: assegna a ogni video una delle cinque fasce di completamento (0-20%, 20-40%, 40-60%, 60-80%, 80-100%).

## Ricerca di momenti

La ricerca di momenti identifica il frame video esatto in cui si verifica un evento critico, ad esempio quando una tazza è piena o viene fatto un nodo. I robot lo utilizzano per verificare il successo, sequenziare i passaggi e attivare le correzioni.

Il seguente prompt di esempio chiede al modello di identificare il momento di completamento di una determinata attività in un video:

```
from google import genai
from google.genai import types

client = genai.Client()

with open("task_video.mp4", "rb") as f:
    video_bytes = f.read()

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(data=video_bytes, mime_type="video/mp4"),
        prompt,
    ],
)

print(response.text)
```

Di seguito sono riportati esempi di frame di un video di ricerca di momenti, con il modello che identifica il timestamp di completamento dell'attività:

![Esempio di fotogrammi video che mostrano l'output della ricerca di momenti con una sovrapposizione di timestamp](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=it)

## Classificazione dell'avanzamento

La classificazione dell'avanzamento assegna un video a una delle cinque fasce di completamento: 0-20%, 20-40%, 40-60%, 60-80% o 80-100%. In questo modo, i robot hanno una consapevolezza situazionale in tempo reale, in modo da poter regolare le azioni o riprovare i passaggi non riusciti senza riavviare un intero flusso di lavoro.

Il seguente prompt di esempio chiede al modello di classificare il livello di avanzamento corrente di un video:

```
from google import genai
from google.genai import types

client = genai.Client()

with open("task_video.mp4", "rb") as f:
    video_bytes = f.read()

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(data=video_bytes, mime_type="video/mp4"),
        prompt,
    ],
)

print(response.text)
```

Di seguito sono riportati esempi di frame di un video di classificazione dell'avanzamento, con il modello che assegna una fascia di avanzamento:

![Esempio di fotogrammi video che mostrano l'output della classificazione dell'avanzamento con un'etichetta di parentesi di avanzamento](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=it)

## Esempi

Per esempi eseguibili completi, incluso il monitoraggio delle attività in più passaggi, consulta il
[ricettario di robotica](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Passaggi successivi

- [API Live per la robotica](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=it): streaming bidirezionale in tempo reale.
- [Orchestrazione delle attività](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=it): attività a lungo termine con ragionamento spaziale.
- [Panoramica di Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=it): confronto e funzionalità dei modelli.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
