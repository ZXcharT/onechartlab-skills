# 决策 Plan 与子代理任务包

通用身份、权限、审批、沟通和门禁由主 Skill 定义。派发前读取对应角色协议；命中沟通事件时必须加载 [沟通协议](communication-protocol.md)。本文件只提供不可缺字段。

## 给 approver 的六段 Plan

```markdown
## 目标
核心问题

## 范围
对象、时间、包含项和排除项

## 处理方式
主要阶段与主/子代理分工

## 交付物
最终结论、文件或产出

## 验收标准
完成且可信的可测条件

## 需要 approver 决定
仅列影响方向的选项；没有写“无”
```

Plan 一屏内完成，技术细节留在内部任务包。批准后持续执行不豁免阶段报告；范围、方向、风险或交付目标实质变化时重新确认。

## Plan 运行配置

```markdown
- delegate_agent：用户指定 / 按职责选择 / current-agent
- plan_reviewer_agent：用户指定 / 按职责选择 / current-agent
- run_root：用户授权工作区中的运行根目录
```

用户指定优先；否则按子任务职责选择合适的专业 Agent。没有合适角色时使用 `current-agent`，继承当前 Agent 角色创建临时子 Agent。用户指定的 Agent 不可用时停止并报告。不同角色使用独立新 thread；同一 thread 不更换 Agent。

## 内部责任映射

```markdown
| 责任域/交付物 | 唯一责任人 | 输入 | 产出路径 | 禁止重叠范围 | 失败后接管者 |
|---|---|---|---|---|---|
```

## 高价值写任务控制

```markdown
- 运行目录：<run_root>/<YYYYMMDD-HHMM>-<任务简称>-<随机短串>/
- 唯一写入责任人：
- FINAL 声明：<运行目录>/FINAL.md
```

```markdown
# FINAL
- 批准范围：
- 范围偏差：无 / ...
- 正式构建入口：
- 正式产物文件名清单：
  - ...
- 关键口径与数据源：
- 验证状态：DRAFT / VALIDATING / NEEDS_REVISION / ACCEPTED
- 最终回复屏障：阻塞 / 已解除（仅 ACCEPTED）
- 重大异常与恢复：无 / 事件、影响、恢复、披露状态
- 未解决项：无 / ...
```

## QUERY_BACKLOG

```markdown
| 查询问题 | 责任域 | 用途/为何需要 | 紧急度 | 建议责任人 |
|---|---|---|---|---|
```

已有域优先续开放的原 `threadId`；独立新方向确有必要时另派 read 研究者。主代理关键路径例外必须记录“为何关键、查什么、停止边界”。

## 子代理派发信封

```markdown
### 派发信封
- agent：<所选 Agent；current-agent 回退时省略 agent / agentType>
- model：继承所选角色当前默认模型（调用时省略 model）；用户批准覆盖时记录
- access：read / write
- 功能角色：研究 / 数据执行 / 一般执行 / 验证 / Plan 审查
- thread：新建 / 续 threadId=<...>
- 角色独立性：新角色必须新 thread；同责任域续派才可续 thread
- 依赖协议：<相对路径>
- 关闭条件：完成后立即关闭 / 等待追加
- 失败升级：按 communication-protocol.md 回传 COMMUNICATION_EVENT
```

新建 thread 用于独立角色；Canary 通过后和域内补充可续原 thread。续派沿用已绑定身份，不跨角色复用 thread。Plan 审查 thread 关闭后，后续研究、执行、验证必须新建 thread。

## 数据执行 Canary 包

```markdown
你是生产数据执行者。当前只做工具 Canary，不开始正式取数。

### 精确工具与最小参数
- 工具全名：
- 最小参数：
- 预期返回形态：

### 成功判据
工具真实可调用且结构符合预期

### 禁止
不搜索网页、不启动浏览器、不创建生产证据、不换源、不安装依赖

### 返回
- CANARY_OK：status=COMPLETED、工具、参数、返回形态
- CANARY_BLOCKED：status=BLOCKED、错误证据、影响、恢复建议、能否安全继续、是否需要 approver 决定
```

## 数据执行生产包

