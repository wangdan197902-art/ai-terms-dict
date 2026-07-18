---
title: "Reparametrisierungstrick"
term_id: "reparameterization_trick"
category: "basic_concepts"
subcategory: ""
tags: ["deep_learning", "probabilistic_models", "optimization"]
difficulty: 4
weight: 1
slug: "reparameterization_trick"
aliases:
  - /de/terms/reparameterization_trick/
date: "2026-07-18T11:32:10.084713Z"
lastmod: "2026-07-18T11:44:44.981681Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Eine Technik, die stochastische Variablen von lernbaren Parametern trennt, um eine gradientenbasierte Optimierung in der variationalen Inferenz zu ermöglichen."
---

## Definition

Der Reparametrisierungstrick ist eine fundamentale Methode, die in variationalen Autoencodern und anderen probabilistischen Modellen verwendet wird. Er ermöglicht den Fluss von Gradienten durch stochastische Knoten, indem eine Zufallsvariable so ausgedrückt wird, dass sie deterministisch von den Parametern und einem unabhängigen Rauschterm abhängt.

### Summary

Eine Technik, die stochastische Variablen von lernbaren Parametern trennt, um eine gradientenbasierte Optimierung in der variationalen Inferenz zu ermöglichen.

## Key Concepts

- Variationale Inferenz
- Gradientenschätzung
- Stochastische Knoten
- Differenzierbare Simulation

## Use Cases

- Training von Variational Autoencodern (VAEs)
- Bayessche Neuronale Netze
- Probabilistische Graphische Modelle

## Code Example

```python
import torch
epsilon = torch.randn(100, 10)
mu = torch.zeros(100, 10)
sigma = torch.ones(100, 10)
z = mu + sigma * epsilon  # Reparameterized sampling
```

## Related Terms

- [ELBO (Evidence Lower Bound)](/en/terms/elbo-evidence-lower-bound/)
- [Latente Variablen](/en/terms/latente-variablen/)
- [Backpropagation](/en/terms/backpropagation/)
- [Monte-Carlo-Schätzung](/en/terms/monte-carlo-schätzung/)
