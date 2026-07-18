---
title: "Agent"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
aliases:
  - /da/terms/agent/
date: "2026-07-18T15:22:13.416350Z"
lastmod: "2026-07-18T17:15:09.216668Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "Et AI-system, der er i stand til at opfatte sit miljø, ræsonnere og udføre handlinger for at opnå specifikke mål autonomt."
---

## Definition

Inden for AI er en agent en enhed, der handler på vegne af en bruger eller et system for at fuldføre opgaver. I modsætning til passive modeller, der kun reagerer på prompts, kan agenter planlægge, bruge værktøjer og iterere over deres handlinger.

### Summary

Et AI-system, der er i stand til at opfatte sit miljø, ræsonnere og udføre handlinger for at opnå specifikke mål autonomt.

## Key Concepts

- Autonomi
- Værktøjsbrug
- Planlægning
- Reaktiv løkke

## Use Cases

- Automatiserede forskningsassistenter
- Selvkodende botte
- Smart home-styringer

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Large Language Model)](/en/terms/llm-large-language-model/)
- [Orchestration (Orkestrering)](/en/terms/orchestration-orkestrering/)
- [Tool Calling (Værktøjskald)](/en/terms/tool-calling-værktøjskald/)
- [ReAct](/en/terms/react/)
