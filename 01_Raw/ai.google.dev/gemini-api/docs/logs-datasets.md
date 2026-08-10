---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=es-419
fetched_at: 2026-08-10T03:18:56.196161+00:00
title: "Registros y conjuntos de datos \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Registros y conjuntos de datos

En esta guía, aprenderás a ver los registros del uso de la API de Gemini en el panel de Google AI Studio para comprender mejor el comportamiento del modelo y cómo los usuarios pueden interactuar con tus aplicaciones. Usa el registro para observar, depurar y *compartir de forma opcional comentarios sobre el uso con Google para ayudar a mejorar Gemini en los casos de uso de los desarrolladores*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=es-419)

Se admiten todas las llamadas a las APIs de `GenerateContent`, `BatchGenerateContent` y `StreamGenerateContent`, y las llamadas a la API de [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=es-419), excepto las de los agentes administrados. Esto incluye las llamadas realizadas a través de los extremos de [compatibilidad con OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=es-419).

## Configura el registro del proyecto

De forma predeterminada, la API almacena todos los objetos de interacción (`store=true`) para simplificar el uso de las funciones de administración de estados del servidor. Por el contrario, la API de Generate Content no almacena solicitudes de forma predeterminada y requiere que el almacenamiento se habilite por solicitud o a nivel del proyecto desde AI Studio.

En [AI Studio](https://aistudio.google.com/logs?hl=es-419) de Google, puedes habilitar o inhabilitar el registro para todos los proyectos o para proyectos específicos, y cambiar estas preferencias en cualquier momento a través del panel **Configuración** en la página [Registros y conjuntos de datos](https://aistudio.google.com/logs?hl=es-419). El registro se puede activar o desactivar de forma independiente para la API de `generateContent` y la API de [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=es-419) para cambiar el comportamiento de almacenamiento predeterminado de un proyecto.

### Registro a nivel de la solicitud

El comportamiento de almacenamiento y registro varía según la API:

- **[API de Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=es-419):** Almacena solicitudes de forma predeterminada (`store=true`) para simplificar la administración del estado del servidor.
- **Generate Content API (`generateContent`):** No almacena solicitudes de forma predeterminada (`store=false`).

A continuación, se explica cómo puedes configurar la propiedad `store`:

**API de GenerateContent**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents='Explain quantum entanglement in simple terms.',
    config={'store': False} # Set to True to enable logging of this request
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: 'Explain quantum entanglement in simple terms.',
    config: {
        store: false // Set to true to enable logging of this request
    }
});

console.log(response.text);
```

**API de Interactions**

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain quantum entanglement in simple terms.",
    store=True # Set to False to disable logging of this request
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Explain quantum entanglement in simple terms.',
    store: true // Set to false to disable logging of this request
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

## Cómo ver los registros del proyecto en AI Studio

1. Ve a la página Registros en [AI Studio](https://aistudio.google.com/logs?hl=es-419).
2. Selecciona un proyecto en el menú desplegable.
3. Si existen, los registros aparecerán en la tabla en orden cronológico inverso para la API de Interactions.
4. Para observar los registros del proyecto de la API de Generate Content, primero habilita esta opción en el [panel de configuración](#configure-logging).

Haz clic en una entrada para obtener una vista previa de la carga útil. Puedes inspeccionar la instrucción y la respuesta completas de Gemini, así como el contexto de los turnos anteriores. En el caso de las solicitudes a la **API de Interactions**, los registros también incluyen un vínculo directo a `previous_interaction_id`.

## Configura la retención del almacenamiento del proyecto

Los registros vencerán y se marcarán para su eliminación después de un período de retención predeterminado de 55 días (a menos que se [guarden en un conjunto de datos](#create), en cuyo caso no vencerán).
Puedes configurar el período de retención de los registros de un proyecto en un máximo de 7, 14, 28 o 55 días.

## Crea y comparte conjuntos de datos

Puedes guardar los registros en conjuntos de datos para organizarlos y exportarlos de manera más eficaz.

- En la [página Registros](https://aistudio.google.com/logs?hl=es-419), busca la barra de filtros en la parte superior para seleccionar una propiedad por la que filtrar.
- En la vista filtrada, usa las casillas de verificación para seleccionar todos los registros o registros individuales.
- Haz clic en el botón **Crear conjunto de datos** que aparece en la parte superior de la lista.
- Asigna un nombre y una descripción opcional a tu nuevo conjunto de datos.
- Verás el conjunto de datos que acabas de crear con el conjunto seleccionado de registros.
- Exporta tu conjunto de datos para realizar un análisis más detallado como archivos CSV, JSONL o a Hojas de cálculo de Google.

Los conjuntos de datos pueden ser útiles para varios casos de uso diferentes.

- **Selecciona conjuntos de desafíos:** Impulsa mejoras futuras que se enfoquen en las áreas en las que deseas que mejore tu IA.
- **Selecciona conjuntos de muestras:** Por ejemplo, una muestra del uso real para generar respuestas a partir de otro modelo o una colección de casos extremos para verificaciones de rutina antes de la implementación.
- **Conjuntos de evaluación:** Son conjuntos representativos del uso real en las capacidades importantes, para la comparación entre otros modelos o iteraciones de instrucciones del sistema.

Puedes contribuir a la investigación y el desarrollo de Gemini compartiendo tus conjuntos de datos con Google como ejemplos de demostración.

## Limitaciones

Por el momento, no se admite el registro para lo siguiente:

- Modelos de Imagen y Veo
- Modelos de incorporación de Gemini
- Modelo de Gemini Robotics
- Entradas que contienen videos, GIFs o PDFs
- Agentes en versión preliminar pública en la API de Gemini

## ¿Qué sigue?

- **Crea prototipos con el historial de sesiones:** Usa [AI Studio Build](https://aistudio.google.com/apps?hl=es-419) para crear apps con vibe coding y agrega tu clave de API para habilitar un historial de registros de la API de Gemini para las funciones basadas en IA.
- **Vuelve a ejecutar los registros con la API de Gemini Batch:** Usa conjuntos de datos para el muestreo de respuestas y la evaluación de modelos o la lógica de la aplicación. Para ello, vuelve a ejecutar los registros con la [API de Gemini Batch](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-22 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-22 (UTC)"],[],[]]
