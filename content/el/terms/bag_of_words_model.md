---
title: "Μοντέλο Σακούλας Λέξεων"
term_id: "bag_of_words_model"
category: "basic_concepts"
subcategory: ""
tags: ["NLP", "text-processing", "feature-engineering"]
difficulty: 2
weight: 1
slug: "bag_of_words_model"
aliases:
  - /el/terms/bag_of_words_model/
date: "2026-07-18T15:52:55.474300Z"
lastmod: "2026-07-18T17:15:09.884147Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Το μοντέλο σακούλας λέξεων είναι μια απλοποιημένη αναπαράσταση κειμένου που περιγράφει τη συχνότητα εμφάνισης των λέξεων σε ένα έγγραφο, αγνοώντας τη γραμματική και τη σειρά των λέξεων."
---

## Definition

Αυτή η τεχνική επεξεργασίας φυσικής γλώσσας αναπαριστά το κείμενο ως ένα πολυσύνολο λέξεων, αδιαφορώντας για τη σύνταξη και τη σειρά. Μετατρέπει τα έγγραφα σε αριθμητικά διανύσματα με βάση τη συχνότητα ή την παρουσία των λέξεων.

### Summary

Το μοντέλο σακούλας λέξεων είναι μια απλοποιημένη αναπαράσταση κειμένου που περιγράφει τη συχνότητα εμφάνισης των λέξεων σε ένα έγγραφο, αγνοώντας τη γραμματική και τη σειρά των λέξεων.

## Key Concepts

- Τοκιοποίηση
- Καταμέτρηση συχνοτήτων
- Χώρος διανυσμάτων
- Εξαγωγή χαρακτηριστικών

## Use Cases

- Ταξινόμηση κειμένου
- Φιλτράρισμα αλληλογραφίας spam
- Ανάκτηση πληροφοριών

## Code Example

```python
from sklearn.feature_extraction.text import CountVectorizer
corpus = ["Hello world", "World hello"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
```

## Related Terms

- [TF-IDF (Βάρος Term-Frequency Inverse Document Frequency)](/en/terms/tf-idf-βάρος-term-frequency-inverse-document-frequency/)
- [N-grams (Ν-γράμματα)](/en/terms/n-grams-ν-γράμματα/)
- [Word Embeddings (Διανυσματικές Αναπαραστάσεις Λέξεων)](/en/terms/word-embeddings-διανυσματικές-αναπαραστάσεις-λέξεων/)
