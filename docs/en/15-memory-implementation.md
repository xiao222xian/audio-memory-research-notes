# Memory Implementation Details

English · [中文](../15-memory-implementation.md)

## Ingestion is more than one summarization call

An event first becomes a MemCell retaining its transcript. Episode, Atomic Fact, Profile, and Foresight candidates are then extracted concurrently. Candidates pass through Extract, Decide, and Execute rather than overwriting confirmed memory directly.

```text
Phase 1: Extract across events concurrently
  └─ Within each event: Episode ∥ Fact ∥ Profile ∥ Foresight

Phase 2: Commit in event-time order
  └─ Episode/cluster → Profile → Fact → Foresight → index sync

Phase 3: After the current event is committed
  └─ Search → Card Pipeline
```

Extraction reads shared immutable event input and can run concurrently. Commit reads and mutates confirmed user state and therefore follows event order. This reduces wall-clock time without allowing later events to change the context used to reconcile earlier ones.

Decisions can add, update, keep, or delete information. Facts retain supersession links. If retrieval encounters an old fact, it can follow `superseded_by` to the latest version while retaining the evolution path for provenance.

## Dual-view queries

Each event query has a full-transcript view and, when reliable, a user-speech view. Semantic and keyword retrieval run for both views; duplicate memory identifiers keep the stronger result within each channel. A second view is not invented when user speech cannot be identified.

The full transcript carries scene and other participants. User speech is more appropriate for personal facts. Collapsing both into one query can allow explicit keywords from another speaker to dominate the user's implicit meaning.

## Semantic and BM25 fusion

Raw BM25 scores are normalized using a sigmoid whose midpoint and steepness vary with query length:

```text
bm25_norm = 1 / (1 + exp(-steepness × (raw_score - midpoint)))
vdb_score = 0.6 × semantic_score + 0.4 × bm25_norm
```

Final scoring adds evidence, type, and recency factors:

```text
final_score = channel_score
            × evidence_multiplier
            × type_priority
            × recency_multiplier
```

Episodes and Foresights use an approximate 30-day half-life, Atomic Facts an approximate 90-day half-life, while Profile is handled as stable context. Items admitted through a dedicated recency quota are not penalized for recency a second time.

These parameters are versioned and evaluated through fixed samples and downstream content review.

## Quota merging

Retrieval reserves slots for Profile and recent items, fills the remaining capacity from fused retrieval, and deduplicates by memory identifier. Quotas prevent stable background or recent experiences from being displaced entirely by many similar facts.

Same-day Episodes can be removed from specific retrieval results so another summary of the current event does not masquerade as past memory. Fact hits resolve to the latest version while retaining their evolution chain.

## What each card stage sees

| Stage | Main context | Output |
|---|---|---|
| Perceive | Current transcript and general world knowledge | Zero to five observations |
| Understand | Each observation, relevant facts and foresights, full Profile, evidence | Linked interpretations |
| Decide | All observations and interpretation summaries | Produce/skip and one narrative axis |
| Write | Narrative axis, transcript, evidence snippets, latest linked-memory snapshots | Title, body, poem |

Write does not receive the full top-40 retrieval set. Discovery happens in Understand. Write receives only selected links and their latest confirmed snapshots, separating evidence selection from expression.

Each stage has a separate trace, allowing a reviewer to distinguish missing perception, bad association, wrong selection, and unsupported wording.

## Consistency and artifacts

Concurrent requests use isolated clients and rate controls. Trace names include stage and task keys. Embedding traces use temporary files followed by atomic replacement. Index synchronization occurs only after the corresponding memory layer commits; Search and Card consume the event only after its write sequence completes.

Run directories retain manifests, step state, memory snapshots, card intermediates, and model traces for comparison, diagnosis, and recovery.
