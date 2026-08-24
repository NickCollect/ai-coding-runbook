---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=es-419
fetched_at: 2026-08-24T02:37:39.997679+00:00
title: "El almacenamiento de contexto en cach\u00e9 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# El almacenamiento de contexto en caché

En un flujo de trabajo de IA típico, es posible que pases los mismos tokens de entrada una y otra vez a un modelo. La API de Gemini ofrece almacenamiento en caché implícito para optimizar el rendimiento y los costos.

## Almacenamiento en caché implícito

El almacenamiento en caché implícito está habilitado de forma predeterminada para todos los modelos de Gemini 2.5 y versiones posteriores. [[Se admite para los modos de conversación con estado (con ) y sin estado.](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419#multi-turn-conversations)](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419#stateless-conversations)`previous_interaction_id`
Pasamos automáticamente los ahorros de costos si tu solicitud alcanza las cachés. No es necesario que hagas nada para habilitar esta función. El recuento mínimo de tokens de entrada para el almacenamiento en caché de contexto se indica en la siguiente tabla para cada modelo:

| Modelo | Límite mínimo de tokens |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| Versión preliminar de Gemini 3.1 Pro | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

Para aumentar las posibilidades de un acierto de caché implícito, haz lo siguiente:

- Intenta colocar contenido grande y común al comienzo de tu instrucción.
- Intenta enviar solicitudes con un prefijo similar en un período breve.

Puedes ver la cantidad de tokens que fueron aciertos de caché en el campo `usage.total_cached_tokens` (Python y JavaScript) del objeto de respuesta.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-30 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-30 (UTC)"],[],[]]
