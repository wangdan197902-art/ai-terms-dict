---
title: "异步处理"
term_id: "async_processing"
category: "engineering_practice"
subcategory: ""
tags: ["programming", "performance", "software_engineering"]
difficulty: 3
weight: 1
slug: "async_processing"
aliases:
  - /zh/terms/async_processing/
date: "2026-07-18T11:07:14.726897Z"
lastmod: "2026-07-18T11:44:45.446608Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种编程范式，任务在主执行线程之外独立运行，允许进行非阻塞操作。"
---

## Definition

异步处理允许软件执行长时间运行的任务（如I/O操作或复杂计算），而不会冻结主应用程序界面或阻塞其他进程。通过事件循环和回调机制，程序可以在等待任务完成的同时继续响应其他请求，从而提高系统的并发能力和响应速度。

### Summary

一种编程范式，任务在主执行线程之外独立运行，允许进行非阻塞操作。

## Key Concepts

- 非阻塞I/O
- 事件循环
- 并发
- 线程

## Use Cases

- 实时视频流处理
- 同时处理多个API请求
- 后台模型训练任务

## Code Example

```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    return 'Data'

asyncio.run(fetch_data())
```

## Related Terms

- [Multithreading (多线程)](/en/terms/multithreading-多线程/)
- [Callbacks (回调)](/en/terms/callbacks-回调/)
- [Promises (承诺/异步对象)](/en/terms/promises-承诺-异步对象/)
- [Microservices (微服务)](/en/terms/microservices-微服务/)
