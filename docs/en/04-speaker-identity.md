# Voiceprint Registration, Speaker Identity, and Attribution

English · [中文](../04-speaker-identity.md)

## Three distinct questions

Diarization asks when the speaker changes. Voiceprint matching asks which known identity resembles a voice. Narrative attribution asks whose experience a statement can describe. Acoustic similarity alone is insufficient to establish ownership of an experience.

## Registration admission

Registration audio follows an independent assessment flow. After decoding and resampling, usable speech, embedding extraction, and audio quality are evaluated. Segment features are aggregated and normalized for registration.

| Check | Purpose | Use |
|---|---|---|
| Usable speech duration | Detect mostly silent input | Decide whether the recording provides enough speech |
| Embedding availability | Obtain usable identity features | Support registration and matching |
| Audio quality | Observe noise and perceptual quality | Supply an admission signal |
| Download, decoding, timeout | Distinguish input and execution failures | Return a meaningful failure reason |

The assessment service returns structured results, while the business flow completes formal registration. Audio-quality scores and identity-matching accuracy are separate measurements used for admission and identity decisions respectively. Version-specific implementation details are described in the [audio deep dive](13-audio-implementation.md).

## Matching and cross-fragment identity

The historical V2 path groups speakers within fragments and uses centroids, known profiles, and clustering to unify identities across files. Constraints help prevent distinct speakers in one file from being merged. V3 matches at the fragment stage and skips the same historical resolution pipeline during Basic Event merging.

Clustering, registration matching, and narrative attribution have separate roles. They should not be combined in a description of a single nonexistent algorithm version.

## From identity to expression

Event summarization can compress identity information; generation can turn an uncertain cue into a definite second-person statement. Quality analysis checks candidate conflicts, role information delivered downstream, reference ownership, and whether the final claim exceeds the evidence.

In a fictional conversation, one participant describes a trip while another merely responds. Even a perfect transcript does not justify presenting the trip as the responder's experience. Identity processing must therefore connect with event organization and generation.

## Engineering outputs

The platform includes registration evaluation, embedding and matching, versioned identity processing, integration contracts, and targeted evaluation. Identity propagation, uncertainty, and narrative attribution are managed as one cross-layer quality problem.
