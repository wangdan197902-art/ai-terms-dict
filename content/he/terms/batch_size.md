---
title: "גודל אצווה"
term_id: "batch_size"
category: "training_techniques"
subcategory: ""
tags: ["hyperparameters", "optimization", "memory"]
difficulty: 2
weight: 1
slug: "batch_size"
aliases:
  - /he/terms/batch_size/
date: "2026-07-18T15:46:08.202392Z"
lastmod: "2026-07-18T17:15:09.516314Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "מספר דוגמאות האימון המנוצלות באיטרציה אחת של אלגוריתם ירידת המדרג הסטוכסטית."
---

## Definition

גודל האצווה הוא היפר-פרמטר קריטי הקובע כמה דגימות מעובדות לפני עדכון הפרמטרים הפנימיים של המודל. גודל אצווה גדול יותר מספק הערכה מדויקת יותר של ה-

### Summary

מספר דוגמאות האימון המנוצלות באיטרציה אחת של אלגוריתם ירידת המדרג הסטוכסטית.

## Key Concepts

- הערכת מדרג (Gradient)
- אילוצי זיכרון
- יציבות התכנסות
- כוונון היפר-פרמטרים

## Use Cases

- כוונון מהירות ההתכנסות של המודל
- ניהול מגבלות זיכרון GPU במהלך האימון
- שיפור הכללה באמצעות מדרגים רועשים

## Related Terms

- [learning_rate (קצב למידה)](/en/terms/learning_rate-קצב-למידה/)
- [stochastic_gradient_descent (ירידת מדרג סטוכסטית)](/en/terms/stochastic_gradient_descent-ירידת-מדרג-סטוכסטית/)
- [mini_batch (אצווה מינימלית)](/en/terms/mini_batch-אצווה-מינימלית/)
- [memory_usage (שימוש בזיכרון)](/en/terms/memory_usage-שימוש-בזיכרון/)
