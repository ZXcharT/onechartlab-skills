# 兼容性

## 目标运行时与验证边界

本 Skill 面向 HanaAgent，当前候选已通过仓库结构、策略 trace、资源链接和打包复检；正式发布前仍需在不覆盖同名现有 Skill 的干净环境中完成安装验证。所需语义包括：`subagent` 新建、`subagent_reply` 续线程、`subagent_close` 关闭、`current_status` 状态检查、`workflow` Agent 身份、`threadId` 生命周期、`access` 读写权限与可选 `session` 审计轨迹。它要求在每个获批 Plan 中显式记录 `delegate_agent_id`，默认模型继承 delegate Agent 配置。

## 静态格式参考

Claude Code 与 Codex 可参考本仓库的开放目录、frontmatter、单层 references 和相对链接格式；未验证其委派、线程、权限、工作流或跨会话语义。

## 未验证与失败方式

其他宿主和跨平台运行未验证。缺少必需 HanaAgent 能力时停止受影响流并报告 `BLOCKED`。Skill/prompt 的 Plan、验证和回复屏障是政策约束，宿主是否硬执行由宿主决定。
