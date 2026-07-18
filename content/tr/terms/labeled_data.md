---
title: "Etiketli Veri"
term_id: "labeled_data"
category: "basic_concepts"
subcategory: ""
tags: ["data", "supervised_learning", "fundamentals"]
difficulty: 1
weight: 1
slug: "labeled_data"
aliases:
  - /tr/terms/labeled_data/
date: "2026-07-18T16:00:13.733499Z"
lastmod: "2026-07-18T16:38:07.325839Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "Girdi özelliklerinin yanı sıra doğru çıktı veya hedef değerin de sağlandığı veri."
---

## Definition

Etiketli veri, denetimli makine öğreniminin temelini oluşturan, girdi örneklerini karşılık gelen gerçek etiketlerle eşleyen bir yapıdır. Algoritmaların girdi ile çıktı arasındaki haritalamayı öğrenmesini sağlar.

### Summary

Girdi özelliklerinin yanı sıra doğru çıktı veya hedef değerin de sağlandığı veri.

## Key Concepts

- Denetimli Öğrenme
- Gerçek Değer (Ground Truth)
- Etiketleme
- Hedef Değişken

## Use Cases

- Görüntü sınıflandırıcıları eğitme
- Konuşma tanıma sistemleri oluşturma
- Finans alanında tahmine dayalı modelleme

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (etiketsiz veri)](/en/terms/unlabeled_data-etiketsiz-veri/)
- [supervised_learning (denetimli öğrenme)](/en/terms/supervised_learning-denetimli-öğrenme/)
- [data_annotation (veri etiketleme)](/en/terms/data_annotation-veri-etiketleme/)
- [training_set (eğitim kümesi)](/en/terms/training_set-eğitim-kümesi/)