```markdown
Canary 已通过。执行生产数据任务。

### 数据目标与范围
### 允许工具与数据源顺序
### 唯一写入目录与允许文件
### 证据包
- 原始响应 / 结构化数据 / 来源账本
- 字段口径 / 缺失冲突 / 可重跑脚本
### 验收与停止条件
### 返回
统一状态、证据路径、关键结果、冲突缺口、恢复建议、能否安全继续、待决定事项；关键异常附 COMMUNICATION_EVENT
```

## 研究型任务包

```markdown
你是研究型子代理。

### 研究目标
### 范围与口径（对象、时间、指标、排除项）
### 背景与已确认决定
### 证据底稿与来源账本
### 来源与工具优先级
### 唯一责任范围与禁止重叠
### 权限上限、禁止动作与升级条件
### 长篇边界
read 任务只精简返回；需长篇文件时报告，由主代理另派 write 任务。
### 输出
统一状态、证据路径、关键发现、冲突缺口、恢复建议、能否安全继续、主代理可裁决项、需 approver 决定项；关键异常附 COMMUNICATION_EVENT
```

## 一般执行任务包

```markdown
你是执行型子代理。

### 目标与交付物
### 已批准范围
### 输入、文件、资源与路径
### 具体要求
### 必须保持不变
### 权限上限与禁止动作
### 验收与自检
### 停止与升级条件
### 输出
统一状态、产出路径、关键结果、验证证据、未完成项、恢复建议、能否安全继续；关键异常附 COMMUNICATION_EVENT
```

## 验证型任务包

```markdown
你是验证型子代理。本次审核将消耗该阶段唯一的审核资格，完成后立即关闭，不进行增量复核。

### 阶段标识与审核资格
- approved_plan_id：
- stage_id：
- audit_status：NOT_AUDITED

### 原始目标 / 已批准 Plan / 验收标准
### 当前状态：DRAFT / VALIDATING / NEEDS_REVISION
### 待验证产出与原始证据
### 确定性断言
| 关键结论 | 原始证据 | 计算或断言 | 通过条件 |
### 构建链重跑标准
### 最终回复屏障：阻塞 / 已解除（仅 ACCEPTED）
### 权限上限与禁止动作
### 输出
一次性返回完整问题清单、建议状态、Plan 缺项、无法验证项、建议动作、能否在批准范围内返修；返回后该阶段记为 AUDIT_DONE，后续由主代理接管，关键异常附 COMMUNICATION_EVENT
```

## Plan 审查任务包

仅六段 Plan 任务使用；按身份路由规则选择审查者，使用 `read`、Plan 审查角色和独立新 thread。Plan 审查消耗该 Plan 阶段唯一审核资格，修订后不再次审查；额外审查仅在用户明确授权时进行。

```markdown
你是 Plan 审查者。只审 Plan，不执行、不写文件。

### 原始请求
### PLAN_DRAFT
### 审查身份与 thread
- plan_reviewer_agent：<所选 Agent / current-agent>
- reviewer_thread：独立新 thread
- access：read
### 审查维度
- 遗漏、偏移、错误假设、矛盾
- 工具/权限/时序不可执行点
- 审批门、thread 生命周期和验证缺口
### 允许
只读取任务包明确列出的文件、状态和证据
### 禁止
不做业务研究、生产查询、写入、变更、下级委派或替 approver 决定
### 输出
PLAN_OK / PLAN_NEEDS_REVISION；问题严重程度、定位、建议；非实质补充建议
```

## Plan 审查账本

```markdown
- approver 反馈：未到 / 已批准 / 有修改意见
- 审查：未到 / PLAN_OK / PLAN_NEEDS_REVISION
- reviewer identity：<所选 Agent / current-agent>
- reviewer thread：<独立 threadId>
- 两方齐全：否 / 是
- 冲突：无 / 有
- 修订：无 / 非实质 / 实质
- 需二次确认：否 / 是（原因）
```

## 窄范围数据验证执行者包

此角色只能作为该阶段唯一一次审核使用；若该阶段已有任何审核记录，不得派发。

```markdown
你是独立数据验证执行者，只复核指定样本，不修改生产底稿。
### Canary
### 抽样范围（禁止全量重建）
### 独立写入目录
### 完成后立即关闭
```

## 跨会话审计任务包

主代理先生成仅含可核查事件、文件路径和错误摘要的 `process_trace`：

```markdown
### 目标会话 ID 与审计范围
### process_trace 路径
### 当前 Skill 与协议路径
### 需核对规则
### 输出
评分、问题表；不可观察项标“无法确认”
```
