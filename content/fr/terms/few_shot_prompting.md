---
title: Incitation à exemples limités
term_id: few_shot_prompting
category: application_paradigms
subcategory: ''
tags:
- prompting
- LLM
- technique
difficulty: 2
weight: 1
slug: few_shot_prompting
date: '2026-07-18T10:59:45.007370Z'
lastmod: '2026-07-18T11:44:45.184584Z'
draft: false
source: agnes_llm
status: published
language: fr
description: L'incitation à exemples limités est une technique où les grands modèles
  de langage (LLM) reçoivent un petit nombre d'exemples entrée-sortie dans l'incitation
  pour guider leur comportement.
---
## Definition

Cette méthode exploite les capacités d'apprentissage contextuel des grands modèles de langage en fournissant quelques exemples illustratifs directement dans l'incitation. Contrairement au réglage fin (fine-tuning), qui nécessite de mettre à jour les poids du modèle, cette approche repose uniquement sur le contexte fourni lors de l'inférence.

### Summary

L'incitation à exemples limités est une technique où les grands modèles de langage (LLM) reçoivent un petit nombre d'exemples entrée-sortie dans l'incitation pour guider leur comportement.

## Key Concepts

- Apprentissage contextuel
- Ingénierie d'incitations
- Guidage par exemples
- Comparaison zéro exemple

## Use Cases

- Formatage de l'analyse de sentiment
- Adaptation du style de code
- Extraction de données structurées

## Code Example

```python
response = llm.generate(
    prompt="Translate English to French:\n"
           "Hello -> Bonjour\n"
           "World -> Monde\n"
           "Cat -> ?"
)
```

## Related Terms

- [zero_shot (zéro exemple)](/en/terms/zero_shot-zéro-exemple/)
- [prompt_engineering (ingénierie d'incitations)](/en/terms/prompt_engineering-ingénierie-d-incitations/)
- [in_context_learning (apprentissage contextuel)](/en/terms/in_context_learning-apprentissage-contextuel/)
- [llm (grand modèle de langage)](/en/terms/llm-grand-modèle-de-langage/)
