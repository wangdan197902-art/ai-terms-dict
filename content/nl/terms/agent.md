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
  - /nl/terms/agent/
date: "2026-07-18T15:22:08.358990Z"
lastmod: "2026-07-18T17:15:08.677849Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Een AI-systeem dat in staat is zijn omgeving waar te nemen, te redeneren en handelingen te verrichten om specifieke doelen autonoom te bereiken."
---

## Definition

In AI is een agent een entiteit die handelt namens een gebruiker of systeem om taken voltooien. In tegenstelling tot passieve modellen die alleen reageren op prompts, kunnen agenten plannen, gereedschap gebruiken en itereren op hun acties.

### Summary

Een AI-systeem dat in staat is zijn omgeving waar te nemen, te redeneren en handelingen te verrichten om specifieke doelen autonoom te bereiken.

## Key Concepts

- Autonomie
- Gereedschapsgebruik
- Planning
- Reactive loop (reactieve lus)

## Use Cases

- Geautomatiseerde onderzoeksassistenten
- Zelfcoderende bots
- Slimme huiscontrollers

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Large Language Model)](/en/terms/llm-large-language-model/)
- [Orchestration (orkestratie)](/en/terms/orchestration-orkestratie/)
- [Tool Calling (gereedschapsaanroep)](/en/terms/tool-calling-gereedschapsaanroep/)
- [ReAct (Reasoning + Acting)](/en/terms/react-reasoning-acting/)
