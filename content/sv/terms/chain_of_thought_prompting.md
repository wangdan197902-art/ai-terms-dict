---
title: "Chain-of-Thought Prompting"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
aliases:
  - /sv/terms/chain_of_thought_prompting/
date: "2026-07-18T15:37:32.516186Z"
lastmod: "2026-07-18T17:15:08.960897Z"
draft: false
source: "agnes_llm"
status: "published"
language: "sv"
description: "Chain-of-Thought Prompting är en teknik som uppmuntrar stora språkmodeller (LLM) att generera mellanliggande resonemangssteg innan de ger ett slutgiltigt svar."
---

## Definition

Chain-of-Thought (CoT)-prompting förbättrar prestandan hos stora språkmodeller på komplexa resonemangsuppgifter genom att uttryckligen be modellen att redogöra för sin stegvisa logik. Istället för att hoppa direkt till

### Summary

Chain-of-Thought Prompting är en teknik som uppmuntrar stora språkmodeller (LLM) att generera mellanliggande resonemangssteg innan de ger ett slutgiltigt svar.

## Key Concepts

- Stegvis resonemang
- Few-shot-lärande
- Logisk deduktion
- Mellanliggande steg

## Use Cases

- Lösning av matematiska ordproblem
- Komplexa logiska resonemangsuppgifter
- Felsökning av fel i kodgenerering

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Zero-Shot Prompting (Prompting utan exempel)](/en/terms/zero-shot-prompting-prompting-utan-exempel/)
- [Few-Shot Prompting (Prompting med några få exempel)](/en/terms/few-shot-prompting-prompting-med-några-få-exempel/)
- [Self-Consistency (Självkonsistensmetod)](/en/terms/self-consistency-självkonsistensmetod/)
- [Resonemang (Logisk tankegång)](/en/terms/resonemang-logisk-tankegång/)
