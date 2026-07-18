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
  - /el/terms/transformer/
date: "2026-07-18T15:35:05.995523Z"
lastmod: "2026-07-18T17:15:09.856976Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Μια αρχιτεκτονική βαθιάς μάθησης βασισμένη σε μηχανισμούς αυτο-προσοχής που επεξεργάζεται δεδομένα ακολουθίας παράλληλα αντί για διαδοχικά."
---

## Definition

Εισήχθη στο άρθρο 'Attention Is All You Need', η αρχιτεκτονική Transformer επαναστάτησε στην επεξεργασία φυσικής γλώσσας και πέραν αυτής. Χρησιμοποιεί πολλαπλή αυτο-προσοχή για να ζυγίζει τη σημασία των

### Summary

Μια αρχιτεκτονική βαθιάς μάθησης βασισμένη σε μηχανισμούς αυτο-προσοχής που επεξεργάζεται δεδομένα ακολουθίας παράλληλα αντί για διαδοχικά.

## Key Concepts

- Αυτο-Προσοχή
- Πολυκεφαλή Προσοχή
- Θέση Κωδικοποίησης
- Δομή Κωδικοποιητή-Αποκωδικοποιητή

## Use Cases

- Μηχανική μετάφραση
- Γενολογία κειμένου
- Αναγνώριση εικόνας (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (μηχανισμός προσοχής)](/en/terms/attention_mechanism-μηχανισμός-προσοχής/)
- [bert (BERT)](/en/terms/bert-bert/)
- [gpt (GPT)](/en/terms/gpt-gpt/)
- [self_attention (αυτο-προσοχή)](/en/terms/self_attention-αυτο-προσοχή/)
