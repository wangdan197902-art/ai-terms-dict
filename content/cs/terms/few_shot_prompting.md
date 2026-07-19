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
date: '2026-07-18T15:35:24.614503Z'
lastmod: '2026-07-18T17:15:09.089546Z'
draft: false
source: agnes_llm
status: published
language: cs
description: Few-shot prompting je technika, při které jsou velké jazykové modely
  (LLM) v rámci zadání (promptu) poskytnuty s malým počtem příkladů vstupů a výstupů
  k řízení jejich chování.
---
## Definition

Tato metoda využívá schopnosti kontextového učení velkých jazykových modelů tím, že přímo do zadání vloží několik ilustrativních příkladů. Na rozdíl od doladění modelu (fine-tuning), které vyžaduje aktualizaci vah modelu, tento přístup mění pouze vstupní kontext pro danou úlohu.

### Summary

Few-shot prompting je technika, při které jsou velké jazykové modely (LLM) v rámci zadání (promptu) poskytnuty s malým počtem příkladů vstupů a výstupů k řízení jejich chování.

## Key Concepts

- Učení v kontextu
- Inženýrství zadání (Prompt engineering)
- Vedení založené na příkladech
- Porovnání s nulovým zásahem (Zero-shot)

## Use Cases

- Formátování analýzy sentimentu
- Přizpůsobení stylu kódování
- Extrakce strukturovaných dat

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

- [zero_shot (učení s nulovým příkladem)](/en/terms/zero_shot-učení-s-nulovým-příkladem/)
- [prompt_engineering (inženýrství zadání)](/en/terms/prompt_engineering-inženýrství-zadání/)
- [in_context_learning (kontextové učení)](/en/terms/in_context_learning-kontextové-učení/)
- [llm (velký jazykový model)](/en/terms/llm-velký-jazykový-model/)
