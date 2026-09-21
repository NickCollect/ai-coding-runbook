---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-2-preview?hl=es-419
fetched_at: 2026-09-21T05:48:41.474778+00:00
title: "Versi\u00f3n preliminar de Gemini Robotics ER 2 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Versión preliminar de Gemini Robotics ER 2

Gemini Robotics ER 2 es un modelo de lenguaje de visión (VLM) para robótica que acepta texto, imágenes, videos y audio como entrada. Admite el razonamiento espacial, la comprensión de videos, la ejecución de código con agentes, la organización de herramientas de varios pasos y la coordinación de varios robots.

[Probar en Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=es-419)

## Documentación

Visita la página de [Robótica](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=es-419) para obtener una cobertura completa de las funciones y capacidades.

## gemini-robotics-er-2-preview

### Versión preliminar de Gemini Robotics ER 2

| Propiedad | Descripción |
| --- | --- |
| Código del modelo id\_card | `gemini-robotics-er-2-preview` |
| saveTipos de datos admitidos | **Entradas**  Texto, imágenes, video y audio  **Resultado**  Texto |
| token\_autoLímites de tokens[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419) | **Límite de tokens de entrada**  131,072  **Límite de tokens de salida**  65,536 |
| handymanFunciones | **[Generación de audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419)**  No compatible  **[Almacenamiento en caché](https://ai.google.dev/gemini-api/docs/caching?hl=es-419)**  Admitido  **[Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419)**  Admitido  **[Uso de la computadora](https://ai.google.dev/gemini-api/docs/computer-use?hl=es-419)**  Admitido  **[Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419)**  Admitido  **[Llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419)**  Admitido  **[Fundamentación con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419)**  Admitido  **[Generación de imágenes](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419)**  No compatible  **[API de Live](https://ai.google.dev/gemini-api/docs/live-api?hl=es-419)**  No compatible  **[Fundamentación con la Búsqueda](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419)**  Admitido  **[Resultados estructurados](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419)**  Admitido  **[Pensamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419)**  Admitido  **[Contexto de la URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419)**  Admitido |
| speedOpciones de consumo | **[API de Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419)**  Admitido  **[Inferencia flexible](https://ai.google.dev/gemini-api/docs/flex-inference?hl=es-419)**  No compatible  **[Inferencia de prioridad](https://ai.google.dev/gemini-api/docs/priority-inference?hl=es-419)**  No compatible |
| Versiones de 123 | Lee los [patrones de versiones del modelo](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#model-versions) para obtener más detalles.  - Vista previa: `gemini-robotics-er-2-preview` |
| calendar\_monthÚltima actualización | Julio de 2026 |
| Ficha del modelo de id\_card | [Ficha del modelo](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=es-419) |

### Versión preliminar de transmisión de Gemini Robotics ER 2

| Propiedad | Descripción |
| --- | --- |
| Código del modelo id\_card | `gemini-robotics-er-2-streaming-preview` |
| saveTipos de datos admitidos | **Entradas**  Texto, imágenes, video y audio  **Resultado**  Texto |
| token\_autoLímites de tokens[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419) | **Límite de tokens de entrada**  131,072  **Límite de tokens de salida**  65,536 |
| handymanFunciones | **[Generación de audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419)**  No compatible  **[Almacenamiento en caché](https://ai.google.dev/gemini-api/docs/caching?hl=es-419)**  No compatible  **[Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419)**  No compatible  **[Uso de la computadora](https://ai.google.dev/gemini-api/docs/computer-use?hl=es-419)**  No compatible  **[Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419)**  No compatible  **[Llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419)**  Admitido  **[Fundamentación con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419)**  No compatible  **[Generación de imágenes](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419)**  No compatible  **[API de Live](https://ai.google.dev/gemini-api/docs/live-api?hl=es-419)**  Admitido  **[Fundamentación con la Búsqueda](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419)**  Admitido  **[Resultados estructurados](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419)**  No compatible  **[Pensamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419)**  Admitido  **[Contexto de la URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419)**  No compatible |
| speedOpciones de consumo | **[API de Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419)**  No compatible  **[Inferencia flexible](https://ai.google.dev/gemini-api/docs/flex-inference?hl=es-419)**  No compatible  **[Inferencia de prioridad](https://ai.google.dev/gemini-api/docs/priority-inference?hl=es-419)**  No compatible |
| Versiones de 123 | Lee los [patrones de versiones del modelo](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#model-versions) para obtener más detalles.  - Vista previa: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthÚltima actualización | Julio de 2026 |
| Ficha del modelo de id\_card | [Ficha del modelo](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=es-419) |

### Versión preliminar de Gemini Robotics ER 1.6

| Propiedad | Descripción |
| --- | --- |
| Código del modelo id\_card | `gemini-robotics-er-1.6-preview` |
| saveTipos de datos admitidos | **Entradas**  Texto, imágenes, video y audio  **Resultado**  Texto |
| token\_autoLímites de tokens[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419) | **Límite de tokens de entrada**  131,072  **Límite de tokens de salida**  65,536 |
| handymanFunciones | **[Generación de audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419)**  No compatible  **[Almacenamiento en caché](https://ai.google.dev/gemini-api/docs/caching?hl=es-419)**  Admitido  **[Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419)**  Admitido  **[Uso de la computadora](https://ai.google.dev/gemini-api/docs/computer-use?hl=es-419)**  Admitido  **[Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419)**  Admitido  **[Llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419)**  Admitido  **[Fundamentación con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419)**  Admitido  **[Generación de imágenes](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419)**  No compatible  **[API de Live](https://ai.google.dev/gemini-api/docs/live-api?hl=es-419)**  No compatible  **[Fundamentación con la Búsqueda](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419)**  Admitido  **[Resultados estructurados](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419)**  Admitido  **[Pensamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419)**  Admitido  **[Contexto de la URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419)**  Admitido |
| speedOpciones de consumo | **[API de Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419)**  Admitido  **[Inferencia flexible](https://ai.google.dev/gemini-api/docs/flex-inference?hl=es-419)**  No compatible  **[Inferencia de prioridad](https://ai.google.dev/gemini-api/docs/priority-inference?hl=es-419)**  No compatible |
| Versiones de 123 | Lee los [patrones de versiones del modelo](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#model-versions) para obtener más detalles.  - Vista previa: `gemini-robotics-er-1.6-preview` |
| calendar\_monthÚltima actualización | Diciembre de 2025 |
| cognition\_2Fecha límite de conocimiento | Enero de 2025 |

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-08-19 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-08-19 (UTC)"],[],[]]
