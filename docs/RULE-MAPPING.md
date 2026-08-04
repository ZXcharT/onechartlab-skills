# 原始规则到公开版映射

本表用于证明公开化没有依靠压缩或“通用化”删除安全约束。原始位置指安装版 v2.6 的六个文件；公开位置指本仓库 Skill。身份名称与审批者名称被参数化，行为语义保留。

| 原始规则 | 原始位置 | 公开版位置 | 处理 | 测试 |
|---|---|---|---|---|
| 主代理负责、子代理无最终回复且不再委派 | `SKILL.md` 核心规则1 | `SKILL.md` 核心规则1 | 原义保留 | T02、T07 |
| 六段 Plan、审查与明确批准双通道 | `SKILL.md` 规则2、Plan 双通道；`task-packets.md` | `SKILL.md` Plan 双通道；`task-packets.md` | 原个人审批者名称改为 approver | T01、T12 |
| Agent 选择、默认模型继承、不可静默替换 | `SKILL.md` 规则3 | `SKILL.md` 配置、规则3；`task-packets.md` 运行配置/派发信封 | 用户指定优先，否则按职责选择；无合适角色时回退当前角色子 Agent | T02 |
| Plan 审查 read、独立新 thread、结束后关闭 | `SKILL.md` Plan 双通道1、7 | `SKILL.md` Plan 双通道1、7；`task-packets.md` Plan 审查包/账本 | 审查者使用同一身份路由规则并记录 reviewer thread | T01、T02 |
| 最小 read/write 权限 | `SKILL.md` 规则4；各协议 | `SKILL.md` 规则5；各协议 | 原义保留 | T03 |
| 一个责任域一个执行者、QUERY_BACKLOG | `SKILL.md` 规则5；`task-packets.md` | `SKILL.md` 规则6；`task-packets.md` | 原义保留 | T05 |
| 结构化工具 Canary、同 thread 生产 | `SKILL.md` 规则6；`execution-protocol.md` | `SKILL.md` 规则7；`execution-protocol.md` | “金融 MCP”泛化为结构化/MCP 工具 | T04 |
| 证据外部化、确定性断言、可重跑 | `SKILL.md` 规则7；执行/研究/验证协议 | `SKILL.md` 规则8；完整角色协议 | 原义保留 | T06、T07 |
| `runs/...` 隔离、单目录单写者 | `SKILL.md` 规则8；`task-packets.md` | `SKILL.md` 配置/规则9；`task-packets.md` | 参数化为授权 `run_root` | T06 |
| FINAL 字段、stage 不等于验收 | `SKILL.md` 规则9；`task-packets.md` | `SKILL.md` 规则10；`task-packets.md` FINAL 模板 | 原义保留 | T07 |
| 状态汇报与批准独立、异常穿透 | `SKILL.md` 规则10；`communication-protocol.md` | `SKILL.md` 规则11；完整沟通协议 | 原义保留 | T08、T09 |
| 协议层级、冲突先停止 | `SKILL.md` 规则11 | `SKILL.md` 规则12 | 原义保留 | T13、T14 |
| 执行者完整硬停止条件 | `execution-protocol.md` write 硬停止 | `execution-protocol.md` write 硬停止 | 全项保留并增加未授权 run_root | T03、T04、T06、T10、T12 |
| 研究者统一底稿、不自行降级来源 | `research-protocol.md` 责任与证据 | `research-protocol.md` 责任与证据 | 原义保留 | T03、T05、T09 |
| 验证一次性审核资格、AUDIT_DONE | `validation-protocol.md` 阶段审核资格 | `validation-protocol.md` 阶段审核资格 | 原义保留 | T07、T11 |
| NEEDS_REVISION 后主代理接管、禁止增量复核 | `validation-protocol.md` 验证门禁/回复屏障 | `validation-protocol.md` 验证门禁/回复屏障 | 原义保留 | T11 |
| read 验证者工具受限时 BLOCKED | `validation-protocol.md` 金融 MCP 受限 | `validation-protocol.md` 结构化/MCP 工具受限 | 领域词泛化，行为保留 | T03、T09 |
| 跨会话只传 process_trace | `validation-protocol.md` 跨会话审计；`task-packets.md` | 同名公开章节 | 增加不得包含私人上下文或凭证 | T09、T12 |
| 统一状态与三类沟通事件 | `communication-protocol.md` 状态与事件 | `communication-protocol.md` 状态与事件 | 原义保留 | T08、T09、T12 |
| 用户可见投递失败链 | `communication-protocol.md` 通知责任链 | `communication-protocol.md` 通知责任链 | 五级责任链保留 | T09 |
| 高价值任务最低必报节点 | `communication-protocol.md` 最低必报节点 | 同名公开章节 | 六个节点保留 | T08、T09 |
| 仅一次局部可逆静默恢复 | `communication-protocol.md` 静默恢复边界 | 同名公开章节 | 原义保留 | T10 |
| 最终回复屏障 | `SKILL.md` 验证；`communication-protocol.md` | `SKILL.md` 验证；`communication-protocol.md` | 原义保留 | T07、T11、T14 |
| 实质变化重新审批 | `SKILL.md` Plan；`communication-protocol.md` | 同名公开章节 | 原义保留 | T12 |
| 沟通协议唯一相对路径 | `communication-protocol.md` 加载闭环 | 同名公开章节 | 原义保留 | T13 |
| 沟通协议加载失败硬阻断 | 主 Skill 与沟通协议 | 主 Skill 与沟通协议 | 只允许停止、保存状态和报告 | T14 |

## 删除项

没有删除安全规则。仅删除或替换以下环境绑定：

- 个人审批者名称 → `approver`。
- 固定本地 Agent id → 用户指定、按职责选择或当前角色子 Agent。
- 固定工作区假设 → 用户授权的 `run_root`。
- 金融领域专用措辞 → 结构化/MCP 工具通用措辞。

完整细则仍由对应协议作为唯一场景规范来源；主 `SKILL.md` 保留不可绕过的安全短摘要。
