---
title: "קידוד זוגות בתים (BPE)"
term_id: "bpe"
category: "engineering_practice"
subcategory: ""
tags: ["NLP", "Tokenization", "Data Preprocessing"]
difficulty: 3
weight: 1
slug: "bpe"
aliases:
  - /he/terms/bpe/
date: "2026-07-18T15:35:46.694057Z"
lastmod: "2026-07-18T17:15:09.496857Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "קידוד זוגות בתים הוא אלגוריתם המשמש לטוקניזציה של תת-מילים (subword tokenization), הממזג באופן איטרטיבי את זוגות התווים הנפוצים ביותר כדי לבנות אוצר מילים."
---

## Definition

קידוד זוגות בתים (BPE) הוא טכניקת דחיסת נתונים שהותאמה לעיבוד שפה טבעית כדי להתמודד עם מילים שאינן קיימות באוצר המילים הקיים. הוא מתחיל מאוצר מילים המורכב מתווים בודדים ומבצע מיזוגים איטרטיביים של זוגות תווים תכופים.

### Summary

קידוד זוגות בתים הוא אלגוריתם המשמש לטוקניזציה של תת-מילים (subword tokenization), הממזג באופן איטרטיבי את זוגות התווים הנפוצים ביותר כדי לבנות אוצר מילים.

## Key Concepts

- טוקניזציית תת-מילים
- מיזוג אוצר מילים
- ניתוח תדירות
- טיפול במילים חוץ-אוצר מילים

## Use Cases

- עיבוד מקדים של טקסט למודלי שפה גדולים
- טיפול בשפות עשירות במורפולוגיה
- הקטנת גודל אוצר המילים ברשתות נוירונים

## Code Example

```python
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode("unhappiness")
print(tokens)
```

## Related Terms

- [WordPiece (שיטת טוקניזציה דומה)](/en/terms/wordpiece-שיטת-טוקניזציה-דומה/)
- [SentencePiece (ספריית טוקניזציה)](/en/terms/sentencepiece-ספריית-טוקניזציה/)
- [טוקניזציה (תהליך פיצול טקסט)](/en/terms/טוקניזציה-תהליך-פיצול-טקסט/)
- [יחידות תת-מילים](/en/terms/יחידות-תת-מילים/)
