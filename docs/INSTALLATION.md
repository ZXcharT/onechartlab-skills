# 安装、更新与卸载

## 推荐方式：安装 `.skill` 文件

正式版本发布后，进入项目的 GitHub Releases 页面，下载：

```text
agent-cowork-control.skill
```

把 `.skill` 文件拖进 HanaAgent 聊天窗口上传，然后发送：

> 请安装这个 Skill。

HanaAgent 会检查安装包，再将它添加到当前 Agent 可使用的 Skills 中。

## 从源码安装

如果还没有 Release，或你希望检查源码：

1. 打开 [OneChartLab Skills GitHub 仓库](https://github.com/ZXcharT/onechartlab-skills)，点击 **Code**，再选择 **Download ZIP**。
2. 解压下载文件。
3. 找到以下目录：

```text
skills/agent-cowork-control/
```

4. 如果 HanaAgent 可以访问解压后的文件夹，在消息中粘贴 `agent-cowork-control` 文件夹的本地路径，然后发送：

> 请安装这个目录中的 Skill。

如果你的聊天界面支持上传文件夹，也可以直接上传整个 `agent-cowork-control` 文件夹。

安装时必须保留目录名 `agent-cowork-control`，并确保目录根部存在 `SKILL.md`。

## 第一次配置

复杂任务可能会由主 AI 请其他助手分别完成查资料、改文件或检查结果。第一次使用时，HanaAgent 会告诉你是否需要这样做，并让你确认。

你通常不需要自行设置文件夹。需要生成文件时，HanaAgent 会使用你已经授权的工作区，并尽量把不同任务的文件分开保存。

## 更新

下载新版本并重新安装整个 `agent-cowork-control` Skill。不要只替换其中一个协议文件，否则可能造成规则版本不一致。

更新不会自动删除以前任务产生的文件和证据。

## 卸载

在 HanaAgent 的 Skill 管理中停用或移除 `agent-cowork-control`。卸载 Skill 不会自动删除已经生成的项目、报告或运行目录。

## 安装失败时检查

- 安装对象是否是 `agent-cowork-control` 文件夹或 `.skill` 文件，而不是整个仓库根目录；
- 文件夹根部是否存在 `SKILL.md`；
- 文件夹名称是否仍为 `agent-cowork-control`；
- 当前 HanaAgent 是否允许使用子 Agent；
- 是否误用了面向其他 Agent 平台的安装位置。

平台与工具要求见 [兼容性说明](COMPATIBILITY.md)。
