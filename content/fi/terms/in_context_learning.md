---
title: "Kontekstipohjainen oppiminen"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
date: "2026-07-18T15:22:52.575547Z"
lastmod: "2026-07-18T17:15:09.345160Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Tekniikka, jossa mallit oppivat suorittamaan tehtäviä havainnoimalla promptissa annettuja esimerkkejä."
---
## Definition

Kontekstipohjainen oppiminen (ICL) mahdollistaa suurten kielimallien mukautumisen uusiin tehtäviin ilman painoarvojen päivitystä. Antamalla syöttö-tulos-parit promptin kontekstiin malli päättelisi kuviota ja pystyy suorittamaan tehtävän välittömästi.

### Summary

Tekniikka, jossa mallit oppivat suorittamaan tehtäviä havainnoimalla promptissa annettuja esimerkkejä.

## Key Concepts

- Harvennusoppiminen (Few-Shot)
- Nollanäyteoppiminen (Zero-Shot)
- Prompt-suunnittelu
- Painoarvovapaa mukauttaminen

## Use Cases

- Mallikykyjen nopea testaus uusilla datamäärillä
- Dynaaminen tehtävien vaihto keskusteluagenttien toiminnassa
- Teekoälysovellusten prototyypitys ilman uudelleenkoulutusta

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Prompt-inženööritaito](/en/terms/prompt-inženööritaito/)
- [Harvennusnäyte (Few-Shot)](/en/terms/harvennusnäyte-few-shot/)
- [Nollanäyte (Zero-Shot)](/en/terms/nollanäyte-zero-shot/)
- [Meta-oppiminen](/en/terms/meta-oppiminen/)
