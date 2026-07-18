---
title: "on-policy"
term_id: "on_policy"
category: "basic_concepts"
subcategory: ""
tags: ["RL", "algorithms", "learning"]
difficulty: 4
weight: 1
slug: "on_policy"
aliases:
  - /fr/terms/on_policy/
date: "2026-07-18T10:57:58.875213Z"
lastmod: "2026-07-18T11:44:45.179810Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Une approche d'apprentissage par renforcement où la politique évaluée et améliorée est identique à celle utilisée pour générer les données."
---

## Definition

Les algorithmes on-policy exigent que l'apprentissage se fasse directement à partir des actions effectuées par sa politique actuelle. Cela signifie que les données collectées lors de l'exploration sont utilisées immédiatement pour mettre à jour la politique, garantissant ainsi la cohérence des données.

### Summary

Une approche d'apprentissage par renforcement où la politique évaluée et améliorée est identique à celle utilisée pour générer les données.

## Key Concepts

- apprentissage par renforcement
- gradient de politique
- cohérence des données
- efficacité d'échantillonnage

## Use Cases

- Contrôle robotique avec contraintes de sécurité
- Agents de jeu nécessitant des mises à jour précises
- Systèmes adaptatifs en temps réel

## Related Terms

- [off-policy (hors politique)](/en/terms/off-policy-hors-politique/)
- [REINFORCE (algorithme REINFORCE)](/en/terms/reinforce-algorithme-reinforce/)
- [PPO (Proximal Policy Optimization)](/en/terms/ppo-proximal-policy-optimization/)
- [actor-critic (acteur-critique)](/en/terms/actor-critic-acteur-critique/)
