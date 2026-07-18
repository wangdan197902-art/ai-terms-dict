---
title: "מגבלת טוקנים"
term_id: "token_limit"
category: "engineering_practice"
subcategory: ""
tags: ["LLM", "constraints", "architecture"]
difficulty: 2
weight: 1
slug: "token_limit"
aliases:
  - /he/terms/token_limit/
date: "2026-07-18T15:39:03.552324Z"
lastmod: "2026-07-18T17:15:09.505127Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "המספר המקסימלי של טוקנים שמודל בינה מלאכותית יכול לעבד ברצף קלט או פלט בודד."
---

## Definition

מגבלת הטוקנים מגדירה את אילוץ גודל חלון ההקשר עבור מודלי שפה גדולים (LLMs), ומגבילה את כמות הטקסט שניתחת או תיוצר בו זמנית. גבול ארכיטקטוני זה משפיע על ניהול הזיכרון, יעילות החישוב ועל הצורך לפרוס מסמכים ארוכים לחלקים קטנים יותר כדי להתאים למגבלות המודל.

### Summary

המספר המקסימלי של טוקנים שמודל בינה מלאכותית יכול לעבד ברצף קלט או פלט בודד.

## Key Concepts

- חלון הקשר
- קיצוץ (Truncation)
- נדפיק הנדסה (Prompt Engineering)
- ניהול זיכרון

## Use Cases

- עיצוב מערכות RAG (חיזוק יצירה באמצעות החזרה)
- אופטימיזציה של אורך הפקודה (Prompt)
- עיבוד מסמכים ארוכים

## Related Terms

- [context_window (חלון הקשר)](/en/terms/context_window-חלון-הקשר/)
- [embedding (הטמעה וקטורית)](/en/terms/embedding-הטמעה-וקטורית/)
- [chunking (חיתוך נתונים לחלקים)](/en/terms/chunking-חיתוך-נתונים-לחלקים/)
- [prompt_tuning (כוונון פקודות)](/en/terms/prompt_tuning-כוונון-פקודות/)
