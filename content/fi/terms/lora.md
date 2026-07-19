---
title: "LoRA"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
date: "2026-07-18T15:28:24.017544Z"
lastmod: "2026-07-18T17:15:09.353765Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Matalan rangin adaptointi on parametritehokas hienosäätömenetelmä, joka ruiskuttaa koulutettavia matalan rangin hajauttamismatriiseja olemassa oleviin mallipainoihin."
---
## Definition

LoRA jäädyttää esikoulutetut mallipainot ja lisää koulutettavia hajauttamismatriiseja jokaiseen transformer-arkkitehtuurin kerrokseen. Optimoiden vain näitä matalan rangin matriiseja, LoRA vähentää merkittävästi

### Summary

Matalan rangin adaptointi on parametritehokas hienosäätömenetelmä, joka ruiskuttaa koulutettavia matalan rangin hajauttamismatriiseja olemassa oleviin mallipainoihin.

## Key Concepts

- Parametritehokas hienosäätö
- Rangin hajauttaminen
- Painojen jäädyttäminen
- Sovitinmoduulit

## Use Cases

- Suurten kielimallien mukauttaminen
- Alakohtainen adaptointi
- Resurssirajoitteinen koulutus

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning)](/en/terms/peft-parameter-efficient-fine-tuning/)
- [Hienosäätö (Fine-Tuning)](/en/terms/hienosäätö-fine-tuning/)
- [Kvantitus](/en/terms/kvantitus/)
