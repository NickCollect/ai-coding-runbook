---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=pl
fetched_at: 2026-08-31T06:34:46.808447+00:00
title: "Wdra\u017canie z Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Wdrażanie z Google AI Studio

Google AI Studio umożliwia wdrażanie aplikacji pełnostosowych bezpośrednio z trybu tworzenia. Umożliwia to szybkie przejście od prototypu do zarządzanego, skalowalnego środowiska produkcyjnego.

## Opcje wdrażania

Wymagania dotyczące wdrażania aplikacji z trybu tworzenia AI Studio zależą od używanego poziomu:

- [**Google Cloud Starter Tier**](https://docs.cloud.google.com/docs/starter-tier?hl=pl):
  Umożliwia opublikowanie maksymalnie 2 aplikacji typu full-stack bez konfigurowania projektu Google Cloud ani konta rozliczeniowego.
- **Wdrożenie standardowe:** wymaga projektu Google Cloud połączonego z kontem AI Studio i włączonych rozliczeń w tym projekcie.

## Informacje o poziomie Starter

Poziom Starter Google Cloud zapewnia uproszczoną ścieżkę wdrażania aplikacji w Google Cloud bezpośrednio z Google AI Studio bez konfigurowania pełnego środowiska Google Cloud ani konta rozliczeniowego.

Każde wdrożenie w Google AI Studio tworzy odpowiednią usługę w Cloud Run. W przypadku usług wdrożonych w Google AI Studio w ramach pakietu Starter obowiązują te ograniczenia:

- Możesz wdrożyć maksymalnie 2 usługi.
- Usługi są wdrażane w [jednym regionie Cloud Run](https://docs.cloud.google.com/run/docs/locations?hl=pl).

## Kroki wdrażania na poziomie startowym

Po zaprojektowaniu aplikacji w trybie tworzenia wdróż ją w ramach pakietu Starter:

1. W prawym górnym rogu kliknij przycisk **Opublikuj**.
2. Kliknij **Rozpocznij**.
3. Kliknij **Opublikuj aplikację**.

Po zakończeniu wdrażania AI Studio udostępnia adres URL Cloud Run, pod którym możesz uzyskać dostęp do działającej aplikacji.

## Niestandardowe adresy URL AI Studio

Podczas publikowania aplikacji z Google AI Studio możesz ustawić niestandardową, łatwą do zapamiętania subdomenę w sekcji `ai.studio` (np. `https://your-app-name.ai.studio`).

Google AI Studio wymaga, aby subdomeny były globalnie unikalne we wszystkich projektach i przydziela je według kolejności zgłoszeń. Jeśli inny projekt używa już danej nazwy, AI Studio poprosi Cię o wybranie innej. Jeśli wycofasz publikację aplikacji lub ją usuniesz, jej niestandardowy URL zostanie zwolniony i będzie dostępny dla innych użytkowników.

### Ustawianie niestandardowego adresu URL

Aby ustawić lub zaktualizować niestandardowy adres URL aplikacji:

1. Otwórz aplikację w Google AI Studio w trybie **Tworzenie**.
2. W prawym górnym rogu kliknij **Opublikuj**.
3. W konfiguracji wdrożenia wpisz preferowaną subdomenę w polu **Niestandardowy URL** lub zaakceptuj sugerowany adres URL.
4. Kliknij **Opublikuj aplikację**.

Aby przenieść istniejący niestandardowy adres URL do innej aplikacji, musisz najpierw cofnąć publikację lub usunąć aplikację, do której jest przypisany ten niestandardowy adres URL, a następnie opublikować nową aplikację, używając wybranej subdomeny.

### Zgłaszanie problemów dotyczących znaków towarowych lub praw autorskich

Niestandardowe subdomeny muszą być zgodne z [Warunkami korzystania z usług Google](https://policies.google.com/terms?hl=pl). Jeśli zauważysz niestandardowy adres URL, który narusza znak towarowy lub używa nazwy chronionej prawem autorskim bez pozwolenia, możesz zgłosić to za pomocą [narzędzia Google do rozwiązywania problemów prawnych](https://support.google.com/legal/troubleshooter/1114905?hl=pl).

## Wdrożenie standardowe

Wraz z rozwojem aplikacji możesz potrzebować funkcji wykraczających poza poziom Starter, takich jak wyższe limity, większe zasoby obliczeniowe lub inne usługi Google Cloud niedostępne na poziomie Starter. Aby odblokować te funkcje, możesz przekształcić w pełni zarządzany projekt na poziomie Starter w standardowy projekt Google Cloud.

Dzięki temu możesz bezproblemowo skalować kampanie bez utraty postępów. Wykonaj czynności, aby [utworzyć konto rozliczeniowe Google Cloud](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=pl#create-new-billing-account), formalnie zaakceptować standardowe Warunki korzystania z usługi Google Cloud i [przejść na standardowy projekt Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=pl#upgradee).
Więcej informacji znajdziesz w artykule [Konfiguracja kont płatnych](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=pl#paid-setup).

Więcej informacji o poziomach płatności znajdziesz w artykule [Rozliczenia i płatności](https://ai.google.dev/gemini-api/docs/billing?hl=pl).

## Usuwanie aplikacji

Jeśli nie potrzebujesz już aplikacji, możesz ją usunąć w Google AI Studio, wykonując te czynności:

1. W Google AI Studio otwórz [stronę Aplikacje](https://aistudio.google.com/app/apps?hl=pl).
2. W menu po lewej stronie kliknij **Aplikacje**.
3. Umieść wskaźnik nad aplikacją, którą chcesz usunąć.
4. Aby usunąć aplikację, kliknij ikonę kosza po prawej stronie wiersza.

## Co dalej?

- Dowiedz się więcej o [poziomie startowym Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=pl).
- Dowiedz się więcej o [płatnościach](https://ai.google.dev/gemini-api/docs/billing?hl=pl) za Gemini API.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-10 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-10 UTC."],[],[]]
