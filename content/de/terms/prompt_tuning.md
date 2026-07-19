---
title: Prompt-Tuning
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
date: '2026-07-18T11:28:44.805994Z'
lastmod: '2026-07-18T11:44:44.977887Z'
draft: false
source: agnes_llm
status: published
language: de
description: Eine parameter-effiziente Feinabstimmungsmethode, die kontinuierliche
  Eingabe-Embeddings optimiert, anstatt die gesamten Modellgewichte zu aktualisieren.
---
## Definition

Beim Prompt-Tuning werden trainierbare „Soft Prompts“ (kontinuierliche Vektoren) zur Eingabeschicht eines vortrainierten Sprachmodells hinzugefügt, während die zugrunde liegenden Modellparameter eingefroren bleiben. Dieser Ansatz ermöglicht eine effiziente Anpassung.

### Summary

Eine parameter-effiziente Feinabstimmungsmethode, die kontinuierliche Eingabe-Embeddings optimiert, anstatt die gesamten Modellgewichte zu aktualisieren.

## Key Concepts

- Soft Prompts
- Parameter-Effizienz
- eingefrorene Gewichte
- Few-Shot-Lernen

## Use Cases

- Anpassung von LLMs an spezifische Domänen
- Feinabstimmung bei geringen Datenressourcen
- Optimierung des Multi-Task-Lernens

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning)](/en/terms/peft-parameter-efficient-fine-tuning/)
- [LoRA (Low-Rank Adaptation)](/en/terms/lora-low-rank-adaptation/)
- [in-context learning (Lernen im Kontext)](/en/terms/in-context-learning-lernen-im-kontext/)
- [fine-tuning (Feinabstimmung)](/en/terms/fine-tuning-feinabstimmung/)
