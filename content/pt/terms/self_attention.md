---
title: "Autoatenção"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
date: "2026-07-18T14:39:35.214343Z"
lastmod: "2026-07-18T15:51:59.439202Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Um mecanismo que permite a uma rede neural pesar a importância de diferentes partes da sequência de entrada em relação às outras."
---
## Definition

A autoatenção permite que os modelos capturem dependências entre todas as posições em uma sequência simultaneamente, independentemente da distância. Ao calcular escores de atenção entre cada par de tokens, ele permite

### Summary

Um mecanismo que permite a uma rede neural pesar a importância de diferentes partes da sequência de entrada em relação às outras.

## Key Concepts

- Consulta-Chave-Valor
- Escores de Atenção
- Ponderação Contextual
- Processamento Paralelo

## Use Cases

- Tradução automática
- Resumo de texto
- Classificação de imagens por meio de Vision Transformers

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer (Transformador)](/en/terms/transformer-transformador/)
- [Multi-Head Attention (Atenção de Múltiplas Cabeças)](/en/terms/multi-head-attention-atenção-de-múltiplas-cabeças/)
- [Embeddings (Embarcamentos/Vetores)](/en/terms/embeddings-embarcamentos-vetores/)
- [Sequence Modeling (Modelagem de Sequências)](/en/terms/sequence-modeling-modelagem-de-sequências/)
