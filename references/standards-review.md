# 规范与模板核验 · 2026-10-31

这是维护记录，不是业务政策来源。没有名为“GitHub Skill标准”的独立强制认证；本包以Agent Skills开放规范为基础，按宿主能力适配。

- [Agent Skills规范](https://agentskills.io/specification)：必需name和description，目录名匹配；license、metadata等为可选。建议入口少于500行、详细资料按需读取。
- [官方参考实现](https://github.com/agentskills/agentskills/tree/69ef37e9424c0a7ea9dd2293b559e43ec8176379/skills-ref)：本轮固定此提交检查。上游说明此库用于演示，不能把通过验证称为认证或生产可靠性保证。
- [Anthropic模板](https://github.com/anthropics/skills/blob/ca45fc496a3436251f191354091d557da31c15b5/template/SKILL.md)：只提供name、description和正文骨架，不提供效果保证。
- [Anthropic编写建议](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)：简洁、按需加载、用真实任务评估。
- [OpenAI当前技能文档](https://learn.chatgpt.com/docs/build-skills)：当前本地用户目录为~/.agents/skills，仓库目录为.agents/skills；分发可复用技能建议打包插件。
- [旧OpenAI技能仓库](https://github.com/openai/skills)：本次打开时已标弃用并指向openai/plugins，不把旧目录当最新模板。
- [OpenAI插件示例](https://github.com/openai/plugins/tree/0722921d5542fc593105c27bd52630babd8b8c2a)：独立发布层，不是修改SKILL.md就等于已进入插件目录。
- [GitHub主题标签](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)：可帮助按主题发现仓库，不承诺搜索排名或访问增长。
- [MIT许可说明与文本](https://choosealicense.com/licenses/mit/)：经所有者本次授权选择MIT；标准文本见LICENSE。

快照只表示以上日期真实取得的资料。宿主功能、规范与入口可能改变，下次发布时重查；不把抓取时间当规范版本号。
