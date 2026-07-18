---
title: "נרמול שכבתי"
term_id: "layer_normalization"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "optimization", "architecture"]
difficulty: 3
weight: 1
slug: "layer_normalization"
aliases:
  - /he/terms/layer_normalization/
date: "2026-07-18T16:09:15.066685Z"
lastmod: "2026-07-18T17:15:09.556877Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "טכניקה המנרמלת את הפעילויות של שכבה ברשת נוירונים לאורך ממד התכונות עבור כל דגימה בנפרד."
---

## Definition

נרמול שכבתי מייצב את האימון על ידי הפחתת ההיסט הקווריאטיבי הפנימי, במיוחד ביעילות בארכיטקטורות רקורסיביות ומתמרות. בניגוד לנרמול אצווה, התלות היא בסטטיסטיקות הדגימה הבודדת ולא באצווה.

### Summary

טכניקה המנרמלת את הפעילויות של שכבה ברשת נוירונים לאורך ממד התכונות עבור כל דגימה בנפרד.

## Key Concepts

- נרמול
- היסט קווריאטיבי פנימי
- מודלי מתמר (Transformer)
- RNNs

## Use Cases

- אימון מודלי מתמר כמו BERT
- ייצוב אימון של RNN/LSTM
- למידה עמוקה עם גודל אצווה קטן

## Code Example

```python
import torch.nn as nn
norm_layer = nn.LayerNorm(normalized_shape=[768])
```

## Related Terms

- [batch_normalization (נרמול אצווה)](/en/terms/batch_normalization-נרמול-אצווה/)
- [transformer (מתמר)](/en/terms/transformer-מתמר/)
- [normalization (נרמול)](/en/terms/normalization-נרמול/)
- [deep_learning (למידה עמוקה)](/en/terms/deep_learning-למידה-עמוקה/)
