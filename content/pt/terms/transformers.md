---
title: "Transformers"
term_id: "transformers"
category: "training_techniques"
subcategory: ""
tags: ["library", "tools", "ecosystem"]
difficulty: 2
weight: 1
slug: "transformers"
date: "2026-07-18T14:40:40.976704Z"
lastmod: "2026-07-18T15:51:59.441607Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Neste contexto, refere-se à biblioteca Hugging Face Transformers, uma ferramenta de código aberto popular para modelos de ponta em PLN (Processamento de Linguagem Natural) e multimodais."
---
## Definition

O termo 'Transformers' frequentemente se refere à biblioteca Python amplamente utilizada mantida pela Hugging Face. Ela fornece interfaces fáceis de usar para baixar, treinar e implantar modelos pré-treinados baseados em arquiteturas Transformer.

### Summary

Neste contexto, refere-se à biblioteca Hugging Face Transformers, uma ferramenta de código aberto popular para modelos de ponta em PLN (Processamento de Linguagem Natural) e multimodais.

## Key Concepts

- Hugging Face Hub
- API de Pipeline
- Cartões de Modelo (Model Cards)
- Integração com Tokenizers

## Use Cases

- Prototipagem rápida de aplicativos de PLN
- Acesso a modelos pré-treinados pela comunidade
- Padronização dos fluxos de trabalho de implantação de modelos

## Code Example

```python
from transformers import pipeline
classifier = pipeline('sentiment-analysis')
```

## Related Terms

- [hugging_face (Plataforma e biblioteca Hugging Face)](/en/terms/hugging_face-plataforma-e-biblioteca-hugging-face/)
- [pipeline (Pipeline de inferência)](/en/terms/pipeline-pipeline-de-inferência/)
- [tokenizer (Tokenizador)](/en/terms/tokenizer-tokenizador/)
- [pytorch (Framework PyTorch)](/en/terms/pytorch-framework-pytorch/)
