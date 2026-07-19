---
title: Prompt-säätö
term_id: prompt_tuning
category: training_techniques
subcategory: ''
tags:
- LLM
- Optimization
- efficiency
difficulty: 3
weight: 1
slug: prompt_tuning
date: '2026-07-18T16:17:02.608251Z'
lastmod: '2026-07-18T17:15:09.446630Z'
draft: false
source: agnes_llm
status: published
language: fi
description: Parametritehokas hienosäätömenetelmä, joka optimoi jatkuvia syöte-embeddings-vektoreita
  päivittämättä koko mallin painoja.
---
## Definition

Prompt-säädössä esikoulutetun kielimallin syöttökerrokseen lisätään koulutettavia pehmeitä prompteja (jatkuvia vektoreita) pitäen samalla mallin taustaparametrit jäähdytettynä (muuttumattomina). Tämä lähestymistapa mahdollistaa tehokkaan mukauttamisen vähäisillä resursseilla.

### Summary

Parametritehokas hienosäätömenetelmä, joka optimoi jatkuvia syöte-embeddings-vektoreita päivittämättä koko mallin painoja.

## Key Concepts

- pehmeät promptit
- parametritehokkuus
- jäähdytetyt painot
- vähäisten esimerkkien oppiminen (few-shot learning)

## Use Cases

- Kielimallien (LLM) mukauttaminen tiettyihin aloihin
- Resurssivilja hienosäätö
- Monitehtävällisen oppimisen optimointi

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning -parametritehokas hienosäätö)](/en/terms/peft-parameter-efficient-fine-tuning-parametritehokas-hienosäätö/)
- [LoRA (Low-Rank Adaptation -matalan rangin sopeutus)](/en/terms/lora-low-rank-adaptation-matalan-rangin-sopeutus/)
- [in-context learning (kontekstipohjainen oppiminen)](/en/terms/in-context-learning-kontekstipohjainen-oppiminen/)
- [fine-tuning (hienosäätö)](/en/terms/fine-tuning-hienosäätö/)
