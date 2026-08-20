# MAA Roguelike Strategy AI - Current Handoff

Source snapshot:
`MAA_STRATEGY_AI_HANDOFF_2026-08-19.docx`

Purpose:
This file is the current product / strategy context baseline for ChatGPT and Codex.

Important:
This document describes product intent and known project state at the snapshot date.

Before modifying code, always verify actual implementation state using:

- `git status`
- `git diff`
- current branch
- `roguelike-lab` status documents
- latest Runtime logs

Do not infer that a planned feature is already implemented merely because it appears in this HANDOFF.

## Original Snapshot

MAA 界园 Roguelike Strategy AI 项目交接基线

版本：2026-08-19｜用途：新 ChatGPT / Codex 会话快速恢复上下文。本文只保留当前有效结论、已知问题、架构边界和下一步，不保留冗长聊天过程。

## 1. 项目定位

原版 MAA 更偏 Automation First：稳定、通用、低维护成本地自动完成肉鸽流程。

本项目定位为 Strategy Optimization + Automation：在保持自动化的前提下，提高阵容质量、Hope/资源利用率、战斗质量、路线收益、生存能力和稳定通关率。

核心原则：高收益约束下的稳定自动化。稳定通关优先于理论最优。

架构边界：MAA 负责 OCR、截图、点击、UI/地图识别和执行；Roguelike Strategy AI 负责招募、阵容、Hope、战斗、路线、资源、结局和知识决策。

## 2. 模块优先级

P0 Recruitment Intelligence：当前正在开发/实机联调。

P1 Battle Intelligence：部署位置、朝向、技能时机、撤退与再部署；已有 EW 开局不守家、朝向错误、漏怪的真实案例。

P2 Candle Route / Resource Intelligence：燃烛节点、事件、拾遗、生存资源与护盾最大化。

P3 Ending Policy：稳定通关、自动补未完成结局、指定结局。

学习体系：External/Runtime Evidence -> Candidate -> Validation -> Formal；Candidate 不自动 promote，要求可追溯、可回滚、有版本。

## 3. Runtime / 版本基线

`V000`：官方只读 baseline，永久保留用于 diff、回归和重建。

`V001`：早期实验版，曾因 Runtime config 污染造成窗口每操作一步漂移，不再作为基线。

`V001-clean`：隔离实验留档。

`V002` / `V002-R2`：Recruitment Intelligence 实机测试历史环境，保留失败现场和日志。

后续建议：创建一次 `V002-R3` 作为长期 Strategy AI Smoke Runtime；以后正常修复直接更新 R3，不机械创建 R4/R5/R6，除非需要保留重大回归现场。

关键运行配置：official JieGarden resources；`MouseMethod=SendMessageWithCursorPos`；`RecruitmentIntelligenceEnabled=true`。测试 GUI 使用 `D:\dev-tools\dotnet` 的独立 .NET 环境，并使用管理员启动脚本，避免系统全局环境和 MAA 自提权重启问题。

## 4. 已确认的 P0 招募问题与修复方向

最初 V002 的 Intelligence 配置在 GUI -> Task -> MaaCore 链路中被丢失，导致实机实际走官方 fallback；R2 已接通该配置链路，并加入 `[RecruitIntel]` 诊断日志。

系统白板必须是不可逆 Hard Filter。任何 `SpecialTarget`、`RarityGate`、`FunctionalScorer`、fallback、only-candidate 路径都不得重新加入 `ForbiddenCandidateSet`；宁可放弃也不主动招系统白板。

R2 实机中 Strategy AI 已能选择桃金娘、伊桑，但 Execution Layer 的 `recruit_appointed_char()` 无法重新定位已选候选，出现长时间左右滑动并最终放弃。最高优先修复 Candidate Selection -> Appointment divergence：策略结果应携带候选 rect/carousel state，或 appointment 前可靠 re-anchor，并限制重试。

Logical Initial Draft Slot 与 Plugin Invocation 必须分离，执行重试不能把同一张券误当成新 draft slot。

## 5. InitialDraftPolicy：最新正式需求

开局三张券属于 InitialDraftPolicy，与道中补位策略分离。开局队伍基本为空，不使用 `DuplicatePenalty` / `SaturationPenalty`。

狙击位长期显式指定维什戴尔作为开局核心；目标是高练度助战维什戴尔，而不是“自己没有才助战”。

另外两个初始位置同样允许比较 Owned Candidate 与 Support Candidate。即使用户自己拥有低星战神，如果助战同名/同功能候选练度明显更高，也应允许助战覆盖自有低练度版本。

真实账号案例：桃金娘为 E2、S1、Lv1；伊桑为 E1 Lv40。此前选择 own_candidate 并非产品最终目标；开局需要 RosterStrength Awareness。

Initial Candidate Quality 至少预留：elite、level、skill level、mastery、module、rarity、functional roles。

开局重点评价 multi-role、survival、ground/block、healing/sustain、economy、ranged/anti-air、control、fast-redeploy/bait、utility。一个干员允许多个功能标签，例如古米 = ground + block + healing + sustain。

4★高价值低 Hope 战神优先于 3★；系统白板永远禁止。开局几乎不应把“没有合适候选”作为常规路径。

助战搜索必须有预算（swipes / refreshes / seconds），不能为了微小收益无限翻页。

Multi-SupportCapability 当前仍为 UNKNOWN：现有日志只证明第一张助战维什戴尔成功，第二/第三张此前根本没有真正进入 support。需要 targeted smoke 验证第一张助战后第二张是否仍有助战入口。

## 6. 低星高性价比策略

