# OneChartLab Skills

[English](README.en.md)

OneChartLab Skills 是一组可审阅、可测试、可本地打包的 Agent Skills。首个 Skill [Agent Cowork Control](skills/agent-cowork-control/SKILL.md) 为 HanaAgent 的复杂协作任务提供 Plan、委派、证据、验证与沟通边界。

## 适用与不适用

适用于需要六段 Plan、子代理委派、跨来源证据、跨模块写入或独立验证的复杂任务。它让主代理保有目标、验收和用户沟通责任，并要求显式选择委派 Agent、最小权限、Canary、隔离运行目录和验证门禁。

不适用于闲聊、纯读取、简单问答、单代理可完成的研究或小范围一次性修改。它不替代宿主的权限系统；Skill 中的门禁是政策约束，除非宿主另有硬执行机制。

## 状态说明

| 状态 | 含义 |
|---|---|
| 目标运行时 | `agent-cowork-control` 按 HanaAgent 的工具与线程语义编写；公开候选已通过结构、策略 trace 与打包测试，正式发布前仍需做一次干净安装验证。|
| 静态格式参考 | Claude Code、Codex 仅作为开放目录/Skill 格式参考，未做运行验证。|
| 未验证 | 其他 Agent 运行时、其他宿主工具语义及跨平台行为不作承诺。|

## HanaAgent 安装与首次使用

1. 将本仓库中的 `skills/agent-cowork-control/` 放入 HanaAgent 的 Skill 目录，保留目录名和 `SKILL.md`。
2. 在每个获批的复杂任务 Plan 中，由 request owner 或 approver 明确解析 `delegate_agent_id`。不可默认猜测、替换或回退到其他 Agent。
3. 默认继承所选 delegate Agent 的配置默认模型；模型覆盖需要用户明确批准并记录。
4. 将任务级 `run_root` 指向用户授权工作区下的 `runs/`，为高价值写任务创建唯一运行目录和 `FINAL.md`。
5. 首次调用只在满足“适用”条件时加载 Skill，并按 `SKILL → task-packets → role protocol → communication protocol` 顺序执行。

## 升级、卸载与排错

**升级**：替换整个 `skills/agent-cowork-control/` 目录；若使用完整仓库，在仓库根运行 `python3 scripts/check_repo.py`。保留本地任务证据，不把本机配置或运行轨迹放入发布包。

**卸载**：从 HanaAgent Skill 目录移除该目录；不会删除已创建的任务运行目录。按你的保留策略单独清理运行产物。

**排错**：先确认目录名与 frontmatter `name` 相同；确认宿主提供 `subagent`、续线程、关闭线程、状态检查和工作流身份语义；确认 Plan 写入了 `delegate_agent_id` 与 `run_root`。结构化/MCP 工具不可用时应看到 `BLOCKED`，而不是网页替代。

## 开发与发布

- [贡献指南](CONTRIBUTING.md)
- [安全政策](SECURITY.md)
- [兼容性边界](docs/COMPATIBILITY.md)
- [标准](docs/STANDARDS.md)
- [原始规则到公开版映射](docs/RULE-MAPPING.md)
- [本地发布流程](docs/RELEASE.md)
- [变更记录](CHANGELOG.md)

只需 Python 标准库：`python3 scripts/check_repo.py`；构建本地 ZIP：`python3 scripts/build_release.py`。

## 许可与品牌

代码和文档采用 [MIT](LICENSE)，版权为 © 2026 ZXcharT。MIT 许可授权使用、复制和修改软件；它本身不授予 ZXcharT、OneChartLab 或相关标识的商标、品牌背书或名称使用权。衍生项目应避免暗示官方关联。
