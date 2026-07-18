---
title: "智能体"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
aliases:
  - /zh/terms/agent/
date: "2026-07-18T07:43:58.206740Z"
lastmod: "2026-07-18T11:44:44.590462Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种能够感知环境、进行推理并自主采取行动以实现特定目标的 AI 系统。"
---

## Definition

在 AI 中，智能体是代表用户或系统执行任务的实体。与仅对提示做出响应的被动模型不同，智能体具备规划能力，可以使用工具，并能根据其行动结果进行迭代和调整，从而更复杂地解决多步骤问题。

### Summary

一种能够感知环境、进行推理并自主采取行动以实现特定目标的 AI 系统。

## Key Concepts

- 自主性
- 工具使用
- 规划
- 反应循环

## Use Cases

- 自动化研究助手
- 自编码机器人
- 智能家居控制器

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (大型语言模型)](/en/terms/llm-大型语言模型/)
- [Orchestration (编排)](/en/terms/orchestration-编排/)
- [Tool Calling (工具调用)](/en/terms/tool-calling-工具调用/)
- [ReAct (推理与行动)](/en/terms/react-推理与行动/)
