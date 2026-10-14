# 记忆系统实现细节

[English](en/15-memory-implementation.md) · 中文

## 写入不是一次“总结”调用

每个事件先成为保留原始转录的 MemCell，再并行产生 Episode、Atomic Fact、Profile 和 Foresight 候选。候选不会直接覆盖已有记忆，而是进入 Extract → Decide → Execute：

```text
Phase 1: 多事件并行 Extract
  └─ 单事件内 Episode ∥ Fact ∥ Profile ∥ Foresight

Phase 2: 按事件时间顺序 Commit
  └─ Episode/聚类 → Profile → Fact → Foresight → 索引同步

Phase 3: 当前事件 Commit 完成后
  └─ Search → Card Pipeline
```

Extract 只读同一事件输入，因此可以并行；Commit 会读写已经确认的用户状态，所以按时间顺序执行。这样既缩短等待时间，也避免后发生的事件抢先改变早期事件的判断上下文。

事实和画像的决策动作可以包括新增、更新、保持或删除。事实保留被替代链，检索命中旧事实时可以沿 `superseded_by` 找到最新版本，同时保留演化路径用于溯源。

## 双视角查询

一次事件查询既保留完整转录视角，也提取明确属于用户发言的视角。两路分别生成语义和关键词查询，再按记忆标识取同通道较高结果。没有可靠用户发言时不伪造第二路。

这解决了一个实际冲突：完整转录包含场景和旁人信息，用户发言更适合判断个人事实。两者直接拼成单一查询，可能让旁人的明确关键词压过用户本人的隐含表达。

## 语义与 BM25 融合

关键词原始分先用随查询词数变化的 sigmoid 归一化：

```text
bm25_norm = 1 / (1 + exp(-steepness × (raw_score - midpoint)))
```

随后和语义相似度融合：

```text
vdb_score = 0.6 × semantic_score + 0.4 × bm25_norm
```

最终排序继续考虑证据、记忆类型与时间：

```text
final_score = channel_score
            × evidence_multiplier
            × type_priority
            × recency_multiplier
```

Episode 与 Foresight 使用约 30 天半衰，Atomic Fact 使用约 90 天半衰；Profile 作为稳定背景使用固定处理。近因专用通道已按配额保证进入候选时，不重复施加时间惩罚。

这些参数通过版本配置管理，并由固定样本与下游内容评测共同验证。

## 配额合并而非只取一个总榜

检索先为 Profile 和最近事件预留位置，再用融合检索补齐剩余名额，最后按记忆标识去重。配额避免稳定背景或近期经历被大量相似事实完全挤出。

同日 Episode 可以从特定召回结果中排除，防止当前事件的另一个摘要被当成“过去记忆”再次注入。事实命中会展开到最新版本；下游仍可查看演化链。

## 四阶段事件卡各自看到什么

| 阶段 | 主要输入 | 输出 |
|---|---|---|
| Perceive | 当前 transcript 与一般世界知识 | 0–5 个观察 |
| Understand | 每个观察、相关 facts/foresights、完整 profile 与证据 | 关联理解 |
| Decide | 全部观察和理解摘要 | produce/skip 与主轴 |
| Write | 主轴、完整 transcript、证据片段、已关联记忆最新快照 | 标题、正文和诗句 |

Write 不重新读取全量检索 TOP40。发现相关材料发生在 Understand；Write 只接收已经选定的关联项和最新确认状态，承担表达而不是再次暗中改变证据集合。

每个阶段保存独立调用轨迹。错误可以定位为没有看到关键信息、关联错误、选择错误或最终表达越界，而不只给整张卡一个总分。

## 一致性和落盘

并发调用使用独立客户端与速率限制；trace 以阶段和任务键命名，避免线程相互覆盖。嵌入 trace 采用临时文件后原子替换。索引同步只在对应层 Commit 之后执行，当前事件完成写入后才供 Search 与 Card 消费。

Run 目录保存输入清单、步骤状态、记忆快照、卡片中间结果和调用轨迹，支持离线比较、问题定位与实验恢复。
