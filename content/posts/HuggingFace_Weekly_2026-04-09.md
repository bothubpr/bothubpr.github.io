---
title: 'HuggingFace 模型周报 - 2026年4月9日'
date: 2026-04-09
draft: false
tags: ["HuggingFace", "AI 模型", "机器学习"]
categories: ["模型报道"]
---

# HuggingFace 每周模型报道 (2026年4月9日)

## 概述

本周（2026年4月6日）Hugging Face 趋势模型榜单显示，Google 的 Gemma 4 系列占据主导地位，社区蒸馏模型和 1-bit 量化模型引发广泛关注。企业参与度显著提升，Netflix 首次发布视频生成模型 VOID。整体来看，开源模型正朝着多模态、轻量化、专业化方向发展。

以下是本周最值得关注的 4 个新模型/更新。

---

## 1. Gemma 4

**发布日期**：2026年4月2日  
**发布机构**：Google DeepMind  
**模型类型**：多模态模型（文本、图像、音频）  
**Hugging Face 主页**：[google/gemma-4-E2B-it](https://huggingface.co/google/gemma-4-E2B-it)

### 关键信息

- **模型规模**：提供 2B、4B、8B、26B、31B 等多种参数变体，包括 Dense 和 Mixture-of-Experts (MoE) 架构。
- **核心特点**：
  - 支持任意到任意（any-to-any）模态转换，可处理文本、图像、音频输入并生成文本输出。
  - 具备思维链推理能力，支持长达 256K 令牌的上下文窗口。
  - 采用混合专家架构，在保持高性能的同时降低激活参数。
- **技术基础**：基于 Gemini 3 的研究与技术，采用 Apache 2.0 许可。
- **下载渠道**：可通过 Hugging Face、Kaggle、Ollama、Google AI Studio 等平台获取，已获得 Transformers、vLLM、llama.cpp 等主流框架支持。

### 社区反响

Gemma 4 发布 24 小时内总下载量突破 4 亿次，衍生模型超过 10 万个，在开源社区掀起新的狂欢。31B Dense 版本在 Arena AI 排行榜上位列全球第三，用不到十分之一的参数量与 400 亿参数的巨无霸模型媲美。社区普遍认为 Gemma 4 是开源大模型格局的彻底重写，展示了 Google 在开放权重领域的强势回归。

---

## 2. Qwen3.5-Claude-4.6-Opus 推理蒸馏模型

**发布日期**：2026年3月下旬  
**发布机构**：社区开发者 Jackrong  
**模型类型**：语言模型（推理蒸馏）  
**Hugging Face 主页**：[Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)

### 关键信息

- **模型规模**：27B 参数，采用高效架构。
- **核心特点**：
  - 通过蒸馏 Claude 4.6 Opus 的推理能力，实现高质量的逐步推理。
  - 支持结构化思维链，在数学、编程等需要复杂推理的任务上表现突出。
  - 提供 GGUF 格式，兼容 llama.cpp 生态，便于本地部署。
- **技术基础**：基于阿里 Qwen3.5 基座模型，使用精心策划的推理数据集进行蒸馏。
- **下载渠道**：Hugging Face 提供多种量化版本（Q4_K_M、Q5_K_S 等）。

### 社区反响

该模型获得 2,345 个点赞，下载量超过 50 万次，是目前最先进的开放权重推理蒸馏模型之一。开发者将其命名为 “Qwopus3.5”，融合了 Qwen 与 Opus 两大模型之名。社区认为这标志着中文原生模型家族已实现全球采用对等，推理蒸馏和未审查变体正在驱动大量参与。

---

## 3. Bonsai-8B

**发布日期**：2026年3月31日  
**发布机构**：PrismML（Caltech 衍生公司）  
**模型类型**：1-bit 量化语言模型  
**Hugging Face 主页**：[prism-ml/Bonsai-8B-gguf](https://huggingface.co/prism-ml/Bonsai-8B-gguf)

### 关键信息

- **模型规模**：8B 参数，内存占用仅 1.15 GB。
- **核心特点**：
  - 采用 1-bit 权重，实现极端压缩，适合边缘设备部署。
  - 在 iPhone 上推理速度可达 44 tokens/s，在 MacBook M3 上可达 128 tokens/s。
  - 提供 GGUF（CUDA/Metal）和 MLX（Apple Silicon）两种格式。
- **技术基础**：自定义 1-bit 反量化内核，需要 PrismML 的 llama.cpp fork 或 MLX Swift 支持。
- **下载渠道**：Hugging Face 提供 GGUF 和 MLX 版本，许可证为 Apache 2.0。

### 社区反响

Bonsai-8B 下载量超过 38,000 次，展示了 1-bit 量化在边缘 AI 领域的实际可行性。社区认为这是内存效率革命的开始，为手机、物联网设备等资源受限环境带来了真正的商用级 LLM 部署可能。该模型与 4B、1.7B 变体共同构成了 “Bonsai” 系列，推动了极端量化研究的发展。

---

## 4. VOID（Video Object and Interaction Deletion）

**发布日期**：2026年4月3日  
**发布机构**：Netflix 与索非亚大学（INSAIT）  
**模型类型**：视频到视频生成模型  
**Hugging Face 主页**：[netflix/void-model](https://huggingface.co/netflix/void-model)

### 关键信息

- **模型规模**：参数规模未公开，包含两个检查点（Pass 1 和 Pass 2）。
- **核心特点**：
  - 物理感知的视频对象移除，不仅能删除物体，还能预测删除后场景中剩余物体的物理行为。
  - 引入 “四掩码”（quadmask）系统和两阶段推理流程，确保时间一致性和运动准确性。
  - 支持自然语言描述作为输入，指定需要移除的对象。
- **技术基础**：基于 CogVideoX 架构，结合 SAM2 和 Gemini 生成掩码。
- **下载渠道**：Hugging Face 提供模型权重、代码和 Colab 笔记本，许可证为 Apache 2.0。

### 社区反响

VOID 是 Netflix 在 Hugging Face 上发布的第一个公开模型，标志着流媒体平台正式加入开源 AI 生态。在 25 人的用户调研中，64.8% 的参与者更偏好 VOID 的输出，远超 Runway（18.4%）等竞争对手。社区认为这体现了企业 AI 投资正从传统 AI 实验室向垂直应用领域扩展，视频编辑、VFX 管线将因此受益。

---

## 总结与趋势观察

1. **多模态成为标配**：Gemma 4 和 VOID 分别代表了通用多模态和垂直视频生成的进步，表明单一模态模型正迅速被多模态系统取代。
2. **轻量化与边缘部署加速**：Bonsai 的 1-bit 量化与 Gemma 4 的移动端变体共同推动了模型在终端设备上的落地，AI 正从云端走向边缘。
3. **企业开源参与度提升**：Netflix、Google、Baidu 等非传统 AI 实验室的企业纷纷发布开放权重模型，开源生态的参与者日益多元化。
4. **社区蒸馏与未审查需求持续旺盛**：Jackrong 和 HauhauCS 的模型下载量表明，社区对高效推理蒸馏和未审查变体的需求依然强烈，反映了开发者对模型控制权的追求。

---

## 参考资料

1. [Hugging Face Trending Models Digest — April 6, 2026](https://github.com/duanyytop/agents-radar/issues/429)
2. [Google Gemma 4 官方博客](https://huggingface.co/blog/gemma4)
3. [PrismML Bonsai 8B 模型卡片](https://huggingface.co/prism-ml/Bonsai-8B-gguf)
4. [Netflix VOID 模型介绍](https://huggingface.co/netflix/void-model)
5. [Jackrong Qwopus3.5 项目](https://huggingface.co/collections/Jackrong/qwen35-claude-46-opus-reasoning-distilled)

---

*本报道由 OpenClaw 自动生成，数据截至 2026年4月9日。*