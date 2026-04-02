---
title: "Claude Code 源码泄露：事件始末、隐藏功能与行业影响"
date: 2026-04-02
author: AI 极客早报
tags:
  - Claude
  - Anthropic
  - AI工具
  - 安全事件
---

# Claude Code 源码泄露：事件始末、隐藏功能与行业影响

## 📅 事件时间线

| 时间 | 事件 |
|------|------|
| 2026年3月31日 | Claude Code npm 包中的 source map 文件意外暴露，TypeScript 源码可公开下载 |
| 2026年4月1日 | 安全研究员 @Fried_rice（Chaofan Shou）率先在 X 上披露此事 |
| 2026年4月2日 | GitHub 镜像仓库出现，开发者社区开始深度分析代码 |

## 🔓 事件始末

### 泄露原因

Anthropic 在发布 Claude Code CLI 工具至 npm  registry 时，附带的 `.map` source map 文件直接指向了 Anthropic 私有 R2 存储桶中的原始 TypeScript 源码。这意味着任何人只需下载 npm 包并解析 map 文件，就能获取**未经混淆的完整源代码**。

这不是一次黑客攻击，而是发布流程中的**供应链暴露（supply-chain exposure）**。

### 泄露规模

- **文件数量**：~1,900 个 TypeScript 文件
- **代码规模**：超过 **512,000 行**代码
- **语言**：TypeScript（strict 模式）
- **运行时**：Bun
- **终端 UI**：React + Ink
- **代码架构**：高度模块化，工具系统、命令系统、bridge 系统分离

### 谁发现了？

@Fried_rice（Chaofan Shou）于 2026年3月31日在 X 上公开了这一发现。他指出：*"Claude code source code has been leaked via a map file in their npm registry!"*

随后，GitHub 用户 **zackautocracy** 建立了一个镜像仓库，声明用于"教育、防守性安全研究和软件供应链分析"，明确表示不声称对原始代码拥有所有权，仅供研究用途。

## 🔍 泄露揭示的隐藏功能

开发者深度分析代码后发现，Claude Code 远不止是一个"API 包装器"，它包含大量**未启用、被注释或隐藏的功能**。

### Kairos — 持久化后台守护进程 ⭐

最引人关注的功能是一个代号 **Kairos** 的持久化守护进程。代码注释显示，这套系统可以在**关闭 Claude Code 终端窗口后继续在后台运行**。

工作原理：
- 系统使用周期性的 `<tick>` 提示定期检查是否需要新操作
- 支持 `PROACTIVE` 标志，主动向用户推送"用户未询问但需要立即看到"的信息
- 依赖文件式记忆系统，实现跨会话持久化

官方注释（被 KAIROS 标志禁用）描述了设计目标：

> "让系统对用户有完整的了解——用户希望如何与 AI 协作、需要避免哪些行为、工作背景是什么"

### AutoDream — 梦境记忆整理

当用户空闲或手动触发"睡眠"时，Claude Code 内的 **AutoDream** 系统会启动一段"AI 梦境"过程：

> "你正在执行一个梦境——对你的记忆文件进行反思性扫描"

这个过程会：
1. 扫描当日对话记录，提取"值得持久化的新信息"
2. 整合记忆，避免"近似重复"和"矛盾"
3. 修剪过于冗长或已过时的记忆
4. 标记"已偏移的既有记忆"（这个问题在给 AI 系统嫁接记忆功能时普遍存在）

### Buddy — 虚拟助手伴侣

代码中发现了 **Buddy** 模块的引用，描述为"伴侣精灵"（Companion Sprite），功能尚不明确，但显然是面向用户陪伴方向的探索。

### Undercover — 隐身模式

一个被注释掉的 **Undercover** 模式，允许 Claude Code 以更隐蔽的方式运行。

### IDE Bridge — 深度 IDE 集成

Claude Code 内置了连接 VS Code 和 JetBrains 扩展的桥接系统：
- 使用 JWT 做身份验证
- 支持从 IDE 向 CLI 发送消息
- 会话管理、权限回调完整实现

### Plugin System — 插件架构

一套完整的插件加载系统，支持第三方扩展 Claude Code 的能力。

### 架构亮点

Claude Code 被开发者描述为"**生产级开发者体验，而非简单的 API 包装**"：
- 约 40,000 行代码用于插件式工具系统
- 约 46,000 行代码用于查询系统
- 内置 50+ 个 slash 命令
- 40+ 个 Agent 工具（全部自包含，每个定义输入模式、权限模型、执行逻辑）
- 完整的 GrowthBook 功能开关和 Analytics 系统

## ⚠️ 行业影响

### 安全研究价值

512,000 行源码为安全社区提供了一份**前所未有的解剖样本**。可以研究：
- Anthropic 如何设计 guardrail 和权限系统
- Agent 工具调用的架构设计
- 记忆系统和持久化的实现方式

### 竞争情报

竞争对手可以：
- 了解 Anthropic 的技术路线图
- 参考其架构设计优化自己的工具
- 识别 Anthropic 尚未解决的问题和差距

### 安全风险

**坏消息**：攻击者现在有了精确的路线图来研究如何绕过 Anthropic 的安全 guardrail。这在"Computer Use"（让 AI 控制计算机）赛道日益重要的背景下，格外值得警惕。

### 法律层面

虽然 Anthropic 的商业机密受法律保护，但架构洞察不受版权保护。Anthropic 可以发出 DMCA 删除镜像仓库，但代码已经在网上传播，无法完全撤回。

## 🤔 业内怎么看

开发者社区反应复杂：

- **震惊**：Claude Code 的工程量远超预期，"既令人鼓舞又令人谦卑"
- **兴奋**：终于可以深入了解顶级 AI Agent 的工程实践
- **担忧**：guardrail 绕过研究可能带来安全风险
- **反思**：这次泄露再次提醒整个行业——**发布流程中的每一个环节都需要安全审计**

## 📚 参考链接

- [Ars Technica 首发报道](https://arstechnica.com/ai/2026/03/entire-claude-code-cli-source-code-leaks-thanks-to-exposed-map-file/)
- [Ars Technica 深度分析：泄露揭示的隐藏功能](https://arstechnica.com/ai/2026/04/heres-what-that-claude-code-source-leak-reveals-about-anthropics-plans/)
- [GitHub 镜像仓库（zackautocracy）](https://github.com/zackautocracy/claude-code)
- [@Fried_rice 原帖](https://x.com/Fried_rice/status/2038894956459290963)

---

*本文由 AI 极客早报整理，仅供参考。*
