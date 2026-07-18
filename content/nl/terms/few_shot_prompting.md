---
title: "Few-Shot Prompting"
term_id: "few_shot_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["prompting", "llm", "technique"]
difficulty: 2
weight: 1
slug: "few_shot_prompting"
aliases:
  - /nl/terms/few_shot_prompting/
date: "2026-07-18T15:36:05.867675Z"
lastmod: "2026-07-18T17:15:08.704748Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Few-shot prompting is een techniek waarbij aan LLM's een klein aantal invoer-uitvoervoorbeelden binnen de prompt worden gegeven om hun gedrag te sturen."
---

## Definition

Deze methode maakt gebruik van de in-context learning-mogelijkheden van grote taalmodellen door enkele illustratieve voorbeelden direct in de prompt te bieden. In tegenstelling tot fine-tuning, waarbij modelgewichten moeten worden bijgewerkt, vereist dit geen hertraining van het model.

### Summary

Few-shot prompting is een techniek waarbij aan LLM's een klein aantal invoer-uitvoervoorbeelden binnen de prompt worden gegeven om hun gedrag te sturen.

## Key Concepts

- In-context learning
- Prompt engineering
- Voorbeeldgestuurde begeleiding
- Vergelijking met zero-shot

## Use Cases

- Opmaak van sentimentanalyse
- Aanpassing van codestijl
- Extractie van gestructureerde gegevens

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

- [zero_shot (zero-shot)](/en/terms/zero_shot-zero-shot/)
- [prompt_engineering (prompt-engineering)](/en/terms/prompt_engineering-prompt-engineering/)
- [in_context_learning (in-context learning)](/en/terms/in_context_learning-in-context-learning/)
- [llm (large language model)](/en/terms/llm-large-language-model/)
