---
source_url: https://ai.google.dev/gemini-api/docs/tools?hl=es-419
fetched_at: 2026-05-11T04:57:33.593310+00:00
title: "Uso de herramientas con la API de Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Uso de herramientas con la API de Gemini

Las herramientas amplían las capacidades de los modelos de Gemini, lo que les permite actuar en el mundo, acceder a información en tiempo real y realizar tareas computacionales complejas. Los modelos pueden usar herramientas en interacciones estándar de solicitud-respuesta y en
sesiones de transmisión en tiempo real con la [API de Live](https://ai.google.dev/gemini-api/docs/live-tools?hl=es-419).

Las herramientas son capacidades específicas (como la Búsqueda de Google o la ejecución de código) que un modelo puede usar para responder consultas. La API de Gemini proporciona un conjunto de herramientas integradas y completamente
administradas, o bien puedes definir herramientas personalizadas con la función [Llamada a
función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419).

Para compilar sistemas de varios pasos orientados a objetivos, consulta la [Descripción general
de los agentes](https://ai.google.dev/gemini-api/docs/agents?hl=es-419).

## Herramientas integradas disponibles

| Herramienta | Descripción | Casos de uso |
| --- | --- | --- |
| [Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419) | Fundamenta las respuestas en hechos y eventos actuales de la Web para reducir las alucinaciones. | \- Responder preguntas sobre eventos recientes   \- Verificar hechos con diversas fuentes |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419) | Compila asistentes que reconozcan la ubicación y puedan encontrar lugares, obtener indicaciones y proporcionar un contexto local enriquecido. | - Planificar itinerarios de viaje con varias paradas   - Encontrar empresas locales según los criterios del usuario |
| [Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419) | Permite que el modelo escriba y ejecute código de Python para resolver problemas matemáticos o procesar datos con precisión. | \- Resolver ecuaciones matemáticas complejas   \- Procesar y analizar datos de texto con precisión |
| [Contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419) | Dirige el modelo para que lea y analice contenido de páginas web o documentos específicos. | \- Responder preguntas basadas en URLs o documentos específicos   \- Recuperar información en diferentes páginas web |
| [Uso de la computadora (vista previa)](https://ai.google.dev/gemini-api/docs/computer-use?hl=es-419) | Permite que Gemini vea una pantalla y genere acciones para interactuar con las IUs del navegador web (ejecución del lado del cliente). | \- Automatizar flujos de trabajo repetitivos basados en la Web   \- Probar las interfaces de usuario de aplicaciones web |
| [Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419) | Indexa y busca tus propios documentos para habilitar la generación mejorada por recuperación (RAG). | - Buscar manuales técnicos   - Búsqueda de respuestas sobre datos de propiedad de la empresa |

Consulta la [página de precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419#pricing_for_tools) para obtener detalles
sobre los costos asociados con herramientas específicas.

## Cómo funciona la ejecución de herramientas

Las herramientas permiten que el modelo solicite acciones durante una conversación. El flujo difiere según si la herramienta es integrada (administrada por Google) o personalizada (administrada por ti).

### Flujo de herramientas integradas

Para las herramientas integradas (Búsqueda de Google, Google Maps, contexto de URL, búsqueda de archivos, ejecución de código), todo el proceso ocurre en una llamada a la API:

1. **Tú** envías una instrucción: "¿Cuál es la raíz cuadrada del precio de las acciones más reciente de GOOG?".
2. **Gemini** decide que necesita herramientas y las ejecuta en los servidores de Google (p.ej., busca el precio de las acciones y, luego, ejecuta código de Python para calcular la raíz cuadrada).
3. **Gemini** envía la respuesta final fundamentada en los resultados de la herramienta.

### Flujo de herramientas personalizadas (llamada a función)

Para las herramientas personalizadas y el uso de la computadora, tu aplicación controla la ejecución:

1. **Tú** envías una instrucción junto con las declaraciones de funciones (herramientas).
2. **Gemini** puede enviar JSON estructurado para llamar a una función específica
   (por ejemplo, `{"name": "get_order_status", "args": {"order_id": "123"}}`),
   siempre con un `id`.
3. **Tú** ejecutas la función en tu aplicación o entorno.
4. **Tú** envías los resultados de la función, con el mismo `id` que la llamada a función, a Gemini.
5. **Gemini** usa los resultados para generar una respuesta final o llamar a otra herramienta.

Obtén más información en la [guía de Llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419).

### Flujo de combinación de herramientas integradas y personalizadas

Para las solicitudes que combinan herramientas integradas y herramientas personalizadas (llamadas a función), el
modelo usa [la circulación del contexto de la herramienta](https://ai.google.dev/gemini-api/docs/toold-combination?hl=es-419) para
coordinar la ejecución en diferentes entornos:

1. **Tú** envías una instrucción y declaras las herramientas integradas y las funciones personalizadas que deseas habilitar, y estableces una marca para activar la compatibilidad con la combinación.
2. **Gemini** ejecuta herramientas integradas y cede al usuario si se genera alguna llamada a función del lado del cliente (lo que se ejecuta primero depende de la instrucción y de lo que decida el modelo). Envía una respuesta con lo siguiente:
   - Confirmación de la llamada a la herramienta
   - Resultados de la respuesta de la herramienta (esto puede aparecer después del JSON si el modelo generó dos llamadas a función paralelas)
   - JSON estructurado para llamar a tu función
   - Firmas de pensamiento encriptadas para preservar el contexto
3. **Tú** ejecutas la función en tu aplicación o entorno.
4. **Tú** muestras todas las partes de la respuesta de Gemini, además de los resultados de la llamada a función.
5. **Gemini** genera la respuesta final con todo el contexto combinado.

Lee la [guía Combinación de herramientas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419) para obtener información sobre
cómo activar la compatibilidad con la combinación de herramientas integradas y personalizadas, y ejemplos de
circulación de contexto.

## Resultados estructurados frente a llamada a función

Gemini ofrece dos métodos para generar resultados estructurados. Usa la función [Llamada a función
cuando el modelo necesite realizar un
paso intermedio conectándose a tus propias herramientas o sistemas de datos.](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) Usa
[resultados estructurados](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419) cuando necesites estrictamente
que la respuesta final del modelo se ajuste a un esquema específico, como para renderizar
una IU personalizada.

## Resultados estructurados con herramientas

Puedes combinar [resultados estructurados](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419) con
herramientas integradas para garantizar que las respuestas del modelo fundamentadas en datos o
cálculos externos sigan ajustándose a un esquema estricto.

Consulta [Resultados estructurados con herramientas](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe&hl=es-419#structured_outputs_with_tools)
para obtener ejemplos de código.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-04-29 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-04-29 (UTC)"],[],[]]
