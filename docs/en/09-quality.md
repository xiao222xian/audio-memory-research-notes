# Quality Engineering and Technical Cases

English · [中文](../09-quality.md)

## Evaluate the entire content chain

Input, perception, semantics, identity, selection, and expression jointly determine quality. Fixed samples, human review, version comparisons, and end-to-end replay locate problems at the responsible layer.

| Layer | Question | Method |
|---|---|---|
| Input | Are files, time, and required fields available? | Input checks and failure records |
| Perception | Are transcription, segmentation, and voiceprints useful? | Listening, segment comparison, targeted tests |
| Semantics | Are source, scene, and continuity reasonable? | Labels, controlled experiments, ablations |
| Identity | Is the statement attributed correctly? | Identity-chain and narrative comparison |
| Generation | Is there enough evidence and value to generate? | Blind review, references, content labels |
| End-to-end | Does a local change improve final content? | Fixed windows, repeated runs, lineage |

## Case 1: Media contamination

Programs, videos, or game audio can be recorded and mistaken for personal experiences. The team separated media presence, prediction, product filtering decisions, and time boundaries, then compared transcription ablations, rules, external signals, and integrated candidates.

Sample mapping was corrected because identical relative times in different events are not the same segment. Event-plus-time alignment yielded 116 reviewed samples. F1 improved from 75.5% for R0 to 84.1% for R7. Relative to R6, R7 fixed more false negatives but introduced additional false positives, so loss of useful content remained part of evaluation.

## Case 2: Identity and narrative attribution

Correct upstream matching does not guarantee correct wording. Diagnosis follows identity candidates, event input, role descriptions, and final person references to find where uncertainty becomes a claim about the user.

Perception errors, information loss at interfaces, and unsupported generation require different fixes. A voiceprint metric cannot summarize the entire chain, and post-fix outcomes need independent verification.

## Case 3: Unsupported generation

Twenty-five selected problem cases were grouped into four metadata issues, four missing-audio cases, and seventeen low-quality or incorrect-narrative cases. Different causes require different intervention points.

One quality threshold blocked 88% of problem cases but also 68.7% of approximately normal controls. This motivated layered analysis of input validity, participation cues, pre-generation selection, and post-generation checking.

## Case 4: Local metrics versus final cards

Replay used 17 fixed windows with five runs each and traced fragments, events, decisions, and references. R7 produced 5 contaminated cards out of 64, compared with R6's 7/62; it matched the original R0 result of 5/64.

Residual errors repeatedly came from one upstream window. The finding focused further work on mixed-scene boundaries and event themes rather than classification scores alone.

## Tools and review methods

Batch execution, cache reuse, listening interfaces, label import/export, error classification, and card lineage support evaluation. Assisted diagnosis may show predictions; independent blind review should avoid that influence. Reports retain label provenance and version definitions.

See [validation results](12-validation-results.md) for complete aggregates and limitations. These historical offline experiments do not measure overall platform accuracy or commercial user benefit.
