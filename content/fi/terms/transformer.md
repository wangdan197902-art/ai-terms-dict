---
title: Muunnin
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
date: '2026-07-18T15:32:15.090653Z'
lastmod: '2026-07-18T17:15:09.361772Z'
draft: false
source: agnes_llm
status: published
language: fi
description: Syväoppimisarkkitehtuuri, joka perustuu itsehuomion mekanismeihin ja
  käsittelee sekvenssidataa rinnakkain peräkkäisen sijaan.
---
## Definition

Muunninarkkitehtuuri, joka esiteltiin artikkelissa "Attention Is All You Need", muutti kokonaan luonnollisen kielen käsittelyn ja sen ulkopuoliset alueet. Se käyttää monipäistä itsehuomiota punotakseen yhteen syvällisiä yhteyksiä datassa.

### Summary

Syväoppimisarkkitehtuuri, joka perustuu itsehuomion mekanismeihin ja käsittelee sekvenssidataa rinnakkain peräkkäisen sijaan.

## Key Concepts

- Itsehuomio
- Monipäinen huomio
- Paikallinen koodaus
- Kooderi-dekooderi-rakenne

## Use Cases

- Konemielikäännös
- Tekstin generointi
- Kuvantunnistus (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (huomiomekanismi)](/en/terms/attention_mechanism-huomiomekanismi/)
- [bert (Bidirectional Encoder Representations from Transformers -malli)](/en/terms/bert-bidirectional-encoder-representations-from-transformers-malli/)
- [gpt (Generative Pre-trained Transformer -malli)](/en/terms/gpt-generative-pre-trained-transformer-malli/)
- [self_attention (itsehuomio)](/en/terms/self_attention-itsehuomio/)
