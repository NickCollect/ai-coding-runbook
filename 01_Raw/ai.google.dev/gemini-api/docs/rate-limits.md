---
source_url: https://ai.google.dev/gemini-api/docs/rate-limits?hl=es-419
fetched_at: 2026-06-08T05:30:37.372399+00:00
title: "L\u00edmites de frecuencia \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Límites de frecuencia

Los límites de frecuencia regulan la cantidad de solicitudes que puedes realizar a la API de Gemini en un período determinado. Estos límites ayudan a mantener un uso justo, proteger contra el abuso y mantener el rendimiento del sistema para todos los usuarios.

[Consulta tus límites de frecuencia activos en AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=es-419)

## Cómo funcionan los límites de frecuencia

Por lo general, los límites de frecuencia se miden en tres dimensiones:

- Solicitudes por minuto (**RPM**)
- Tokens por minuto (entrada) (**TPM**)
- Solicitudes por día (**RPD**)

Tu uso se evalúa en función de cada límite, y si superas alguno de ellos, se activará un error de límite de frecuencia. Por ejemplo, si tu límite de RPM es de 20, realizar 21 solicitudes en un minuto generará un error, incluso si no superaste tu límite de TPM ni otros límites.

Los límites de frecuencia se aplican por proyecto, no por clave de API. Las cuotas de solicitudes por día (**RPD**) se restablecen a medianoche, hora del Pacífico.

Los límites varían según el modelo específico que se use, y algunos límites solo se aplican a modelos específicos. Por ejemplo, las imágenes por minuto (IPM) solo se calculan para los modelos capaces de generar imágenes (Nano Banana), pero son conceptualmente similares a las TPM. Otros modelos pueden tener un límite de tokens por día (TPD).

Los límites de frecuencia son más estrictos para los modelos experimentales y de vista previa.

## Niveles de uso

Los límites de frecuencia están vinculados al nivel de uso del proyecto. A medida que aumente tu uso y gasto de la API, se te actualizará automáticamente a un nivel superior con límites de frecuencia más altos.

Los requisitos para los niveles 2 y 3 se basan en la inversión acumulada total en los servicios de Google Cloud (incluida, sin limitaciones, la API de Gemini) para la cuenta de facturación vinculada a tu proyecto.

