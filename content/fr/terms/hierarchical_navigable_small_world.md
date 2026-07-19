---
title: Petit monde navigable hiérarchique
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
date: '2026-07-18T11:22:13.817430Z'
lastmod: '2026-07-18T11:44:45.270556Z'
draft: false
source: agnes_llm
status: published
language: fr
description: Une structure de données basée sur un graphe permettant une recherche
  efficace de voisins approximatifs dans des espaces de grande dimension.
---
## Definition

L'algorithme du petit monde navigable hiérarchique (HNSW) construit un graphe multicouche où chaque couche contient un sous-ensemble de nœuds de la couche inférieure. La navigation commence à la couche supérieure pour un parcours rapide à travers le graphe, puis descend vers les couches inférieures pour affiner la recherche locale, permettant ainsi une recherche de voisins les plus proches approximative avec une complexité logarithmique.

### Summary

Une structure de données basée sur un graphe permettant une recherche efficace de voisins approximatifs dans des espaces de grande dimension.

## Key Concepts

- Recherche dans les graphes
- Voisin le plus proche approximatif
- Graphe multicouche
- Complexité logarithmique

## Use Cases

- Recherche vectorielle
- Moteurs de recommandation
- Récupération d'images

## Related Terms

- [K plus proches voisins (Algorithme de classification basé sur la proximité)](/en/terms/k-plus-proches-voisins-algorithme-de-classification-basé-sur-la-proximité/)
- [Faiss (Bibliothèque de similarité dense et de clustering)](/en/terms/faiss-bibliothèque-de-similarité-dense-et-de-clustering/)
- [Annoy (Bibliothèque de recherche de voisins approximatifs d'Apple)](/en/terms/annoy-bibliothèque-de-recherche-de-voisins-approximatifs-d-apple/)
