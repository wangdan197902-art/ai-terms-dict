---
title: "WordPiece"
term_id: "wordpiece"
category: "engineering_practice"
subcategory: ""
tags: ["nlp", "tokenization", "bert"]
difficulty: 3
weight: 1
slug: "wordpiece"
aliases:
  - /es/terms/wordpiece/
date: "2026-07-18T11:13:45.019638Z"
lastmod: "2026-07-18T11:44:44.866605Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "Un algoritmo de tokenización de subpalabras que fusiona recursivamente los pares de caracteres más frecuentes para manejar palabras fuera del vocabulario."
---

## Definition

WordPiece es un método de tokenización ampliamente utilizado en modelos de procesamiento del lenguaje natural como BERT y ALBERT. Divide las palabras en unidades de subpalabras más pequeñas para gestionar la riqueza morfológica y reducir el tamaño del vocabulario, mejorando así el manejo de palabras desconocidas.

### Summary

Un algoritmo de tokenización de subpalabras que fusiona recursivamente los pares de caracteres más frecuentes para manejar palabras fuera del vocabulario.

## Key Concepts

- Tokenización de subpalabras
- Expansión del vocabulario
- Manejo de palabras fuera de vocabulario (OOV)
- Análisis morfológico

## Use Cases

- Preprocesamiento de texto para modelos BERT
- Manejo de idiomas con pocos recursos
- Reducción del tamaño de la matriz de incrustaciones (embeddings)

## Code Example

```python
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('unhappiness')
print(tokens)
```

## Related Terms

- [Codificación por par de bytes (Byte-Pair Encoding, otro algoritmo similar)](/en/terms/codificación-por-par-de-bytes-byte-pair-encoding-otro-algoritmo-similar/)
- [SentencePiece (Librería que implementa WordPiece y otros métodos)](/en/terms/sentencepiece-librería-que-implementa-wordpiece-y-otros-métodos/)
- [Tokenización (Proceso de dividir texto en unidades)](/en/terms/tokenización-proceso-de-dividir-texto-en-unidades/)
- [Preprocesamiento de PLN (Fase inicial en NLP)](/en/terms/preprocesamiento-de-pln-fase-inicial-en-nlp/)
