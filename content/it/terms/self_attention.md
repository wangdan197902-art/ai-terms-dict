---
title: "Auto-attenzione"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
date: "2026-07-18T15:29:24.301132Z"
lastmod: "2026-07-18T17:15:08.574626Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Un meccanismo che consente a una rete neurale di valutare l'importanza delle diverse parti della sequenza di input rispetto alle altre."
---
## Definition

L'auto-attenzione consente ai modelli di catturare le dipendenze tra tutte le posizioni in una sequenza simultaneamente, indipendentemente dalla distanza. Calcolando i punteggi di attenzione tra ogni coppia di token, permette...

### Summary

Un meccanismo che consente a una rete neurale di valutare l'importanza delle diverse parti della sequenza di input rispetto alle altre.

## Key Concepts

- Query-Chiave-Valore
- Punteggi di Attenzione
- Ponderazione Contestuale
- Elaborazione Parallela

## Use Cases

- Traduzione automatica
- Riassunto di testi
- Classificazione di immagini tramite Vision Transformers

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Trasformatore](/en/terms/trasformatore/)
- [Multi-head Attention (Attenzione multi-testa)](/en/terms/multi-head-attention-attenzione-multi-testa/)
- [Embeddings (Vettorializzazioni)](/en/terms/embeddings-vettorializzazioni/)
- [Modellazione di Sequenze](/en/terms/modellazione-di-sequenze/)
