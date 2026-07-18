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
  - /sv/terms/agent/
date: "2026-07-18T15:22:10.153270Z"
lastmod: "2026-07-18T17:15:08.934996Z"
draft: false
source: "agnes_llm"
status: "published"
language: "sv"
description: "Ett AI-system som kan uppfatta sin omgivning, resonera och vidta åtgärder för att uppnå specifika mål autonomt."
---

## Definition

Inom AI är en agent en enhet som agerar åt en användare eller ett system för att slutföra uppgifter. Till skillnad från passiva modeller som endast svarar på prompts, kan agenter planera, använda verktyg och iterera på sina handlingar.

### Summary

Ett AI-system som kan uppfatta sin omgivning, resonera och vidta åtgärder för att uppnå specifika mål autonomt.

## Key Concepts

- Autonomi
- Verktygsanvändning
- Planering
- Reaktiv loop

## Use Cases

- Automatiserade forskningsassistenter
- Självgenererande kodbotar
- Smart home-styrning

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Stor Språkmodell)](/en/terms/llm-stor-språkmodell/)
- [Orkestrering](/en/terms/orkestrering/)
- [Tool Calling (Verktygsanrop)](/en/terms/tool-calling-verktygsanrop/)
- [ReAct (Reasoning + Acting)](/en/terms/react-reasoning-acting/)
