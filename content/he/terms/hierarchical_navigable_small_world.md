---
title: עולם קטן ניווט היררכי
term_id: hierarchical_navigable_small_world
category: basic_concepts
subcategory: ''
tags:
- algorithms
- search
- Data Structures
difficulty: 4
weight: 1
slug: hierarchical_navigable_small_world
date: '2026-07-18T16:04:13.298856Z'
lastmod: '2026-07-18T17:15:09.547531Z'
draft: false
source: agnes_llm
status: published
language: he
description: מבנה נתונים מבוסס גרף המאפשר חיפוש קרובים קרובים משוערים יעיל במרחבים
  רב-ממדיים.
---
## Definition

אלגוריתם העולם הקטן הנavigable ההיררכי (HNSW) בונה גרף רב-שכבתי, שבו כל שכבה מכילה תת-קבוצה של צמתים מהשכבה שמתחתיה. הניווט מתחיל בשכבה העליונה (הדלילה ביותר) ויורד לשכבות עמוקות יותר ככל שהחיפוש מתמקד, מה שמאפשר מציאת שכנים קרובים בזמן לוגריתמי.

### Summary

מבנה נתונים מבוסס גרף המאפשר חיפוש קרובים קרובים משוערים יעיל במרחבים רב-ממדיים.

## Key Concepts

- חיפוש בגרף (Graph Search)
- קרובים קרובים משוערים (Approximate Nearest Neighbor)
- גרף רב-שכבתי (Multi-layer Graph)
- מורכבות לוגריתמית (Logarithmic Complexity)

## Use Cases

- חיפוש וקטורי
- מנועי המלצות
- איחזור תמונות

## Related Terms

- [K-Nearest Neighbors (K שכנים קרובים)](/en/terms/k-nearest-neighbors-k-שכנים-קרובים/)
- [Faiss (ספריית Faiss של פייסבוק)](/en/terms/faiss-ספריית-faiss-של-פייסבוק/)
- [Annoy (ספריית Annoy של ספוטיפיי)](/en/terms/annoy-ספריית-annoy-של-ספוטיפיי/)
