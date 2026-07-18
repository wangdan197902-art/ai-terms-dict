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
  - /cs/terms/agent/
date: "2026-07-18T15:22:18.954434Z"
lastmod: "2026-07-18T17:15:09.061362Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Systém AI schopný vnímat své prostředí, uvažovat a podnikat akce k dosažení konkrétních cílů autonomně."
---

## Definition

V AI je agent entita, která jedná jménem uživatele nebo systému za účelem splnění úkolů. Na rozdíl od pasivních modelů, které pouze reagují na prompty, mohou agenti plánovat, používat nástroje a iterovat na svých akcích.

### Summary

Systém AI schopný vnímat své prostředí, uvažovat a podnikat akce k dosažení konkrétních cílů autonomně.

## Key Concepts

- Autonomie
- Používání nástrojů
- Plánování
- Reaktivní smyčka

## Use Cases

- Automatizovaní výzkumní asistenti
- Boty pro samostatné programování
- Ovladače chytrých domácností

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Velký jazykový model)](/en/terms/llm-velký-jazykový-model/)
- [Orchestration (Orchestrace)](/en/terms/orchestration-orchestrace/)
- [Tool Calling (Volání nástrojů)](/en/terms/tool-calling-volání-nástrojů/)
- [ReAct (Reakční metoda)](/en/terms/react-reakční-metoda/)
