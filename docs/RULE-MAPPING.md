# 原始规则到当前公开版映射

本表记录安装版 v2.6 规则如何演进为当前公开版。原始位置指安装版 v2.6 的六个文件；当前位置指本仓库 Skill。

这是一份演进账本，不表示所有原始流程都按原义保留。当前版本将协作分为直接执行、轻量协作和受控协作，并把部分原本无条件执行的流程改为按模式、风险和交接需求触发。运行时事实源仍是 `SKILL.md`、对应 references、[行为契约](../skills/agent-cowork-control/references/behavior-contract.md) 和 T01–T14 回归测试。

| 原始规则 | 原始位置 | 当前处理 | 当前位置 | 测试 |
|---|---|---|---|---|
| 主代理负责、子代理无最终回复且不再委派 | `SKILL.md` 核心规则1 | 保留 | `SKILL.md` 核心规则1 | T02、T07 |
| 六段 Plan、独立审查与明确批准 | `SKILL.md` 规则2、Plan 双通道；`task-packets.md` | 分层：直接任务无 Plan；普通多步骤和轻量协作使用简短“步骤 → 验证”计划并由用户确认；受控协作保留六段 Plan、用户确认和一次独立 Plan 审查 | `SKILL.md` 规则2、Plan 双通道；`task-packets.md` | T01、T12 |
| Agent 选择、默认模型继承、不可静默替换 | `SKILL.md` 规则3 | 参数化：用户指定优先，否则按职责选择；无合适角色时使用当前角色子 Agent | `SKILL.md` 规则3；`task-packets.md` 运行配置与派发信封 | T02 |
| Plan 审查使用 read、独立新 thread、结束后关闭 | `SKILL.md` Plan 双通道 | 仅受控协作使用；每个获批 Plan 最多一次 | `SKILL.md` Plan 双通道；`task-packets.md` Plan 审查包与账本 | T01、T02、T11 |
| 最小 read/write 权限 | `SKILL.md` 规则4；各协议 | 保留 | `SKILL.md` 规则5；各协议 | T03 |
| 一个责任域一个执行者、补充查询不重复派人 | `SKILL.md` 规则5；`task-packets.md` | 单一责任保留；正式 `QUERY_BACKLOG` 仅用于受控协作 | `SKILL.md` 规则6；`task-packets.md` | T05 |
| 结构化工具先 Canary、同 thread 生产 | `SKILL.md` 规则6；`execution-protocol.md` | 条件化：安全单次只读调用可直接执行；轻量协作遇到风险调用时升级；受控协作的批量、写入、不确定、高成本或高影响调用先 Canary | `SKILL.md` 规则7；`execution-protocol.md` | T04 |
| 证据外部化、确定性断言、可重跑 | `SKILL.md` 规则7；执行、研究与验证协议 | 保留，按任务规模使用 | `SKILL.md` 规则8；完整角色协议 | T06、T07 |
| `runs/...` 隔离、单目录单写者 | `SKILL.md` 规则8；`task-packets.md` | 条件化：普通单一写入者使用授权目标目录；非受控模式命中隔离条件时先升级，受控协作才为多个写入责任域、批量或正式数据、可重跑证据及中间产物隔离使用授权 `run_root` | `SKILL.md` 规则9；`task-packets.md` | T06 |
| FINAL 字段、stage 不等于验收 | `SKILL.md` 规则9；`task-packets.md` | 条件化：非受控模式命中交接条件时先升级；受控协作仅在持久交接、跨会话恢复、多产物汇总或用户明确要求正式证据包时创建 `FINAL.md` | `SKILL.md` 规则10；`task-packets.md` FINAL 模板 | T07 |
| 状态汇报与批准独立、异常穿透 | `SKILL.md` 规则10；`communication-protocol.md` | 安全语义保留；完整沟通状态机仅用于受控协作，轻量协作使用平台常规反馈 | `SKILL.md` 规则11；`communication-protocol.md` | T08、T09 |
| 协议层级、冲突先停止 | `SKILL.md` 规则11 | 保留；完整协议适用于受控协作 | `SKILL.md` 规则12 | T13、T14 |
| 执行者完整硬停止条件 | `execution-protocol.md` write 硬停止 | 保留；写入位置按授权目标目录或条件触发的 `run_root` 判断 | `execution-protocol.md` write 硬停止 | T03、T04、T06、T10、T12 |
| 研究者统一底稿、不自行降级来源 | `research-protocol.md` 责任与证据 | 受控协作保留；轻量协作使用自包含的最小任务说明 | `research-protocol.md`；`SKILL.md` 任务包规则 | T03、T05、T09 |
| 一次性审核资格、`AUDIT_DONE` | `validation-protocol.md` 阶段审核资格 | 受控协作分为一次 `PLAN_REVIEW` 和一次 `RESULT_REVIEW`；轻量协作不启用独立审核 | `validation-protocol.md`；`task-packets.md` | T07、T11 |
| `NEEDS_REVISION` 后主代理接管、禁止重复审核 | `validation-protocol.md` 验证门禁与回复屏障 | 受控协作保留；额外审核仅在用户明确授权时进行 | `validation-protocol.md` 验证门禁与回复屏障 | T11 |
| read 验证者工具受限时阻断 | `validation-protocol.md` 金融 MCP 受限 | 领域泛化为结构化/MCP 工具；受控结果审核保留 | `validation-protocol.md` 结构化/MCP 工具受限 | T03、T09 |
| 跨会话只传 `process_trace` | `validation-protocol.md` 跨会话审计；`task-packets.md` | 保留，并明确不得包含私人上下文或凭证 | 同名公开章节 | T09、T12 |
| 统一状态与三类沟通事件 | `communication-protocol.md` 状态与事件 | 仅受控协作使用完整状态机 | `communication-protocol.md` 状态与事件 | T08、T09、T12 |
| 用户可见投递失败链 | `communication-protocol.md` 通知责任链 | 受控协作保留；主代理仍承担最终通知责任 | `communication-protocol.md` 通知责任链 | T09 |
| 高价值任务最低必报节点 | `communication-protocol.md` 最低必报节点 | 仅受控协作使用 | `communication-protocol.md` 最低必报节点 | T08、T09 |
| 仅一次局部可逆静默恢复 | `communication-protocol.md` 静默恢复边界 | 受控协作保留；不得借恢复改变来源、权限或目标 | 同名公开章节 | T10 |
| 最终回复屏障 | `SKILL.md` 验证；`communication-protocol.md` | 分层：轻量协作由主代理验收后回复；受控协作等待一次结果审核并由主代理裁决为 `ACCEPTED` | `SKILL.md` 验证；`validation-protocol.md`；`communication-protocol.md` | T07、T11、T14 |
| 实质变化重新审批 | `SKILL.md` Plan；`communication-protocol.md` | 保留，适用于所有已批准计划 | 同名公开章节 | T12 |
| 沟通协议唯一相对路径 | `communication-protocol.md` 加载闭环 | 受控协作保留 | 同名公开章节 | T13 |
| 沟通协议加载失败硬阻断 | 主 Skill 与沟通协议 | 受控协作保留；只允许停止、保存状态和报告失败 | 主 Skill 与沟通协议 | T14 |

## 当前版本的主要变化

- 以明确协作收益而非任务体量作为启用条件。
- 将六段 Plan、独立 Plan 审查和独立结果审核限定于受控协作。
- 将 Canary、运行目录和 `FINAL.md` 从无条件流程改为按风险、写入结构和交接需求触发。
- 将固定审批者、Agent、工作区和金融领域措辞参数化为公开可复用的配置。

## 始终保留的安全边界

- 研究、检查和审查默认只读；写权限只授予明确写入责任人。
- 一个责任域只有一个执行者，不允许写入范围重叠或归属不明。
- 工具或来源失败时，不静默换源、扩权、安装依赖或降低可信度。
- 关键异常必须进入用户可见层，主代理承担最终通知责任。
- 目标、范围、来源、权限、外部影响或风险发生实质变化时，必须重新确认。

完整细则以对应协议为准；本表仅用于追踪规则来源和演进，不替代运行时规范或行为测试。
