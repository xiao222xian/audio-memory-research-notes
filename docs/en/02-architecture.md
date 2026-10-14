# System Architecture and Data Flow

English · [中文](../02-architecture.md)

## Responsibilities across the project

The project includes audio algorithms, a business-data boundary, an Agent content service, independent memory experiments, a voice Demo, and development tooling. The business backend supplies events and user context. Audio services form events; Agent services consume them to generate content. Memory experiments have their own ingestion and retrieval responsibilities.

| System | Main inputs | Processing | Outputs |
|---|---|---|---|
| Audio algorithms | Recording, time, known identity cues | Audio processing, transcription, fragment analysis, aggregation | Segments, Fragments, Basic Events |
| Business data | User information and events | Data management and business APIs | Context and event query results |
| Agent content | Task type, version, candidate events | Context preparation, model execution, validation | Structured cards, letters, insights, and related results |
| Memory experiments | Events and transcripts | Extraction, updates, retrieval, experimental card generation | Layered memories, content, and audit traces |
| Live voice Demo | Questions, speech, separate memory corpus | Routing, retrieval, reasoning, speech synthesis | Spoken answers, cognition panels, session records |
| Development platform | Runtime state, artifacts, feedback | Monitoring, review, replay, comparison | Diagnostic evidence, evaluations, handoff materials |

## How the data objects develop

A **segment** carries a time range, transcript, and speaker cues. A **Fragment** adds scene, topic, summary, continuity, and source semantics. A **Basic Event** aggregates related fragments while retaining their relationships. A **content result** is generated from selected events and linked back through references.

These objects serve different purposes: the card is an expression, the event is organized material, and the segment is closer to the input. Diagnosis follows these relationships back toward the source.

## Six engineering layers in the audio service

| Layer | Responsibility | Benefit |
|---|---|---|
| Entrypoints | Message consumers, CLI, scheduling, initialization | Consistent execution entry points |
| Domain orchestration | Downloads, computation, storage, downstream triggers | Side effects are concentrated in one layer |
| Pipelines | Compose computational stages | Independent testing and stage reuse |
| Algorithm units | Audio, speech, extraction, synthesis | Replaceable algorithms and models |
| Data interfaces | Object storage, event storage, business APIs | Separate external systems from computation |
| Infrastructure | Configuration, model calls, queues, logs, metrics | Shared supporting capabilities |

Independent data models define the structures exchanged between layers. Computational pipelines do not directly upload files, persist business data, or dispatch messages; domain orchestration connects those operations.

## Main services and experiments

Main services deliver material through stable event contracts. Experiments use separate preparation steps, run directories, and artifacts. Validated candidates can become scoped changes with regression evidence before entering the main flow. Public diagrams explain collaboration without exposing deployment topology, addresses, or credentials.

## Key contracts

1. **Recording to algorithms:** file availability, time information, and task metadata.
2. **Algorithms to events:** semantics and identity linked to segment boundaries.
3. **Events to generation:** explicit candidate sets, user ownership, and references.
4. **Generation to display:** distinguish generated content, skips, failures, and empty results.
5. **Experiments to engineering:** version, input conditions, evaluation definitions, and scope.
