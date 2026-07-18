---
title: "Rate Limiting"
term_id: "rate_limiting"
category: "engineering_practice"
subcategory: ""
tags: ["infrastructure", "security", "devops"]
difficulty: 2
weight: 1
slug: "rate_limiting"
aliases:
  - /en/terms/rate_limiting/
date: "2026-07-18T10:13:36.396620Z"
lastmod: "2026-07-18T11:44:44.716048Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "An engineering control mechanism that restricts the number of requests a client can make to a service within a specific time window."
---

## Definition

Rate limiting protects AI services and APIs from abuse, overload, and excessive resource consumption. It ensures fair usage among users and maintains system stability by capping throughput. Common strategies include token bucket, leaky bucket, and fixed window counters. In AI deployments, it is critical for managing inference costs and preventing Denial of Service (DoS) attacks on sensitive models.

### Summary

An engineering control mechanism that restricts the number of requests a client can make to a service within a specific time window.

## Key Concepts

- API protection
- Throughput control
- Fair usage policy
- System stability

## Use Cases

- LLM API gateway management
- Preventing DDoS attacks
- Managing cloud compute costs

## Related Terms

- [Throttling](/en/terms/throttling/)
- [QoS](/en/terms/qos/)
- [API Gateway](/en/terms/api-gateway/)
- [Load balancing](/en/terms/load-balancing/)
