# Audio and Semantic Algorithms

English · [中文](../03-algorithms.md)

## Six core pipelines

| Pipeline | Responsibility | Output and use |
|---|---|---|
| Audio to segments | Decode, resample, process audio, detect speech, segment, transcribe | Time-aligned speech segments and text |
| Fragment analysis | Relevance judgment, semantic annotation, transcript correction, source detection | Structured fragment events |
| Basic event analysis | Aggregate fragments and synthesize titles and summaries | Coherent life events |
| Speaker embedding | Extract and normalize speaker representations | Features for registration and matching |
| Speaker resolution | Unify identities across fragments in the historical path | Global speaker mappings |
| Voiceprint admission evaluation | Assess usable speech, features, and quality | Registration assessment results |

Execution depends on version and business requirements; not every request runs all six pipelines.

## Audio perception

Everyday audio may contain silence, reverberation, noise, and several speakers. The implementation provides source separation, enhancement, dereverberation, resampling, and voice activity detection, combined with diarization to prepare model inputs. Configuration and version determine which operations run; enhancement is not assumed to improve every input.

The system supports Whisper and FunASR paths and a vLLM transcription execution path. Speaker intervals, speech coverage, and time alignment govern transcription inputs. Handling short segments, repetition, and implausible text must balance hallucination control against retaining real short utterances.

A model loading or execution failure requires error handling or fallback. An empty result after speech gating can be valid. Retrying the latter with weaker conditions can reintroduce unsupported transcription.

## Fragment understanding

The fragment stage combines audio, initial text, segment timing, identity cues, and context. It produces relevance, scene, topic, continuity, and content-origin information.

The V3 path combines relevance judgment and semantic annotation, then corrects existing ASR text and adds speaker-related annotations. Results are mapped back to source segments with time checks. Failure handling is stage-specific: a failed semantic request differs from an irrelevant fragment; failed correction can retain the initial transcript.

This organization reduces repeated interpretation and makes stage outputs easier to compare. Cost and accuracy improvements require controlled measurement rather than assumptions based on call counts.

## Event organization

Rule-based aggregation first combines transcripts, types, scenes, sources, and speaker information. A model then synthesizes an event title, summary, and topics. Basic Events retain their component relationships for business queries and downstream generation.

Two questions remain separate: which fragments belong together, and what their combined event should say. Short media excerpts or incorrect transcription can dominate a topic, so event processing still needs source and identity information.

## Version evolution

| Dimension | Earlier path | Later development |
|---|---|---|
| Transcription | Organized within multimodal enrichment | Separate initial ASR from correction |
| Semantic decisions | Several independent judgments | Combine selected relevance, semantic, and continuity judgments |
| Speaker representation | WeSpeaker | ReDimNet2 |
| Identity placement | Some resolution during event merging | Matching at the fragment stage in V3 |
| Inference | Segment-by-segment execution | Batch and vLLM paths with fallback |

These are project-specific changes, not general performance rankings of the underlying models.

## Evaluation

Baselines, label versions, and sample mappings support ablations, error-difference analysis, and downstream replay. Evaluation covers transcription, attribution, loss of useful content, and final card quality alongside classification metrics. See the [implementation details](13-audio-implementation.md) for algorithms and failure semantics.
