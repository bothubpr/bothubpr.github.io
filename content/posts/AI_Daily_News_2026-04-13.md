---
title: "极客早报 | 2026-04-13"
date: "2026-04-13"
slug: "ai-daily-news-2026-04-13"
tags: ["AI", "Daily News", "Tech"]
---

早上好，各位极客们。今天是 2026 年 4 月 13 日，星期一，欢迎收听今天的极客早报。本期，我们将关注 Sam Altman 正面回应《New Yorker》争议报道、加州居民集体起诉 AI 医疗转录工具 Abridge 事件，以及 AI 安全评估体系遭质疑等重要议题。

---

### Sam Altman 回应《New Yorker》争议文章，称其「煽动性」且与住所遭袭事件相关

上周，OpenAI CEO Sam Altman 罕见地在官方博客发布长文，首次正面回应《New Yorker》对其诚信问题的深度质疑报道。他措辞激烈地批评该文「煽动性十足」，并罕见地将矛头指向此前其住所遭袭事件，暗示两者存在关联。这篇争议文章由知名调查记者执笔，深入剖析了 Altman 在 OpenAI 治理结构中的角色、股权安排，以及公司安全问题处理方式。值得关注的是，Altman 此前在公开场合一贯以冷静、职业的形象示人，此次主动将暴力袭击与媒体报道挂钩，在 AI 行业领袖中极为罕见。AI 行业观察者指出，随着 OpenAI 估值超过 1500 亿美元，公众对 AI 安全和公司治理的关注已与日俱增，Altman 的个人形象管理正成为整个行业的风向标。

