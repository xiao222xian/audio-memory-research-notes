# Realtime Voice Demo and Frontend Experience

English · [中文](../08-live-experience.md)

## A conversational memory interface

LiveMemory connects retrieval, language reasoning, and voice interaction in a frontend/backend Demo. A user asks a question through a microphone; the backend routes it, retrieves material, prepares an answer, and speaks it. A cognition panel presents related organized information.

It is a single-user demonstration and research tool with a separately imported corpus, not a claim of a completed multi-tenant commercial service or full device acceptance.

## Frontend and backend responsibilities

| Layer | Technology and responsibility |
|---|---|
| Frontend | React, TypeScript, Vite; routing, voice controls, answer and cognition display |
| Backend | Python, FastAPI; sessions, speech connections, retrieval, reasoning |
| Bidirectional connection | WebSocket for realtime audio and session state |
| Corpus input | Portable import, run listing, material previews |
| Presentation entry | Product presentation and explicitly enabled Live Demo |
| Operations | Unified CLI for start, stop, status, diagnostics |

## Two voice paths

The **composed path** connects streaming ASR, an intermediate language model, and TTS so each stage can be configured and observed. The **native-audio path** explores direct realtime model interaction. Configuration selects the provider path.

The interface and backend organize listening, thinking, and speaking states with interruption handling. Device, network, and provider conditions affect experience; this document makes no unverified fixed-latency promise.

## Question-aware routing

| Question type | Focus |
|---|---|
| Fact | Locate explicit material and relevant source text |
| Pattern | Compare evidence across observations |
| Insight | Apply multiple perspectives when appropriate |
| Count | Count matches within a defined scope |
| Temporal | Filter by dates and time ranges |

Explicit questions should receive grounded answers before broader association is introduced. Cross-domain reasoning is not forced onto every request.

## A shared basis for speech and the cognition panel

Spoken responses and the panel consume the same organized information package, reducing divergence from independent generation. The panel can display nodes, relationships, and synthesis. Debug views expose additional retrieval and tool-use information.

## Session traces

Development traces record transcription, state changes, retrieval, tool calls, interruptions, and turn boundaries, with navigable model inputs and outputs. Audio failures can be inspected through the state timeline; content failures through retrieval and model context.

The Demo supports both experience exploration and diagnosis. Public documentation excludes real memories and conversations. The [voice implementation chapter](16-voice-implementation.md) details turn assembly, HOLD behavior, and cancellation.
