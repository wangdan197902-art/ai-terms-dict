---
title: "MobileNet"
term_id: "mobilenet"
category: "basic_concepts"
subcategory: ""
tags: ["CNN", "Optimization", "Mobile AI"]
difficulty: 2
weight: 1
slug: "mobilenet"
aliases:
  - /el/terms/mobilenet/
date: "2026-07-18T16:21:45.940385Z"
lastmod: "2026-07-18T17:15:09.932587Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Το MobileNet είναι μια οικογένεια ελαφρών βαθιών νευρωνικών δικτύων, σχεδιασμένη για εφαρμογές όρασης σε κινητές και ενσωματωμένες συσκευές."
---

## Definition

Τα MobileNet χρησιμοποιούν χωριστές βάθους διαχωριστικές συστάδες (depthwise separable convolutions) για να μειώσουν δραματικά το υπολογιστικό κόστος και το μέγεθος του μοντέλου σε σύγκριση με τις τυπικές συστάδες. Αυτή η αρχιτεκτονική επιτρέπει την αποδοτική εξαγωγή χαρακτηριστικών σε

### Summary

Το MobileNet είναι μια οικογένεια ελαφρών βαθιών νευρωνικών δικτύων, σχεδιασμένη για εφαρμογές όρασης σε κινητές και ενσωματωμένες συσκευές.

## Key Concepts

- Χωριστές Βάθους Διαχωριστικές Συστάδες
- Απόδοση Μοντέλου
- Υπολογισμός Άκρου (Edge Computing)
- Μεταφορά Μάθησης

## Use Cases

- Ανίχνευση αντικειμένων σε πραγματικό χρόνο σε smartphones
- Ταξινόμηση εικόνων σε συσκευές IoT
- Αναγνώριση προσώπου σε εφαρμογές κινητών

## Code Example

```python
from tensorflow.keras.applications import MobileNetV2
model = MobileNetV2(weights='imagenet', input_shape=(224, 224, 3))
```

## Related Terms

- [ShuffleNet (Δίκτυο ανακάτευξης)](/en/terms/shufflenet-δίκτυο-ανακάτευξης/)
- [SqueezeNet (Ελαφρύ δίκτυο συμπίεσης)](/en/terms/squeezenet-ελαφρύ-δίκτυο-συμπίεσης/)
- [EfficientNet (Αποδοτικό δίκτυο)](/en/terms/efficientnet-αποδοτικό-δίκτυο/)
- [Convolutional Neural Network (Νευρωνικό Δίκτυο Συστάδων)](/en/terms/convolutional-neural-network-νευρωνικό-δίκτυο-συστάδων/)
