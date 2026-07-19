---
title: "Agent"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
date: "2026-07-18T15:22:22.749364Z"
lastmod: "2026-07-18T17:15:08.804832Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "System AI zdolny do postrzegania środowiska, rozumowania i podejmowania działań w celu osiągnięcia określonych celów autonomicznie."
---
## Definition

W sztucznej inteligencji agentem jest podmiot działający w imieniu użytkownika lub systemu w celu wykonania zadań. W przeciwieństwie do pasywnych modeli reagujących tylko na prompty, agenci mogą planować, korzystać z narzędzi i iteracyjnie doskonalić swoje działania.

### Summary

System AI zdolny do postrzegania środowiska, rozumowania i podejmowania działań w celu osiągnięcia określonych celów autonomicznie.

## Key Concepts

- Autonomia
- Korzystanie z narzędzi
- Planowanie
- Pętla reaktywna

## Use Cases

- Zautomatyzowani asystenci badawczy
- Boty piszące kod samodzielnie
- Kontrolery inteligentnego domu

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Duży Model Językowy)](/en/terms/llm-duży-model-językowy/)
- [Orchestration (Orkiestracja)](/en/terms/orchestration-orkiestracja/)
- [Tool Calling (Wywoływanie narzędzi)](/en/terms/tool-calling-wywoływanie-narzędzi/)
- [ReAct (Reakcja)](/en/terms/react-reakcja/)
