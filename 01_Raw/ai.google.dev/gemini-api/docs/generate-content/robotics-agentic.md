---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=it
fetched_at: 2026-08-03T04:38:02.082667+00:00
title: "Funzionalit\u00e0 di visione agentica \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Funzionalità di visione agentica

I modelli ER di Gemini Robotics possono scrivere ed eseguire codice Python per manipolare le immagini e applicare la logica prima di rispondere. Questa pagina illustra esempi di esecuzione del codice: rilevamento di oggetti con zoom e ritaglio, lettura di strumenti, misurazione di fluidi, lettura di schede di circuiti e annotazione di immagini.

Per adattare questi esempi al tuo caso d'uso, sostituisci il testo del prompt e il file immagine caricato con i tuoi. Puoi anche modificare lo schema JSON richiesto nel prompt in modo che corrisponda alla struttura di output di cui ha bisogno la tua applicazione oppure aggiungere un `system_instruction` per applicare il formato e la precisione dell'output.

Per il codice eseguibile completo, consulta il
[ricettario di robotica](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Livello di pensiero

Puoi controllare il livello di pensiero per scambiare la latenza con la precisione. Le attività spaziali come il rilevamento di oggetti funzionano bene con un livello di pensiero basso. Le attività complesse come il conteggio o la stima del peso traggono vantaggio da un livello di pensiero più elevato.

L'esempio seguente imposta il livello di pensiero su `high` per un'attività di conteggio complessa:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('scene.jpeg', 'rb') as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        "Identify and count all objects on the table."
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    )
)

print(response.text)
```

Per i dettagli, consulta [Pensiero](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=it).

## Rilevamento di oggetti (zoom e ritaglio)

L'esempio seguente mostra come utilizzare l'esecuzione del codice per ingrandire e ritagliare un'immagine per una visualizzazione più chiara durante il rilevamento degli oggetti e la restituzione dei riquadri di delimitazione.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('sorting.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = """
Return JSON in the format {label: val, y: val, x: val, y2: val, x2: val} for
the compostable objects in this scene. Please Zoom and crop the image for a
clearer view. Return an annotated image of the final result with the bounding
boxes drawn on it to the API caller as a part of your process.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

L'output del modello sarà simile alla seguente risposta JSON:

```
[
  {"label": "compostable", "y": 256, "x": 482, "y2": 295, "x2": 546},
  {"label": "compostable", "y": 317, "x": 478, "y2": 350, "x2": 542},
  {"label": "compostable", "y": 586, "x": 556, "y2": 668, "x2": 595},
  {"label": "compostable", "y": 463, "x": 669, "y2": 511, "x2": 718},
  {"label": "compostable", "y": 178, "x": 565, "y2": 250, "x2": 609}
]
```

L'immagine seguente mostra le caselle restituite dal modello.

![Un esempio che mostra i riquadri di delimitazione per gli oggetti trovati](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-bounding-boxes.png?hl=it)

## Leggere un indicatore analogico e applicare la logica

L'esempio seguente mostra come utilizzare il modello per leggere un indicatore analogico ed eseguire calcoli temporali. Utilizza un'istruzione di sistema per applicare un output JSON.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('gauge.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Read the current value from this gauge. Then, calculate how long
        it will take at the current rate for the value to reach maximum.
        Reply in JSON: {"current_value": val, "max_value": val,
        "time_to_max_minutes": val}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

## Misurare il fluido in un contenitore

L'esempio seguente mostra come utilizzare l'esecuzione del codice per misurare il livello di fluido in un contenitore.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('fluid.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Measure the amount of fluid in the container. Reply in JSON:
        {"fluid_level_ml": val, "container_capacity_ml": val,
        "percentage_full": val}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

## Leggere i segni su una scheda di circuiti

L'esempio seguente mostra come utilizzare l'esecuzione del codice per leggere i segni su una scheda di circuiti.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('circuit_board.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Read all visible component labels and markings on this circuit
        board. Reply in JSON: {"components": [{"label": val,
        "location": [y, x]}]}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

![Esempio che mostra i segni su una scheda di circuito](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-circuit-board.png?hl=it)

## Annotazione immagine

L'esempio seguente mostra come utilizzare l'esecuzione del codice per annotare un'immagine (ad es. disegnare frecce per le istruzioni di smaltimento) e restituire l'immagine modificata.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('sorting.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = """
Look at this image and return it as an annotated version using arrows of
different colors to represent which items should go in which bins for
disposal. You must return the final image to the API caller.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

Di seguito è riportata un'immagine di input di esempio.

![Un esempio che mostra un orologio da leggere](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-image-annotation.png?hl=it)

L'output del modello sarà simile al seguente:

```
  The annotated image shows the suggested disposal locations for the items on the table:
  - **Green bin (Compost/Organic)**: Green chili, red chili, grapes, and cherries.
  - **Blue bin (Recycling)**: Yellow crushed can and plastic container.
  - **Black bin (Trash)**: Chocolate bar wrapper, Welch's packet, and white tissue.
```

## Passaggi successivi

- [Orchestrazione delle attività](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=it): attività a lungo termine con API robot personalizzate.
- [Robotica con streaming](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=it): streaming bidirezionale in tempo reale (solo Gemini Robotics ER 2).
- [Comprensione video](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=it): ricerca di momenti e classificazione dei progressi (solo Gemini Robotics ER 2).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
