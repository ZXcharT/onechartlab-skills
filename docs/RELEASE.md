# 本地发布流程

1. 在候选根执行 `python3 scripts/check_repo.py`。
2. 执行 `python3 scripts/build_release.py`。它生成顶层为 `onechartlab-skills/` 的 ZIP 和 `SHA256SUMS`，排除 Git、缓存、日志、会话轨迹、运行控制文件、本机配置与测试残留。
3. 构建器会在干净临时目录解压 ZIP 并再次运行仓库检查；失败即退出非零。
4. 对工作树与归档执行隐私扫描，人工核对第三方来源和将来 Git 历史。
5. 维护者可再使用兼容 Agent Skills 规范的打包器，将 `skills/agent-cowork-control/` 生成独立 `.skill` 安装包；随后重跑 `python3 scripts/build_release.py`，构建器会把现有 `.skill` 与仓库 ZIP 的摘要共同写入最终 `SHA256SUMS`。
6. 运行统一归档验证：`python3 scripts/verify_artifacts.py --zip <repo.zip> --skill <skill.skill> --sha256sums <SHA256SUMS>`。它检查顶层结构、危险路径、缓存/日志/本机状态、隐私模式、Skill 包内链接和哈希。
7. 正式 Release 前，在不会覆盖现有同名 Skill 的干净 HanaAgent 环境完成安装验证，并据实更新兼容矩阵。

本流程只生成本地候选产物，不创建远程仓库、发布、提交、推送或修改外部对象。
