---
title: "Agente"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
date: "2026-07-18T15:22:14.280322Z"
lastmod: "2026-07-18T17:15:08.558845Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Un sistema di IA capace di percepire il proprio ambiente, ragionare e intraprendere azioni per raggiungere obiettivi specifici in modo autonomo."
---
## Definition

Nell'IA, un agente è un'entità che agisce per conto di un utente o di un sistema per completare compiti. A differenza dei modelli passivi che rispondono solo ai prompt, gli agenti possono pianificare, utilizzare strumenti e iterare sulle proprie azioni.

### Summary

Un sistema di IA capace di percepire il proprio ambiente, ragionare e intraprendere azioni per raggiungere obiettivi specifici in modo autonomo.

## Key Concepts

- Autonomia
- Uso di strumenti
- Pianificazione
- Loop reattivo

## Use Cases

- Assistenti di ricerca automatizzati
- Bot di codifica autonoma
- Controller per la casa intelligente

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Large Language Model)](/en/terms/llm-large-language-model/)
- [Orchestrazione](/en/terms/orchestrazione/)
- [Tool Calling (Chiamata di strumenti)](/en/terms/tool-calling-chiamata-di-strumenti/)
- [ReAct](/en/terms/react/)
