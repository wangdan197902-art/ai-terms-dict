---
title: "البيانات الموسومة"
term_id: "labeled_data"
category: "basic_concepts"
subcategory: ""
tags: ["data", "supervised_learning", "fundamentals"]
difficulty: 1
weight: 1
slug: "labeled_data"
aliases:
  - /ar/terms/labeled_data/
date: "2026-07-18T16:05:20.138241Z"
lastmod: "2026-07-18T17:15:08.520783Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "بيانات يتم فيها توفير المخرجات الصحيحة أو قيمة الهدف جنباً إلى جنب مع ميزات الإدخال."
---

## Definition

تتكون البيانات الموسومة من عينات إدخال مقترنة بتسميات الحقيقة الأساسية المقابلة، مما يشكل الأساس لتعلم الآلة الخاضع للإشراف. تتيح هذه البيانات للخوارزميات تعلم العلاقة بين مدخلات

### Summary

بيانات يتم فيها توفير المخرجات الصحيحة أو قيمة الهدف جنباً إلى جنب مع ميزات الإدخال.

## Key Concepts

- التعلم الخاضع للإشراف
- الحقيقة الأساسية
- التوسيم
- متغير الهدف

## Use Cases

- تدريب مصنّفات الصور
- بناء أنظمة التعرف على الكلام
- النمذجة التنبؤية في مجال التمويل

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (البيانات غير الموسومة)](/en/terms/unlabeled_data-البيانات-غير-الموسومة/)
- [supervised_learning (التعلم الخاضع للإشراف)](/en/terms/supervised_learning-التعلم-الخاضع-للإشراف/)
- [data_annotation (توسيم البيانات)](/en/terms/data_annotation-توسيم-البيانات/)
- [training_set (مجموعة التدريب)](/en/terms/training_set-مجموعة-التدريب/)
