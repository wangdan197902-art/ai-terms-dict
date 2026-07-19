---
title: Few-shot prompting
term_id: few_shot_prompting
category: application_paradigms
subcategory: ''
tags:
- prompting
- LLM
- technique
difficulty: 2
weight: 1
slug: few_shot_prompting
date: '2026-07-18T15:38:10.807134Z'
lastmod: '2026-07-18T17:15:08.962692Z'
draft: false
source: agnes_llm
status: published
language: sv
description: Few-shot prompting är en teknik där stora språkmodeller (LLM) ges ett
  litet antal indata-och-utdata-exempel i prompten för att styra deras beteende.
---
## Definition

Denna metod utnyttjar stora språkmodellers förmåga till kontextbaserad inlärning genom att ge några illustrativa exempel direkt i prompten. Till skillnad från finjustering, som kräver uppdatering av modellens vikter...

### Summary

Few-shot prompting är en teknik där stora språkmodeller (LLM) ges ett litet antal indata-och-utdata-exempel i prompten för att styra deras beteende.

## Key Concepts

- Kontextbaserad inlärning
- Prompt-engineering
- Exempelledad styrning
- Jämförelse med zero-shot

## Use Cases

- Formatering av sentimentanalys
- Anpassning av kodstil
- Strukturerad dataextraktion

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

- [zero_shot (noll-skott/inlärning)](/en/terms/zero_shot-noll-skott-inlärning/)
- [prompt_engineering (prompt-design)](/en/terms/prompt_engineering-prompt-design/)
- [in_context_learning (inlärning i kontext)](/en/terms/in_context_learning-inlärning-i-kontext/)
- [llm (stor språkmodell)](/en/terms/llm-stor-språkmodell/)
