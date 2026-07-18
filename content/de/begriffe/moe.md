---
title: "Mixture of Experts"
term_id: "moe"
category: "basic_concepts"
subcategory: ""
tags: ["Architecture", "Efficiency", "LLMs"]
difficulty: 4
weight: 1
slug: "moe"
aliases:
  - /de/terms/moe/
date: "2026-07-18T11:24:23.548967Z"
lastmod: "2026-07-18T11:44:44.966785Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Ein Architekturmuster, bei dem mehrere spezialisierte neuronale Netze (Experten) durch einen Gating-Mechanismus kombiniert werden, um Eingaben zu verarbeiten."
---

## Definition

Mixture of Experts (MoE) ist eine Machine-Learning-Architektur, die entwickelt wurde, um Effizienz und Skalierbarkeit zu verbessern. Anstatt ein einzelnes großes Modell für alle Aufgaben zu verwenden, setzt MoE mehrere kleinere 'Expert'-N

### Summary

Ein Architekturmuster, bei dem mehrere spezialisierte neuronale Netze (Experten) durch einen Gating-Mechanismus kombiniert werden, um Eingaben zu verarbeiten.

## Key Concepts

- Sparsity Activation (Spärliche Aktivierung)
- Gating Network (Steuerungsnetzwerk)
- Expert Specialization (Experten-Spezialisierung)
- Skalierbarkeit

## Use Cases

- Effizientes Training großer Sprachmodelle
- Reduzierung der Inferenzlatenz für massive Modelle
- Verarbeitung unterschiedlicher Eingabetypen in multimodalen Systemen

## Related Terms

- [Sparse Transformers (Spärliche Transformer)](/en/terms/sparse-transformers-spärliche-transformer/)
- [Conditional Computation (Bedingte Berechnung)](/en/terms/conditional-computation-bedingte-berechnung/)
- [Large Language Models (Große Sprachmodelle)](/en/terms/large-language-models-große-sprachmodelle/)
- [Neural Architecture Search (Neuronale Architektursuche)](/en/terms/neural-architecture-search-neuronale-architektursuche/)
