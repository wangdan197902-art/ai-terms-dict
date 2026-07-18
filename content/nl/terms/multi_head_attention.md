---
title: "Multi-Head Attention"
term_id: "multi_head_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformer", "nlp", "deep_learning"]
difficulty: 4
weight: 1
slug: "multi_head_attention"
aliases:
  - /nl/terms/multi_head_attention/
date: "2026-07-18T15:28:13.847482Z"
lastmod: "2026-07-18T17:15:08.689326Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Een mechanisme in transformermodellen dat het model in staat stelt gelijktijdig informatie uit verschillende representatiesubruimten te benaderen."
---

## Definition

Multi-Head Attention breidt het standaard attention-mechanisme uit door deze meerdere keren parallel uit te voeren met verschillende geleerde lineaire projecties. Dit stelt het model in staat gezamenlijk informatie te benaderen uit verschillende representatieruimtes.

### Summary

Een mechanisme in transformermodellen dat het model in staat stelt gelijktijdig informatie uit verschillende representatiesubruimten te benaderen.

## Key Concepts

- Self-Attention (Zelfattention)
- Lineaire Projecties
- Concatenatie

## Use Cases

- Natural Language Processing (NLP)
- Machinevertaling
- Afbeeldingsclassificatie met Vision Transformers

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

- [Scaled Dot-Product Attention (Geschaald dot-product attention)](/en/terms/scaled-dot-product-attention-geschaald-dot-product-attention/)
- [Transformer (Transformer)](/en/terms/transformer-transformer/)
- [Embedding (Embedding)](/en/terms/embedding-embedding/)
