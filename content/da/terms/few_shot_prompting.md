---
title: Few-Shot Prompting
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
date: '2026-07-18T15:35:10.489011Z'
lastmod: '2026-07-18T17:15:09.244529Z'
draft: false
source: agnes_llm
status: published
language: da
description: Few-shot prompting er en teknik, hvor store sprogmodeller (LLM'er) gives
  et lille antal input-output-eksempler i prompten for at vejlede deres adfærd.
---
## Definition

Denne metode udnytter store sprogmodellers evne til kontekstuel læring ved at give et par illustrerende eksempler direkte i prompten. I modsætning til finjustering, som kræver opdatering af modellens vægte, ændrer denne teknik kun konteksten for modellen.

### Summary

Few-shot prompting er en teknik, hvor store sprogmodeller (LLM'er) gives et lille antal input-output-eksempler i prompten for at vejlede deres adfærd.

## Key Concepts

- Kontekstuel læring
- Prompt-engineering
- Eksempelbaseret vejledning
- Sammenligning med zero-shot

## Use Cases

- Formatering af sentimentanalyse
- Tilpasning af kodestil
- Udtrækning af strukturerede data

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

- [zero_shot (nul-skud)](/en/terms/zero_shot-nul-skud/)
- [prompt_engineering (prompt-engineering)](/en/terms/prompt_engineering-prompt-engineering/)
- [in_context_learning (kontekstuel læring)](/en/terms/in_context_learning-kontekstuel-læring/)
- [llm (store sprogmodeller)](/en/terms/llm-store-sprogmodeller/)
