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
  - /de/terms/transformer/
date: "2026-07-18T10:54:44.482482Z"
lastmod: "2026-07-18T11:44:44.886088Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Eine Deep-Learning-Architektur, die auf Selbst-Aufmerksamkeitsmechanismen basiert und sequenzielle Daten parallel statt sequentiell verarbeitet."
---

## Definition

Die Transformer-Architektur, vorgestellt im Paper 'Attention Is All You Need', hat die Verarbeitung natürlicher Sprache und darüber hinaus revolutioniert. Sie nutzt Multi-Head-Selbst-Aufmerksamkeit, um die Bedeutung von...

### Summary

Eine Deep-Learning-Architektur, die auf Selbst-Aufmerksamkeitsmechanismen basiert und sequenzielle Daten parallel statt sequentiell verarbeitet.

## Key Concepts

- Selbst-Aufmerksamkeit
- Multi-Head-Aufmerksamkeit
- Positions-Encoding
- Encoder-Decoder-Struktur

## Use Cases

- Maschinelle Übersetzung
- Textgenerierung
- Bilderkennung (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (Aufmerksamkeitsmechanismus)](/en/terms/attention_mechanism-aufmerksamkeitsmechanismus/)
- [bert (Bidirectional Encoder Representations from Transformers)](/en/terms/bert-bidirectional-encoder-representations-from-transformers/)
- [gpt (Generative Pre-trained Transformer)](/en/terms/gpt-generative-pre-trained-transformer/)
- [self_attention (Selbst-Aufmerksamkeit)](/en/terms/self_attention-selbst-aufmerksamkeit/)
