# v24-bidirectional

The baseline with one relationship changed: Sales to Customer filters in both directions. Everything else is the same as in the baseline.

## What changed vs baseline

| Relationship | Baseline | v24 |
|---|---|---|
| `Sales[CustomerKey]` to `Customer[CustomerKey]` | single direction (Customer filters Sales) | both directions (Sales also filters Customer) |

With both directions, a filter on Product reaches Customer through Sales. On the filtered page (`pf` in `reports/spec.yaml`), the Country slicer then lists only countries with Computers sales, and the Cities table only cities whose customers bought Computers.

## Why this run

Bidirectional relationships are a common fix for "my slicer shows items with no data". The question is what they cost at query time. Refresh should not change: the relationship is built the same way whichever direction it filters.

## Expected effect

- Refresh peak and model size: same as baseline.
- Pages p01 to p20: same as baseline, because no filter there has to travel from Sales to Customer.
- Page pf: more storage engine queries and more time for the visuals that group by Customer columns (the Country slicer, f04 Cities). No numbers until measured.

## Runs

1. Refresh on F64 with 1M.
2. Query workload on F64 with 1M, pages p01 to p20 and pf. Compare with v00-baseline's pf.

## Results

F64, 1M, harness runs on 2026-11-10.

Refresh (run `20261110T144309Z-v24-17f8`): peak 608 MB, Power Query 335 MB, 1 min, model 73 MB. Inside the baseline's range on F64 (551 to 785 MB over four runs), as expected.

Query workload (run `20261110T145027Z-v24-0303`, 968 queries, none failed), against v00-baseline (runs `20261110T103141Z-v00-5b3b` for p01 to p20 and `20261110T143547Z-v00-92e4` for pf). Medians over 5 repeats, cold cache, all visuals at once:

| Page | Slowest visual v00 | Slowest visual v24 | CPU v00 | CPU v24 | Peak per query v00 | Peak per query v24 |
|---|---|---|---|---|---|---|
| p20 | 672 ms | 688 ms | 2,033 ms | 1,986 ms | 58 MB | 55 MB |
| pf | 63 ms | 62 ms | 220 ms | 235 ms | 12 MB | 11 MB |

The only visual that changed is the Country slicer on pf: 2 storage engine queries instead of 1, 16 ms instead of 0, and 2.5 MB. Its list now has to go through Sales to find the countries with Computers sales. It still lists all 8 countries, because every country has Computers sales. Every other visual on pf has a measure on Sales, so the engine filters through Sales with or without the bidirectional relationship, and those visuals did not change.

On a single star with 1M rows, a bidirectional relationship cost nothing measurable beyond the slicer.

## PPU and Pro, full pass (2026-11-16 to 18)

Every model was refreshed on Premium Per User (PPU) and on a Pro workspace in one pass, through the harness, with the data in its committed files. PPU numbers are from an XMLA trace of the refresh. Pro gives only the result and the duration: it has no XMLA endpoint and no workspace monitoring.

| Capacity | Data | Result | Peak MB | Power Query MB | Duration | Model size | In memory after refresh |
|---|---|---|---|---|---|---|---|
| PPU | 1M | refreshed | 551 | 460 | 0.9 min | 73 MB | 92.7 MB |
| Pro | 1M | refreshed |  |  | 0.8 min |  |  |

Runs: `results/harness/20261117T055553Z-v24-5c7d/`.

## F2 and F64 gap pass (2026-11-18)

Refreshed on F2 with the 1M data in 2.0 min. In memory after refresh: 92.7 MB. F2 has no workspace monitoring, so there is no peak; the F64 and PPU peaks are well below the F2 limit of about 3,066 MB, as finding 9 predicts.

Run: `results/harness/20261118T123936Z-v24-800c/`.
