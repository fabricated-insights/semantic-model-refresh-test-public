# Harness run 20261117T194928Z-v99c-de5d

- Task: refresh
- Variant: v99c-crossjoin-only
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 0d69046b-b82d-4bd5-a8c8-23ac74268cd1
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 25,918 MB, Power Query 25,808 MB, duration 42 min, CPU 8,641 s, rows 35,817,730, model 358 MB (Backup step in XMLA trace)
- Refresh request 784009c1-5da3-4bf0-83c8-b870760e8004, 2026-11-17T19:52:48.92 to 2026-11-17T20:35:41.5, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99c-crossjoin-only on PPU data-1m-v1: refreshed, peak 25,914 MB (2026-11-17T08:30:23Z).
  - Peak change: +4 MB (+0.0%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 25,918 MB vs 550 MB (+25,368 MB), Power Query 25,808 MB vs 270 MB, model 358 MB vs 73 MB.
- Model size in memory when the full refresh started: 380 MB. The refresh may use the SKU maximum minus this: 102,020 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,686 MB: OVER (965%); F16 4,740 MB: OVER (547%); F32 9,860 MB: OVER (263%); F64 25,220 MB: OVER (103%); PPU 102,020 MB: fits (25%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            364f4109-e09b-4cda-a773-d642978613b4 TabularSequencePoint       2547.7     0.5       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       2449.8    26.6       0
                           Sales Flat.Sales Flat       TabularRefresh       2379.0    89.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process       1556.1    26.6       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData       1555.7    26.6 2349091
                           Sales Flat.Sales Flat           ExecuteSql       1259.9     0.0       0
                           Sales Flat.Sales Flat              Process       1119.0    89.7       0
                           Sales Flat.Sales Flat             ReadData       1118.4    89.7 2349091
                   Customer Stats.Customer Stats       TabularRefresh       1040.6     2.9       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        893.6     0.0       0
                   Customer Stats.Customer Stats              Process        607.0     2.8       0
                   Customer Stats.Customer Stats             ReadData        606.4     2.4  471482
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 16 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 3490ce77-8725-4be0-a262-d0ed432f93cf, 2026-11-17T20:36:52.613Z to 2026-11-17T20:52:35.583Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99c-crossjoin-only on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T08:52:45Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T19:52:03Z run 20261117T194928Z-v99c-de5d: variant=v99c-crossjoin-only data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T19:52:14Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T19:52:21Z PPU: v99c-crossjoin-only is 364f4109-e09b-4cda-a773-d642978613b4, DataTag reads back data-1m-v1
2026-11-17T19:52:21Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T19:52:22Z Pro: v99c-crossjoin-only is 6af71876-9875-4b2d-8a55-fbde4a52de4f, DataTag reads back data-1m-v1
2026-11-17T19:52:45Z PPU: model size in memory before the refresh: 380.4 MB
2026-11-17T19:52:48Z PPU: trace started (full)
2026-11-17T19:52:49Z PPU: refresh started, request 784009c1-5da3-4bf0-83c8-b870760e8004
2026-11-17T20:36:06Z PPU: refresh refreshed (Completed) 
2026-11-17T20:36:37Z PPU: trace captured 613 events: ProgressReportEnd 592, ExecutionMetrics 11, CommandEnd 10
2026-11-17T20:36:39Z PPU: model size in memory right after the refresh: 486.6 MB
2026-11-17T20:36:52Z Pro: model size in memory before the refresh: None MB
2026-11-17T20:36:52Z Pro: standard refresh started
2026-11-17T20:52:55Z Pro: refresh refreshed (Completed) 
2026-11-17T20:52:55Z Pro: model size in memory right after the refresh: None MB
```
