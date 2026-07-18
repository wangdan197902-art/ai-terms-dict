---
title: "Modelul Bag-of-Words"
term_id: "bag_of_words_model"
category: "basic_concepts"
subcategory: ""
tags: ["NLP", "text-processing", "feature-engineering"]
difficulty: 2
weight: 1
slug: "bag_of_words_model"
aliases:
  - /ro/terms/bag_of_words_model/
date: "2026-07-18T15:46:51.194570Z"
lastmod: "2026-07-18T17:15:09.631868Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "Modelul Bag-of-Words este o reprezentare simplificatoare a textului care descrie apariția cuvintelor într-un document, ignorând gramatica și ordinea cuvintelor."
---

## Definition

Această tehnică de procesare a limbajului natural reprezintă textul ca un multiset de cuvinte, ignorând sintaxa și secvența. Converteste documentele în vectori numerici pe baza frecvenței sau prezenței cuvintelor. Cuv...

### Summary

Modelul Bag-of-Words este o reprezentare simplificatoare a textului care descrie apariția cuvintelor într-un document, ignorând gramatica și ordinea cuvintelor.

## Key Concepts

- Tokenizare
- Numărarea frecvenței
- Spațiu vectorial
- Extragerea caracteristicilor

## Use Cases

- Clasificarea textului
- Filtrarea spam-ului
- Recuperarea informațiilor

## Code Example

```python
from sklearn.feature_extraction.text import CountVectorizer
corpus = ["Hello world", "World hello"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
```

## Related Terms

- [TF-IDF (Term Frequency-Inverse Document Frequency)](/en/terms/tf-idf-term-frequency-inverse-document-frequency/)
- [N-grams (N-grame)](/en/terms/n-grams-n-grame/)
- [Word Embeddings (Încorporări de cuvinte)](/en/terms/word-embeddings-încorporări-de-cuvinte/)
