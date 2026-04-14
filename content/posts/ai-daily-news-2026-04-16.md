---
title: "极客早报 | 2026-04-16"
date: "2026-04-16"
slug: "ai-daily-news-2026-04-16"
tags: ["AI", "Daily News", "Tech"]
---

早上好，各位极客们。今天是 2026 年 4 月 16 日，星期四，欢迎收听今天的极客早报。

WordPress 插件后门风波持续发酵，伦敦 Robotaxi 测试启动预示自动驾驶全球化进入新阶段，脑机接口公司 Science Corp. 即将迈出人体植入第一步——今天的极客早报，精彩纷呈。

---

### 黑客在数十个 WordPress 插件中植入后门，影响数千网站

WordPress（全球最流行的开源内容管理系统，CMS）生态再遭供应链攻击。安全研究人员发现，数十个 WordPress 插件被劫持后推送恶意更新，攻击者通过购买插件所有权植入后门代码，再通过自动更新机制分发至所有安装该插件的网站，受影响网站数以千计。

这一攻击的核心逻辑并不复杂：攻击者找到拥有大量用户但维护者安全意识薄弱的插件，通过购买或漏洞接管其发布权，随后的恶意更新通过 WordPress 的自动更新机制静默推送至所有网站。对于启用了插件自动更新的站点，恶意代码在毫无察觉的情况下完成注入。后门通常表现为隐藏的管理员账户或恶意重定向，用于窃取流量或进一步横向渗透。

这起事件的本质是信任链的滥用——WordPress 插件生态的开放性是其最大优势，也成为最薄弱的一环。插件开发者与站点管理员之间的信任关系，被攻击者精准利用。从 SolarWinds 到现在，供应链攻击一次次证明：安全链条的强度取决于最薄弱的一环。

