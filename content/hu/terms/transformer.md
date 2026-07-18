---
title: "Transzformer"
term_id: "transformer"
category: "basic_concepts"
subcategory: ""
tags: ["architecture", "nlp", "attention"]
difficulty: 4
weight: 1
slug: "transformer"
aliases:
  - /hu/terms/transformer/
date: "2026-07-18T15:33:37.364837Z"
lastmod: "2026-07-18T17:15:09.732501Z"
draft: false
source: "agnes_llm"
status: "published"
language: "hu"
description: "Egy mélytanulási architektúra, amely az önmagára figyelő mechanizmusokon alapul, és párhuzamosan, nem pedig sorosan dolgozza fel a szekvenciális adatokat."
---

## Definition

Az 'Attention Is All You Need' című cikkben bemutatott transzformer architektúra forradalmasította a természetes nyelvfeldolgozást és azon túlmutató területeket. Többfejű önmagára figyelést használ a jelentőség súlyozására.

### Summary

Egy mélytanulási architektúra, amely az önmagára figyelő mechanizmusokon alapul, és párhuzamosan, nem pedig sorosan dolgozza fel a szekvenciális adatokat.

## Key Concepts

- Önmagára figyelem
- Többfejű figyelem
- Pozicionális kódolás
- Kodoló-dekodoló szerkezet

## Use Cases

- Gépi fordítás
- Szöveggenerálás
- Képfelismerés (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (figyelési mechanizmus)](/en/terms/attention_mechanism-figyelési-mechanizmus/)
- [bert (Bidirectional Encoder Representations from Transformers)](/en/terms/bert-bidirectional-encoder-representations-from-transformers/)
- [gpt (Generative Pre-trained Transformer)](/en/terms/gpt-generative-pre-trained-transformer/)
- [self_attention (önfigyelem)](/en/terms/self_attention-önfigyelem/)
