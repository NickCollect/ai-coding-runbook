---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=es-419
fetched_at: 2026-06-01T06:08:56.576780+00:00
title: "Gu\u00eda de soluci\u00f3n de problemas \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Guía de solución de problemas

Usa esta guía para diagnosticar y resolver problemas comunes que surgen cuando llamas a la API de Gemini. Es posible que encuentres problemas en el servicio de backend de la API de Gemini o en los SDKs de cliente. Nuestros SDKs para clientes son de código abierto y se encuentran en los siguientes repositorios:

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

Si tienes problemas con la clave de API, verifica que la hayas configurado correctamente según la [guía de configuración de la clave de API](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419).

## Códigos de error del servicio de backend de la API de Gemini

En la siguiente tabla, se enumeran los códigos de error de backend comunes que puedes encontrar, junto con explicaciones de sus causas y pasos para solucionar problemas:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Código HTTP** | **Estado** | **Descripción** | **Ejemplo** | **Solución** |
| 400 | INVALID\_ARGUMENT | El cuerpo de la solicitud tiene un formato incorrecto. | Hay un error de escritura o falta un campo obligatorio en tu solicitud. | Consulta la [referencia de la API](https://ai.google.dev/api?hl=es-419) para conocer el formato de la solicitud, los ejemplos y las versiones compatibles. Usar funciones de una versión de API más reciente con un extremo anterior puede causar errores. |
| 400 | FAILED\_PRECONDITION | El nivel gratuito de la API de Gemini no está disponible en tu país. Habilita la facturación en tu proyecto de Google AI Studio. | Estás realizando una solicitud en una región en la que no se admite el nivel gratuito y no habilitaste la facturación en tu proyecto en Google AI Studio. | Para usar la API de Gemini, deberás configurar un plan pagado con [Google AI Studio](https://aistudio.google.com/app/apikey?hl=es-419). |
| 403 | PERMISSION\_DENIED | Tu clave de API no tiene los permisos necesarios. | Estás usando la clave de API incorrecta o intentas usar un modelo ajustado sin pasar por la [autenticación adecuada](https://ai.google.dev/gemini-api/docs/model-tuning?hl=es-419). | Verifica que tu clave de API esté configurada y tenga el acceso correcto. Además, asegúrate de realizar la autenticación adecuada para usar los modelos ajustados. |
| 404 | NOT\_FOUND | No se encontró el recurso solicitado. | No se encontró un archivo de imagen, audio o video al que se hace referencia en tu solicitud. | Verifica si todos los [parámetros de tu solicitud son válidos](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=es-419#check-api) para tu versión de la API. |
| 429 | RESOURCE\_EXHAUSTED | Superaste el límite de frecuencia. | Estás enviando demasiadas solicitudes por minuto con el nivel gratuito de la API de Gemini. | Verifica que estés dentro del [límite de frecuencia](https://ai.google.dev/gemini-api/docs/rate-limits?hl=es-419) del modelo. [Solicita un aumento de la cuota](https://ai.google.dev/gemini-api/docs/rate-limits?hl=es-419#request-rate-limit-increase) si es necesario. |
| 499 | CANCELADO | La operación se canceló (por lo general, la cancela el emisor). | El cliente cerró la conexión antes de que la API pudiera terminar de responder. | Verifica si tu cliente o infraestructura de red están cerrando la conexión de forma prematura (p.ej., debido a un tiempo de espera del cliente). |
| 500 | INTERNAL | Se produjo un error inesperado en Google. | El contexto de entrada es demasiado largo. | Consulta la [página de estado de la API de Gemini](https://aistudio.google.com/status?hl=es-419) para ver si hay incidentes en curso. Reduce el contexto de entrada o cambia temporalmente a otro modelo (p.ej., de Gemini 2.5 Pro a Gemini 2.5 Flash) y comprueba si funciona. O bien espera un momento y vuelve a intentarlo. Si el problema persiste después de volver a intentarlo, infórmalo con el botón **Enviar comentarios** en Google AI Studio. |
| 503 | NO DISPONIBLE | Es posible que el servicio esté inactivo o temporalmente sobrecargado. | El servicio se está quedando sin capacidad temporalmente. | Consulta la [página de estado de la API de Gemini](https://aistudio.google.com/status?hl=es-419) para ver si hay incidentes en curso. Cambia temporalmente a otro modelo (p.ej., de Gemini 2.5 Pro a Gemini 2.5 Flash) y observa si funciona. O bien espera un momento y vuelve a intentarlo. Si el problema persiste después de volver a intentarlo, infórmalo con el botón **Enviar comentarios** en Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | El servicio no puede terminar el procesamiento dentro de la fecha límite. | Tu instrucción (o contexto) es demasiado grande para procesarse a tiempo. | Establece un "tiempo de espera" más largo en la solicitud del cliente para evitar este error. |

## Verifica si hay errores en los parámetros del modelo en tus llamadas a la API

Verifica que los parámetros del modelo se encuentren dentro de los siguientes valores:

|  |  |
| --- | --- |
| **Parámetro del modelo** | **Valores (rango)** |
| Recuento de candidatos | 1 a 8 (número entero) |
| Temperatura | 0.0-1.0 |
| Cantidad máxima de tokens de salida | Usa la [página de modelos](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419) para determinar la cantidad máxima de tokens del modelo que usas. |
| TopP | 0.0-1.0 |

Además de verificar los valores de los parámetros, asegúrate de usar la [versión de la API](https://ai.google.dev/gemini-api/docs/api-versions?hl=es-419) correcta (p.ej., `/v1` o `/v1beta`) y el modelo que admite las funciones que necesitas. Por ejemplo, si una función está en versión beta, solo estará disponible en la versión de la API de `/v1beta`.

## Comprueba si tienes el modelo correcto

Verifica que estés usando un modelo compatible que se encuentre en nuestra [página de modelos](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419).

## Mayor latencia o uso de tokens con los modelos 2.5

Si observas una mayor latencia o uso de tokens con los modelos 2.5 Flash y Pro, esto puede deberse a que vienen con la **función de pensamiento habilitada de forma predeterminada** para mejorar la calidad. Si priorizas la velocidad o necesitas minimizar los costos, puedes ajustar o inhabilitar el pensamiento.

Consulta la [página de sugerencias](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419#set-budget) para obtener orientación y código de muestra.

## Problemas de seguridad

Si ves que se bloqueó una instrucción debido a un parámetro de configuración de seguridad en la llamada a la API, revisa la instrucción en relación con los filtros que estableciste en la llamada a la API.

Si ves `BlockedReason.OTHER`, es posible que la búsqueda o la respuesta incumplan las [condiciones del servicio](https://ai.google.dev/terms?hl=es-419) o que no se admitan.

## Problema de recitación

Si ves que el modelo deja de generar resultados debido al motivo de RECITACIÓN, significa que el resultado del modelo puede parecerse a ciertos datos. Para solucionar este problema, intenta que la instrucción o el contexto sean lo más únicos posible y usa una temperatura más alta.

## Problema de tokens repetitivos

Si ves tokens de salida repetidos, prueba las siguientes sugerencias para reducirlos o eliminarlos.

| Descripción | Causa | Solución alternativa sugerida |
| --- | --- | --- |
| Guiones repetidos en tablas de Markdown | Esto puede ocurrir cuando el contenido de la tabla es largo, ya que el modelo intenta crear una tabla de Markdown alineada visualmente. Sin embargo, la alineación en Markdown no es necesaria para el procesamiento correcto. | Agrega instrucciones en tu instrucción para darle al modelo lineamientos específicos para generar tablas de Markdown. Proporciona ejemplos que sigan esos lineamientos. También puedes intentar ajustar la temperatura. Para generar código o resultados muy estructurados, como tablas de Markdown, se ha demostrado que una temperatura alta funciona mejor (≥ 0.8).  A continuación, se incluye un ejemplo de un conjunto de lineamientos que puedes agregar a tu instrucción para evitar este problema:     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Tokens repetidos en tablas de Markdown | Al igual que con los guiones repetidos, esto ocurre cuando el modelo intenta alinear visualmente el contenido de la tabla. La alineación en Markdown no es necesaria para el procesamiento correcto. | - Intenta agregar instrucciones como las siguientes a tu instrucción del sistema:      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - Intenta ajustar la temperatura. Las temperaturas más altas (≥ 0.8) suelen ayudar a eliminar las repeticiones o la duplicación en el resultado. |
| Saltos de línea repetidos (`\n`) en el resultado estructurado | Cuando la entrada del modelo contiene secuencias de escape o Unicode, como `\u` o `\t`, puede generar saltos de línea repetidos. | - Verifica y reemplaza las secuencias de escape prohibidas por caracteres UTF-8 en tu instrucción. Por ejemplo, la secuencia de escape `\u` de tus ejemplos de JSON puede hacer que el modelo también la use en su resultado. - Indica al modelo los escapes permitidos. Agrega una instrucción del sistema como esta:      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| Texto repetido con salida estructurada | Cuando el resultado del modelo tiene un orden diferente para los campos que el esquema estructurado definido, esto puede generar texto repetido. | - No especifiques el orden de los campos en tu instrucción. - Haz que todos los campos de salida sean obligatorios. |
| Llamadas a herramientas repetitivas | Esto puede ocurrir si el modelo pierde el contexto de pensamientos anteriores o llama a un extremo no disponible al que se ve obligado a llamar. | Indícale al modelo que mantenga el estado dentro de su proceso de pensamiento. Agrega lo siguiente al final de las instrucciones del sistema:    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| Texto repetitivo que no forma parte de la salida estructurada | Esto puede ocurrir si el modelo se atasca en una solicitud que no puede resolver. | - Si el pensamiento está activado, evita dar órdenes explícitas sobre cómo pensar en un problema en las instrucciones. Solo pide el resultado final. - Prueba con una temperatura más alta, mayor o igual a 0.8. - Agrega instrucciones como "Sé conciso", "No te repitas" o "Proporciona la respuesta una sola vez". |

## Claves de API bloqueadas o que no funcionan

En esta sección, se describe cómo verificar si tu clave de la API de Gemini está bloqueada y qué hacer al respecto.

### Comprende por qué se bloquean las llaves

Identificamos una vulnerabilidad por la que algunas claves de API podrían haberse expuesto públicamente. Para proteger tus datos y evitar el acceso no autorizado, bloqueamos de forma proactiva el acceso a la API de Gemini de estas claves filtradas conocidas.

### Confirma si tus llaves están afectadas

Si se sabe que se filtró tu clave, ya no podrás usarla con la API de Gemini. Puedes usar [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=es-419) para ver si alguna de tus claves de API está bloqueada para llamar a la API de Gemini y generar claves nuevas. También es posible que veas el siguiente error cuando intentes usar estas claves:

```
Your API key was reported as leaked. Please use another API key.
```

### Acción para las claves de API bloqueadas

Debes generar nuevas claves de API para tus integraciones de la API de Gemini con [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=es-419). Te recomendamos que revises tus prácticas de administración de claves de API para asegurarte de que las claves nuevas estén protegidas y no se expongan públicamente.

### Cargos inesperados debido a vulnerabilidades

[Envía un caso de asistencia para la facturación](https://console.cloud.google.com/support/chat?hl=es-419).
Nuestro equipo de facturación está trabajando en este problema y te comunicaremos las actualizaciones lo antes posible.

### Medidas de seguridad de Google para las claves filtradas

**¿Cómo me ayudará Google a proteger mi cuenta del abuso y el exceso de costos si se filtran mis claves de API?**

- Estamos trabajando para emitir claves de API cuando solicites una nueva con [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=es-419), que, de forma predeterminada, se limitará solo a Google AI Studio y no aceptará claves de otros servicios.
  Esto ayudará a evitar el uso no deseado de teclas cruzadas.
- De forma predeterminada, bloqueamos las claves de API que se filtran y se usan con la API de Gemini, lo que ayuda a evitar el abuso de los costos y los datos de tu aplicación.
- Podrás encontrar el estado de tus claves de API en [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=es-419), y trabajaremos para comunicarnos de forma proactiva cuando identifiquemos que se filtraron tus claves de API para que tomes medidas de inmediato.

## Mejora el resultado del modelo

Para obtener resultados de mayor calidad, explora la escritura de instrucciones más estructuradas. En la página de la [guía de ingeniería de instrucciones](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=es-419), se presentan algunos conceptos básicos, estrategias y prácticas recomendadas para comenzar.

## Información sobre los límites de tokens

Lee nuestra [Guía de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419) para comprender mejor cómo contar tokens y sus límites.

## Problemas conocidos

- La API solo admite una cantidad de idiomas seleccionados. Si envías instrucciones en idiomas no admitidos, es posible que se generen respuestas inesperadas o incluso bloqueadas. Consulta los [idiomas disponibles](https://ai.google.dev/gemini-api/docs/models?hl=es-419#supported-languages) para ver las actualizaciones.

## Informa un error

Si tienes preguntas, únete al debate en el [foro para desarrolladores de IA de Google](https://discuss.ai.google.dev?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-28 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-28 (UTC)"],[],[]]
