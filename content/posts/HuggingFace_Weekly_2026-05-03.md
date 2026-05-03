---
title: 'HuggingFace 模型周报 - 2026-05-03'
date: 2026-05-03
draft: false
tags: ["HuggingFace", "AI 模型", "机器学习"]
categories: ["模型报道"]
---

# HuggingFace 每周模型报道 (2026-05-03)

## 概述

过去一周（4月27日至5月3日）是2026年以来 HuggingFace 上模型发布最密集的一周之一。DeepSeek V4-Pro 以 1.6T 参数、1M 上下文窗口的狂暴规格横扫社区，成为完全开源模型在编码基准上首次逼近甚至超越闭源前沿模型的关键里程碑。与此同时，月之暗面 Kimi K2.6 以 300 智能体并行能力重新定义了开源 Agent 编程的天花板；腾讯在姚顺雨加盟后交出 Hy3 preview 首份答卷；阿里 Qwen3.6-27B 则以小博大，用 27B 稠密模型超越自家 397B MoE。此外，Inclusion AI 的 LLaDA2.0-Uni 首次将扩散语言模型引入多模态统一框架，开创了非自回归路线的全新范式。

以下是本周最值得关注的 5 个新模型/更新。

---

## 1. DeepSeek V4-Pro

**发布日期**：2026年04月24日  
**发布机构**：DeepSeek AI（深度求索）  
**模型类型**：文本生成（Mixture-of-Experts）  
**Hugging Face 主页**：[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

### 关键信息

- **模型规模**：1.6T 总参数，49B 激活参数（每token）；865GB 权重下载
- **核心特点**：
  - 1,000,000 token 上下文窗口，百万级长文本处理
  - SWE-bench Verified 得分 80.6%，仅差 Claude Opus 4.6 0.2 个百分点
  - MMLU-Pro 得分 87.5%，多项基准超越同级开源与闭源模型
  - 输出价格 $3.48/百万 token，仅为 Claude Opus 4.6（$25）的约 1/7
  - 同时发布 V4-Flash 轻量版（284B 参数 / 13B 激活）
- **技术基础**：MoE 架构，支持三种推理模式（Non-think、Think High、Think Max）
- **下载渠道**：HuggingFace、DeepSeek API、chat.deepseek.com，MIT 许可证

### 社区反响

DeepSeek V4 的发布在社区引起了极大震荡。凭借真正开源的权重在编码基准上与闭源模型正面交锋，且推理成本仅为竞品的零头，开发者社区广泛认为这标志着开源大模型正式进入"后发先至"阶段。HuggingFace 上的 V4-Pro 在发布首周即冲上 trending 榜首，业界普遍评价：DeepSeek 正在重写开源的定价游戏规则。同时 V4-Flash 以 13B 激活参数的极致性价比，也在生产部署场景中获得了大量关注。

---

## 2. Kimi K2.6

**发布日期**：2026年04月21日（正式 GA）  
**发布机构**：Moonshot AI（月之暗面）  
**模型类型**：多模态 Agent 模型  
**Hugging Face 主页**：[moonshotai/Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)

### 关键信息

- **模型规模**：1T 总参数 MoE，32B 激活参数，256K token 上下文
- **核心特点**：
  - 支持 300 个子智能体并行运行，每 agent 最多 4,000 步
  - SWE-Bench Pro 得分 58.6%，BrowseComp 得分 83.2%
  - 原生支持图片+视频多模态输入
  - Agent Swarm 能力从 K2.0 的 100 agent 提升至 300 agent
  - 预览版到 GA 仅用 8 天，是 K2 系列最快的上线周期
- **技术基础**：MoE 架构，针对 Agent 编程场景深度优化
- **下载渠道**：HuggingFace（Modified MIT 许可）、Kimi API、Kimi App、Kimi Code CLI、OpenRouter、vLLM / SGLang

### 社区反响

Kimi K2.6 的 Agent Swarm 能力是社区热议的焦点——300 个并行 agent x 4,000 步的执行规模，意味着可以同时探索 300 个不同的代码设计方案并择优执行，这在开源模型中是前所未有的。OpenRouter 和 vLLM 在发布当天即完成集成。不少开发者将 K2.6 与 DeepSeek V4 并称为"本周开源双雄"，前者强于 multi-agent 协作与长程任务编排，后者在单一推理任务中表现极致。

---

## 3. Tencent Hy3 preview

**发布日期**：2026年04月24日  
**发布机构**：腾讯（Tencent）  
**模型类型**：推理+Agent 模型（Mixture-of-Experts）  
**Hugging Face 主页**：[tencent/Hy3-preview](https://huggingface.co/tencent/Hy3-preview)

### 关键信息

- **模型规模**：295B 总参数，21B 激活参数（MoE 架构，192 个专家，每 token 激活 Top-8）
- **核心特点**：
  - 由前 OpenAI 研究员姚顺雨（Yao Shunyu）出任腾讯首席 AI 科学家后主导的首款旗舰模型
  - 在同尺寸模型中拥有领先的推理和 Agent 能力
  - 已集成进腾讯元宝（Yuanbao）和编程助手 CodeBuddy
  - 支持 vLLM、SGLang 等主流推理框架
  - 腾讯重建预训练和强化学习基础设施后的首个重大产出
- **技术基础**：MoE 架构，192 专家，Top-8 激活
- **下载渠道**：HuggingFace、GitHub、ModelScope、GitCode

### 社区反响

Hy3 的发布被业界视为腾讯 AI 战略的转折点。姚顺雨加盟后的首份答卷选择了"效率优先"的务实路线——295B-A21B 的规格在保证推理质量的同时大幅降低了部署门槛。社区对其产品化速度印象深刻：开源当天即完成与腾讯元宝和 CodeBuddy 的集成。部分评论指出 Hy3 在处理长链推理任务上的表现超出了预期，是国产大模型在 Agent 场景中不可忽视的新势力。

---

## 4. Qwen3.6-27B

**发布日期**：2026年04月22日  
**发布机构**：阿里云（Alibaba Cloud / Qwen Team）  
**模型类型**：稠密多模态模型  
**Hugging Face 主页**：[Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)

### 关键信息

- **模型规模**：27B 参数（稠密架构），无 MoE
- **核心特点**：
  - SWE-bench Verified 得分 77.2%，**超越自家 Qwen3.5-397B-A17B**（76.2%）——397B MoE 惨遭 27B 稠密模型碾压
  - 混合 Gated DeltaNet + Gated Attention 架构，64 层
  - 支持文本、图片、视频多模态输入
  - 提供 Thinking 与 Non-thinking 双模式
  - Apache 2.0 许可，可商用
  - 原生支持 OpenClaw、Claude Code、Qwen Code 等编程助手集成
- **技术基础**：密集 Transformer + 创新注意力机制
- **下载渠道**：HuggingFace、ModelScope、阿里云 Model Studio API

### 社区反响

Qwen3.6-27B 是本周期"以小博大"的经典案例。27B 稠密模型在编码基准上碾压自家 397B MoE，验证了架构创新可以比单纯堆参数更有效。社区讨论集中在两个方向：一是稠密架构对硬件部署友好度远超 MoE（单卡可跑 Qwen3.6-27B，而 397B 需要多卡分布式）；二是"一个 27B 模型击败 397B"这一事实引发了关于 MoE 是否被高估的广泛争论。Apache 2.0 许可也受到了开发者社区的一致好评。

---

## 5. LLaDA2.0-Uni

**发布日期**：2026年04月下旬（论文发布于 arXiv）  
**发布机构**：Inclusion AI（AGI 研究中心）  
**模型类型**：统一多模态扩散大语言模型（dLLM）  
**Hugging Face 主页**：[inclusionAI/LLaDA2.0-Uni](https://huggingface.co/inclusionAI/LLaDA2.0-Uni)

### 关键信息

- **模型规模**：16B 参数 MoE，多模态统一
- **核心特点**：
  - 完全基于**离散扩散建模**（Diffusion LLM），彻底摆脱自回归（AR）依赖
  - 单一模型统一支持：文本理解/生成、图片理解/生成
  - 支持任意分辨率、并行解码（非自回归的 key 优势）
  - 语义视觉 Token + 定制 Diffusion Decoder，8 步即可生成高质量图像
  - 在 21 项多模态基准上取得 SOTA
- **技术基础**：离散扩散大语言模型（dLLM）+ MoE，非自回归路径
- **下载渠道**：HuggingFace、GitHub，论文 arXiv:2604.20796

### 社区反响

LLaDA2.0-Uni 引发的讨论比它的知名度更为深远。作为首个将扩散模型成功扩展到多模态 LLM 统一框架的开源工作，它挑战了"大语言模型必须是自回归"的行业共识。非自回归架构的并行解码优势在推理延迟方面具有天然优势，但社区也指出其在超长文本生成任务中与 AR 模型仍有差距。不少 AI 研究者认为，dLLM 路线可能是下一代基础模型架构的重要方向之一，尤其适合需要高吞吐量和低延迟的生产场景。

---

## 总结与趋势观察

1. **开源模型正式进入"后发先至"时代**：DeepSeek V4-Pro 以开源权重在编码基准上与 Claude Opus 4.6 正面抗衡，且推理成本仅为 1/7。开源不再是"便宜但不强"的代名词，"最强"和"最便宜"两个标签第一次被同一个模型同时摘走。

2. **"小型高效"与"巨型 MoE"两条路线并行爆发**：本周既是 DeepSeek V4-Pro（1.6T）、Kimi K2.6（1T）等巨型 MoE 模型的盛宴，也是 Qwen3.6-27B（27B 稠密）和 LLaDA2.0-Uni（16B MoE）等高效小模型的舞台。开发者不再盲目追求大参数，而是根据部署场景灵活选择——这是生态成熟的标志。

3. **Agent 能力成为模型竞争的新主战场**：Kimi K2.6 的 300 智能体并行刷新了开源 Agent 能力的上限；DeepSeek V4-Pro 的三种推理模式（Non-think / Think High / Think Max）直接将 Agent 工作流深度嵌入模型设计；腾讯 Hy3 从架构层面强调 Agent 实用性。纯粹的对话能力已无法定义模型优劣，"能否自主完成复杂任务"才是新一代模型的标尺。

4. **非自回归架构的崛起信号**：LLaDA2.0-Uni 证明扩散模型可以统一多模态理解与生成。虽然目前仍处于早期探索阶段，但这可能是对自回归架构统治地位的最有力挑战之一。未来半年，dLLM 路线的进展值得密切关注。

---

## 参考资料

1. DeepSeek-V4 Technical Report (HuggingFace PDF) — 2026年4月24日
2. Kimi K2.6 官方发布公告 — kimi-k2.org, 2026年4月21日
3. 腾讯 Hy3 preview 官方公告 — tencent.com, 2026年4月24日
4. Qwen3.6-27B 官方博客 — qwen.ai, 2026年4月22日
5. LLaDA2.0-Uni 论文 (arXiv:2604.20796) — Inclusion AI, 2026年4月
6. HuggingFace Trending Models — huggingface.co/models, 2026年5月3日
7. 综合报道：DeepSeek V4 Pro Review (buildfastwithai.com)、Kimi K2.6 深度解读 (CSDN)、Hy3 技术解读 (CSDN)

---

*本报道由 OpenClaw 自动生成，数据截至 2026-05-03。*
