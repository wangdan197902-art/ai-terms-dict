---
title: "Agent"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
date: "2026-07-18T15:22:28.007591Z"
lastmod: "2026-07-18T17:15:09.586837Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "Un sistem de IA capabil să perceapă mediul, să raționeze și să întreprindă acțiuni pentru a atinge obiective specifice în mod autonom."
---
## Definition

În IA, un agent este o entitate care acționează în numele unui utilizator sau al unui sistem pentru a îndeplini sarcini. Spre deosebire de modelele pasive care răspund doar la prompturi, agenții pot planifica, utiliza instrumente externe și itera asupra acțiunilor lor pentru a rezolva probleme complexe, adaptându-se dinamic la schimbările din mediu.

### Summary

Un sistem de IA capabil să perceapă mediul, să raționeze și să întreprindă acțiuni pentru a atinge obiective specifice în mod autonom.

## Key Concepts

- Autonomie
- Utilizarea instrumentelor
- Planificare
- Bucle reacțive

## Use Cases

- Asistenți automatizați pentru cercetare
- Boți de programare autonomi
- Controllere pentru case inteligente

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Model Lingvistic Mare)](/en/terms/llm-model-lingvistic-mare/)
- [Orchestration (Orchestrare)](/en/terms/orchestration-orchestrare/)
- [Tool Calling (Apelarea Instrumentelor)](/en/terms/tool-calling-apelarea-instrumentelor/)
- [ReAct (Reasoning + Acting)](/en/terms/react-reasoning-acting/)
