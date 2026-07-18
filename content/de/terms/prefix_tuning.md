---
title: "Prefix-Tuning"
term_id: "prefix_tuning"
category: "training_techniques"
subcategory: ""
tags: ["fine_tuning", "efficiency", "transformers"]
difficulty: 4
weight: 1
slug: "prefix_tuning"
aliases:
  - /de/terms/prefix_tuning/
date: "2026-07-18T11:28:02.085041Z"
lastmod: "2026-07-18T11:44:44.976374Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Eine parametereffiziente Feinabstimmungsmethode, die trainierbare kontinuierliche Vektoren zum Eingang von Transformer-Schichten hinzufügt."
---

## Definition

Prefix-Tuning ist eine parametereffiziente Adaptierungstechnik für vortrainierte Transformer-Modelle. Anstatt alle Modellgewichte zu aktualisieren, wird eine Sequenz von trainierbaren kontinuierlichen Vektoren (das Prefix) vor den eigentlichen Eingabe-Token angehängt. Dies ermöglicht es, das Modell an neue Aufgaben anzupassen, ohne die ursprünglichen Gewichte zu verändern.

### Summary

Eine parametereffiziente Feinabstimmungsmethode, die trainierbare kontinuierliche Vektoren zum Eingang von Transformer-Schichten hinzufügt.

## Key Concepts

- Parametereffizientes Tuning
- Weiche Prompts (Soft Prompts)
- Transformer-Schichten
- Gefrorener Backbone

## Use Cases

- Adaption für Few-Shot-Learning
- Multi-Task-Learning mit begrenzten Ressourcen
- Anpassung von LLMs für Nischendomänen

## Related Terms

- [prompt_tuning (Prompt-Tuning)](/en/terms/prompt_tuning-prompt-tuning/)
- [p_tuning (P-Tuning)](/en/terms/p_tuning-p-tuning/)
- [adapter_modules (Adapter-Module)](/en/terms/adapter_modules-adapter-module/)
- [peft (Parameter-Efficient Fine-Tuning)](/en/terms/peft-parameter-efficient-fine-tuning/)
