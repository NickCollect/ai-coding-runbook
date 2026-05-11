---
source_url: https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl
fetched_at: 2026-05-11T05:02:44.115419+00:00
title: "Ograniczenia liczby \u017c\u0105da\u0144 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Ograniczenia liczby żądań

Limity liczby żądań regulują liczbę żądań, które możesz wysyłać do interfejsu Gemini API w określonym czasie. Te limity pomagają zachować uczciwe użytkowanie, chronić przed nadużyciami i utrzymywać wydajność systemu dla wszystkich użytkowników.

[Wyświetlanie aktywnych limitów żądań w AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=pl)

## Jak działają limity szybkości

Limity szybkości są zwykle mierzone w 3 wymiarach:

- Żądania na minutę (**RPM**)
- Tokeny na minutę (dane wejściowe) (**TPM**)
- Żądania dziennie (**RPD**)

Wykorzystanie jest oceniane w odniesieniu do każdego limitu, a przekroczenie któregokolwiek z nich spowoduje błąd limitu szybkości. Jeśli na przykład limit RPM wynosi 20, wysłanie 21 żądań w ciągu minuty spowoduje błąd, nawet jeśli nie przekroczysz limitu TPM ani innych limitów.

Limity liczby żądań są stosowane w przypadku poszczególnych projektów, a nie kluczy interfejsu API. Limity liczby żądań dziennie (**RPD**) są resetowane o północy czasu pacyficznego.

Limity różnią się w zależności od używanego modelu, a niektóre z nich dotyczą tylko określonych modeli. Na przykład liczba obrazów na minutę (IPM) jest obliczana tylko w przypadku modeli, które mogą generować obrazy (Nano Banana), ale jest podobna do liczby tokenów na minutę (TPM). Inne modele mogą mieć limit tokenów na dzień (TPD).

W przypadku modeli eksperymentalnych i wersji zapoznawczych limity liczby żądań są bardziej restrykcyjne.

## Kategorie wykorzystania

Limity liczby żądań są powiązane z poziomem wykorzystania projektu. Wraz ze wzrostem wykorzystania interfejsu API i wydatków automatycznie przejdziesz na wyższy poziom z większymi limitami liczby żądań.

Kryteria kwalifikacji do poziomów 2 i 3 są oparte na łącznych wydatkach na usługi Google Cloud (w tym na Gemini API) na koncie rozliczeniowym połączonym z Twoim projektem.

