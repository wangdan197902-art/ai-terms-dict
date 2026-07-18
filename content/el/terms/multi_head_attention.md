---
title: "Πολυκεφαλική Προσοχή"
term_id: "multi_head_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformer", "nlp", "deep_learning"]
difficulty: 4
weight: 1
slug: "multi_head_attention"
aliases:
  - /el/terms/multi_head_attention/
date: "2026-07-18T15:29:39.277115Z"
lastmod: "2026-07-18T17:15:09.849789Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Ένας μηχανισμός στα μοντέλα Transformer που επιτρέπει στο μοντέλο να προσέχει πληροφορίες από διαφορετικούς υποχώρους αναπαράστασης ταυτόχρονα."
---

## Definition

Η Πολυκεφαλική Προσοχή επεκτείνει τον τυπικό μηχανισμό προσοχής εκτελώντας τον πολλές φορές παράλληλα με διαφορετικές μαθημένες γραμμικές προβολές. Αυτό επιτρέπει στο μοντέλο να εξετάζει ταυτόχρονα πληροφορίες από διάφορες πηγές.

### Summary

Ένας μηχανισμός στα μοντέλα Transformer που επιτρέπει στο μοντέλο να προσέχει πληροφορίες από διαφορετικούς υποχώρους αναπαράστασης ταυτόχρονα.

## Key Concepts

- Αυτο-Προσοχή
- Γραμμικές Προβολές
- Σύμπλεξη

## Use Cases

- Επεξεργασία Φυσικής Γλώσσας (NLP)
- Μηχανική Μετάφραση
- Ταξινόμηση Εικόνων με Vision Transformers

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

- [Scaled Dot-Product Attention (Προσοχή Κλιμακωμένου Εσωτερικού Γινόμενου)](/en/terms/scaled-dot-product-attention-προσοχή-κλιμακωμένου-εσωτερικού-γινόμενου/)
- [Transformer (Transformer)](/en/terms/transformer-transformer/)
- [Embedding (Ενσωμάτωση/Embedding)](/en/terms/embedding-ενσωμάτωση-embedding/)
