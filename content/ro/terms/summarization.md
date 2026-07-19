---
title: Rezumat (Sumarizare)
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
date: '2026-07-18T15:38:35.785302Z'
lastmod: '2026-07-18T17:15:09.619177Z'
draft: false
source: agnes_llm
status: published
language: ro
description: O sarcină de Procesare a Limbajului Natural (NLP) care generează un rezumat
  concis și coerent al unui text mai lung, păstrându-i informațiile cheie.
---
## Definition

Rezumatul textual reduce volumele mari de text în versiuni mai scurte fără a pierde sensul critic. Poate fi extractivă, selectând propoziții importante din sursă, sau abstractivă, generând texte noi.

### Summary

O sarcină de Procesare a Limbajului Natural (NLP) care generează un rezumat concis și coerent al unui text mai lung, păstrându-i informațiile cheie.

## Key Concepts

- Rezumat extractiv
- Rezumat abstractiv
- Densitate informațională
- Coerență

## Use Cases

- Condensarea articolelor de știri
- Generarea proceselor-verbale de ședințe
- Revizuirea documentelor juridice

## Code Example

```python
from transformers import pipeline
summarizer = pipeline("summarization")
result = summarizer("AI is transforming industries...", max_length=50, min_length=10)[0]['summary_text']
```

## Related Terms

- [Procesarea limbajului natural (NLP)](/en/terms/procesarea-limbajului-natural-nlp/)
- [Modele Transformer](/en/terms/modele-transformer/)
- [BERT](/en/terms/bert/)
- [T5](/en/terms/t5/)
