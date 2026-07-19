---
title: 偏好学习
term_id: preference_learning
category: training_techniques
subcategory: ''
tags:
- alignment
- Human Feedback
- rlhf
difficulty: 3
weight: 1
slug: preference_learning
date: '2026-07-18T11:30:18.063183Z'
lastmod: '2026-07-18T11:44:45.544225Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种利用比较反馈训练模型，使其输出与人类偏好对齐的技术。
---
## Definition

偏好学习侧重于教导模型根据人类的判断而非绝对标签来区分好坏输出。它通常涉及收集成对的响应数据，其中人类标注者指出哪个响应更符合其偏好，从而训练奖励模型以量化这些偏好。

### Summary

一种利用比较反馈训练模型，使其输出与人类偏好对齐的技术。

## Key Concepts

- 人类反馈
- 成对比较
- 奖励建模
- 对齐

## Use Cases

- 大型语言模型的基于人类反馈的强化学习 (RLHF)
- 推荐系统
- 内容审核过滤

## Related Terms

- [rlhf (基于人类反馈的强化学习)](/en/terms/rlhf-基于人类反馈的强化学习/)
- [reward_modeling (奖励建模)](/en/terms/reward_modeling-奖励建模/)
- [human_in_the_loop (人在回路)](/en/terms/human_in_the_loop-人在回路/)
- [alignment (对齐)](/en/terms/alignment-对齐/)
