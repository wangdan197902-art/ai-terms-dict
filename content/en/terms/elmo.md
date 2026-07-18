---
title: "ELMo"
term_id: "elmo"
category: "basic_concepts"
subcategory: ""
tags: ["NLP", "Embeddings", "History"]
difficulty: 3
weight: 1
slug: "elmo"
aliases:
  - /en/terms/elmo/
date: "2026-07-18T09:56:08.548985Z"
lastmod: "2026-07-18T11:44:44.667475Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Embeddings from Language Models, a deep contextualized word representation method using bidirectional LSTMs."
---

## Definition

ELMo generates context-sensitive word embeddings by processing input text through a bidirectional LSTM trained on a large corpus. Unlike static embeddings like Word2Vec, ELMo captures polysemy by producing different vector representations for the same word depending on its surrounding context. This approach significantly improved performance on various NLP benchmarks by allowing downstream tasks to leverage rich, dynamic linguistic features extracted from pre-trained language models.

### Summary

Embeddings from Language Models, a deep contextualized word representation method using bidirectional LSTMs.

## Key Concepts

- Contextual Embeddings
- Bidirectional LSTM
- Pre-training
- Polysemy

## Use Cases

- Sentiment analysis
- Named entity recognition
- Coreference resolution

## Related Terms

- [Word2Vec](/en/terms/word2vec/)
- [BERT](/en/terms/bert/)
- [Transformer](/en/terms/transformer/)
- [Language Modeling](/en/terms/language-modeling/)
