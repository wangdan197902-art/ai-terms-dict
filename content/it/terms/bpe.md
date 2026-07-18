---
title: "BPE"
term_id: "bpe"
category: "engineering_practice"
subcategory: ""
tags: ["NLP", "Tokenization", "Data Preprocessing"]
difficulty: 3
weight: 1
slug: "bpe"
aliases:
  - /it/terms/bpe/
date: "2026-07-18T15:34:52.481551Z"
lastmod: "2026-07-18T17:15:08.583473Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "L'encoding a coppie di byte (BPE) è un algoritmo utilizzato per la tokenizzazione sub-parola che fonde iterativamente le coppie di caratteri più frequenti per costruire un vocabolario."
---

## Definition

L'encoding a coppie di byte (BPE) è una tecnica di compressione dei dati adattata all'elaborazione del linguaggio naturale per gestire le parole fuori dal vocabolario. Parte da un vocabolario di singoli caratteri e fonde iterativamente

### Summary

L'encoding a coppie di byte (BPE) è un algoritmo utilizzato per la tokenizzazione sub-parola che fonde iterativamente le coppie di caratteri più frequenti per costruire un vocabolario.

## Key Concepts

- Tokenizzazione sub-parola
- Unione del vocabolario
- Analisi della frequenza
- Gestione delle parole fuori dal vocabolario

## Use Cases

- Preprocessing del testo per i modelli linguistici di grandi dimensioni
- Gestione di lingue morfologicamente ricche
- Riduzione delle dimensioni del vocabolario nelle reti neurali

## Code Example

```python
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode("unhappiness")
print(tokens)
```

## Related Terms

- [WordPiece (Metodo di tokenizzazione simile)](/en/terms/wordpiece-metodo-di-tokenizzazione-simile/)
- [SentencePiece (Libreria di tokenizzazione indipendente dalla lingua)](/en/terms/sentencepiece-libreria-di-tokenizzazione-indipendente-dalla-lingua/)
- [Tokenizzazione (Processo di suddivisione del testo)](/en/terms/tokenizzazione-processo-di-suddivisione-del-testo/)
- [Unità sub-parola (Componenti lessicali più piccole della parola)](/en/terms/unità-sub-parola-componenti-lessicali-più-piccole-della-parola/)
