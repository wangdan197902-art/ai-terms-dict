---
title: Denetimli Öğrenme
term_id: supervised_learning
category: basic_concepts
subcategory: ''
tags:
- ML Basics
- training
- paradigms
difficulty: 1
weight: 1
slug: supervised_learning
date: '2026-07-18T15:37:31.383506Z'
lastmod: '2026-07-18T16:38:07.264575Z'
draft: false
source: agnes_llm
status: published
language: tr
description: Bir modelin etiketli eğitim örneklerine dayanarak girdileri çıktılara
  eşlemeyi öğrendiği bir makine öğrenimi paradigması.
---
## Definition

Denetimli öğrenmede algoritma, etiketli bir veri seti üzerinde eğitilir; yani her girdi örneği doğru çıktı ile eşleştirilir. Amaç, modelin girdiler ile çıktılar arasındaki temel ilişkiyi öğrenmesini sağlamaktır.

### Summary

Bir modelin etiketli eğitim örneklerine dayanarak girdileri çıktılara eşlemeyi öğrendiği bir makine öğrenimi paradigması.

## Key Concepts

- Etiketli Veri
- Girdi-Çıktı Eşlemesi
- Sınıflandırma
- Regresyon

## Use Cases

- Spam e-posta tespiti
- Ev fiyatı tahmini
- Görüntü tanıma

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Unsupervised Learning (Denetimsiz Öğrenme)](/en/terms/unsupervised-learning-denetimsiz-öğrenme/)
- [Training Set (Eğitim Kümesi)](/en/terms/training-set-eğitim-kümesi/)
- [Validation Set (Doğrulama Kümesi)](/en/terms/validation-set-doğrulama-kümesi/)
- [Model Accuracy (Model Doğruluğu)](/en/terms/model-accuracy-model-doğruluğu/)
