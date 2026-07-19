---
title: Trasformatore
term_id: transformer
category: basic_concepts
subcategory: ''
tags:
- architecture
- NLP
- attention
difficulty: 4
weight: 1
slug: transformer
date: '2026-07-18T15:30:42.122940Z'
lastmod: '2026-07-18T17:15:08.576912Z'
draft: false
source: agnes_llm
status: published
language: it
description: Un'architettura di deep learning basata su meccanismi di auto-attenzione
  che elabora dati sequenziali in parallelo anziché in sequenza.
---
## Definition

Introdotta nell'articolo 'Attention Is All You Need', l'architettura Trasformatore ha rivoluzionato l'elaborazione del linguaggio naturale e non solo. Utilizza l'auto-attenzione multi-testa per ponderare l'importanza dei

### Summary

Un'architettura di deep learning basata su meccanismi di auto-attenzione che elabora dati sequenziali in parallelo anziché in sequenza.

## Key Concepts

- Auto-attenzione
- Attenzione multi-testa
- Codifica posizionale
- Struttura encoder-decoder

## Use Cases

- Traduzione automatica
- Generazione di testo
- Riconoscimento di immagini (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (meccanismo di attenzione)](/en/terms/attention_mechanism-meccanismo-di-attenzione/)
- [bert (Bidirectional Encoder Representations from Transformers)](/en/terms/bert-bidirectional-encoder-representations-from-transformers/)
- [gpt (Generative Pre-trained Transformer)](/en/terms/gpt-generative-pre-trained-transformer/)
- [self_attention (auto-attenzione)](/en/terms/self_attention-auto-attenzione/)
