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
date: '2026-07-18T15:15:51.755890Z'
lastmod: '2026-07-18T15:51:59.520756Z'
draft: false
source: agnes_llm
status: published
language: pt
description: PagedAttention é um algoritmo de gerenciamento de memória que adapta
  conceitos de paginação de memória virtual para otimizar o armazenamento e acesso
  aos caches Key-Value (KV) em modelos transformador
---
## Definition

PagedAttention é uma técnica introduzida pelo projeto vLLM para melhorar a eficiência da inferência de Grandes Modelos de Linguagem (LLMs). Ela aborda problemas de fragmentação e sobrecarga no gerenciamento do cache KV, onde...

### Summary

PagedAttention é um algoritmo de gerenciamento de memória que adapta conceitos de paginação de memória virtual para otimizar o armazenamento e acesso aos caches Key-Value (KV) em modelos transformadores.

## Key Concepts

- Gerenciamento de Cache KV
- Fragmentação de Memória
- Otimização de Inferência
- Paginação de Memória Virtual

## Use Cases

- Serviço de LLMs de alta vazão
- Redução do uso de memória GPU
- Otimização do processamento em lote em produção

## Related Terms

- [vLLM (Biblioteca de inferência de LLMs)](/en/terms/vllm-biblioteca-de-inferência-de-llms/)
- [Cache Key-Value (Estrutura de dados usada em atenção)](/en/terms/cache-key-value-estrutura-de-dados-usada-em-atenção/)
- [Arquitetura Transformer (Modelo de rede neural)](/en/terms/arquitetura-transformer-modelo-de-rede-neural/)
- [Otimização de Memória GPU (Melhorias no uso de hardware gráfico)](/en/terms/otimização-de-memória-gpu-melhorias-no-uso-de-hardware-gráfico/)
