# v99k-no-buffers

Diagnostic run K for v99-kitchen-sink. It is v99a without its last two `Table.Buffer` steps.

## What changed vs v99a

- `Sales`: the `Table.Buffer` after the full-table sort is removed. The sort stays.
- `Customer Stats`: the `Table.Buffer` before the Group By is removed. The Group By stays.

No query evaluated during refresh uses `Table.Buffer` now. `fnLoadParquet` keeps its `Binary.Buffer` of the downloaded file, the same as the baseline, which refreshes on F2. `Sales Flat` (not loaded) and `Unused Heavy Query` (commented out) still contain `Table.Buffer`, but refresh never evaluates them.

Everything else is identical to v99a:

- staging queries that turn every column into text, with types converted late
- full-table sorts in `Sales` and the Group By over the full fact in `Customer Stats`
- high-cardinality columns `Sales[Order Line]` and `Sales[Order DateTime]`
- eight calculated columns on Sales (RELATED, CALCULATE with ALLEXCEPT, RANKX, text concatenation)
- bidirectional relationships, many-to-many to `Customer Stats`, auto date/time

## Why this run

v99a refreshed on F64 but failed on F2 at 3,099 MB, only 34 MB over the 3,065 MB limit. Earlier runs showed one `Table.Buffer` on the Sales staging data was enough to fail F64, so the two remaining buffers are the first suspect.

## How to read the result

- If K refreshes on F2, the two buffers pushed v99a over the limit, and the model antipatterns in it fit on F2.
- If K fails on F2, the cost is in the model and the other Power Query steps: calculated columns, auto date/time, text staging, sorts and Group By. The next split would be calculated columns versus Power Query steps.

## Results

| Capacity | Result | Details |
|---|---|---|
| F64 | refreshed | |
| F2 | failed | consumed memory not recorded yet |

Removing the buffers was not enough. What remains in v99a, without any `Table.Buffer`, still does not fit in the 3 GB limit on F2.

## PPU and Pro, full pass (2026-11-16 to 18)

Every model was refreshed on Premium Per User (PPU) and on a Pro workspace in one pass, through the harness, with the data in its committed files. PPU numbers are from an XMLA trace of the refresh. Pro gives only the result and the duration: it has no XMLA endpoint and no workspace monitoring.

| Capacity | Data | Result | Peak MB | Power Query MB | Duration | Model size | In memory after refresh |
|---|---|---|---|---|---|---|---|
| PPU | 1M | refreshed | 13,038 | 12,936 | 31 min | 185 MB | 232.6 MB |
| Pro | 1M | refreshed |  |  | 16 min |  |  |

Runs: `results/harness/20261116T225204Z-v99k-aeca/`.
