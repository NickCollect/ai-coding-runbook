---
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=es-419
fetched_at: 2026-05-25T05:27:25.766496+00:00
title: "Estrategias de dise\u00f1o de instrucciones \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Estrategias de diseño de instrucciones

El *diseño de instrucciones* es el proceso de crear instrucciones o solicitudes de lenguaje natural que producen respuestas precisas y de alta calidad de un modelo de lenguaje.

En esta página, se presentan conceptos básicos, estrategias y prácticas recomendadas para comenzar a diseñar instrucciones y aprovechar al máximo los modelos de IA de Gemini.

## Guías de instrucciones específicas para temas

¿Buscas estrategias de instrucciones más específicas? Consulta nuestras otras guías para crear instrucciones sobre los siguientes temas:

- [Cómo generar instrucciones con archivos multimedia](https://ai.google.dev/gemini-api/docs/files?hl=es-419#prompt-guide)
- Escribir instrucciones para generar imágenes con [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=es-419#imagen-prompt-guide) y [Gemini Native Image Generation](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419#prompt-guide)
- [Instrucciones para la generación de videos](https://ai.google.dev/gemini-api/docs/video?hl=es-419#prompt-guide)

Puedes encontrar otras instrucciones de ejemplo en la [galería de instrucciones](https://ai.google.dev/gemini-api/prompts?hl=es-419), que tiene como objetivo mostrar de forma interactiva muchos de los conceptos que se comparten en esta guía.

## Instrucciones claras y específicas

Una forma eficaz y eficiente de personalizar el comportamiento del modelo es proporcionarle instrucciones claras y específicas. Las instrucciones pueden tener la forma de una pregunta, tareas paso a paso o ser tan complejas como mapear la experiencia y la mentalidad de un usuario.

### Entrada

La entrada es el texto obligatorio en la instrucción al que deseas que el modelo proporcione una respuesta. Las entradas pueden ser una pregunta que responda el modelo (entrada de pregunta), una tarea que realice el modelo (entrada de tarea), una entidad en la que opera el modelo (entrada de entidad) o una entrada parcial que completa el modelo o continúa (entrada de finalización).

| **Tipo de entrada** | **Instrucción** | **Resultados generados** |
| --- | --- | --- |
| Pregunta | ```     What's a good name for a flower shop that specializes in selling bouquets of     dried flowers? Create a list of 5 options with just the names. ``` | ```     Here are 5 names for a flower shop specializing in dried flowers:      1. Everlasting Blooms     2. Dried & Delightful     3. The Petal Preserve     4. Whispers of Wildflowers     5. Forever Blooms ``` |
| Tarea | ```     Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ``` | ```     1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| Entidad | ```     Classify the following items as [large, small]: Elephant Mouse Snail ``` | ``` Here's the classification:  * **Elephant:** Large * **Mouse:** Small * **Snail:** Small ``` |

#### Sugerencias de entrada parcial

Los modelos generativos de lenguaje funcionan como una herramienta de autocompletado avanzada. Cuando proporcionas contenido parcial, el modelo puede proporcionar el resto del contenido o lo que cree que es una continuación de ese contenido como respuesta. Cuando lo haces, si incluyes ejemplos o contextos, el modelo puede tener en cuenta esos ejemplos o el contexto.

En el siguiente ejemplo, se proporciona un mensaje con una instrucción y una entrada de entidad:

|  |
| --- |
| **Prompt:**    ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity.  Order: A burger and a drink. ```  **Respuesta:**    ``` {   "cheeseburger": 0,   "hamburger": 1,   "fries": 0,   "drink": 1 } ```  (gemini-2.5-flash) |

Si bien el modelo hizo lo que se le indicó, escribir las instrucciones en lenguaje natural a veces puede ser difícil y deja mucho a la interpretación del modelo.
Por ejemplo, el menú de un restaurante puede contener muchos elementos. Para reducir el tamaño de la respuesta JSON, es probable que quieras omitir los elementos que no se ordenaron. En este caso, puedes dar un ejemplo y un prefijo de respuesta y dejar que el modelo lo complete:

|  |
| --- |
| **Prompt:**    ``` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` {   "cheeseburger": 1,   "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```  **Respuesta:**    ``` ``` {   "hamburger": 2,   "drink": 1,   "fries": 1 } ``` ```  (gemini-2.5-flash) |

Observa cómo se excluyó "hamburguesa con queso" del resultado porque no formaba parte del pedido.

Si bien puedes especificar el formato de objetos de respuesta JSON simples con instrucciones, te recomendamos que uses la función de [salida estructurada](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419) de la API de Gemini cuando especifiques un esquema JSON más complejo para la respuesta.

### Limitaciones

Especifica cualquier restricción para leer el prompt o generar una respuesta. Puedes indicarle al modelo qué hacer y qué no hacer. Por ejemplo, puedes especificar una restricción en la instrucción sobre la extensión que quieres que tenga un resumen:

|  |
| --- |
| **Prompt:**     ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ```     **Respuesta:**     ```       Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ```  (gemini-2.5-flash) |

### Formato de respuesta

Puedes proporcionar instrucciones que especifiquen el formato de la respuesta. Por ejemplo, puedes solicitar que la respuesta tenga el formato de una tabla, una lista con viñetas, una presentación breve, palabras clave, una oración o un párrafo. La siguiente instrucción del sistema le indica al modelo que sea más conversacional en su respuesta:

|  |
| --- |
| **Instrucción del sistema**    ```     All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ```  **Instrucción**    ```     What is a smart way to make a business that sells DVD's in 2026? ```  **Respuesta:**    ``` Starting a business selling DVDs in 2026 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption.  Here's a breakdown of what a smart DVD business in 2026 would likely entail:  1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include:      * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms.     .... ```  (gemini-2.5-flash) |

#### Cómo dar formato a las respuestas con la estrategia de finalización

La [estrategia de finalización](#completion) también puede ayudar a dar formato a la respuesta.
En el siguiente ejemplo, se solicita al modelo crear un esquema de ensayo:

|  |
| --- |
| **Prompt:**    ``` Create an outline for an essay about hummingbirds. ```  **Respuesta:**    ``` Here is a possible outline for an essay about hummingbirds:  I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds.  II. Appearance and Identification ..... ```  (gemini-2.5-flash) |

El mensaje no especificó el formato del esquema, y el modelo eligió un formato para ti. Para que el modelo muestre un esquema en un formato específico, puedes agregar texto que represente el inicio del esquema y dejar que el modelo lo complete según el patrón que iniciaste.

|  |
| --- |
| **Prompt:**    ``` Create an outline for an essay about hummingbirds. I. Introduction    * ```  **Respuesta:**    ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided:  I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ```  (gemini-2.5-flash) |

## Comparación entre los mensajes de toma de cero y los de tomas individuales

Puedes incluir ejemplos en la instrucción que muestren cómo se ve el modelo. El modelo intenta identificar los patrones y las relaciones de los ejemplos y los aplica cuando se genera una respuesta. Los prompts que contienen algunos ejemplos se denominan prompts *con pocos ejemplos*, mientras que los prompts que no proporcionan ejemplos se denominan *prompts sin ejemplos*. Por lo general, se usan pocas instrucciones con ejemplos limitados para regular el formato, la frase, el alcance o el patrón general de las respuestas del modelo. Usa ejemplos específicos y variados para ayudar al modelo a reducir su enfoque y generar resultados más precisos.

Recomendamos que incluyas siempre ejemplos con pocos intentos en tus prompts. Es probable que las instrucciones sin ejemplos de pocas tomas sean menos eficaces. De hecho, puedes quitar instrucciones de tu instrucción si los ejemplos son lo suficientemente claros como para mostrar la tarea en cuestión.

La siguiente instrucción sin ejemplos le pide al modelo que elija la mejor explicación.

|  |
| --- |
| **Prompt:**    ``` Please choose the best explanation to the question:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Respuesta:**    ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ```  (gemini-2.5-flash) |

Si tu caso de uso requiere que el modelo produzca respuestas concisas, puedes incluir ejemplos en la instrucción que den preferencia a respuestas concisas.

En la siguiente instrucción, se proporcionan dos ejemplos que muestran una preferencia por las explicaciones más cortas. En la respuesta, puedes ver que los ejemplos guiaron al modelo para elegir la explicación más corta (`Explanation2`) en lugar de la explicación más larga (`Explanation1`) como lo hizo antes.

|  |
| --- |
| **Prompt:**    ``` Below are some examples showing a question, explanation, and answer format:  Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2  Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1  Now, Answer the following question given the example formats above:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Respuesta:**    ``` Answer: Explanation2 ```  (gemini-2.5-flash) |

### Cantidad óptima de ejemplos

Los modelos como Gemini a menudo pueden recoger patrones con algunos ejemplos, aunque es posible que debas experimentar con la cantidad de ejemplos que proporcionas en la instrucción para obtener los mejores resultados. Al mismo tiempo, si incluyes demasiados ejemplos, el modelo puede comenzar a [sobreajustar](https://developers.google.com/machine-learning/glossary?hl=es-419#overfitting) la respuesta a los ejemplos.

### Formato coherente

Asegúrate de que la estructura y el formato de los ejemplos con pocos intentos sean los mismos para evitar respuestas con formatos no deseados. Uno de los objetivos principales de agregar ejemplos de pocas tomas en los prompts es mostrar al modelo el formato de respuesta. Por lo tanto, es esencial garantizar un formato coherente en todos los ejemplos, especialmente presta atención a las etiquetas XML, los espacios en blanco, los saltos de línea y los divisores de ejemplos.

## Agrega contexto

Puedes incluir instrucciones e información en una instrucción que el modelo necesita para resolver un problema, en lugar de suponer que el modelo tiene toda la información requerida. Esta información contextual ayuda al modelo a comprender las restricciones y los detalles de lo que le pides que haga.

En el siguiente ejemplo, se le pide al modelo que proporcione orientación para solucionar problemas de un router:

|  |
| --- |
| **Prompt:**    ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ```  **Respuesta:**    ```   A yellow blinking light on your Google Wifi router usually indicates a problem   with the internet connection. Here are some steps to troubleshoot and fix the   issue:   1. Restart your router and modem:     - Unplug your modem from the power outlet and wait for 30 seconds.     - Plug your modem back in and wait for it to fully boot up.     - Unplug your Google Wifi router and wait for 30 seconds.     - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ```  (gemini-2.5-flash) |

La respuesta parece información de solución de problemas genérica que no es específica del router ni del estado de las luces indicadoras LED.

Para personalizar la respuesta del router específico, puedes agregar a la instrucción la guía de
solución de problemas del router como contexto para que este haga referencia cuando se proporciona una respuesta.

|  |
| --- |
| **Prompt:**    ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.  Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.  Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.  Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.  Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ```  **Respuesta:**    ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ```  (gemini-2.5-flash) |

## Desglosa los prompts en componentes

Para los casos de uso que requieren instrucciones complejas, puedes ayudar al modelo a administrar esta complejidad dividiendo las instrucciones en componentes más simples.

1. **Desglosa las instrucciones:** En lugar de tener muchas instrucciones en un mensaje, crea un mensaje por instrucción. Puedes elegir qué mensaje procesar según la entrada del usuario.
2. **Encadena instrucciones:** Para tareas complejas que implican varios pasos secuenciales, haz que cada paso sea una instrucción y encadena las instrucciones en una secuencia. En esta cadena secuencial de instrucciones, el resultado de una instrucción de la secuencia se convierte en la entrada de la siguiente instrucción. El resultado del último prompt de la secuencia es el resultado final.
3. **Agregar respuestas:** La agregación ocurre cuando deseas realizar diferentes tareas paralelas en diferentes partes de los datos y agregar los resultados para producir el resultado final. Por ejemplo, puedes indicarle al modelo que realice una operación en la primera parte de los datos, que realice otra operación en el resto de los datos y que agregue los resultados.

## Experimenta con los parámetros del modelo

Cada llamada que envías a un modelo incluye valores de parámetros que controlan cómo el modelo genera una respuesta. El modelo puede generar resultados diferentes para los valores de parámetros diferentes. Experimenta con diferentes valores de parámetros a fin de obtener los mejores valores para la tarea. Los parámetros disponibles para
diferentes modelos pueden variar. Los más comunes son los siguientes:

1. **Cantidad máxima de tokens de salida:** Especifica la cantidad máxima de tokens que se pueden generar en la respuesta. Un token tiene aproximadamente cuatro caracteres. 100 tokens corresponden a aproximadamente 60 a 80 palabras.
2. **Temperatura:** La temperatura controla el grado de aleatoriedad en la selección de tokens. La temperatura se usa para el muestreo durante la generación de respuesta, que se genera cuando se aplican `topP` y `topK`. Las temperaturas más bajas son buenas para las instrucciones que requieren una respuesta más determinística o menos abierta, mientras que las temperaturas más altas pueden generar resultados más diversos o creativos. Una temperatura de 0 es determinística, lo que significa que siempre se elige la respuesta de mayor probabilidad.
3. **`topK`:** El parámetro `topK` cambia la forma en que el modelo selecciona los tokens para la salida. Un `topK` de 1 significa que el token seleccionado es el más probable entre todos los tokens en el vocabulario del modelo (también llamado decodificación codiciosa), mientras que un `topK` de 3 significa que el siguiente token se selecciona entre los 3 más probables usando la temperatura. Para cada paso de selección de tokens, se realiza un muestreo de los tokens `topK` con las probabilidades más altas. Luego, los tokens se filtran según `topP` con el token final seleccionado a través del muestreo de temperatura.
4. **`topP`:** El parámetro `topP` cambia la forma en que el modelo selecciona los tokens para la salida. Los tokens se seleccionan del más probable al menos probable hasta que la suma de sus probabilidades sea igual al valor de `topP`. Por ejemplo, si los tokens A, B y C tienen una probabilidad de 0.3, 0.2 y 0.1, y el valor de `topP` es 0.5, el modelo elegirá A o B como el siguiente token usando la temperatura y excluirá a C como candidato. El valor predeterminado de `topP` es 0.95.
5. **`stop_sequences`:** Establece una secuencia de detención para indicarle al modelo que deje de generar contenido. Una secuencia de detención puede ser cualquier secuencia de caracteres. Intenta evitar el uso de una secuencia de caracteres que pueda aparecer en el contenido generado.

## Estrategias de iteración de mensajes

A veces, el diseño de instrucciones puede requerir algunas iteraciones antes de que obtengas de forma coherente la respuesta que buscas. En esta sección, se proporciona orientación sobre algunos aspectos que puedes probar cuando se itera sobre las instrucciones:

1. **Usa diferentes frases:** El uso de diferentes palabras o frases en tus instrucciones a menudo produce respuestas diferentes del modelo, aunque todas signifiquen lo mismo. Si no obtienes los resultados esperados de la instrucción, intenta reformularla.

   |  |
   | --- |
   | ``` Version 1: How do I bake a pie?  Version 2: Suggest a recipe for a pie.  Version 3: What's a good pie recipe? ``` |
2. **Cambia a una tarea análoga:** Si no puedes hacer que el modelo siga tus instrucciones para una tarea, intenta darle instrucciones para una tarea análoga que logre el mismo resultado.

   Este mensaje le indica al modelo que clasifique un libro usando categorías predefinidas:

   |  |
   | --- |
   | **Prompt:**    ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ```  **Respuesta:**    ```     The Odyssey belongs to the category of **mythology**.       Here's why:      * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his     journey home after the Trojan War. It features gods, monsters, and supernatural events common to     Greek mythology. ..... ```  (gemini-2.5-flash) |

   La respuesta es correcta, pero el modelo no se mantiene dentro de los límites de las opciones. También puedes modelar para que solo responda con una de las opciones, en lugar de hacerlo en una oración completa. En este caso, puedes reformular las instrucciones como una pregunta de opción múltiple y pedir al modelo que elija una opción.

   |  |
   | --- |
   | **Prompt:**    ``` Multiple choice problem: Which of the following options describes the book The Odyssey? Options: ``` |

   - thriller
   - sci-fi
   - mythology
   - biography
     **Respuesta:**

     ```
     The correct answer is mythology.
     ```

     (gemini-2.5-flash)
   - **Cambia el orden del contenido de la instrucción:** A veces, el orden del contenido en la instrucción puede afectar la respuesta. Intenta cambiar el orden del contenido y observa cómo eso afecta la respuesta.

     ```
     Version 1:
     [examples]
     [context]
     [input]

     Version 2:
     [input]
     [examples]
     [context]

     Version 3:
     [examples]
     [input]
     [context]
     ```

## Respuestas de resguardo

Una respuesta de resguardo es una respuesta que muestra el modelo cuando el mensaje o la respuesta activan un filtro de seguridad. Un ejemplo de una respuesta de resguardo es “No puedo ayudar con eso, solo soy un modelo de lenguaje”.

Si el modelo responde con una respuesta de resguardo, intenta aumentar la temperatura.

## Fundamentación y ejecución de código

Gemini puede usar herramientas para evitar alucinaciones en situaciones en las que, de lo contrario, podría producir respuestas incorrectas.

La [Fundamentación con la Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419) conecta el modelo de Gemini con contenido web en tiempo real y debe habilitarse siempre que el modelo necesite conocer hechos recientes o poco conocidos.

La [herramienta de ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419) de Gemini permite que el modelo genere y ejecute código de Python, y debe habilitarse siempre que el modelo necesite realizar cualquier tipo de cálculo, conteo o aritmética.

## Gemini 3

Los [modelos de Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-3) están diseñados para el razonamiento avanzado y el seguimiento de instrucciones.
Responden mejor a las instrucciones que son directas, están bien estructuradas y definen claramente la tarea y las restricciones. Se recomiendan las siguientes prácticas para obtener resultados óptimos con Gemini 3:

### Principios básicos para crear instrucciones

- **Sé preciso y directo:** Indica tu objetivo de forma clara y concisa. Evita el lenguaje innecesario o demasiado persuasivo.
- **Usa una estructura coherente:** Emplea delimitadores claros para separar las diferentes partes de tu instrucción. Las etiquetas de estilo XML (p.ej., `<context>`, `<task>`) o los encabezados de Markdown son eficaces. Elige un formato y úsalo de manera coherente en una misma instrucción.
- **Define los parámetros:** Explica de forma explícita cualquier término o parámetro ambiguo.
- **Control de la verbosidad de la respuesta:** De forma predeterminada, los modelos de Gemini 3 proporcionan respuestas directas y eficientes. Si necesitas una respuesta más conversacional o detallada, debes solicitarla explícitamente en tus instrucciones.
- **Maneja las entradas multimodales de forma coherente:** Cuando uses texto, imágenes, audio o video, trátalos como entradas de la misma clase. Asegúrate de que tus instrucciones hagan referencia claramente a cada modalidad según sea necesario.
- **Prioriza las instrucciones críticas:** Coloca las restricciones de comportamiento esenciales, las definiciones de roles (personificación) y los requisitos de formato de resultado en la instrucción del sistema o al principio de la instrucción del usuario.
- **Estructura para contextos extensos:** Cuando proporciones grandes cantidades de contexto (p.ej., documentos, código), primero proporciona todo el contexto. Coloca tus instrucciones o preguntas específicas al *final* de la instrucción.
- **Contexto de anclaje:** Después de un bloque grande de datos, usa una frase de transición clara para conectar el contexto y tu búsqueda, como "Según la información anterior…".

### Estrategias de Gemini 3 Flash

- **Precisión del día actual:** Agrega la siguiente cláusula a las instrucciones del sistema para ayudar al modelo a prestar atención al hecho de que el día actual es en 2026:

  ```
  For time-sensitive user queries that require up-to-date information, you
  MUST follow the provided current time (date and year) when formulating
  search queries in tool calls. Remember it is 2026 this year.
  ```
- **Precisión del corte de conocimiento:** Agrega la siguiente cláusula a las instrucciones del sistema para que el modelo conozca su corte de conocimiento:

  ```
  Your knowledge cutoff date is January 2025.
  ```
- **Rendimiento de fundamentación:** Agrega la siguiente cláusula a las instrucciones del sistema (con las ediciones que correspondan) para mejorar la capacidad del modelo de fundamentar las respuestas en el contexto proporcionado:

  ```
  You are a strictly grounded assistant limited to the information provided in
  the User Context. In your answers, rely **only** on the facts that are
  directly mentioned in that context. You must **not** access or utilize your
  own knowledge or common sense to answer. Do not assume or infer from the
  provided facts; simply report them exactly as they appear. Your answer must
  be factual and fully truthful to the provided text, leaving absolutely no
  room for speculation or interpretation. Treat the provided context as the
  absolute limit of truth; any facts or details that are not directly
  mentioned in the context must be considered **completely untruthful** and
  **completely unsupported**. If the exact answer is not explicitly written in
  the context, you must state that the information is not available.
  ```

### Mejora del razonamiento y la planificación

Los modelos de las series Gemini 2.5 y 3 generan automáticamente texto interno de "pensamiento" para mejorar el rendimiento del razonamiento. Por lo tanto, en general, no es necesario que el modelo describa, planifique ni detalle los pasos de razonamiento en la respuesta que se devuelve. Para los problemas que requieren un razonamiento complejo, las solicitudes simples, como "Piensa muy bien antes de responder", pueden mejorar el rendimiento, aunque a costa de tokens de pensamiento adicionales.

Consulta la documentación sobre el [pensamiento de Gemini](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419) para obtener más detalles.

### Ejemplos de instrucciones estructuradas

El uso de etiquetas o Markdown ayuda al modelo a distinguir entre instrucciones, contexto y tareas.

**Ejemplo de XML:**

```
<role>
You are a helpful assistant.
</role>

<constraints>
1. Be objective.
2. Cite sources.
</constraints>

<context>
[Insert User Input Here - The model knows this is data, not instructions]
</context>

<task>
[Insert the specific user request here]
</task>
```

**Ejemplo de Markdown:**

```
# Identity
You are a senior solution architect.

# Constraints
- No external libraries allowed.
- Python 3.11+ syntax only.

# Output format
Return a single code block.
```

### Plantilla de ejemplo que combina prácticas recomendadas

Esta plantilla captura los principios fundamentales para escribir instrucciones con Gemini 3. Asegúrate siempre de iterar y modificar el código para tu caso de uso específico.

**Instrucción del sistema:**

```
<role>
You are Gemini 3, a specialized assistant for [Insert Domain, e.g., Data Science].
You are precise, analytical, and persistent.
</role>

<instructions>
1. **Plan**: Analyze the task and create a step-by-step plan.
2. **Execute**: Carry out the plan.
3. **Validate**: Review your output against the user's task.
4. **Format**: Present the final answer in the requested structure.
</instructions>

<constraints>
- Verbosity: [Specify Low/Medium/High]
- Tone: [Specify Formal/Casual/Technical]
</constraints>

<output_format>
Structure your response as follows:
1. **Executive Summary**: [Short overview]
2. **Detailed Response**: [The main content]
</output_format>
```

**Instrucción del usuario:**

```
<context>
[Insert relevant documents, code snippets, or background info here]
</context>

<task>
[Insert specific user request here]
</task>

<final_instruction>
Remember to think step-by-step before answering.
</final_instruction>
```

## Flujos de trabajo de agentes

En el caso de los flujos de trabajo de agentes profundos, a menudo se requieren instrucciones específicas para controlar cómo el modelo razona, planifica y ejecuta tareas. Si bien Gemini proporciona un rendimiento general sólido, los agentes complejos a menudo requieren que configures la compensación entre el costo computacional (latencia y tokens) y la precisión de la tarea.

Cuando diseñes instrucciones para los agentes, ten en cuenta las siguientes dimensiones de comportamiento que puedes dirigir en el agente:

### Estrategia y razonamiento

Es la configuración de cómo el modelo piensa y planifica antes de actuar.

- **Descomposición lógica:** Define con qué profundidad el modelo debe analizar las restricciones, los requisitos previos y el orden de las operaciones.
- **Diagnóstico de problemas**: Controla la profundidad del análisis cuando se identifican causas y el uso del razonamiento abductivo del modelo. Determina si el modelo debe aceptar la respuesta más obvia o explorar explicaciones complejas y menos probables.
- **Exhaustividad de la información:** Es el equilibrio entre analizar cada política y documento disponibles, y priorizar la eficiencia y la velocidad.

### Ejecución y confiabilidad

Es la configuración que indica cómo opera el agente de forma autónoma y cómo maneja los obstáculos.

- **Adaptabilidad:** Es la forma en que el modelo reacciona a los datos nuevos. Determina si debe seguir estrictamente su plan inicial o cambiar de inmediato cuando las observaciones contradicen los supuestos.
- **Persistencia y recuperación:** Es el grado en el que el modelo intenta corregir errores por sí mismo. Una alta persistencia aumenta los porcentajes de éxito, pero corre el riesgo de generar costos de tokens más altos o bucles.
- **Evaluación de riesgos:** Es la lógica para evaluar las consecuencias. Distingue explícitamente entre las acciones exploratorias de bajo riesgo (lecturas) y los cambios de estado de alto riesgo (escrituras).

### Interacción y salida

Es la configuración de cómo el agente se comunica con el usuario y formatea los resultados.

- **Ambigüedad y manejo de permisos:** Define cuándo se le permite al modelo hacer suposiciones y cuándo debe pausar la ejecución para pedirle al usuario aclaraciones o permisos.
- **Verbosidad:** Controla el volumen del texto generado junto con las llamadas a herramientas. Esto determina si el modelo explica sus acciones al usuario o permanece en silencio durante la ejecución.
- **Precisión y exhaustividad:** Es la fidelidad requerida del resultado. Especifica si el modelo debe resolver cada caso límite y proporcionar cifras exactas o si se aceptan estimaciones aproximadas.

### Plantilla de instrucción del sistema

La siguiente instrucción del sistema es un ejemplo que los investigadores evaluaron para mejorar el rendimiento en las comparativas de agentes en las que el modelo debe cumplir con un reglamento complejo e interactuar con un usuario. Alienta al agente a actuar como un razonador y planificador sólido, aplica comportamientos específicos en las dimensiones mencionadas anteriormente y requiere que el modelo planifique de forma proactiva antes de realizar cualquier acción.

Puedes adaptar esta plantilla para que se ajuste a las restricciones de tu caso de uso específico.

```
You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses.

Before taking any action (either tool calls *or* responses to the user), you must proactively, methodically, and independently plan and reason about:

1) Logical dependencies and constraints: Analyze the intended action against the following factors. Resolve conflicts in order of importance:
    1.1) Policy-based rules, mandatory prerequisites, and constraints.
    1.2) Order of operations: Ensure taking an action does not prevent a subsequent necessary action.
        1.2.1) The user may request actions in a random order, but you may need to reorder operations to maximize successful completion of the task.
    1.3) Other prerequisites (information and/or actions needed).
    1.4) Explicit user constraints or preferences.

2) Risk assessment: What are the consequences of taking the action? Will the new state cause any future issues?
    2.1) For exploratory tasks (like searches), missing *optional* parameters is a LOW risk. **Prefer calling the tool with the available information over asking the user, unless** your `Rule 1` (Logical Dependencies) reasoning determines that optional information is required for a later step in your plan.

3) Abductive reasoning and hypothesis exploration: At each step, identify the most logical and likely reason for any problem encountered.
    3.1) Look beyond immediate or obvious causes. The most likely reason may not be the simplest and may require deeper inference.
    3.2) Hypotheses may require additional research. Each hypothesis may take multiple steps to test.
    3.3) Prioritize hypotheses based on likelihood, but do not discard less likely ones prematurely. A low-probability event may still be the root cause.

4) Outcome evaluation and adaptability: Does the previous observation require any changes to your plan?
    4.1) If your initial hypotheses are disproven, actively generate new ones based on the gathered information.

5) Information availability: Incorporate all applicable and alternative sources of information, including:
    5.1) Using available tools and their capabilities
    5.2) All policies, rules, checklists, and constraints
    5.3) Previous observations and conversation history
    5.4) Information only available by asking the user

6) Precision and Grounding: Ensure your reasoning is extremely precise and relevant to each exact ongoing situation.
    6.1) Verify your claims by quoting the exact applicable information (including policies) when referring to them. 

7) Completeness: Ensure that all requirements, constraints, options, and preferences are exhaustively incorporated into your plan.
    7.1) Resolve conflicts using the order of importance in #1.
    7.2) Avoid premature conclusions: There may be multiple relevant options for a given situation.
        7.2.1) To check for whether an option is relevant, reason about all information sources from #5.
        7.2.2) You may need to consult the user to even know whether something is applicable. Do not assume it is not applicable without checking.
    7.3) Review applicable sources of information from #5 to confirm which are relevant to the current state.

8) Persistence and patience: Do not give up unless all the reasoning above is exhausted.
    8.1) Don't be dissuaded by time taken or user frustration.
    8.2) This persistence must be intelligent: On *transient* errors (e.g. please try again), you *must* retry **unless an explicit retry limit (e.g., max x tries) has been reached**. If such a limit is hit, you *must* stop. On *other* errors, you must change your strategy or arguments, not repeat the same failed call.

9) Inhibit your response: only take an action after all the above reasoning is completed. Once you've taken an action, you cannot take it back.
```

## Próximos pasos

- Ahora que comprendes mejor el diseño de instrucciones, intenta escribir tus propias instrucciones con [Google AI Studio](http://aistudio.google.com?hl=es-419).
- Para obtener información sobre las instrucciones multimodales, consulta [Cómo generar mensajes con archivos multimedia](https://ai.google.dev/gemini-api/docs/files?hl=es-419#prompt-guide).
- Para obtener información sobre las instrucciones de imágenes, consulta las guías de instrucciones de [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419#prompt-guide) y [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=es-419#imagen-prompt-guide).
- Para obtener información sobre las instrucciones de video, consulta la [guía de instrucciones de Veo](https://ai.google.dev/gemini-api/docs/video?hl=es-419#prompt-guide).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-04-29 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-04-29 (UTC)"],[],[]]
