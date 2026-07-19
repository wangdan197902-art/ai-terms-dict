---
title: Co-apprentissage
term_id: co_training
category: training_techniques
subcategory: ''
tags:
- Semi Supervised
- algorithm
- Data Efficiency
difficulty: 4
weight: 1
slug: co_training
date: '2026-07-18T11:08:11.691292Z'
lastmod: '2026-07-18T11:44:45.207834Z'
draft: false
source: agnes_llm
status: published
language: fr
description: Le co-apprentissage est un algorithme d'apprentissage semi-supervisé
  où deux vues des données sont utilisées pour entraîner des classificateurs séparés
  qui étiquettent itérativement les données non ét
---
## Definition

Cette méthode exploite plusieurs ensembles de caractéristiques distincts (vues) des mêmes points de données. Initialement, deux classificateurs sont entraînés sur de petits ensembles de données étiquetés provenant de chaque vue. Ils prédisent ensuite les étiquettes pour les données non étiquetées

### Summary

Le co-apprentissage est un algorithme d'apprentissage semi-supervisé où deux vues des données sont utilisées pour entraîner des classificateurs séparés qui étiquettent itérativement les données non étiquetées les unes pour les autres.

## Key Concepts

- Apprentissage semi-supervisé
- Multiples vues
- Étiquetage itératif
- Sélection haute confiance

## Use Cases

- Classification de texte avec multiples caractéristiques
- Catégorisation de pages web
- Augmentation de données avec peu d'étiquettes

## Related Terms

- [Apprentissage semi-supervisé](/en/terms/apprentissage-semi-supervisé/)
- [Auto-apprentissage](/en/terms/auto-apprentissage/)
- [Apprentissage multi-vues](/en/terms/apprentissage-multi-vues/)
- [Apprentissage actif](/en/terms/apprentissage-actif/)
