# 豆包与DeepSeek接入核验 · 2026-10-31

## 核对结果与适用范围

|入口|本次可以确认|本包处理|尚未验证|
|---|---|---|---|
|豆包普通对话/云盘|官方说明支持上传文件，云盘支持文件夹|提供UTF-8单文件skill.txt和启动语；不依赖模型自动读取本地目录|具体账号的TXT解析、全文读取和执行效果|
|豆包工作/上传技能|本次官方工作页未能访问；未取得可核验的导入格式说明|保留标准SKILL.md目录作为候选；没有入口则用单文件|原生导入、YAML字段接受范围、是否挂载成功|
|DeepSeek普通聊天|官方隐私政策明确存在文本、文件等对话输入|提供完整单文件，外链读取失败时粘贴全文；不叫原生安装|账号当前支持的附件类型、URL抓取和全文执行|
|DeepSeek Harness|官方文档接受<name>/SKILL.md，只扫描一层技能入口|使用同名顶层目录；项目可放.dsh/skills/<name>/SKILL.md，references随目录保留|本机客户端实际发现、加载和业务工具执行|

## 官方依据

- [豆包云盘使用须知](https://www.doubao.com/legal/ai_space)，第1.1与1.2条：文件/文件夹上传。文件夹存储不等于安装技能。
- [DeepSeek隐私政策](https://cdn.deepseek.com/policies/zh-CN/deepseek-privacy-policy.html)，智能对话部分：文本、图片、文件等输入；不是文件扩展名或大小限制说明。
- [DeepSeek Harness技能文档固定快照](https://github.com/deepseek-ai/deepseek-harness/blob/ce7073d51254c26cd63b22a60835b8f948deb447/docs/subsystems/skills.md)，Local discovery priority与Skill identity：项目.dsh/skills、.agents/skills，目录入口不递归扫描。
- [Harness官网](https://www.deepseek.com/en/harness/)：它是独立Harness产品，不能把其目录规则套到普通聊天网站。
- [豆包工作页](https://www.doubao.com/work)：本次访问失败，仅记录入口，不能据此确认导入操作。

未采用第三方教程冒充官方格式要求；未推测当前文件大小、数量或上下文上限。

## 单文件聊天方式

打开skill.txt或chat/skill.txt，把全文粘贴到对话；界面支持该类型附件时也可上传。再发chat/start.txt中的启动语。文件带资源索引与首尾标记；Markdown中的references路径可对应本文件内RESOURCE章节，不要求普通聊天访问本地文件。
模型只拿到链接但无法读取时，不得声称加载成功。若正文被截断，请分段提供，并在完整资料到齐后再执行。末尾标记是完整性提示，不是模型理解或行为正确的证明。

## 原生目录方式

解压folder包后，最外层就是技能同名目录。Harness项目布局示例：

```text
项目目录/
  .dsh/
    skills/
      xhs-content-loop/
        SKILL.md
        references/
```

不要再套一层“下载包/技能合集/技能名”后直接放进技能根目录。其他同名技能可能覆盖发现结果，先核对客户端列表与实际路径；本包不会自动移动用户目录。

## 验收与降级

首次仅根据实际取得的资料说明：当前是聊天文本方式还是原生目录方式、读到了哪些资料、缺哪些能力。不要在普通聊天声称“已永久安装”，不要为了展示成功而编工具调用。
没有联网则保留动态事实待核验；没有文件工具则在回复中提供成果和接力摘要；没有账号权限则只给草稿。不另装插件、不运行额外脚本、不发布内容来证明加载。
结构和导出完整性已在本地校验，客户端操作与模型业务效果尚未实测。ChatGPT等其他聊天宿主也可按实际能力使用此文本模式，但不把它列为本次新增实测。
