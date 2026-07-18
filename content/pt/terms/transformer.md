---
title: "Transformer"
term_id: "transformer"
category: "basic_concepts"
subcategory: ""
tags: ["architecture", "nlp", "attention"]
difficulty: 4
weight: 1
slug: "transformer"
aliases:
  - /pt/terms/transformer/
date: "2026-07-18T14:40:25.887559Z"
lastmod: "2026-07-18T15:51:59.441482Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Uma arquitetura de aprendizado profundo baseada em mecanismos de autoatenção que processa dados sequenciais em paralelo, em vez de sequencialmente."
---

## Definition

Introduzido no artigo 'Attention Is All You Need', a arquitetura Transformer revolucionou o processamento de linguagem natural e além. Ela usa autoatenção multi-cabeça para pesar a significância de...

### Summary

Uma arquitetura de aprendizado profundo baseada em mecanismos de autoatenção que processa dados sequenciais em paralelo, em vez de sequencialmente.

## Key Concepts

- Autoatenção
- Atenção Multi-Cabeça
- Codificação Posicional
- Estrutura Codificador-Decodificador

## Use Cases

- Tradução automática
- Geração de texto
- Reconhecimento de imagens (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (mecanismo de atenção)](/en/terms/attention_mechanism-mecanismo-de-atenção/)
- [bert (BERT)](/en/terms/bert-bert/)
- [gpt (GPT)](/en/terms/gpt-gpt/)
- [self_attention (autoatenção)](/en/terms/self_attention-autoatenção/)
