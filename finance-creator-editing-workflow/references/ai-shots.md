# AI 镜头增强流程

## 用途

本流程把 Vidmuse 或其他已实际连接的生成器，接入现有的财经混合拼贴剪辑。生成镜头只说明抽象概念、情绪和转场；真人讲述、讲解者小窗、真实主体贴图、实际事件素材、纸片标题和箭头圈注仍是主体。

一条约 60 秒视频通常生成 4–8 个镜头，每个 2–3 秒。根据语义安排在真人主画面之间，不连续铺满，也不拿生成画面替代需要真实依据的财经事实。

## 每条视频的操作

1. 写入已确认口播文案，然后启动工程：

```sh
finance-edit prepare <工程目录> --topic '主题' --script <文案.txt>
```

2. 完成口播顺稿，确认本条真人出镜、原声、双语字幕、BGM 选择和事实核验范围。文案变动后要重新生成计划，不能沿用旧提示词。

3. 生成 AI 镜头计划：

```sh
finance-edit ai-plan <工程目录> --provider vidmuse --shots 8 --duration 3 --ratio 9:16
```

命令写入：

```text
<工程目录>/.finance-workflow/ai-shots/
├── manifest.json
└── vidmuse-prompts.md
```

先在 `vidmuse-prompts.md` 删除不需要的镜头，再把选中的提示词复制到你已登录的 Vidmuse。当前本地入口只生成计划，不检测、登录或消耗 Vidmuse 额度。

4. 每条生成素材通过画面检查后登记。登记会复制原文件、计算 SHA-256，并用 `ffprobe` 验证视频可解码且为竖屏：

```sh
finance-edit ai-register <工程目录> --shot-id ai01 --file <Vidmuse导出.mp4> --request-id <可选请求ID> --model <实际模型名>
```

5. 逐条确认。AI 镜头只有在可商用权限和与口播的关系都写清楚后，才可进时间线：

```sh
finance-edit ai-review <工程目录> --shot-id ai01 \
  --rights-status approved --rights-note '已核对当前 Vidmuse 账户的导出使用条款' \
  --semantic-status approved --semantic-note '抽象展示本句的资金流动关系，不代表具体事件现场' \
  --used-in-timeline
```

6. 在 Remotion/Vox 或当前剪辑器中混排：每 2–3 秒改变或新增一个有意义的画面状态。AI 镜头可用作短插片、背景动势或纸片层的动态底，不得成为连续全屏视频墙。按已有流程重建 PCM 派生字幕、场景和音效，然后做技术和编辑两轮验收，最后运行 `finance-edit check <工程目录>`。

## 提示词原则

- 画幅为 `9:16`，时长 2–3 秒，留底部双语字幕和顶部声明的安全区。
- 提示具体动作和构图，如“文件组合成交易关系”，不要只写“高级金融科技背景”。
- 加入 `no readable text, logo, watermark, real person face, fake news, product UI` 等约束。
- 现实人物、特定企业产品界面、签约、新闻现场、数字图表和市场事实优先真实来源。生成画面不能替代它们。
- 有实际新闻、产品、交易或人物的台词时，AI 镜头只能作为说明性补充，真实素材和来源记录仍是主证据。

## 工程记录

`manifest.json` 记录每个镜头的口播句、用途、提示词、服务、模型、请求 ID、文件、哈希、解码信息、权限说明和语义审核。它是素材证据的一部分，不包含 API key、登录 cookie、私人原声或人像。

工程 `status` 会显示已计划、已登记、可进时间线和待审核的 AI 镜头数量。生成服务是否连接、实际模型名称及消耗额度，只能以当前账户页面或导出记录为准。
