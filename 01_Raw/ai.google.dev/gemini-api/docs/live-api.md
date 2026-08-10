---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=es-419
fetched_at: 2026-08-10T03:11:17.027723+00:00
title: "Descripci\u00f3n general de la API de Gemini Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Descripción general de la API de Gemini Live

La API de Live permite interacciones de voz y visión en tiempo real con baja latencia con Gemini. Procesa flujos continuos de audio, imágenes y texto para brindar respuestas habladas inmediatas y similares a las humanas, lo que crea una experiencia conversacional natural para tus usuarios.

![Descripción general de la API de Live](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=es-419)

[Probar la API en vivo en Google AI Studiomic](https://aistudio.google.com/live?hl=es-419)
[Clonar apps de ejemplo desde GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[Usar habilidades de agentes de programaciónterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=es-419)

## Casos de uso

La API de Live se puede usar para compilar agentes de voz en tiempo real para una variedad de industrias, incluidas las siguientes:

- **Comercio electrónico y venta minorista:** Asistentes de compras que ofrecen recomendaciones personalizadas y agentes de asistencia que resuelven los problemas de los clientes.
- **Juegos:** Personajes controlados por la máquina (NPC) interactivos, asistentes de ayuda en el juego y traducción en tiempo real del contenido del juego
- **Interfaces de nueva generación:** Experiencias habilitadas para voz y video en robótica, anteojos inteligentes y vehículos
- **Cuidado de la salud:** Compañeros de salud para la asistencia y educación de los pacientes
- **Servicios financieros:** Asesores de IA para la administración de patrimonio y la orientación sobre inversiones
- **Educación:** Mentores y compañeros de aprendizaje basados en IA que brindan instrucción y comentarios personalizados.
- **Traducción y localización:** Traducción en tiempo real y de baja latencia de conversaciones habladas, lo que permite una comunicación multilingüe fluida.

## Características clave

La API de Live ofrece un conjunto integral de funciones para crear agentes de voz sólidos:

- [**Compatibilidad con varios idiomas**](https://ai.google.dev/gemini-api/docs/live-guide?hl=es-419#supported-languages):
  Conversa en 70 idiomas compatibles.
- [**Interrupción**](https://ai.google.dev/gemini-api/docs/live-guide?hl=es-419#interruptions):
  Los usuarios pueden interrumpir el modelo en cualquier momento para tener interacciones responsivas.
- [**Uso de herramientas**](https://ai.google.dev/gemini-api/docs/live-tools?hl=es-419):
  Integra herramientas como llamadas a funciones y la Búsqueda de Google para interacciones dinámicas.
- [**Transcripciones de audio**](https://ai.google.dev/gemini-api/docs/live-guide?hl=es-419#audio-transcription):
  Proporciona transcripciones de texto de la entrada del usuario y el resultado del modelo.
- [**Audio proactivo**](https://ai.google.dev/gemini-api/docs/live-guide?hl=es-419#proactive-audio):
  Te permite controlar cuándo responde el modelo y en qué contextos.
- [**Diálogo afectivo**](https://ai.google.dev/gemini-api/docs/live-guide?hl=es-419#affective-dialog):
  Adapta el estilo y el tono de la respuesta para que coincidan con la expresión de entrada del usuario.
- [**Traducción instantánea**](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=es-419): Traducción de voz a voz en tiempo real en más de 70 idiomas

## Especificaciones técnicas

En la siguiente tabla, se describen las especificaciones técnicas de la API de Live:

| Categoría | Detalles |
| --- | --- |
| Modalidades de entrada | Audio (audio PCM sin procesar de 16 bits, 16 kHz, little-endian), imágenes (JPEG <= 1 FPS), texto |
| Modalidades de salida | Audio (audio PCM sin procesar de 16 bits, 24 kHz, little-endian) |
| Protocolo | Conexión de WebSocket con estado (WSS) |

## Elige un enfoque de implementación

Cuando realices la integración con la API de Live, deberás elegir uno de los siguientes enfoques de implementación:

- **Servidor a servidor**: Tu backend se conecta a la API de Live con [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Por lo general, tu cliente envía datos de transmisión (audio, video, texto) a tu servidor, que luego los reenvía a la API de Live.
- **Cliente a servidor**: Tu código de frontend se conecta directamente a la API de Live con [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) para transmitir datos, lo que omite tu backend.

## Comenzar

Selecciona la guía que coincida con tu entorno de desarrollo:

De servidor a servidor

### [Instructivo del SDK de IA generativa](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=es-419)

Conéctate a la API de Gemini Live con el SDK de GenAI para compilar una aplicación multimodal en tiempo real con un backend de Python.

Cliente a servidor

### [Tutorial de WebSocket](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=es-419)

Conéctate a la API de Gemini Live con WebSockets para crear una aplicación multimodal en tiempo real con un frontend de JavaScript y tokens efímeros.

Kit de desarrollo de agentes

### [Instructivo de ADK](https://google.github.io/adk-docs/streaming/)

Crea un agente y usa la transmisión del Kit de desarrollo de agentes (ADK) para habilitar la comunicación por voz y video.

## Integraciones a socios

Para optimizar el desarrollo de apps de audio y video en tiempo real, puedes usar una integración de terceros que admita la API de Gemini Live a través de WebRTC o WebSockets.

[LiveKit

Usa la API de Gemini Live con los agentes de LiveKit.](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat de Daily

Crea un chatbot de IA en tiempo real con Gemini Live y Pipecat.](https://docs.pipecat.ai/guides/features/gemini-live)
[Fishjam de Software Mansion

Crea aplicaciones de transmisión de audio y video en vivo con Fishjam.](https://docs.fishjam.io/tutorials/gemini-live-integration)
[Agentes de Vision por transmisión

Crea aplicaciones de IA de voz y video en tiempo real con Vision Agents.](https://visionagents.ai/integrations/gemini)
[Voximplant

Conecta llamadas entrantes y salientes a la API de Live con Voximplant.](https://voximplant.com/products/gemini-client)
[Agora

Crea aplicaciones de IA conversacional en tiempo real con Agora.](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[SDK de Firebase AI

Comienza a usar la API de Gemini Live con Firebase AI Logic.](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=es-419)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-12 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-12 (UTC)"],[],[]]
