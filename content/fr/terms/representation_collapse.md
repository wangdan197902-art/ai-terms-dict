---
title: Effondrement de la représentation
term_id: representation_collapse
category: basic_concepts
subcategory: ''
tags:
- Self Supervised
- Training Dynamics
- Computer Vision
difficulty: 3
weight: 1
slug: representation_collapse
date: '2026-07-18T11:36:23.002310Z'
lastmod: '2026-07-18T11:44:45.323005Z'
draft: false
source: agnes_llm
status: published
language: fr
description: Un mode d'échec dans l'apprentissage auto-supervisé où le modèle produit
  des représentations identiques pour toutes les entrées, perdant ainsi son pouvoir
  discriminatif.
---
## Definition

L'effondrement de la représentation se produit lorsqu'un réseau de neurones, en particulier dans les cadres d'apprentissage contrastif auto-supervisé, apprend à mapper tous les points de données d'entrée vers le même vecteur de sortie fixe. Cette solution triviale réduit l'utilité du modèle pour les tâches de downstream.

### Summary

Un mode d'échec dans l'apprentissage auto-supervisé où le modèle produit des représentations identiques pour toutes les entrées, perdant ainsi son pouvoir discriminatif.

## Key Concepts

- Apprentissage auto-supervisé
- Perte contrastive
- Solutions triviales
- Apprentissage de caractéristiques

## Use Cases

- Débogage des modèles SimCLR ou MoCo
- Amélioration des fonctions de perte contrastive
- Analyse de la convergence du modèle

## Related Terms

- [Apprentissage contrastif](/en/terms/apprentissage-contrastif/)
- [Normalisation par lot](/en/terms/normalisation-par-lot/)
- [Encodeur à momentum](/en/terms/encodeur-à-momentum/)
- [Extraction de caractéristiques](/en/terms/extraction-de-caractéristiques/)
