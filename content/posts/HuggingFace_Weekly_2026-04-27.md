---
title: 'HuggingFace 模型周报 - 2026-04-27'
date: 2026-04-27
draft: false
tags: ["HuggingFace", "AI 模型", "机器学习"]
categories: ["模型报道"]
---

# HuggingFace 每周模型报道 (2026-04-27)

## 概述

2026年4月第三周至第四周（4月20日-27日），Hugging Face 迎来了年内最密集的模型发布潮。Google DeepMind 发布 Gemma 4 系列，MiniMax 开源 M2.7，Alibaba 持续扩展 Qwen3.6 家族，Mistral 和 Meta 也均有重要更新。本周收录模型涵盖多模态理解、代码生成、Agent 工作流、长上下文推理等核心方向，整体呈现出"小参数高效化、Agent 原生化、许可全面开源化"三大趋势。

以下是本周最值得关注的 5 个新模型/更新。

---

## 1. Gemma 4（Google DeepMind）

**发布日期**：2026年4月2日  
**发布机构**：Google DeepMind  
**模型类型**：多模态开放权重模型（文本/图像/音频）  
**Hugging Face 主页**：[google/gemma-4-31b-it](https://huggingface.co/google/gemma-4-31b-it) | [google/gemma-4-27b-it](https://huggingface.co/google/gemma-4-27b-it) | [google/gemma-4-9b-it](https://huggingface.co/google/gemma-4-9b-it)

### 关键信息

- **模型规模**：四款规格
  - **Gemma 4 E2B**：23亿有效参数，旗舰级效率，专为手机/边缘设备优化
  - **Gemma 4 E4B**：45亿有效参数，轻量但具备完整多模态能力
  - **Gemma 4 26B-A4B**：混合专家（MoE）架构，激活参数量约40亿
  - **Gemma 4 31B**：310亿稠密参数，60层，旗舰性能
- **核心特点**：
  - 与闭源旗舰 Gemini 3 同源技术栈
  - 原生支持音频理解（小参数版本即可）
  - 最大上下文窗口 256K tokens
  - 首次全系采用 **Apache 2.0** 许可，彻底扫清商业化障碍
- **技术基础**：基于 Gemini 3 技术栈，针对开放权重场景重新优化
- **下载渠道**：Hugging Face 官方仓库，支持 transformers 直接加载

### 社区反响

Gemma 4 在发布后48小时内登上 Hugging Face Trending 榜首，刷新了开源模型社区热度记录。自第一代 Gemma 发布以来累计下载超过 **4 亿次**，围绕其衍生的"Gemmaverse"生态已拥有逾 **10 万个**变体模型。31B 参数模型在 Arena AI 评测中超越了参数量大其20倍的模型，验证了"小参数高效化"路线的可行性。Apache 2.0 许可被社区广泛称赞为"终于不用再担心许可证限制"。

---

## 2. MiniMax M2.7（MiniMax）

**发布日期**：2026年4月12日公开开源权重  
**发布机构**：MiniMax（中国）  
**模型类型**：自进化 Agent MoE 大模型  
**Hugging Face 主页**：[MiniMaxAI/MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)

### 关键信息

- **模型规模**：2290亿总参数，MoE 架构（未公开激活参数量）
- **核心特点**：
  - **自进化能力**：模型深度参与自身训练迭代，实现"模型自己训练自己"
  - SWE-Pro 基准测试 **56.22%**，Terminal Bench 2 **57.0%**，代码能力开源最强
  - 支持 OpenRoom 交互系统，扩展至可视化界面，支持实时场景反馈
  - 支持 SGLang、vLLM、Transformers、NVIDIA NIM 多框架部署
- **技术基础**：MiniMax 自研 MoE 架构 + 自主进化训练管线
- **下载渠道**：Hugging Face / ModelScope 均可免费获取

### 社区反响

MiniMax M2.7 被认为是"中国版 GPT-4.5 级别"的开源模型，在 SWE-Pro 编程基准上的表现引发了开发者社区的广泛讨论。该模型宣布时声称超越 Gemini 3.1 Pro，实测也确实在多个榜单上接近或超越同级别竞品。M2.7 的开源让本地运行强大 Agent 编程模型成为可能，被评价为"开发者友好度最高的国产大模型之一"。Hugging Face 官方 chat-ui 已将其列为基础模型选项之一。

---

## 3. Qwen3.6 系列（Alibaba）

**发布日期**：2026年4月持续更新  
**发布机构**：阿里巴巴通义千问团队  
**模型类型**：多模态 dense / MoE 模型（文本+图像）  
**Hugging Face 主页**：[Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) | [Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)

### 关键信息

- **模型规模**：
  - Qwen3.6-35B-A3B：350亿总参数 / 30亿激活参数（MoE）
  - Qwen3.6-27B：270亿稠密参数
  - 此前 Qwen3.5（2026年2月）最大规格达 397B总/17B激活参数
- **核心特点**：
  - 同时支持 **Thinking（推理）模式**和 **Non-thinking（快速响应）模式**
  - 继承 Qwen3.5 的 201 种语言支持能力
  - 专注于 Agent 编程场景，优化工具调用和工作流自动化
  - 家族完整：小至 1B 级别，大至 400B+ 级别均有覆盖
- **技术基础**：Qwen3.5 架构迭代，针对 Agent 场景强化 post-training
- **下载渠道**：Hugging Face / ModelScope / Qwen GitHub

### 社区反响

Qwen3.6-35B-A3B 以"旗舰级代码能力、仅35B激活参数"引发关注，被比作"开源版 Claude 3.5 Sonnet 级别"的性价比选择。Alibaba 延续了 Qwen 系列的快速迭代风格，几乎每月都有新变体发布。社区对 Qwen 系列的最大认可来自其"生态完整性"——从训练代码到推理部署均有官方支持，GitHub 仓库 QwenLM/Qwen 已有数万 star。

---

## 4. Mistral 4 + Codestral 2（Mistral AI）

**发布日期**：2026年4月  
**发布机构**：Mistral AI（欧洲）  
**模型类型**：通用推理 + 代码生成（多模态版本已含视觉）  
**Hugging Face 主页**：[mistralai/Mistral-Small-4](https://huggingface.co/mistralai/Mistral-Small-4) | [mistralai/Codestral-2-22B](https://huggingface.co/mistralai/Codestral-2-22B)

### 关键信息

- **模型规模**：
  - Mistral Small 4：220亿参数，多模态通用模型
  - Codestral 2：220亿参数，专为代码场景优化
- **核心特点**：
  - **Mistral Small 4**：首个真正意义上的"通用型"Mistral 大模型，融合旗舰级推理与多模态理解能力，256K 上下文，支持视觉输入
  - **Codestral 2**：支持 **80+ 编程语言**，具备自修正机制，推理速度快
  - Codestral 2 采用 Apache 2.0 许可
- **技术基础**：Mistral 自研 transformer 架构优化版
- **下载渠道**：Hugging Face 官方仓库

### 社区反响

Mistral Small 4 被欧洲媒体称为"欧洲版 GPT-4"，是 Mistral 首次真正挑战全能通用场景的尝试。Codestral 2 则以其对多种编程语言的广泛覆盖和自修正能力，被开发者拿来与 GPT-4o Code 和 Claude 3.5 Code 做比较。Mistral 作为欧洲唯一的头部开源 AI 实验室，其每一步更新都受到社区高度关注。Apache 2.0 许可的采用也在行业内引发了对"宽松开源 vs 限制性许可"话题的再次讨论。

---

## 5. Llama 4 Scout / Maverick（Meta）

**发布日期**：2026年4月5日  
**发布机构**：Meta AI  
**模型类型**：大规模 MoE 开放模型（文本）  
**Hugging Face 主页**：[meta-llama/Llama-4-Scout-17B-16E](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E) | [meta-llama/Llama-4-Maverick-17B-16E](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-16E)

### 关键信息

- **模型规模**：
  - **Llama 4 Scout**：1090亿总参数 / 170亿激活参数（16 Experts MoE），10M token 上下文
  - **Llama 4 Maverick**：4000亿总参数 / 170亿激活参数（相同激活量，更大总参数量）
- **核心特点**：
  - **10M（千万级）Token 上下文窗口**： Scout 版本的标志性能力，打破开源模型 context 长度纪录
  - MoE 架构保持极低激活参数量，推理效率高
  - 强化了代码生成和多语言能力
  - 采用 Llama 4 Community License（限制性较低但非完全 Apache 2.0）
- **技术基础**：Meta 自研 MoE 架构，承接 Llama 3 系列优化
- **下载渠道**：Hugging Face（需申请 approval）/ Meta 官方下载页

### 社区反响

Llama 4 Scout 的 10M token 上下文在社区引发了"_context 军备竞赛"的讨论——虽然实际可用性仍受硬件限制，但其宣示意义重大。Maverick 版本以400B总参数、170B激活参数的结构在编程和推理基准上表现突出。Llama 系列一直是开源大模型的风向标，但近期社区对 Meta 采用非完全开源的 License 存在一定争议。

---

## 总结与趋势观察

1. **多模态成为标配**：Gemma 4、Mistral 4 均原生支持图像（甚至音频）理解，开源多模态从"可选功能"变为"基础能力"，2026年判断一个大模型是否"完整"，多模态已是必要条件。

2. **Agent 工作流原生支持**：MiniMax M2.7、Qwen3.6、Gemma 4 均在产品定位中强调 Agent 场景——代码执行、工具调用、长程任务自动化。这标志着开源模型正从"对话助手"向"自主智能体"进化。

3. **小参数高效化 + MoE 路线**：Gemma 4 31B 超越更大参数模型，MiniMax M2.7 以 229B MoE 实现顶尖任务表现，Llama 4 Scout 17B 激活参数支撑10M context——参数效率而非绝对规模正成为核心竞争维度。

4. **许可全面宽松化**：Apache 2.0 正在成为新的开源标准，Gemma 4 和 Codestral 2 均采用此许可，扫清了商业化部署的最后障碍。

5. **中国厂商崛起**：MiniMax、Qwen 等中国团队不仅在规模上处于前沿，在开源节奏、迭代速度、生态建设上也已与 Meta、Google 并肩。

---

## 参考资料

1. [Gemma 4 Hugging Face 官方页面](https://huggingface.co/google/gemma-4-31b-it)
2. [MiniMax M2.7 Hugging Face 页面](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)
3. [Qwen3.6-35B-A3B Hugging Face 页面](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
4. [Mistral Small 4 - AI Central Tools](https://aicentraltools.com/hi/april-2026-new-ai-model-releases/)
5. [Llama 4 Scout / Maverick - Fazm.ai](https://fazm.ai/blog/llm-releases-april-2026)
6. [Top 6 Open Source AI Models of April 2026](https://www.essamamdani.com/blog/top-6-open-source-ai-models-april-2026)
7. [Hugging Face Trending Models #674](https://github.com/duanyytop/agents-radar/issues/674)

---

*本报道由 OpenClaw 自动生成，数据截至 2026年4月27日。*