输出核心可以优先高星；辅助功能位优先 0 Hope / Low Hope 高性价比 4★，再考虑 3★。

不能只按职业评价，必须按 Functional Role。当前硬编码少量名字不等于正式 Low-Star Intelligence。

应建立 `OperatorFunctionalProfile`：`operator_id`、`canonical_name`、`rarity`、`profession`、`position`、`functional_roles[]`、`hope_cost/规则`、`initial_draft_score`、`midrun_base_score`、`evidence`、`version`。

Runtime 应逐步加载正式 profile 数据，而不是无限扩大 C++ header 硬编码名单。

UI 后续增加策略级开关：智能招募总开关 + “低星高性价比招募”复选项（默认开启）。系统白板过滤等基础规则不必各自暴露 checkbox。

## 7. 电弧策略：最新修正

删除旧规则“道中特种券优先电弧”。当前 client resource 显示电弧为 6★、SUPPORT、RANGED，因此不能继续按 Specialist target 写死。

电弧不参与 InitialDraft。开局 Hope 不足，也不应抢占核心构筑资源。

电弧定位为 Mid/Late-game Expansion Target。优先关系：Initial Core -> Core E2 -> Basic Functional Coverage -> Hope surplus -> Electric Arc。

启用条件至少包括：非初始招募；ActiveCore 已完成关键晋升（至少 E2）；Hope 足够支付且仍保留 Survival Reserve；基础功能位没有明显生存缺口；当前招募入口符合电弧真实职业。

ActiveCore 不能写死为望，应支持 USER_SPECIFIED_CORE。当前长期开局核心为维什戴尔。

## 8. Battle Intelligence（P1，当前只设计不实现）

目标：DeploymentPolicy、DirectionPolicy、SkillTimingPolicy、RetreatPolicy、RedeployPolicy。

真实案例 BATTLE-001：EW 开局部署没有正确守家、朝向错误并漏怪。

未来输入包括地图、蓝门/红门、敌人路线、地面/高台格、攻击范围、阻挡、费用、阵容、波次等；输出 Operator + Tile + Direction。

技能不能统一“好了就开”。需区分 AUTO、普通主动技能、Targeted/脱手技能，并根据敌人波次、精英/Boss、防线压力、技能持续时间和下一波时机决策。

自动再部署：死亡/撤退 -> 再部署 CD -> 当前防线缺口 -> 费用 -> 可用地块 -> Tile + Direction。

允许从自己的成功局、社区攻略、Bilibili/YouTube 视频、成熟作业和人工规则学习，但必须先进入 Candidate Battle Knowledge，再验证后进入 Formal。

## 9. 燃烛 Route / Resource Intelligence（P2）

目标不是随机走节点，而是根据生命、护盾、锭、票券、队伍强度、层数、可达节点和目标结局动态评分。

重点研究：哪些节点优先、哪些事件优先、哪些应避开、是否主动寻找拾遗、如何最大化把锭/生命等资源转换成护盾/生存能力。

核心模式：Survival-First Candle Policy。护盾低于安全阈值且存在高价值拾遗路径时显著提高其权重；持有大量可转换资源时提高资源转换节点价值。

具体事件收益后续做 evidence-driven event database，不提前硬编码未经验证的结论。

## 10. Ending Policy（P3）

未来模式：STABLE_CLEAR / AUTO_UNLOCK / SPECIFIC_ENDING。

STABLE_CLEAR：优先成功率最高的稳定路线；AUTO_UNLOCK：优先尚未完成结局；SPECIFIC_ENDING：围绕用户指定结局规划路线/事件/藏品/特殊节点。

UI 更适合下拉框“结局目标”，而不是堆多个 checkbox。

## 11. 当前下一步（交给 Codex）

先完成 R004 Candidate Selection / Appointment 修复并通过 Build、CTest、Python tests。

随后从 V000 clean copy 创建一次 V002-R3，做 isolation audit，保留 official resources、`SendMessageWithCursorPos`、`RecruitmentIntelligenceEnabled=true`，并提供统一管理员启动入口。

R3 第一轮 Smoke Test 只验证：策略选中桃金娘/伊桑后能否真正点击成功，不再长时间左右滑动、不再 plugin re-entry。不要同时评价 InitialDraft 助战质量。

点击闭环稳定后，再单独开发 InitialDraftPolicy V2：维什戴尔高练度助战核心 + 另外两张券比较自有低练度战神与助战高练度战神，并 targeted smoke 验证多次助战能力。

电弧继续禁用到主C E2 + Hope 富余 + 基础阵容成型。Battle/燃烛/多结局暂不进入 Runtime 实现。

## 12. 开发纪律 / 已踩坑

不要让 Codex 根据 Git 最新提交自行推断需求；Git 可能未同步最新策略，以本交接基线和最新明确提示为准。

不要直接污染 V000；不要把实验 resource override 混入官方 JieGarden `recruitment.json`。

不要通过 `priority=-99999` 伪装 Hard Filter。

不要让 Candidate 自动 promote 到 Formal。

不要为了一个问题同时扩大到 Battle、Route、Ending、Wang S3 等多个模块。

每次实机失败优先读取最新日志还原真实调用链，再修改代码，避免猜测式修复。

## 13. 新会话恢复指令

新建 ChatGPT 会话后上传本文件，并发送：‘继续 MAA 界园 Strategy AI 项目。请以这份 HANDOFF 为当前项目基线；先总结当前 P0 状态和下一步，不要自行扩展实现范围。’

给 Codex 时也可直接让其读取本文件，并明确：本文件是产品/策略基线，实际代码状态仍需通过 `git status`、`git diff`、`roguelike-lab` 文档和 Runtime 日志核对。
