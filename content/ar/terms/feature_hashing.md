---
title: "تجزئة الميزات"
term_id: "feature_hashing"
category: "basic_concepts"
subcategory: ""
tags: ["preprocessing", "text-mining", "optimization"]
difficulty: 3
weight: 1
slug: "feature_hashing"
aliases:
  - /ar/terms/feature_hashing/
date: "2026-07-18T15:57:51.470789Z"
lastmod: "2026-07-18T17:15:08.503994Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "تقنية تقوم بربط الميزات المتفرقة عالية الأبعاد في متجه ذي حجم ثابت باستخدام دالة التجزئة."
---

## Definition

تسمح تجزئة الميزات، والمعروفة أيضاً باسم حيلة التجزئة، لنماذج التعلم الآلي بالتعامل مع مساحات ميزات كبيرة ومتفرقة دون الحاجة إلى الحفاظ على خريطة صريحة بين الميزات والفهارس. من خلال تطبيق دالة التجزئة، يتم تحويل الميزات إلى أبعاد ثابتة، مما يقلل من تعقيد الحسابات ويحسن الكفاءة.

### Summary

تقنية تقوم بربط الميزات المتفرقة عالية الأبعاد في متجه ذي حجم ثابت باستخدام دالة التجزئة.

## Key Concepts

- دالة التجزئة
- المتجهات المتفرقة
- اختزال الأبعاد
- كفاءة الذاكرة

## Use Cases

- تصنيف النصوص ذات المفردات الكبيرة
- أنظمة التوصية بمجموعات عناصر ضخمة
- معالجة بيانات التدفق في الوقت الفعلي

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

- [One-hot encoding (التشفير الساخن)](/en/terms/one-hot-encoding-التشفير-الساخن/)
- [Bag of Words (كيس الكلمات)](/en/terms/bag-of-words-كيس-الكلمات/)
- [Dimensionality reduction (اختزال الأبعاد)](/en/terms/dimensionality-reduction-اختزال-الأبعاد/)
- [Sparse matrix (المصفوفة المتفرقة)](/en/terms/sparse-matrix-المصفوفة-المتفرقة/)
