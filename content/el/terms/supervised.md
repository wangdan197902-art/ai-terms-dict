---
title: "Υποθετημένη / Κατευθυνόμενη"
term_id: "supervised"
category: "training_techniques"
subcategory: ""
tags: ["ML", "training"]
difficulty: 2
weight: 1
slug: "supervised"
aliases:
  - /el/terms/supervised/
date: "2026-07-18T15:33:30.764445Z"
lastmod: "2026-07-18T17:15:09.855504Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Ένα παράδειγμα μηχανικής μάθησης όπου τα μοντέλα εκπαιδεύονται σε ζεύγη εισόδου-εξόδου με ετικέτες."
---

## Definition

Η μάθηση με υποθεσία περιλαμβάνει την παροχή δεδομένων σε έναν αλγόριθμο που περιλαμβάνει τόσο εισόδους όσο και σωστές απαντήσεις (ετικέτες). Το μοντέλο μαθαίνει να χαρτογραφεί τις εισόδους στις εξόδους ελαχιστοποιώντας τα σφάλματα πρόβλεψης. Αυτή η τεχνική...

### Summary

Ένα παράδειγμα μηχανικής μάθησης όπου τα μοντέλα εκπαιδεύονται σε ζεύγη εισόδου-εξόδου με ετικέτες.

## Key Concepts

- Δεδομένα με ετικέτες
- Χαρτογράφηση
- Ελαχιστοποίηση απωλειών

## Use Cases

- Ταξινόμηση εικόνων
- Ανίχνευση spam
- Πρόβλεψη τιμών

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

## Related Terms

- [Unsupervised (Μη υποθετημένη)](/en/terms/unsupervised-μη-υποθετημένη/)
- [Label (Ετικέτα)](/en/terms/label-ετικέτα/)
- [Regression (Παλινδρόμηση)](/en/terms/regression-παλινδρόμηση/)
