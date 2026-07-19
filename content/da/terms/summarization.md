---
title: Tekstsammendrag
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
date: '2026-07-18T15:37:59.426726Z'
lastmod: '2026-07-18T17:15:09.250301Z'
draft: false
source: agnes_llm
status: published
language: da
description: En NLP-opgave, der genererer et koncist og sammenhængende sammendrag
  af en længere tekst, mens de vigtigste oplysninger bevares.
---
## Definition

Tekstsammendrag reducerer store mængder tekst til kortere versioner uden at miste kritisk mening. Det kan være ekstraktivt, hvor vigtige sætninger udvælges fra kildeteksten, eller abstraktivt, hvor ny tekst genereres.

### Summary

En NLP-opgave, der genererer et koncist og sammenhængende sammendrag af en længere tekst, mens de vigtigste oplysninger bevares.

## Key Concepts

- Ekstraktivt sammendrag
- Abstraktivt sammendrag
- Informationsdensitet
- Sammenhæng

## Use Cases

- Kondensering af nyhedsartikler
- Generering af mødereferater
- Gennemgang af juridiske dokumenter

## Code Example

```python
from transformers import pipeline
summarizer = pipeline("summarization")
result = summarizer("AI is transforming industries...", max_length=50, min_length=10)[0]['summary_text']
```

## Related Terms

- [NLP (Natural Language Processing / Behandling af naturligt sprog)](/en/terms/nlp-natural-language-processing-behandling-af-naturligt-sprog/)
- [Transformer Models (transformatormodeller)](/en/terms/transformer-models-transformatormodeller/)
- [BERT (Bidirectional Encoder Representations from Transformers)](/en/terms/bert-bidirectional-encoder-representations-from-transformers/)
- [T5 (Text-to-Text Transfer Transformer)](/en/terms/t5-text-to-text-transfer-transformer/)
