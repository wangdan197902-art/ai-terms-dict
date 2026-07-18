---
title: "Etuliitelukitus"
term_id: "prefix_tuning"
category: "training_techniques"
subcategory: ""
tags: ["fine_tuning", "efficiency", "transformers"]
difficulty: 4
weight: 1
slug: "prefix_tuning"
aliases:
  - /fi/terms/prefix_tuning/
date: "2026-07-18T16:16:06.727083Z"
lastmod: "2026-07-18T17:15:09.444953Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Parametreja säästävä hienosäätömenetelmä, joka lisää opetettavia jatkuvia vektoreita transformer-kerrosten syötteeseen."
---

## Definition

Etuliitelukitus on parametreja säästävä sopeutustekniikka esikoulutetuille transformer-malleille. Sen sijaan, että kaikkia mallin painoarvoja päivitettäisiin, menetelmään lisätään opetettavien jatkuvien vektorien (etuliitteen) sekvenssi mallin syötteeseen tai kerroksiin, mikä mahdollistaa tehokkaan mukauttamisen vähäisellä laskentakustannuksella.

### Summary

Parametreja säästävä hienosäätömenetelmä, joka lisää opetettavia jatkuvia vektoreita transformer-kerrosten syötteeseen.

## Key Concepts

- Parametreja säästävä säätö
- Pehmeät kehotteet (soft prompts)
- Transformer-kerrokset
- Jäädytetty ydinmalli

## Use Cases

- Harvinaisen esimerkin oppimisen sopeutus
- Monitehtäväinen oppiminen rajoitetuilla resursseilla
- LLM:n räätälöinti niemeille aloille

## Related Terms

- [prompt_tuning (kehotelukitus)](/en/terms/prompt_tuning-kehotelukitus/)
- [p_tuning (parametrinen lukitus)](/en/terms/p_tuning-parametrinen-lukitus/)
- [adapter_modules (sovitusmoduulit)](/en/terms/adapter_modules-sovitusmoduulit/)
- [peft (parametreja säästävät hienosäädöt)](/en/terms/peft-parametreja-säästävät-hienosäädöt/)
