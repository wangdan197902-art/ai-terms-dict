---
title: "Διασταυρούμενη Επαλήθευση"
term_id: "cross_validation"
category: "training_techniques"
subcategory: ""
tags: ["evaluation", "machine-learning", "statistics"]
difficulty: 2
weight: 1
slug: "cross_validation"
aliases:
  - /el/terms/cross_validation/
date: "2026-07-18T15:57:32.719520Z"
lastmod: "2026-07-18T17:15:09.893709Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Μια διαδικασία δειγματοληψίας που χρησιμοποιείται για την αξιολόγηση μοντέλων μηχανικής μάθησης σε περιορισμένο δείγμα δεδομένων, χωρίζοντας τα δεδομένα σε υποσύνολα για εκπαίδευση και δοκιμή."
---

## Definition

Η διασταυρούμενη επαλήθευση είναι μια στατιστική μέθοδος που χρησιμοποιείται για την εκτίμηση της απόδοσης των μοντέλων μηχανικής μάθησης. Η πιο συνηθισμένη μορφή είναι η k-fold διασταυρούμενη επαλήθευση, όπου τα δεδομένα χωρίζονται σε k ίσα μέρη.

### Summary

Μια διαδικασία δειγματοληψίας που χρησιμοποιείται για την αξιολόγηση μοντέλων μηχανικής μάθησης σε περιορισμένο δείγμα δεδομένων, χωρίζοντας τα δεδομένα σε υποσύνολα για εκπαίδευση και δοκιμή.

## Key Concepts

- Χωρισμός K-Fold
- Γενίκευση Μοντέλου
- Ανίχνευση Υπερπροσαρμογής
- Εκτίμηση Απόδοσης

## Use Cases

- Ρύθμιση υπερπαραμέτρων
- Σύγκριση διαφορετικών αλγορίθμων
- Επαλήθευση της σταθερότητας του μοντέλου σε μικρά σύνολα δεδομένων

## Code Example

```python
from sklearn.model_selection import cross_val_score
cv_scores = cross_val_score(model, X, y, cv=5)
```

## Related Terms

- [Train-Test Split (Χωρισμός Εκπαίδευσης-Δοκιμής)](/en/terms/train-test-split-χωρισμός-εκπαίδευσης-δοκιμής/)
- [Leave-One-Out (Απόλυση-Ένα-Προς-Έξω)](/en/terms/leave-one-out-απόλυση-ένα-προς-έξω/)
- [Bootstrap (Bootstrap)](/en/terms/bootstrap-bootstrap/)
