# Layered Memory, Updates, and Retrieval Research

English · [中文](../07-memory.md)

## From stored events to continuing understanding

The independent memory implementation explores how ongoing events become updateable, traceable memories. Raw conversation supports facts; facts and events support longer-term observations; abstraction retains its connection to lower-level evidence.

This chapter describes an experimental implementation, not a claim that it has been merged into the main Agent production service.

## L0–L5 responsibilities

| Layer | Content | Purpose |
|---|---|---|
| L0 BasicInfo | Product-confirmed information | Identity anchor |
| L1 MemCell | Original conversation unit | Source evidence and traceability |
| L2 AtomicFact | Independently referencable facts | Factual queries and updates |
| L3 Episode | Event narrative | Organize an experience and its context |
| L4 Foresight | Derived forward-looking information | Evidence-linked, time-sensitive expectations |
| L5 Profile | Relatively stable observations | Longer-term context |

These are not successive compression stages that discard original text. Different types retain evidence and update rules, preventing an unsupported generalization from replacing historical facts.

## Updating memory

Facts, profiles, and foresights use extraction, decision, and execution stages. Extraction proposes candidates; decision compares them with existing information; execution applies updates. Explicit intermediate judgments reduce uncontrolled overwriting.

Independent extraction from shared read-only input can run concurrently. Updates that depend on prior results run in order. Event commits and retrieval snapshots have explicit boundaries so generation does not consume partially updated state.

## Retrieval channels

The implementation combines semantic and keyword matching with memory-specific channels. Full-conversation and user-speech views separate the discussion as a whole from the user's own statements. Scores and quotas organize candidates for the consuming task.

Semantic matching helps with paraphrases; keywords help with explicit names and details; profiles supply stable background; facts and episodes supply referencable content. Context composition follows the task rather than a universal prompt bundle.

## Four-stage experimental event cards

```mermaid
flowchart LR
    A[Perceive the event] --> B[Understand with memory]
    B --> C[Decide produce or skip]
    C --> D[Write the content]
```

Perceive extracts observations. Understand associates relevant memories. Decide selects whether and what to express. Write renders the selected material. Intermediate results and model traces help locate errors in observation, association, selection, or wording.

The archived memory consumer is an event-card path. Letters and profile tasks in the main Agent service have separate implementations; their existence does not prove integration with this memory pipeline.

## Related research paths

Historical L6/L7 slow-thinking work is outside the current experimental main path. The realtime voice Demo uses a separate corpus structure whose directory layer names are not equivalent to this L0–L5 model. See the [memory implementation details](15-memory-implementation.md) for scoring, update ordering, and stage-specific contexts.
