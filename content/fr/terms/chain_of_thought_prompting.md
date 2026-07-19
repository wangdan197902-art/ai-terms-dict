---
title: "Incitation à la chaîne de pensée"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
date: "2026-07-18T10:59:05.923980Z"
lastmod: "2026-07-18T11:44:45.182760Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "L'incitation à la chaîne de pensée est une technique qui encourage les grands modèles de langage à générer des étapes de raisonnement intermédiaires avant de produire une réponse finale."
---
## Definition

L'incitation à la chaîne de pensée (CoT) améliore les performances des grands modèles de langage sur des tâches de raisonnement complexes en demandant explicitement au modèle d'articuler sa logique étape par étape. Au lieu de sauter directement à la conclusion, le modèle décompose le problème.

### Summary

L'incitation à la chaîne de pensée est une technique qui encourage les grands modèles de langage à générer des étapes de raisonnement intermédiaires avant de produire une réponse finale.

## Key Concepts

- Raisonnement étape par étape
- Apprentissage avec quelques exemples
- Déduction logique
- Étapes intermédiaires

## Use Cases

- Résolution de problèmes mathématiques verbaux
- Tâches complexes de raisonnement logique
- Débogage des erreurs de génération de code

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Incitation sans exemple (Prompting zero-shot)](/en/terms/incitation-sans-exemple-prompting-zero-shot/)
- [Incitation avec quelques exemples (Prompting few-shot)](/en/terms/incitation-avec-quelques-exemples-prompting-few-shot/)
- [Cohérence interne (Self-Consistency)](/en/terms/cohérence-interne-self-consistency/)
- [Raisonnement (Processus cognitif ou computationnel)](/en/terms/raisonnement-processus-cognitif-ou-computationnel/)