| Nivel de uso | Calificación | [Límite del nivel de facturación](https://ai.google.dev/gemini-api/docs/billing?hl=es-419#tier-spend-caps) |
| --- | --- | --- |
| **Gratis** | [Proyecto activo](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419#google-cloud-projects) o prueba gratuita | N/A |
| **Nivel 1** | [Configura y vincula una cuenta de facturación activa](https://ai.google.dev/gemini-api/docs/billing?hl=es-419#setup-billing) | $250 |
| **Nivel 2** | Se pagaron USD 100 y pasaron 3 días desde el primer pago exitoso. | $2,000 |
| **Nivel 3** | Se pagaron USD 1,000 y pasaron 30 días desde el primer pago exitoso | De USD 20,000 a más de USD 100,000 |

Si bien cumplir con los criterios de calificación establecidos suele ser suficiente para la aprobación, en casos excepcionales, se puede rechazar una solicitud de actualización en función de otros factores identificados durante el proceso de revisión.

Este sistema ayuda a mantener la seguridad y la integridad de la plataforma de la API de Gemini para todos los usuarios.

## Límites de frecuencia de la API de Gemini

Los límites de frecuencia dependen de diversos factores (como tu nivel de uso) y se pueden consultar en Google AI Studio. A medida que cambien tu nivel y el estado de tu cuenta con el tiempo, los límites de frecuencia se actualizarán automáticamente.

[Consulta tus límites de frecuencia activos en AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=es-419)

Los límites de frecuencia especificados no están garantizados y la capacidad real puede variar.

## Límites de frecuencia de la inferencia de prioridad

El consumo de [prioridad](https://ai.google.dev/gemini-api/docs/priority-inference?hl=es-419) tiene sus propios límites de frecuencia, aunque el consumo se contabiliza para los límites de frecuencia generales del tráfico interactivo. **Los límites de frecuencia predeterminados son 0.3 veces el [límite de frecuencia estándar](https://aistudio.google.com/rate-limit?hl=es-419) para cada modelo y nivel**

## Límites de frecuencia de la API de Batch

Las solicitudes a la [API por lotes](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419) están sujetas a sus propios límites de frecuencia, que son independientes de las llamadas a la API que no son por lotes.

- **Solicitudes por lotes simultáneas:** 100
- **Límite de tamaño del archivo de entrada:** 2 GB
- **Límite de almacenamiento de archivos:** 20 GB
- **Tokens en cola por modelo:** En la tabla **Tokens en cola por lotes**, se indica la cantidad máxima de tokens que se pueden poner en cola para el procesamiento por lotes en todos los trabajos por lotes activos para un modelo determinado.

### Nivel 1

| Modelo | Tokens en cola por lotes |
| --- | --- |
| Modelos de texto de salida | | | | |
| --- | --- | --- | --- | --- |
| Versión preliminar de Gemini 3.1 Pro | 5,000,000 |
| Gemini 3.1 Flash-Lite | 10,000,000 |
| Versión preliminar de Gemini 3.1 Flash-Lite | 10,000,000 |
| Gemini 3.5 Flash | 3,000,000 |
| Gemini 3.5 Flash | 3,000,000 |
| Gemini 2.5 Pro | 5,000,000 |
| Gemini 2.5 Pro TTS | 25,000 |
| Gemini 2.5 Flash | 3,000,000 |
| Versión preliminar de Gemini 2.5 Flash | 3,000,000 |
| Versión preliminar de Gemini 2.5 Flash Image | 3,000,000 |
| TTS de Gemini 2.5 Flash | 100,000 |
| Gemini 2.5 Flash-Lite | 10,000,000 |
| Versión preliminar de Gemini 2.5 Flash-Lite | 10,000,000 |
| Gemini 2.0 Flash | 10,000,000 |
| Gemini 2.0 Flash Image | 3,000,000 |
| Gemini 2.0 Flash-Lite | 10,000,000 |
| Modelos de generación multimodal | | | | |
| Versión preliminar de Gemini 3.1 Flash Image 🍌 | 1,000,000 |
| Versión preliminar de Gemini 3 Pro Image 🍌 | 2,000,000 |
| Modelos de embeddings | | | | |
| Gemini Embedding | 500,000 |

### Nivel 2

| Modelo | Tokens en cola por lotes |
| --- | --- |
| Modelos de texto de salida | | | | |
| --- | --- | --- | --- | --- |
| Versión preliminar de Gemini 3.1 Pro | 500,000,000 |
| Gemini 3.1 Flash-Lite | 500,000,000 |
| Versión preliminar de Gemini 3.1 Flash-Lite | 500,000,000 |
| Gemini 3.5 Flash | 400,000,000 |
| Gemini 3.5 Flash | 400,000,000 |
| Gemini 2.5 Pro | 500,000,000 |
| Gemini 2.5 Pro TTS | 100,000 |
| Gemini 2.5 Flash | 400,000,000 |
| Versión preliminar de Gemini 2.5 Flash | 400,000,000 |
| Versión preliminar de Gemini 2.5 Flash Image | 400,000,000 |
| TTS de Gemini 2.5 Flash | 100,000 |
| Gemini 2.5 Flash-Lite | 500,000,000 |
| Versión preliminar de Gemini 2.5 Flash-Lite | 500,000,000 |
| Gemini 2.0 Flash | 1,000,000,000 |
| Gemini 2.0 Flash Image | 400,000,000 |
| Gemini 2.0 Flash-Lite | 1,000,000,000 |
| Modelos de generación multimodal | | | | |
| Versión preliminar de Gemini 3.1 Flash Image 🍌 | 250,000,000 |
| Versión preliminar de Gemini 3 Pro Image 🍌 | 270,000,000 |
| Modelos de embeddings | | | | |
| Gemini Embedding | 5,000,000 |

### Nivel 3

| Modelo | Tokens en cola por lotes |
| --- | --- |
| Modelos de texto de salida | | | | |
| --- | --- | --- | --- | --- |
| Versión preliminar de Gemini 3.1 Pro | 1,000,000,000 |
| Gemini 3.1 Flash-Lite | 1,000,000,000 |
| Versión preliminar de Gemini 3.1 Flash-Lite | 1,000,000,000 |
| Gemini 3.5 Flash | 1,000,000,000 |
| Gemini 3.5 Flash | 1,000,000,000 |
| Gemini 2.5 Pro | 1,000,000,000 |
| Gemini 2.5 Pro TTS | 1,000,000 |
| Gemini 2.5 Flash | 1,000,000,000 |
| Versión preliminar de Gemini 2.5 Flash | 1,000,000,000 |
| Versión preliminar de Gemini 2.5 Flash Image | 1,000,000,000 |
| TTS de Gemini 2.5 Flash | 4,000,000 |
| Gemini 2.5 Flash-Lite | 1,000,000,000 |
| Versión preliminar de Gemini 2.5 Flash-Lite | 1,000,000,000 |
| Gemini 2.0 Flash | 5,000,000,000 |
| Gemini 2.0 Flash Image | 1,000,000,000 |
| Gemini 2.0 Flash-Lite | 5,000,000,000 |
| Modelos de generación multimodal | | | | |
| Versión preliminar de Gemini 3.1 Flash Image 🍌 | 750,000,000 |
| Versión preliminar de Gemini 3 Pro Image 🍌 | 1,000,000,000 |
| Modelos de embeddings | | | | |
| Gemini Embedding | 10,000,000 |

## Cómo actualizar al siguiente nivel

Para cambiar del nivel gratuito a un nivel pagado, primero debes [configurar la facturación en AI Studio](https://ai.google.dev/gemini-api/docs/billing?hl=es-419).

Una vez que tu proyecto cumpla con los [criterios especificados](#usage-tiers), se actualizará automáticamente al siguiente nivel. Las actualizaciones de nivel del plan gratuito al nivel 1 suelen aplicarse de inmediato, y las actualizaciones de nivel posteriores se aplicarán en un plazo de 10 minutos. Navega a la [página Proyectos](https://aistudio.google.com/projects?hl=es-419) en AI Studio para verificar tus niveles.

## Solicita un aumento del límite de frecuencia

Cada variación del modelo tiene un límite de frecuencia asociado (solicitudes por minuto, RPM).
Para obtener detalles sobre esos límites de frecuencia, consulta la página [Límites de frecuencia de AI Studio](https://aistudio.google.com/rate-limit?hl=es-419).

[Solicita un aumento del límite de la tarifa del nivel pagado](https://forms.gle/ETzX94k8jf7iSotH9)

No ofrecemos garantías sobre el aumento del límite de frecuencia, pero haremos todo lo posible para revisar tu solicitud.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-28 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-28 (UTC)"],[],[]]
