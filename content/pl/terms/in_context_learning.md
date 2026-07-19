---
title: "Uczenie w kontekście"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
date: "2026-07-18T15:23:05.011731Z"
lastmod: "2026-07-18T17:15:08.806382Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "Technika, w której modele uczą się wykonywać zadania poprzez obserwację przykładów dostarczonych w podpowiedzi."
---
## Definition

Uczenie w kontekście (ICL) pozwala dużym modelom językowym dostosowywać się do nowych zadań bez aktualizacji ich wag. Poprzez dostarczenie par wejście-wyjście w kontekście podpowiedzi, model wnioskuje wzorzec i...

### Summary

Technika, w której modele uczą się wykonywać zadania poprzez obserwację przykładów dostarczonych w podpowiedzi.

## Key Concepts

- Uczenie z niewielką liczbą przykładów
- Zero-shot
- Projektowanie podpowiedzi
- Adaptacja bez zmian wag

## Use Cases

- Szybkie testowanie możliwości modelu na nowych zbiorach danych
- Dynamiczne przełączanie zadań w agentach konwersacyjnych
- Prototypowanie aplikacji AI bez ponownego trenowania

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Inżynieria podpowiedzi](/en/terms/inżynieria-podpowiedzi/)
- [Few-shot (z małymi próbkami)](/en/terms/few-shot-z-małymi-próbkami/)
- [Zero-shot](/en/terms/zero-shot/)
- [Uczenie metryczne](/en/terms/uczenie-metryczne/)
