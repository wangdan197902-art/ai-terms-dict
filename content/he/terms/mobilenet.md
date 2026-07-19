---
title: "MobileNet"
term_id: "mobilenet"
category: "basic_concepts"
subcategory: ""
tags: ["CNN", "Optimization", "Mobile AI"]
difficulty: 2
weight: 1
slug: "mobilenet"
date: "2026-07-18T16:12:55.323559Z"
lastmod: "2026-07-18T17:15:09.565069Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "MobileNet היא משפחה של רשתות נוירונים עמוקות קלות משקל, המיועדות ליישומי ראייה במכשירים ניידים ובמערכות משובצות."
---
## Definition

רשתות MobileNet משתמשות בהטלות ספרביליות עומק (depthwise separable convolutions) כדי להפחית דרמטית את העלות החישובית ואת גודל המודל בהשוואה להטלות סטנדרטיות. ארכיטקטורה זו מאפשרת חילוץ תכונות יעיל על

### Summary

MobileNet היא משפחה של רשתות נוירונים עמוקות קלות משקל, המיועדות ליישומי ראייה במכשירים ניידים ובמערכות משובצות.

## Key Concepts

- הטלות ספרביליות עומק
- יעילות מודל
- חישוב בקצה (Edge Computing)
- למידה בהעברה (Transfer Learning)

## Use Cases

- זיהוי עצמים בזמן אמת בסמארטפונים
- מיון תמונות במכשירי IoT
- זיהוי פנים באפליקציות ניידות

## Code Example

```python
from tensorflow.keras.applications import MobileNetV2
model = MobileNetV2(weights='imagenet', input_shape=(224, 224, 3))
```

## Related Terms

- [ShuffleNet (רשת נוירונים קלה)](/en/terms/shufflenet-רשת-נוירונים-קלה/)
- [SqueezeNet (מודל קומפקטי)](/en/terms/squeezenet-מודל-קומפקטי/)
- [EfficientNet (ארכיטקטורה יעילה)](/en/terms/efficientnet-ארכיטקטורה-יעילה/)
- [Convolutional Neural Network (רשת נוירונים קונוולוציונית)](/en/terms/convolutional-neural-network-רשת-נוירונים-קונוולוציונית/)
