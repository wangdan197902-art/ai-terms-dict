---
title: Softmax
term_id: softmax
category: basic_concepts
subcategory: ''
tags:
- math
- Neural Networks
- Classification
difficulty: 2
weight: 1
slug: softmax
date: '2026-07-18T15:45:07.264131Z'
lastmod: '2026-07-18T17:15:09.871140Z'
draft: false
source: agnes_llm
status: published
language: el
description: Μια μαθηματική συνάρτηση που μετατρέπει ένα διάνυσμα πραγματικών τιμών
  σε κατανομή πιθανότητας.
---
## Definition

Η Softmax χρησιμοποιείται ευρέως στο στρώμα εξόδου των νευρωνικών δικτύων για εργασίες ταξινόμησης πολλαπλών κλάσεων. Λαμβάνει ένα διάνυσμα ωμών λογίθ και τα κανονικοποιεί έτσι ώστε κάθε στοιχείο να αντιπροσωπεύει μια πιθανότητα.

### Summary

Μια μαθηματική συνάρτηση που μετατρέπει ένα διάνυσμα πραγματικών τιμών σε κατανομή πιθανότητας.

## Key Concepts

- Κατανομή Πιθανότητας
- Logits
- Κανονικοποίηση
- Ταξινόμηση Πολλαπλών Κλάσεων

## Use Cases

- Στρώματα εξόδου ταξινόμησης εικόνων
- Πρόβλεψη tokens σε γλωσσικά μοντέλα
- Ταξινόμηση πολλαπλών ετικετών

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (Ευρετήριο μέγιστης τιμής)](/en/terms/argmax-ευρετήριο-μέγιστης-τιμής/)
- [Cross-Entropy Loss (Απώλεια διασταυρούμενης εντροπίας)](/en/terms/cross-entropy-loss-απώλεια-διασταυρούμενης-εντροπίας/)
- [Logits (Ακατέργαστες προβλέψεις)](/en/terms/logits-ακατέργαστες-προβλέψεις/)
- [Neural Network (Νευρωνικό δίκτυο)](/en/terms/neural-network-νευρωνικό-δίκτυο/)
