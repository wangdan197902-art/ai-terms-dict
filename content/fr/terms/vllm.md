---
title: "vLLM"
term_id: "vllm"
category: "application_paradigms"
subcategory: ""
tags: ["inference", "optimization", "serving", "library"]
difficulty: 4
weight: 1
slug: "vllm"
aliases:
  - /fr/terms/vllm/
date: "2026-07-18T11:42:21.741457Z"
lastmod: "2026-07-18T11:44:45.355674Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "vLLM est un moteur d'inférence à haut débit et économe en mémoire pour les grands modèles de langage, utilisant la technique PagedAttention pour optimiser l'utilisation de la mémoire GPU."
---

## Definition

vLLM (Virtual Large Language Model) est une bibliothèque open source conçue pour accélérer le déploiement des LLM. Elle introduit PagedAttention, une technique de gestion de la mémoire inspirée de la mémoire virtuelle des systèmes d'exploitation, permettant une allocation de mémoire KV cache plus efficace.

### Summary

vLLM est un moteur d'inférence à haut débit et économe en mémoire pour les grands modèles de langage, utilisant la technique PagedAttention pour optimiser l'utilisation de la mémoire GPU.

## Key Concepts

- PagedAttention
- Gestion du cache KV
- Serveur d'inférence
- Optimisation du débit

## Use Cases

- Serveur d'API à haute concurrence
- Traitement par lots de l'inférence
- Déploiement rentable de LLM

## Code Example

```python
from vllm import LLM, SamplingParams
llm = LLM(model="facebook/opt-125m")
prompts = ["Hello, my name is", "The capital of France is"]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
outputs = llm.generate(prompts, sampling_params)
```

## Related Terms

- [TensorRT (Accélérateur NVIDIA)](/en/terms/tensorrt-accélérateur-nvidia/)
- [TGI (Text Generation Inference)](/en/terms/tgi-text-generation-inference/)
- [PagedAttention (Mécanisme d'attention par pages)](/en/terms/pagedattention-mécanisme-d-attention-par-pages/)
- [Serveur de LLM (LLM Serving)](/en/terms/serveur-de-llm-llm-serving/)
