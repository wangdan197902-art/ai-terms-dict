---
title: "BPE"
term_id: "bpe"
category: "engineering_practice"
subcategory: ""
tags: ["NLP", "Tokenization", "Data Preprocessing"]
difficulty: 3
weight: 1
slug: "bpe"
date: "2026-07-18T10:57:35.607269Z"
lastmod: "2026-07-18T11:44:44.892817Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Byte Pair Encoding ist ein Algorithmus zur Subwort-Tokenisierung, der wiederholt die häufigsten Zeichenpaare zusammenführt, um einen Wortschatz aufzubauen."
---
## Definition

Byte Pair Encoding (BPE) ist eine Datenkomprimierungstechnik, die für die Verarbeitung natürlicher Sprache adaptiert wurde, um mit Wörtern außerhalb des Wortschatzes (Out-of-Vocabulary) umzugehen. Es beginnt mit einem Wortschatz aus einzelnen Zeichen und führt wiederholt

### Summary

Byte Pair Encoding ist ein Algorithmus zur Subwort-Tokenisierung, der wiederholt die häufigsten Zeichenpaare zusammenführt, um einen Wortschatz aufzubauen.

## Key Concepts

- Subwort-Tokenisierung
- Wortschatz-Zusammenführung
- Häufigkeitsanalyse
- Umgang mit Out-of-Vocabulary-Wörtern

## Use Cases

- Vorverarbeitung von Texten für Large Language Models
- Umgang mit morphologisch reichen Sprachen
- Reduzierung der Wortschatzgröße in neuronalen Netzen

## Code Example

```python
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode("unhappiness")
print(tokens)
```

## Related Terms

- [WordPiece (ähnliches Tokenisierungsverfahren)](/en/terms/wordpiece-ähnliches-tokenisierungsverfahren/)
- [SentencePiece (unabhängiges Tokenisierungstool)](/en/terms/sentencepiece-unabhängiges-tokenisierungstool/)
- [Tokenisierung (Zerlegung von Text in Einheiten)](/en/terms/tokenisierung-zerlegung-von-text-in-einheiten/)
- [Subword-Einheiten (Wortbestandteile)](/en/terms/subword-einheiten-wortbestandteile/)
