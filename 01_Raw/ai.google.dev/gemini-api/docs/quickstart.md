---
source_url: https://ai.google.dev/gemini-api/docs/quickstart?hl=es-419
fetched_at: 2026-05-05T19:45:17.186720+00:00
title: "Gu\u00eda de inicio r\u00e1pido de la API de Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Guía de inicio rápido de la API de Gemini

En esta guía de inicio rápido, se muestra cómo instalar nuestras [bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419) y realizar tu primera solicitud a la API de Gemini.

## Antes de comenzar

Para usar la API de Gemini, necesitas una clave de API. Puedes crear una de forma gratuita para comenzar.

[Crea una clave de la API de Gemini](https://aistudio.google.com/app/apikey?hl=es-419)

## Instala el SDK de IA generativa de Google

### Python

Con [Python 3.9 o versiones posteriores](https://www.python.org/downloads/), instala el [paquete `google-genai`](https://pypi.org/project/google-genai/) con el siguiente [comando pip](https://packaging.python.org/en/latest/tutorials/installing-packages/):

```
pip install -q -U google-genai
```

### JavaScript

Con [Node.js v18 o versiones posteriores](https://nodejs.org/en/download/package-manager), instala el [SDK de IA generativa de Google para TypeScript y JavaScript](https://www.npmjs.com/package/@google/genai) con el siguiente [comando npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm):

```
npm install @google/genai
```

### Go

Instala [google.golang.org/genai](https://pkg.go.dev/google.golang.org/genai) en el directorio de tu módulo con el [comando go get](https://go.dev/doc/code):

```
go get google.golang.org/genai
```

### Java

Si usas Maven, puedes instalar [google-genai](https://github.com/googleapis/java-genai) agregando lo siguiente a tus dependencias:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

Instala [googleapis/go-genai](https://googleapis.github.io/dotnet-genai/) en el directorio de tu módulo con el [comando dotnet add](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-add).

```
dotnet add package Google.GenAI
```

### Apps Script

1. Para crear un nuevo proyecto de Apps Script, ve a [script.new](https://script.google.com/u/0/home/projects/create?hl=es-419).
2. Haz clic en **Proyecto sin título**.
3. Cámbiale el nombre al proyecto de Apps Script **AI Studio** y haz clic en **Cambiar nombre**.
4. Establece tu [clave de API](https://developers.google.com/apps-script/guides/properties?hl=es-419#manage_script_properties_manually).
   1. A la izquierda, haz clic en **Configuración del proyecto** ![El ícono de configuración del proyecto](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/settings/default/24px.svg).
   2. En **Propiedades de secuencia de comandos**, haz clic en **Agregar propiedad de secuencia de comandos**.
   3. En **Propiedad**, ingresa el nombre de la clave: `GEMINI_API_KEY`.
   4. En **Valor**, ingresa el valor de la clave de API.
   5. Haz clic en **Guardar las propiedades de la secuencia de comandos**.
5. Reemplaza el contenido del archivo `Code.gs` por el siguiente código:

## Realiza tu primera solicitud

Este es un ejemplo que usa el método [`generateContent`](https://ai.google.dev/api/generate-content?hl=es-419#method:-models.generatecontent) para enviar una solicitud a la API de Gemini con el modelo Gemini 2.5 Flash.

Si [configuras tu clave de API](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419#set-api-env-var) como la variable de entorno `GEMINI_API_KEY`, el cliente la detectará automáticamente cuando uses las [bibliotecas de la API de Gemini](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419).
De lo contrario, deberás [pasar tu clave de API](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419#provide-api-key-explicitly) como un argumento cuando inicialices el cliente.

Ten en cuenta que todas las muestras de código en la documentación de la API de Gemini suponen que estableciste la variable de entorno `GEMINI_API_KEY`.

### Python

```
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The client gets the API key from the environment variable `GEMINI_API_KEY`.
const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    // The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    // The client gets the API key from the environment variable `GEMINI_API_KEY`.
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    // The client gets the API key from the environment variable `GOOGLE_API_KEY`.
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3-flash-preview", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');
function main() {
  const payload = {
    contents: [
      {
        parts: [
          { text: 'Explain how AI works in a few words' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## ¿Qué sigue?

Ahora que realizaste tu primera solicitud a la API, te recomendamos que explores las siguientes guías que muestran Gemini en acción:

- [Generación de texto](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419)
- [Generación de imágenes](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419)
- [Comprensión de imágenes](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419)
- [Pensamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419)
- [Llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419)
- [Contexto largo](https://ai.google.dev/gemini-api/docs/long-context?hl=es-419)
- [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=es-419)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-04-29 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-04-29 (UTC)"],[],[]]
