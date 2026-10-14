# Audio Algorithm Implementation Details

English · [中文](../13-audio-implementation.md)

## From a recording to identity-aware segments

Audio processing is a configurable sequence rather than an unconditional stack:

```text
decode and normalize sample rate
  → optional separation / enhancement / dereverberation
  → voice activity detection and diarization
  → interval filtering and alignment
  → ASR
  → per-segment speaker embeddings
  → timeline merge and structured output
```

Pipelines accept bytes and version configuration and return computational results. Domain orchestration owns download, upload, persistence, and downstream messages, allowing algorithms to be reused in tests, batch experiments, and service tasks.

## ASR and segmentation

The audio engine supports Whisper, FunASR, and vLLM-backed execution paths. Diarization supplies candidate intervals; VAD coverage removes intervals without sufficient speech; duration, character-rate, and repetition checks address short noise and pathological outputs.

In a gated mode, only intervals supported by both diarization and speech activity are transcribed. An empty list can mean that no valid speech survived gating, while `None` or an exception represents execution failure. Only the latter should trigger model fallback; weakening a legitimate empty result can reintroduce unsupported text.

When the vLLM path cannot load, runs out of GPU memory, or returns inconsistent batches, the pipeline can fall back to segment-level inference. GPU cleanup boundaries and model caching allow ASR, diarization, embeddings, and separation to share constrained hardware.

## Fragment V3's two model calls

1. **Semantic annotation:** use audio, initial text, and context to decide relevance and produce scene, event type, content origin, and continuity.
2. **Transcript correction:** correct the ASR baseline and add gender, paralinguistic, and speaker descriptions, then map results back to source segment indexes.

A failed semantic call is a retryable pipeline error; an explicit irrelevant judgment is a valid business result. If correction fails, the system keeps baseline ASR rather than losing the fragment.

## Speaker representation and matching

An earlier path used 512-dimensional WeSpeaker representations; a later path used 192-dimensional ReDimNet2 representations. Segment embeddings are L2-normalized. Registration aggregates multiple segment embeddings and normalizes the result again for cosine matching.

V2 cross-file resolution computes duration-weighted centroids for `(file, local speaker)` groups and applies constrained complete-linkage clustering:

- distinct speakers in one file receive cannot-link constraints;
- groups confirmed as one voiceprint receive must-link constraints;
- confirmed different identities receive cannot-link constraints;
- an identity can propagate within a resulting cluster.

V3 performs voiceprint matching at the Fragment stage, so Basic Event aggregation skips the historical V2 resolution path. These are version alternatives rather than two simultaneous stages.

## Three independent registration signals

Registration evaluates usable speech duration, embedding availability, and non-intrusive audio quality independently. Quality combines DNSMOS, NISQA, and DISTILL-MOS. Valid speech intervals are concatenated with short silence gaps and capped in length to remain within model constraints.

Failure in one sub-evaluation does not erase the others. The business layer maps download, decode, inference, and timeout failures into distinct outcomes. Evaluation supplies evidence; business integration completes formal registration.

## Synthetic output example

```json
{
  "segment": {
    "start_ms": 1240,
    "end_ms": 4680,
    "text": "synthetic example",
    "local_speaker": "speaker_1",
    "identity": {"status": "candidate", "confidence": 0.78}
  },
  "fragment": {
    "meaningful": true,
    "scene": "conversation",
    "content_origin": "mixed",
    "topics": ["planning"],
    "source_segment_ids": ["synthetic-segment-1"]
  }
}
```

This synthetic structure exposes time, text, identity uncertainty, semantics, and lineage without revealing internal schemas, users, or storage locations.
