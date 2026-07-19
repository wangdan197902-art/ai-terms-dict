---
title: מודל שקית המילים
term_id: bag_of_words_model
category: basic_concepts
subcategory: ''
tags:
- NLP
- Text Processing
- Feature Engineering
difficulty: 2
weight: 1
slug: bag_of_words_model
date: '2026-07-18T15:45:52.895207Z'
lastmod: '2026-07-18T17:15:09.515715Z'
draft: false
source: agnes_llm
status: published
language: he
description: מודל שקית המילים הוא ייצוג מפשט של טקסט המתאר את שכיחות המילים במסמך,
  תוך התעלמות מדקדוק וסדר המילים.
---
## Definition

טכניקה זו בעיבוד שפה טבעית מייצגת טקסט כרב-קבוצה (multiset) של מילים, תוך זניחת תחביר ורצף. היא ממירה מסמכים לוקטורים מספריים על בסיס שכיחות המילים או נוכחותן.

### Summary

מודל שקית המילים הוא ייצוג מפשט של טקסט המתאר את שכיחות המילים במסמך, תוך התעלמות מדקדוק וסדר המילים.

## Key Concepts

- טוקניזציה (פירוק למרכיבים)
- ספירת שכיחויות
- מרחב וקטורי
- חילוץ מאפיינים

## Use Cases

- מיון טקסט
- סינון דואר זבל
- שליפה מידע

## Code Example

```python
from sklearn.feature_extraction.text import CountVectorizer
corpus = ["Hello world", "World hello"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
```

## Related Terms

- [TF-IDF (משקל תדירות-תדירות הפיכה במסמך)](/en/terms/tf-idf-משקל-תדירות-תדירות-הפיכה-במסמך/)
- [N-grams (רצפי n מילים)](/en/terms/n-grams-רצפי-n-מילים/)
- [Word Embeddings (הטמעות מילים)](/en/terms/word-embeddings-הטמעות-מילים/)