| Kategoria wykorzystania | Kwalifikacje | [Limit poziomu płatności](https://ai.google.dev/gemini-api/docs/billing?hl=pl#tier-spend-caps) |
| --- | --- | --- |
| **Free** | [Aktywny projekt](https://ai.google.dev/gemini-api/docs/api-key?hl=pl#google-cloud-projects) lub bezpłatny okres próbny | Nie dotyczy |
| **Poziom 1** | [Skonfiguruj i połącz aktywne konto rozliczeniowe](https://ai.google.dev/gemini-api/docs/billing?hl=pl#setup-billing) | 250 USD |
| **Poziom 2** | Zapłacono 100 USD + 3 dni od pierwszej udanej płatności | 2000 USD |
| **Pracownik obsługi klienta poziomu 3** | Zapłacono 1000 USD + 30 dni od pierwszej udanej płatności | 20 000–100 000 USD i więcej |

Spełnienie podanych kryteriów kwalifikacji zwykle wystarcza do zatwierdzenia, ale w rzadkich przypadkach prośba o uaktualnienie może zostać odrzucona z powodu innych czynników wykrytych podczas procesu weryfikacji.

Ten system pomaga zachować bezpieczeństwo i integralność platformy interfejsu Gemini API dla wszystkich użytkowników.

## Limity liczby żądań interfejsu Gemini API

Limity żądań zależą od wielu czynników (np. od poziomu użytkowania) i można je sprawdzić w Google AI Studio. W miarę jak Twój poziom i stan konta będą się zmieniać, limity szybkości będą się automatycznie aktualizować.

[Wyświetlanie aktywnych limitów żądań w AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=pl)

Określone limity szybkości nie są gwarantowane, a rzeczywista przepustowość może się różnić.

## Limity szybkości wnioskowania o priorytetach

Zużycie [priorytetowe](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl) ma własne limity szybkości, mimo że zużycie jest wliczane do ogólnych limitów szybkości ruchu interaktywnego. **Domyślne limity to: 0,3x [standardowego limitu](https://aistudio.google.com/rate-limit?hl=pl) dla każdego modelu i poziomu**

## Limity częstotliwości żądań interfejsu Batch API

Żądania [interfejsu Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl) podlegają własnym limitom liczby żądań, które są niezależne od wywołań interfejsu API niebędących żądaniami zbiorczymi.

- **Równoczesne żądania zbiorcze:** 100
- **Maksymalny rozmiar pliku wejściowego:** 2 GB
- **Limit miejsca na pliki:** 20 GB
- **Tokeny w kolejce według modelu:** tabela **Tokeny w kolejce w przypadku przetwarzania wsadowego** zawiera maksymalną liczbę tokenów, które można umieścić w kolejce do przetwarzania wsadowego we wszystkich aktywnych zadaniach wsadowych dla danego modelu.

### Poziom 1

| Model | Tokeny w kolejce do przetwarzania zbiorczego |
| --- | --- |
| Modele tekstowe | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro (wersja testowa) | 5 000 000 |
| Gemini 3.1 Flash-Lite | 10 000 000 |
| Gemini 3.1 Flash-Lite (wersja testowa) | 10 000 000 |
| Gemini 3 Flash (wersja testowa) | 3 000 000 |
| Gemini 2.5 Pro | 5 000 000 |
| Gemini 2.5 Pro TTS | 25 000 |
| Gemini 2.5 Flash | 3 000 000 |
| Gemini 2.5 Flash (wersja testowa) | 3 000 000 |
| Gemini 2.5 Flash Image (wersja testowa) | 3 000 000 |
| Gemini 2.5 Flash TTS | 100 000 |
| Gemini 2.5 Flash-Lite | 10 000 000 |
| Gemini 2.5 Flash-Lite (wersja testowa) | 10 000 000 |
| Gemini 2.0 Flash | 10 000 000 |
| Gemini 2.0 Flash Image | 3 000 000 |
| Gemini 2.0 Flash-Lite | 10 000 000 |
| Modele generowania multimodalnego | | | | |
| Gemini 3.1 Flash Image (wersja testowa) 🍌 | 1 000 000 |
| Gemini 3 Pro Image (wersja testowa) 🍌 | 2 000 000 |
| Modele wektorów dystrybucyjnych | | | | |
| Osadzanie Gemini | 500 000 |

### Poziom 2

| Model | Tokeny w kolejce do przetwarzania zbiorczego |
| --- | --- |
| Modele tekstowe | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro (wersja testowa) | 500 000 000 |
| Gemini 3.1 Flash-Lite | 500 000 000 |
| Gemini 3.1 Flash-Lite (wersja testowa) | 500 000 000 |
| Gemini 3.1 Flash (wersja testowa) | 400 000 000 |
| Gemini 2.5 Pro | 500 000 000 |
| Gemini 2.5 Pro TTS | 100 000 |
| Gemini 2.5 Flash | 400 000 000 |
| Gemini 2.5 Flash (wersja testowa) | 400 000 000 |
| Gemini 2.5 Flash Image (wersja testowa) | 400 000 000 |
| Gemini 2.5 Flash TTS | 100 000 |
| Gemini 2.5 Flash-Lite | 500 000 000 |
| Gemini 2.5 Flash-Lite (wersja testowa) | 500 000 000 |
| Gemini 2.0 Flash | 1 000 000 000 |
| Gemini 2.0 Flash Image | 400 000 000 |
| Gemini 2.0 Flash-Lite | 1 000 000 000 |
| Modele generowania multimodalnego | | | | |
| Gemini 3.1 Flash Image (wersja testowa) 🍌 | 250 000 000 |
| Gemini 3 Pro Image (wersja testowa) 🍌 | 270 000 000 |
| Modele wektorów dystrybucyjnych | | | | |
| Osadzanie Gemini | 5 000 000 |

### Poziom 3

| Model | Tokeny w kolejce do przetwarzania zbiorczego |
| --- | --- |
| Modele tekstowe | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro (wersja testowa) | 1 000 000 000 |
| Gemini 3.1 Flash-Lite | 1 000 000 000 |
| Gemini 3.1 Flash-Lite (wersja testowa) | 1 000 000 000 |
| Gemini 3.1 Flash (wersja testowa) | 1 000 000 000 |
| Gemini 2.5 Pro | 1 000 000 000 |
| Gemini 2.5 Pro TTS | 1 000 000 |
| Gemini 2.5 Flash | 1 000 000 000 |
| Gemini 2.5 Flash (wersja testowa) | 1 000 000 000 |
| Gemini 2.5 Flash Image (wersja testowa) | 1 000 000 000 |
| Gemini 2.5 Flash TTS | 4 000 000 |
| Gemini 2.5 Flash-Lite | 1 000 000 000 |
| Gemini 2.5 Flash-Lite (wersja testowa) | 1 000 000 000 |
| Gemini 2.0 Flash | 5 000 000 000 |
| Gemini 2.0 Flash Image | 1 000 000 000 |
| Gemini 2.0 Flash-Lite | 5 000 000 000 |
| Modele generowania multimodalnego | | | | |
| Gemini 3.1 Flash Image (wersja testowa) 🍌 | 750 000 000 |
| Gemini 3 Pro Image (wersja testowa) 🍌 | 1 000 000 000 |
| Modele wektorów dystrybucyjnych | | | | |
| Osadzanie Gemini | 10 000 000 |

## Jak przejść na wyższy poziom

Aby przejść z poziomu bezpłatnego na płatny, musisz najpierw [skonfigurować płatności w AI Studio](https://ai.google.dev/gemini-api/docs/billing?hl=pl).

Gdy Twój projekt spełni [określone kryteria](#usage-tiers), zostanie automatycznie uaktualniony do wyższego poziomu. Przejście z abonamentu Free na abonament Tier 1 zwykle następuje natychmiast, a kolejne przejścia na wyższe abonamenty zaczynają obowiązywać w ciągu 10 minut. Otwórz [stronę Projektów](https://aistudio.google.com/projects?hl=pl) w AI Studio, aby sprawdzić swoje poziomy.

## Wysyłanie prośby o zwiększenie limitu częstotliwości

Każda odmiana modelu ma powiązany limit szybkości (żądania na minutę, RPM).
Szczegółowe informacje o tych limitach znajdziesz na stronie [Limity szybkości w AI Studio](https://aistudio.google.com/rate-limit?hl=pl).

[Prośba o zwiększenie limitu częstotliwości w przypadku wersji płatnej](https://forms.gle/ETzX94k8jf7iSotH9)

Nie możemy zagwarantować zwiększenia limitu żądań, ale dołożymy wszelkich starań, aby rozpatrzyć Twoją prośbę.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-07 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-07 UTC."],[],[]]
