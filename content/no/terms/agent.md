---
title: "Agent"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
date: "2026-07-18T15:22:14.715160Z"
lastmod: "2026-07-18T16:38:06.929911Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "Et AI-system som evner å oppfatte sitt miljø, resonnere og utføre handlinger for å oppnå spesifikke mål autonomt."
---
## Definition

Innefor AI er en agent en enhet som handler på vegne av en bruker eller et system for å fullføre oppgaver. I motsetning til passive modeller som bare responderer på prompts, kan agenter planlegge, bruke verktøy og iterere på sine handlinger for å nå et mål.

### Summary

Et AI-system som evner å oppfatte sitt miljø, resonnere og utføre handlinger for å oppnå spesifikke mål autonomt.

## Key Concepts

- Autonomi
- Verktøybruk
- Planlegging
- Reaktiv løkke

## Use Cases

- Automatiserte forskningsassistenter
- Selvkodende boter
- Styringssystemer for smarte hjem

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Stor språkmodell)](/en/terms/llm-stor-språkmodell/)
- [Orchestration (Koordinering av flere komponenter)](/en/terms/orchestration-koordinering-av-flere-komponenter/)
- [Tool Calling (Anrop av eksterne verktøy)](/en/terms/tool-calling-anrop-av-eksterne-verktøy/)
- [ReAct (Resonnering og Handling)](/en/terms/react-resonnering-og-handling/)
