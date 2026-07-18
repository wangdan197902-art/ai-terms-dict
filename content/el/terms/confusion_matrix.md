---
title: "Πίνακας Σύγχυσης"
term_id: "confusion_matrix"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "classification", "metrics"]
difficulty: 2
weight: 1
slug: "confusion_matrix"
aliases:
  - /el/terms/confusion_matrix/
date: "2026-07-18T15:56:36.723321Z"
lastmod: "2026-07-18T17:15:09.891822Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Ένας πίνακας που χρησιμοποιείται για την περιγραφή της απόδοσης ενός μοντέλου ταξινόμησης σε ένα σύνολο δεδομένων δοκιμής."
---

## Definition

Ένας πίνακας σύγχυσης είναι μια συγκεκριμένη διάταξη πίνακα που επιτρέπει την οπτικοποίηση της απόδοσης ενός αλγορίθμου, συνήθως ενός εποπτευόμενου μοντέλου μάθησης. Δείχνει τις συχνότητες των αληθώς θετικών, αληθώς αρνητικών, ψευδώς θετικών και ψευδώς αρνητικών αποτελεσμάτων.

### Summary

Ένας πίνακας που χρησιμοποιείται για την περιγραφή της απόδοσης ενός μοντέλου ταξινόμησης σε ένα σύνολο δεδομένων δοκιμής.

## Key Concepts

- Αληθώς Θετικά
- Ψευδώς Αρνητικά
- Ακρίβεια
- Επαναφορά

## Use Cases

- Αξιολόγηση δυαδικών ταξινομητών
- Ανάλυση απόδοσης πολυταξονικής ταξινόμησης
- Αποσφαλμάτωση προκατάληψης μοντέλου σε ανισορροπημένα σύνολα δεδομένων

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (Ακρίβεια)](/en/terms/precision-ακρίβεια/)
- [recall (Επαναφορά)](/en/terms/recall-επαναφορά/)
- [F1 score (Βαθμολογία F1)](/en/terms/f1-score-βαθμολογία-f1/)
- [ROC curve (Καμπύλη ROC)](/en/terms/roc-curve-καμπύλη-roc/)
