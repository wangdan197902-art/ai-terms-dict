---
title: "Positionell kodning"
term_id: "positional_encoding"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "nlp", "architecture"]
difficulty: 3
weight: 1
slug: "positional_encoding"
aliases:
  - /sv/terms/positional_encoding/
date: "2026-07-18T15:39:34.052480Z"
lastmod: "2026-07-18T17:15:08.965301Z"
draft: false
source: "agnes_llm"
status: "published"
language: "sv"
description: "En teknik som injicerar information om den relativa eller absoluta positionen för token i en sekvens in i transformer-modeller."
---

## Definition

Eftersom transformers behandlar alla token parallellt snarare än sekventiellt som RNN:er saknar de inneboende kunskap om tokenordning. Positionell kodning lägger till specifika vektorer till inbäddningsvektorerna för att bevara ordningsinformationen.

### Summary

En teknik som injicerar information om den relativa eller absoluta positionen för token i en sekvens in i transformer-modeller.

## Key Concepts

- Sekvensordning
- Självuppmärksamhet
- Sinusfunktioner
- Token-inbäddningar

## Use Cases

- Maskinöversättning
- Textsammanfattning
- Språkmodellering

## Code Example

```python
import torch
import math
def get_positional_encoding(seq_len, d_model):
    pe = torch.zeros(seq_len, d_model)
    position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)
    div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)
    return pe.unsqueeze(0)
```

## Related Terms

- [Transformerarkitektur (Arkitekturen bakom Transformer-modeller)](/en/terms/transformerarkitektur-arkitekturen-bakom-transformer-modeller/)
- [Inbäddning (Vektorrepresentation av data)](/en/terms/inbäddning-vektorrepresentation-av-data/)
- [Uppmärksamhetsmekanism (Metod för att fokusera på delar av indata)](/en/terms/uppmärksamhetsmekanism-metod-för-att-fokusera-på-delar-av-indata/)
- [RoPE (Rotated Positional Encoding)](/en/terms/rope-rotated-positional-encoding/)
