---
title: "ערבוב מומחים"
term_id: "moe"
category: "basic_concepts"
subcategory: ""
tags: ["Architecture", "Efficiency", "LLMs"]
difficulty: 4
weight: 1
slug: "moe"
aliases:
  - /he/terms/moe/
date: "2026-07-18T16:13:12.225021Z"
lastmod: "2026-07-18T17:15:09.565821Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "תבנית ארכיטקטורה שבה מספר רשתות עצביות מומחות (מומחים) משולבות באמצעות מנגנון הפעלה (Gating) לעיבוד קלט."
---

## Definition

ערבוב מומחים (MoE) היא ארכיטקטורת למידת מכונה המיועדת לשפר יעילות ונדידות. במקום להשתמש במודל גדול אחד לכל המשימות, MoE משתמש במספר מודלים קטנים יותר ('מומחים') שנבחרים בהתאם לקלט הספציפי.

### Summary

תבנית ארכיטקטורה שבה מספר רשתות עצביות מומחות (מומחים) משולבות באמצעות מנגנון הפעלה (Gating) לעיבוד קלט.

## Key Concepts

- הפעלה דלילה
- רשת הפעלה (Gating Network)
- התמחות של מומחים
- נדידות (Scalability)

## Use Cases

- אימון יעיל של מודלי שפה גדולים
- הפחתת זמן השהייה (Latency) בחישוב עבור מודלים ענקיים
- טיפול בסוגי קלט מגוונים במערכות רב-מודאליות

## Related Terms

- [Sparse Transformers (טרנספורמרים דלילים)](/en/terms/sparse-transformers-טרנספורמרים-דלילים/)
- [Conditional Computation (חישוב תנאי)](/en/terms/conditional-computation-חישוב-תנאי/)
- [Large Language Models (מודלי שפה גדולים)](/en/terms/large-language-models-מודלי-שפה-גדולים/)
- [Neural Architecture Search (חיפוש ארכיטקטורת עצבית)](/en/terms/neural-architecture-search-חיפוש-ארכיטקטורת-עצבית/)
