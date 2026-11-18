# v24a-second-fact

The baseline plus a second fact table, Orders, with one row per order. All relationships filter in one direction, as in the baseline. This is the control for v24b-second-fact-bidirectional.

## What changed vs baseline

- New table `Orders` from `orders.parquet` in the same data release: `Order Number`, `Order Date`, `Delivery Date`, `CustomerKey`, `StoreKey`, `Currency Code`. On 1M data it has 980,666 rows, one per order in Sales.
- New measure `Orders[Order Count] = COUNTROWS ( Orders )`.
- New relationships, many to one, single direction: `Orders[CustomerKey]` to `Customer`, `Orders[StoreKey]` to `Store`, `Orders[Order Date]` to `Date`.

Orders and Sales share Customer, Store and Date, so the model has two facts on the same dimensions, a common shape in real models (for example sales and budget, or orders and returns). There is no relationship between Orders and Sales.

## Why this run

It isolates the cost of the second fact table itself, so v24b can show what the bidirectional relationship adds on top. It also shows what a second fact does to refresh: one more table to load, compress and relate.

## Expected effect

- Refresh: a higher peak and a larger model than the baseline, from one more table of about a million rows. No numbers until measured.
- Pages p01 to p20 and pf: same as baseline, the visuals do not use Orders.
- Page po (Orders filtered): the Category slicer does not filter the Orders visuals, because Product has no path to Orders. The Country slicer does, through Customer.

## Runs

1. Refresh on F64 with 1M.
2. Query workload on F64 with 1M, pages p01 to p20, pf and po.

## Results

F64, 1M, harness runs on 2026-11-10.

Refresh (run `20261110T150725Z-v24a-f994`): peak 933 MB, Power Query 911 MB, 1 min, 3,541,806 rows, model 103 MB. The baseline peaked at 551 to 785 MB over four runs with a 73 MB model. The Orders table adds 30 MB to the model. The peak is above the baseline's range, almost all of it in Power Query, but it is one run and the baseline's own Power Query peaks spread over more than 300 MB.

Query workload (run `20261110T151413Z-v24a-c285`, 1,100 queries, none failed). Medians over 5 repeats, cold cache, all visuals at once:

| Page | Slowest visual | CPU | Peak per query |
|---|---|---|---|
| p20 | 719 ms (v00: 672 ms) | 2,017 ms (v00: 2,033 ms) | 55 MB (v00: 58 MB) |
| pf | 62 ms (v00: 63 ms) | 233 ms (v00: 220 ms) | 12 MB (v00: 12 MB) |
| po | 16 ms | 48 ms | 6 MB |

What the Orders page shows (checked with DAX on 2026-11-10):

| Filter | Order Count |
|---|---|
| none | 980,666 |
| Germany | 111,258 |
| Computers | 980,666 |
| Computers and Germany | 111,258 |

The Category slicer does not filter Orders, because Product has no relationship path to Orders. The Country slicer does, through Customer. This is what single-direction relationships give, and the report shows it without any warning.

## PPU and Pro, full pass (2026-11-16 to 18)

Every model was refreshed on Premium Per User (PPU) and on a Pro workspace in one pass, through the harness, with the data in its committed files. PPU numbers are from an XMLA trace of the refresh. Pro gives only the result and the duration: it has no XMLA endpoint and no workspace monitoring.

| Capacity | Data | Result | Peak MB | Power Query MB | Duration | Model size | In memory after refresh |
|---|---|---|---|---|---|---|---|
| PPU | 1M | refreshed | 857 | 765 | 1.6 min | 103 MB | 110.0 MB |
| Pro | 1M | refreshed |  |  | 0.9 min |  |  |

Runs: `results/harness/20261117T060102Z-v24a-53c5/`.

## F2 and F64 gap pass (2026-11-18)

Refreshed on F2 with the 1M data in 1.2 min. In memory after refresh: 110.0 MB. F2 has no workspace monitoring, so there is no peak; the F64 and PPU peaks are well below the F2 limit of about 3,066 MB, as finding 9 predicts.

Run: `results/harness/20261118T124806Z-v24a-90b5/`.
