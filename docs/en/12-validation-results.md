# Historical Validation Results and Definitions

English · [中文](../12-validation-results.md)

This technical appendix reports local quality experiments, not a single score for the entire platform.

## Fragment classification

The same 116 reviewed labels contain 52 media positives and 64 negatives:

| Version | TP | FP | FN | TN | Precision | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| R0 | 40 | 14 | 12 | 50 | 74.1% | 76.9% | 75.5% |
| R6 | 41 | 7 | 11 | 57 | 85.4% | 78.8% | 82.0% |
| R7 | 45 | 10 | 7 | 54 | 81.8% | 86.5% | 84.1% |

F1 = 2TP / (2TP + FP + FN). R0 to R7 improved by approximately 8.6 percentage points on this fixed set. The task measures media classification, not independently validated correctness of deleting entire segments.

## Generated content

Each version used 17 fixed windows and five runs per window, giving 85 execution slots. Some runs skipped generation; contamination rates use generated cards as the denominator.

| Version | Cards | Contaminated cards | Rate | Label source |
|---|---:|---:|---:|---|
| R0 | 64 | 5 | 7.8% | 63 user-blind reviews, 1 internal supplementary review |
| R6 | 62 | 7 | 11.3% | 62 user-blind reviews |
| R7 | 64 | 5 | 7.8% | 59 labels inherited for equivalent content, 5 retrospective confirmations |

R7 has two fewer contaminated cards than R6, a decrease of about 3.5 percentage points, and matches R0. The team therefore investigated upstream windows, event boundaries, and generated themes alongside fragment metrics.

## Unsupported generation

Twenty-five selected problem cases comprised four metadata issues, four missing-audio cases, and seventeen low-quality evidence, transcription, attribution, or over-elaboration cases. The categories identify intervention points rather than a universal filter.

Quality-score experiments compared 25 problem cases with 83 approximately normal controls. A threshold of 2.0 blocked 88% of problem cases and 68.7% of controls; at 3.0, control rejection was about 94%. This evidence argued against using one quality threshold as the sole admission rule.

## Pre-generation selection

Twenty-six candidate events were organized into six groups: one produced content, five skipped, with zero execution failures and zero invalid reference identifiers. This demonstrated selection behavior and motivated evaluation of useful events that might be excluded.

The decision unit was a group, so these counts do not establish event-level precision or recall. Valid identifiers do not establish narrative truth.

## Interpretation

- Reviewers saw model predictions for the 116-label set, creating anchoring risk. Repeated reuse is not independent holdout validation.
- R7 card labels include inheritance and retrospective review rather than complete new blind review. Repeated outputs from the same windows are correlated.
- The 83 controls were selected approximately through an existing owner-detection signal, not fully confirmed normal ground truth.
- Selected problem cases do not estimate production incidence.
- These are offline results. No unmeasured production gains, latency reductions, cost savings, or retention figures are claimed.

Aggregate files are in the repository's `results/` directory. From the repository root, `python3 tools/verify.py` checks arithmetic and file integrity without invoking models.
