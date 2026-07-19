---
title: "速率限制"
term_id: "rate_limiting"
category: "engineering_practice"
subcategory: ""
tags: ["infrastructure", "security", "devops"]
difficulty: 2
weight: 1
slug: "rate_limiting"
date: "2026-07-18T11:31:50.443914Z"
lastmod: "2026-07-18T11:44:45.549530Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种工程控制机制，限制客户端在特定时间窗口内向服务发起的请求数量。"
---
## Definition

速率限制保护 AI 服务和 API 免受滥用、过载和过度资源消耗的侵害。它通过限制吞吐量确保用户间的公平使用，并维持系统稳定性。常见的策略包括令牌桶或漏桶算法。

### Summary

一种工程控制机制，限制客户端在特定时间窗口内向服务发起的请求数量。

## Key Concepts

- API 保护
- 吞吐量控制
- 公平使用政策
- 系统稳定性

## Use Cases

- 大语言模型 (LLM) API 网关管理
- 防止分布式拒绝服务 (DDoS) 攻击
- 管理云计算成本

## Related Terms

- [节流 (Throttling)](/en/terms/节流-throttling/)
- [服务质量 (QoS)](/en/terms/服务质量-qos/)
- [API 网关 (API Gateway)](/en/terms/api-网关-api-gateway/)
- [负载均衡 (Load balancing)](/en/terms/负载均衡-load-balancing/)
