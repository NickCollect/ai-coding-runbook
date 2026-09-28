---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=es-419
fetched_at: 2026-09-28T06:30:46.627478+00:00
title: "Desarrolla apps de pila completa en Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Desarrolla apps de pila completa en Google AI Studio

Google AI Studio ahora admite el desarrollo de pila completa, lo que te permite compilar aplicaciones que van más allá de los prototipos del cliente. Con un entorno de ejecución del servidor, puedes administrar secretos, conectarte a APIs externas y crear experiencias multijugador en tiempo real.

## Entorno de ejecución del servidor

Las aplicaciones de Google AI Studio ahora pueden incluir un componente del servidor (Node.js).
Esto te permite hacer lo siguiente:

- **Ejecutar lógica del servidor**: Ejecuta código que no debe exponerse al
  cliente.
- **Acceder a paquetes de npm**: El [agente Antigravity](https://antigravity.google/docs/agent?hl=es-419)
  puede instalar y usar paquetes del vasto ecosistema de npm.
- **Administrar secretos**: Usa de forma segura las claves de API y las credenciales.

### Usar paquetes de npm

No es necesario que ejecutes `npm install` de forma manual. Solo pídele al agente que agregue la funcionalidad que requiere un paquete, y se encargará de la instalación y la importación.

**Ejemplo**: > "Usa `axios` para recuperar datos de la API externa".

## Administrar secretos de forma segura

Con el código del servidor y la administración de secretos, ahora puedes compilar apps que interactúen con el mundo.

### Clave de API de Gemini

Cuando creas una app nueva que usa la API de Gemini, AI Studio configura automáticamente tu `GEMINI_API_KEY` como un secreto del servidor, sin necesidad de configuración manual. Puedes ver esta clave en el panel **Secretos** de Configuración. Las llamadas a la API de Gemini de tu app se realizan desde el código del servidor con esta clave, por lo que nunca se expone en el navegador.

### Claves de API de terceros

Para otros servicios, puedes agregar claves de API de forma manual:

- **APIs de terceros**: Conéctate a servicios como Stripe, SendGrid o APIs de REST personalizadas.
- **Bases de datos**: Conéctate a bases de datos externas (p.ej., a través de Supabase, Firebase,
  o MongoDB Atlas) para conservar los datos más allá de la sesión.

Cuando compilas apps del mundo real, a menudo necesitas conectarte a servicios de terceros (como Twilio, Slack o bases de datos) que requieren claves de API. Puedes agregar claves de forma manual con los siguientes pasos:

1. **Agrega un secreto**: Ve al menú **Configuración** en Google AI Studio y busca
   la sección Secretos.
2. **Almacena tu clave**: Agrega aquí tus claves de API o tokens secretos.
3. **Accede al código**: El agente puede escribir código del servidor que acceda a estos
   secretos de forma segura (por lo general, a través de variables de entorno), lo que garantiza que nunca se
   expongan al navegador del cliente.

Cuando sea necesario, el agente también mostrará una tarjeta en el chat que te solicitará que agregues claves cada vez que se necesite un secreto nuevo o cuando se detecte una clave nueva en las variables de entorno del proyecto.

### Integración de Firebase para la base de datos y la autenticación

Google AI Studio ahora facilita la adición de una base de datos o la autenticación a tu
app a través de una
[integración de Firebase](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=es-419).
El agente Antigravity puede aprovisionar y configurar automáticamente los siguientes servicios:

- **Base de datos de Firestore**: Una base de datos NoSQL flexible, escalable y en la nube para almacenar
  y sincronizar datos para el desarrollo en el cliente y el servidor.
- **Firebase Authentication**: Permite que los usuarios accedan de forma segura a tu
  aplicación con los flujos de "Acceder con Google".

Solo pídele al agente que "agregue una base de datos a mi app" o que "configure el acceso con Google", y se encargará de la configuración necesaria y la generación de código por ti.

Firebase te permite comenzar de forma gratuita y, de manera opcional, escalar con una cuenta pagada cuando estés listo para obtener más cuota o usar funciones pagadas.

## APIs de Google Workspace

Google AI Studio te permite compilar apps que se conectan a las APIs de Google Workspace, de modo que los usuarios puedan trabajar con sus datos reales: correos electrónicos, hojas de cálculo, documentos, eventos del calendario y mucho más, todo dentro de tu app. Ya no necesitas configurar un proyecto de Google Cloud, configurar OAuth ni administrar tu API de forma manual.

### Cómo funciona

Puedes agregar una integración de Workspace de dos maneras:

- **Descríbela en el panel de chat**: Solo dile al agente lo que quieres en el panel de chat en la parte inferior. Por ejemplo, *"Compila un registro de gastos que registre recibos en mi Hoja de cálculo de Google"* o *"Crea un panel que resuma mis mensajes no leídos de Gmail"*
- **Selecciona en el panel de integraciones**: Abre el panel **Integraciones** en la barra lateral derecha del modo de compilación y habilita la app de Workspace a la que deseas conectarte.

Cuando agregas una app de Workspace, AI Studio hace lo siguiente de forma automática:

1. Conecta la API de Google necesaria para tu app.
2. Genera el código del servidor para llamar a la API.
3. Agrega un flujo seguro de "Acceder con Google" para que los usuarios finales de tu app puedan autorizar el acceso a sus propios datos.

### Apps compatibles

Las siguientes apps de Google Workspace están disponibles:

| Aplicación | Qué puedes compilar |
| --- | --- |
| Calendario de Google | Leer, crear y administrar eventos y calendarios |
| Google Chat | Leer e interactuar con conversaciones y espacios grupales |
| Documentos de Google | Crear, leer, actualizar y dar formato a documentos |
| Google Drive | Organizar, buscar y administrar archivos y carpetas |
| Formularios de Google | Crear encuestas, actualizar preguntas y recuperar respuestas |
| Gmail | Leer, enviar y administrar contenido de correo electrónico |
| Google Keep | Administrar notas, listas y archivos adjuntos |
| Google Meet | Programar y administrar videollamadas |
| Contactos | Sincronizar y administrar contactos |
| Hojas de cálculo de Google | Leer, escribir y dar formato a datos de hojas de cálculo |
| Presentaciones de Google | Crear y modificar presentaciones |
| Google Tasks | Crear, administrar y organizar tareas |

### Autenticación y permisos

Como compilador, no necesitas configurar clientes de OAuth, administrar credenciales ni configurar un proyecto de Google Cloud. AI Studio se encarga de todo esto por ti.

Las apps con APIs de Workspace integradas usan "Acceder con Google" para autenticar a los usuarios finales. Cuando un usuario abre tu app, se le solicita que acceda y otorgue los permisos específicos que necesita tu app (por ejemplo, acceso de solo lectura a su calendario o la capacidad de editar una hoja de cálculo). Tu app solo accede a los datos de la persona que la usa. Cada usuario autoriza el acceso a su propia cuenta.

### Ejemplos de instrucciones

Estas son algunas ideas para comenzar a usar las integraciones de Workspace:

- *"Compila una app que lea mi Calendario de Google y redacte correos electrónicos de preparación en
  Gmail para cada reunión."*
- *"Crea una herramienta que tome un Documento de Google y genere una presentación de resumen de 5 diapositivas
  en Presentaciones de Google."*
- *"Crea un registro de gastos en el que suba un recibo, Gemini extraiga los
  detalles y registre una fila nueva en mi Hoja de cálculo de Google"*

### Configura OAuth

Un caso de uso clave para la administración de secretos es configurar OAuth para conectarse a otros sitios web o apps. Cuando tu instrucción incluye instrucciones para conectarse a una app de terceros que requiere autenticación de OAuth, el agente proporcionará instrucciones para configurar OAuth para esa aplicación. Estas instrucciones incluirán las URLs de devolución de llamada necesarias para configurar tu aplicación de OAuth.
También puedes encontrar las URLs de devolución de llamada en **Integraciones** en el panel Configuración.

## Crea experiencias multijugador

El entorno de ejecución de pila completa habilita las funciones de colaboración en tiempo real.

- **Estado en tiempo real**: Puedes pedirle al agente que compile funciones como "un chat
  en vivo", "una pizarra colaborativa" o "un juego multijugador".
- **Sesiones sincronizadas**: El servidor administra el estado, lo que permite que varios usuarios
  interactúen con la misma instancia de la aplicación en tiempo real.

**Ejemplo de instrucción**: > "Haz que este sea un juego multijugador en el que los jugadores puedan ver los cursores de los demás."

### Sugerencias para probar apps multijugador

Puedes probar el modo multijugador de dos maneras antes de implementar tu app.

1. Abre tu app en el modo de compilación de Google AI Studio en varias pestañas. Cuando desarrollas en el modo de compilación, tu app está en un contenedor de desarrollo. Abrir la app en varias pestañas te permitirá simular varios jugadores que usan tu app.
2. Comparte la app con otras personas usando el menú **Compartir** en la esquina superior derecha. Luego, usa la **URL compartida** de la pestaña **Integraciones** del menú **Compartir** para usar la app con los jugadores con los que la compartiste.

## Prácticas recomendadas

- **Llamadas a la API de Gemini**: Tu `GEMINI_API_KEY` se configura automáticamente como un
  secreto del servidor. Realiza llamadas a la API de Gemini desde el código del servidor con esta clave. Puedes verlo en el panel **Secretos**.
- **Seguridad de secretos**: Siempre usa el administrador de secretos para las claves sensibles.
  Nunca los codifiques de forma rígida en tus archivos.
- **Separación de intereses**: Mantén la lógica de la IU en el framework del cliente
  (React/Angular) y la lógica empresarial o el manejo de datos en el servidor.
- **Manejo de errores**: Asegúrate de que el código del servidor controle de forma sólida los errores
  de las llamadas a la API externa para evitar que la app falle.

## ¿Qué sigue?

- [Compila apps en Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=es-419)
- [Implementa desde Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=es-419)
- [Galería de apps](https://aistudio.google.com/apps?source=showcase&hl=es-419)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-08-19 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-08-19 (UTC)"],[],[]]
