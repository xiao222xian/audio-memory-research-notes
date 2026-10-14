# Engineering Deliverables, Technology, and Status

English · [中文](../10-delivery.md)

## Delivery map

| Area | Archived engineering outputs | Status represented publicly |
|---|---|---|
| Audio service | Six pipelines, layered implementation, interfaces, test descriptions | Main-service engineering with historical release records |
| Event understanding | Fragments, Basic Events, semantics, source information | Main processing chain |
| Identity | Admission evaluation, embeddings, matching, version evolution | Service and registration integration |
| Agent service | Content tasks, executor, schemas, context, hooks | Independent content service |
| Runtime platform | API, queues, state, SSE, Monitor, failure handling | Operational and development support |
| Memory | L0–L5, updates, retrieval, four-stage cards, audit artifacts | Independent experiment, not asserted merged into the main service |
| Realtime voice | Frontend/backend, voice paths, routing, panel, traces | Single-user Demo and research tool |
| System map | Interactive architecture, modules, data flow | Collaboration and presentation tool |
| Quality tools | Batch runs, listening, labels, comparison, lineage | Offline evaluation and development |

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

This describes archived engineering choices, not a procurement specification or availability commitment.

## Interpreting status

**Main-service engineering** is supported by code, interfaces, configuration, and historical changes. The project is concluded; this publication does not verify that those services remain online.

**Experimental implementations** have workflows and artifacts but are not presented as capabilities serving all users. The memory consumer is an event-card path; memory-backed letters and memoirs require their own implementation and validation.

**Demos** demonstrate interactions and technical paths. Multi-user operation, long-term reliability, and device performance need separate acceptance.

**Historical or changing capabilities** retain research value. Spin has removal work documented as pending deployment; this material claims neither completed production removal nor current availability. L6/L7 slow thinking is outside the current memory path.

## Handoff and public scope

Modules are documented by responsibilities, contracts, execution, versions, and evidence. The public project description explains the system; private archives retain implementation and recovery records. User data, management addresses, and raw debug context remain private.

## Publication verification

Documentation and selected implementation files were checked against the archive. Existing aggregates, links, bilingual coverage, examples, and file integrity are checked locally. This publication does not reinstall the original system, rerun audio models, or perform live deployment acceptance.
