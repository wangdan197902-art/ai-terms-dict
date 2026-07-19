---
title: "Agent"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
date: "2026-07-18T07:42:27.302403Z"
lastmod: "2026-07-18T11:44:44.587671Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Un système d'IA capable de percevoir son environnement, de raisonner et d'entreprendre des actions pour atteindre des objectifs spécifiques de manière autonome."
---
## Definition

En IA, un agent est une entité qui agit au nom d'un utilisateur ou d'un système pour accomplir des tâches. Contrairement aux modèles passifs qui ne font que répondre aux invites, les agents peuvent planifier, utiliser des outils et itérer sur leurs actions.

### Summary

Un système d'IA capable de percevoir son environnement, de raisonner et d'entreprendre des actions pour atteindre des objectifs spécifiques de manière autonome.

## Key Concepts

- Autonomie
- Utilisation d'outils
- Planification
- Boucle réactive

## Use Cases

- Assistants de recherche automatisés
- Bots de codage autonome
- Contrôleurs de maison intelligente

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Grand modèle de langage)](/en/terms/llm-grand-modèle-de-langage/)
- [Orchestration (Orchestration)](/en/terms/orchestration-orchestration/)
- [Tool Calling (Appel d'outils)](/en/terms/tool-calling-appel-d-outils/)
- [ReAct (Réaction raisonnée)](/en/terms/react-réaction-raisonnée/)