来源：[TechCrunch](https://techcrunch.com/2026/04/11/sam-altman-responds-to-incendiary-new-yorker-article-after-attack-on-his-home/)

---

### 小型 AI 模型同样发现 Mythos 识别的高危漏洞，AI 安全基准遭质疑

AI 安全公司 Aisle 发布重磅研究，打破了「只有最大最强模型才能发现关键漏洞」的行业假设。研究团队选取了多个小型开源模型与 Anthropic 高调限制发布的 Mythos 模型进行对比测试，结果令人震惊：小模型同样能识别出 Mythos 标注的所有高危漏洞。Aisle 创始人表示，这一发现揭示了当前 AI 安全评估体系的深层结构问题——行业过度关注模型规模与能力排行榜，而忽视了漏洞发现能力与推理过程的本质联系。研究同时发现，不同模型在漏洞识别上呈现明显的「参差不齐的前沿」（jagged frontier）特征，即在同一模型内，某些任务表现卓越而相邻任务却完全失败。该研究已在 Aisle 官方博客发布，随即在 HN 引发 822 分热议，成为本周最具讨论度的 AI 安全话题。

来源：[Aisle Blog](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier)

---

### 加州居民起诉 AI 问诊录音工具 Abridge：未经同意录制医患对话

多名加州居民对医疗机构 Sutter Health 和 MemorialCare 提起集体诉讼，指控 AI 转录工具 Abridge 在患者未明确同意的情况下自动录制医患对话，并将音频数据传输至院外服务器。诉讼文件显示，Abridge 的转录功能在患者不知情状态下全程开启，录制的医患沟通内容随后被用于模型训练和商业目的。原告律师援引 HIPAA（健康保险便携性和责任法案）及加州 CMIA（医疗信息保密法）指出，未经患者同意录制并传输敏感医疗对话构成严重违法。Abridge 则辩称其产品已获得医疗机构授权，符合行业常规。目前，该案已引发医疗 AI 监管的热烈讨论，隐私权益组织呼吁 FDA 和联邦贸易委员会（FTC）介入调查 AI 医疗工具的数据合规性。

来源：[Ars Technica](https://arstechnica.com/tech-policy/2026/04/californians-sue-over-ai-tool-that-records-doctor-visits/)

---

### Nvidia 投资的 SiFive 估值达 36.5 亿美元，押注开源 RISC-V AI 芯片

RISC-V 架构芯片设计公司 SiFive 宣布完成新一轮融资，估值跃升至 36.5 亿美元，投资方包括 Nvidia 等知名机构。SiFive 是全球领先的 RISC-V（Reduced Instruction Set Computer – Five）处理器 IP 供应商，与传统 x86 和 ARM 架构不同，RISC-V 采用完全开源的指令集架构（ISA, Instruction Set Architecture），任何公司和个人均可自由设计、制造和销售基于 RISC-V 的芯片，无需支付专利授权费用。SiFive 本轮融资明确表示将加速 AI 推理芯片的产品化，目标是在数据中心和边缘计算场景中提供低功耗、高能效的 AI 推理加速方案。此举被视为直接挑战 Nvidia 在 AI 芯片市场的主导地位，同时为芯片国产化浪潮中的各国厂商提供替代选择。

来源：[TechCrunch](https://techcrunch.com/2026/04/11/nvidia-backed-sifive-hits-3-65-billion-valuation-for-open-ai-chips/)

---

### AI 模型预测足球比赛结果普遍失误，xAI Grok 表现最差

AI 初创公司 General Reasoning 发布 KellyBench 报告，系统性测试了 Google Gemini、OpenAI GPT 系列、Anthropic Claude 和 xAI Grok 等主流模型对 2023-24 英超联赛 380 场比赛的投注预测能力。测试采用严格的 Kelly Criterion（凯利准则）进行资金管理，模拟真实投注场景。结果令人失望：所有测试模型在完整赛季中均录得净亏损，无一盈利。其中 xAI Grok 表现最差，亏损幅度高达 41%；Google Gemini 亏损最少，但仍达到 12%。报告分析指出，足球比赛结果受球员心理、裁判判罚、天气、伤病等大量非结构化因素影响，AI 模型在捕捉这类长周期、非量化信息方面存在明显短板。值得注意的是，即便引入实时新闻和赔率数据，模型表现也无显著提升，再次印证了 AI 在真实世界长周期分析中的固有局限。

来源：[Ars Technica](https://arstechnica.com/ai/2026/04/ai-models-are-terrible-at-betting-on-soccer-especially-xai-grok/)

---

### Cirrus Labs 宣布加入 OpenAI，瞄准 AI Agent 开发工具链整合

知名 CI/CD（持续集成/持续部署）平台 Cirrus Labs 高调宣布将加入 OpenAI，成为后者扩展 AI Agent（AI 智能体）生态战略的关键一环。Cirrus Labs 以其快速、可扩展的云端持续集成服务著称，长期为开源项目和大型软件开发团队提供自动化构建与测试支持。此次整合后，Cirrus Labs 的自动化工具链将与 OpenAI 的 Agent 开发框架（Agent SDK 和 Agents）深度融合，为开发者提供从代码开发、测试到 AI 推理部署的一站式体验。OpenAI 近期明显加大在 Agent 工具链的投入，此前已收购多家开发工具公司，目标是打造完整的 AI Native（AI 原生）开发平台。行业观察者认为，Cirrus Labs 的加入将补齐 OpenAI 在 CI/CD 环节的空白，使开发者能在单一平台内完成 AI Agent 的全生命周期管理。

来源：[HN / Cirrus Labs](https://cirruslabs.org/)

---

### 原子级存储重大突破：零保留能耗下实现 447 TB/cm² 存储密度

一支跨机构研究团队在氟化石墨烯（fluorographene）材料上实现原子级存储的重大突破，实验数据显示存储密度高达 447 TB/cm²，且数据写入后无需额外能耗即可保留数据，彻底解决了传统 DRAM（Dynamic Random Access Memory）断电即失的痛点。这一密度意味着理论上只需指甲盖大小的存储介质，即可容纳相当于 125 部高清电影（约 125TB）的数据量。更为关键的是，氟化石墨烯存储器的写入过程不涉及相变或化学反应，而是通过改变材料表面电子分布实现数据写入，写入速度据报道可达纳秒级。该研究已发表在开放科学平台 Zenodo，所有原始实验数据和材料配方均向公众开放。研究团队表示，尽管距离商业化仍有工程化难题待解，但这一突破为 MRAM（Magnetoresistive Random Access Memory）、ReRAM（Resistive Random Access Memory）等下一代非易失性存储器开辟了全新路径。

来源：[Zenodo](https://zenodo.org/records/19513269)

---

### APL 编程语言源代码正式开源：计算机历史珍藏重现

计算机历史博物馆（Computer History Museum）正式开源了 APL（Array Programming Language）编程语言早期版本的完整源代码（2012 年整理版），为全球开发者打开了一扇了解计算机编程历史的窗口。APL 由 Kenneth Iverson 于 1960 年代在 IBM 发明，以其独特的数学符号语法和强大的数组处理能力闻名，创立了独具一格的数组编程（Array Programming）范式。APL 的符号系统突破了传统键盘字符限制，曾需要专用物理键盘才能输入，这也使其成为编程语言史上最具辨识度也最「异类」的存在。该语言在金融工程（尤其是量化交易）和科学计算领域有重要影响，MATLAB 和 NumPy 等现代工具的数组操作概念均可追溯到 APL。源码开源后，开发者可以在 GitHub 上浏览这一计算机历史瑰宝的原始实现，甚至尝试在现代硬件上复现这一经典语言。

来源：[Computer History Museum](https://computerhistory.org/blog/the-apl-programming-language-source-code/)

---

### 保持 Postgres 队列健康的实战经验：锁竞争与 VACUUM 调优

PlanetScale 工程师 Kuan-Ting Chen 在官方博客分享了维护高吞吐 Postgres（PostgreSQL）消息队列的生产级实战经验，重点剖析了轻量级锁（lightweight lock）竞争、VACUUM 参数调优以及队列性能的权衡取舍等核心问题。在大规模 OLTP（Online Transaction Processing）场景中，数据库队列常因并发写入产生大量死元组（dead tuples），若不及时清理，不仅会拖慢查询速度，还会造成表膨胀（bloat）。文章深入解析了 VACUUM 的 autovacuum_vacuum_cost_delay、autovacuum_vacuum_scale_factor 等关键参数的调优思路，以及如何通过 pg_stat_activity 和 pg_stat_bgwriter 等系统视图实时监控锁等待事件。工程师还分享了一个易被忽视的陷阱：当队列消费者故障未能及时清理时，积压的消息会持续产生死元组，一旦表膨胀到某个临界点，即便重启 autovacuum 也需要数小时才能完成清理，对线上服务造成严重影响。该文为运维团队提供了可直接落地的优化方案。

来源：[PlanetScale](https://planetscale.com/blog/keeping-a-postgres-queue-healthy)

---

### Kalshi 赢得亚利桑那州刑事案件临时禁令，CFTC 监管权再获确认

预测市场平台 Kalshi 宣布赢得联邦法院临时限制令（Temporary Restraining Order），成功暂停亚利桑那州对其发起的刑事诉讼程序。此前，亚利桑那州检察官指控 Kalshi 允许用户对现实事件结果进行金融押注，涉嫌违反州级反赌博法规。联邦法院在裁决中认可了 Kalshi 的核心抗辩：该平台运营的预测市场属于 CFTC（商品期货交易委员会，Commodity Futures Trading Commission）监管的合法金融工具范畴，而非非法赌博。CFTC 此前已明确将预测市场纳入其管辖权，并发表声明支持 Kalshi 平台。法律专家指出，该案结果将直接影响美国预测市场行业的监管格局；若 Kalshi 最终胜诉，各州将难以再以刑事手段干预 CFTC 授权的预测市场平台。目前，Kalshi 的市场活跃度和用户注册量已因此案出现明显波动，投资者密切关注后续进展。

来源：[TechCrunch](https://techcrunch.com/2026/04/11/kalshi-wins-temporary-pause-in-arizona-criminal-case/)

---

本周的极客早报围绕两条主线展开：AI 行业的责任与边界争议，以及芯片市场的格局重塑。Sam Altman 首次将暴力袭击与媒体监督挂钩，Altman 的形象危机折射出 AI 行业领袖在聚光灯下的深层焦虑；与此同时，Abridge 面临的集体诉讼揭示了 AI 医疗工具在高速商业化进程中隐私合规的严峻挑战。Aisle 的研究打破了「模型越大越安全」的迷思，SiFive 36.5 亿美元的高估值印证了 RISC-V 开源芯片浪潮的商业潜力，而 Kalshi 赢得 CFTC 案件则为预测市场的合法化路径注入一针强心剂。技术层面，Cirrus Labs 加入 OpenAI 吹响了 AI Agent 工具链整合的号角，原子级存储密度的突破让我们窥见了后硅时代存储技术的曙光，但 AI 模型在足球预测上的集体失手也在提醒我们：现实世界的复杂性仍是当前 AI 最大的盲区。好了，以上就是今天极客早报的全部内容，如果这些内容对你有帮助，欢迎转发给身边的朋友。我是 ziv，我们明天见。

---

### 首席架构师的深度阅读指南

本期最值得深入阅读的三篇文章推荐：

1. **[Aisle 研究：Mythos 之后的 AI 网络安全 — Aisle Blog](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier)**：Aisle 揭示了 AI 安全评估体系的深层结构问题，"参差不齐的前沿"概念对所有 AI 安全从业者都有重要启发意义。

2. **[APL 编程语言源代码正式开源 — Computer History Museum](https://computerhistory.org/blog/the-apl-programming-language-source-code/)**：计算机历史的珍贵档案开源，数组编程范式对理解现代数据处理工具的演化脉络极有价值。

3. **[原子级存储突破：447 TB/cm² 密度 — Zenodo](https://zenodo.org/records/19513269)**：实验数据完全开放，可复现性强，是研究新型非易失性存储器不可多得的原始文献。

---

*「极客早报」每日更新，订阅地址：your-blog-url*
