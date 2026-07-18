---
title: "Self-Attention (Αυτο-προσοχή)"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
aliases:
  - /el/terms/self_attention/
date: "2026-07-18T15:33:16.932316Z"
lastmod: "2026-07-18T17:15:09.854631Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Μηχανισμός που επιτρέπει σε ένα νευρωνικό δίκτυο να ζυγίζει τη σημασία διαφορετικών τμημάτων της ακολουθίας εισόδου σε σχέση με το καθένα."
---

## Definition

Η αυτο-προσοχή επιτρέπει στα μοντέλα να αποτυπώνουν εξαρτήσεις μεταξύ όλων των θέσεων σε μια ακολουθία ταυτόχρονα, ανεξάρτητα από την απόσταση. Υπολογίζοντας βαθμολογίες προσοχής μεταξύ κάθε ζεύγους συμβόλων, επιτρέπει...

### Summary

Μηχανισμός που επιτρέπει σε ένα νευρωνικό δίκτυο να ζυγίζει τη σημασία διαφορετικών τμημάτων της ακολουθίας εισόδου σε σχέση με το καθένα.

## Key Concepts

- Ερώτηση-Κλειδί-Τιμή (Query-Key-Value)
- Βαθμολογίες Προσοχής
- Πλαίσιο Βάρους
- Παράλληλη Επεξεργασία

## Use Cases

- Μηχανική μετάφραση
- Σύνοψη κειμένου
- Ταξινόμηση εικόνων μέσω Vision Transformers

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer (Μετασχηματιστής)](/en/terms/transformer-μετασχηματιστής/)
- [Multi-Head Attention (Πολυκεφαλής Προσοχή)](/en/terms/multi-head-attention-πολυκεφαλής-προσοχή/)
- [Embeddings (Ενσωματώσεις)](/en/terms/embeddings-ενσωματώσεις/)
- [Sequence Modeling (Μοντελοποίηση Ακολουθιών)](/en/terms/sequence-modeling-μοντελοποίηση-ακολουθιών/)
