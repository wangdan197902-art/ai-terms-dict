---
title: "Promptowanie Myślenia Krok po Kroku"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
aliases:
  - /pl/terms/chain_of_thought_prompting/
date: "2026-07-18T15:34:01.618976Z"
lastmod: "2026-07-18T17:15:08.830152Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "Promptowanie Myślenia Krok po Kroku to technika zachęcająca duże modele językowe do generowania pośrednich kroków rozumowania przed wydaniem ostatecznej odpowiedzi."
---

## Definition

Promptowanie Myślenia Krok po Kroku (Chain-of-Thought, CoT) poprawia wydajność dużych modeli językowych w złożonych zadaniach rozumowania, wyraźnie prosząc model o uzasadnienie jego logiki krok po kroku. Zamiast przeskakiwać bezpośrednio do wyniku, model wyjaśnia swój proces myślowy.

### Summary

Promptowanie Myślenia Krok po Kroku to technika zachęcająca duże modele językowe do generowania pośrednich kroków rozumowania przed wydaniem ostatecznej odpowiedzi.

## Key Concepts

- Rozumowanie krok po kroku
- Uczenie z małymi próbkami
- Dedukcja logiczna
- Kroki pośrednie

## Use Cases

- Rozwiązywanie matematycznych zadań tekstowych
- Złożone zadania rozumowania logicznego
- Debugowanie błędów w generowanym kodzie

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Promptowanie Zero-Shot (bez przykładów)](/en/terms/promptowanie-zero-shot-bez-przykładów/)
- [Promptowanie Few-Shot (z kilkoma przykładami)](/en/terms/promptowanie-few-shot-z-kilkoma-przykładami/)
- [Spójność wewnętrzna (self-consistency)](/en/terms/spójność-wewnętrzna-self-consistency/)
- [Rozumowanie (proces logiczny)](/en/terms/rozumowanie-proces-logiczny/)
