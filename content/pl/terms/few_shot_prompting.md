---
title: "Promptowanie few-shot"
term_id: "few_shot_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["prompting", "llm", "technique"]
difficulty: 2
weight: 1
slug: "few_shot_prompting"
aliases:
  - /pl/terms/few_shot_prompting/
date: "2026-07-18T15:35:16.858838Z"
lastmod: "2026-07-18T17:15:08.832386Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "Promptowanie few-shot to technika, w której duże modele językowe (LLM) otrzymują w prompcie niewielką liczbę przykładów wejścia i wyjścia, aby kierować ich zachowaniem."
---

## Definition

Ta metoda wykorzystuje zdolności uczenia się w kontekście (in-context learning) dużych modeli językowych poprzez dostarczenie kilku ilustracyjnych przykładów bezpośrednio w prompcie. W przeciwieństwie do dostrajania (fine-tuning), które wymaga aktualizacji wag modelu...

### Summary

Promptowanie few-shot to technika, w której duże modele językowe (LLM) otrzymują w prompcie niewielką liczbę przykładów wejścia i wyjścia, aby kierować ich zachowaniem.

## Key Concepts

- Uczenie w kontekście
- Inżynieria promptów
- Kierowanie oparte na przykładach
- Porównanie z zero-shot

## Use Cases

- Formatowanie analizy sentymentu
- Dostosowanie stylu kodowania
- Ekstrakcja danych strukturalnych

## Code Example

```python
response = llm.generate(
    prompt="Translate English to French:\n"
           "Hello -> Bonjour\n"
           "World -> Monde\n"
           "Cat -> ?"
)
```

## Related Terms

- [zero_shot (uczenie zero-shot)](/en/terms/zero_shot-uczenie-zero-shot/)
- [prompt_engineering (inżynieria promptów)](/en/terms/prompt_engineering-inżynieria-promptów/)
- [in_context_learning (uczenie w kontekście)](/en/terms/in_context_learning-uczenie-w-kontekście/)
- [llm (duże modele językowe)](/en/terms/llm-duże-modele-językowe/)
