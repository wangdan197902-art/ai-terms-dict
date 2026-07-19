---
title: WordPiece
term_id: wordpiece
category: engineering_practice
subcategory: ''
tags:
- NLP
- tokenization
- BERT
difficulty: 3
weight: 1
slug: wordpiece
date: '2026-07-18T11:38:19.941069Z'
lastmod: '2026-07-18T11:44:45.000040Z'
draft: false
source: agnes_llm
status: published
language: de
description: Ein Subwort-Tokenisierungsalgorithmus, der die häufigsten Zeichenpaare
  rekursiv zusammenführt, um Wörter außerhalb des Vokabulars zu behandeln.
---
## Definition

WordPiece ist eine Tokenisierungsmethode, die weit verbreitet in Natural-Language-Processing-Modellen wie BERT und ALBERT eingesetzt wird. Sie zerlegt Wörter in kleinere Subworteinheiten, um morphologische Vielfalt zu bewältigen und das V...

### Summary

Ein Subwort-Tokenisierungsalgorithmus, der die häufigsten Zeichenpaare rekursiv zusammenführt, um Wörter außerhalb des Vokabulars zu behandeln.

## Key Concepts

- Subwort-Tokenisierung
- Erweiterung des Wortschatzes
- Umgang mit Out-of-Vocabulary-Wörtern
- Morphologische Analyse

## Use Cases

- Vorverarbeitung von Text für BERT-Modelle
- Behandlung ressourcenschwacher Sprachen
- Reduzierung der Größe der Einbettungsmatrix

## Code Example

```python
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('unhappiness')
print(tokens)
```

## Related Terms

- [Byte-Pair Encoding (Byte-Paar-Codierung)](/en/terms/byte-pair-encoding-byte-paar-codierung/)
- [SentencePiece (SentencePiece-Bibliothek)](/en/terms/sentencepiece-sentencepiece-bibliothek/)
- [Tokenization (Tokenisierung)](/en/terms/tokenization-tokenisierung/)
- [NLP preprocessing (NLP-Vorverarbeitung)](/en/terms/nlp-preprocessing-nlp-vorverarbeitung/)