来源：[TechCrunch](https://techcrunch.com/2026/04/14/someone-planted-backdoors-in-dozens-of-wordpress-plugins-used-in-thousands-of-websites/)

---

### AI 数据中心创业公司 Fluidstack 正洽谈 10 亿美元融资，估值 180 亿美元

AI 基础设施赛道再现超级吸金选手。Fluidstack 正在洽谈新一轮 10 亿美元融资，估值高达 180 亿美元，距离其拿下为 Anthropic 构建价值 500 亿美元数据中心的合同仅仅数月之隔。

Fluidstack 的崛起路径颇具代表性：抓住大厂 AI 算力需求爆发的窗口期，通过拿下头部 AI 公司的基础设施订单快速放大估值。这套打法在云计算时代并不罕见——CoreWeave（加密货币挖矿转型的 GPU 云服务商）已经验证过类似路径。但 Fluidstack 的估值倍数已经远超 CoreWeave 当年的水平。

值得关注的是，180 亿美元的估值背后是尚未被验证的商业模式复制能力。AI 数据中心建设的确定性在于需求，不确定性在于：这些创业公司能否在 GPU 资源稀缺性缓解后依然保持竞争力。当推理（Inference）成本大幅下降，云厂商自建比例上升，这些中间层玩家的生存空间将面临真实考验。

来源：[TechCrunch](https://techcrunch.com/2026/04/14/ai-datacenter-startup-fluidstack-in-talks-for-1b-round-at-18b-valuation-months-after-hitting-7-5b-says-report/)

---

### Flock 被开发者指控运营「国内间谍计划」，隐私倡导者联名致信要求退出

企业设备追踪平台 Flock 正面临来自开发者社区的强烈质疑。一名开发者在联系 Flock 隐私联系人请求删除公司数据后，公开了对方的回复内容，引发 Hacker News 社区广泛讨论，帖子获得 427 分。

Flock 收集的数据范围远超正常企业设备管理的必要范畴——除了基础的设备位置和运行时长，还包括员工的物理移动轨迹、在特定场所的停留时间，以及将这些数据与第三方数据 broker（数据中间商，以收集和转售个人数据为主要商业模式的公司）共享的行为。当该开发者要求删除数据时，Flock 隐私联系人的回复被形容为"模板化的企业套话"，缺乏实质性回应。

目前，多个隐私倡导组织已联名致信企业决策者，呼吁停止使用 Flock 的服务。这起事件折射出 B2B 监控工具领域的监管空白——原本设计用于保护公司资产的安全工具，正在以"安全"为名系统性地侵犯员工隐私。工具的合法性与道德边界，需要更清晰的监管框架来厘清。

来源：[Hacker News](https://honeypot.net/2026/04/14/i-wrote-to-flocks-privacy.html)

---

### OpenSSL 4.0.0 正式发布：全球最广泛使用的开源 TLS 库迎重大更新

互联网基础设施核心组件迎来里程碑版本。OpenSSL（Secure Sockets Layer，开源加密协议库，是全球 HTTPS 流量的安全基石）4.0.0 正式发布，这是该开源项目近五年来的首个重大版本更新，Hacker News 社区给予 168 分高度关注。

OpenSSL 4.0.0 的核心改进围绕现代计算场景重新设计：在性能层面，引入了对 QUIC（Quick UDP Internet Connection，一种现代传输协议，旨在解决 TCP 的拥塞控制问题）协议的实验性支持，并大幅优化了椭圆曲线密码学（Elliptic Curve Cryptography，ECC）的运算效率；在安全层面，废弃了若干已不再安全的历史加密算法，并强化了对后量子密码学（Post-Quantum Cryptography，PQC，指设计能够抵御量子计算攻击的加密算法）的初步支持。

QUIC 协议的引入尤为重要——当 Google（全球最大互联网公司之一）和 Meta 等巨头正在推动将 QUIC 作为 HTTP/3 的底层传输协议，OpenSSL 的支持意味着 TLS 库终于能够原生拥抱这一趋势，而非依赖应用层自行处理加密。对于整个互联网而言，这意味着更低的连接建立延迟和更高的传输效率。

来源：[Hacker News](https://github.com/openssl/openssl/releases/tag/openssl-4.0.0)

---

### Google Chrome 推出 Skills 功能：AI 提示词一键变浏览器工具

Google 在 Chrome 浏览器中推出 Skills 功能，用户能够将表现最佳的 AI 提示词直接转换为浏览器中的一键操作工具。该功能基于 Gemini（Google 的多模态 AI 模型）集成构建，代表了 AI 辅助工具从"问答"向"执行"的重要转变。

Skills 功能的实现逻辑是：用户在与 AI 对话过程中保存的高质量提示词，经 Chrome 解析后生成可直接调用的浏览器扩展（Extension），无需用户编写任何代码。在演示中，用户将一个商品比价提示词保存为 Skill 后，只需点击浏览器工具栏按钮，即可对当前页面中的产品自动执行比价操作。

这不仅是 AI 与浏览器融合的里程碑，更是 AI 原生应用形态的一次探索——从"AI 帮你找答案"到"AI 帮你完成任务"，Chrome 正在模糊 AI 助手与传统工具的边界。随着 Skills 生态的成熟，浏览器可能成为 AI Agent（AI 代理，能够自主完成多步骤任务的 AI 系统）进入用户日常的数字入口。

来源：[Hacker News](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)

---

### Max Hodak 的 Science Corp 准备将脑部传感器首次植入人体

前 Neuralink（由 Elon Musk 创立的脑机接口公司）总裁 Max Hodak 创办的 Science Corp. 宣布，将自研脑部传感器首次植入人体。该设备通过柔性网状电极（而非 Neuralink 的金属丝线程设计）贴合于大脑皮层表面，可向脑或脊髓损伤区域发送温和电刺激以促进细胞修复，目标是为脊髓损伤、脑震荡、抑郁症等神经系统疾病提供新的治疗路径。

Science Corp. 与 Neuralink 的技术路线存在本质差异：Neuralink 采用穿透式电极直接插入脑组织，信号精度高但创伤风险也相应更大；Science Corp. 的柔性电极贴附于大脑皮层表面，侵入性更低但信号分辨率受限。两种路线代表脑机接口领域的两种工程哲学的碰撞，最终哪种方案更安全有效，需要临床数据来验证。

脑机接口（Brain-Computer Interface，BCI，通过技术手段建立大脑与外部设备之间的直接通信通道）行业正在从动物实验走向人体试验的临界点。Neuralink 已完成首例人体植入，Synchron（另一家脑机接口公司，采用血管介入式技术路线）在 2022 年获得 FDA（美国食品药品监督管理局）批准开始临床试验，Science Corp. 即将加入这一行列。真正的考验才刚刚开始。

来源：[TechCrunch](https://techcrunch.com/2026/04/14/max-hodaks-science-corp-is-preparing-to-place-its-first-sensor-in-a-human-brain/)

---

### Waymo 伦敦开测：英国迎来首个 Robotaxi 商业化前奏

Alphabet（Google 母公司）旗下的自动驾驶出租车公司 Waymo 宣布在伦敦开始自动驾驶出租车测试，标志着其全球化扩张进入实质阶段。伦敦有望成为 Waymo 在美国之外的第一个海外商业化落地点。

Waymo 目前已在美国的旧金山（San Francisco）、凤凰城（Phoenix）和洛杉矶（Los Angeles）开展商业运营，累计完成数百万次出行服务。伦敦测试的启动，意味着 Waymo 将挑战右舵驾驶和更复杂的城市路况——英国街道更窄、环岛众多、骑行者密度极高，这些因素都对感知和决策算法提出了不同挑战。伦敦测试初期将限制在小范围区域内，并配备安全驾驶员。

对英国政府而言，Waymo 的进入是自动驾驶监管框架的一次真实检验。英国已建立相对完善的自动驾驶法律框架，并将其定位为国家工业战略的重要组成部分。但责任认定、保险制度、伦理审查等关键问题尚未完全解决。伦敦 Robotaxi 能否真正商业化，将是整个自动驾驶行业在北美之外发展的风向标。

来源：[TechCrunch](https://techcrunch.com/2026/04/14/london-gets-closer-to-its-first-robotaxi-service-as-waymo-begins-testing/)

---

### Adobe 紧急修复 PDF 零日漏洞：黑客已利用数月

Adobe 紧急修复了一个被黑客持续利用数月的 PDF 零日安全漏洞。安全研究人员的分析显示，该漏洞最早在 2025 年 11 月即被攻击者利用，黑客通过在 PDF 文档中嵌入恶意代码，受害者打开文件即可被感染。

零日漏洞（Zero-Day Vulnerability，指被发现后立即被攻击者利用、尚未有官方修复补丁的漏洞，"零日"意味着修复窗口为零）是网络攻击中最具破坏力的工具之一。由于 Adobe PDF Reader 是全球最普及的文档查看工具，从个人简历到企业合同都以此格式流转，该漏洞的潜在影响范围极大。目前尚不清楚确切的受害人数规模，但考虑到此类攻击的高度针对性，受影响范围可能远超公开报道的数字。

这起事件再次揭示了一个被低估的风险：PDF 阅读器的安全性。PDF 格式的复杂性——支持 JavaScript（PDF 内嵌脚本语言）、外部资源引用、多媒体内容——使其天然具备丰富的攻击面。用户应当养成不随意打开来源不明的 PDF 文件的习惯，并在 Adobe 发布安全更新后尽快安装。

来源：[TechCrunch](https://techcrunch.com/2026/04/14/adobe-fixes-pdf-zero-day-security-bug-that-hackers-have-exploited-for-months/)

---

### 财务风险管理平台 Pillar 获 a16z 领投 2000 万美元种子轮

财务管理软件领域出现了一个值得关注的新玩家。Pillar 宣布完成 2000 万美元种子轮融资，由 Andreessen Horowitz（a16z，顶级风险投资公司）领投，目标是让机构级金融对冲工具真正普惠中小企业。

传统意义上，利率掉期（Interest Rate Swap，IRS，一种利率对冲工具，双方约定在未来交换固定利率与浮动利率现金流）、货币对冲等复杂金融工具只有大型金融机构才有能力部署——高昂的定价门槛、复杂的合规要求、专业的运维团队，让中小企业对这些工具望而却步。Pillar 的核心赌注是：将这一切做得像用会计软件一样简单，让中小企业主也能通过直观界面管理自己的汇率风险和大宗商品敞口。

a16z 的投资逻辑并不难理解：中小企业市场足够大，而现有解决方案极度匮乏。但金融工具的民主化从来都是双刃剑——当复杂的对冲操作被简化到几次点击就能完成，缺乏专业金融知识的中小企业主是否会做出超越自身风险承受能力的决策？这是一个需要持续观察的问题。

来源：[TechCrunch](https://techcrunch.com/2026/04/14/financial-risk-management-platform-pillar-raises-20m-seed-in-round-led-by-a16z/)

---

本周极客早报涵盖安全风险、AI 基础设施投资热潮、隐私边界争议、两项重大技术发布、伦敦 Robotaxi 启动以及脑机接口人体试验的里程碑进展。从 WordPress 供应链攻击到脑机接口的临床前沿，技术世界在危机与突破之间快速前进。明天同一时间，极客早报与你不见不散。

---

### 首席架构师的深度阅读指南

本期最值得深入阅读的三篇文章推荐：

1. **[OpenSSL 4.0.0 正式发布 — Hacker News](https://github.com/openssl/openssl/releases/tag/openssl-4.0.0)**：QUIC 协议支持与后量子密码学初步融合，是理解未来互联网安全演进的关键入口。

2. **[Max Hodak 的 Science Corp 准备将脑部传感器首次植入人体 — TechCrunch](https://techcrunch.com/2026/04/14/max-hodaks-science-corp-is-preparing-to-place-its-first-sensor-in-a-human-brain/)**：柔性电极 vs. 穿透式电极，脑机接口两条技术路线的首次正面交锋，临床数据将决定未来方向。

3. **[Flock 被开发者指控运营「国内间谍计划」— Hacker News](https://honeypot.net/2026/04/14/i-wrote-to-flocks-privacy.html)**：B2B 监控工具的监管空白与员工隐私边界问题，是数字时代劳动关系的新命题。

---

*「极客早报」每日更新，订阅地址：your-blog-url*
