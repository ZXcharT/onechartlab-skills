# 贡献指南

提交前保持最小范围，不引入依赖、不放入运行轨迹、本机配置、缓存或凭证。Skill 目录名必须与 frontmatter `name` 一致；参考资料只放在单层 `references/`，链接使用 Skill 根相对路径。

变更安全规则时：保留安全短摘要，更新对应协议、T01–T14 fixture/断言和 `CHANGELOG.md`；不得把政策约束表述成宿主硬执行机制。运行 `python3 scripts/check_repo.py` 与 `python3 scripts/build_release.py`，在干净解压目录复检 ZIP。

新增运行时声明必须标示“实际验证”“静态格式参考”或“未验证”。不要提交第三方内容，除非许可和归属已明确审查。
