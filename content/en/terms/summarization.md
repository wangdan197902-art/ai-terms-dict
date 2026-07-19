---
title: Summarization
term_id: summarization
category: application_paradigms
subcategory: ''
tags:
- NLP
- Text Processing
- applications
difficulty: 3
weight: 1
slug: summarization
date: '2026-07-18T09:42:48.759013Z'
lastmod: '2026-07-18T11:44:44.633591Z'
draft: false
source: agnes_llm
status: published
language: en
description: An NLP task that generates a concise and coherent summary of a longer
  text while preserving its key information.
---
## Definition

Text summarization reduces large volumes of text into shorter versions without losing critical meaning. It can be extractive, selecting important sentences from the source, or abstractive, generating new sentences that capture the essence. This technique is crucial for digesting vast amounts of information quickly, aiding users in decision-making and information retrieval across various domains like news, legal documents, and research papers.

### Summary

An NLP task that generates a concise and coherent summary of a longer text while preserving its key information.

## Key Concepts

- Extractive Summarization
- Abstractive Summarization
- Information Density
- Coherence

## Use Cases

- News article condensation
- Meeting notes generation
- Legal document review

## Code Example

```python
from transformers import pipeline
summarizer = pipeline("summarization")
result = summarizer("AI is transforming industries...", max_length=50, min_length=10)[0]['summary_text']
```

## Related Terms

- [NLP](/en/terms/nlp/)
- [Transformer Models](/en/terms/transformer-models/)
- [BERT](/en/terms/bert/)
- [T5](/en/terms/t5/)
