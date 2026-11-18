# v35-calc-tables-four-copies

v23-dax-calc-tables with four copies of the Sales rows in `Sales Copy` instead of one, on the 10M data. A model whose refresh needs more than the 25.6 GB of F64 in the model itself, not in Power Query.

## What changed vs v23-dax-calc-tables

| Knob | v23 | This run |
|---|---|---|
| `CopyCount` in `tables/Sales Copy.tmdl` | 1 | 4 |
| `DataTag` in `expressions.tmdl` | `data-1m-v1` | `data-10m-v1` |

With the 10M data, `Sales Copy` has 4 x 23.7M = 94.9M rows. Everything else is the same as v23, which is the baseline plus four calculated tables.

## Why this run

The tests so far showed that Premium Per User (100 GB per model) refreshes models that fail on F64, but only by a small margin: v99 failed on F64 at 25,599 MB and peaked at 26,115 MB on PPU, almost all of it Power Query. v19 showed that the Power Query limit does not grow on PPU at all. This run tests the model side: calculated tables need no Power Query, and are built in memory in full before they are compressed.

v23 on 10M peaks at about 13 GB in four runs, of which 1.2 to 1.9 GB is Power Query. Most of the rest is the calculated tables, and `Sales Copy` is the largest of them.

## Expected effect

- F64: fails on the model memory limit, if each copy adds several GB as the v23 runs suggest. No number until measured.
- PPU: refreshes, with a peak above 25.6 GB.
- If F64 refreshes, four copies were not enough, and the result says how much one copy costs.

## Runs

1. Refresh on F64 with 10M, through Git (harness).
2. Refresh on PPU with 10M, measured with the XMLA trace. The PPU workspace is not connected to Git: open `v35-calc-tables-four-copies.pbip` in Desktop, do not refresh, and publish to the PPU workspace. The harness then refreshes it there with the committed parameters.

## Results

F64, 10M, 2026-11-13, harness run `20261113T122445Z-v35-6ea1`:

| Model | Result | Peak | Power Query | Duration | CPU | Model in memory after |
|---|---|---|---|---|---|---|
| v23 (1 copy), 3 harness runs on 10M | refreshed | 13,062 to 13,139 MB | 1,707 to 1,870 MB | 7.5 to 8.2 min | 809 to 878 s | 1,379 to 1,387 MB |
| v35 (4 copies) | refreshed | 13,063 MB | 1,601 MB | 17 min | 1,827 s | 2,803 MB |

Four copies did not raise the peak at all. The model doubled (2,803 MB against 1,379 MB), `Sales Copy` took 448 s instead of 99 s for its 94.9M rows, but the peak stayed at 13,063 MB. So a bigger copy table does not raise the peak. The four calculated tables are independent of each other: each reads only imported tables (Sales, Customer, Product, Date, Store). The refresh log shows they are not built one after the other: in v35 `Product Date Grid` ran while Sales was still loading, and `Sales Copy` and `Sales Summary` both started at 12:37:07 UTC and ran side by side (99 s for the summary, 448 s for the copy). At the peak both were in memory together, so the copy's working memory did not grow with its row count, or stayed below what the summary needed. The log gives one peak per refresh, not one per table.

That step is most likely `Sales Summary`, a `SUMMARIZECOLUMNS` over customer, year and category with three measures, one of them a `DISTINCTCOUNT`, 16.5M rows on 10M. The refresh log gives one peak for the whole refresh, not one per table, so this is not proven.

The model did not exceed the F64 limit, so it was not run on PPU.

## PPU and Pro, full pass (2026-11-16 to 18)

Every model was refreshed on Premium Per User (PPU) and on a Pro workspace in one pass, through the harness, with the data in its committed files. PPU numbers are from an XMLA trace of the refresh. Pro gives only the result and the duration: it has no XMLA endpoint and no workspace monitoring.

| Capacity | Data | Result | Peak MB | Power Query MB | Duration | Model size | In memory after refresh |
|---|---|---|---|---|---|---|---|
| PPU | 10M | refreshed | 9,737 | 1,754 | 28 min | 3,281 MB | 2,829.4 MB |
| Pro | 10M | failed, model 2192 MB over the 1024 MB limit |  |  | 14 min |  |  |

Pro error (10M): "Unable to save the changes since the new dataset of size 2192 MB exceeds the limit of 1024 MB."

Runs: `results/harness/20261117T093046Z-v35-f6d2/`.

## F2 and F64 gap pass (2026-11-18)

Failed on F2 with the 10M data after 13 min (resource governance). The service retried the refresh and gave up: "Retry attempts for failures while executing the refresh exceeded the retry limit set on the request." Each attempt stopped at a consumed memory of 3,066 MB or a little more, against a limit of 3,066 MB. The peak on F64 and PPU is far above that, as finding 9 predicts.

Run: `results/harness/20261118T142517Z-v35-9344/`.
