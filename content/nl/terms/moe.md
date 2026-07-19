---
title: "Mixture of Experts"
term_id: "moe"
category: "basic_concepts"
subcategory: ""
tags: ["Architecture", "Efficiency", "LLMs"]
difficulty: 4
weight: 1
slug: "moe"
date: "2026-07-18T16:08:29.816075Z"
lastmod: "2026-07-18T17:15:08.769358Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Een architectuurpatroon waarbij meerdere gespecialiseerde neurale netwerken (experts) worden gecombineerd via een stuurmechanisme (gating mechanism) om invoer te verwerken."
---
## Definition

Mixture of Experts (MoE) is een machine learning-architectuur die is ontworpen om efficiëntie en schaalbaarheid te verbeteren. In plaats van één groot model voor alle taken te gebruiken, maakt MoE gebruik van meerdere kleinere 'expert'-netwerken die dynamisch worden geactiveerd op basis van de invoer.

### Summary

Een architectuurpatroon waarbij meerdere gespecialiseerde neurale netwerken (experts) worden gecombineerd via een stuurmechanisme (gating mechanism) om invoer te verwerken.

## Key Concepts

- Sparse Activation (spaarse activatie)
- Gating Network (sturnetwerk)
- Expert Specialization (expertspecialisatie)
- Schaalbaarheid

## Use Cases

- Efficiënt trainen van grote taalmodellen
- Verminderen van inferentielatentie voor massieve modellen
- Omgaan met diverse invoertypen in multimodale systemen

## Related Terms

- [Sparse Transformers (sparse transformatoren)](/en/terms/sparse-transformers-sparse-transformatoren/)
- [Conditional Computation (conditionele berekening)](/en/terms/conditional-computation-conditionele-berekening/)
- [Large Language Models (grote taalmodellen)](/en/terms/large-language-models-grote-taalmodellen/)
- [Neural Architecture Search (neurale architectuuroverzicht)](/en/terms/neural-architecture-search-neurale-architectuuroverzicht/)
