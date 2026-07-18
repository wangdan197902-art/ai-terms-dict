---
title: "נתוני שמירה (Held-out)"
term_id: "held_out"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "data_splitting", "validation"]
difficulty: 2
weight: 1
slug: "held_out"
aliases:
  - /he/terms/held_out/
date: "2026-07-18T15:32:53.102643Z"
lastmod: "2026-07-18T17:15:09.492451Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "מדגמי נתונים ששמורים מחוץ לערכת האימון כדי להעריך את ביצועי המודל ולמנוע התאמה יתר (Overfitting) במהלך הפיתוח."
---

## Definition

ערכת נתונים 'held-out' (שמורה) מורכבת מדוגמאות שהוצאו בכוונה מתהליך האימון של מודל למידת מכונה. תת-קבוצה זו משמשת להערכת יכולת הכללה של המודל לנתונים שלא ראה בעבר, ומספקת הערכה אובייקטיבית יותר של הביצועים בהשוואה לשימוש באותם נתונים לאימון.

### Summary

מדגמי נתונים ששמורים מחוץ לערכת האימון כדי להעריך את ביצועי המודל ולמנוע התאמה יתר (Overfitting) במהלך הפיתוח.

## Key Concepts

- כלליות (Generalization)
- התאמה יתר (Overfitting)
- ערכת אימות (Validation set)
- הערכה חסרת הטיה

## Use Cases

- כוונון היפר-פרמטרים
- השוואה בין ארכיטקטורות מודל שונות
- הערכת ביצועים סופית לפני הפעלה בסביבת ייצור

## Related Terms

- [training_set (ערכת אימון)](/en/terms/training_set-ערכת-אימון/)
- [test_set (ערכת בדיקה)](/en/terms/test_set-ערכת-בדיקה/)
- [cross_validation (אימות צולב)](/en/terms/cross_validation-אימות-צולב/)
- [generalization (כלליות)](/en/terms/generalization-כלליות/)
