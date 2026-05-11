---
source_url: https://ai.google.dev/gemini-api/docs/long-context?hl=es-419
fetched_at: 2026-05-11T04:58:57.820523+00:00
title: "Contexto largo \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Contexto largo

Muchos modelos de Gemini incluyen ventanas de contexto grandes de 1 millón o más tokens.
Históricamente, los modelos de lenguaje grandes (LLMs) estaban limitados de manera significativa por la cantidad de texto (o tokens) que se podían pasar al modelo a la vez.
La ventana de contexto largo de Gemini desbloquea muchos casos de uso y paradigmas de desarrolladores nuevos.

El código que ya usas para casos como la [generación de
texto](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419) o las [entradas
multimodales](https://ai.google.dev/gemini-api/docs/vision?hl=es-419) funcionará sin cambios con un contexto largo.

En este documento, se ofrece una descripción general de lo que puedes lograr con modelos con ventanas de contexto de 1 millón o más tokens. En la página, se ofrece una breve descripción general de una ventana de contexto y se explora cómo los desarrolladores deben pensar en el contexto largo, varios casos de uso reales para un contexto largo y formas de optimizar el uso del contexto largo.

Para conocer los tamaños de las ventanas de contexto de modelos específicos, consulta la
[página Modelos](https://ai.google.dev/gemini-api/docs/models?hl=es-419).

## ¿Qué es una ventana de contexto?

La forma básica de usar los modelos de Gemini es pasar información (contexto) al modelo, que luego generará una respuesta. Una analogía para la ventana de contexto es la memoria a corto plazo. Hay una cantidad limitada de información que se puede almacenar en la memoria a corto plazo de una persona, y lo mismo sucede con los modelos generativos.

Puedes obtener más información sobre cómo funcionan los modelos en nuestra [guía
de modelos generativos](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=es-419#under-the-hood).

## Comienza a usar el contexto largo

Las versiones anteriores de los modelos generativos solo podían procesar 8,000 tokens a la vez. Los modelos más nuevos ampliaron esta capacidad al aceptar 32,000 o incluso 128,000 tokens. Gemini es el primer modelo capaz de aceptar 1 millón de tokens.

En la práctica, 1 millón de tokens se vería de la siguiente manera:

- 50,000 líneas de código (con los 80 caracteres estándar por línea)
- Todos los mensajes de texto que enviaste en los últimos 5 años
- 8 novelas en inglés de longitud promedio
- Transcripciones de más de 200 episodios de podcasts de longitud promedio

Las ventanas de contexto más limitadas que son comunes en muchos otros modelos suelen requerir estrategias como descartar arbitrariamente mensajes antiguos, resumir contenido, usar RAG con bases de datos vectoriales o filtrar instrucciones para guardar tokens.

Si bien estas técnicas siguen siendo valiosas en situaciones específicas, la extensa ventana de contexto de Gemini invita a un enfoque más directo: proporcionar toda la información pertinente por adelantado. Debido a que los modelos de Gemini se crearon con capacidades de contexto masivas, demuestran un aprendizaje en contexto potente. Por
ejemplo, con solo materiales instructivos en contexto (una gramática de referencia de 500
páginas, un diccionario y ≈400 oraciones paralelas), Gemini
[aprendió a traducir](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf)
del inglés al kalamang (un idioma papúa con
menos de 200 hablantes) con una calidad similar a la de un estudiante humano que usa los mismos
materiales. Esto ilustra el cambio de paradigma que permite el contexto largo de Gemini, lo que potencia nuevas posibilidades a través de un aprendizaje en contexto sólido.

## Casos de uso de contexto largo

Si bien el caso de uso estándar para la mayoría de los modelos generativos sigue siendo la entrada de texto, la familia de modelos de Gemini permite un nuevo paradigma de casos de uso multimodales. Estos modelos pueden comprender de forma nativa texto, video, audio e imágenes. Se acompañan de la [API de Gemini que acepta tipos de archivos multimodales para mayor comodidad.](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=es-419)

### Texto de formato largo

El texto demostró ser la capa de inteligencia que sustenta gran parte del impulso en torno a los LLMs. Como se mencionó anteriormente, gran parte de la limitación práctica de los LLMs se debía a que no tenían una ventana de contexto lo suficientemente grande como para realizar ciertas tareas. Esto llevó a la adopción rápida de la generación mejorada de recuperación (RAG) y otras técnicas que proporcionan de forma dinámica al modelo información contextual relevante. Ahora, con ventanas de contexto más y más grandes, hay nuevas técnicas disponibles que permiten casos de uso nuevos.

Estos son algunos casos de uso emergentes y estándar para el contexto largo basado en texto:

- Resumir grandes corpus de texto
  - Las opciones de resumen anteriores con modelos de contexto más pequeños requerirían una ventana deslizante o alguna otra técnica para mantener el estado de las secciones anteriores a medida que se pasan tokens nuevos al modelo.
- Preguntas y respuestas
  - Históricamente, esto solo era posible con RAG, dada la cantidad limitada de contexto y el bajo recuerdo fáctico de los modelos.
- Flujos de trabajo con agentes
  - El texto es la base de cómo los agentes mantienen el estado de lo que hicieron y lo que necesitan hacer; no tener suficiente información sobre el mundo y el objetivo del agente es una limitación en la confiabilidad de los agentes

El [aprendizaje en contexto con muchas tomas](https://arxiv.org/pdf/2404.11018) es una de las capacidades más únicas que permiten los modelos de contexto largos. La investigación demostró que tomar el paradigma de ejemplo común de “una sola toma” o “varias tomas”, en el que se le presenta al modelo uno o algunos ejemplos de una tarea, y aumentarlo a cientos, miles o incluso cientos de miles de ejemplos, puede generar capacidades de modelo nuevas. También se demostró que este enfoque de varias tomas funciona de manera similar a los modelos que se ajustaron para una tarea específica. Para los casos de uso en los que el rendimiento de un modelo de Gemini aún no es suficiente para una implementación de producción, puedes probar el enfoque de varias tomas. Como verás más adelante en la sección de optimización de contexto largo, la caché de contexto hace que este tipo de carga de trabajo de token de entrada alta sea mucho más factible económicamente y, en algunos casos, incluso tenga una latencia más baja.

### Video de formato largo

La utilidad del contenido de video se vio limitada durante mucho tiempo por la falta de accesibilidad del medio en sí. Era difícil hojear el contenido, las transcripciones a menudo no capturaban los matices de un video y la mayoría de las herramientas no procesan imágenes, texto y audio juntos. Con Gemini, las capacidades de texto de contexto largo se traducen en la capacidad de razonar y responder preguntas sobre entradas multimodales con un rendimiento sostenido.

Estos son algunos casos de uso emergentes y estándar para contextos de video largos:

- Preguntas y respuestas sobre videos
- Memoria de video, como se muestra con [el Project Astra de Google](https://deepmind.google/technologies/gemini/project-astra/?hl=es-419)
- Subtitulado de videos
- Sistemas de recomendación de videos, mediante el enriquecimiento de los metadatos existentes con una nueva comprensión multimodal
- Personalización de videos, mediante la observación de un corpus de datos y los metadatos de video asociados, y luego la eliminación de partes de los videos que no son pertinentes para el usuario
- Moderación de contenido de video
- Procesamiento de video en tiempo real

Cuando trabajes con videos, es importante tener en cuenta cómo los [videos se
procesan en tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419#media-token), lo que afecta la
facturación y los límites de uso. Puedes obtener más información sobre las instrucciones con archivos de video en
la [guía de instrucciones](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=es-419#prompting-with-videos).

### Audio de formato largo

Los modelos de Gemini fueron los primeros modelos de lenguaje grandes multimodales de forma nativa que podían comprender audio. Históricamente, el flujo de trabajo típico de los desarrolladores implicaba unir varios modelos específicos del dominio, como un modelo de voz a texto y un modelo de texto a texto, para procesar audio. Esto generó una latencia adicional requerida para realizar varias solicitudes de ida y vuelta y un rendimiento reducido que suele atribuirse a arquitecturas desconectadas de la configuración de varios modelos.

Estos son algunos casos de uso emergentes y estándar para el contexto de audio:

- Transcripciones y traducciones en tiempo real
- Preguntas y respuestas sobre podcasts o videos
- Transcripción y resumen de reuniones
- Asistentes de voz

Puedes obtener más información sobre las instrucciones con archivos de audio en la [guía
de instrucciones](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=es-419#prompting-with-videos).

## Optimizaciones de contexto largo

La optimización principal cuando se trabaja con contexto largo y los modelos de Gemini
es usar [el almacenamiento en caché de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=es-419). Además de la imposibilidad anterior de procesar muchos tokens en una sola solicitud, la otra restricción principal era el costo. Si tienes una app de "chat con tus datos" en la que un usuario carga 10 archivos PDF, un video y algunos documentos de trabajo, históricamente, tendrías que trabajar con una herramienta o un framework de generación mejorada de recuperación (RAG) más complejos para procesar estas solicitudes y pagar una cantidad significativa por los tokens que se mueven a la ventana de contexto. Ahora, puedes almacenar en caché los archivos que sube el usuario y pagar para almacenarlos por hora. El costo de entrada / salida por solicitud con Gemini Flash, por ejemplo, es aproximadamente 4 veces menor que el costo estándar de entrada / salida, por lo que si el usuario chatea con sus datos lo suficiente, se generará un gran ahorro de costos para ti como desarrollador.

## Limitaciones de contexto largo

En varias secciones de esta guía, hablamos sobre cómo los modelos de Gemini logran un alto rendimiento en varias evaluaciones de recuperación de aguja en un pajar. Estas pruebas consideran la configuración más básica, en la que tienes una sola aguja que buscas. En los casos en los que puedas tener varias “agujas” o información específica que buscas, el modelo no funciona con la misma exactitid. El rendimiento puede variar en gran medida según el contexto. Es importante tener en cuenta que existe una compensación inherente entre obtener la información correcta y el costo. Puedes obtener aproximadamente un 99% en una sola consulta, pero debes pagar el costo del token de entrada cada vez que envías esa consulta. Por lo tanto, para recuperar 100 datos, si necesitas un rendimiento del 99%, es probable que debas enviar 100 solicitudes. Este es un buen ejemplo de dónde el almacenamiento en caché de contexto puede reducir significativamente el costo asociado con el uso de modelos de Gemini y, al mismo tiempo, mantener un rendimiento alto.

## Preguntas frecuentes

### ¿Cuál es el mejor lugar para colocar mi consulta en la ventana de contexto?

En la mayoría de los casos, en especial si el contexto total es largo, el rendimiento del modelo será mejor si colocas tu consulta o pregunta al final de la instrucción (después de todo el contexto).

### ¿Pierdo rendimiento del modelo cuando agrego más tokens a una consulta?

En general, si no necesitas que se pasen tokens al modelo, es mejor evitar pasarlos. Sin embargo, si tienes una gran cantidad de tokens con información y quieres hacer preguntas sobre esa información, el modelo es muy capaz de extraer esa información (hasta un 99% de exactitud en muchos casos).

### ¿Cómo puedo reducir mi costo con consultas de contexto largo?

Si tienes un conjunto similar de tokens o contexto que deseas volver a usar muchas
veces, [el almacenamiento en caché de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=es-419) puede ayudar a reducir los costos
asociados con hacer preguntas sobre esa información.

### ¿La longitud del contexto afecta la latencia del modelo?

Hay una cantidad fija de latencia en cualquier solicitud determinada, independientemente del tamaño, pero, en general, las consultas más largas tendrán una latencia más alta (tiempo hasta el primer token).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-04-29 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-04-29 (UTC)"],[],[]]
