---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=es-419
fetched_at: 2026-06-01T05:58:31.456225+00:00
title: "Descripci\u00f3n general de los agentes \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Descripción general de los agentes

Los agentes administrados en la API de Gemini te brindan un arnés de agente configurable. Una sola llamada a la API aprovisiona una zona de pruebas de Linux en la que el agente razona, ejecuta código, administra archivos y navega por la Web de forma autónoma.

[rocket\_launch

Guía de inicio rápido

Realiza tu primera llamada al agente, transmite respuestas y crea un agente personalizado.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=es-419)
[smart\_toy

Agente de Antigravity

Funciones, herramientas, entrada multimodal y precios para el agente predeterminado.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419)
[experiment

Agentes en AI Studio

Entorno de pruebas visual para crear prototipos de agentes sin escribir código.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=es-419)

## Agentes administrados disponibles

- **[Agente de Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419)**: Agente administrado
  de uso general con tecnología de Gemini 3.5 Flash. Ejecuta código, administra archivos y busca en la Web dentro de una zona de pruebas segura de Linux alojada por Google. Puedes
  extenderlo con tus propias instrucciones, habilidades y datos para
  [crear un agente personalizado](https://ai.google.dev/gemini-api/docs/custom-agents?hl=es-419).
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419)**: Agente de investigación autónomo
  que planifica, ejecuta y sintetiza tareas de investigación de varios pasos para casos de uso
  como análisis de mercado, diligencia debida y revisiones de literatura.

## Seguridad y prácticas recomendadas

Cada agente se ejecuta en un entorno de zona de pruebas aislado a nivel del SO.
De forma predeterminada, la zona de pruebas tiene acceso de red saliente sin restricciones. Puedes restringir o inhabilitar el acceso a la red con una lista de entidades permitidas.

### Acceso a la red

De forma predeterminada, los entornos tienen acceso de red saliente sin restricciones. Usa una lista de entidades permitidas `network` para restringir el tráfico saliente a dominios específicos o patrones comodín. Para obtener detalles sobre la configuración, consulta
[Lista de entidades permitidas de red](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=es-419#network_allow_list) (AI
Studio) o [Reglas de red](https://ai.google.dev/gemini-api/docs/custom-agents?hl=es-419#with_network_rules)
(API).

### Herramientas y APIs externas

Puedes conectar herramientas y APIs externas para extender el agente. Usa solo herramientas de fuentes confiables y permisos de alcance al mínimo requerido. Las credenciales se pueden insertar de forma segura a través de transformaciones de encabezado de proxy de salida y nunca se exponen dentro de la zona de pruebas. El agente puede usar cualquier credencial a la que tenga acceso, por lo que solo debes proporcionar credenciales cuyo alcance completo estés dispuesto a otorgar.

- Usa cuentas de servicio o claves de API con privilegios mínimos.
- Prefiere los tokens de corta duración a las claves de larga duración.
- Solo proporciona credenciales cuyo alcance completo estés dispuesto a otorgar.
- Rota las credenciales con regularidad.

Para obtener detalles sobre la configuración de las transformaciones de encabezado, consulta
[Credenciales](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419#credentials).

### Supervisión humana

Siempre verifica los resultados (código generado, transformaciones de datos, cambios de configuración) antes de implementarlos, en especial para las tareas que modifican datos o interactúan con sistemas externos.

## Precios

Los agentes administrados usan un [modelo de pago por uso](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419#pricing-for-agents) basado en tokens del modelo de Gemini y uso de herramientas. Una sola interacción puede activar varios bucles de razonamiento, que suelen consumir entre 100,000 y 3 millones de tokens. El procesamiento del entorno **no se factura** durante la versión preliminar. Consulta los [costos estimados](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419#availability-and-pricing) para los desgloses por tarea.

## Límites

| Límite | Descripción |
| --- | --- |
| **Tiempo de actividad del entorno** | Los entornos se borran de forma permanente después de 7 días de inactividad. |
| **Apagado de VM** | Las VMs se apagan después de un breve período de inactividad para conservar los recursos. La siguiente solicitud restablece el estado (con un inicio en frío). |
| **Software preinstalado** | Entorno basado en Ubuntu con Python 3.12 y Node.js 22. Para obtener más información sobre la imagen base del entorno, consulta [Software preinstalado](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419#pre-installed-software). |
| **Cantidad máxima de agentes** | Puedes tener hasta 1,000 agentes administrados. |

## Frameworks de agentes

También puedes crear agentes con Gemini usando estos frameworks y SDKs:

- [**\*\*LangChain / LangGraph\*\***](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=es-419): Crea
  flujos de aplicaciones complejos con estado y sistemas multiagente con estructuras de gráficos.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=es-419): Conecta agentes de Gemini a
  tus datos privados para flujos de trabajo mejorados con RAG.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=es-419): Organiza agentes de IA autónomos y colaborativos que interpretan roles.
- [**SDK de IA de Vercel**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=es-419): Crea
  interfaces de usuario y agentes con tecnología de IA en JavaScript o TypeScript.
- [**\*\*ADK de Google\*\***](https://google.github.io/adk-docs/get-started/python/): Es un
  framework de código abierto para crear y organizar agentes de IA
  interoperables.
- [**SDK de Antigravity**](https://antigravity.google/product/antigravity-sdk?hl=es-419): Crea
  agentes de IA autónomos con las mismas herramientas, bucle de agente y administración de contexto
  que impulsan Google Antigravity, programable en Python.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-20 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-20 (UTC)"],[],[]]
