---
title: "Tokenisierung"
term_id: "tokenization"
category: "engineering_practice"
subcategory: ""
tags: ["NLP", "preprocessing"]
difficulty: 3
weight: 1
slug: "tokenization"
aliases:
  - /de/terms/tokenization/
date: "2026-07-18T10:54:31.976463Z"
lastmod: "2026-07-18T11:44:44.885700Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Tokenisierung ist der Prozess des Aufteilens von Rohdaten in kleinere Einheiten, sogenannte Tokens, die von maschinellen Lernalgorithmen verarbeitet werden können."
---

## Definition

Tokenisierung ist ein kritischer Vorverarbeitungsschritt in der Natürlichen Sprachverarbeitung (NLP), der unstrukturierten Text in strukturierte Daten umwandelt, die für die Aufnahme durch Modelle geeignet sind. Dabei werden Sätze oder Texte in kleinere Einheiten zerlegt, die vom Modell interpretiert werden können.

### Summary

Tokenisierung ist der Prozess des Aufteilens von Rohdaten in kleinere Einheiten, sogenannte Tokens, die von maschinellen Lernalgorithmen verarbeitet werden können.

## Key Concepts

- Textaufteilung
- Vorverarbeitung
- WordPiece
- Byte-Pair-Encoding

## Use Cases

- Vorbereitung von Datensätzen für das BERT-Training
- Eingabeformatierung für GPT-Modelle
- Datenbereinigung für die Stimmungsanalyse

## Code Example

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('Hello world!')
```

## Related Terms

- [Tokenizer (Tokenisierer)](/en/terms/tokenizer-tokenisierer/)
- [Vocabulary (Wortschatz)](/en/terms/vocabulary-wortschatz/)
- [Embedding (Einbettung)](/en/terms/embedding-einbettung/)
- [Preprocessing (Vorverarbeitung)](/en/terms/preprocessing-vorverarbeitung/)
