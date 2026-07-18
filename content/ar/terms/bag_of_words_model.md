---
title: "نموذج كيس الكلمات"
term_id: "bag_of_words_model"
category: "basic_concepts"
subcategory: ""
tags: ["NLP", "text-processing", "feature-engineering"]
difficulty: 2
weight: 1
slug: "bag_of_words_model"
aliases:
  - /ar/terms/bag_of_words_model/
date: "2026-07-18T15:46:49.821826Z"
lastmod: "2026-07-18T17:15:08.479877Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "نموذج كيس الكلمات هو تمثيل مبسط للنص يصف تكرار ظهور الكلمات في المستند، متجاهلاً القواعد النحوية وترتيب الكلمات."
---

## Definition

هذه التقنية في معالجة اللغات الطبيعية تمثل النص كمجموعة متعددة من الكلمات، متجاهلة التركيب النحوي والتسلسل. تقوم بتحويل المستندات إلى متجهات رقمية بناءً على تكرار الكلمات أو وجودها فقط.

### Summary

نموذج كيس الكلمات هو تمثيل مبسط للنص يصف تكرار ظهور الكلمات في المستند، متجاهلاً القواعد النحوية وترتيب الكلمات.

## Key Concepts

- تجزئة النص (Tokenization)
- عد التكرارات
- فضاء المتجهات
- استخراج الميزات

## Use Cases

- تصنيف النصوص
- فلترة البريد العشوائي
- استرجاع المعلومات

## Code Example

```python
from sklearn.feature_extraction.text import CountVectorizer
corpus = ["Hello world", "World hello"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
```

## Related Terms

- [TF-IDF](/en/terms/tf-idf/)
- [النماذج n-gram (N-grams)](/en/terms/النماذج-n-gram-n-grams/)
- [تضمين الكلمات (Word Embeddings)](/en/terms/تضمين-الكلمات-word-embeddings/)
