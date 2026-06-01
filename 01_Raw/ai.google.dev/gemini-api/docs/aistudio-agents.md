---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=es-419
fetched_at: 2026-06-01T06:05:56.335582+00:00
title: "Agentes en AI Studio Playground \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Agentes en AI Studio Playground

Google AI Studio Playground proporciona una interfaz visual para crear prototipos y aprender a compilar agentes administrados sin tener que crear ni escribir llamadas a la API.

Para comenzar, navega a la pestaña **Playground** en el panel de navegación de Google AI Studio y cambia el botón de activación a **Agentes**.

## Plantillas prediseñadas

La pestaña **Agentes** tiene una serie de plantillas que preconfiguran el agente base de Antigravity estableciendo configuraciones de herramientas y entorno. Todas las plantillas son de código abierto y se publican en el repositorio [google-gemini/gemini-managed-agents-templates](https://github.com/google-gemini/gemini-managed-agents-templates/). Explorar estas plantillas es una excelente manera de aprender a crear y estructurar tu propio agente administrado.

Por ejemplo, cuando eliges la plantilla de IA Radio, se habilitan todas las herramientas permitidas y se vinculan un archivo `AGENTS.md` especializado y habilidades para la producción de programas de radio. Puedes ver estos parámetros de configuración en la IU de Playground en la sección **Environment**. Para ello, haz clic en el botón **Sources**.

## Configuración de herramientas

En la configuración del agente en Playground, puedes activar o desactivar el acceso a las siguientes herramientas integradas:

- **Búsqueda de Google:** Accede a la Web abierta para fundamentar la información en tiempo real.
- **Contexto de URL:** Recupera y analiza el contenido de texto de URLs de páginas web específicas.
- **Ejecución de código:** Ejecuta comandos de Bash y Python directamente en el entorno aislado de zona de pruebas.
- **Herramientas del sistema de archivos:** Lee, escribe, enumera y borra archivos dentro del espacio de trabajo.

## Configuración del entorno

Los agentes administrados se ejecutan en una zona de pruebas de Linux efímera y segura (el entorno) que proporciona el espacio de trabajo y las herramientas que necesitan para operar. Para obtener más información, consulta la guía del [entorno de agente administrado](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419).

### Cómo controlar el comportamiento del agente

El comportamiento, la personalidad y las capacidades del agente se determinan principalmente por los archivos presentes en su entorno. El agente detecta y carga automáticamente la configuración desde una carpeta `.agents` especial:

- **`AGENTS.md`**: Se carga previamente en el contexto del agente para definir las instrucciones y la personalidad del sistema.
- **`SKILL.md`**: Se encuentra en las carpetas de habilidades respectivas (p.ej., `.agents/skills/my-skill/SKILL.md`) para definir capacidades y flujos de trabajo específicos.

### Aprovisiona el entorno

Puedes configurar el entorno que usará el agente. Para ello, debes activar archivos en el entorno antes de iniciar una sesión. Puedes compilar un entorno nuevo con la incorporación de fuentes o restablecer uno anterior:

- **Para crear un entorno nuevo**, haz clic en **Agregar fuentes** en el panel Configuración del entorno y elige entre los siguientes tipos de fuentes:

| Tipo de fuente | Descripción | Ruta de montaje |
| --- | --- | --- |
| **Archivos intercalados** | Escribe o pega archivos de configuración, conjuntos de datos simulados o secuencias de comandos de utilidad (hasta 100 KB) directamente en la IU de Playground. | Ruta de destino definida por el usuario (p. ej., `/workspace/scripts/parser.py`) |
| **Google Cloud Storage** | Activar un bucket público o privado de Cloud Storage.  Los buckets privados requieren un token del portador OAuth 2.0 estándar. Para obtener más información, consulta [Fuentes privadas](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419#private-sources). | Asigna una ruta de acceso a un bucket de GCS (p.ej., `gs://your-bucket-name/data/`) a un directorio de espacio de trabajo (p.ej., `/workspace/data/`). |
| **Repositorios de GitHub** | Clona bases de código públicas o privadas.  Los repositorios privados requieren autenticación básica con tu token de acceso personal (PAT) de GitHub. Para obtener más información, consulta [Fuentes privadas](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419#private-sources). | Se clonó directamente en `/workspace/` (por lo general, en `/workspace/<repo-name>`). |

- **Para restablecer un entorno anterior**, puedes [reutilizar un ID de entorno existente](#reusing-an-existing-environment-id) para clonar y bifurcar su estado exacto.

### Cómo reutilizar un ID de entorno existente

Si ya dedicaste tiempo a configurar un entorno de zona de pruebas, no tienes que comenzar desde cero. Para usar un entorno existente, haz lo siguiente:

1. Ve al panel Environments en AI Studio y cambia **Type** a **Existing**.
2. Ingresa el **ID del entorno** (p. ej., `env_abc123`).

Para obtener más información, consulta [Cómo configurar un entorno](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419#configure-an-environment). También puedes recuperar el ID del entorno de la sesión actual en la pestaña Environment de la IU.

Una vez que envíes tu primer mensaje al agente, la configuración del entorno se fijará para esa sesión. No puedes activar fuentes nuevas ni modificar la lista de entidades permitidas de la red mientras la interacción se esté ejecutando de forma activa.

## Descarga el entorno

Una vez que se crea un entorno, puedes descargar la instantánea del entorno en cualquier momento con el botón **Descargar** en la configuración del entorno de AI Studio Playground para recuperar los archivos del entorno como un archivo tar.

## Seguridad y administración de costos

### Administra el consumo de tokens

A diferencia de una solicitud de chat estándar que produce un solo resultado, el agente de Antigravity ejecuta un flujo de trabajo autónomo. Planifica, ejecuta código, observa los resultados y realiza iteraciones. Esto significa que una sola instrucción puede generar un consumo ilimitado de tokens.

Para administrar los costos, **proporciona criterios de finalización claros en tus instrucciones y delimita las tareas del agente**. Un buen ejemplo podría ser una instrucción como
*Revisa la solicitud de extracción y detente una vez que hayas generado el resumen en Markdown.
No intentes escribir la corrección por tu cuenta*.

### Costos adicionales

De forma predeterminada, todas las plantillas de agentes en Playground tienen acceso al servicio de la API de Gemini y pueden realizar llamadas a la API desde el entorno para satisfacer las solicitudes. Es posible que se generen costos adicionales que no se reflejarán en el consumo de tokens.

Del mismo modo, si agregas otros servicios externos, es posible que el agente incurra en costos adicionales por llamar a estos servicios en tu nombre.

### Lista de entidades permitidas de la red

De forma predeterminada, en AI Studio, todas las solicitudes de red salientes desde el entorno de zona de pruebas de tu agente se controlan y restringen estrictamente para garantizar la seguridad. Para otorgarle a tu agente la capacidad de acceder a APIs externas, servicios web o administradores de paquetes, debes declararlos de forma explícita:

1. Ve al panel Entornos en AI Studio.
2. Selecciona el botón **rules** junto a **Network**.
3. En el panel **Configuración de red**, haz clic en **Agregar a la lista de entidades permitidas** y completa los detalles pertinentes:
   - **Restricción de dominio:** Solo se puede acceder a los dominios específicos o los patrones de comodín que se agregaron a la lista desde la máquina virtual del agente. Por ejemplo, puedes ingresar dominios exactos, como `api.github.com`, o patrones amplios, como `*.googleapis.com`.
   - **Agrega encabezados HTTP y la inserción de tokens:** Usa la opción **Agregar encabezado HTTP** para insertar de forma segura las credenciales requeridas (como un token de API) para un dominio específico. Estas credenciales pasan de forma segura a través de un proxy de salida y nunca se exponen directamente como texto sin formato dentro de la zona de pruebas del agente.

Siempre ten cuidado cuando agregues dominios a tu lista de entidades permitidas. Si le otorgas acceso a servicios autenticados, el agente podrá actuar en tu nombre, lo que podría generar acciones no deseadas si no se supervisa con cuidado.

### Prácticas recomendadas para las credenciales

Si tu flujo de trabajo requiere que el agente se autentique con servicios externos, eres responsable de aprovisionar y definir el alcance de esas credenciales. Sigue estos lineamientos para reducir el riesgo:

- **Usa credenciales con privilegios mínimos:** Crea cuentas de servicio o claves de API con solo los permisos que necesita tu agente. Evita pasar credenciales con acceso amplio o administrativo.
- **Prefiere los tokens de corta duración:** Cuando sea posible, usa credenciales o tokens con límite de tiempo que vencen en lugar de claves de API de larga duración.
- **Asume acceso completo:** El agente puede usar cualquier credencial a la que tenga acceso para completar la tarea que le asignaste. Solo proporciona credenciales cuyo alcance completo de acceso estés dispuesto a otorgar.
- **Rota las credenciales con regularidad:** Trata las credenciales compartidas con el agente de la misma manera en que tratarías cualquier credencial programática; rótalas de forma regular.

### Conexión de APIs y herramientas externas

Puedes conectar herramientas y APIs externas (como los servidores del Protocolo de contexto del modelo o MCP) para ampliar las capacidades del agente. Cuando lo hagas, ten en cuenta lo siguiente:

- Solo conecta herramientas de fuentes confiables. Una herramienta maliciosa o mal escrita podría exponer datos o realizar acciones no deseadas.
- Configura las herramientas con los permisos mínimos necesarios para tu caso de uso. Si una herramienta admite el modo de solo lectura, úsalo, a menos que las escrituras sean estrictamente necesarias.
- Antes de conectar una herramienta a una fuente de datos de producción, pruébala con datos de muestra o sintéticos para verificar que el agente la use según lo previsto.

### Supervisión humana

Los agentes pueden razonar, planificar y ejecutar flujos de trabajo de varios pasos con un alto grado de autonomía. Si bien esto es potente, también significa que debes aplicar una supervisión adecuada, en especial para las tareas que modifican datos o interactúan con sistemas externos.

Siempre verifica los resultados críticos, como el código generado, las transformaciones de datos o los cambios de configuración, antes de implementarlos.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-20 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-20 (UTC)"],[],[]]
