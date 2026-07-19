---
title: Lifelong Planning A*
term_id: lifelong_planning_a
category: application_paradigms
subcategory: ''
tags:
- algorithms
- robotics
- Graph Theory
difficulty: 4
weight: 1
slug: lifelong_planning_a
date: '2026-07-18T11:25:42.850228Z'
lastmod: '2026-07-18T11:44:45.284760Z'
draft: false
source: agnes_llm
status: published
language: fr
description: Un algorithme de recherche de chemin incrémental qui met à jour efficacement
  les chemins les plus courts dans des graphes dynamiques sans recalculer depuis zéro
  après des modifications des poids des a
---
## Definition

Lifelong Planning A* (LPA*) est une extension de l'algorithme de recherche A* conçue pour les environnements où les coûts changent avec le temps. Au lieu de redémarrer la recherche, LPA* maintient une file de priorité et met à jour les coûts de manière incrémentale, optimisant ainsi l'efficacité dans les scénarios dynamiques.

### Summary

Un algorithme de recherche de chemin incrémental qui met à jour efficacement les chemins les plus courts dans des graphes dynamiques sans recalculer depuis zéro après des modifications des poids des arêtes.

## Key Concepts

- Recherche incrémentale
- Recherche de chemin
- Graphes dynamiques
- Navigation robotique

## Use Cases

- Routage des véhicules autonomes dans le trafic
- Navigation des robots dans des entrepôts changeants
- Mouvement de l'IA dans les jeux de stratégie en temps réel

## Related Terms

- [a_star (algorithme A*)](/en/terms/a_star-algorithme-a/)
- [d_star (algorithme D*)](/en/terms/d_star-algorithme-d/)
- [incremental_search (recherche incrémentale)](/en/terms/incremental_search-recherche-incrémentale/)
- [path_planning (planification de trajectoire)](/en/terms/path_planning-planification-de-trajectoire/)
