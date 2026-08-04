# OneChartLab Skills 项目工作规则

本文件是 OneChartLab Skills 公开仓库的项目级规则入口，只对本仓库生效。

## 1. 项目定位

本仓库维护可公开安装、审查和发布的 Agent Skills。当前主要内容是 `agent-cowork-control`，其规则必须同时满足：人能读懂、Agent 能执行、测试能验证、发布包能复现。

仓库中的政策约束不能冒充 HanaAgent 或其他宿主平台的硬权限机制。运行能力不足时应明确 `BLOCKED`，不得静默换来源、降级安全门禁或虚构验证结果。

## 2. 开工门禁

任何写入前核对：

```text
仓库绝对路径：
Git 根目录：
当前 branch：
当前 commit：
working tree：clean / dirty
本次基线：
任务类型：Skill 行为 / 测试协议 / 文档 / 发布
```

存在无法解释的改动、目标不是唯一正式 Git 根、规则与测试相互冲突或同一工作区有其他写入者时，停止修改并报告。

## 3. 必读文件

首次进入仓库先读取：

- `README.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `docs/STANDARDS.md`

涉及 Skill 行为时再读取：

- `skills/agent-cowork-control/SKILL.md`
- 受影响的 `skills/agent-cowork-control/references/`
- 对应测试与 fixture

涉及打包、版本或公开发布时再读取：

- `docs/RELEASE.md`
- `CHANGELOG.md`
- `scripts/build_release.py`
- `scripts/verify_artifacts.py`

项目文件和当前测试结果优先于历史聊天或助手记忆。

## 4. 结构与修改边界

- Skill 目录名必须与 `SKILL.md` frontmatter 的 `name` 一致。
- Skill 内不新增 README；完整角色语义和协议放在单层 `references/`。
- Skill 内链接使用 Skill 根相对路径，不写本机绝对路径。
- 安全短摘要保留在 `SKILL.md`；详细协议、fixture、断言和变更记录同步维护。
- 新增运行时声明必须标示“实际验证”“静态格式参考”或“未验证”。
- 不把政策要求写成宿主必然具备的工具、权限或自动执行能力。
- 不提交第三方内容，除非许可、归属和再分发边界已经核对。
- 不新增依赖、平台绑定或发布渠道，除非任务明确需要且得到批准。
- 一次只解决一个主要问题，不顺手重写提示词体系、调整无关测试或扩大兼容范围。

## 5. 安全与隐私

禁止提交或写入测试材料：

- token、secret、Authorization 值、密码、密钥和证书；
- 私有路径、会话标识、账户信息和内部服务地址；
- 日志、缓存、运行轨迹、真实用户数据和未脱敏证据；
- 未经许可的第三方文档、模板或代码。

发现疑似泄露时停止分发，保留最少必要证据，按 `SECURITY.md` 处理，并重新扫描工作树与候选归档。

## 6. 验证要求

普通修改至少执行：

```bash
python3 scripts/check_repo.py
git diff --check
```

修改 Skill 安全规则、协议或行为时：

- 更新对应的 T01–T14 fixture、断言和 `CHANGELOG.md`；
- 验证可读规则、references 与可执行断言没有冲突；
- 对新增行为同时覆盖成功、阻塞和关键失败路径。

涉及发布候选时再执行：

```bash
python3 scripts/build_release.py
```

并按照 `docs/RELEASE.md` 在干净解压目录检查仓库 ZIP、Skill 包和 `SHA256SUMS`。缺少独立安装环境或平台能力时标记 `NOT_RUN`，不得声称兼容或可发布。

## 7. Git 与外部边界

- 同一工作区同一时间只允许一个写入责任人。
- 每项变更形成单一职责 commit；版本、发布说明和产物必须能追溯到唯一 commit。
- 不从 `dist/`、ZIP 解压目录、旧副本或临时 run 继续开发。
- Git push、GitHub Release、商店发布、远程仓库设置和外部安装验证必须获得仓库所有者单独批准。
- 本地构建成功只代表候选产物生成，不等于已公开发布或所有平台兼容。

## 8. 完成报告

完成时至少说明：

```text
状态：COMPLETED / NEEDS_REVISION / BLOCKED
本次解决：
本次未做：
变更文件：
实际命令与退出结果：
测试与安装验证：
版本、commit 与产物：
外部影响：
回滚入口：
已知风险与未验证项：
需要仓库所有者做什么：
```
