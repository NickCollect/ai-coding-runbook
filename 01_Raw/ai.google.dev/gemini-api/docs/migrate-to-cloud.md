---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=es-419
fetched_at: 2026-05-25T05:19:40.697437+00:00
title: "Comparaci\u00f3n entre la API de Gemini Developer y Agent Platform de Gemini Enterprise \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Comparación entre la API de Gemini Developer y Agent Platform de Gemini Enterprise

Cuando desarrollas soluciones de IA generativa con Gemini, Google ofrece dos productos de API:
la [API de Gemini Developer](https://ai.google.dev/gemini-api/docs?hl=es-419) y la [API de Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=es-419).

La API de Gemini Developer proporciona la ruta más rápida para compilar, producir y escalar aplicaciones potenciadas por Gemini. La mayoría de los desarrolladores deberían usar la API de Gemini Developer, a menos que necesiten controles empresariales específicos.

Gemini Enterprise Agent Platform ofrece un ecosistema integral de funciones y servicios listos para la empresa para compilar e implementar aplicaciones de IA generativa respaldadas por Google Cloud.

Recientemente, simplificamos la migración entre estos servicios. Ahora se puede acceder a la API de Gemini
Developer y a la API de Gemini Enterprise Agent Platform a través del
[SDK unificado de Google Gen AI](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419).

## Comparación de código

En esta página, se incluyen comparaciones de código en paralelo entre las guías de inicio rápido de la API de Gemini Developer y Gemini Enterprise Agent Platform para la generación de texto.

### Python

Puedes acceder a los servicios de la API de Gemini Developer y Gemini Enterprise Agent Platform a través de la biblioteca `google-genai`. Consulta la página de [bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419)
para obtener instrucciones sobre cómo instalar `google-genai`.

### API de Gemini Developer

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### API de Gemini Enterprise Agent Platform

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript y TypeScript

Puedes acceder a los servicios de la API de Gemini Developer y Gemini Enterprise Agent Platform a través de la biblioteca `@google/genai`. Consulta la página de [bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419) para obtener instrucciones sobre cómo
instalar `@google/genai`.

### API de Gemini Developer

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### API de Gemini Enterprise Agent Platform

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

Puedes acceder a los servicios de la API de Gemini Developer y Gemini Enterprise Agent Platform a través de la biblioteca `google.golang.org/genai`. Consulta la página de [bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419) para obtener instrucciones sobre cómo
instalar `google.golang.org/genai`.

### API de Gemini Developer

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### API de Gemini Enterprise Agent Platform

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your GCP project
const project = "your-project"

// A GCP location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Otros casos prácticos y plataformas

Consulta las guías específicas de casos prácticos en la documentación de la API de [Gemini Developer](https://ai.google.dev/gemini-api/docs?hl=es-419)
y la documentación de [Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=es-419)
para obtener información sobre otras plataformas y casos prácticos.

## Consideraciones sobre la migración

Cuando migres, ten en cuenta lo siguiente:

- Deberás usar cuentas de servicio de Google Cloud para autenticarte. Consulta la [documentación de Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=es-419)
  para obtener más información.
- Puedes usar tu proyecto existente de Google Cloud
  (el mismo que usaste para generar tu clave de API) o puedes
  [crear un proyecto nuevo de Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=es-419).
- Las regiones compatibles pueden diferir entre la API de Gemini Developer y la API de Gemini Enterprise Agent Platform. Consulta la lista de
  [regiones compatibles para la IA generativa en Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=es-419).
- Todos los modelos que creaste en Google AI Studio deben volver a entrenarse en Gemini Enterprise Agent Platform.

Si ya no necesitas usar tu clave de API de Gemini para la API de Gemini Developer, sigue las prácticas recomendadas de seguridad y bórrala.

Para borrar una clave de API, haz lo siguiente:

1. Abre la
   [página Credenciales de la API de Google Cloud](https://console.cloud.google.com/apis/credentials?hl=es-419).
2. Busca la clave de API que deseas borrar y haz clic en el ícono **Acciones**.
3. Selecciona **Borrar clave de API**.
4. En la ventana modal **Borrar credencial**, selecciona **Borrar**.

   Borrar una clave de API por completo demora algunos minutos. Una vez que finalice este proceso, el tráfico que use la clave de API borrada se rechazará.

## Próximos pasos

- Consulta la
  [descripción general de la IA generativa en Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/multimodal/overview?hl=es-419)
  para obtener más información sobre las soluciones de IA generativa en Gemini Enterprise Agent Platform.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-19 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-19 (UTC)"],[],[]]
