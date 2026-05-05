---
source_url: https://ai.google.dev/gemini-api/docs/nanobanana?hl=es-419
fetched_at: 2026-05-05T19:47:10.621483+00:00
title: "Nano Banana (generaci\u00f3n de im\u00e1genes) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)

Enviar comentarios

# Nano Banana (generación de imágenes)

**Nano Banana** es el nombre de las capacidades nativas de generación de imágenes de Gemini. Actualmente, se refiere a dos modelos distintos disponibles en la API de Gemini:

- **Nano Banana**: El modelo [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#gemini-2.5-flash-image) (`gemini-2.5-flash-image`). Este modelo está diseñado para ofrecer velocidad y eficiencia, y se optimizó para tareas de alto volumen y baja latencia.
- **Nano Banana Pro**: El modelo [Gemini 3 Pro Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#gemini-3-pro-image-preview) (`gemini-3-pro-image-preview`). Este modelo está diseñado para la producción de recursos profesionales, ya que utiliza un razonamiento avanzado ("Pensar") para seguir instrucciones complejas y renderizar texto de alta fidelidad.

## Comenzar

Puedes generar imágenes con el método `generate_content` usando el nombre del modelo que corresponde a la versión que deseas usar.

### Python

```
from google import genai
from PIL import Image

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents="Create a picture of a futuristic banana with neon lights in a cyberpunk city.",
)

for part in response.parts:
    if part.inline_data:
        image = part.as_image()
        image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-2.5-flash-image",
  contents: "Create a picture of a futuristic banana with neon lights in a cyberpunk city.",
});

for (const part of response.candidates[0].content.parts) {
  if (part.inlineData) {
    const buffer = Buffer.from(part.inlineData.data, "base64");
    fs.writeFileSync("banana.png", buffer);
  }
}
```

### Go

```
package main

import (
    "context"
    "os"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        // handle error
    }

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-2.5-flash-image",
        genai.Text("Create a picture of a futuristic banana with neon lights in a cyberpunk city."),
    )

    for _, part := range resp.Candidates[0].Content.Parts {
        if part.InlineData != nil {
            _ = os.WriteFile("banana.png", part.InlineData.Data, 0644)
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;

public class ImageGen {
  public static void main(String[] args) throws Exception {
    try (Client client = new Client()) {
      GenerateContentResponse response = client.models.generateContent(
          "gemini-2.5-flash-image",
          "Create a picture of a futuristic banana with neon lights in a cyberpunk city.",
          null);

      for (Part part : response.parts()) {
        if (part.inlineData().isPresent()) {
           Files.write(Paths.get("banana.png"), part.inlineData().get().data().get());
        }
      }
    }
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Create a picture of a futuristic banana with neon lights in a cyberpunk city."}
      ]
    }]
  }'
```

## Más información

Para obtener documentación completa sobre la generación de imágenes, la edición, las instrucciones avanzadas y las comparaciones de modelos, consulta la guía completa:

- [**Generación de imágenes con Gemini**](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419): La guía completa para usar los modelos Nano Banana y Nano Banana Pro
- [**Información del modelo**](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419): Detalles sobre las versiones, las capacidades y los precios del modelo

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-01-22 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-01-22 (UTC)"],[],[]]
