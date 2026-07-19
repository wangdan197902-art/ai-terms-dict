---
title: "Agente"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
date: "2026-07-18T14:32:09.368148Z"
lastmod: "2026-07-18T15:51:59.422673Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Um sistema de IA capaz de perceber seu ambiente, raciocinar e executar ações para alcançar objetivos específicos de forma autônoma."
---
## Definition

Em IA, um agente é uma entidade que age em nome de um usuário ou sistema para concluir tarefas. Diferente dos modelos passivos que apenas respondem a prompts, os agentes podem planejar, usar ferramentas e iterar sobre suas ações.

### Summary

Um sistema de IA capaz de perceber seu ambiente, raciocinar e executar ações para alcançar objetivos específicos de forma autônoma.

## Key Concepts

- Autonomia
- Uso de Ferramentas
- Planejamento
- Loop Reativo

## Use Cases

- Assistentes de pesquisa automatizados
- Bots de codificação autônomos
- Controladores de casa inteligente

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Modelo de Linguagem Grande)](/en/terms/llm-modelo-de-linguagem-grande/)
- [Orquestração (Coordenação de componentes)](/en/terms/orquestração-coordenação-de-componentes/)
- [Tool Calling (Chamada de Ferramentas)](/en/terms/tool-calling-chamada-de-ferramentas/)
- [ReAct (Raciocínio e Ação)](/en/terms/react-raciocínio-e-ação/)
