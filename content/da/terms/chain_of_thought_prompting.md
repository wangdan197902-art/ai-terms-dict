---
title: "Chain-of-Thought Prompting"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
date: "2026-07-18T15:33:51.592669Z"
lastmod: "2026-07-18T17:15:09.242627Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "Chain-of-Thought Prompting er en teknik, der opmuntrer store sprogmodeller til at generere mellemste ræsonneringstrin, før de producerer et endeligt svar."
---
## Definition

Chain-of-Thought (CoT) prompting forbedrer ydeevnen hos store sprogmodeller på komplekse ræsonneringsopgaver ved eksplicit at bede modellen om at formulere sin trin-for-trin logik. I stedet for at springe direkte til svaret, bryder modellen opgaven ned i mindre, logiske dele.

### Summary

Chain-of-Thought Prompting er en teknik, der opmuntrer store sprogmodeller til at generere mellemste ræsonneringstrin, før de producerer et endeligt svar.

## Key Concepts

- Trin-for-trin ræsonnement
- Few-Shot Learning (læring med få eksempler)
- Logisk deduktion
- Mellemste trin

## Use Cases

- Løsning af matematiske ordproblemer
- Komplekse logiske ræsonneringsopgaver
- Fejlfinding i kodegenereringsfejl

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Zero-Shot Prompting (prompting uden eksempler)](/en/terms/zero-shot-prompting-prompting-uden-eksempler/)
- [Few-Shot Prompting (prompting med få eksempler)](/en/terms/few-shot-prompting-prompting-med-få-eksempler/)
- [Self-Consistency (selvkonsistens)](/en/terms/self-consistency-selvkonsistens/)
- [Ræsonnement (logisk tankegang)](/en/terms/ræsonnement-logisk-tankegang/)
