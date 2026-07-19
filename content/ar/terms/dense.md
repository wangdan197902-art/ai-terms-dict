---
title: كثيف
term_id: dense
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
difficulty: 2
weight: 1
slug: dense
date: '2026-07-18T15:53:34.133840Z'
lastmod: '2026-07-18T17:15:08.495819Z'
draft: false
source: agnes_llm
status: published
language: ar
description: طبقة أو موتر تكون فيه كل عنصر متصلاً بكل عنصر في الطبقة أو البعد السابق.
---
## Definition

في الشبكات العصبية، يشير مصطلح 'كثيف' إلى الطبقات المتصلة بالكامل حيث يتلقى كل عصبون مدخلات من جميع العصبيونات في الطبقة السابقة. وهذا يتناقض مع الاتصالات المتفرقة الموجودة في الشبكات التلافيفية أو...

### Summary

طبقة أو موتر تكون فيه كل عنصر متصلاً بكل عنصر في الطبقة أو البعد السابق.

## Key Concepts

- متصل بالكامل
- مصفوفة الأوزان
- دالة التنشيط
- دمج الميزات

## Use Cases

- طبقات التصنيف النهائية في الشبكات العصبية متعددة الطبقات (MLPs)
- دمج الميزات في النماذج الهجينة
- مهام الانحدار البسيطة

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neural Network (شبكة عصبية أمامية)](/en/terms/feedforward-neural-network-شبكة-عصبية-أمامية/)
- [Backpropagation (الانتشار العكسي)](/en/terms/backpropagation-الانتشار-العكسي/)
- [ReLU (دالة الوحدة الخطية المصححة)](/en/terms/relu-دالة-الوحدة-الخطية-المصححة/)
- [Bias Term (حد التحيز)](/en/terms/bias-term-حد-التحيز/)
