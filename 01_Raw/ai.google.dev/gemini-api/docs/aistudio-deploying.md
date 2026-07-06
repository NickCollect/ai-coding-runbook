---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=pl
fetched_at: 2026-07-06T05:07:46.866435+00:00
title: "Wdra\u017canie z Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

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
- **Wdrożenie standardowe:** wymaga projektu w chmurze Google Cloud połączonego z kontem AI Studio i włączonych rozliczeń w tym projekcie.

## Informacje o poziomie Starter

Poziom Starter Google Cloud zapewnia uproszczoną ścieżkę wdrażania aplikacji w Google Cloud bezpośrednio z Google AI Studio bez konfigurowania pełnego środowiska Google Cloud ani konta rozliczeniowego.

Każde wdrożenie w Google AI Studio tworzy odpowiednią usługę w Cloud Run. W przypadku usług wdrożonych w Google AI Studio w ramach pakietu Starter obowiązują te ograniczenia:

- Możesz wdrożyć maksymalnie 2 usługi.
- Usługi są wdrażane w [jednym regionie Cloud Run](https://docs.cloud.google.com/run/docs/locations?hl=pl).

## Kroki wdrażania na poziomie Starter

Po zaprojektowaniu aplikacji w trybie tworzenia wdróż ją w ramach poziomu startowego:

1. W prawym górnym rogu kliknij przycisk **Opublikuj**.
2. Kliknij **Rozpocznij**.
3. Kliknij **Opublikuj aplikację**.

Po zakończeniu wdrażania AI Studio udostępnia adres URL Cloud Run, pod którym możesz uzyskać dostęp do aktywnej aplikacji.

## Wdrożenie standardowe

Wraz z rozwojem aplikacji możesz potrzebować funkcji wykraczających poza poziom Starter, takich jak wyższe limity, większe zasoby obliczeniowe lub inne usługi Google Cloud niedostępne na poziomie Starter. Aby odblokować te funkcje, możesz przekształcić w pełni zarządzany projekt na poziomie Starter w standardowy projekt Google Cloud.

Dzięki temu możesz bezproblemowo skalować usługi bez utraty postępów. Wykonaj te czynności, aby [utworzyć konto rozliczeniowe Cloud](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=pl#create-new-billing-account), formalnie zaakceptować standardowe Warunki korzystania z usług Google Cloud i [przejść na standardowy projekt Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=pl#upgradee). Więcej informacji znajdziesz w artykule [Konfigurowanie kont płatnych](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=pl#paid-setup).

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

Ostatnia aktualizacja: 2026-06-16 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-16 UTC."],[],[]]
