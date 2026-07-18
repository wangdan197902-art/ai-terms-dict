---
title: "Sanapussi-malli"
term_id: "bag_of_words_model"
category: "basic_concepts"
subcategory: ""
tags: ["NLP", "text-processing", "feature-engineering"]
difficulty: 2
weight: 1
slug: "bag_of_words_model"
aliases:
  - /fi/terms/bag_of_words_model/
date: "2026-07-18T15:45:00.616182Z"
lastmod: "2026-07-18T17:15:09.386989Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Sanapussi-malli on tekstin sieventävä esitys, joka kuvaa sanojen esiintymistä dokumentissa jättäen kieliopin ja sanojen järjestyksen huomiotta."
---

## Definition

Tämä luonnollen kielen käsittelyn tekniikka esittää tekstin sanan monijoukkona, sivuuttaen syntaksin ja sekvenssin. Se muuntaa dokumentit numeerisiksi vektoreiksi sanojen taajuuden tai esiintymisen perusteella.

### Summary

Sanapussi-malli on tekstin sieventävä esitys, joka kuvaa sanojen esiintymistä dokumentissa jättäen kieliopin ja sanojen järjestyksen huomiotta.

## Key Concepts

- Tokenisointi
- Taajuuslaskenta
- Vektoritila
- Ominaisuuspoiminta

## Use Cases

- Tekstiluokittelu
- Roskapostin suodatus
- Tietohaku

## Code Example

```python
from sklearn.feature_extraction.text import CountVectorizer
corpus = ["Hello world", "World hello"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
```

## Related Terms

- [TF-IDF (Term Frequency-Inverse Document Frequency)](/en/terms/tf-idf-term-frequency-inverse-document-frequency/)
- [N-grams (N-grammit)](/en/terms/n-grams-n-grammit/)
- [Word Embeddings (Sanavektorit)](/en/terms/word-embeddings-sanavektorit/)
