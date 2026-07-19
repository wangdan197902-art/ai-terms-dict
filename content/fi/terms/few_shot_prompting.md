---
title: Few-shot-prompting
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
date: '2026-07-18T15:36:25.697003Z'
lastmod: '2026-07-18T17:15:09.370319Z'
draft: false
source: agnes_llm
status: published
language: fi
description: Few-shot-prompting on tekniikka, jossa suurille kielimalleille annetaan
  ohjeistuksessa pieni määrä syöte-tuloste-esimerkkejä käyttäytymisen ohjaamiseksi.
---
## Definition

Tämä menetelmä hyödyntää suurten kielimallien kontekstissa oppimiskykyjä tarjoamalla muutamia havainnollistavia esimerkkejä suoraan promptissa. Toisin kuin hienosäätö, joka vaatii mallin painojen päivittämistä.

### Summary

Few-shot-prompting on tekniikka, jossa suurille kielimalleille annetaan ohjeistuksessa pieni määrä syöte-tuloste-esimerkkejä käyttäytymisen ohjaamiseksi.

## Key Concepts

- Kontekstissa oppiminen
- Prompt-insinööritaito
- Esimerkkeihin perustuva ohjaus
- Vertailu nollanäytteiseen oppimiseen

## Use Cases

- Tunneanalyysin muotoilu
- Koodityylin mukauttaminen
- Rakenteisen datan erottaminen

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

- [zero_shot (nollanäyte)](/en/terms/zero_shot-nollanäyte/)
- [prompt_engineering (prompt-insinööritaito)](/en/terms/prompt_engineering-prompt-insinööritaito/)
- [in_context_learning (kontekstissa oppiminen)](/en/terms/in_context_learning-kontekstissa-oppiminen/)
- [llm (suuri kielimalli)](/en/terms/llm-suuri-kielimalli/)
