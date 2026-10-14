# 数据契约与异步运行时

[English](en/14-contracts-runtime.md) · 中文

## 为什么需要分层契约

平台处理的是长耗时、概率型任务。输入校验、模型输出和业务返回如果共用一个结构，模型策略的小调整就可能破坏调用方。Agent 服务因此使用三层 Schema：

| 契约 | 负责什么 | 典型失败 |
|---|---|---|
| Input Schema | 用户、任务版本和业务参数 | 缺字段、类型错误、越权事件 |
| Agent Output Schema | 约束模型产生的 JSON | 字段缺失、枚举或嵌套结构错误 |
| Response Schema | 稳定 HTTP 与消息流结果 | 内外字段映射错误 |

例如模型内部可以输出 `decision=produce|skip`，适配层再转为业务侧 `found` 和内容对象。提示词可以迭代，对外契约仍保持清晰。

## Fragment 与 Basic Event

Fragment 是片段理解单元，包含时间、转录、音段、场景、来源、说话人分析和主题信息。Basic Event 记录它由哪些 Fragment 组成，并聚合完整转录、身份、标题、摘要和主题。

合成契约示例：

```json
{
  "event_id": "synthetic-event-1",
  "time_range": {"start": "2026-01-01T10:00:00Z", "end": "2026-01-01T10:12:00Z"},
  "source_fragments": ["synthetic-fragment-1", "synthetic-fragment-2"],
  "participants": [{"role": "user", "certainty": "confirmed"}],
  "content_origin": "conversation",
  "summary": "A synthetic example event",
  "evidence": [{"segment_id": "synthetic-segment-1", "speaker_role": "user"}]
}
```

这不是内部真实接口，但体现了平台必须保留的关系：事件时间、组成片段、身份确定程度和证据引用。

## 任务配置怎样成为插件

每个任务版本将运行时、模型、超时、重试、沙箱使用方式和输出结构写入配置；模板负责组织任务指令；Schema 和 hooks 负责程序化规则。启动时注册表读取可用版本并生成对应入口。

执行顺序可以概括为：

```text
Input 校验
→ 准备用户时间与候选事件
→ 建立任务工作区或内存上下文
→ pre-execute hooks
→ 构造提示
→ 模型执行与流式事件
→ Agent Output 校验
→ async guards
→ result adapters
→ Response 校验
```

工具型 Agent 的工作区包含事件文件、索引和本次任务指令；单次调用路径直接在内存中组织有限候选。每个任务创建独立工作区，不将用户缓存直接作为可写任务目录。

## Redis Streams 任务生命周期

API 校验请求并生成任务标识，将 `pending` 状态和消息写入输入流。Consumer 使用消费者组读取消息，将状态改为 `running`，调用统一 Executor，最后写入完成或失败状态及输出流。调用方可以轮询状态或订阅实时事件。

Worker 在拉取新消息前取得并发令牌，避免读入超过本机处理能力的任务。后台回收逻辑识别长期未完成的 pending message，并在获得 worker 容量后重新处理。每个处理任务在 `finally` 中释放并发令牌。

## ACK、重试和死信的语义

- Executor 已经形成明确业务失败结果时，任务状态被记录并 ACK，避免消息一直留在待处理列表；
- 未捕获异常在记录错误后进入 dead-letter，再 ACK 原消息；
- 模型结构校验或业务 guard 可在任务内部按版本配置重试；
- Consumer 连接异常采用退避恢复，与单条业务任务重试分开；
- 强制生成等业务条件由 guard 判定，不能把合法 `skip` 和技术失败混成同一状态。

运行时采用 at-least-once 交付语义；调用方通过稳定任务标识与幂等策略管理业务副作用，而不是依赖队列提供 exactly-once 保证。

## 可观测数据

轻量状态保存任务状态、结果摘要、模型、token、费用和错误。文本增量、工具调用与阶段事件通过实时通道传递；大体积上下文和调试材料保存为独立 artifact，仅在状态中留引用。

这种分层使 Monitor 可以展示任务列表、过程、失败和重试，同时避免 Redis 状态对象无限增长。指标按整体任务和具体阶段记录，能够区分上下文准备、模型执行和后处理耗时。
