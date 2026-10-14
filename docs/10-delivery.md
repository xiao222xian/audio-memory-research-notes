# 工程交付、技术栈与能力状态

[English](en/10-delivery.md) · 中文

## 项目交付版图

| 板块 | 工程成果 | 能力层级 |
|---|---|---|
| 音频算法服务 | 六条核心流水线、分层实现、接口与测试体系 | Core Platform |
| 事件理解 | Fragment、Basic Event、语义与来源信息 | Core Platform |
| 身份体系 | 准入评估、声纹表示、匹配及版本演进 | Core Platform |
| Agent 服务 | 多内容任务、执行器、Schema、上下文与 hooks | Core Platform |
| 运行平台 | API、队列、状态、SSE、Monitor、异常处理 | Platform Infrastructure |
| 记忆系统 | L0–L5、更新、召回、四阶段卡片与审计 | Experimental System |
| 实时语音 | 前后端、语音链路、问题路由、面板、轨迹 | Interactive Demo |
| 系统地图 | 交互式架构、模块和数据流说明 | Developer Experience |
| 质量工具 | 批量实验、听审、标注、比较与来源追踪 | Evaluation Platform |

## 技术栈概览

| 技术领域 | 项目采用的工程方式 |
|---|---|
| 服务端 | Python、FastAPI、Pydantic |
| 前端展示 | React、TypeScript、Vite；系统地图有独立前端工程 |
| 音频与语音 | FFmpeg、VAD、ASR、说话人切分、声纹嵌入与质量评分 |
| 推理运行 | 本地音频模型、vLLM 路径、多模态和文本模型调用 |
| Agent | 工具型执行器、单次调用、版本化提示与 hooks |
| 异步处理 | Redis Streams、消费者组、任务状态、死信与重试 |
| 数据组织 | 对象存储、事件数据接口、任务产物与记忆快照 |
| 交互与观测 | WebSocket、SSE、日志、OpenTelemetry 指标与 Monitor |
| 工程验证 | 模块测试、集成测试、批量回放、人工复核与指标脚本 |

## 能力成熟度

**Core Platform** 覆盖音频理解、事件组织、身份处理和 Agent 内容任务，是项目的核心技术底座。

**Platform Infrastructure** 提供异步任务、状态、监控、重试和可观测能力，支撑算法与内容服务运行。

**Experimental System** 用于验证多层记忆、更新和召回策略；当前重点消费路径为事件卡。

**Interactive Demo** 验证实时语音、记忆召回与认知界面的完整体验链路。

**Developer Experience** 与 **Evaluation Platform** 面向研发协作、系统理解和质量评估。

## 交付如何支持后续协作

各模块以职责、数据契约、运行方式、版本和验证体系组织交付，使算法、平台、产品和体验团队可以围绕同一条数据链路协作。

## 工程质量体系

项目通过模块测试、集成测试、固定样本回归、人工听审、端到端回放和运行监控覆盖不同层次的质量问题。算法指标、系统运行状态和最终内容体验分别评估，避免用单一数字概括整个平台。
