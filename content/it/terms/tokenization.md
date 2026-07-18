---
title: "Tokenizzazione"
term_id: "tokenization"
category: "engineering_practice"
subcategory: ""
tags: ["NLP", "preprocessing"]
difficulty: 3
weight: 1
slug: "tokenization"
aliases:
  - /it/terms/tokenization/
date: "2026-07-18T15:30:25.030113Z"
lastmod: "2026-07-18T17:15:08.576522Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "La tokenizzazione è il processo di suddivisione del testo grezzo in unità più piccole chiamate token, che possono essere elaborate dagli algoritmi di apprendimento automatico."
---

## Definition

La tokenizzazione è un passaggio critico di pre-elaborazione nell'Elaborazione del Linguaggio Naturale (NLP) che converte il testo non strutturato in dati strutturati adatti all'ingestione da parte dei modelli. Coinvolge la scomposizione di frasi e documenti in componenti più piccoli, gestendo sfide come la gestione di parole sconosciute o la normalizzazione del testo.

### Summary

La tokenizzazione è il processo di suddivisione del testo grezzo in unità più piccole chiamate token, che possono essere elaborate dagli algoritmi di apprendimento automatico.

## Key Concepts

- Divisione del Testo
- Pre-elaborazione
- WordPiece
- Byte-Pair Encoding

## Use Cases

- Preparazione di dataset per l'addestramento di BERT
- Formattazione dell'input per i modelli GPT
- Pulizia dei dati per l'analisi del sentiment

## Code Example

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('Hello world!')
```

## Related Terms

- [Tokenizer (Tokenizzatore)](/en/terms/tokenizer-tokenizzatore/)
- [Vocabulary (Vocabolario)](/en/terms/vocabulary-vocabolario/)
- [Embedding (Vettorizzazione)](/en/terms/embedding-vettorizzazione/)
- [Preprocessing (Pre-elaborazione)](/en/terms/preprocessing-pre-elaborazione/)
