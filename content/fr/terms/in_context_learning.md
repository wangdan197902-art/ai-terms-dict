---
title: "Apprentissage en contexte"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
date: "2026-07-18T07:43:15.896521Z"
lastmod: "2026-07-18T11:44:44.589519Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Une technique où les modèles apprennent à effectuer des tâches en observant des exemples fournis dans l'invite."
---
## Definition

L'apprentissage en contexte (ICL) permet aux grands modèles de langage de s'adapter à de nouvelles tâches sans mettre à jour leurs poids. En fournissant des paires entrée-sortie dans le contexte de l'invite, le modèle déduit le motif et...

### Summary

Une technique où les modèles apprennent à effectuer des tâches en observant des exemples fournis dans l'invite.

## Key Concepts

- Apprentissage few-shot
- Zéro-shot
- Conception de prompt
- Adaptation sans mise à jour des poids

## Use Cases

- Tester rapidement les capacités du modèle sur de nouveaux ensembles de données
- Changement dynamique de tâche dans les agents conversationnels
- Prototypage d'applications d'IA sans réentraînement

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Ingénierie de prompt (optimisation des invites)](/en/terms/ingénierie-de-prompt-optimisation-des-invites/)
- [Few-shot (apprentissage avec quelques exemples)](/en/terms/few-shot-apprentissage-avec-quelques-exemples/)
- [Zero-shot (apprentissage sans exemples)](/en/terms/zero-shot-apprentissage-sans-exemples/)
- [Méta-apprentissage (apprendre à apprendre)](/en/terms/méta-apprentissage-apprendre-à-apprendre/)
