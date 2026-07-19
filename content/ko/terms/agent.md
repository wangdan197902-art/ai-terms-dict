---
title: "에이전트"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
date: "2026-07-18T15:22:07.926617Z"
lastmod: "2026-07-18T16:38:06.765187Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "환경을 지각하고 추론하여 특정 목표를 달성하기 위해 자율적으로 행동을 취할 수 있는 AI 시스템입니다."
---
## Definition

AI에서 에이전트는 사용자를 대신하거나 시스템을 위해 작업을 완료하는 주체입니다. 프롬프트에만 응답하는 수동적인 모델과 달리 에이전트는 계획을 세우고, 도구를 사용하며, 행동을 반복적으로 개선할 수 있습니다.

### Summary

환경을 지각하고 추론하여 특정 목표를 달성하기 위해 자율적으로 행동을 취할 수 있는 AI 시스템입니다.

## Key Concepts

- 자율성
- 도구 사용
- 계획 수립
- 반응 루프

## Use Cases

- 자동화된 연구 보조 도구
- 자동 코딩 봇
- 스마트 홈 컨트롤러

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (대규모 언어 모델)](/en/terms/llm-대규모-언어-모델/)
- [Orchestration (오케스트레이션)](/en/terms/orchestration-오케스트레이션/)
- [Tool Calling (툴 호출)](/en/terms/tool-calling-툴-호출/)
- [ReAct (ReAct 프롬프팅 기법)](/en/terms/react-react-프롬프팅-기법/)
