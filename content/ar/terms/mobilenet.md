---
title: "موبايل نت"
term_id: "mobilenet"
category: "basic_concepts"
subcategory: ""
tags: ["CNN", "Optimization", "Mobile AI"]
difficulty: 2
weight: 1
slug: "mobilenet"
aliases:
  - /ar/terms/mobilenet/
date: "2026-07-18T16:13:21.574551Z"
lastmod: "2026-07-18T17:15:08.528845Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "موبايل نت هو عائلة من الشبكات العصبية العميقة خفيفة الوزن، مصممة لتطبيقات الرؤية على الأجهزة المحمولة والمدمجة."
---

## Definition

تستخدم شبكات موبايل نت الالتواءات القابلة للفصل العمقي لتقليل التكلفة الحسابية وحجم النموذج بشكل كبير مقارنة بالالتواءات القياسية. يتيح هذا الهيكل استخراج الميزات بكفاءة على

### Summary

موبايل نت هو عائلة من الشبكات العصبية العميقة خفيفة الوزن، مصممة لتطبيقات الرؤية على الأجهزة المحمولة والمدمجة.

## Key Concepts

- الالتواءات القابلة للفصل العمقي
- كفاءة النموذج
- الحوسبة الطرفية
- التعلم بالنقل

## Use Cases

- كشف الأشياء في الوقت الفعلي على الهواتف الذكية
- تصنيف الصور على أجهزة إنترنت الأشياء
- التعرف على الوجه في تطبيقات الهاتف المحمول

## Code Example

```python
from tensorflow.keras.applications import MobileNetV2
model = MobileNetV2(weights='imagenet', input_shape=(224, 224, 3))
```

## Related Terms

- [ShuffleNet (شوفل نت)](/en/terms/shufflenet-شوفل-نت/)
- [SqueezeNet (سكوييز نت)](/en/terms/squeezenet-سكوييز-نت/)
- [EfficientNet (إفيشنت نت)](/en/terms/efficientnet-إفيشنت-نت/)
- [Convolutional Neural Network (الشبكة العصبية الالتوائية)](/en/terms/convolutional-neural-network-الشبكة-العصبية-الالتوائية/)
