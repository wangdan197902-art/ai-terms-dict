---
title: "Karışıklık Matrisi"
term_id: "confusion_matrix"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "classification", "metrics"]
difficulty: 2
weight: 1
slug: "confusion_matrix"
aliases:
  - /tr/terms/confusion_matrix/
date: "2026-07-18T15:46:04.805847Z"
lastmod: "2026-07-18T16:38:07.285699Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "Bir sınıflandırma modelinin test verileri üzerindeki performansını tanımlamak için kullanılan bir tablo."
---

## Definition

Karışıklık matrisi, genellikle denetimli öğrenme olan bir algoritmanın performansını görselleştirmeye izin veren özel bir tablo düzenidir. Gerçek pozitif, gerçek negatif, yanlış pozitif ve yanlış negatif sayılarını gösterir.

### Summary

Bir sınıflandırma modelinin test verileri üzerindeki performansını tanımlamak için kullanılan bir tablo.

## Key Concepts

- Gerçek Pozitifler
- Yanlış Negatifler
- Kesinlik (Precision)
- Hatırlama (Recall)

## Use Cases

- İkili sınıflandırıcıları değerlendirme
- Çok sınıflı sınıflandırma performansını analiz etme
- Dengesiz veri setlerinde model önyargısını hata ayıklama

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (kesinlik)](/en/terms/precision-kesinlik/)
- [recall (hatırlama)](/en/terms/recall-hatırlama/)
- [F1 skoru](/en/terms/f1-skoru/)
- [ROC eğrisi](/en/terms/roc-eğrisi/)
