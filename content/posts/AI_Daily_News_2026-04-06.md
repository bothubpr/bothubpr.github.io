---
title: "极客早报 | 2026年4月6日"
date: 2026-04-06T08:00:00+08:00
lastmod: 2026-04-06T08:00:00+08:00
description: "每日科技新闻极客早报，涵盖 OpenAI Codex 定价调整、Anthropic 收购生物科技公司、日本 Physical AI 落地、SpaceX 轨道数据中心、Rust 尾调用解释器等热点话题。"
slug: "ai-daily-news-2026-04-06"
tags: ["极客早报", "AI", "科技新闻", "日报"]
categories: ["科技"]
author: "极客早报"
excerpt: "今日科技新闻速览：OpenAI Codex 定价重大调整、Rust 尾调用解释器亮相、SpaceX 轨道数据中心愿景、日本 Physical AI 规模化部署。"
---

# 极客早报 | 2026年4月6日，星期一

> 清晨八点，准时送达。今天的新闻有点猛——OpenAI 改了 Codex 的收费模式，Anthropic 收购了生物科技公司，Sony 悄悄涨了 PS5 的价格，还有个 Rust 的尾调用解释器很有意思。

---

## OpenAI Codex 改用 Token 用量计费，开发者社区热议

**来源：[HN](https://help.openai.com/en/articles/20001106-codex-rate-card)** | **热度：170+ points，120+ 评论**

OpenAI 今日宣布 Codex 定价模型重大调整：由原来的**按消息计费**改为**按 API Token 用量计费**。这一转变意味着开发者可以根据实际处理的 token 数量精确付费，而非按请求次数付固定费用。

社区反应热烈。大量开发者认为按 token 计费更公平，尤其是处理长文档或复杂代码分析时；对于短小请求较多的场景，则担心费用反而上升。120 多条评论中，主流声音是"终于不用为每个 API 调用多付钱了"，但也有人提醒：实际费用还需等官方费率表出炉才能下定论。

**阅读原文：[OpenAI Codex Rate Card](https://help.openai.com/en/articles/20001106-codex-rate-card)**

---

## Anthropic 收购 Coefficient Bio：AI + 生物科技赛道再添重磅交易

**来源：[TechCrunch](https://techcrunch.com/2026/04/03/anthropic-buys-biotech-startup-coefficient-bio-in-400m-deal-reports/)** | **热度：首日报道**

Anthropic 宣布以**4 亿美元**股票交易收购生物科技 AI 创业公司 Coefficient Bio。这是 Claude 开发商迄今为止规模最大的并购交易，标志着 AI + 生物医药领域正式成为头部公司的战略重心。

Coefficient Bio 此前一直保持神秘，专注于将大语言模型用于药物发现流程。消息人士透露，其平台能大幅缩短蛋白质结构预测和候选分子筛选的时间。Anthropic 方面表示，交易完成后 Coefficient Bio 将保持独立运营。

**阅读原文：[Anthropic buys biotech startup Coefficient Bio](https://techcrunch.com/2026/04/03/anthropic-buys-biotech-startup-coefficient-bio-in-400m-deal-reports/)**

---

## Claude Code 订阅用户使用 OpenClaw 等第三方工具需额外付费

**来源：[TechCrunch](https://techcrunch.com/2026/04/04/anthropic-says-claude-code-subscribers-will-need-to-pay-extra-for-openclaw-support/)** | **热度：持续发酵**

Anthropic 向 Claude Code 订阅者发出通知：通过 OpenClaw 等第三方工具使用 Claude Code 将产生**额外费用**，原有订阅不再包含此类集成使用方式。

这一消息在开发者社区引发广泛关注。OpenClaw 作为知名 AI 编程辅助工具，拥有大量活跃用户。有分析认为 Anthropic 此举意在规范第三方生态、避免收入分流；但也有开发者担心这会促使部分用户流向价格更透明的竞品。Anthropic 尚未公布具体费率细节。

**阅读原文：[Claude Code subscribers need to pay extra for OpenClaw](https://techcrunch.com/2026/04/04/anthropic-says-claude-code-subscribers-will-need-to-pay-extra-for-openclaw-support/)**

---

## 日本推进 Physical AI：从试点项目到真实世界规模化部署

**来源：[TechCrunch](https://techcrunch.com/2026/04/05/japan-is-proving-experimental-physical-ai-is-ready-for-the-real-world/)** | **热度：首日报道**

受国内严重劳动力短缺驱动，日本正在将 Physical AI（物理 AI）从试点项目**大规模推向真实部署场景**。工业机器人在制造业流水线上早已不稀奇，但现在服务业也开始跟进——酒店、餐饮、物流仓储等场景正在快速引入 AI 驱动的物理机器人。

报道称，日本多家大型企业已与 AI 机器人公司签订数千台部署合同，部分工厂的自动化率预计在三年内从当前的 30% 提升至 70%。这不仅是 AI 软件的胜利，更代表了机器人硬件产业链的成熟。

**阅读原文：[Japan is proving experimental Physical AI is ready for the real world](https://techcrunch.com/2026/04/05/japan-is-proving-experimental-physical-ai-is-ready-for-the-real-world/)**

---

## 轨数据数据中心能否撑起 SpaceX 天价估值？

**来源：[TechCrunch](https://techcrunch.com/2026/04/05/can-orbital-data-centers-help-justify-a-massive-valuation-for-spacex/)** | **TechCrunch Equity 播客**

Elon Musk 日前提出的**轨道数据中心**愿景正在引发热议。TechCrunch Equity 播客本期节目深入探讨：这个听起来像科幻的点子，究竟是 SpaceX 高估值的真实支撑，还是一场精心包装的叙事？

支持者认为轨道数据中心可规避地面自然灾害和地缘政治风险，且 SpaceX 已有成熟发射能力；批评者则指出轨道环境的辐射问题、冷却难题和维护成本远超地面数据中心。节目结论是：愿景诱人，但十年内难见规模落地。

**阅读原文：[Can orbital data centers help justify a massive valuation for SpaceX?](https://techcrunch.com/2026/04/05/can-orbital-data-centers-help-justify-a-massive-valuation-for-spacex/)**

---

## LibreOffice 官方澄清：关于未来的所有猜测到此为止

**来源：[HN](https://blog.documentfoundation.org/blog/2026/04/05/lets-put-an-end-to-the-speculation/)** | **热度：74 points**

The Document Foundation 官方博客今日发文，正式回应社区近期关于 LibreOffice 未来的种种猜测，澄清项目路线图及治理结构。

近期社区流传多个版本的说法，包括项目可能合并、商业版本与社区版本分裂等。官方博客明确表示：LibreOffice 将维持开源治理模式，社区版本不会消失，但会加强与大型企业赞助商的合作以保障长期资金支持。

**阅读原文：[Let's put an end to the speculation](https://blog.documentfoundation.org/blog/2026/04/05/lets-put-an-end-to-the-speculation/)**

---

## Rust (nightly) 尾调用解释器实现：类型系统探索函数式编程

**来源：[HN](https://www.mattkeeter.com/blog/2026-04-05-tailcall/)** | **热度：74 points**

开发者 Matt Keeter 在 Rust nightly 版本中实现了一个**尾调用（tail-call）解释器**，探索 Rust 类型系统对函数式编程范式的原生支持。

尾调用优化是 Scheme 等函数式语言的重要特性，允许递归调用在不增加调用栈的情况下执行。Keeter 的实现巧妙利用了 Rust 的生命周期和类型系统，在安全性和性能之间取得了有趣平衡。该项目已开源，引发 Rust 社区对函数式编程特性的新一轮讨论。

**阅读原文：[Tail-call interpreter in Rust nightly](https://www.mattkeeter.com/blog/2026-04-05-tailcall/)**

---

## 特朗普提议大幅削减 NASA 预算 23%，恰逢宇航员登月任务进行中

**来源：[Ars Technica](https://arstechnica.com/space/2026/04/trump-proposes-steep-cut-to-nasa-budget-as-astronauts-head-for-the-moon/)** | **热度：持续关注**

Artemis II 发射两天后，白宫发布 2027 财年预算蓝图，计划将 NASA 预算**削减 23%**。削减重点包括科学任务部门和未来月球、火星探索计划拨款。

此次削减正值 4 名宇航员执飞 50 多年来首次载人登月任务期间，引发"预算削减时机不当"的广泛批评。国会方面，预计将再次否决类似提案——与去年情况相似。NASA 局长尚未发表评论。

**阅读原文：[Trump proposes steep cut to NASA budget as astronauts head for the moon](https://arstechnica.com/space/2026/04/trump-proposes-steep-cut-to-nasa-budget-as-astronauts-head-for-the-moon/)**

---

## 美国 CBP 设施代码疑因在线闪卡服务 Quizlet 泄露

**来源：[Ars Technica](https://arstechnica.com/security/2026/04/cbp-facility-codes-sure-seem-to-have-leaked-via-online-flashcards/)** | **来源：[WIRED](https://www.wired.com)** | **热度：安全事件关注中**

WIRED 调查发现，Quizlet 上的一份**公开闪卡集**疑似暴露了美国 CBP（海关与边境保护局）设施的门禁安全信息，包括部分设施代码和进入程序的描述。

CBP 已启动审查，初步评估认为泄露内容对设施安全构成潜在风险。Quizlet 方面表示正在配合调查，并已移除相关闪卡集。专家警告：即便是看似无害的闪卡内容，恶意行为者也可通过汇总大量公开信息还原敏感安全数据。

**阅读原文：[CBP facility codes seem to have leaked via online flashcards](https://arstechnica.com/security/2026/04/cbp-facility-codes-sure-seem-to-have-leaked-via-online-flashcards/)**

---

## Suno AI 版权过滤器漏洞：轻松生成疑似侵权音乐

**来源：[The Verge](https://www.theverge.com/ai-artificial-intelligence/906896/sunos-copyright-ai-music-covers)** | **热度：版权争议持续**

AI 音乐平台 Suno 声称拥有强大的版权识别过滤机制，但实际极容易被绕过。测试显示，通过简单的提示词调整，即可生成与 Beyoncé、Black Sabbath 等热门歌曲**高度相似的 AI 模仿版本**。

这一发现引发音乐版权争议。唱片公司已开始关注此事，部分艺术家公开批评 Suno 的版权保护承诺缺乏技术支撑。Suno 回应称已加强过滤模型，但拒绝透露具体技术细节。

**阅读原文：[Suno's copyright filter is apparently easy to bypass](https://www.theverge.com/ai-artificial-intelligence/906896/sunos-copyright-ai-music-covers)**

---

## Meta 暂停与 Mercor 合作：数据泄露危及 AI 行业机密

**来源：[Wired](https://www.wired.com/story/meta-pauses-work-with-mercer-after-data-breach-puts-ai-industry-secrets-at-risk/)** | **热度：数据安全持续发酵**

Mercor 数据泄露事件影响持续扩大，继 OpenAI、Anthropic 等主要 AI 实验室之后，Meta 也宣布**暂停与 Mercor 的合作**。泄露数据涉及关键 AI 训练数据来源，引发行业对数据供应链安全的深度担忧。

据 Wired 报道，Mercor 平台的安全漏洞导致大量内部通信和训练数据外泄，受影响公司数量可能远超此前披露。安全研究人员称此次泄露为"2026 年 AI 行业最严重的数据安全事件"。

**阅读原文：[Meta pauses work with Mercor after data breach](https://www.wired.com/story/meta-pauses-work-with-mercer-after-data-breach-puts-ai-industry-secrets-at-risk/)**

---

## 索尼 PS5 涨价：游戏主机世代远未结束，延续可能是好事

**来源：[Wired](https://www.wired.com/story/sonys-ps5-price-hikes-prove-this-console-generation-is-far-from-over-good/)** | **热度：行业观察**

索尼对 PS5 实施涨价策略，多个市场的官方零售价上调 10%-15%。与此同时，任天堂 Switch 2 的发布时间持续推迟，暗示**当前主机世代将比预期更长**。

行业分析师认为，主机世代延长对玩家未必是坏事：硬件迭代放缓意味着游戏开发商有更多时间针对同一硬件平台优化体验，PS5 的游戏阵容在涨价后反而可能更有保障。索尼股价在消息发布后小幅上涨，市场似乎认可这一策略。

**阅读原文：[Sony's PS5 price hikes prove this console generation is far from over](https://www.wired.com/story/sonys-ps5-price-hikes-prove-this-console-generation-is-far-from-over-good/)**

---

## 首席架构师的深度阅读指南

今天的新闻覆盖了 AI 定价、收购、监管、数据安全、硬件和开源软件等多个领域。值得关注的是：

- **Anthropic 连续两天出现在头条**，先是收购生物科技公司，后是 Claude Code 收费模式调整，动作频频
- **SpaceX 轨道数据中心**概念值得持续跟踪——这是 Elon Musk 多元化叙事的一部分，还是有技术可行性的长远规划？
- **日本 Physical AI** 是今天最容易被忽视但实际上影响最深远的一条，传统工业自动化的 AI 化正在加速

---

*本报道由极客早报整理发布，每日早 8 点更新。新闻来源：HN、TechCrunch、Ars Technica、The Verge、Wired*
