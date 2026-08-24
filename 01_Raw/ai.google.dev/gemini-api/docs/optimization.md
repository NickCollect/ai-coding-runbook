---
source_url: https://ai.google.dev/gemini-api/docs/optimization?hl=es-419
fetched_at: 2026-08-24T02:29:51.511222+00:00
title: "Optimizaci\u00f3n e inferencia de la API de Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Optimización e inferencia de la API de Gemini

La API de Gemini ofrece una variedad de mecanismos de optimización para ayudarte a equilibrar la velocidad, el costo y la confiabilidad según las necesidades específicas de tu carga de trabajo.
Ya sea que estés creando bots conversacionales en tiempo real o ejecutando canalizaciones de procesamiento de datos sin conexión pesadas, elegir el paradigma adecuado puede reducir significativamente los costos o aumentar el rendimiento.

| Función | Estándar | Flexible | Prioridad | Lote | Almacenamiento en caché |
| --- | --- | --- | --- | --- | --- |
| **Precios** | Precio completo | 50% de descuento | Entre un 75% y un 100% más que el estándar | 50% de descuento | 90% de descuento + almacenamiento de tokens prorrateado |
| **Latencia** | De segundos a minutos | Minutos (objetivo de 1 a 15 min) | Segundos | Hasta 24 horas | Tiempo hasta el primer token más rápido |
| **Confiabilidad** | Alta / media-alta | Mejor esfuerzo (descartable) | Alta (no se desprende) | Alta (para la capacidad de procesamiento) | N/A |
| **Interfaz** | Síncrona | Síncrona | Síncrona | Asíncrono | Estado guardado |
| **Mejor caso de uso** | Flujos de trabajo generales de la aplicación | Cadenas secuenciales no urgentes | Apps de producción para el usuario | Conjuntos de datos masivos y evaluaciones sin conexión | Consultas recurrentes sobre el mismo archivo |

## Niveles de servicio de inferencia (síncronos)

Puedes cambiar entre el tráfico síncrono optimizado para la confiabilidad y el optimizado para el costo pasando el parámetro `service_tier` en tus llamadas de generación estándar.

### Inferencia estándar (predeterminada)

El nivel estándar es la opción predeterminada para la generación de contenido secuencial.
Proporciona tiempos de respuesta normales sin primas adicionales ni largas filas.

- **Confiabilidad:** Criticidad estándar
- **Precio:** Precios estándar.
- **Ideal para:** La mayoría de las aplicaciones interactivas cotidianas.

### Inferencia prioritaria (optimización de latencia)

El procesamiento con [prioridad](https://ai.google.dev/gemini-api/docs/priority-inference?hl=es-419) dirige tus solicitudes a colas de procesamiento de alta criticidad.
Este tráfico es estrictamente no descartable (nunca se interrumpe por otros niveles) y ofrece la mayor confiabilidad. Si superas los límites de prioridad dinámica, el sistema degradará correctamente la solicitud al procesamiento estándar en lugar de fallar con un error.

- **Confiabilidad:** Criticidad más alta
- **Precio:** Entre un 75% y un 100% más que las tarifas estándar.
- **Ideal para:** Chatbots de atención al cliente, detección de fraudes en tiempo real y copilotos fundamentales para la empresa.

### Inferencia flexible (con optimización de costos)

[Flex inference](https://ai.google.dev/gemini-api/docs/flex-inference?hl=es-419) ofrece un 50% de descuento en comparación con las tarifas estándar, ya que utiliza capacidad de procesamiento oportunista fuera de las horas pico. Las solicitudes se procesan de forma síncrona, lo que significa que no es necesario que reescribas el código para administrar objetos por lotes.
Dado que es tráfico "descartable", es posible que las solicitudes se interrumpan si el sistema experimenta picos de tráfico estándar.

- **Confiabilidad:** Criticidad descartable y no garantizada
- **Precio:** El 50% del precio estándar (se factura por token).
- **Ideal para:** Flujos de trabajo de agentes de varios pasos en los que la llamada N+1 depende del resultado de la llamada N, actualizaciones del CRM en segundo plano y evaluaciones sin conexión.

## API de Batch (masiva y asíncrona)

[La API de Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419) está diseñada para procesar grandes volúmenes de solicitudes de forma asíncrona con el 50% del costo estándar. Puedes enviar solicitudes como diccionarios intercalados o con un archivo de entrada JSONL (hasta 2 GB). Procesa las solicitudes con colas de capacidad de procesamiento en segundo plano con un tiempo de respuesta objetivo de 24 horas.

- **Confiabilidad:** Descartable, pero con reintentos automáticos y sistema de filas de espera las 24 horas
- **Precio:** El 50% del precio estándar.
- **Ideal para:** Realizar el procesamiento previo de conjuntos de datos masivos, ejecutar conjuntos de pruebas de regresión periódicas y generar grandes volúmenes de imágenes o incorporaciones

## Almacenamiento de contexto en caché (ahorro de entradas)

El [almacenamiento en caché de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=es-419) se usa cuando las solicitudes más cortas hacen referencia repetidamente a un contexto inicial sustancial.

- **Almacenamiento en caché implícito:** Se habilita automáticamente en los modelos de Gemini 2.5 y versiones posteriores.
  El sistema transfiere los ahorros de costos si tu solicitud alcanza las cachés existentes basadas en prefijos de instrucciones comunes.
- **Almacenamiento en caché explícito:** Puedes crear manualmente un objeto de caché con un tiempo de actividad (TTL) específico. Una vez creados, puedes consultar los tokens almacenados en caché para las solicitudes posteriores y evitar pasar la misma carga útil del corpus de forma repetida.
- **Precio:** Se factura según la cantidad de tokens de caché y la duración del almacenamiento (TTL).
- **Ideal para:** Chatbots con instrucciones del sistema extensas, análisis repetitivos de archivos de video largos o consultas en grandes conjuntos de documentos

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-04-29 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-04-29 (UTC)"],[],[]]
