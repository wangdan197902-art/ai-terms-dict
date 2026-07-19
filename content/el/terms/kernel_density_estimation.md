---
title: Kernel density estimation
term_id: kernel_density_estimation
category: basic_concepts
subcategory: ''
tags:
- statistics
- probability
- Data Analysis
difficulty: 3
weight: 1
slug: kernel_density_estimation
date: '2026-07-18T16:16:11.063724Z'
lastmod: '2026-07-18T17:15:09.922855Z'
draft: false
source: agnes_llm
status: published
language: el
description: Μια μη παραμετρική μέθοδος που χρησιμοποιείται για την εκτίμηση της συνάρτησης
  πυκνότητας πιθανότητας μιας τυχαίας μεταβλητής με βάση ένα πεπερασμένο δείγμα δεδομένων.
---
## Definition

Η Εκτίμηση Πυκνότητας Πυρήνα (KDE) είναι μια θεμελιώδης στατιστική τεχνική που λειαίνει διακριτά σημεία δεδομένων για να δημιουργήσει μια συνεχή καμπύλη κατανομής πιθανότητας. Τοποθετεί μια συνάρτηση πυρήνα (συνήθως Γκαουσιανή) σε κάθε σημείο δεδομένου και αθροίζει αυτές τις συνεισφορές, παρέχοντας μια πιο ομαλή και ακριβέστερη απεικόνιση της υποκείμενης κατανομής σε σχέση με τα ιστογράγματα.

### Summary

Μια μη παραμετρική μέθοδος που χρησιμοποιείται για την εκτίμηση της συνάρτησης πυκνότητας πιθανότητας μιας τυχαίας μεταβλητής με βάση ένα πεπερασμένο δείγμα δεδομένων.

## Key Concepts

- Συνάρτηση Πυκνότητας Πιθανότητας
- Μη Παραμετρική Στατιστική
- Λείανση (Smoothing)
- Γκαουσιανός Πυρήνας

## Use Cases

- Εξερευνητική Ανάλυση Δεδομένων (EDA)
- Ανίχνευση ακραίων περιπτώσεων (anomalies) σε μονοδιάστατα δεδομένα
- Οπτικοποίηση των κατανομών χαρακτηριστικών σε σύνολα δεδομένων

## Code Example

```python
from scipy.stats import gaussian_kde
import numpy as np

data = np.random.normal(0, 1, 100)
kde = gaussian_kde(data)
x_vals = np.linspace(-3, 3, 100)
y_vals = kde(x_vals)
```

## Related Terms

- [Histogram (Ιστόγραμμα)](/en/terms/histogram-ιστόγραμμα/)
- [Parzen Window (Παράθυρο Parzen)](/en/terms/parzen-window-παράθυρο-parzen/)
- [Bandwidth Selection (Επιλογή Πλάτους Ζώνης)](/en/terms/bandwidth-selection-επιλογή-πλάτους-ζώνης/)
- [Scipy Stats (Βιβλιοθήκη Στατιστικών στην Python)](/en/terms/scipy-stats-βιβλιοθήκη-στατιστικών-στην-python/)
