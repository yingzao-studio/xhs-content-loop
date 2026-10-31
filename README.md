<!-- PUBLIC-ACCESS:START -->
## 所有人可获取：DeepSeek · 豆包 · ChatGPT

**小红书资料变内容**

- [完整技能文本，复制后交给模型](https://raw.githubusercontent.com/yingzao-studio/xhs-content-loop/main/%E9%80%9A%E7%94%A8%E6%8F%90%E7%A4%BA%E8%AF%8D.txt)
- [ZIP下载](https://github.com/yingzao-studio/xhs-content-loop/releases/download/public-20261031/xhs-content-loop.zip)
- [三平台使用步骤](三平台使用说明.md)

公开下载不代表官方目录收录；模型能否读附件、联网或自动读取链接取决于实际环境。
<!-- PUBLIC-ACCESS:END -->

# 小红书资料变内容 · v2.1.0

把已有文字、图片与视频资料整理为7天选题，并完成首篇图文草稿。 不虚构经历和数据，不保证流量或成交。默认只制作草稿。

## 下载与安装

- [下载v2.1.0技能包](https://github.com/yingzao-studio/xhs-content-loop/releases/latest)
- [更新与版本下载](https://github.com/yingzao-studio/xhs-content-loop/releases/latest)

解压后，将完整的`xhs-content-loop`文件夹放入当前工具的技能目录。Codex常用目录为`~/.agents/skills`；其他宿主以其配置为准。新开对话或刷新技能列表后调用。不要只复制SKILL.md而遗漏参考文件。

## 一句话开始

> 使用 xhs-content-loop，盘点我上传的资料，给7天选题并完成首篇图文草稿。缺资料最多先问三个关键问题，不编体验或互动数据，本次只做草稿，不发布。

最少输入、适用人群和默认成果见[技能入口](SKILL.md)。不知道受众和目标可以留空，AI先根据资料提出待确认方向。

## 先看交付样子

- [原创演示：成稿、逐图稿与7天计划](examples/public-demo.md)
- [调用提示词](references/prompt-template.md)
- [联用时的共用记录](references/shared-contract.md)
- [跨环境适配](references/agent-adaptation.md)
- [安装说明](安装与使用.md) / [更新说明](更新说明.md) / [验证结果](验证结果.md)

演示为原创虚构材料，不是真实客户成绩。文字稿不代表已成图，未发布不代表已验证流量。

## 配合另一个技能

xhs-content-loop负责素材、排期与进度；xhs-viral-replica负责参考拆解与单篇创作。两者可独立使用，联用时共用事实、素材及证据编号，不重复询问已确认信息。

## v2更新

补充新手入口和缺资料处理，先展示成稿再附分析；移除对私人附件的必需依赖。通用包不含私人原始Excel、第三方原图、账号凭据或历史业务台账。旧文件可能仍在仓库历史中，本次不重写历史、不改变仓库可见性。

## 能力与验证边界

技能不自带账号登录、联网、图片模型或发布权限。不支持技能目录的聊天环境可使用[通用提示词](通用提示词.txt)，能力缺失时按说明降级。跨环境属于适配设计，未声称所有国内外模型实测通过。

本轮完成基础结构审计和四种情形的同一助手手工试跑，未完成独立跨模型回归、真实平台发布或增长效果验证。运行`python scripts/validate_package.py`可检查基础结构；它不是模型效果评测。


## 标准、维护与许可

版本2.1.0。采用[MIT许可证](LICENSE)，第三方与历史素材的范围见[许可说明](THIRD_PARTY.md)。[本次官方规范核验](references/standards-review.md)列明来源与快照版本。
当前OpenAI文档列出的本地目录为~/.agents/skills及项目.agents/skills。旧版本或宿主可能有其他目录，按该工具实际技能列表确认，避免安装同名副本。此电脑已有的发现目录不在此次更新中迁移。
使用本技能无需安装Python依赖；维护校验才需要：先运行`python -m pip install -r requirements-dev.txt`，再运行`python -X utf8 scripts/validate_package.py`。GitHub检查配置已附带，但只有提交仓库并实际跑完后才可称CI通过。
[行为评估用例](evals/README.md)独立于文件校验，目前尚未完成独立模型实测。不把手写演示或结构通过称为成功案例。

## English quick start

Use the skill with your own source material. It produces a reviewable draft or a beginner's next action, keeps unknown facts explicit, and never assumes account access. Live research requires browsing; image production requires an image tool. Plain chat users can upload the bundled text instructions. Examples are synthetic, not customer results.

## 使用反馈

反馈时提供：使用的模型与工具、去敏后的最小输入、预期结果、实际结果及失败阶段。不要提交证件、凭据、买家信息或无权公开的截图。优先修复能复现的失败，再增加新功能；不以功能数量代替实用性。
