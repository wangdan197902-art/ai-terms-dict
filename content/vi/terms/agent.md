---
title: "Agent (Tác nhân AI)"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
aliases:
  - /vi/terms/agent/
date: "2026-07-18T15:22:23.225783Z"
lastmod: "2026-07-18T16:38:07.677448Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Một hệ thống AI có khả năng nhận biết môi trường, lập luận và thực hiện các hành động để đạt được mục tiêu cụ thể một cách tự chủ."
---

## Definition

Trong AI, một agent là một thực thể hành động thay mặt người dùng hoặc hệ thống để hoàn thành nhiệm vụ. Khác với các mô hình thụ động chỉ phản hồi lại prompt, các agent có thể lập kế hoạch, sử dụng công cụ và lặp lại các hành động của mình.

### Summary

Một hệ thống AI có khả năng nhận biết môi trường, lập luận và thực hiện các hành động để đạt được mục tiêu cụ thể một cách tự chủ.

## Key Concepts

- Tính tự chủ (Autonomy)
- Sử dụng công cụ (Tool use)
- Lập kế hoạch (Planning)
- Vòng lặp phản ứng (Reactive loop)

## Use Cases

- Trợ lý nghiên cứu tự động
- Bot tự viết mã
- Bộ điều khiển nhà thông minh

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Mô hình ngôn ngữ lớn)](/en/terms/llm-mô-hình-ngôn-ngữ-lớn/)
- [Orchestration (Điều phối)](/en/terms/orchestration-điều-phối/)
- [Tool Calling (Gọi công cụ)](/en/terms/tool-calling-gọi-công-cụ/)
- [ReAct (Kết hợp Suy nghĩ và Hành động)](/en/terms/react-kết-hợp-suy-nghĩ-và-hành-động/)
