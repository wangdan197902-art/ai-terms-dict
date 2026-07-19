---
title: "BPE"
term_id: "bpe"
category: "engineering_practice"
subcategory: ""
tags: ["NLP", "Tokenization", "Data Preprocessing"]
difficulty: 3
weight: 1
slug: "bpe"
date: "2026-07-18T14:43:27.836957Z"
lastmod: "2026-07-18T15:51:59.447580Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Codificação por Par de Bytes é um algoritmo usado para tokenização de subpalavras que mescla iterativamente os pares de caracteres mais frequentes para construir um vocabulário."
---
## Definition

A Codificação por Par de Bytes (BPE) é uma técnica de compressão de dados adaptada para processamento de linguagem natural para lidar com palavras fora do vocabulário. Ela começa com um vocabulário de caracteres individuais e mescla...

### Summary

Codificação por Par de Bytes é um algoritmo usado para tokenização de subpalavras que mescla iterativamente os pares de caracteres mais frequentes para construir um vocabulário.

## Key Concepts

- Tokenização de Subpalavras
- Mesclagem de Vocabulário
- Análise de Frequência
- Tratamento de Palavras Fora do Vocabulário

## Use Cases

- Pré-processamento de texto para Grandes Modelos de Linguagem
- Manipulação de idiomas morfologicamente ricos
- Redução do tamanho do vocabulário em redes neurais

## Code Example

```python
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode("unhappiness")
print(tokens)
```

## Related Terms

- [WordPiece](/en/terms/wordpiece/)
- [SentencePiece](/en/terms/sentencepiece/)
- [Tokenization (Tokenização)](/en/terms/tokenization-tokenização/)
- [Subword Units (Unidades de Subpalavra)](/en/terms/subword-units-unidades-de-subpalavra/)
