---
title: "Agent"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
date: "2026-07-18T07:40:21.074398Z"
lastmod: "2026-07-18T11:44:44.582804Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Ein KI-System, das in der Lage ist, seine Umgebung wahrzunehmen, zu reasoned und Maßnahmen zu ergreifen, um spezifische Ziele autonom zu erreichen."
---
## Definition

In der KI ist ein Agent eine Entität, die im Auftrag eines Benutzers oder Systems handelt, um Aufgaben zu erledigen. Im Gegensatz zu passiven Modellen, die nur auf Prompts reagieren, können Agenten planen, Werkzeuge nutzen und ihre Aktionen iterativ anpassen.

### Summary

Ein KI-System, das in der Lage ist, seine Umgebung wahrzunehmen, zu reasoned und Maßnahmen zu ergreifen, um spezifische Ziele autonom zu erreichen.

## Key Concepts

- Autonomie
- Werkzeugnutzung
- Planung
- Reaktiver Loop (Schleife)

## Use Cases

- Automatisierte Forschungsassistenten
- Selbstschreibende Bots
- Smart-Home-Controller

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Large Language Model)](/en/terms/llm-large-language-model/)
- [Orchestrierung](/en/terms/orchestrierung/)
- [Tool Calling (Werkzeufruf)](/en/terms/tool-calling-werkzeufruf/)
- [ReAct (Reasoning + Acting)](/en/terms/react-reasoning-acting/)
