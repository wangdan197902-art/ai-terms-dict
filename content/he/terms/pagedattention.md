---
title: PagedAttention
term_id: pagedattention
category: training_techniques
subcategory: ''
tags:
- inference
- Optimization
- Memory Management
difficulty: 4
weight: 1
slug: pagedattention
date: '2026-07-18T16:16:02.263967Z'
lastmod: '2026-07-18T17:15:09.571939Z'
draft: false
source: agnes_llm
status: published
language: he
description: PagedAttention הוא אלגוריתם לניהול זיכרון המותאם ממושגי הדפוס של זיכרון
  וירטואלי כדי לייעל את אחסון וגישת ה-KV Cache (מטמון מפתח-ערך) במודלי טרנספורמר.
---
## Definition

PagedAttention היא טכניקה שהוכנסה על ידי פרויקט vLLM כדי לשפר את היעילות של הסקת מסקנות (Inference) במודלי שפה גדולים. היא פותרת את בעיות השבירה (Fragmentation) והעומס בניהול ה-KV Cache, המאפשרות ניצול יעיל יותר של זיכרון ה-GPU.

### Summary

PagedAttention הוא אלגוריתם לניהול זיכרון המותאם ממושגי הדפוס של זיכרון וירטואלי כדי לייעל את אחסון וגישת ה-KV Cache (מטמון מפתח-ערך) במודלי טרנספורמר.

## Key Concepts

- ניהול KV Cache
- שבירת זיכרון
- אופטימיזציית הסקה
- דפוס זיכרון וירטואלי

## Use Cases

- הפעלת LLM עם פלט גבוה (High-throughput serving)
- הפחתת שימוש בזיכרון GPU
- אופטימיזציה של עיבוד אצוות (Batch processing) בסביבת ייצור

## Related Terms

- [vLLM](/en/terms/vllm/)
- [מטמון מפתח-ערך (Key-Value Cache)](/en/terms/מטמון-מפתח-ערך-key-value-cache/)
- [ארכיטקטורת טרנספורמר (Transformer Architecture)](/en/terms/ארכיטקטורת-טרנספורמר-transformer-architecture/)
- [אופטימיזציית זיכרון GPU (GPU Memory Optimization)](/en/terms/אופטימיזציית-זיכרון-gpu-gpu-memory-optimization/)
