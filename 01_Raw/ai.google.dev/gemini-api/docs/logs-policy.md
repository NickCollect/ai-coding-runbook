---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=es-419
fetched_at: 2026-10-12T07:02:18.631781+00:00
title: "Registro y uso compartido de datos \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Registro y uso compartido de datos

En esta página, se describe el almacenamiento y la administración de
[los registros de la API de Gemini](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=es-419), que son datos de la
API propiedad del desarrollador de llamadas admitidas a la API de Gemini para proyectos con la facturación habilitada. Los registros abarcan todo el proceso, desde la solicitud de un usuario hasta la respuesta del modelo.
Estos registros, que son privados para tu proyecto de Google Cloud, están separados de los
registros que se conservan únicamente con fines de [supervisión de abusos](https://ai.google.dev/gemini-api/docs/usage-policies?hl=es-419).

## Datos que se pueden compartir

Como propietario del proyecto, puedes habilitar el registro de las llamadas a la API de Gemini para tu propio uso o para enviar comentarios y compartirlos con Google para ayudarnos a mejorar continuamente nuestros modelos.

Si habilitas el registro, puedes ayudarnos a crear sistemas de IA que sigan siendo valiosos para los desarrolladores en varios campos y casos de uso. Para ello, puedes contribuir con los siguientes datos para mejorar los productos y el entrenamiento de modelos:

- **Conjuntos de datos:** Usa la interfaz de registros y conjuntos de datos de Google AI Studio para elegir los registros (solicitudes, respuestas, metadatos, etcétera) de interés de las llamadas admitidas a la API de Gemini. Estos se aportan a través de la inclusión en conjuntos de datos, con la opción de inhabilitar la participación durante la creación del conjunto de datos.
- **Comentarios:** Cuando revises los registros, puedes enviar comentarios, incluidas las calificaciones de Me gusta y No me gusta, y cualquier comentario escrito que proporciones.

Cuando compartes un conjunto de datos con Google, tus registros en ese conjunto de datos, incluidas las
solicitudes y las respuestas, se procesarán de acuerdo con nuestras
[Condiciones](https://developers.google.com/terms?hl=es-419) de los
"[Servicios no pagados](https://ai.google.dev/gemini-api/terms?hl=es-419#data-use-unpaid)",
lo que significa que el conjunto de datos se puede usar para desarrollar y mejorar los
productos, los servicios y las tecnologías de aprendizaje automático de Google, lo que incluye mejorar y
entrenar nuestros modelos. **No incluyas información personal, sensible ni confidencial.**

## Cómo usamos tus datos

Los registros se conservan durante un período máximo predeterminado de 55 días. Después de este período, los registros se marcan automáticamente para su eliminación. La ventana de retención de almacenamiento de un proyecto se puede actualizar en AI Studio para marcar automáticamente los registros para su eliminación después de 7, 14, 28 o 55 días.

[Se pueden crear conjuntos de datos](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=es-419) para conservar los registros de
interés más allá del período de retención establecido para casos de uso posteriores y la
contribución opcional a las mejoras del modelo. Los registros almacenados en conjuntos de datos no tienen períodos de retención establecidos.

De forma predeterminada, debido a que el registro solo está disponible para los proyectos habilitados para la facturación,
las instrucciones y las respuestas dentro de los registros no se usan para mejorar o
desarrollar productos, de acuerdo con nuestras [Condiciones](https://developers.google.com/terms?hl=es-419)
sobre el uso de datos.

Si decides compartir conjuntos de datos de tus registros con Google, esos conjuntos de datos se usarán como datos de demostración del mundo real para comprender mejor la diversidad de dominios y contextos en los que se usan los sistemas y las aplicaciones de IA. Estos datos se pueden usar para mejorar la calidad del modelo y para informar el entrenamiento y la evaluación de futuros modelos y servicios. Estos datos se procesan de acuerdo con nuestras condiciones de uso de datos
para los [Servicios no pagados](https://ai.google.dev/gemini-api/terms?hl=es-419#data-use-unpaid).

En consecuencia, los revisores humanos pueden leer, anotar y procesar las entradas y salidas de la API que compartes. Antes de que se usen los datos para mejorar el modelo, Google toma medidas para proteger la privacidad del usuario como parte de este proceso. Esto incluye desvincular estos datos de tu Cuenta de Google, clave de API o proyecto de Cloud antes de que los revisores los analicen o les agreguen anotaciones.

## Permisos de datos

Si decides contribuir con datos de la API, confirmas que tienes los permisos necesarios para que Google procese y use los datos como se describe en esta documentación. **No contribuyas con registros que contengan información sensible, confidencial o de propiedad obtenida a través del servicio pagado**.
La licencia que usted le otorga a Google en virtud del artículo "[Envío de Contenido](https://developers.google.com/terms?hl=es-419#b_submission_of_content)"
de las Condiciones de las APIs también incluye, en la medida en que lo exijan las leyes aplicables
para nuestro uso, cualquier contenido (p.ej., las instrucciones, incluidas las instrucciones del sistema asociadas,
el contenido almacenado en caché y los archivos, como imágenes, videos o documentos) que envíe a los Servicios y las respuestas generadas.

## Uso compartido de datos y comentarios

Puedes ayudarnos a avanzar en la frontera de la investigación de IA, la API de Gemini y Google AI Studio si decides compartir tus datos como ejemplos, lo que nos permite mejorar continuamente nuestros modelos en varios contextos y crear sistemas de IA que sigan siendo valiosos para los desarrolladores en varios campos y casos de uso.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-08 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-08 (UTC)"],[],[]]
