---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=es-419
fetched_at: 2026-05-18T05:11:44.611341+00:00
title: "Notas de la versi\u00f3n \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Notas de la versión

En esta página, se documentan las actualizaciones de la API de Gemini.

## 7 de mayo de 2026

- Se lanzó `gemini-3.1-flash-lite`, la versión con disponibilidad general (DG) de [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=es-419), optimizada para la velocidad, la escalabilidad y la rentabilidad.
- Anuncio de baja: El modelo `gemini-3.1-flash-lite-preview` dejará de estar disponible el 11/5/26 y se [dará de baja](https://ai.google.dev/gemini-api/docs/deprecations?hl=es-419) el 25 de mayo de 2026.

## 6 de mayo de 2026

- **Próximo cambio que genera interrupción**: Cambiarán el esquema de solicitud y respuesta (`outputs` → `steps`) y la configuración del formato de salida (`response_format`) de la [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=es-419). El nuevo esquema se convertirá en el predeterminado el **26 de mayo** y el esquema heredado se quitará el **8 de junio**.
  Consulta la [guía de migración](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=es-419) para obtener más detalles.

## 5 de mayo de 2026

- Se actualizó la **Búsqueda de archivos** para admitir la búsqueda multimodal. Ahora puedes incorporar y buscar imágenes de forma nativa con el modelo `gemini-embedding-2`.
  Los metadatos de fundamentación ahora incluyen `media_id` para las citas visuales y `page_numbers` que indican dónde se encuentra la información. Para obtener más información, consulta la guía de [Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419).

## 4 de mayo de 2026

- Se lanzó la compatibilidad con [Webhooks](https://ai.google.dev/gemini-api/docs/webhooks?hl=es-419) controlados por eventos en la API de Gemini para reemplazar los flujos de trabajo de sondeo de la API de Batch y las operaciones de larga duración.

## 30 de abril de 2026

- El modelo `gemini-robotics-er-1.5-preview` se [apagó](https://ai.google.dev/gemini-api/docs/deprecations?hl=es-419). En su lugar, usa [`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=es-419).

## 22 de abril de 2026

- Se lanzó `gemini-embedding-2` con disponibilidad general (DG). Para obtener más información, consulta la página [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=es-419).

## 21 de abril de 2026

- Se lanzaron nuevas versiones del agente de [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) con planificación colaborativa, compatibilidad con visualizaciones, integración del servidor de MCP y búsqueda de archivos:

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=es-419): Diseñado para la velocidad y la eficiencia, ideal para transmitirse a una IU del cliente.
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=es-419): Máxima exhaustividad para la recopilación y síntesis automatizadas de contexto.

## 15 de abril de 2026

- Lanzamos la [versión preliminar de Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=es-419), nuestro modelo de texto a voz rentable, expresivo y adaptable. Consulta los documentos de [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419) para obtener más información.

## 14 de abril de 2026

- Se lanzó `gemini-robotics-er-1.6-preview`, nuestro modelo de robótica actualizado.
  Ahora tiene nuevas capacidades, como la lectura de instrumentos y capacidades mejoradas de razonamiento espacial y físico. Para obtener más información, consulta la página de [Gemini Robotics-ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=es-419) y el [blog](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=es-419).
- Anuncio de baja: El modelo `gemini-robotics-er-1.5-preview` se [dará de baja](https://ai.google.dev/gemini-api/docs/deprecations?hl=es-419) el 30 de abril de 2026 a las 9 a.m. (PST).

## 2 de abril de 2026

- Se lanzaron `gemma-4-26b-a4b-it` y `gemma-4-31b-it`, disponibles en [AI Studio](https://aistudio.google.com?hl=es-419) y a través de la API de Gemini, como parte del lanzamiento de [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=es-419).

## 1 de abril de 2026

- Se presentaron los nuevos niveles de inferencia [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=es-419) y [Priority](https://ai.google.dev/gemini-api/docs/priority-inference?hl=es-419), que ofrecen más opciones para optimizar el costo o la latencia.

## 31 de marzo de 2026

- Lanzamos la versión preliminar de Veo 3.1 Lite, [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=es-419), nuestro modelo de [generación de videos](https://ai.google.dev/gemini-api/docs/video?hl=es-419) más rentable, diseñado para la iteración rápida y la creación de aplicaciones de gran volumen.
- Se apagó el modelo `gemini-2.5-flash-lite-preview-09-2025`. En su lugar, usa [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=es-419).

## 26 de marzo de 2026

- Se lanzó [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=es-419), el modelo de audio a audio (A2A) más reciente diseñado para el diálogo en tiempo real y las aplicaciones de IA centradas en la voz. Lee la documentación de la [API de Live](https://ai.google.dev/gemini-api/docs/live-api?hl=es-419) para comenzar.

## 25 de marzo de 2026

- Se lanzaron los modelos de generación de música [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=es-419): [`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=es-419)
  (clips de 30 segundos) y [`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=es-419)
  (canciones completas). Ambos modelos aceptan entradas de texto e imágenes, y generan audio estéreo de alta calidad a 48 kHz. Consulta la guía de [generación de música](https://ai.google.dev/gemini-api/docs/music-generation?hl=es-419) para obtener detalles y muestras de código.

## March 23, 2026

- Se lanzaron los [planes de facturación prepago y pospago](https://ai.google.dev/gemini-api/docs/billing?hl=es-419) en AI Studio. Es posible que las cuentas existentes se vean afectadas. Para obtener más información, consulta la documentación de [Facturación](https://ai.google.dev/gemini-api/docs/billing?hl=es-419).

## 18 de marzo de 2026

- Se lanzó la nueva función [Combinación de herramientas integradas y llamadas a funciones](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419), que permite usar las herramientas integradas de Gemini junto con las herramientas de llamadas a funciones personalizadas en una sola llamada a la API.
- Ahora se admite la [Fundamentación con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419#supported_models) en los modelos de Gemini 3.

## 16 de marzo de 2026

- Se actualizaron los [niveles de uso](https://ai.google.dev/gemini-api/docs/billing?hl=es-419#about-billing) y los [límites de inversión de la cuenta de facturación](https://ai.google.dev/gemini-api/docs/billing?hl=es-419#tier-spend-caps) para mejorar la experiencia de facturación del usuario.

## 12 de marzo de 2026

- Se introdujeron los [límites de inversión a nivel del proyecto](https://ai.google.dev/gemini-api/docs/billing?hl=es-419#project-spend-caps) en la facturación de AI Studio.

## 10 de marzo de 2026

- Lanzamos `gemini-embedding-2-preview`, nuestro primer modelo de incorporación multimodal.
  Admite entradas de texto, imagen, video, audio y PDF, y asigna todas las modalidades a un espacio de embedding unificado. Para obtener más información, consulta [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=es-419).
- Anuncio de baja: El modelo `gemini-2.5-flash-lite-preview-09-2025` se [dará de baja](https://ai.google.dev/gemini-api/docs/deprecations?hl=es-419) el 31 de marzo de 2026.

## 9 de marzo de 2026

- Se [cerró](https://ai.google.dev/gemini-api/docs/deprecations?hl=es-419) el modelo de versión preliminar de Gemini 3 Pro. El `gemini-3-pro-preview` ahora apunta a [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=es-419).

## 3 de marzo de 2026

- Se lanzó la versión preliminar de Gemini 3.1 Flash-Lite, el primer modelo Flash-Lite de la serie Gemini 3. Consulta la [página del modelo](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=es-419) para conocer las especificaciones, las actualizaciones específicas y la orientación para desarrolladores.

## 26 de febrero de 2026

- Se lanzó Nano Banana 2, [Gemini 3.1 Flash Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image-preview?hl=es-419), un modelo de alta eficiencia optimizado para la velocidad y los casos de uso de gran volumen.
- Anuncio de baja: La versión preliminar de Gemini 3 Pro (`gemini-3-pro-preview`) [se cerrará](https://ai.google.dev/gemini-api/docs/deprecations?hl=es-419) el 9 de marzo de 2026.

## 19 de febrero de 2026

- Lanzamos la [versión preliminar de Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=es-419), nuestra iteración más reciente de la nueva familia de modelos Gemini 3.
- Se lanzó un extremo independiente `gemini-3.1-pro-preview-customtools`, que es mejor para priorizar herramientas personalizadas, para los usuarios que compilan con una combinación de bash y herramientas.

## 18 de febrero de 2026

- Anuncio de baja: Los siguientes modelos se [desactivarán](https://ai.google.dev/gemini-api/docs/deprecations?hl=es-419) el 1 de junio de 2026:

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

## 17 de febrero de 2026

- Los siguientes modelos se [apagaron](https://ai.google.dev/gemini-api/docs/deprecations?hl=es-419):

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`

## 29 de enero de 2026

- Se lanzó la compatibilidad con la herramienta Uso de la computadora en `gemini-3-pro-preview` y `gemini-3-flash-preview`.

## 21 de enero de 2026

- Se cambiaron los alias de `latest`:

  - Se cambió `gemini-pro-latest` a `gemini-3-pro-preview`
  - Se cambió `gemini-flash-latest` a `gemini-3-flash-preview`

## 15 de enero de 2026

- Anuncio de baja: Los siguientes modelos se [apagarán](https://ai.google.dev/gemini-api/docs/deprecations?hl=es-419) el 17 de febrero de 2026:

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- Se apagó el modelo `gemini-2.5-flash-image-preview`.

## 14 de enero de 2026

- El modelo `text-embedding-004` se [apagó](https://ai.google.dev/gemini-api/docs/deprecations?hl=es-419).

## 13 de enero de 2026

- Se agregaron resoluciones de salida en 4K para [Veo](https://ai.google.dev/gemini-api/docs/video?hl=es-419) y más compatibilidad con videos verticales en todas las resoluciones.

## 12 de enero de 2026

- Se lanzó la función de ciclo de vida del modelo. Algunos modelos ahora especificarán la etapa del ciclo de vida y el cronograma de baja. Consulta la siguiente documentación para obtener más información:

  - [Etapas del modelo](https://ai.google.dev/api/generate-content?hl=es-419#ModelStatus)

## 8 de enero de 2026

- Se lanzó la compatibilidad con buckets de Cloud Storage y cualquier URL firmada previamente de BD pública y privada como fuente de entrada de datos para la API de Gemini. El límite de tamaño del archivo también aumentó de 20 MB a 100 MB. Para obtener más información, consulta la [guía de métodos de entrada de archivos](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=es-419).

## 19 de diciembre de 2025

- Se introdujo un cambio rotundo en la versión beta pública de la API de Interactions en la versión v1beta. Se cambió el nombre del campo `total_reasoning_tokens` a `total_thought_tokens` para que se alinee mejor con el concepto de "pensamientos" en los modelos de pensamiento.

## 17 de diciembre de 2025

- Se lanzó la versión preliminar de Gemini 3 Flash, `gemini-3-flash-preview`, que ofrece un rendimiento rápido de primera clase que compite con modelos más grandes a una fracción del costo. Con razonamiento visual y espacial mejorado, y capacidades de agente para programación Lee la documentación sobre algunas funciones nuevas, como las siguientes:

  - [Respuestas de funciones multimodales](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419#multimodal)
  - [Ejecución de código con imágenes](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419#images)

## 12 de diciembre de 2025

- Se lanzó `gemini-2.5-flash-native-audio-preview-12-2025`, un nuevo modelo de audio nativo para la API de Live. Esta actualización mejora la capacidad del modelo para controlar flujos de trabajo complejos. Para obtener más información, consulta la [guía de la API de Live](https://ai.google.dev/gemini-api/docs/live-guide?hl=es-419) y [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-live?hl=es-419).

## 11 de diciembre de 2025

- Se lanzó la API de Interactions en versión beta. Esta API proporciona una interfaz unificada para interactuar con modelos y agentes de Gemini. Si deseas obtener más información, consulta la guía de la [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=es-419).
- Se lanzó el agente de Deep Research de Gemini en versión preliminar. Puede planificar, ejecutar y sintetizar de forma autónoma los resultados de tareas de investigación de varios pasos. Consulta la guía de [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) para obtener más detalles.

## 10 de diciembre de 2025

- Lanzamos mejoras en nuestros [modelos de texto a voz](https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419), la versión preliminar de Gemini 2.5 Flash TTS (optimizado para baja latencia) y la versión preliminar de Gemini 2.5 Pro TTS (optimizado para calidad), que incluyen mayor expresividad, ritmo preciso y diálogo fluido.

## 9 de diciembre de 2025

- Los siguientes modelos de la API de Gemini Live ya no están disponibles:
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## 5 de diciembre de 2025

- La facturación de Gemini 3 para la [Fundamentación con la Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419) comenzará el 5 de enero de 2026.

## 4 de diciembre de 2025

- Anuncio de baja: El modelo `gemini-2.5-flash-image-preview` se cerrará el 15 de enero de 2026.

## 13 de diciembre de 2023

- Anuncio de baja: El modelo `text-embedding-004` se cerrará el 14 de enero de 2026.

## 20 de noviembre de 2025

- Se lanzó la versión preliminar de Gemini 3 Pro Image, `gemini-3-pro-image-preview`, la próxima iteración del modelo Nano Banana. Lee la página [Generación de imágenes](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419) para obtener más detalles.

## 18 de noviembre de 2025

- Lanzamos el primer modelo de la serie Gemini 3, `gemini-3-pro-preview`, nuestro modelo de vanguardia para el razonamiento y la comprensión multimodal con potentes capacidades de agente y programación.

  Además de las mejoras en la inteligencia y el rendimiento, la versión preliminar de Gemini 3 Pro presenta un nuevo comportamiento en relación con lo siguiente:

  - [Resolución de medios](https://ai.google.dev/gemini-api/docs/media-resolution?hl=es-419)
  - [Firmas de pensamiento](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=es-419)
  - [Niveles de pensamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419#thinking-levels)

  Lee la [Guía para desarrolladores de Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=es-419) para obtener información sobre la migración, las funciones nuevas y las especificaciones.

## 11 de noviembre de 2025

- Anuncio de baja: Se cerrarán los siguientes modelos:

  - 12 de noviembre:

    - `veo-3.0-fast-generate-preview`
    - `veo-3.0-generate-preview`
  - 14 de noviembre:

    - `gemini-2.0-flash-exp-image-generation`
    - `gemini-2.0-flash-preview-image-generation`

## 10 de noviembre de 2025

- Se apagó el siguiente modelo:

  - `imagen-3.0-generate-002`

  En su lugar, usa [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=es-419#imagen-4). Consulta la [tabla de bajas de Gemini](https://ai.google.dev/gemini-api/docs/deprecations?hl=es-419) para obtener más detalles.

## 6 de noviembre de 2025

- Se lanzó la API de File Search en versión preliminar pública, lo que permite a los desarrolladores fundamentar las respuestas en sus propios datos. Lee la nueva página de [Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419) para obtener más información.

## 4 de noviembre de 2025

- En el caso de [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419), la cantidad de tokens de entrada para las imágenes se redujo de 1,290 a 258, lo que disminuyó el costo de la edición de imágenes.
- Anuncio de baja: Se cerrarán los siguientes modelos:

  - 18 de noviembre:

    - `gemini-2.5-flash-lite-preview-06-17`
    - `gemini-2.5-flash-preview-05-20`
  - 2 de diciembre:

    - `gemini-2.0-flash-thinking-exp`
    - `gemini-2.0-flash-thinking-exp-01-21`
    - `gemini-2.0-flash-thinking-exp-1219`
    - `gemini-2.5-pro-preview-03-25`
    - `gemini-2.5-pro-preview-05-06`
    - `gemini-2.5-pro-preview-06-05`
  - 9 de diciembre:

    - `gemini-2.0-flash-lite-preview`
    - `gemini-2.0-flash-lite-preview-02-05`
    - `gemini-2.0-flash-exp`
    - `gemini-2.0-pro-exp`
    - `gemini-2.0-pro-exp-02-05`

## 29 de octubre de 2025

- Se lanzó la nueva herramienta de [registros y conjuntos de datos](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=es-419) para la API de Gemini.

## 20 de octubre de 2025

- Los siguientes modelos de la API de Gemini Live ya no están disponibles:

  - `gemini-2.5-flash-preview-native-audio-dialog`
  - `gemini-2.5-flash-exp-native-audio-thinking-dialog`

  En su lugar, puedes usar `gemini-2.5-flash-native-audio-preview-09-2025`.
- Anuncio de baja: Se cerrarán `gemini-2.0-flash-live-001` y `gemini-live-2.5-flash-preview` el 9 de diciembre de 2025.

## 17 de octubre de 2025

- La **Fundamentación con Google Maps** ya está disponible de forma general. Para obtener más información, consulta la documentación de [Fundamentación con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419).

## 15 de octubre de 2025

- Se lanzaron los modelos [Veo 3.1 y 3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=es-419#veo-3.1) en versión preliminar pública, con nuevas funciones, como las siguientes:

  - Extender los videos creados con Veo
  - Hacer referencia a hasta tres imágenes para generar un video
  - Proporciona imágenes del primer y último fotograma para generar videos.

  Con este lanzamiento, también se agregaron más opciones para la duración de los videos generados por Veo 3: 4, 6 y 8 segundos.
- Anuncio de baja: `veo-3.0-generate-preview` y `veo-3.0-fast-generate-preview` dejarán de estar disponibles el 12 de noviembre de 2025.

## 7 de octubre de 2025

- Se lanzó la [versión preliminar de Gemini 2.5 Computer Use](https://ai.google.dev/gemini-api/docs/computer-use?hl=es-419)

## 4 de octubre de 2023

- Se lanzó la DG de Gemini 2.5 Flash Image: [Generación de imágenes con Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419)

## 29 de septiembre de 2025

- Los siguientes modelos de Gemini 1.5 ya no están disponibles:
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## 25 de septiembre de 2025

- Se lanzó el modelo Gemini Robotics-ER 1.5 en versión preliminar. Consulta la [descripción general de la robótica](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=es-419) para obtener información sobre cómo usar el modelo en tu aplicación de robótica.
- Se lanzaron los siguientes modelos de vista previa:

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  Consulta la página [Modelos](https://ai.google.dev/gemini-api/docs/models?hl=es-419) para obtener más detalles.

## 23 de septiembre de 2025

- Se lanzó `gemini-2.5-flash-native-audio-preview-09-2025`, un nuevo modelo de audio nativo para la API de Live con una mejor llamada a función y manejo de cortes de voz. Para obtener más información, consulta la [guía de la API de Live](https://ai.google.dev/gemini-api/docs/live-guide?hl=es-419) y [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-2.5-flash-native-audio).

## 16 de septiembre de 2025

- Anuncio de baja: Los siguientes modelos se apagarán en octubre de 2025:

  - `embedding-001`
  - `embedding-gecko-001`
  - `gemini-embedding-exp-03-07` (`gemini-embedding-exp`)

  Consulta la página [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=es-419) para obtener detalles sobre el modelo de embeddings más reciente.

## 10 de septiembre de 2025

- Se lanzó la compatibilidad con el [modelo de Embeddings en la API de Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419#batch-embedding) y se agregó la API de Batch a la [biblioteca de compatibilidad con OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=es-419#batch) para que sea aún más fácil comenzar a usar las consultas por lotes.

## Septiembre

- Se lanzó la DG de Veo 3 y Veo 3 Fast, con precios más bajos y nuevas opciones para las relaciones de aspecto, la resolución y la generación de imágenes iniciales. Lee la [documentación de Veo](https://ai.google.dev/gemini-api/docs/video?hl=es-419#model-features) para obtener más información.

## 26 de agosto de 2025

- Lanzamos [Gemini 2.5 Image Preview](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-2.5-flash-image-preview), nuestro modelo de generación de imágenes nativo más reciente.

## 18 de agosto de 2025

- Se lanzó la [herramienta de contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419) para la disponibilidad general (DG), una herramienta para proporcionar URLs como contexto adicional para las instrucciones. En una semana, se dejará de admitir el uso del contexto de URL con el modelo `gemini-2.0-flash` (disponible durante la versión experimental).

## 14 de agosto de 2025

- Se lanzaron los modelos Imagen 4 Ultra, Standard y Fast con disponibilidad general (DG). Para obtener más información, consulta la página [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=es-419).

## 7 de agosto de 2025

- El parámetro de configuración `allow_adult` en la generación de imágenes a video ahora está disponible en regiones restringidas. Consulta la página de [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=es-419#veo-model-parameters) para obtener más detalles.

## 31 de julio de 2025

- Se lanzó la generación de videos a partir de imágenes para el modelo Veo 3 Preview.
- Se lanzó el modelo Veo 3 Fast Preview.
- Para obtener más información sobre Veo 3, visita la página de [Veo](https://ai.google.dev/gemini-api/docs/video?hl=es-419).

## 22 de julio de 2025

- Lanzamos `gemini-2.5-flash-lite`, nuestro modelo Gemini 2.5 rápido, económico y de alto rendimiento. Para obtener más información, consulta [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-2.5-flash-lite).

## 17 de julio de 2025

- Se lanzó `veo-3.0-generate-preview`, la actualización más reciente de Veo que incluye la generación de videos con audio. Para obtener más información sobre Veo 3, visita la página de [Veo](https://ai.google.dev/gemini-api/docs/video?hl=es-419).
- Se aumentaron los límites de frecuencia de Imagen 4 Estándar y Ultra. Visita la página [Límites de frecuencia](https://ai.google.dev/gemini-api/docs/rate-limits?hl=es-419) para obtener más detalles.

## 14 de julio de 2025

- Lanzamos `gemini-embedding-001`, la versión estable de nuestro modelo de embedding de texto. Para obtener más información, consulta [embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=es-419). El modelo `gemini-embedding-exp-03-07` quedará obsoleto el 14 de agosto de 2025.

## 7 de julio de 2025

- Se lanzó el modo por lotes de la API de Gemini. Agrupa las solicitudes en lotes y envíalas para que se procesen de forma asíncrona. Para obtener más información, consulta [Modo por lotes](https://ai.google.dev/gemini-api/docs/batch-mode?hl=es-419).

## 26 de junio de 2025

- Los modelos en versión preliminar `gemini-2.5-pro-preview-05-06` y `gemini-2.5-pro-preview-03-25` ahora se redireccionan a la versión estable más reciente `gemini-2.5-pro`.
- Se apagó `gemini-2.5-pro-exp-03-25`.

## 24 de junio de 2025

- Se lanzaron los modelos de vista previa de Imagen 4 Ultra y Standard. Para obtener más información, consulta la página [Generación de imágenes](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419).

## 17 de junio de 2025

- Lanzamos `gemini-2.5-pro`, la versión estable de nuestro modelo más potente, ahora con pensamiento adaptativo. Para obtener más información, consulta [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-2.5-pro) y [Pensamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419). `gemini-2.5-pro-preview-05-06`
  se redireccionará a `gemini-2.5-pro` el 26 de junio de 2025.
- Lanzamos `gemini-2.5-flash`, nuestro primer modelo estable de 2.5 Flash. Para obtener más información, consulta [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-2.5-flash).
  `gemini-2.5-flash-preview-04-17` quedará obsoleta a partir del 15 de julio de 2025.
- Se lanzó `gemini-2.5-flash-lite-preview-06-17`, un modelo de Gemini 2.5 de alto rendimiento y bajo costo. Para obtener más información, consulta la [versión preliminar de Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-2.5-flash-lite).

## 5 de junio de 2025

- Lanzamos `gemini-2.5-pro-preview-06-05`, una nueva versión de nuestro modelo más potente, ahora con razonamiento adaptativo. Para obtener más información, consulta [Versión preliminar de Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-2.5-pro-preview-06-05) y [Pensamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419).
  `gemini-2.5-pro-preview-05-06` se redireccionará a `gemini-2.5-pro` el 26 de junio de 2025.

## 27 de mayo de 2025

- Se cerró el último modelo de ajuste disponible, Gemini 1.5 Flash 001.
  Ya no se admite el ajuste en ningún modelo.
  Consulta [Ajuste con la API de Gemini](https://ai.google.dev/gemini-api/docs/model-tuning?hl=es-419).

## 20 de mayo de 2025

**Actualizaciones de la API:**

- Se lanzó la compatibilidad con el [preprocesamiento de video personalizado](https://ai.google.dev/gemini-api/docs/video-understanding?hl=es-419#customize-video-processing) con intervalos de recorte y muestreo de velocidad de fotogramas configurable.
- Se lanzó el uso de varias herramientas, que admite la configuración de la [ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419) y la [fundamentación con la Búsqueda de Google](https://ai.google.dev/gemini-api/docs/grounding?hl=es-419) en la misma solicitud de `generateContent`.
- Se lanzó la compatibilidad con las [llamadas a funciones asíncronas](https://ai.google.dev/gemini-api/docs/live-tools?hl=es-419#async-function-calling) en la API de Live.
- Se lanzó una [herramienta experimental de contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419) para proporcionar URLs como contexto adicional a las instrucciones.

**Actualizaciones del modelo:**

- Se lanzó `gemini-2.5-flash-preview-05-20`, un modelo de [vista previa](https://ai.google.dev/gemini-api/docs/models?hl=es-419#model-versions) de Gemini optimizado para el rendimiento en relación con el precio y el pensamiento adaptativo. Para obtener más información, consulta [Versión preliminar de Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-2.5-flash-preview) y [Pensamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419).
- Se lanzaron los modelos [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-2.5-pro-preview-tts) y [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-2.5-flash-preview-tts), que pueden [generar voz](https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419) con uno o dos oradores.
- Se lanzó el modelo `lyria-realtime-exp`, que [genera música](https://ai.google.dev/gemini-api/docs/music-generation?hl=es-419) en tiempo real.
- Se lanzaron `gemini-2.5-flash-preview-native-audio-dialog` y `gemini-2.5-flash-exp-native-audio-thinking-dialog`, nuevos modelos de Gemini para la API de Live con capacidades de salida de audio nativas. Para obtener más información, consulta la [guía de la API de Live](https://ai.google.dev/gemini-api/docs/live-guide?hl=es-419#native-audio-output) y [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-2.5-flash-native-audio).
- Se lanzó la versión preliminar de `gemma-3n-e4b-it`, disponible en [AI Studio](https://aistudio.google.com?hl=es-419) y a través de la API de Gemini, como parte del lanzamiento de [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=es-419).

## 7 de mayo de 2025

- Se lanzó `gemini-2.0-flash-preview-image-generation`, un modelo de vista previa para generar y editar imágenes. Para obtener más información, consulta [Generación de imágenes](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419) y [Generación de imágenes de vista previa con Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-2.0-flash-preview-image-generation).

## 6 de mayo de 2025

- Lanzamos `gemini-2.5-pro-preview-05-06`, una nueva versión de nuestro modelo más potente, con mejoras en el código y las llamadas a funciones. `gemini-2.5-pro-preview-03-25`
  apuntará automáticamente a la nueva versión del modelo.

## 17 de abril de 2025

- Se lanzó `gemini-2.5-flash-preview-04-17`, un modelo de [vista previa](https://ai.google.dev/gemini-api/docs/models?hl=es-419#model-versions) de Gemini optimizado para el rendimiento en relación con el precio y el pensamiento adaptativo. Para obtener más información, consulta [Versión preliminar de Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-2.5-flash-preview) y [Pensamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419).

## 16 de abril de 2025

- Se lanzó el almacenamiento en caché del contexto para [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-2.0-flash).

## 9 de abril de 2025

**Actualizaciones del modelo:**

- Se lanzó `veo-2.0-generate-001`, un modelo de texto y de imagen a video con disponibilidad general (DG) capaz de generar videos detallados y con matices artísticos. Para obtener más información, consulta los [documentos de Veo](https://ai.google.dev/gemini-api/docs/video?hl=es-419).
- Se lanzó `gemini-2.0-flash-live-001`, una versión de vista previa pública del modelo de la [API de Live](https://ai.google.dev/gemini-api/docs/live?hl=es-419) con la facturación habilitada.

  - **Administración y confiabilidad de sesiones mejoradas**

    - **Reanudación de sesión:** Mantén las sesiones activas durante las interrupciones temporales de la red. La API ahora admite el almacenamiento del estado de la sesión del servidor (hasta por 24 horas) y proporciona identificadores (session\_resumption) para volver a conectarse y reanudar la sesión donde la dejaste.
    - **Sesiones más largas a través de la compresión de contexto:** Permite interacciones extendidas más allá de los límites de tiempo anteriores. Configura la compresión de la ventana de contexto con un mecanismo de ventana deslizante para administrar automáticamente la longitud del contexto y evitar terminaciones abruptas debido a los límites de contexto.
    - **Notificación de desconexión correcta:** Recibe un mensaje del servidor `GoAway` que indica cuándo está por cerrarse una conexión, lo que permite un manejo correcto antes de la finalización.
  - **Más control sobre la dinámica de interacción**
  - **Detección de actividad de voz (VAD) configurable:** Elige niveles de sensibilidad o inhabilita la VAD automática por completo y usa nuevos eventos del cliente (`activityStart`, `activityEnd`) para el control manual del turno.
  - **Control de interrupciones configurable:** Decide si la entrada del usuario debe interrumpir la respuesta del modelo.
  - **Cobertura de turnos configurable:** Elige si la API procesa toda la entrada de audio y video de forma continua o solo la captura cuando se detecta que el usuario final está hablando.
  - **Resolución de medios configurable:** Selecciona la resolución de los medios de entrada para optimizar la calidad o el uso de tokens.
  - **Salida y funciones más enriquecidas**
  - **Opciones de voz y lenguaje expandidas:** Elige entre dos voces nuevas y 30 idiomas nuevos para la salida de audio. Ahora se puede configurar el idioma de salida en `speechConfig`.
  - **Transmisión de texto:** Recibe respuestas de texto de forma incremental a medida que se generan, lo que permite mostrarlas más rápido al usuario.
  - **Informes de uso de tokens:** Obtén estadísticas sobre el uso con recuentos detallados de tokens proporcionados en el campo `usageMetadata` de los mensajes del servidor, desglosados por modalidad y fases de la instrucción o la respuesta.

## 4 de abril de 2025

- Se lanzó `gemini-2.5-pro-preview-03-25`, una versión preliminar pública de Gemini 2.5 Pro con la facturación habilitada. Puedes seguir usando `gemini-2.5-pro-exp-03-25` en el nivel gratuito.

## 25 de marzo de 2025

- Se lanzó `gemini-2.5-pro-exp-03-25`, un modelo experimental público de Gemini con el modo de pensamiento siempre activado de forma predeterminada.
  Para obtener más información, consulta [Gemini 2.5 Pro Experimental](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-2.5-pro-preview-03-25).

## 12 de marzo de 2025

**Actualizaciones del modelo:**

- Se lanzó un modelo experimental de [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419#gemini) capaz de generar y editar imágenes.
- Se lanzó `gemma-3-27b-it` y está disponible en [AI Studio](https://aistudio.google.com?hl=es-419) y a través de la API de Gemini, como parte del lanzamiento de [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=es-419).

**Actualizaciones de la API:**

- Se agregó compatibilidad con las [URLs de YouTube](https://ai.google.dev/gemini-api/docs/vision?hl=es-419#youtube) como fuente de medios.
- Se agregó compatibilidad para incluir un [video intercalado](https://ai.google.dev/gemini-api/docs/vision?hl=es-419#inline-video) de menos de 20 MB.

## March 11, 2025

**Actualizaciones del SDK:**

- Se lanzó el [SDK de IA generativa de Google para TypeScript y JavaScript](https://googleapis.github.io/js-genai) en versión preliminar pública.

## 7 de marzo de 2025

**Actualizaciones del modelo:**

- Se lanzó `gemini-embedding-exp-03-07`, un modelo de incorporaciones [experimental](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=es-419) basado en Gemini en versión preliminar pública.

## 28 de febrero de 2025

**Actualizaciones de la API:**

- Se agregó compatibilidad con [Search como herramienta](https://ai.google.dev/gemini-api/docs/grounding?hl=es-419) a `gemini-2.0-pro-exp-02-05`, un modelo experimental basado en Gemini 2.0 Pro.

## 25 de febrero de 2025

**Actualizaciones del modelo:**

- Lanzamos `gemini-2.0-flash-lite`, una versión con disponibilidad general (DG) de [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#gemini-2.0-flash-lite), que se optimizó para la velocidad, la escala y la rentabilidad.

## 19 de febrero de 2025

**Actualizaciones de AI Studio:**

- Se agregó compatibilidad con [regiones adicionales](https://ai.google.dev/gemini-api/docs/available-regions?hl=es-419) (Kosovo, Groenlandia y las Islas Feroe).

**Actualizaciones de la API:**

- Se agregó compatibilidad con [regiones adicionales](https://ai.google.dev/gemini-api/docs/available-regions?hl=es-419) (Kosovo, Groenlandia y las Islas Feroe).

## 18 de febrero de 2025

**Actualizaciones del modelo:**

- Ya no se admite Gemini 1.0 Pro. Para obtener la lista de modelos compatibles, consulta [Modelos de Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419).

## 11 de febrero de 2025

**Actualizaciones de la API:**

- Se actualizaron las [bibliotecas de OpenAI para que sean compatibles](https://ai.google.dev/gemini-api/docs/openai?hl=es-419).

## 6 de febrero de 2025

**Actualizaciones del modelo:**

- Se lanzó `imagen-3.0-generate-002`, una versión con disponibilidad general (DG) de [Imagen 3 en la API de Gemini](https://ai.google.dev/gemini-api/docs/imagen?hl=es-419).

**Actualizaciones del SDK:**

- Se lanzó el [SDK de IA generativa de Google para Java](https://github.com/googleapis/java-genai) en versión preliminar pública.

## 5 de febrero de 2025

**Actualizaciones del modelo:**

- Se lanzó `gemini-2.0-flash-001`, una versión con disponibilidad general (DG) de [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#gemini-2.0-flash) que admite resultados solo de texto.
- Se lanzó `gemini-2.0-pro-exp-02-05`, una versión preliminar pública [experimental](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=es-419) de Gemini 2.0 Pro.
- Se lanzó `gemini-2.0-flash-lite-preview-02-05`, un [modelo](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#gemini-2.0-flash-lite) experimental de vista previa pública optimizado para la rentabilidad.

**Actualizaciones de la API:**

- Se agregó compatibilidad con la [entrada de archivos y la salida de gráficos](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419#input-output) para la ejecución de código.

**Actualizaciones del SDK:**

- Se lanzó el [SDK de IA generativa de Google para Python](https://googleapis.github.io/python-genai/) para la disponibilidad general (GA).

## 21 de enero de 2025

**Actualizaciones del modelo:**

- Se lanzó `gemini-2.0-flash-thinking-exp-01-21`, la versión preliminar más reciente del modelo que impulsa el [modelo Gemini 2.0 Flash Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419).

## December 19, 2024

**Actualizaciones del modelo:**

- Se lanzó el modo Gemini 2.0 Flash Thinking en versión preliminar pública. El Modo de pensamiento es un modelo de procesamiento en tiempo de prueba que te permite ver el proceso de pensamiento del modelo mientras genera una respuesta y produce respuestas con capacidades de razonamiento más sólidas.

  Obtén más información sobre el modo Gemini 2.0 Flash Thinking en nuestra [página de descripción general](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=es-419).

## 11 de diciembre de 2024

**Actualizaciones del modelo:**

- Se lanzó [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#gemini-2.0-flash) para la versión preliminar pública. La lista parcial de funciones de Gemini 2.0 Flash Experimental incluye lo siguiente:
  - El doble de rápido que Gemini 1.5 Pro
  - Transmisión bidireccional con nuestra API de Live
  - Generación de respuestas multimodales en forma de texto, imágenes y voz
  - Uso de herramientas integradas con razonamiento de varios turnos para usar funciones como ejecución de código, búsqueda, llamadas a funciones y mucho más

Obtén más información sobre Gemini 2.0 Flash en nuestra [página de descripción general](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=es-419).

## 21 de noviembre de 2024

**Actualizaciones del modelo:**

- Se lanzó `gemini-exp-1121`, un modelo de API de Gemini experimental aún más potente.

**Actualizaciones del modelo:**

- Se actualizaron los alias de los modelos `gemini-1.5-flash-latest` y `gemini-1.5-flash` para usar `gemini-1.5-flash-002`.
  - Cambio en el parámetro `top_k`: El modelo `gemini-1.5-flash-002` admite valores de `top_k` entre 1 y 41 (sin incluir este último).
    Los valores superiores a 40 se cambiarán a 40.

## 14 de noviembre de 2024

**Actualizaciones del modelo:**

- Se lanzó `gemini-exp-1114`, un potente modelo experimental de la API de Gemini.

## 8 de noviembre de 2024

**Actualizaciones de la API:**

- Se agregó [compatibilidad con Gemini](https://ai.google.dev/gemini-api/docs/openai?hl=es-419) en las bibliotecas de OpenAI y la API de REST.

## 31 de octubre de 2024

**Actualizaciones de la API:**

- Se agregó [compatibilidad con la Fundamentación con la Búsqueda de Google](https://ai.google.dev/gemini-api/docs/grounding?hl=es-419).

## 3 de octubre de 2024

**Actualizaciones del modelo:**

- Lanzamos `gemini-1.5-flash-8b-001`, una versión estable de nuestro modelo de API de Gemini más pequeño.

## 24 de septiembre de 2024

**Actualizaciones del modelo:**

- Lanzamos `gemini-1.5-pro-002` y `gemini-1.5-flash-002`, dos nuevas versiones estables de Gemini 1.5 Pro y 1.5 Flash, disponibles de forma general.
- Se actualizó el código del modelo `gemini-1.5-pro-latest` para usar `gemini-1.5-pro-002` y el código del modelo `gemini-1.5-flash-latest` para usar `gemini-1.5-flash-002`.
- Se lanzó `gemini-1.5-flash-8b-exp-0924` para reemplazar `gemini-1.5-flash-8b-exp-0827`.
- Se lanzó el [filtro de seguridad de integridad cívica](https://ai.google.dev/gemini-api/docs/safety-settings?hl=es-419#safety-filters) para la API de Gemini y AI Studio.
- Se lanzó la compatibilidad con dos parámetros nuevos para Gemini 1.5 Pro y 1.5 Flash en Python y Node.js: [`frequencyPenalty`](https://ai.google.dev/api/generate-content?hl=es-419#FIELDS.frequency_penalty) y [`presencePenalty`](https://ai.google.dev/api/generate-content?hl=es-419#FIELDS.presence_penalty).

## 19 de septiembre de 2024

**Actualizaciones de AI Studio:**

- Se agregaron botones de Me gusta y No me gusta a las respuestas del modelo para que los usuarios puedan proporcionar comentarios sobre la calidad de una respuesta.

**Actualizaciones de la API:**

- Se agregó compatibilidad con los créditos de Google Cloud, que ahora se pueden usar para el uso de la API de Gemini.

## 17 de septiembre de 2024

**Actualizaciones de AI Studio:**

- Se agregó un botón **Abrir en Colab** que exporta una instrucción y el código para ejecutarla a un notebook de Colab. La función aún no admite la generación de instrucciones con herramientas (modo JSON, llamadas a funciones o ejecución de código).

## 13 de septiembre de 2024

**Actualizaciones de AI Studio:**

- Se agregó compatibilidad con el modo de comparación, que te permite comparar respuestas en diferentes modelos y mensajes para encontrar la mejor opción para tu caso de uso.

## 30 de agosto de 2024

**Actualizaciones del modelo:**

- Gemini 1.5 Flash admite [proporcionar esquemas JSON a través de la configuración del modelo](https://ai.google.dev/gemini-api/docs/json-mode?hl=es-419#supply-schema-in-config).

## 27 de agosto de 2024

**Actualizaciones del modelo:**

- Se lanzaron los siguientes [modelos experimentales](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=es-419):
  - `gemini-1.5-pro-exp-0827`
  - `gemini-1.5-flash-exp-0827`
  - `gemini-1.5-flash-8b-exp-0827`

## 9 de agosto de 2024

**Actualizaciones de la API:**

- Se agregó compatibilidad con el [procesamiento de PDF](https://ai.google.dev/gemini-api/docs/document-processing?hl=es-419).

## 5 de agosto de 2024

**Actualizaciones del modelo:**

- Se lanzó la compatibilidad con el ajuste para Gemini 1.5 Flash.

## 1 de agosto de 2024

**Actualizaciones del modelo:**

- Lanzamos `gemini-1.5-pro-exp-0801`, una nueva versión experimental de [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#gemini-1.5-pro).

## 12 de julio de 2024

**Actualizaciones del modelo:**

- Se quitó la compatibilidad con Gemini 1.0 Pro Vision de los servicios y las herramientas de la IA de Google.

## 27 de junio de 2024

**Actualizaciones del modelo:**

- Se lanzó la versión de disponibilidad general de la ventana de contexto de 2 millones de tokens de Gemini 1.5 Pro.

**Actualizaciones de la API:**

- Se agregó compatibilidad con la [ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419).

## 18 de junio de 2024

**Actualizaciones de la API:**

- Se agregó compatibilidad con el [almacenamiento en caché del contexto](https://ai.google.dev/gemini-api/docs/caching?hl=es-419).

## 12 de junio de 2024

**Actualizaciones del modelo:**

- Se dejó de usar Gemini 1.0 Pro Vision.

## 23 de mayo de 2024

**Actualizaciones del modelo:**

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#gemini-1.5-pro) (`gemini-1.5-pro-001`) tiene disponibilidad general (DG).
- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#gemini-1.5-flash) (`gemini-1.5-flash-001`) está disponible de forma general (DG).

## 14 de mayo de 2024

**Actualizaciones de la API:**

- Se introdujo una ventana de contexto de 2 millones de tokens para Gemini 1.5 Pro (lista de espera).
- Se introdujo la [facturación](https://ai.google.dev/gemini-api/docs/billing?hl=es-419) de pago por uso para Gemini 1.0 Pro, y próximamente se incluirá la facturación de Gemini 1.5 Pro y Gemini 1.5 Flash.
- Se aumentaron los límites de frecuencia para el próximo nivel pagado de Gemini 1.5 Pro.
- Se agregó compatibilidad con videos integrados a la [API de File](https://ai.google.dev/api/rest/v1beta/files?hl=es-419).
- Se agregó compatibilidad con texto sin formato a la [API de File](https://ai.google.dev/api/rest/v1beta/files?hl=es-419).
- Se agregó compatibilidad con la llamada a función paralela, que devuelve más de una llamada a la vez.

## 10 de mayo de 2024

**Actualizaciones del modelo:**

- Se lanzó [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#gemini-1.5-flash) (`gemini-1.5-flash-latest`) en versión preliminar.

## 9 de abril de 2024

**Actualizaciones del modelo:**

- Se lanzó [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#gemini-1.5-pro) (`gemini-1.5-pro-latest`) en versión preliminar.
- Se lanzó un nuevo modelo de embedding de texto, `text-embeddings-004`, que admite tamaños de [embedding elástico](https://ai.google.dev/gemini-api/docs/embeddings?hl=es-419#elastic-embedding) inferiores a 768.

**Actualizaciones de la API:**

- Se lanzó la [API de File](https://ai.google.dev/api/rest/v1beta/files?hl=es-419) para almacenar temporalmente archivos multimedia y usarlos en instrucciones.
- Se agregó compatibilidad con instrucciones que incluyen datos de texto, imágenes y audio, también conocidas como instrucciones *multimodales*. Para obtener más información, consulta [Cómo generar instrucciones con contenido multimedia](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=es-419).
- Se lanzaron las [instrucciones del sistema](https://ai.google.dev/gemini-api/docs/system-instructions?hl=es-419) en versión beta.
- Se agregó el [modo de llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419#function_calling_mode), que define el comportamiento de ejecución para la llamada a función.
- Se agregó compatibilidad con la opción de configuración `response_mime_type`, que te permite solicitar respuestas en [formato JSON](https://ai.google.dev/gemini-api/docs/api-overview?hl=es-419#json).

## 19 de marzo de 2024

**Actualizaciones del modelo:**

- Se agregó compatibilidad para [ajustar Gemini 1.0 Pro](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/) en Google AI Studio o con la API de Gemini.

## 13 de diciembre de 2023

**Actualizaciones del modelo:**

- gemini-pro: Es un nuevo modelo de texto para una amplia variedad de tareas. Equilibra la capacidad y la eficiencia.
- gemini-pro-vision: Es un nuevo modelo multimodal para una amplia variedad de tareas.
  Equilibra la capacidad y la eficiencia.
- embedding-001: Es un nuevo modelo de embeddings.
- aqa: Es un nuevo modelo especialmente ajustado que se entrena para responder preguntas usando pasajes de texto para fundamentar las respuestas generadas.

Consulta [Modelos de Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419) para obtener más detalles.

**Actualizaciones de la versión de la API:**

- v1: Es el canal de la API estable.
- v1beta: Es el canal beta. Este canal tiene funciones que pueden estar en desarrollo.

Consulta [el tema sobre las versiones de la API](https://ai.google.dev/gemini-api/docs/api-versions?hl=es-419) para obtener más detalles.

**Actualizaciones de la API:**

- `GenerateContent` es un único extremo unificado para chat y texto.
- La transmisión está disponible a través del método `StreamGenerateContent`.
- Capacidad multimodal: La imagen es una nueva modalidad admitida
- Nuevas funciones beta:
  - [Llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419)
  - [Semantic Retriever](https://ai.google.dev/gemini-api/docs/semantic_retrieval?hl=es-419)
  - Búsqueda de respuestas atribuidas (AQA)
- Se actualizó el recuento de candidatos: Los modelos de Gemini solo devuelven 1 candidato.
- Diferentes categorías de SafetyRating y configuración de seguridad Consulta la [configuración de seguridad](https://ai.google.dev/gemini-api/docs/safety-settings?hl=es-419) para obtener más detalles.
- Aún no se admite el ajuste de modelos de Gemini (en desarrollo).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-07 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-07 (UTC)"],[],[]]
