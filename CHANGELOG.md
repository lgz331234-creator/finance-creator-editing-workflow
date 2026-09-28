# Changelog / 变更记录

## 1.6.0 · 2026-09-29

- 同一工程记录一个主剪辑任务；新任务接手需明确交接，完成后释放记录。工具不会自动停止另一任务。
- 文案文件被改动、文案预检或音画重建仍待办时，导出检查返回阻断；短状态卡继续减少重复上下文。
- 单条视频的无 BGM 等明确例外只保存在该项目，不覆盖其他视频的默认声音规则。
- 当前默认画面为真人讲述、小窗、真实贴图及动态素材混合，按台词语义更新；必要时插入全屏画面。

## 1.0.0 — 2026-09-25

- Set sample duration per user request; the current FREYA showcase is 60 seconds, with a suit-portrait cover and voice-over body, not a talking-head opening.
- Initial public release of the Finance Creator Editing Workflow / 财经博主剪辑工作流.
- Captured portrait-cover and full-screen visual defaults, with no bottom production-note layer.
- Required one PCM-sample-derived timeline for narration, captions, semantic scene cuts, effects, and duration; documented the stale-metadata drift failure and its repair principle.
- Added Korean/Japanese voice and main-caption workflows with English secondary captions and translated graphic text.
- Added verification of the actual export, honest listening status, private run logs, and a separate reviewed public-release process.
- Included original bilingual prompts and installation instructions. No private assets or third-party implementations are included.

后续只记录已确认、可公开的默认规则变化。实验、个人媒体、私有路径及单次交付日志不进入公开变更记录。

Only confirmed public workflow changes belong here. Experiments, personal media, private paths, and per-delivery logs remain private.

## 2026-09-25 · 开头音效规则

- 新增当前创作者首秒综艺音效偏好，覆盖当前修改及后续多语视频。
- 首句人声优先，混合参考先分离，保留试听状态；参考音频不随公开技能分发。

## 2026-09-26 · 质量与变化规则

- 将蔡公子成片作为人声响度与清晰度的技术参考，不复制其声音身份；人声必须清楚，BGM 适度压低。
- 连续视频轮换 BGM，记录最近使用曲目，避免每条成片使用同一首音乐。
- 每次试听检查口播卡顿、重复词、吞字、断句和英文品牌发音，并据此重建字幕与画面时间轴。
- 每条视频轮换实拍、动图、图表、行业截图、贴图样式、强调字幕、动效和转场；素材必须与台词对应，避免重复画面造成视觉疲劳。
- 借鉴直男财经的黄金开头、强反差、口语化、高密度切镜和图表叙事方法，不复制其脸、声音、文案、水印或素材。
- 成片交付前执行两遍独立复查：第一遍检查解码、音画同步、响度、字幕和卡顿；第二遍检查内容对应、素材重复、视觉冲击和品牌发音。

## 2026-09-27 · 紧凑上下文交接

- 每个任务只读取一次最新版入口，后续阶段只传递版本、项目路径、定稿标识、变更差异和最近检查结果。
- 不重复携带完整对话、未变化的文案、旧分镜和运行日志；文案修改只重建受影响的音频、字幕、画面和音效时间段。
- 保留文案顺口、品牌发音、音画同步、素材语义匹配和双轮成片复查，不以减少上下文替代质量检查。
# 1.4.6

- 增加本地最新版入口：工程状态卡、版本门禁、文案变更后的字幕/时码阻断。
- 增加联网资料与素材候选流程：逐句记录来源、许可、语义对应关系和文件哈希；未核验候选不能直接下载进成片。
- 支持 Wikimedia Commons 图片/视频候选检索与公开网页资料快照；不包含私人素材、原声、人像、账号配置或凭据。
