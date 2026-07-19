---
title: الشبكة العصبية التلافيفية
term_id: convolutional_neural_network
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- images
- Deep Learning
difficulty: 4
weight: 1
slug: convolutional_neural_network
date: '2026-07-18T15:22:50.269401Z'
lastmod: '2026-07-18T17:15:08.432433Z'
draft: false
source: agnes_llm
status: published
language: ar
description: فئة متخصصة من الشبكات العصبية العميقة تُستخدم أساساً لمعالجة البيانات
  ذات البنية الشبكية، مثل الصور، من خلال تطبيق مرشحات تلافيفية.
---
## Definition

تم تصميم الشبكات العصبية التلافيفية (CNNs) للتعلم التلقائي والتكيفي للتسلسلات الهرمية للميزات من المدخلات البصرية. فهي تستخدم طبقات تلافيفية تطبق مرشحات للكشف عن الأنماط المكانية والميزات المحلية في البيانات.

### Summary

فئة متخصصة من الشبكات العصبية العميقة تُستخدم أساساً لمعالجة البيانات ذات البنية الشبكية، مثل الصور، من خلال تطبيق مرشحات تلافيفية.

## Key Concepts

- الطبقات التلافيفية
- الدمج (Pooling)
- خرائط الميزات
- التسلسل الهرمي المكاني

## Use Cases

- تصنيف الصور
- كشف الأجسام في تدفقات الفيديو
- تشخيص الصور الطبية

## Code Example

```python
import tensorflow as tf
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10)
])
```

## Related Terms

- [Deep Learning (التعلم العميق)](/en/terms/deep-learning-التعلم-العميق/)
- [Computer Vision (الرؤية الحاسوبية)](/en/terms/computer-vision-الرؤية-الحاسوبية/)
- [Backpropagation (الانتشار العكسي)](/en/terms/backpropagation-الانتشار-العكسي/)
- [Neural Network (الشبكة العصبية)](/en/terms/neural-network-الشبكة-العصبية/)
