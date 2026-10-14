# Product Positioning and Use Cases

English · [中文](../01-product.md)

## Turning everyday sound into experiences people can revisit

Spiro explores how everyday audio can become a lasting personal information resource. It extracts events from conversations, retains time and participant cues, and presents them in readable forms. The project considers transcription completeness, whether an event is worth retaining, whether the content belongs to the user, and whether the source material supports the wording.

The experience has three parts: recording daily life, understanding experiences, and reconnecting with them. Recording reduces information loss. Understanding organizes fragments into events. Content tasks and memory research explore connections between past experiences and current questions.

## The user journey

| Stage | User experience | System work |
|---|---|---|
| Record | Submit audio through a recording entry point | Receive the file and time information; create a task |
| Establish identity cues | Provide registration speech | Evaluate usable speech, speaker features, and recording quality |
| Organize in the background | Avoid manually editing every transcript segment | Process audio, transcribe, distinguish speakers, and analyze fragments |
| Form events | Browse coherent experiences | Group fragments using continuity and context |
| Generate content | Read event cards or other task results | Select evidence, produce structured content, retain references |
| Revisit | Inspect sources and related experiences | Trace events; explore memory association and voice interaction in separate modules |

This journey connects the project components. It does not imply that every entry point and content format has been commercially released.

## Content formats and responsibilities

**Event cards** organize a particular experience around its time, scene, and evidence. Multi-event cards select material that belongs together and can skip generation when support is insufficient.

**Insight letters** use events from a period of time to support longer-form expression. The Agent service provides task configuration and language checks; content quality still requires review.

**Profile and insight tasks** organize observations from events as context for further content. These are observation and expression capabilities, with no claim of clinical diagnosis or therapeutic effectiveness.

**Conversational memory** is explored in a separate Demo that retrieves material according to the question and delivers a spoken answer, accompanied by a cognition panel.

## Typical scenarios

- **Revisiting daily conversations:** organize multi-speaker dialogue into events without attributing another person's experience to the user.
- **Reviewing work and plans:** organize decisions, plans, and their context. Turning these into actionable to-dos requires additional product rules.
- **Observing a period of life:** provide time-bounded events to content tasks so users can revisit recurring topics.
- **Memory questions with sources:** use different routes for facts, dates, and patterns instead of treating every question as an abstract insight request.

## Connecting product value to engineering

Lower recording effort depends on ingestion and asynchronous processing. Meaningful content depends on event understanding and selection. Personalization depends on identity and context. Long-term trust depends on evidence links, updates, and evaluation. Algorithms, services, interfaces, and development tools jointly support these goals.
