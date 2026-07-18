---
title: "Agensi"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
aliases:
  - /fi/terms/agent/
date: "2026-07-18T15:22:09.621560Z"
lastmod: "2026-07-18T17:15:09.343326Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Tekoälyjärjestelmä, joka kykenee havainnoimaan ympäristöään, päättelyyn ja toimimaan autonomisesti saavuttaakseen tiettyjä tavoitteita."
---

## Definition

Tekoälyssä agensi on yksikkö, joka toimii käyttäjän tai järjestelmän puolesta suorittaakseen tehtäviä. Toisin kuin passiiviset mallit, jotka vain vastaavat prompteihin, agenssit voivat suunnitella, käyttää työkaluja ja iteroida toimissaan.

### Summary

Tekoälyjärjestelmä, joka kykenee havainnoimaan ympäristöään, päättelyyn ja toimimaan autonomisesti saavuttaakseen tiettyjä tavoitteita.

## Key Concepts

- Autonomia
- Työkalujen käyttö
- Suunnittelu
- Reaktiivinen silmukka

## Use Cases

- Automaattiset tutkimusavustajat
- Itsekoodaavat botit
- Älykodin ohjaimet

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Suuri kielimalli)](/en/terms/llm-suuri-kielimalli/)
- [Orchestration (Orkestrointi)](/en/terms/orchestration-orkestrointi/)
- [Tool Calling (Työkalukutsu)](/en/terms/tool-calling-työkalukutsu/)
- [ReAct](/en/terms/react/)
