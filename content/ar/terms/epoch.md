---
title: "حقبة تدريبية"
term_id: "epoch"
category: "training_techniques"
subcategory: ""
tags: ["training", "neural_networks", "basics"]
difficulty: 2
weight: 1
slug: "epoch"
aliases:
  - /ar/terms/epoch/
date: "2026-07-18T15:56:49.835934Z"
lastmod: "2026-07-18T17:15:08.501951Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "مرور كامل واحد لمجموعة بيانات التدريب عبر خوارزمية تعلم الآلة أثناء تدريب النموذج."
---

## Definition

في تعلم الآلة، تمثل الحقبة التدريبية تكراراً واحداً عبر مجموعة بيانات التدريب بأكملها. خلال كل حقبة، يعالج النموذج جميع أمثلة التدريب، ويحدث أوزانه عبر الانتشار العكسي، ويقيّم الأداء.

### Summary

مرور كامل واحد لمجموعة بيانات التدريب عبر خوارزمية تعلم الآلة أثناء تدريب النموذج.

## Key Concepts

- تكرار التدريب
- الانتشار العكسي
- الاقتراب من الحل الأمثل
- ضبط المعاملات الفائقة

## Use Cases

- تكوين حلقات تدريب الشبكات العصبية
- مراقبة فقدان التحقق من الصحة لكل دورة
- تنفيذ استراتيجيات الإيقاف المبكر

## Code Example

```python
for epoch in range(num_epochs):
    for inputs, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
```

## Related Terms

- [حجم الدفعة (Batch Size)](/en/terms/حجم-الدفعة-batch-size/)
- [تكرار (Iteration)](/en/terms/تكرار-iteration/)
- [معدل التعلم (Learning Rate)](/en/terms/معدل-التعلم-learning-rate/)
- [الإفراط في التخصيص (Overfitting)](/en/terms/الإفراط-في-التخصيص-overfitting/)
