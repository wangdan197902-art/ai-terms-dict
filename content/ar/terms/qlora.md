---
title: QLoRA
term_id: qlora
category: training_techniques
subcategory: ''
tags:
- Optimization
- Fine-Tuning
- efficiency
difficulty: 4
weight: 1
slug: qlora
date: '2026-07-18T15:38:09.821447Z'
lastmod: '2026-07-18T17:15:08.464699Z'
draft: false
source: agnes_llm
status: published
language: ar
description: التكيف منخفض الرتبة المُكمَّم، وهي طريقة لضبط نماذج اللغات الكبيرة بدقة
  وكفاءة باستخدام التكميم الرباعي البت (4-bit) والمُكيّفات منخفضة الرتبة.
---
## Definition

يجمع QLoRA بين التكيف منخفض الرتبة (LoRA) والتكميم بدقة 4 بت لتقليل البصمة الذاكرة المطلوبة لضبط النماذج الضخمة. من خلال تخزين الأوزان بتنسيق 4 بت وإضافة مُكيّفات صغيرة قابلة للتدريب، يتيح QLoRA ضبط النماذج الكبيرة على أجهزة استهلاكية ذات موارد محدودة دون التضحية بالدقة بشكل كبير.

### Summary

التكيف منخفض الرتبة المُكمَّم، وهي طريقة لضبط نماذج اللغات الكبيرة بدقة وكفاءة باستخدام التكميم الرباعي البت (4-bit) والمُكيّفات منخفضة الرتبة.

## Key Concepts

- التكيف منخفض الرتبة
- التكميم بدقة 4 بت
- كفاءة الذاكرة
- الضبط الدقيق

## Use Cases

- الضبط الدقيق على وحدات معالجة الرسومات الاستهلاكية
- البيئات المقيدة الموارد
- التكرار السريع للنماذج

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32, target_modules=["q_proj", "v_proj"])
model = get_peft_model(base_model, config)
```

## Related Terms

- [LoRA](/en/terms/lora/)
- [PEFT](/en/terms/peft/)
- [التكميم (Quantization)](/en/terms/التكميم-quantization/)
- [الضبط الدقيق الفعال للمعاملات (Parameter-Efficient Fine-Tuning)](/en/terms/الضبط-الدقيق-الفعال-للمعاملات-parameter-efficient-fine-tuning/)
