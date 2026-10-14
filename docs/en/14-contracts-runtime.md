# Data Contracts and Asynchronous Runtime

English · [中文](../14-contracts-runtime.md)

## Three contract layers

Long-running probabilistic tasks need separate request, model-output, and business-response contracts:

| Contract | Responsibility | Typical failure |
|---|---|---|
| Input Schema | User, task version, business parameters | Missing fields, types, unauthorized events |
| Agent Output Schema | Generated JSON | Missing fields, invalid enums or nesting |
| Response Schema | Stable HTTP and stream result | Incorrect internal-to-external mapping |

For example, a model can produce `decision=produce|skip`; an adapter translates it into a business-facing `found` value and content object. Prompt behavior can evolve without leaking every internal shape to callers.

## Fragment and Basic Event

A Fragment contains time, transcript, source segments, scene, content origin, speaker analysis, and topics. A Basic Event records its component Fragments and aggregates their transcript, identities, title, summary, and topics.

Synthetic public example:

```json
{
  "event_id": "synthetic-event-1",
  "time_range": {"start": "2026-01-01T10:00:00Z", "end": "2026-01-01T10:12:00Z"},
  "source_fragments": ["synthetic-fragment-1", "synthetic-fragment-2"],
  "participants": [{"role": "user", "certainty": "confirmed"}],
  "content_origin": "conversation",
  "summary": "A reconstructed example event",
  "evidence": [{"segment_id": "synthetic-segment-1", "speaker_role": "user"}]
}
```

This is not an internal API, but it demonstrates the necessary relationships among time, fragments, identity certainty, and evidence.

## Task plugins

Each task version configures runtime, model, timeout, retry, sandbox behavior, and output schema. Templates organize instructions; schemas and hooks enforce programmatic rules. The registry discovers enabled versions and exposes their entry points.

```text
input validation
→ resolve user time and candidate events
→ prepare workspace or in-memory context
→ pre-execute hooks
→ build prompt
→ model execution and streamed events
→ Agent Output validation
→ asynchronous guards
→ result adapters
→ Response validation
```

A tool-using Agent receives event files, an index, and task instructions in an isolated workspace. A single-call task assembles a bounded candidate set in memory. User caches are not treated as writable task workspaces.

## Redis Streams lifecycle

The API validates a request, generates a task identifier, writes `pending` state, and publishes to an input stream. A consumer-group worker marks it `running`, invokes the shared Executor, and writes completed or failed state plus the output stream. Callers can query state or consume realtime events.

Workers acquire concurrency capacity before reading more work, preventing them from claiming tasks beyond local capacity. A reclaim loop detects stale pending messages and reschedules them after worker capacity becomes available. Semaphore release is guaranteed around processing.

## ACK, retry, and dead-letter semantics

- A handled business failure is recorded and ACKed so it does not remain pending forever.
- An uncaught exception is recorded, copied to the dead-letter stream, then ACKed from the source stream.
- Schema failures and business guards may retry inside the task according to version configuration.
- Consumer connection recovery uses separate backoff from task-level retries.
- A forced-generation guard distinguishes a rejected skip from infrastructure failure.

These mechanisms support recoverable processing in an at-least-once environment. They do not establish exactly-once business side effects by themselves; stable task identifiers and idempotency still matter.

## Observability data

Lightweight state stores status, a result summary, model, token and cost metadata, and errors. Text deltas, tool calls, and stages flow through realtime events. Large prompts and debug outputs become separate artifacts referenced from state.

Monitor can therefore inspect tasks, progress, failures, and retries without allowing Redis state objects to grow without bound. Metrics separate total task time from context preparation, model execution, and post-processing.
