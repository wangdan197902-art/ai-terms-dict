---
title: Few-shot promptolás
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
date: '2026-07-18T15:38:04.261979Z'
lastmod: '2026-07-18T17:15:09.740769Z'
draft: false
source: agnes_llm
status: published
language: hu
description: A few-shot promptolás egy technika, ahol a nagy nyelvi modelleknek (LLM)
  kis számú bemenet-kimenet példát adnak a prompton belül a viselkedésük irányítása
  érdekében.
---
## Definition

Ez a módszer kihasználja a nagy nyelvi modellek kontextusbeli tanulási képességeit, közvetlenül a promptba ágyazva néhány illusztratív példát. A finomhangolással (fine-tuning) ellentétben, amely a modell súlyainak frissítését igényli, ez a megközelítés azonnal alkalmazható, és segít a modellnek megérteni a kívánt formátumot vagy stílust a megadott példák alapján.

### Summary

A few-shot promptolás egy technika, ahol a nagy nyelvi modelleknek (LLM) kis számú bemenet-kimenet példát adnak a prompton belül a viselkedésük irányítása érdekében.

## Key Concepts

- Kontextusbeli tanulás
- Prompt mérnöki munka
- Példa-alapú irányítás
- Nulladik lövéses összehasonlítás

## Use Cases

- Hangulatértékelés formázása
- Kódolási stílus adaptálása
- Strukturált adatok kinyerése

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

- [zero_shot (nulladik lövéses)](/en/terms/zero_shot-nulladik-lövéses/)
- [prompt_engineering (prompt mérnöki munka)](/en/terms/prompt_engineering-prompt-mérnöki-munka/)
- [in_context_learning (kontextusbeli tanulás)](/en/terms/in_context_learning-kontextusbeli-tanulás/)
- [llm (nagy nyelvi modell)](/en/terms/llm-nagy-nyelvi-modell/)
