---
title: "Phi Katsayısı"
term_id: "phi_coefficient"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "evaluation_metrics", "binary_classification"]
difficulty: 3
weight: 1
slug: "phi_coefficient"
aliases:
  - /tr/terms/phi_coefficient/
date: "2026-07-18T16:09:12.140919Z"
lastmod: "2026-07-18T16:38:07.348879Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "İki ikili değişken arasındaki ilişkiyi ölçen istatistiksel bir ölçü."
---

## Definition

Phi katsayısı (φ), iki ikili değişken arasındaki ilişkiyi ölçen bir göstergedir ve ikili değişkenler için Pearson korelasyon katsayısı olarak hizmet eder. -1 ile +1 arasında değişir; 0, hiçbir ilişki olmadığını belirtir.

### Summary

İki ikili değişken arasındaki ilişkiyi ölçen istatistiksel bir ölçü.

## Key Concepts

- İkili değişkenler
- Korelasyon
- Bağımsızlık tablosu
- İlişki gücü

## Use Cases

- Doğruluk dışında ikili sınıflandırıcı performansını değerlendirme
- Evet/Hayır yanıtları içeren anket verilerindeki ilişkileri analiz etme
- Kategorik girdilere sahip veri setlerinde özellik seçimi

## Code Example

```python
import numpy as np
from scipy.stats import chi2_contingency
# Example: Calculate phi coefficient from a 2x2 confusion matrix
tn, fp, fn, tp = 90, 10, 5, 95
matrix = [[tn, fp], [fn, tp]]
chi2, p, dof, expected = chi2_contingency(matrix)
phi = np.sqrt(chi2 / (tn + fp + fn + tp))
print(f'Phi coefficient: {phi:.3f}')
```

## Related Terms

- [Cramer's V (Kramer'in V katsayısı)](/en/terms/cramer-s-v-kramer-in-v-katsayısı/)
- [Pearson correlation (Pearson korelasyonu)](/en/terms/pearson-correlation-pearson-korelasyonu/)
- [Confusion matrix (Karışıklık matrisi)](/en/terms/confusion-matrix-karışıklık-matrisi/)
- [Mutual information (Karşılıklı bilgi)](/en/terms/mutual-information-karşılıklı-bilgi/)
