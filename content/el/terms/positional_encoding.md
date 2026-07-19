---
title: Θέση Κωδικοποίησης
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
date: '2026-07-18T15:43:02.239997Z'
lastmod: '2026-07-18T17:15:09.869192Z'
draft: false
source: agnes_llm
status: published
language: el
description: Μια τεχνική που ενσωματώνει πληροφορίες σχετικά με τη σχετική ή απόλυτη
  θέση των tokens σε μια ακολουθία στα μοντέλα Transformer.
---
## Definition

Επειδή τα μοντέλα Transformer επεξεργάζονται όλα τα tokens παράλληλα και όχι διαδοχικά όπως τα RNN, δεν διαθέτουν εγγενή γνώση της σειράς των tokens. Η κωδικοποίηση θέσης προσθέτει συγκεκριμένα διανύσματα στις εισόδους ενσωμάτωσης (embeddings) για να παρέχει πληροφορίες σχετικά με τη σειρά των δεδομένων.

### Summary

Μια τεχνική που ενσωματώνει πληροφορίες σχετικά με τη σχετική ή απόλυτη θέση των tokens σε μια ακολουθία στα μοντέλα Transformer.

## Key Concepts

- Σειρά Ακολουθίας
- Αυτο-Προσοχή
- Ημιτονοειδείς Συναρτήσεις
- Ενσωματώσεις Tokens

## Use Cases

- Μηχανική Μετάφραση
- Σύνοψη Κειμένου
- Γλωσσικό Μοντελοποίηση

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

- [Transformer Architecture (Αρχιτεκτονική Transformer)](/en/terms/transformer-architecture-αρχιτεκτονική-transformer/)
- [Embedding (Ενσωμάτωση)](/en/terms/embedding-ενσωμάτωση/)
- [Attention Mechanism (Μηχανισμός Προσοχής)](/en/terms/attention-mechanism-μηχανισμός-προσοχής/)
- [RoPE (Rotary Positional Embedding)](/en/terms/rope-rotary-positional-embedding/)
