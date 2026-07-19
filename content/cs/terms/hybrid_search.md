---
title: Hybridní vyhledávání
term_id: hybrid_search
category: application_paradigms
subcategory: ''
tags:
- retrieval
- Search Engine
- rag
difficulty: 3
weight: 1
slug: hybrid_search
date: '2026-07-18T16:01:49.408406Z'
lastmod: '2026-07-18T17:15:09.139761Z'
draft: false
source: agnes_llm
status: published
language: cs
description: Strategie vyhledávání, která kombinuje sémantické vyhledávání pomocí
  vektorů s tradičním indexováním založeným na klíčových slovech, aby se zlepšila
  přesnost a relevance výsledků.
---
## Definition

Hybridní vyhledávání integruje dva odlišné metody vyhledávání: husté vektorové vyhledávání, které zachycuje sémantický význam a kontext, a řídké vektorové (klíčová slova) vyhledávání, které odpovídá přesným termínům. Využíváním obou přístupů dosahuje systém vyšší kvality výsledků než při použití pouze jedné z metod.

### Summary

Strategie vyhledávání, která kombinuje sémantické vyhledávání pomocí vektorů s tradičním indexováním založeným na klíčových slovech, aby se zlepšila přesnost a relevance výsledků.

## Key Concepts

- Vektorové vyhledávání
- Shoda klíčových slov
- Přehodnocování pořadí (Reranking)
- Reciproké fúze pořadí (Reciprocal Rank Fusion)

## Use Cases

- Vyhledávání v podnikových dokumentech
- Vyhledávání produktů v e-commerce
- Pokročilé pipeline pro RAG (Retrieval-Augmented Generation)

## Related Terms

- [semantic_search (sémantické vyhledávání)](/en/terms/semantic_search-sémantické-vyhledávání/)
- [sparse_vectors (řídké vektory)](/en/terms/sparse_vectors-řídké-vektory/)
- [dense_vectors (husté vektory)](/en/terms/dense_vectors-husté-vektory/)
- [vector_database (vektorová databáze)](/en/terms/vector_database-vektorová-databáze/)
