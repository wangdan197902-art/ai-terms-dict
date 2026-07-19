---
title: Codifica Posizionale
term_id: positional_encoding
category: basic_concepts
subcategory: ''
tags:
- transformers
- NLP
- architecture
difficulty: 3
weight: 1
slug: positional_encoding
date: '2026-07-18T15:36:49.930079Z'
lastmod: '2026-07-18T17:15:08.588524Z'
draft: false
source: agnes_llm
status: published
language: it
description: Una tecnica che inietta informazioni sulla posizione relativa o assoluta
  dei token in una sequenza nei modelli transformer.
---
## Definition

Poiché i transformer elaborano tutti i token in parallelo anziché in sequenza come le RNN, non possiedono una conoscenza intrinseca dell'ordine dei token. La codifica posizionale aggiunge vettori specifici agli embedding di input per preservare l'ordine sequenziale.

### Summary

Una tecnica che inietta informazioni sulla posizione relativa o assoluta dei token in una sequenza nei modelli transformer.

## Key Concepts

- Ordine della Sequenza
- Auto-Attenzione
- Funzioni Senoidali
- Embedding dei Token

## Use Cases

- Traduzione Automatica
- Riassunto del Testo
- Modellazione Linguistica

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

- [Architettura Transformer (Struttura del modello basata su attention)](/en/terms/architettura-transformer-struttura-del-modello-basata-su-attention/)
- [Embedding (Rappresentazione vettoriale delle parole)](/en/terms/embedding-rappresentazione-vettoriale-delle-parole/)
- [Meccanismo di Attenzione (Metodo per pesare l'importanza delle parti dell'input)](/en/terms/meccanismo-di-attenzione-metodo-per-pesare-l-importanza-delle-parti-dell-input/)
- [RoPE (Rotary Positional Embedding, una specifica tecnica di codifica posizionale)](/en/terms/rope-rotary-positional-embedding-una-specifica-tecnica-di-codifica-posizionale/)
