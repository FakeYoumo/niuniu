
OP: u/cyber_niuniu  
原始地址: /r/FakeYoumo/comments/1cjqpt9/最强_ai_文爱软件_sillytavern_简单教程/  
正文:  
OP: u/EvenDogWontUseReddit  

 原始地址: /r/NEWTo_Cave/comments/1cjf041/最强_ai_文爱软件_sillytavern_简单教程/  

大名鼎鼎的 SillyTavern （江湖人称“酒馆”） 这个软件我早有耳闻，但因为试玩过觉得太复杂，我一度觉得这是只有 AI 文爱魔怔人才用的软件。但在红迪某位友友的强烈推荐下我试玩了一下，才发现这个软件的强大与好用。

这个软件能接入 OpenAI GPT、Anthropic Claude、Cohere、Google Gemini 等 LLM API 接口，每次你发送一条消息，他会自动给你的消息加上 NSFW 越狱指令，并且允许你自由编辑上下文，文爱体验比在这些 AI 的官网好得多。它还有角色卡功能，你可以把角色人设写成一张角色卡，然后你就可以和不同人物对话。

中文文档： [https://github.com/SillyTavern/SillyTavern/blob/release/.github/readme-zh\_cn.md](https://github.com/SillyTavern/SillyTavern/blob/release/.github/readme-zh_cn.md)

效果图：

https://preview.redd.it/lgjxjvel19yc1.png?width=639&format=png&auto=webp&s=cbad76d63c58e28b6c49548f3fbe5920619cc434

https://preview.redd.it/qg4c7tvl19yc1.png?width=639&format=png&auto=webp&s=2368c4282a3a722703b756f7b7f51d27fd33b990

下面是教程，这个教程假定你用的是 Windows 系统，用 Mac 的富蛆滚；如果你用的是安卓机，可以用 Termux 运行，用 iPhone 的富蛆滚

首先最好加一下这个 AI 文爱群 [https://discord.com/invite/B7Wr25Z7BZ](https://discord.com/invite/B7Wr25Z7BZ) 如果群邀请链接过期可以在 [https://rentry.org/teralomaniac\_clewd](https://rentry.org/teralomaniac_clewd) 看最新链接

在翻墙软件上打开 TUN 模式。广泛使用的 Clash 有 TUN 模式，这个模式通过创建虚拟网络接口来强制所有软件网络请求经过 Clash；如果是安卓上的翻墙软件，那么本来就是虚拟 VPN 接口所以什么都不用做。

Windows 教程在 [https://docs.sillytavern.app/installation/windows/](https://docs.sillytavern.app/installation/windows/) 如果看不懂英文可以用浏览器翻译功能，我推荐 staging 测试版本，有最新的功能

安卓教程在 [https://rentry.org/STAI-Termux](https://rentry.org/STAI-Termux)

安装完运行 Start 脚本，如果一切成功，首先会出现一个输入你的角色名称对话框，默认是 “User”，比如这里你可以输入你的角色名称是 “毛刃支” 然后确定

接下来点第二个插头按钮，选择 API 为 Chat Completion，然后去 [https://dashboard.cohere.com/api-keys](https://dashboard.cohere.com/api-keys) 注册拿一个 API KEY，这个是免费的 Command R+ 接口，每个月免费用 1000 次

点第一个预设设置按钮，点“对话补全预设”里的“导入预设”按钮，导入在 AI 文爱群得到的破限预设文件；然后重新在 API 设置选择一下 Cohere，这是因为这个软件的设计，切换预设会连 API 一起切换

Cohere 的 API 限制频率惩罚和存在惩罚必须有至少一个是 0，AI 文爱群的破限预设是为 Claude 设计所以它不符合这个要求需要自己修改。同时 Cohere 的 API 限制最大回复长度不能大于 4000 所以也需要自己修改成 4000。

接着是角色卡设置，是最后一个按钮。可以在 AI 文爱群随便偷一个先试试，注意角色卡文件可以是图片文件（信息藏在图片文件二进制流的末尾），所以角色卡经常用图片的形式发布，下载原图导入就行。

然后开始聊天试试，简单的教程就到这里
