---
title: Atenção Multi-Cabeça
term_id: multi_head_attention
category: basic_concepts
subcategory: ''
tags:
- transformer
- NLP
- Deep Learning
difficulty: 4
weight: 1
slug: multi_head_attention
date: '2026-07-18T14:37:21.715301Z'
lastmod: '2026-07-18T15:51:59.434740Z'
draft: false
source: agnes_llm
status: published
language: pt
description: Um mecanismo em modelos transformadores que permite ao modelo prestar
  atenção a informações de diferentes subespaços de representação simultaneamente.
---
## Definition

A Atenção Multi-Cabeça estende o mecanismo de atenção padrão executando-o várias vezes em paralelo com diferentes projeções lineares aprendidas. Isso permite que o modelo atenda conjuntamente a diferentes tipos de informação e padrões nos dados.

### Summary

Um mecanismo em modelos transformadores que permite ao modelo prestar atenção a informações de diferentes subespaços de representação simultaneamente.

## Key Concepts

- Autoatenção
- Projeções Lineares
- Concatenação

## Use Cases

- Processamento de Linguagem Natural (PLN)
- Tradução Automática
- Classificação de Imagens com Vision Transformers

## Code Example

```python
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)

    def forward(self, x):
        # Simplified forward pass logic
        pass
```

## Related Terms

- [Scaled Dot-Product Attention (Atenção de Produto Escalar)](/en/terms/scaled-dot-product-attention-atenção-de-produto-escalar/)
- [Transformer (Transformador)](/en/terms/transformer-transformador/)
- [Embedding (Embedding/Representação Vetorial)](/en/terms/embedding-embedding-representação-vetorial/)
