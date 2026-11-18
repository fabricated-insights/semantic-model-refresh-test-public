# v21-pq-group-by

The baseline plus one summary table built with a Group By in Power Query. Nothing else changes.

## What changed vs baseline

- New loaded table `Customer Stats`: reads `sales.parquet` and groups all 2.35M lines by customer and year. Per group it computes a distinct count of orders, a row count and the sales amount. It loads one row per customer and year with sales.
- Many-to-many relationship from `Sales[CustomerKey]` to `Customer Stats[CustomerKey]`, because a customer appears once per year.

The query is the same as in v99q.

## Hypothesis

A Group By cannot stream either. Power Query has to read the whole fact table and keep every group, with its rows for the distinct count, until the last row is read. In the v99 diagnostic runs, v99q (v99m plus this table) failed on F2 while v99m refreshed. This run tests whether the table alone takes the clean baseline off F2.

## Expected effect

- Model size: baseline plus a few MB for the summary table.
- Peak refresh memory: higher than baseline. The Sales file is also read a second time, once for `Sales` and once for `Customer Stats`.
- Duration: higher than baseline.

## How to read the result

- If it fails on F2, one ordinary summary table in Power Query is enough to push a well-built model of this size off the smallest capacity.
- If it refreshes, the Group By only fails F2 together with the rest of v99m.

## Results

| Capacity | Result | Details |
|---|---|---|
| F64 | refreshed | |
| F2 | failed | consumed memory not recorded |

One summary table built with a Group By in Power Query takes the baseline off F2. The table itself is small; the memory is used while Power Query groups the full Sales table.

## PPU and Pro, full pass (2026-11-16 to 18)

Every model was refreshed on Premium Per User (PPU) and on a Pro workspace in one pass, through the harness, with the data in its committed files. PPU numbers are from an XMLA trace of the refresh. Pro gives only the result and the duration: it has no XMLA endpoint and no workspace monitoring.

| Capacity | Data | Result | Peak MB | Power Query MB | Duration | Model size | In memory after refresh |
|---|---|---|---|---|---|---|---|
| PPU | 1M | refreshed | 3,582 | 3,338 | 1.6 min | 84 MB | 118.6 MB |
| Pro | 1M | refreshed |  |  | 1.7 min |  |  |

Runs: `results/harness/20261117T091313Z-v21-add0/`.
