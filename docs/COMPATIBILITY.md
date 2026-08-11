# 兼容性

## 已验证运行时与验证边界

本 Skill 当前已验证运行时为 HanaAgent。v0.1.1 候选已通过仓库结构、策略 trace、资源链接、打包复检，并在不含同名 Skill 的 HanaAgent 虚拟机中完成干净安装验证；安装后可正常加载并执行显式调用。自动匹配由宿主和模型共同决定，不保证每次稳定；未自动加载时应明确指定 Agent Cowork Control。其他 Agent 工具需要具备相当能力，所需语义包括：`subagent` 新建、`subagent_reply` 续线程、`subagent_close` 关闭、`current_status` 状态检查、`workflow` Agent 身份、当前角色子实例、`threadId` 生命周期、`access` 读写权限与可选 `session` 审计轨迹。用户未指定 Agent 时按子任务选择合适的专业角色；没有合适角色时通过省略 `agent` / `agentType` 创建当前角色的临时子 Agent。

## 静态格式参考

Claude Code 与 Codex 可参考本仓库的开放目录、frontmatter、单层 references 和相对链接格式；未验证其委派、线程、权限、工作流或跨会话语义。

## 未验证与失败方式

其他宿主和跨平台运行未验证。缺少上述必要能力时停止受影响流并报告 `BLOCKED`。Skill/prompt 的 Plan、验证和回复屏障是政策约束，宿主是否硬执行由宿主决定。
