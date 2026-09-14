---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=es-419
fetched_at: 2026-09-14T05:46:15.838887+00:00
title: "Acelera el descubrimiento con Gemini para la investigaci\u00f3n \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)

# Acelera el descubrimiento con Gemini para la investigación

[Obtén una clave de API de Gemini](https://aistudio.google.com/apikey?hl=es-419)

Los modelos de Gemini se pueden usar para avanzar en la investigación fundamental en todas las disciplinas.
Estas son algunas formas en las que puedes explorar Gemini para tu investigación:

- **Analiza y controla los resultados del modelo**: Para realizar un análisis más detallado, puedes examinar un candidato a respuesta generado por el modelo con herramientas como `CitationMetadata`. También puedes configurar opciones para la generación y los resultados del modelo, como `responseSchema`, `topP` y `topK`. [Obtén más información](https://ai.google.dev/api/generate-content?hl=es-419).
- **Entradas multimodales**: Gemini puede procesar imágenes, audio y videos, lo que permite una gran cantidad de emocionantes direcciones de investigación. [Obtén más información](https://ai.google.dev/gemini-api/docs/vision?hl=es-419).
- **Capacidades de contexto extenso**: Gemini 3.0 Flash y Pro incluyen una ventana de contexto de 1 millón de tokens. [Obtén más información](https://ai.google.dev/gemini-api/docs/long-context?hl=es-419).
- **Crece con Google**: Accede rápidamente a los modelos de Gemini a través de la API y Google AI Studio para casos de uso de producción. Si buscas una plataforma basada en Google Cloud, Gemini Enterprise Agent Platform puede proporcionar infraestructura de asistencia adicional.

Para respaldar la investigación académica y promover la investigación de vanguardia, Google proporciona acceso a créditos de la API de Gemini para científicos e investigadores académicos a través del [Programa Académico de Gemini](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=es-419#gemini-academic-program).

## Comienza a usar Gemini

La API de Gemini y Google AI Studio te ayudan a comenzar a trabajar con los modelos más recientes de Google y a convertir tus ideas en aplicaciones que se pueden escalar.

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="How large is the universe?",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "How large is the universe?"}]
    }]
   }'
```

## Académicos destacados

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=es-419)

"Nuestra investigación analiza Gemini como un modelo de lenguaje visual (VLM) y sus comportamientos de agente en diversos entornos desde perspectivas de solidez y seguridad. Hasta ahora, evaluamos la solidez de Gemini ante distracciones, como ventanas emergentes, cuando los agentes de VLM realizan tareas en la computadora, y aprovechamos Gemini para analizar la interacción social, los eventos temporales y los factores de riesgo en función de la entrada de video".

[Sitio web de Diyi Yang](https://cs.stanford.edu/~diyiy/)

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=es-419)

"Gemini Pro y Flash, con su larga ventana de contexto, nos han ayudado en OK-Robot, nuestro proyecto de manipulación móvil de vocabulario abierto. Gemini permite realizar consultas y comandos complejos en lenguaje natural sobre la "memoria" del robot: en este caso, las observaciones anteriores que realizó el robot durante un largo período de funcionamiento. Mahi Shafiullah y yo también usamos Gemini para desglosar tareas en código que el robot puede ejecutar en el mundo real".

[Sitio web de Lerrel Pinto](https://www.lerrelpinto.com/)

## Programa académico de Gemini

Los investigadores académicos calificados (como el cuerpo docente, el personal y los estudiantes de doctorado) de los [países admitidos](https://ai.google.dev/gemini-api/docs/available-regions?hl=es-419) pueden solicitar créditos de la API de Gemini y límites de frecuencia más altos para proyectos de investigación. Esta compatibilidad permite una mayor capacidad de procesamiento para los experimentos científicos y avanza la investigación.

Nos interesan especialmente las áreas de investigación que se mencionan en la siguiente sección, pero aceptamos solicitudes de diversas disciplinas científicas:

- **Evaluaciones y comparativas**: Métodos de evaluación respaldados por la comunidad que pueden proporcionar una señal de rendimiento sólida en áreas como la facticidad, la seguridad, el cumplimiento de instrucciones, el razonamiento y la planificación.
- **Acelerar el descubrimiento científico en beneficio de la humanidad**: Aplicaciones potenciales de la IA en la investigación científica interdisciplinaria, incluidas áreas como las enfermedades raras y desatendidas, la biología experimental, la ciencia de los materiales y la sustentabilidad
- **Incorporación e interacciones**: Utilizar modelos de lenguaje grandes para investigar interacciones novedosas en los campos de la IA incorporada, las interacciones ambientales, la robótica y la interacción humano-computadora
- **Capacidades emergentes**: Exploramos nuevas capacidades de agentes necesarias para mejorar el razonamiento y la planificación, y cómo se pueden expandir las capacidades durante la inferencia (p.ej., utilizando Gemini Flash).
- **Interacción y comprensión multimodales**: Identificar brechas y oportunidades para los modelos de base multimodales para el análisis, el razonamiento y la planificación en una variedad de tareas

Elegibilidad: Solo pueden postularse personas físicas (miembros del cuerpo docente, investigadores o equivalentes) afiliadas a una institución académica o una organización de investigación académica válidas. Ten en cuenta que el acceso a la API y los créditos se otorgarán y quitarán a discreción de Google. Revisamos las solicitudes todos los meses.

### Comienza a investigar con la API de Gemini

[Postularse ahora](https://forms.gle/HMviQstU8PxC5iCt5)

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-12 (UTC)

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-12 (UTC)"],[],[]]
