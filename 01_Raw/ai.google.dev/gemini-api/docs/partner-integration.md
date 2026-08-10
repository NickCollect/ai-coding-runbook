---
source_url: https://ai.google.dev/gemini-api/docs/partner-integration?hl=es-419
fetched_at: 2026-08-10T03:10:24.657493+00:00
title: "Integraciones de socios y bibliotecas \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Integraciones de socios y bibliotecas

En esta guía, se describen las estrategias de arquitectura para compilar bibliotecas, plataformas y puertas de enlace sobre la API de Gemini. Detalla las compensaciones técnicas entre el uso de los SDKs oficiales de IA generativa, la API directa (REST/gRPC) y la capa de compatibilidad con OpenAI.

Usa esta guía si compilas herramientas para otros desarrolladores, como frameworks de código abierto, puertas de enlace empresariales o agregadores de SaaS, y necesitas optimizar la higiene de las dependencias, el tamaño del paquete o la paridad de funciones.

## ¿Qué es la integración de socios?

Un socio es cualquier persona que cree una integración entre la API de Gemini y los desarrolladores de usuarios finales. Categorizamos a los socios en cuatro arquetipos. Identificar con cuál te identificas más te ayudará a elegir la ruta de integración adecuada.

#### Marco del ecosistema

- **Quién eres:** Mantenedor de un framework de código abierto (p. ej., LangChain, LlamaIndex, Spring AI) o clientes específicos del idioma
- **Tu objetivo:** Amplia compatibilidad. Quieres que tu biblioteca funcione en cualquier entorno que elija el usuario sin forzar conflictos.

#### Plataforma de tiempo de ejecución y de borde

- **Quién eres:** Plataformas de SaaS, puertas de enlace de IA o proveedores de infraestructura en la nube (p.ej., Vercel, Cloudflare, Zapier) en los que la ejecución de código se realiza en entornos restringidos.
- **Tu objetivo:** Rendimiento Necesitas baja latencia, un tamaño de paquete mínimo y rápidos inicios en frío.

#### Agregador

- **Quién eres:** Plataformas, proxies o "Model Gardens" internos que normalizan el acceso a muchos proveedores diferentes de LLM (p.ej., OpenAI, Anthropic, Google) en una sola interfaz.
- **Tu objetivo:** Portabilidad y uniformidad.

#### Puerta de enlace empresarial

- **Quién eres:** Equipos internos de ingeniería de plataformas en grandes empresas que crean "rutas doradas" para cientos de desarrolladores internos.
- **Tu objetivo:** Estandarización, administración y autenticación unificada.

## Comparación rápida

