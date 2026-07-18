---
title: "Bag-of-Words-Modell"
term_id: "bag_of_words_model"
category: "basic_concepts"
subcategory: ""
tags: ["NLP", "text-processing", "feature-engineering"]
difficulty: 2
weight: 1
slug: "bag_of_words_model"
aliases:
  - /de/terms/bag_of_words_model/
date: "2026-07-18T11:04:31.565011Z"
lastmod: "2026-07-18T11:44:44.913281Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Das Bag-of-Words-Modell ist eine vereinfachende Darstellung von Text, die das Vorkommen von Wörtern in einem Dokument beschreibt, wobei Grammatik und Wortreihenfolge ignoriert werden."
---

## Definition

Diese Technik des Natural Language Processing (NLP) stellt Text als Multiset von Wörtern dar und berücksichtigt dabei Syntax und Sequenz nicht. Sie konvertiert Dokumente in numerische Vektoren basierend auf der Wortfrequenz oder bloßen Präsenz.

### Summary

Das Bag-of-Words-Modell ist eine vereinfachende Darstellung von Text, die das Vorkommen von Wörtern in einem Dokument beschreibt, wobei Grammatik und Wortreihenfolge ignoriert werden.

## Key Concepts

- Tokenisierung
- Häufigkeitszählung
- Vektorraum
- Merkmalsextraktion

## Use Cases

- Textklassifizierung
- Spam-Filterung
- Information Retrieval (Informationsrückgewinnung)

## Code Example

```python
from sklearn.feature_extraction.text import CountVectorizer
corpus = ["Hello world", "World hello"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
```

## Related Terms

- [TF-IDF](/en/terms/tf-idf/)
- [N-Gramme](/en/terms/n-gramme/)
- [Word Embeddings (Wort-Embeddings)](/en/terms/word-embeddings-wort-embeddings/)
