---
title: "Chain-of-Thought-prompting"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
aliases:
  - /no/terms/chain_of_thought_prompting/
date: "2026-07-18T15:36:23.215304Z"
lastmod: "2026-07-18T16:38:06.956665Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "Chain-of-Thought-prompting er en teknikk som oppfordrer store språkmodeller (LLM-er) til å generere mellomliggende resonnementstrinn før de produserer et endelig svar."
---

## Definition

Chain-of-Thought (CoT)-prompting forbedrer ytelsen til store språkmodeller på komplekse resonnementoppgaver ved eksplisitt å be modellen om å artikulere logikken steg for steg. I stedet for å hoppe direkte til svaret, bryter modellen ned problemet i mindre, logiske deler.

### Summary

Chain-of-Thought-prompting er en teknikk som oppfordrer store språkmodeller (LLM-er) til å generere mellomliggende resonnementstrinn før de produserer et endelig svar.

## Key Concepts

- Steg-for-steg-resonnement
- Læring med få eksempler (Few-Shot)
- Logisk deduksjon
- Mellomliggende steg

## Use Cases

- Løsning av matematiske ordproblemer
- Komplekse logiske resonnementoppgaver
- Feilsøking av feil i kodegenerering

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Zero-Shot-prompting (prompting uten eksempler)](/en/terms/zero-shot-prompting-prompting-uten-eksempler/)
- [Few-Shot-prompting (prompting med eksempler)](/en/terms/few-shot-prompting-prompting-med-eksempler/)
- [Selvkonsistens (sjekk av svar)](/en/terms/selvkonsistens-sjekk-av-svar/)
- [Resonnement (tankegang)](/en/terms/resonnement-tankegang/)
