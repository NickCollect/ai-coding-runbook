---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=es-419
fetched_at: 2026-06-01T06:06:28.747467+00:00
title: "Registros y conjuntos de datos \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Registros y conjuntos de datos

Esta guía contiene todo lo que necesitas para comenzar a habilitar el registro para tus aplicaciones existentes de la API de Gemini. En esta guía, aprenderás a ver los registros de una aplicación existente o nueva en el panel de Google AI Studio para comprender mejor el comportamiento del modelo y cómo los usuarios pueden interactuar con tus aplicaciones. Usa el registro para observar, depurar y *compartir de forma opcional comentarios de uso
con Google para ayudar a mejorar Gemini en los casos de uso de los desarrolladores*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=es-419)

Se admiten todas las llamadas a la API de `GenerateContent` y `StreamGenerateContent`,
incluidas las que se realizan a través de extremos de compatibilidad de [OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=es-419).

## 1. Habilita el registro en Google AI Studio

Antes de comenzar, asegúrate de tener un proyecto habilitado para la facturación que sea de tu propiedad.

1. Abre la página de registros en Google [AI Studio](https://aistudio.google.com/logs?hl=es-419).
2. Elige tu proyecto en el menú desplegable y presiona el botón de habilitar para habilitar el registro de todas las solicitudes de forma predeterminada.

![](https://ai.google.dev/static/gemini-api/docs/images/logs-state.png?hl=es-419)

Puedes habilitar o inhabilitar el registro para todos los proyectos o para proyectos específicos, y cambiar estas preferencias en cualquier momento a través de Google AI Studio.

## 2. Visualiza los registros en AI Studio

1. Ve a [AI Studio](https://aistudio.google.com/logs?hl=es-419).
2. Selecciona el proyecto para el que habilitaste el registro.
3. Deberías ver tus registros en la tabla en orden cronológico inverso.

![](https://storage.googleapis.com/generativeai-downloads/images/nano-banana-logs.gif)

Haz clic en una entrada para ver la vista de página completa del par de solicitud y respuesta. Puedes inspeccionar la instrucción completa, la respuesta completa de Gemini y el contexto del turno anterior. Ten en cuenta que cada proyecto tiene un límite de almacenamiento predeterminado de hasta 1,000 registros, y los registros que no se guarden en conjuntos de datos vencerán después de 55 días. Si tu proyecto alcanza su límite de almacenamiento, se te pedirá que borres los registros.

## 3. Selecciona y comparte conjuntos de datos

- En la tabla de registros, ubica la barra de filtros en la parte superior para seleccionar una propiedad por la que filtrar.
- En la vista filtrada de los registros, usa las casillas de verificación para seleccionar todos o algunos de los registros.
- Haz clic en el botón "Crear conjunto de datos" que aparece en la parte superior de la lista.
- Asigna un nombre descriptivo a tu nuevo conjunto de datos y una descripción opcional.
- Verás el conjunto de datos que acabas de crear con el conjunto seleccionado de registros.
- Exporta tu conjunto de datos para realizar un análisis más detallado como archivos CSV, JSONL o a Hojas de cálculo de Google.

![](https://storage.googleapis.com/generativeai-downloads/images/sales-dataset.gif)

Los conjuntos de datos pueden ser útiles para varios casos de uso diferentes.

- **Selecciona conjuntos de desafíos:** Impulsa mejoras futuras que se enfoquen en las áreas en las que deseas que mejore tu IA.
- **Selecciona conjuntos de muestras:** Por ejemplo, una muestra del uso real para generar respuestas de otro modelo o una colección de casos extremos para verificaciones de rutina antes de la implementación.
- **Conjuntos de evaluación:** Conjuntos que son representativos del uso real en capacidades importantes, para la comparación entre otros modelos o iteraciones de instrucciones del sistema.

Puedes ayudar a impulsar el progreso en la investigación de IA, la API de Gemini y Google AI Studio si eliges compartir tus conjuntos de datos como ejemplos de demostración. Esto nos permite refinar nuestros modelos en diversos contextos y crear sistemas de IA que sigan siendo útiles para los desarrolladores en muchos campos y aplicaciones.

## Próximos pasos y qué probar

Ahora que tienes habilitado el registro, puedes probar lo siguiente:

- **Crea prototipos con el historial de sesiones:** Aprovecha la función de compilación de [AI Studio](https://aistudio.google.com/apps?hl=es-419) para crear aplicaciones de código y agregar tu clave de API para habilitar un historial de registros de usuarios.
- **Vuelve a ejecutar registros con la API de Gemini Batch:** Usa conjuntos de datos para el muestreo de respuestas
  y la evaluación de modelos o la lógica de la aplicación volviendo a ejecutar registros a través de la
  [API de Gemini Batch](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

## Compatibilidad

Actualmente, el registro no es compatible con lo siguiente:

- Modelos de Imagen y Veo
- Modelo de incorporación de Gemini
- Entradas que contienen videos, GIFs o PDFs

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-04-29 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-04-29 (UTC)"],[],[]]
