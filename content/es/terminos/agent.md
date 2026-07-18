---
title: "Agente"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
aliases:
  - /es/terms/agent/
date: "2026-07-18T07:39:26.714082Z"
lastmod: "2026-07-18T11:44:44.579858Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "Un sistema de IA capaz de percibir su entorno, razonar y realizar acciones para alcanzar objetivos específicos de forma autónoma."
---

## Definition

En IA, un agente es una entidad que actúa en nombre de un usuario o sistema para completar tareas. A diferencia de los modelos pasivos que solo responden a prompts, los agentes pueden planificar, utilizar herramientas externas e iterar sobre sus acciones para resolver problemas complejos.

### Summary

Un sistema de IA capaz de percibir su entorno, razonar y realizar acciones para alcanzar objetivos específicos de forma autónoma.

## Key Concepts

- Autonomía
- Uso de herramientas
- Planificación
- Bucle reactivo

## Use Cases

- Asistentes de investigación automatizados
- Bots de codificación autónomos
- Controladores de hogares inteligentes

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Modelo de Lenguaje Grande)](/en/terms/llm-modelo-de-lenguaje-grande/)
- [Orchestration (Orquestación)](/en/terms/orchestration-orquestación/)
- [Tool Calling (Llamada a Herramientas)](/en/terms/tool-calling-llamada-a-herramientas/)
- [ReAct (Patrón de Razonamiento y Acción)](/en/terms/react-patrón-de-razonamiento-y-acción/)
