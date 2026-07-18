---
title: "Ανίχνευση Χαρακτηριστικών (Feature Hashing)"
term_id: "feature_hashing"
category: "basic_concepts"
subcategory: ""
tags: ["preprocessing", "text-mining", "optimization"]
difficulty: 3
weight: 1
slug: "feature_hashing"
aliases:
  - /el/terms/feature_hashing/
date: "2026-07-18T16:07:16.335685Z"
lastmod: "2026-07-18T17:15:09.908085Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Μια τεχνική που χαρτογραφεί χαρακτηριστικά υψηλής διάστασης και αραιά σε ένα διάνυσμα σταθερού μεγέθους χρησιμοποιώντας μια συνάρτηση αρίθμησης (hash function)."
---

## Definition

Η ανίχνευση χαρακτηριστικών, γνωστή επίσης ως το κόλπο της αρίθμησης (hashing trick), επιτρέπει στα μοντέλα μηχανικής μάθησης να διαχειρίζονται μεγάλους, αραιούς χώρους χαρακτηριστικών χωρίς να διατηρούν ρητή χαρτογράφηση μεταξύ των χαρακτηριστικών και των δεικτών τους. Εφαρμόζοντας

### Summary

Μια τεχνική που χαρτογραφεί χαρακτηριστικά υψηλής διάστασης και αραιά σε ένα διάνυσμα σταθερού μεγέθους χρησιμοποιώντας μια συνάρτηση αρίθμησης (hash function).

## Key Concepts

- Συνάρτηση αρίθμησης (Hash function)
- Αραιά διανύσματα (Sparse vectors)
- Μείωση διαστάσεων (Dimensionality reduction)
- Απόδοση μνήμης (Memory efficiency)

## Use Cases

- Ταξινόμηση κειμένου με μεγάλα λεξιλόγια
- Συστήματα σύστασης με τεράστιες συλλογές αντικειμένων
- Επεξεργασία δεδομένων σε πραγματικό χρόνο (streaming)

## Code Example

```python
from sklearn.feature_extraction import FeatureHasher
import numpy as np

# Example: Hashing text features
hasher = FeatureHasher(n_features=10, input_type='string')
docs = ['hello world', 'hello python', 'world python']
hashed = hasher.transform(docs)
print(hashed.toarray())
```

## Related Terms

- [One-hot encoding (Κωδικοποίηση ενός-προς-ένα)](/en/terms/one-hot-encoding-κωδικοποίηση-ενός-προς-ένα/)
- [Bag of Words (Σακούλα Λέξεων)](/en/terms/bag-of-words-σακούλα-λέξεων/)
- [Dimensionality reduction (Μείωση διαστάσεων)](/en/terms/dimensionality-reduction-μείωση-διαστάσεων/)
- [Sparse matrix (Αραιός πίνακας)](/en/terms/sparse-matrix-αραιός-πίνακας/)
