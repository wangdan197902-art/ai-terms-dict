---
title: PagedAttention
term_id: pagedattention
category: training_techniques
subcategory: ''
tags:
- inference
- Optimization
- Memory Management
difficulty: 4
weight: 1
slug: pagedattention
date: '2026-07-18T16:14:31.748260Z'
lastmod: '2026-07-18T17:15:08.656629Z'
draft: false
source: agnes_llm
status: published
language: it
description: PagedAttention è un algoritmo di gestione della memoria che adatta i
  concetti di paging della memoria virtuale per ottimizzare lo storage e l'accesso
  alle cache Key-Value (KV) nei modelli transformer.
---
## Definition

PagedAttention è una tecnica introdotta dal progetto vLLM per migliorare l'efficienza dell'inferenza dei grandi modelli linguistici. Affronta i problemi di frammentazione e overhead nella gestione della cache KV, consentendo un utilizzo della memoria GPU molto più efficiente rispetto ai metodi tradizionali, supportando così batch di richiesta più grandi e una latenza ridotta.

### Summary

PagedAttention è un algoritmo di gestione della memoria che adatta i concetti di paging della memoria virtuale per ottimizzare lo storage e l'accesso alle cache Key-Value (KV) nei modelli transformer.

## Key Concepts

- Gestione della Cache KV
- Frammentazione della Memoria
- Ottimizzazione dell'Inferenza
- Paging della Memoria Virtuale

## Use Cases

- Servizio di LLM ad alta throughput
- Riduzione dell'utilizzo della memoria GPU
- Ottimizzazione dell'elaborazione batch in produzione

## Related Terms

- [vLLM](/en/terms/vllm/)
- [Cache Key-Value](/en/terms/cache-key-value/)
- [Architettura Transformer](/en/terms/architettura-transformer/)
- [Ottimizzazione della Memoria GPU](/en/terms/ottimizzazione-della-memoria-gpu/)
