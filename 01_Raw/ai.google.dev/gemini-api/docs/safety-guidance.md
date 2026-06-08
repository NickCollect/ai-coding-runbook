---
source_url: https://ai.google.dev/gemini-api/docs/safety-guidance?hl=es-419
fetched_at: 2026-06-08T05:30:41.730132+00:00
title: "Orientaci\u00f3n sobre seguridad y facticidad \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Orientación sobre seguridad y facticidad

Los modelos de inteligencia artificial generativa son herramientas potentes, pero no están exentos de limitaciones. Su versatilidad y aplicabilidad a veces pueden generar resultados inesperados, como resultados imprecisos, sesgados u ofensivos. El procesamiento posterior y la evaluación manual rigurosa son esenciales para limitar el riesgo de daño de esos resultados.

Los modelos que proporciona la API de Gemini se pueden usar para una amplia variedad de aplicaciones de IA generativa y procesamiento de lenguaje natural (NLP). El uso de estas
funciones solo está disponible a través de la API de Gemini o la app web
de Google AI Studio. El uso de la API de Gemini también está sujeto a la [Política de Uso Prohibido de IA Generativas](https://policies.google.com/terms/generative-ai/use-policy?hl=es-419) y a las
[Condiciones del Servicio de la API de Gemini](https://ai.google.dev/terms?hl=es-419).

Parte de lo que hace que los modelos de lenguaje grandes (LLM) sean tan útiles es que son herramientas creativas que pueden abordar muchas tareas de lenguaje diferentes. Lamentablemente, esto también implica que los modelos de lenguaje grandes pueden generar resultados inesperados, incluyendo contenido ofensivo, insensible o incorrecto desde el punto de vista fáctico.
Además, la increíble versatilidad de estos modelos es lo que dificulta la predicción exacta de los tipos de resultados no deseados que podrían producir. Si bien la
API de Gemini se diseñó teniendo en cuenta los [principios de IA
de Google](https://ai.google/principles/?hl=es-419), la responsabilidad de aplicar estos modelos de manera responsable recae en los desarrolladores. Para ayudar a los desarrolladores a crear aplicaciones seguras y responsables, la API de Gemini tiene algunos filtros de contenido integrados, así como parámetros de configuración de seguridad ajustables en 4 dimensiones de daño. Consulta la
[guía de parámetros de configuración de seguridad](https://ai.google.dev/gemini-api/docs/safety-settings?hl=es-419) para obtener más información. También ofrece la Fundamentación con la Búsqueda de Google habilitada para mejorar la veracidad, aunque esto se puede inhabilitar para los desarrolladores cuyos casos de uso son más creativos y no buscan información.

El objetivo de este documento es presentarte algunos riesgos de seguridad que pueden surgir cuando se usan LLM y recomendar las nuevas recomendaciones de diseño y desarrollo de seguridad. (Ten en cuenta que las leyes y los reglamentos también pueden imponer restricciones, pero esas consideraciones están fuera del alcance de esta guía).

Se recomiendan los siguientes pasos cuando se compilan aplicaciones con LLM:

- Comprender los riesgos de seguridad de tu aplicación
- Considerar realizar ajustes para mitigar los riesgos de seguridad
- Realizar pruebas de seguridad adecuadas según tu caso de uso
- Solicitar comentarios de los usuarios y supervisar el uso

Las fases de ajuste y prueba deben ser iterativas hasta que alcances el rendimiento adecuado para tu aplicación.

![Ciclo de implementación del modelo](https://ai.google.dev/static/gemini-api/docs/images/safety_diagram.png?hl=es-419)

## Comprende los riesgos de seguridad de tu aplicación

En este contexto, la seguridad se define como la capacidad de un LLM para evitar causar daño a sus usuarios, por ejemplo, generando lenguaje tóxico o contenido que promueva estereotipos. Los modelos disponibles a través de la API de Gemini se diseñaron teniendo en cuenta los [principios de la IA de Google](https://ai.google/principles/?hl=es-419) y su uso está sujeto a la [Política de Uso Prohibido de IA Generativas](https://policies.google.com/terms/generative-ai/use-policy?hl=es-419). La API proporciona filtros de seguridad integrados para ayudar a abordar algunos problemas comunes de los modelos de lenguaje, como el lenguaje tóxico y la incitación al odio o a la violencia, y se esfuerza por lograr la inclusión y evitar los estereotipos. Sin embargo, cada aplicación puede plantear un conjunto diferente de riesgos para sus usuarios. Por lo tanto, como propietario de la aplicación, eres responsable de conocer a tus usuarios y los posibles daños que puede causar tu aplicación, y de asegurarte de que tu aplicación use LLM de forma segura y responsable.

Como parte de esta evaluación, debes considerar la probabilidad de que se produzcan daños y determinar su gravedad y los pasos de mitigación. Por ejemplo, una app que genera ensayos basados en eventos fácticos debería tener más cuidado para evitar la información errónea, en comparación con una app que genera historias de ficción para el entretenimiento. Una buena manera de comenzar a explorar los posibles riesgos de seguridad es investigar a tus usuarios finales y a otras personas que podrían verse afectadas por los resultados de tu aplicación. Esto puede adoptar muchas formas, como investigar estudios de vanguardia en el dominio de tu app, observar cómo las personas usan apps similares o realizar un estudio de usuarios, una encuesta o entrevistas informales con usuarios potenciales.

### Sugerencias avanzadas

- Habla con una combinación diversa de usuarios potenciales dentro de tu público objetivo sobre tu aplicación y su propósito previsto para obtener una perspectiva más amplia sobre los riesgos potenciales y ajustar los criterios de diversidad según sea necesario.
- El [Marco de Administración de Riesgos de IA](https://www.nist.gov/itl/ai-risk-management-framework)
  publicado por el
  Instituto Nacional de Estándares y Tecnología (NIST) del Gobierno de EE.UU. proporciona orientación más
  detallada y recursos de aprendizaje adicionales para la administración de riesgos de IA.
- La publicación de DeepMind sobre los
  [riesgos éticos y sociales de los daños de los modelos de lenguaje](https://arxiv.org/abs/2112.04359)
  describe en detalle las formas en que las aplicaciones de modelos de lenguaje
  pueden causar daño.

## Considera realizar ajustes para mitigar los riesgos de seguridad y veracidad

Ahora que comprendes los riesgos, puedes decidir cómo mitigarlos. Determinar qué riesgos priorizar y qué tanto debes hacer para intentar prevenirlos es una decisión fundamental, similar a la clasificación de errores en un proyecto de software. Una vez que hayas determinado las prioridades, puedes comenzar a pensar en los tipos de mitigaciones que serían más apropiados. A menudo, los cambios simples pueden marcar la diferencia y reducir los riesgos.

Por ejemplo, cuando diseñes una aplicación, considera lo siguiente:

- **Ajustar el resultado del modelo** para reflejar mejor lo que es aceptable en el contexto de tu aplicación. El ajuste puede hacer que el resultado del modelo sea más predecible y coherente y, por lo tanto, puede ayudar a mitigar ciertos riesgos.
- **Proporcionar un método de entrada que facilite resultados más seguros.** La entrada exacta que le das a un LLM puede marcar la diferencia en la calidad del resultado.
  Experimentar con instrucciones de entrada para encontrar lo que funciona de forma más segura en tu caso de uso vale la pena, ya que luego puedes proporcionar una UX que lo facilite. Por ejemplo, puedes restringir a los usuarios para que elijan solo de una lista desplegable de instrucciones de entrada o ofrecer sugerencias emergentes con frases descriptivas que hayas encontrado que funcionan de forma segura en el contexto de tu aplicación.
- **Bloquear las entradas no seguras y filtrar el resultado antes de que se muestre al usuario.** En situaciones simples, se pueden usar listas de entidades bloqueadas para identificar y bloquear palabras o frases no seguras en las instrucciones o respuestas, o bien requerir que los revisores humanos modifiquen o bloqueen manualmente ese contenido.
- **Usar clasificadores entrenados para etiquetar cada instrucción con posibles daños o señales adversas.** Luego, se pueden emplear diferentes estrategias para administrar la solicitud en función del tipo de daño que se detectó. Por ejemplo, si la entrada es de evidente naturaleza adversaria o abusiva, se puede bloquear y, en su lugar, emitir una respuesta predeterminada.
  **Sugerencia avanzada:** Si las señales determinan que el resultado es dañino, la aplicación puede emplear las siguientes opciones:

  - Proporcionar un mensaje de error o una salida predeterminada.
  - Vuelve a probar la instrucción, en caso de que se genere una salida segura alternativa, ya que, a veces, la misma instrucción generará resultados diferentes.
- **Implementar medidas de protección contra el uso indebido deliberado** , como asignar a cada usuario un ID único e imponer un límite en el volumen de consultas de usuarios que se pueden enviar en un período determinado. Otra medida de protección es intentar protegerse contra la posible inserción de instrucciones. La inserción de instrucciones, al igual que la inserción de SQL, es una forma en que los usuarios maliciosos diseñan una instrucción de entrada que manipula el resultado del modelo, por ejemplo, enviando una instrucción de entrada que le indica al modelo que ignore cualquier ejemplo anterior. Consulta la
  [Política de Uso Prohibido de IA Generativas](https://policies.google.com/terms/generative-ai/use-policy?hl=es-419)
  para obtener detalles sobre el uso indebido deliberado.
- **Ajustar la funcionalidad a algo que sea inherentemente de menor riesgo.**
  Las tareas que tienen un alcance más limitado (p.ej., extraer palabras clave de pasajes de texto) o que tienen una mayor supervisión humana (p.ej., generar contenido de formato corto que revisará una persona) suelen representar un riesgo menor. Por lo tanto, por ejemplo, en lugar de crear una aplicación para escribir una respuesta de correo electrónico desde cero, puedes limitarla a expandir un esquema o sugerir frases alternativas.
- **Ajustar los parámetros de configuración de seguridad de contenido dañino para disminuir la probabilidad de que veas respuestas que podrían ser perjudiciales.** La API de Gemini proporciona parámetros de configuración de seguridad que puedes ajustar durante la fase de creación de prototipos para determinar si tu aplicación requiere una configuración de seguridad más o menos restrictiva. Puedes ajustar estos parámetros en cinco categorías de filtros para restringir o permitir ciertos tipos de contenido. Consulta la [guía de parámetros de configuración de seguridad](https://ai.google.dev/gemini-api/docs/safety-settings?hl=es-419) para obtener información sobre
  los parámetros de configuración de seguridad ajustables disponibles a través de la API de Gemini.
- **Habilita la Fundamentación con la Búsqueda de Google para disminuir las posibles imprecisiones o alucinaciones fácticas**. Recuerda que muchos modelos de IA son experimentales y pueden presentar información imprecisa desde el punto de vista fáctico, alucinar o producir resultados problemáticos. La función Fundamentación con la Búsqueda de Google conecta el modelo de Gemini con contenido web en tiempo real y funciona con todos los idiomas disponibles. Esto permite que Gemini proporcione respuestas más precisas y cite fuentes verificables más allá de la fecha límite de conocimiento de los modelos.

## Realiza pruebas de seguridad adecuadas según tu caso de uso

Las pruebas son una parte fundamental de la compilación de aplicaciones sólidas y seguras, pero la extensión, el alcance y las estrategias para las pruebas variarán. Por ejemplo, es probable que un generador de haikus solo por diversión plantee riesgos menos graves que, por ejemplo, una aplicación diseñada para que la usen los bufetes de abogados para resumir documentos legales y ayudar a redactar contratos. Sin embargo, el generador de haikus puede ser usado por una variedad más amplia de usuarios, lo que significa que el potencial de intentos adversarios o incluso entradas dañinas no deseadas puede ser mayor. El contexto de implementación también es importante. Por ejemplo, una aplicación con resultados que revisan expertos humanos antes de que se tome cualquier medida podría considerarse menos propensa a producir resultados dañinos que la aplicación idéntica sin esa supervisión.

No es raro pasar por varias iteraciones de realizar cambios y pruebas antes de sentir confianza de que estás listo para lanzar, incluso para aplicaciones que tienen un riesgo relativamente bajo. Hay dos tipos de pruebas que son particularmente útiles para las aplicaciones de IA:

- **La evaluación comparativa de seguridad** implica diseñar métricas de seguridad que reflejen las formas en que tu aplicación podría ser insegura en el contexto de cómo es probable que se use y, luego, probar qué tan bien se desempeña tu aplicación en las métricas con conjuntos de datos de evaluación. Es una buena práctica pensar en los niveles mínimos aceptables de las métricas de seguridad antes de realizar las pruebas para que 1) puedas evaluar los resultados de las pruebas en función de esas expectativas y 2) puedas recopilar el conjunto de datos de evaluación en función de las pruebas que evalúan las métricas que más te interesan.

  **Sugerencias avanzadas:**

  - Ten cuidado de no depender demasiado de los enfoques “listos para usar”, ya que es probable que necesites compilar tus propios conjuntos de datos de prueba con evaluadores humanos para que se adapten por completo al contexto de tu aplicación.
  - Si tienes más de una métrica, deberás decidir cómo compensarás si un cambio genera mejoras para una métrica en detrimento de otra. Al igual que con otras ingenierías de rendimiento, es posible que desees enfocarte en el rendimiento en el peor de los casos en tu conjunto de evaluación en lugar del rendimiento promedio.
- **Las pruebas adversarias** implican intentar romper tu aplicación de forma proactiva. El objetivo es identificar los puntos débiles para que puedas tomar medidas para solucionarlos según corresponda. Las pruebas adversarias pueden requerir mucho tiempo y esfuerzo de los evaluadores con experiencia en tu aplicación, pero cuanto más lo hagas, mayores serán tus posibilidades de detectar problemas, en especial aquellos que ocurren con poca frecuencia o solo después de ejecuciones repetidas de la aplicación.

  - Las pruebas adversarias son un método para evaluar de manera sistemática un modelo de AA con la intención de aprender cómo se comporta cuando se le proporcionan entradas maliciosas o inadvertidamente dañinas:
    - Una entrada puede ser maliciosa cuando está claro que está diseñada para producir una salida insegura o dañina, por ejemplo, pedirle a un modelo de generación de texto que genere una diatriba de odio sobre una religión en particular.
    - Una entrada es inadvertidamente dañina cuando la entrada en sí puede ser inocua, pero produce una salida dañina, por ejemplo, pedirle a un modelo de generación de texto que describa a una persona de una etnia en particular y recibir una salida racista.
  - Lo que distingue una prueba adversaria de una evaluación estándar es la composición de los datos que se usan para la prueba. Para las pruebas adversarias, selecciona
    datos de prueba que tengan más probabilidades de generar resultados problemáticos de
    l modelo. Esto significa probar el comportamiento del modelo para todos los tipos de daños posibles, incluidos ejemplos poco comunes o inusuales y casos extremos que sean relevantes para las políticas de seguridad. También debe incluir diversidad en las diferentes dimensiones de una oración, como la estructura, el significado y la longitud. Puedes consultar las prácticas de [IA responsable de Google
    en cuanto a la
    equidad](https://ai.google/responsibilities/responsible-ai-practices/?category=fairness&hl=es-419)
    para obtener más detalles sobre qué tener en cuenta cuando compilas un conjunto de datos de prueba.
    **Sugerencias avanzadas:**
  - Usa [pruebas automatizadas](https://www.deepmind.com/blog/red-teaming-language-models-with-language-models?hl=es-419)
    en lugar del método tradicional de reclutar personas en “equipos
    rojos” para intentar romper tu aplicación. En las pruebas automatizadas, el “equipo rojo” es otro modelo de lenguaje que encuentra texto de entrada que genera resultados dañinos del modelo que se está probando.

## Supervisa para detectar problemas

Sin importar cuánto pruebes y mitigues, nunca podrás garantizar la perfección, así que planifica con anticipación cómo detectarás y abordarás los problemas que surjan. Los enfoques comunes incluyen configurar un canal supervisado para que los usuarios compartan comentarios (p.ej., calificación de me gusta o no me gusta) y realizar un estudio de usuarios para solicitar comentarios de forma proactiva de una combinación diversa de usuarios, lo que es especialmente valioso si los patrones de uso son diferentes de las expectativas.

### Sugerencias avanzadas

- Cuando los usuarios envían comentarios a los productos de IA, pueden mejorar en gran medida el rendimiento de la IA y la experiencia del usuario con el tiempo, por ejemplo, ayudándote a elegir mejores ejemplos para el ajuste de instrucciones. En el
  [capítulo Comentarios y control](https://pair.withgoogle.com/chapter/feedback-controls/)
  de la [guía Personas y la IA de Google](https://pair.withgoogle.com/guidebook/chapters)
  , se destacan las consideraciones clave que se deben tener en cuenta cuando se diseñan
  mecanismos de comentarios.

## Próximos pasos

- Consulta la
  [guía de parámetros de configuración de seguridad](https://ai.google.dev/gemini-api/docs/safety-settings?hl=es-419) para obtener información sobre los parámetros de configuración de seguridad ajustables
  disponibles a través de la API de Gemini.
- Consulta la [introducción a las instrucciones](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=es-419) para comenzar a
  escribir tus primeras instrucciones.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-05 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-05 (UTC)"],[],[]]
