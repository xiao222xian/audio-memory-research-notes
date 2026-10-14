# Engineering Deliverables, Technology, and Status

English · [中文](../10-delivery.md)

## Delivery map

| Area | Engineering outputs | Capability tier |
|---|---|---|
| Audio service | Six pipelines, layered implementation, interfaces, test system | Core Platform |
| Event understanding | Fragments, Basic Events, semantics, source information | Core Platform |
| Identity | Admission evaluation, embeddings, matching, version evolution | Core Platform |
| Agent service | Content tasks, executor, schemas, context, hooks | Core Platform |
| Runtime platform | API, queues, state, SSE, Monitor, failure handling | Platform Infrastructure |
| Memory | L0–L5, updates, retrieval, four-stage cards, audit artifacts | Experimental System |
| Realtime voice | Frontend/backend, voice paths, routing, panel, traces | Interactive Demo |
| System map | Interactive architecture, modules, data flow | Developer Experience |
| Quality tools | Batch runs, listening, labels, comparison, lineage | Evaluation Platform |

## Technology overview

| Domain | Approach |
|---|---|
| Backend | Python, FastAPI, Pydantic |
| Frontend | React, TypeScript, Vite; separate system-map frontend |
| Audio and speech | FFmpeg, VAD, ASR, diarization, embeddings, quality scoring |
| Inference | Local audio models, vLLM path, multimodal and text model calls |
| Agent execution | Tool-using and single-call runtimes, versioned prompts, hooks |
| Asynchronous work | Redis Streams, consumer groups, task state, dead letters, retries |
| Data | Object storage, event interfaces, artifacts, memory snapshots |
| Interaction and observability | WebSocket, SSE, logs, OpenTelemetry, Monitor |
| Verification | Module and integration tests, replay, human review, metric scripts |

## Capability maturity

**Core Platform** covers audio understanding, event organization, identity, and Agent content tasks.

**Platform Infrastructure** supplies asynchronous execution, task state, monitoring, retry, and observability.

**Experimental System** validates layered memory, update, and retrieval strategies; its current content path focuses on event cards.

**Interactive Demo** validates the full realtime voice, memory retrieval, and cognition-interface experience.

**Developer Experience** and the **Evaluation Platform** support system understanding, collaboration, and quality assessment.

## Handoff model

Modules are delivered through clear responsibilities, data contracts, runtime modes, versions, and validation systems, enabling algorithm, platform, product, and experience teams to work on one shared data chain.

## Engineering quality system

Module tests, integration tests, fixed-set regression, listening review, end-to-end replay, and runtime monitoring cover different classes of failure. Algorithm metrics, system health, and final content quality are evaluated separately rather than collapsed into one platform score.
