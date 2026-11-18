# v99d-power-query

Diagnostic run D for v99-kitchen-sink. It is v99a plus one change: `Unused Heavy Query` has its original body again.

## What changed vs v99a

- `Unused Heavy Query` merges orders and order rows, sorts, buffers and groups them. It is not loaded and nothing references it, so refresh should never evaluate it.

Everything else is identical to v99a, including `Sales Flat`, which stays in Power Query as a not-loaded query.

## History of this variant

1. First version: v99a plus `Sales Flat` loaded, `Table.Buffer` back in `stg Sales` and `stg Customer`, and the unused query restored. Failed on F64, cancelled at 25,598 MB (Activity ID `73e0313e-8747-486d-ae26-349b16cb31bf`).
2. Second version: the staging buffers removed again. Not run.
3. Current version: `Sales Flat` not loaded either.

## How to read the result

- If D refreshes with about the same peak, duration and CU as v99a, an unreferenced query costs nothing, as expected.
- If D differs from v99a, refresh evaluates queries that nothing loads, which would be worth a closer look.
- D passing tells nothing new about the first version's failure. That failure came from loading `Sales Flat`, from the staging buffers, or from both together. Separating them needs v99a plus `Sales Flat` loaded with unbuffered staging (the second version above).

## PPU and Pro, full pass (2026-11-16 to 18)

Every model was refreshed on Premium Per User (PPU) and on a Pro workspace in one pass, through the harness, with the data in its committed files. PPU numbers are from an XMLA trace of the refresh. Pro gives only the result and the duration: it has no XMLA endpoint and no workspace monitoring.

| Capacity | Data | Result | Peak MB | Power Query MB | Duration | Model size | In memory after refresh |
|---|---|---|---|---|---|---|---|
| PPU | 1M | refreshed | 16,132 | 16,018 | 23 min | 185 MB | 232.6 MB |
| Pro | 1M | refreshed |  |  | 50 min |  |  |

Runs: `results/harness/20261117T084801Z-v99d-4ab7/`.
