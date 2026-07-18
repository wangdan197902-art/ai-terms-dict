---
title: "דיסטילציה"
term_id: "distillation"
category: "training_techniques"
subcategory: ""
tags: ["optimization", "compression", "model_efficiency"]
difficulty: 3
weight: 1
slug: "distillation"
aliases:
  - /he/terms/distillation/
date: "2026-07-18T15:24:35.980260Z"
lastmod: "2026-07-18T17:15:09.475424Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "דיסטילציה של ידע היא טכניקה לדחיסת מודל שבה מודל סטודנט קטן לומד לחקות את התנהגותו של מודל מורה גדול יותר."
---

## Definition

תהליך זה כולל העברת ידע מרשת נוירונים מורכבת ובעלת ביצועים גבוהים ('מורה') לרשת פשוטה ויעילה יותר ('סטודנט'). הסטודנט לומד לא רק מתוויות קשות אלא גם מההסתברויות הרכות המופקות על ידי המורה.

### Summary

דיסטילציה של ידע היא טכניקה לדחיסת מודל שבה מודל סטודנט קטן לומד לחקות את התנהגותו של מודל מורה גדול יותר.

## Key Concepts

- ארכיטקטורת מורה-סטודנט
- מטרות רכות (Soft Targets)
- דחיסת מודל
- יעילות מסקנות (Inference)

## Use Cases

- הטמעת מודלי שפה גדולים במכשירים ניידים
- הפחתת זמן השהייה (Latency) ביישומי ראייה ממוחשבת בזמן אמת
- אופטימיזציה של מודלי למידה עמוקה לסביבות חישוב בקצה (Edge Computing)

## Related Terms

- [Quantization (כמותיות/קוונטיזציה)](/en/terms/quantization-כמותיות-קוונטיזציה/)
- [Pruning (גיזום)](/en/terms/pruning-גיזום/)
- [Transfer Learning (למידה בהעברה)](/en/terms/transfer-learning-למידה-בהעברה/)
- [Neural Architecture Search (חיפוש ארכיטקטורת נוירונים)](/en/terms/neural-architecture-search-חיפוש-ארכיטקטורת-נוירונים/)
