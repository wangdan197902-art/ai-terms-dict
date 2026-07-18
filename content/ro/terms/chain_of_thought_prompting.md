---
title: "Prompting prin lanț de gândire"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
aliases:
  - /ro/terms/chain_of_thought_prompting/
date: "2026-07-18T15:34:44.277503Z"
lastmod: "2026-07-18T17:15:09.612541Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "Prompting-ul prin lanț de gândire este o tehnică care încurajează modelele lingvistice mari (LLM) să genereze pași intermediari de raționament înainte de a produce un răspuns final."
---

## Definition

Prompting-ul prin lanț de gândire (CoT) îmbunătățește performanța modelelor lingvistice mari la sarcini complexe de raționament, cerând explicit modelului să își articuleze logica pas cu pas. În loc să sară direct

### Summary

Prompting-ul prin lanț de gândire este o tehnică care încurajează modelele lingvistice mari (LLM) să genereze pași intermediari de raționament înainte de a produce un răspuns final.

## Key Concepts

- Raționament pas cu pas
- Învățare few-shot
- Deducție logică
- Pași intermediari

## Use Cases

- Rezolvarea problemelor matematice
- Sarcini complexe de raționament logic
- Depanarea erorilor de generare a codului

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Prompting zero-shot](/en/terms/prompting-zero-shot/)
- [Prompting few-shot](/en/terms/prompting-few-shot/)
- [Consistență internă](/en/terms/consistență-internă/)
- [Raționament](/en/terms/raționament/)
