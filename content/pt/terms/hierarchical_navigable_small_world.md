---
title: Mundo pequeno navegável hierárquico
term_id: hierarchical_navigable_small_world
category: basic_concepts
subcategory: ''
tags:
- algorithms
- search
- Data Structures
difficulty: 4
weight: 1
slug: hierarchical_navigable_small_world
date: '2026-07-18T15:04:08.787886Z'
lastmod: '2026-07-18T15:51:59.498238Z'
draft: false
source: agnes_llm
status: published
language: pt
description: Uma estrutura de dados baseada em grafos que permite a busca eficiente
  de vizinhos mais próximos aproximados em espaços de alta dimensão.
---
## Definition

O algoritmo Mundo Pequeno Navegável Hierárquico (HNSW) constrói um grafo multicamadas, onde cada camada contém um subconjunto de nós da camada inferior. A navegação começa na camada superior, movendo-se para camadas inferiores à medida que a proximidade é refinada, permitindo buscas rápidas e escaláveis em grandes conjuntos de dados vetoriais.

### Summary

Uma estrutura de dados baseada em grafos que permite a busca eficiente de vizinhos mais próximos aproximados em espaços de alta dimensão.

## Key Concepts

- Busca em Grafos
- Vizinho Mais Próximo Aproximado
- Grafo Multicamadas
- Complexidade Logarítmica

## Use Cases

- Busca vetorial
- Motores de recomendação
- Recuperação de imagens

## Related Terms

- [K-Vizinhos Mais Próximos (Algoritmo clássico de classificação e clustering)](/en/terms/k-vizinhos-mais-próximos-algoritmo-clássico-de-classificação-e-clustering/)
- [Faiss (Biblioteca da Meta para busca de similaridade vetorial)](/en/terms/faiss-biblioteca-da-meta-para-busca-de-similaridade-vetorial/)
- [Annoy (Biblioteca da Spotify para busca de vizinhos mais próximos aproximados)](/en/terms/annoy-biblioteca-da-spotify-para-busca-de-vizinhos-mais-próximos-aproximados/)
