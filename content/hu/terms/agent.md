---
title: "Ügynök"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
aliases:
  - /hu/terms/agent/
date: "2026-07-18T15:22:26.336577Z"
lastmod: "2026-07-18T17:15:09.712918Z"
draft: false
source: "agnes_llm"
status: "published"
language: "hu"
description: "Egy AI rendszer, amely képes érzékelni a környezetét, érvelni, és autonóm módon cselekedni a konkrét célok elérése érdekében."
---

## Definition

Az AI-ban egy ügynök egy entitás, amely felhasználó vagy rendszer nevében végzi el a feladatokat. A passzív modellekkel ellentétben, amelyek csak promptokra válaszolnak, az ügynökök képesek tervezni, eszközöket használni és iterálni a cselekvéseiken.

### Summary

Egy AI rendszer, amely képes érzékelni a környezetét, érvelni, és autonóm módon cselekedni a konkrét célok elérése érdekében.

## Key Concepts

- Autonómia
- Eszközhasználat
- Tervezés
- Reaktív hurok

## Use Cases

- Automatikus kutatóasszisztensek
- Önkódoló botok
- Okosotthon-vezérlők

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Nagy Nyelvi Modell)](/en/terms/llm-nagy-nyelvi-modell/)
- [Orchestration (Orchestráció / Koordináció)](/en/terms/orchestration-orchestráció-koordináció/)
- [Tool Calling (Eszközlehívás)](/en/terms/tool-calling-eszközlehívás/)
- [ReAct (Reasoning + Acting / Érvelés és Cselekvés)](/en/terms/react-reasoning-acting-érvelés-és-cselekvés/)
