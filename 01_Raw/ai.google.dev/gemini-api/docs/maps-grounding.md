---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id
fetched_at: 2026-11-02T07:08:44.288649+00:00
title: "Grounding dengan Google Maps \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Grounding dengan Google Maps

Grounding with Google Maps menghubungkan kemampuan generatif Gemini dengan data Google Maps yang kaya, faktual, dan terbaru. Fitur ini memungkinkan developer dengan mudah menggabungkan fungsi berbasis lokasi ke dalam aplikasi mereka. Saat kueri pengguna memiliki konteks yang terkait dengan data Maps, model Gemini akan memanfaatkan Google Maps untuk memberikan jawaban yang faktual, akurat, dan terbaru yang relevan dengan lokasi atau area umum yang ditentukan pengguna.

- **Respons yang akurat dan berbasis lokasi:** Manfaatkan data Google Maps yang ekstensif dan terbaru untuk kueri yang spesifik secara geografis.
- **Personalisasi yang ditingkatkan:** Sesuaikan rekomendasi dan informasi berdasarkan lokasi yang diberikan pengguna.

## Mulai

Contoh ini menunjukkan cara mengintegrasikan Grounding with Google Maps ke dalam aplikasi Anda untuk memberikan respons yang akurat dan berbasis lokasi terhadap kueri pengguna. Perintah meminta rekomendasi lokal dengan lokasi pengguna opsional, sehingga model Gemini dapat menggunakan data Google Maps.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "What are the best Italian restaurants within a 15-minute walk from here?"))
        .tools(
            Arrays.asList(
                GoogleMaps.builder().latitude(34.050481).longitude(-118.248526).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// Print the model's text response and annotations
if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("What are the best Italian restaurants within a 15-minute walk from here?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(34.050481),
                        Longitude: genai.Ptr(-118.248526),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Print the model's text response and annotations
    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    fmt.Println(content.TextContent.Text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.PlaceCitation != nil {
                                c := annotation.PlaceCitation
                                name := ""
                                if c.Name != nil {
                                    name = *c.Name
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  - %s: %s\n", name, url)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Cara kerja Grounding with Google Maps

Grounding with Google Maps mengintegrasikan Gemini API dengan ekosistem Google Geo menggunakan Maps API sebagai sumber grounding. Saat kueri pengguna berisi konteks geografis, model Gemini dapat memanggil alat Grounding with Google Maps. Model ini kemudian dapat menghasilkan respons yang didasarkan pada data Google Maps yang relevan dengan lokasi yang diberikan.

Proses ini biasanya melibatkan:

1. **Kueri pengguna:** Pengguna mengirimkan kueri ke aplikasi Anda, yang mungkin menyertakan konteks geografis (misalnya, "kafe di dekat saya", "museum di San Francisco").
2. **Pemanggilan alat:** Model Gemini, yang mengenali maksud geografis, memanggil alat Grounding with Google Maps. Alat ini dapat secara opsional diberikan `latitude` dan `longitude` pengguna. Alat ini adalah alat penelusuran teks dan berperilaku mirip dengan penelusuran di Maps, yang mana kueri lokal ("di dekat saya") akan menggunakan koordinat, sedangkan kueri spesifik atau non-lokal kemungkinan tidak akan terpengaruh oleh lokasi eksplisit.
3. **Pengambilan data:** Layanan Grounding with Google Maps mengkueri Google Maps untuk mendapatkan informasi yang relevan (misalnya, tempat, ulasan, foto, alamat, jam buka).
4. **Generasi yang didasarkan pada data:** Data Maps yang diambil digunakan untuk menginformasikan respons model Gemini, sehingga memastikan akurasi dan relevansi faktual.
5. **Respons &anotasi:** Model menampilkan respons teks dengan anotasi inline yang ditautkan ke sumber Google Maps, sehingga developer dapat menampilkan kutipan.

## Mengapa dan kapan Grounding with Google Maps sebaiknya digunakan

Grounding with Google Maps sangat ideal untuk aplikasi yang memerlukan informasi yang akurat, terbaru, dan spesifik lokasi. Fitur ini meningkatkan pengalaman pengguna dengan menyediakan konten yang relevan dan dipersonalisasi yang didukung oleh database Google Maps yang ekstensif dengan lebih dari 250 juta tempat di seluruh dunia.

Anda harus menggunakan Grounding with Google Maps jika aplikasi Anda perlu:

- Memberikan respons yang lengkap dan akurat terhadap pertanyaan yang spesifik secara geografis.
- Membuat perencana perjalanan percakapan dan panduan lokal.
- Merekomendasikan tempat menarik berdasarkan lokasi dan preferensi pengguna seperti restoran atau toko.
- Membuat pengalaman berbasis lokasi untuk layanan sosial, retail, atau pengiriman makanan.

Grounding with Google Maps unggul dalam kasus penggunaan yang mengutamakan kedekatan dan data faktual saat ini, seperti menemukan "kafe terbaik di dekat saya" atau mendapatkan rute.

## Kasus penggunaan

Grounding with Google Maps mendukung berbagai kasus penggunaan berbasis lokasi.

### Menangani pertanyaan spesifik tempat

Ajukan pertanyaan mendetail tentang tempat tertentu untuk mendapatkan jawaban berdasarkan ulasan pengguna Google dan data Maps lainnya.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Is there a cafe near the corner of 1st and Main that has outdoor seating?"))
        .tools(
            Arrays.asList(
                GoogleMaps.builder().latitude(34.050481).longitude(-118.248526).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Is there a cafe near the corner of 1st and Main that has outdoor seating?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(34.050481),
                        Longitude: genai.Ptr(-118.248526),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    fmt.Println(content.TextContent.Text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.PlaceCitation != nil {
                                c := annotation.PlaceCitation
                                name := ""
                                if c.Name != nil {
                                    name = *c.Name
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  - %s: %s\n", name, url)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### Menyediakan personalisasi berbasis lokasi

Dapatkan rekomendasi yang disesuaikan dengan preferensi pengguna dan area geografis tertentu.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Which family-friendly restaurants near here have the best playground reviews?"))
        .tools(
            Arrays.asList(GoogleMaps.builder().latitude(30.2672).longitude(-97.7431).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Which family-friendly restaurants near here have the best playground reviews?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(30.2672),
                        Longitude: genai.Ptr(-97.7431),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    fmt.Println(content.TextContent.Text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.PlaceCitation != nil {
                                c := annotation.PlaceCitation
                                name := ""
                                if c.Name != nil {
                                    name = *c.Name
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  - %s: %s\n", name, url)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### Membantu perencanaan itinerari

Buat rencana beberapa hari dengan rute dan informasi tentang berbagai lokasi, yang cocok untuk aplikasi perjalanan.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

String prompt =
    "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .tools(
            Arrays.asList(GoogleMaps.builder().latitude(37.78193).longitude(-122.40476).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// ... code to process response
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput(prompt),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(37.78193),
                        Longitude: genai.Ptr(-122.40476),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    // ... code to process response
    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## Persyaratan penggunaan layanan

Bagian ini menjelaskan persyaratan penggunaan layanan untuk Grounding with Google Maps.

### Memberi tahu pengguna tentang penggunaan sumber Google Maps

Dengan setiap hasil Grounding Google Maps, Anda akan menerima anotasi sumber di blok konten langkah `model_output` yang mendukung setiap respons. Metadata berikut akan ditampilkan:

- URL sumber
- nama

Saat menyajikan hasil dari Grounding with Google Maps, Anda harus menentukan sumber Google Maps terkait, dan memberi tahu pengguna Anda tentang hal berikut:

- Sumber Google Maps harus segera mengikuti konten yang dihasilkan yang didukung oleh sumber tersebut. Konten yang dihasilkan ini juga disebut Hasil Grounding Google Maps.
- Sumber Google Maps harus dapat dilihat dalam satu interaksi pengguna.

### Menampilkan sumber Google Maps dengan link Google Maps

Untuk setiap anotasi sumber, pratinjau link harus dibuat dengan mengikuti persyaratan berikut:

- Atribusikan setiap sumber ke Google Maps dengan mengikuti panduan atribusi teks Google Maps
  [Google Maps](#maps-attribution-guidelines).
- Tampilkan nama sumber yang diberikan dalam respons.
- Tautkan ke sumber menggunakan `url` dari anotasi.

### Panduan atribusi teks Google Maps

Saat Anda mengatribusikan sumber ke Google Maps dalam teks, ikuti panduan berikut:

- Jangan ubah teks Google Maps dengan cara apa pun:
  - Jangan ubah kapitalisasi Google Maps.
  - Jangan gabungkan Google Maps ke beberapa baris.
  - Jangan lokalkan Google Maps ke bahasa lain.
  - Cegah browser menerjemahkan Google Maps dengan menggunakan atribut HTML translate="no".

Untuk mengetahui informasi selengkapnya tentang beberapa penyedia data Google Maps dan persyaratan lisensinya, lihat [pemberitahuan hukum Google Maps dan Google Earth](https://www.google.com/help/legalnotices_maps/?hl=id).

## Praktik terbaik

- **Berikan lokasi pengguna:** Untuk mendapatkan respons yang paling relevan dan dipersonalisasi, selalu sertakan `latitude` dan `longitude` dalam konfigurasi alat `google_maps` Anda saat lokasi pengguna diketahui.
- **Beri Tahu Pengguna Akhir:** Beri tahu pengguna akhir Anda dengan jelas bahwa data Google Maps digunakan untuk menjawab kueri mereka, terutama saat alat diaktifkan.
- **Nonaktifkan Jika Tidak Diperlukan:** Grounding with Google Maps dinonaktifkan secara default. Hanya aktifkan (`"tools": [{"type": "google_maps"}]`) saat kueri memiliki
  konteks geografis yang jelas, untuk mengoptimalkan performa dan biaya.

## Batasan

- Grounding with Google Maps saat ini hanya mendukung perintah dan respons dalam bahasa Inggris.
- Alat ini mungkin tidak tersedia di semua wilayah.
- Hasil dapat bervariasi berdasarkan akurasi lokasi dan data Maps yang tersedia.
- **Cakupan Geografis:** Grounding with Google Maps tersedia secara global.
- **Status Default:** Alat Grounding with Google Maps dinonaktifkan secara default.
  Anda harus mengaktifkannya secara eksplisit dalam permintaan API.

## Harga dan batas kapasitas

Harga Grounding with Google Maps berbeda-beda bergantung pada generasi model:

- **Model Gemini 3 dan yang lebih baru:** Project Anda akan ditagih untuk setiap kueri penelusuran yang diputuskan untuk dijalankan oleh model, dengan 5.000 permintaan gratis per bulan yang dibagikan di semua model Gemini 3 dan yang lebih baru, lalu **$14 per 1.000 kueri penelusuran**. Satu perintah penelusuran (permintaan API Anda ke model) dapat menyebabkan model menjalankan beberapa kueri penelusuran untuk menemukan informasi yang diperlukan. Setiap kueri ini dihitung sebagai penggunaan alat yang dapat ditagih.
- **Model Gemini 2.5 dan yang lebih lama:** Project Anda akan ditagih per perintah penelusuran ($25 per 1.000 perintah yang didasarkan pada data). Permintaan hanya akan ditagih jika perintah berhasil menampilkan setidaknya satu hasil yang didasarkan pada data Google Maps, terlepas dari berapa banyak kueri penelusuran individual yang dilakukan model secara internal untuk mendapatkan hasil tersebut.

Kuota untuk Grounding with Google Maps biasanya selaras dengan batas kapasitas model Gemini yang mendasarinya. Untuk mengetahui informasi harga mendetail, lihat halaman harga [Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=id).

## Model yang didukung

Model berikut mendukung Grounding with Google Maps:

| Model | Grounding with Google Maps |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=id) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=id) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=id) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=id) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=id) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=id) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=id) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=id) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=id) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=id) | ✔️ |

## Kombinasi alat yang didukung

Anda dapat menggunakan Grounding with Google Maps dengan alat bawaan lainnya seperti
[Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=id) (didukung di
model Gemini 3.5 Flash-Lite dan yang lebih baru) untuk mendukung kasus penggunaan yang lebih kompleks.
Model Gemini 3 juga mendukung penggabungan alat bawaan ini dengan alat kustom (panggilan fungsi). Pelajari lebih lanjut di halaman
[kombinasi alat](https://ai.google.dev/gemini-api/docs/tool-combination?hl=id).

## Langkah berikutnya

- Pelajari alat lain yang [tersedia](https://ai.google.dev/gemini-api/docs/tools?hl=id).
- Untuk mempelajari praktik terbaik AI yang bertanggung jawab dan filter keamanan Gemini API lebih lanjut, lihat [panduan Setelan keamanan](https://ai.google.dev/gemini-api/docs/safety-settings?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-10-13 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-10-13 UTC."],[],[]]
