---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=pl
fetched_at: 2026-07-06T05:11:44.306523+00:00
title: "Korzystanie z kluczy interfejsu Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Korzystanie z kluczy interfejsu Gemini API

Aby korzystać z Gemini API, musisz uwierzytelnić swoje żądania. Możesz uwierzytelnić się za pomocą standardowego klucza interfejsu API lub klucza autoryzacji.

[Tworzenie lub wyświetlanie klucza interfejsu Gemini API](https://aistudio.google.com/apikey?hl=pl)

## Typy kluczy interfejsu API: standardowy i autoryzacji

Klucze interfejsu API zapewniają dostęp do Gemini API, ale różnią się pod względem bezpieczeństwa. Aby zwiększyć bezpieczeństwo, Gemini API przechodzi ze standardowych kluczy interfejsu API na klucze autoryzacji:

- **Standardowe klucze interfejsu API**: powiązują żądania z projektem w chmurze Google Cloud na potrzeby
  rozliczeń i limitów. Klucze standardowe nie identyfikują dzwoniącego, co ogranicza szczegółowość uprawnień i kontroli dostępu, które mogą obsługiwać.
- **Klucze autoryzacji**: są powiązane bezpośrednio z kontem usługi Google Cloud. Gdy używasz klucza autoryzacji, Twoje żądania są przetwarzane w ramach tożsamości powiązanego konta usługi, co umożliwia szczegółową kontrolę dostępu. Klucze autoryzacji są domyślnie ograniczone do Generative Language API (Gemini API) i zapewniają szybkie egzekwowanie wycieku klucza, które szybko zatrzymuje użycie wyciekłych kluczy wykrytych przez nasze systemy.

Aby zapewnić bezpieczne korzystanie, Gemini API przejdzie ze standardowych kluczy na klucze autoryzacji:

- **Domyślne klucze autoryzacji**: wszystkie nowe klucze interfejsu API utworzone w Google AI Studio
  są automatycznie tworzone jako klucze autoryzacji.
- **19 czerwca 2026 r.**: Gemini API będzie odrzucać żądania
  z **nieograniczonych kluczy standardowych**. Standardowe klucze interfejsu API, do których zastosowano wyraźne ograniczenia, będą nadal działać. To ograniczenie uniemożliwia nieautoryzowane użycie kluczy, które mogą być udostępniane publicznie lub powiązane z innymi usługami.
- **We wrześniu 2026 r.:** Gemini API będzie odrzucać żądania z **kluczy
  standardowych**. Aby uniknąć przerw w działaniu usługi, musisz [przeprowadzić migrację na klucze autoryzacji](#migrate-to-auth-key)
  przed tą datą. Pamiętaj, aby przeprowadzić migrację na klucze autoryzacji przed wrześniem 2026 r.

## Zarządzanie kluczami interfejsu API w Google AI Studio

Projektami i kluczami możesz zarządzać bezpośrednio w [Google AI Studio](https://aistudio.google.com/apikey?hl=pl).

### Projekty Google Cloud

Każdy klucz interfejsu Gemini API jest powiązany z projektem [Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=pl).
Projekty Google Cloud zarządzają rozliczeniami, współpracownikami i uprawnieniami. Google AI Studio udostępnia uproszczony interfejs umożliwiający dostęp do tych projektów.

- **Domyślny projekt**: jeśli jesteś nowym użytkownikiem, po zaakceptowaniu Warunków korzystania z usługi Google AI Studio automatycznie utworzy domyślny projekt w chmurze Google Cloud i klucz interfejsu API. Możesz zmienić nazwę tego projektu, otwierając widok **Projekty** na panelu.
- **Istniejące projekty**: jeśli masz już konto Google Cloud, AI
  Studio nie utworzy domyślnego projektu. Zamiast tego musisz zaimportować istniejące projekty.

### Importowanie projektów

Domyślnie Google AI Studio nie wyświetla wszystkich projektów Google Cloud. Musisz zaimportować projekty, których chcesz używać:

1. Otwórz [Google AI Studio](https://aistudio.google.com?hl=pl).
2. W panelu po lewej stronie otwórz **Panel** i wybierz **Projekty**.
3. Kliknij przycisk **Importuj projekty**.
4. Wyszukaj i wybierz projekt Google Cloud, który chcesz zaimportować, a potem kliknij **Importuj**.
5. Po zaimportowaniu otwórz stronę **Klucze interfejsu API** na panelu, aby utworzyć klucz w tym projekcie.

### Rozwiązywanie problemów z uprawnieniami do tworzenia kluczy

Jeśli przycisk **Utwórz klucz interfejsu API** jest niedostępny i wyświetla się komunikat
*„Nie masz uprawnień do tworzenia klucza w tym projekcie”*, oznacza to, że nie masz
wymaganych uprawnień IAM.

Poproś administratora projektu w chmurze lub administratora organizacji Google Cloud o przypisanie Ci roli zawierającej te uprawnienia (np. Edytujący projekt):

- `resourcemanager.projects.get`: umożliwia AI Studio weryfikację projektu.
- `apikeys.keys.create`: umożliwia generowanie kluczy.
- `serviceusage.services.enable`: zapewnia włączenie Generative Language API.
- `iam.serviceAccounts.create`: wymagane do utworzenia połączonego konta usługi.
- `iam.serviceAccountApiKeyBindings.create`: wiąże konto usługi z kluczem interfejsu API.

Jeśli nie możesz uzyskać dostępu administracyjnego, możesz utworzyć nowy projekt Google Cloud, który nie jest powiązany z organizacją, aby wygenerować klucze.

## Konfigurowanie środowiska

Gdy masz już klucz, skonfiguruj środowisko, aby bezpiecznie używać go w aplikacjach.

### Opcja 1. Użyj zmiennych środowiskowych (zalecane)

Ustaw zmienną środowiskową `GEMINI_API_KEY` lub `GOOGLE_API_KEY`. Biblioteki klienta Gemini API automatycznie wykrywają i używają tych zmiennych. Jeśli obie są ustawione, pierwszeństwo ma `GOOGLE_API_KEY`.

Aby ustawić zmienną, wybierz system operacyjny:

### Linux/macOS – Bash

Sprawdź, czy masz plik konfiguracyjny bash:

```
~/.bashrc
```

Jeśli nie, utwórz go i otwórz:

```
touch ~/.bashrc && open ~/.bashrc
```

Na końcu pliku dodaj polecenie eksportu:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Zapisz plik, a potem zastosuj zmiany:

```
source ~/.bashrc
```

### macOS – Zsh

Sprawdź, czy masz plik konfiguracyjny zsh:

```
~/.zshrc
```

Jeśli nie, utwórz go i otwórz:

```
touch ~/.zshrc && open ~/.zshrc
```

Dodaj polecenie eksportu:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Zapisz plik, a potem zastosuj zmiany:

```
source ~/.zshrc
```

### Windows

1. Na pasku wyszukiwania systemu Windows wyszukaj „Zmienne środowiskowe”.
2. W oknie Właściwości systemu kliknij **Zmienne środowiskowe**.
3. W sekcji **Zmienne użytkownika** lub **Zmienne systemowe** kliknij **Nowa…**.
4. Ustaw nazwę zmiennej na `GEMINI_API_KEY`, a wartość na klucz interfejsu API.
5. Aby zapisać zmiany, kliknij **OK**. Aby wczytać zmienną, otwórz nową sesję terminala.

### Opcja 2. Podaj klucz interfejsu API bezpośrednio w kodzie

Klucz interfejsu API możesz przekazać bezpośrednio podczas inicjowania klienta. Zrób to tylko wtedy, gdy nie możesz używać zmiennych środowiskowych.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.output_text);
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
    "google.golang.org/genai/interactions"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  "YOUR_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction, err := client.Interactions.NewModel(ctx, interactions.NewModelParams{
        Model: "gemini-3.5-flash",
        Input: interactions.Input{
            String: "Explain how AI works in a few words",
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range interaction.Steps {
        if step.ModelOutput != nil {
            for _, content := range step.ModelOutput.Content {
                if content.Text != nil {
                    fmt.Println(content.Text.Text)
                }
            }
        }
    }
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.interactions.models.interactions.CreateModelInteractionParams;
import com.google.genai.interactions.models.interactions.Interaction;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    CreateModelInteractionParams params =
        CreateModelInteractionParams.builder()
            .input("Explain how AI works in a few words")
            .model("gemini-3.5-flash")
            .build();

    Interaction interaction = client.interactions.create(params);

    interaction.steps().forEach(step -> {
      if (step.isModelOutput()) {
        step.asModelOutput().content().ifPresent(contents -> {
          contents.forEach(content -> {
            content.text().ifPresent(text -> System.out.println(text.text()));
          });
        });
      }
    });
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## Bezpieczeństwo i zarządzanie obiektami tajnymi

Traktuj klucz interfejsu Gemini API jak hasło. Jeśli zostanie on naruszony, inne osoby mogą wykorzystać limit projektu, ponieść nieoczekiwane opłaty i uzyskać dostęp do zasobów prywatnych.

### Krytyczne reguły bezpieczeństwa

- **Zachowaj klucze w tajemnicy**: nigdy nie sprawdzaj kluczy interfejsu API w systemach kontroli źródła
  takich jak Git.
- **Nigdy nie udostępniaj kluczy po stronie klienta w środowisku produkcyjnym**: nie koduj na stałe kluczy interfejsu API
  bezpośrednio w aplikacjach internetowych ani mobilnych. Klucze skompilowane w kodzie po stronie klienta mogą zostać wyodrębnione przez użytkowników. Aby zabezpieczyć aplikacje po stronie klienta, uruchom serwer proxy backendu, który będzie wykonywać rzeczywiste wywołania interfejsu API.

### Sprawdzone metody zarządzania obiektami tajnymi

- **Zmienne środowiskowe**: odczytuj klucze ze zmiennych środowiskowych, a nie z plików konfiguracyjnych.
- **Secret Manager**: w środowisku produkcyjnym przechowuj klucze w bezpiecznym magazynie obiektów tajnych
  takim jak [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=pl).
- **Alerty rozliczeniowe**: skonfiguruj w konsoli Google Cloud alerty rozliczeniowe, które będą Cię informować o nagłym wzroście wykorzystania lub kosztów.

### Lista kontrolna dotycząca reagowania na wyciek danych

Jeśli podejrzewasz, że Twój klucz interfejsu API wyciekł:

1. **Wygeneruj nowy klucz**: utwórz klucz zastępczy w Google AI Studio lub
   Cloud Console.
2. **Zaktualizuj aplikację**: wdróż kod z użyciem nowego klucza.
3. **Wyłącz lub usuń naruszony klucz**: gdy nowy klucz zostanie zweryfikowany, wyłącz wyciekły klucz w
   Cloud Console. Aby uniknąć przestoju aplikacji, nie usuwaj starego klucza, dopóki nowy klucz nie będzie w pełni aktywny.
4. **Sprawdź wykorzystanie**: sprawdź logi rozliczeń i wykorzystanie interfejsu API w Google Cloud
   Console, aby zidentyfikować nieautoryzowaną aktywność.

## Ograniczanie i zabezpieczanie kluczy

Dodanie ograniczeń do kluczy interfejsu API minimalizuje potencjalne szkody w przypadku naruszenia bezpieczeństwa klucza.

### Stosowanie ograniczeń dotyczących pochodzenia żądania

Ograniczenia dotyczące pochodzenia ograniczają, które adresy IP, witryny lub aplikacje mogą używać Twojego klucza.

1. Otwórz stronę [Dane logowania w konsoli Google Cloud](https://console.cloud.google.com/apis/credentials?hl=pl).
2. Wybierz projekt i kliknij nazwę klucza interfejsu API, który chcesz ograniczyć.
3. W sekcji **Ograniczenia aplikacji** wybierz **Adresy IP** (lub
   odpowiedni typ ograniczenia dla Twojego środowiska).
4. Określ dozwolone adresy IP lub zakresy adresów, a potem kliknij **Zapisz**.

### Zabezpieczanie nieograniczonych standardowych kluczy interfejsu API

Aby nadal korzystać z Gemini API po 19 czerwca 2026 r., musisz zabezpieczyć wszystkie nieograniczone klucze.

#### Metoda A. Ogranicz klucz tylko do Gemini API (AI Studio)

Jeśli używasz klucza tylko do Gemini API, zabezpiecz go bezpośrednio w AI Studio:

1. Na stronie **Klucze interfejsu API** w [Google AI Studio](https://aistudio.google.com/api-keys?hl=pl) znajdź klucze oznaczone etykietą
   **Nieograniczone**.
2. Najedź kursorem na etykietę i w oknie kliknij **Dodaj ograniczenia**.
3. Wybierz **Ogranicz tylko do Gemini API**.
4. Aby potwierdzić, kliknij **Ogranicz klucz**.

#### Metoda B. Ogranicz klucz do innych usług (konsola Google Cloud)

Jeśli klucz jest udostępniany innym interfejsom API Google (niezalecane), ogranicz go w Cloud Console. **Uwaga: po zastosowaniu tych ograniczeń żądania Gemini API używające tego klucza będą kończyć się niepowodzeniem.**

1. Otwórz stronę [Dane logowania w konsoli Google Cloud](https://console.cloud.google.com/apis/credentials?hl=pl).
2. Wybierz projekt i klucz interfejsu API.
3. W sekcji **Ograniczenia interfejsów API** użyj menu **Wybierz ograniczenia interfejsu API** , aby
   wybrać interfejsy API, do których ten klucz ma mieć dostęp. Nie wybieraj **Generative Language API**.
4. Kliknij **Zapisz**. Aby nadal korzystać z Gemini API, utwórz w AI Studio osobny klucz z ograniczeniami.

### Zablokowane nieaktywne klucze

Od 7 maja 2026 r. Gemini API będzie blokować nieograniczone klucze interfejsu API, które przez dłuższy czas były nieaktywne. Te klucze są oznaczone w AI Studio tagiem **Zablokowane**. Aby kontynuować, musisz wygenerować nowy klucz lub użyć istniejącego klucza z ograniczeniami.

## Migracja na klucz autoryzacji

Aby utworzyć nowy klucz autoryzacji i zaktualizować aplikacje, wykonaj te czynności:

1. Otwórz stronę [Klucze interfejsu API w AI Studio](https://aistudio.google.com/api-keys?hl=pl).
2. Sprawdź kolumnę **Typ klucza** , aby zidentyfikować klucze oznaczone jako **Standardowy**.
3. Aby wygenerować nowy klucz, kliknij **Utwórz klucz interfejsu API**. Wszystkie nowe klucze utworzone w AI Studio są automatycznie tworzone jako klucze autoryzacji.
4. Skopiuj nowy klucz autoryzacji.
5. Zaktualizuj kod aplikacji, zmienne środowiskowe i konfiguracje wdrożenia, aby używać nowego klucza autoryzacji.
6. Przetestuj aplikację, aby sprawdzić, czy działa prawidłowo z nowym kluczem.
7. Gdy sprawdzisz, czy wszystko działa, usuń lub unieważnij stary klucz ruchu, aby zapobiec jego nadużyciu.

## Ograniczenia

Google AI Studio nakłada te ograniczenia dotyczące zarządzania projektami i kluczami:

- Na stronie **Projekty** w Google AI Studio możesz utworzyć maksymalnie 10 projektów naraz.
- Na stronach **Klucze interfejsu API** i **Projekty** wyświetla się maksymalnie 100 kluczy i 50 projektów.
- Wyświetlane są tylko klucze interfejsu API, które nie mają ograniczeń lub są ograniczone tylko do Generative Language API (Gemini API).

Aby korzystać z zaawansowanego zarządzania projektami lub modyfikować klucze z innymi ograniczeniami, użyj strony [Dane logowania w konsoli Google Cloud](https://console.cloud.google.com/apis/credentials?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-24 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-24 UTC."],[],[]]
