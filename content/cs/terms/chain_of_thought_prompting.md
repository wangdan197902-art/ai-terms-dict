---
title: "Prompting myšlenkovým řetězcem"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
aliases:
  - /cs/terms/chain_of_thought_prompting/
date: "2026-07-18T15:34:23.578117Z"
lastmod: "2026-07-18T17:15:09.087804Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Prompting myšlenkovým řetězcem je technika, která podporuje velké jazykové modely k generování mezilehlých kroků úsudku před vydáním finální odpovědi."
---

## Definition

Prompting myšlenkovým řetězcem (CoT) zlepšuje výkon velkých jazykových modelů na složitých úlohách úsudku tím, že explicitně žádá model, aby formuloval svou logiku krok za krokem. Místo toho, aby skočil di

### Summary

Prompting myšlenkovým řetězcem je technika, která podporuje velké jazykové modely k generování mezilehlých kroků úsudku před vydáním finální odpovědi.

## Key Concepts

- Krok za krokem úsudku
- Učení s několika příklady
- Logická dedukce
- Mezilehlé kroky

## Use Cases

- Řešení matematických slovních úloh
- Úlohy složitého logického úsudku
- Ladění chyb ve generovaném kódu

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Prompting nulového příkladu (Zero-Shot)](/en/terms/prompting-nulového-příkladu-zero-shot/)
- [Prompting s několika příklady (Few-Shot)](/en/terms/prompting-s-několika-příklady-few-shot/)
- [Sebe-konzistence (Self-Consistency)](/en/terms/sebe-konzistence-self-consistency/)
- [Úsudk (Reasoning)](/en/terms/úsudk-reasoning/)
