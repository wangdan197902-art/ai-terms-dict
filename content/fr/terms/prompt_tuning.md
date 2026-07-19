---
title: Régulation des invites (Prompt Tuning)
term_id: prompt_tuning
category: training_techniques
subcategory: ''
tags:
- LLM
- Optimization
- efficiency
difficulty: 3
weight: 1
slug: prompt_tuning
date: '2026-07-18T11:34:39.582919Z'
lastmod: '2026-07-18T11:44:45.316024Z'
draft: false
source: agnes_llm
status: published
language: fr
description: Une méthode d'ajustement fin efficace en paramètres qui optimise les
  embeddings d'entrée continus plutôt que de mettre à jour l'ensemble des poids du
  modèle.
---
## Definition

La régulation des invites consiste à ajouter des invites entraînables continues (vecteurs continus) à la couche d'entrée d'un modèle de langage pré-entraîné, tout en gelant les paramètres sous-jacents du modèle. Cette approche permet une adaptation efficace sans réentraînement complet.

### Summary

Une méthode d'ajustement fin efficace en paramètres qui optimise les embeddings d'entrée continus plutôt que de mettre à jour l'ensemble des poids du modèle.

## Key Concepts

- invites souples (soft prompts)
- efficacité paramétrique
- poids gelés
- apprentissage few-shot

## Use Cases

- Adaptation des LLM à des domaines spécifiques
- Ajustement fin à faible ressource
- Optimisation de l'apprentissage multi-tâches

## Related Terms

- [PEFT (Techniques d'ajustement fin efficaces en paramètres)](/en/terms/peft-techniques-d-ajustement-fin-efficaces-en-paramètres/)
- [LoRA (Low-Rank Adaptation, méthode d'ajustement fin par décomposition de rang faible)](/en/terms/lora-low-rank-adaptation-méthode-d-ajustement-fin-par-décomposition-de-rang-faible/)
- [apprentissage en contexte (capacité d'un modèle à apprendre à partir d'exemples fournis dans l'invite)](/en/terms/apprentissage-en-contexte-capacité-d-un-modèle-à-apprendre-à-partir-d-exemples-fournis-dans-l-invite/)
- [ajustement fin (processus d'entraînement supplémentaire d'un modèle pré-entraîné sur un ensemble de données spécifique)](/en/terms/ajustement-fin-processus-d-entraînement-supplémentaire-d-un-modèle-pré-entraîné-sur-un-ensemble-de-données-spécifique/)
