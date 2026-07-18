---
title: "Riassunzione"
term_id: "summarization"
category: "application_paradigms"
subcategory: ""
tags: ["nlp", "text-processing", "applications"]
difficulty: 3
weight: 1
slug: "summarization"
aliases:
  - /it/terms/summarization/
date: "2026-07-18T15:40:54.938652Z"
lastmod: "2026-07-18T17:15:08.590345Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Un compito di NLP che genera un riassunto conciso e coerente di un testo più lungo preservandone le informazioni chiave."
---

## Definition

La riassunzione del testo riduce grandi volumi di testo in versioni più brevi senza perdere il significato critico. Può essere estrattiva, selezionando frasi importanti dalla fonte, o astrattiva, generando nuovo testo.

### Summary

Un compito di NLP che genera un riassunto conciso e coerente di un testo più lungo preservandone le informazioni chiave.

## Key Concepts

- Riassunzione Estrattiva
- Riassunzione Astrattiva
- Densità Informativa
- Coerenza

## Use Cases

- Condensazione di articoli di notizie
- Generazione di verbali di riunione
- Revisione di documenti legali

## Code Example

```python
from transformers import pipeline
summarizer = pipeline("summarization")
result = summarizer("AI is transforming industries...", max_length=50, min_length=10)[0]['summary_text']
```

## Related Terms

- [NLP (elaborazione del linguaggio naturale)](/en/terms/nlp-elaborazione-del-linguaggio-naturale/)
- [Transformer Models (modelli basati su architettura transformer)](/en/terms/transformer-models-modelli-basati-su-architettura-transformer/)
- [BERT (modello linguistico bidirezionale)](/en/terms/bert-modello-linguistico-bidirezionale/)
- [T5 (modello testo-a-testo)](/en/terms/t5-modello-testo-a-testo/)
