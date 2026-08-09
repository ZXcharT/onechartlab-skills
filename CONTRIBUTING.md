# 贡献指南

开始前按 [`AGENTS.md`](AGENTS.md) 判断工作阶段。保持最小范围，不引入无关依赖，不提交运行轨迹、本机配置、缓存或凭证。Skill 目录名必须与 frontmatter `name` 一致；参考资料只放在单层 `references/`，链接使用 Skill 根相对路径。

## 按阶段验证

- 探索：只验证受影响方案，不默认更新全部测试、CHANGELOG、commit 或发布包。
- 正式实现：保留安全短摘要，更新受影响的协议、fixture、断言和文档；运行 `python3 scripts/check_repo.py` 与 `git diff --check`。
- 发布：更新版本和 CHANGELOG，完整执行 [`docs/RELEASE.md`](docs/RELEASE.md)，包括构建、统一归档验证、干净解压和适用的安装验证。

不得把政策约束表述成宿主硬执行机制。新增运行时声明必须标示“实际验证”“静态格式参考”或“未验证”。不要提交第三方内容，除非许可、归属和再分发边界已经审查。
