---
title: "API"
term_id: "api"
category: "engineering_practice"
subcategory: ""
tags: ["Development", "Integration", "Infrastructure"]
difficulty: 1
weight: 1
slug: "api"
aliases:
  - /zh/terms/api/
date: "2026-07-18T07:43:58.206729Z"
lastmod: "2026-07-18T11:44:44.590357Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "应用程序编程接口，允许不同的软件系统进行通信和数据交换。"
---

## Definition

API 定义了一套用于构建软件和应用程序的协议与工具。在 AI 领域，API 使开发人员能够访问强大的模型（如大语言模型或图像生成器），而无需在本地托管这些模型，从而简化了集成过程并降低了计算成本。

### Summary

应用程序编程接口，允许不同的软件系统进行通信和数据交换。

## Key Concepts

- 端点
- REST
- 身份验证
- 负载

## Use Cases

- 将聊天机器人集成到网站中
- 访问基于云的机器学习模型
- 从 AI 服务中检索数据

## Code Example

```python
import requests
response = requests.get('https://api.ai.com/v1/generate', headers={'Authorization': 'Bearer token'})
```

## Related Terms

- [REST (表述性状态转移)](/en/terms/rest-表述性状态转移/)
- [SDK (软件开发工具包)](/en/terms/sdk-软件开发工具包/)
- [Webhook (网络钩子)](/en/terms/webhook-网络钩子/)
- [Integration (集成)](/en/terms/integration-集成/)
