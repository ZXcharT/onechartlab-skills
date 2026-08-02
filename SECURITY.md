# 安全政策

请勿在公开 issue、测试 fixture、日志或压缩包中提交 token、secret、Authorization 值、password、私有路径、会话标识或其他凭证。发现泄露时停止分发，保留最少必要证据，撤销受影响凭证，并在修复后重新扫描工作树与归档。

本项目的 Agent 门禁是公开的政策约束，不能替代宿主的权限隔离。HanaAgent 目标运行时缺少所需委派、权限或结构化/MCP 工具时应 `BLOCKED`，不得静默降级到网页或其他来源。

仓库公开后，优先通过 GitHub Private Vulnerability Reporting 报告安全问题；若该功能尚未启用，请使用维护者明确公布的私密联系渠道。不要在公开 issue 中披露可利用细节，并在公开讨论前留出合理修复窗口。
