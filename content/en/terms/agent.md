---
title: "Agent"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
date: "2026-07-18T07:38:16.921858Z"
lastmod: "2026-07-18T11:44:44.576791Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "An AI system capable of perceiving its environment, reasoning, and taking actions to achieve specific goals autonomously."
---
## Definition

In AI, an agent is an entity that acts on behalf of a user or system to complete tasks. Unlike passive models that only respond to prompts, agents can plan, use tools, and iterate on their actions. They often employ loops of thought, action, and observation. Agents can interact with external APIs, browse the web, or execute code. This paradigm shifts AI from a conversational interface to an active participant in complex workflows, enabling automation of multi-step processes.

### Summary

An AI system capable of perceiving its environment, reasoning, and taking actions to achieve specific goals autonomously.

## Key Concepts

- Autonomy
- Tool use
- Planning
- Reactive loop

## Use Cases

- Automated research assistants
- Self-coding bots
- Smart home controllers

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM](/en/terms/llm/)
- [Orchestration](/en/terms/orchestration/)
- [Tool Calling](/en/terms/tool-calling/)
- [ReAct](/en/terms/react/)
