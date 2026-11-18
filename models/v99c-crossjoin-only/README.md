# v99c-crossjoin-only

Diagnostic run C for v99-kitchen-sink.

v99 failed on F64: the refresh was cancelled at 25,599 MB against a 25,593 MB limit. Runs A, B and C split v99 into parts so each part's peak refresh memory can be measured on F64.

## What changed vs v99

Run A plus the full Product x Date crossjoin (10.1M rows). Sales Copy is empty.

| Knob | v99 | This run |
|---|---|---|
| `CopyCount` in `tables/Sales Copy.tmdl` | 2 | 0 |
| `FirstYear` in `tables/Product Date Grid.tmdl` | 2016 | 2016 |

A knob of 0 copies or a first year of 2099 leaves the table in the model with zero rows. The model structure is otherwise identical to v99.

## How to read the result

- Peak of B minus peak of A: the cost of one Sales copy.
- Peak of C minus peak of A: the cost of the 10.1M row crossjoin.
- If A fails on F64 by itself, the main cost is somewhere else in v99.

Same Desktop steps as v99 before publishing: refresh once so the calculated tables get their columns, and toggle auto date/time off and on.

## PPU and Pro, full pass (2026-11-16 to 18)

Every model was refreshed on Premium Per User (PPU) and on a Pro workspace in one pass, through the harness, with the data in its committed files. PPU numbers are from an XMLA trace of the refresh. Pro gives only the result and the duration: it has no XMLA endpoint and no workspace monitoring.

| Capacity | Data | Result | Peak MB | Power Query MB | Duration | Model size | In memory after refresh |
|---|---|---|---|---|---|---|---|
| PPU | 1M | refreshed | 25,918 | 25,808 | 42 min | 358 MB | 486.6 MB |
| Pro | 1M | refreshed |  |  | 16 min |  |  |

Runs: `results/harness/20261117T194928Z-v99c-de5d/`.

## F2 and F64 gap pass (2026-11-18)

Failed on F64 after 2.8 min (resource governance), at a peak of 25,592 MB, of which Power Query 25,518 MB, against the limit of 25,592 MB. "Retry attempts for failures while executing the refresh exceeded the retry limit set on the request." On PPU the same model refreshed with a peak just above the F64 limit, so the F64 failure is what that peak predicts.

Run: `results/harness/20261118T141706Z-v99c-b7fd/`.