**Práctica recomendada global:** Todos los socios deben enviar el [encabezado `x-goog-api-client`](#client-id), independientemente de la ruta elegida.

| Si eres… | Ruta recomendada | Beneficio clave | Compensación clave | Práctica recomendada |
| --- | --- | --- | --- | --- |
| **Puerta de enlace empresarial, framework del ecosistema** | **[SDK de IA generativa de Google](#genai-sdk)** | **Paridad y velocidad de Gemini Enterprise Agent Platform.** Control integrado para tipos, autenticación y funciones complejas (p. ej., cargas de archivos) Migración sin interrupciones a Google Cloud | **Peso de la dependencia:** Las dependencias transitivas pueden ser complejas y estar fuera de tu control. Se limita a los lenguajes compatibles (Python/Node/Go/Java). | **Bloquea versiones.** Fija las versiones del SDK en tus imágenes base internas para garantizar la estabilidad en todos los equipos. |
| **Framework del ecosistema, plataformas perimetrales y agregadores** | **[API directa](#rest)**  *(REST / gRPC)* | **Sin dependencias.** Controlas el cliente HTTP y el tamaño exacto del paquete. Acceso completo a todas las funciones de la API y el modelo. | **Sobrecarga alta para el desarrollador** Las estructuras JSON pueden estar profundamente anidadas y requieren una validación manual y una verificación de tipos estrictas. | **Usa especificaciones de OpenAPI.** Automatiza la generación de tipos con nuestras especificaciones oficiales en lugar de escribirlas a mano. |
| **Agregador que usa los SDKs de OpenAI que solo requieren flujos de trabajo basados en texto**  *(Optimización para la portabilidad heredada)* | **[Compatibilidad con OpenAI](#openai)** | **Portabilidad instantánea.** Reutiliza código o bibliotecas existentes compatibles con OpenAI. | **Límite de funciones:** Es posible que no estén disponibles las funciones específicas del modelo (video nativo, almacenamiento en caché). | **Plan de migración.** Úsala para la validación rápida, pero planifica actualizar a la API directa para obtener la función completa de la API. |

## Integración del SDK de IA generativa de Google

En el caso de los frameworks, implementar el [SDK de IA generativa de Google](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419) suele ser la ruta más sencilla, ya que requiere la menor cantidad de líneas de código en los lenguajes admitidos.

En el caso de los equipos internos de la plataforma, el principal producto entregable suele ser una "ruta dorada" que permite a los ingenieros de productos avanzar rápido y, al mismo tiempo, cumplir con las políticas de seguridad.

**Beneficios:**

- **Interfaz unificada para la migración de Gemini Enterprise Agent Platform:** Los desarrolladores internos suelen crear prototipos con claves de API (API de Gemini) y realizar implementaciones en Gemini Enterprise Agent Platform (IAM) para cumplir con los requisitos de producción. El SDK abstrae estas diferencias de autenticación.
  Del mismo modo, para los frameworks, puedes implementar una ruta de código y admitir dos conjuntos de usuarios.
- **Asistentes del cliente:** El SDK incluye utilidades idiomáticas que reducen el código repetitivo para tareas complejas.
  - *Ejemplos:* Compatibilidad con objetos de imagen `PIL` directamente en las instrucciones, llamadas a funciones automáticas y tipos integrales.
- **Acceso a las funciones el día del lanzamiento:** Las nuevas funciones de la API están disponibles en el momento del lanzamiento a través de los SDKs.
- **Mejor compatibilidad con la generación de código:** La instalación local del SDK expone definiciones de tipos y cadenas de documentación a los asistentes de programación (p.ej., Cursor y Copilot).
  Este contexto mejora la precisión de la generación de código en comparación con la generación de solicitudes REST sin procesar.

**La compensación:**

- **Peso y complejidad de las dependencias:** Los SDKs tienen sus propias dependencias, lo que puede aumentar el tamaño del paquete y el riesgo de la cadena de suministro.
- **Control de versiones:** Las nuevas funciones de la API suelen estar vinculadas a versiones mínimas del SDK.
  Es posible que debas enviar actualizaciones a los usuarios para que accedan a funciones o modelos nuevos, lo que, en algunos casos, puede requerir cambios en las dependencias transitivas que afecten a tus usuarios.
- **Límites de protocolo:** Los SDKs solo admiten HTTPS para la API principal y WebSockets (WSS) para la API de Live. gRPC no se admite con los clientes de SDK de alto nivel.
- **Compatibilidad con idiomas:** Los SDKs admiten versiones de idiomas *actuales*. Si necesitas admitir versiones EOL (p.ej., Python 3.9), deberás mantener una bifurcación.

**Práctica recomendada:**

- **Bloquea las versiones:** Fija la versión del SDK en tus imágenes base internas para garantizar la estabilidad en todos los equipos.

## Integración directa con la API

Si distribuyes una biblioteca a miles de desarrolladores, ejecutas en un entorno restringido o compilas un agregador que requiere las funciones de vanguardia de Gemini, es posible que debas realizar la integración directamente con la API a través de REST o gRPC.

**Beneficios:**

- **Acceso completo a las funciones:** A diferencia de la capa de compatibilidad con OpenAI, usar la API directamente habilita funciones específicas de Gemini, como la carga en la API de File, la creación de almacenamiento en caché de contenido y el uso de la API de Live bidireccional.
- **Dependencias mínimas:** En un entorno en el que las dependencias son sensibles debido al tamaño o a los costos de auditoría. Usar la API directamente a través de una biblioteca estándar como `fetch` o a través de un wrapper como `httpx` garantiza que tu biblioteca siga siendo ligera.
- **Independiente del lenguaje:** Esta es la única ruta para los lenguajes que no cubren los SDKs, como Rust, PHP y Ruby, ya que no hay restricciones de lenguaje.
- **Rendimiento:** La API de Direct no tiene sobrecarga de inicialización, lo que minimiza los inicios en frío en las funciones sin servidores.

**La compensación:**

- **Implementación manual de Gemini Enterprise Agent Platform:** A diferencia del SDK, usar la API directamente no controla automáticamente las diferencias de autenticación entre AI Studio (clave de API) y Gemini Enterprise Agent Platform (IAM). Debes implementar controladores de autenticación separados si deseas admitir ambos entornos.
- **Sin tipos ni asistentes nativos:** No obtienes finalizaciones de código ni verificaciones en tiempo de compilación para los objetos de solicitud, a menos que los implementes por tu cuenta. No hay "ayudantes" del cliente (p.ej., convertidores de funciones a esquemas), por lo que debes escribir esta lógica de forma manual.

**Práctica recomendada**

Exponemos una especificación legible por máquina que puedes usar para generar definiciones de tipos para tu biblioteca, lo que te ahorra tener que escribirlas a mano. Descarga la especificación durante el proceso de compilación, genera los tipos y envía el código compilado.

- **Extremo:** `https://generativelanguage.googleapis.com/$discovery/OPENAPI3_0`

## Integración del SDK de OpenAI

Si eres una plataforma que prioriza un esquema unificado (finalizaciones de chat de OpenAI) por sobre las funciones específicas del modelo, esta es la ruta más rápida.

**Beneficios:**

- **Baja fricción:** A menudo, puedes agregar compatibilidad con Gemini cambiando `baseURL` y `apiKey`. Esta es una forma rápida de integrar implementaciones de "Aporta tu propia clave", lo que permite agregar compatibilidad con Gemini sin escribir código nuevo.
- **Restricciones:** Esta ruta solo se recomienda si estás limitado al SDK de OpenAI y no necesitas funciones avanzadas de Gemini, como la API de File, o agregar manualmente compatibilidad con herramientas como la fundamentación con la Búsqueda de Google.

**La compensación:**

- **Limitaciones de las funciones:** La capa de compatibilidad proporciona limitaciones a las capacidades principales de Gemini. Las herramientas disponibles del servidor difieren entre las plataformas y pueden requerir un manejo manual para trabajar con las herramientas de la API de Gemini.
- **Sobrecarga de traducción:** Debido a que el esquema de OpenAI no se asigna 1:1 a la arquitectura de Gemini, depender de la capa de compatibilidad introduce algunas complejidades que requieren trabajo de implementación adicional para resolver, como asignar una herramienta de "búsqueda" del usuario a la herramienta de plataforma correcta.
  Si necesitas una gran cantidad de casos especiales, puede ser más valioso usar un SDK o una API dedicados para cada plataforma.

**Práctica recomendada**

Siempre que sea posible, intégrate directamente con la API de Gemini. Sin embargo, para lograr la máxima compatibilidad, considera usar una biblioteca que conozca los diferentes proveedores y pueda controlar la asignación de herramientas y mensajes por ti.

## Práctica recomendada para todos los socios: identificación del cliente

Cuando realices llamadas a la API de Gemini como plataforma o biblioteca, debes identificar tu cliente con el encabezado `x-goog-api-client`.

Esto le permite a Google identificar tus segmentos de tráfico específicos y, si tu biblioteca produce un patrón de error específico, podemos comunicarnos contigo para ayudarte a depurar.

Usa el formato `company-product/version` (p.ej., `acme-framework/1.2.0`).

### Ejemplos de implementación

### SDK de IA generativa

Cuando proporcionas el cliente de API, el SDK agrega automáticamente tu encabezado personalizado a sus encabezados internos.

```
from google import genai

client = genai.Client(
    api_key="...",
    http_options={
        "headers": {
            "x-goog-api-client": "acme-framework/1.2.0",
        }
    }
)
```

### API directa (REST)

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H 'x-goog-api-client: acme-framework/1.2.0' \
    -d '{...}'
```

### SDK de OpenAI

```
from openai import OpenAI

client = OpenAI(
    api_key="...",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    default_headers={
        "x-goog-api-client": "acme-framework-oai/1.2.0",
    }
)
```

## Próximos pasos

- Visita la [descripción general de la biblioteca](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419) para obtener información sobre los SDKs de IA generativa.
- Explora la [referencia de la API](https://ai.google.dev/api?hl=es-419)
- Lee la [guía de compatibilidad de OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=es-419)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-22 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-22 (UTC)"],[],[]]
