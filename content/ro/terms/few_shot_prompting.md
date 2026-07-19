---
title: Prompting cu Puține Exemple
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
date: '2026-07-18T15:35:52.633773Z'
lastmod: '2026-07-18T17:15:09.614293Z'
draft: false
source: agnes_llm
status: published
language: ro
description: Prompting-ul cu puține exemple este o tehnică în care modelele lingvistice
  mari primesc un număr mic de exemple intrare-ieșire în cadrul promptului pentru
  a ghida comportamentul lor.
---
## Definition

Această metodă exploatează capacitatea de învățare în context a modelelor lingvistice mari, furnizând câteva exemple ilustrative direct în prompt. Spre deosebire de ajustarea fină (fine-tuning), care necesită actualizarea ponderilor modelului, această abordare modifică doar contextul de intrare pentru a îmbunătăți performanța.

### Summary

Prompting-ul cu puține exemple este o tehnică în care modelele lingvistice mari primesc un număr mic de exemple intrare-ieșire în cadrul promptului pentru a ghida comportamentul lor.

## Key Concepts

- Învățare în context
- Ingineria prompturilor
- Ghidare bazată pe exemple
- Comparație zero-shot

## Use Cases

- Formatarea analizei sentimentelor
- Adaptarea stilului de codare
- Extragerea structurată a datelor

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

- [zero_shot (fără exemple)](/en/terms/zero_shot-fără-exemple/)
- [prompt_engineering (ingineria prompturilor)](/en/terms/prompt_engineering-ingineria-prompturilor/)
- [in_context_learning (învățare în context)](/en/terms/in_context_learning-învățare-în-context/)
- [llm (model lingvistic mare)](/en/terms/llm-model-lingvistic-mare/)
