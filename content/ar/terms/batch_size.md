---
title: حجم الدفعة
term_id: batch_size
category: training_techniques
subcategory: ''
tags:
- hyperparameters
- Optimization
- memory
difficulty: 2
weight: 1
slug: batch_size
date: '2026-07-18T15:47:03.311349Z'
lastmod: '2026-07-18T17:15:08.480473Z'
draft: false
source: agnes_llm
status: published
language: ar
description: عدد أمثلة التدريب المستخدمة في تكرار واحد لخوارزمية النزول التدرجي العشوائي.
---
## Definition

يُعد حجم الدفعة معلمة فائقة حاسمة تحدد عدد العينات التي تتم معالجتها قبل تحديث المعلمات الداخلية للنموذج. يوفر حجم الدفعة الأكبر تقديراً أكثر دقة للـ

### Summary

عدد أمثلة التدريب المستخدمة في تكرار واحد لخوارزمية النزول التدرجي العشوائي.

## Key Concepts

- تقدير التدرج
- قيود الذاكرة
- استقرار التقارب
- ضبط المعلمة الفائقة

## Use Cases

- ضبط سرعة تقارب النموذج
- إدارة حدود ذاكرة وحدة معالجة الرسومات أثناء التدريب
- تحسين التعميم عبر التدرجات الضوضائية

## Related Terms

- [learning_rate (معدل التعلم)](/en/terms/learning_rate-معدل-التعلم/)
- [stochastic_gradient_descent (النزول التدرجي العشوائي)](/en/terms/stochastic_gradient_descent-النزول-التدرجي-العشوائي/)
- [mini_batch (دفعة صغيرة)](/en/terms/mini_batch-دفعة-صغيرة/)
- [memory_usage (استخدام الذاكرة)](/en/terms/memory_usage-استخدام-الذاكرة/)
