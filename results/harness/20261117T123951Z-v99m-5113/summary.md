# Harness run 20261117T123951Z-v99m-5113

- Task: refresh
- Variant: v99m-baseline-pq
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 88a69690-9128-4722-a6a6-3b177d4bdafd
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 770 MB, Power Query 589 MB, duration 1 min, CPU 115 s, rows 21,583,972, model 102 MB (Backup step in XMLA trace)
- Refresh request 4af567b3-6fa9-4ca1-b17d-ce1bc48f0ccb, 2026-11-17T12:41:22.953 to 2026-11-17T12:42:39.413, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99m-baseline-pq on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 770 MB vs 550 MB (+220 MB), Power Query 589 MB vs 270 MB, model 102 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (25%); F16 5,120 MB: fits (15%); F32 10,240 MB: fits (8%); F64 25,600 MB: fits (3%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  3394eba6-7666-49c7-99a1-cd99723178be TabularSequencePoint         66.1     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         58.4    20.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         56.6    20.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         56.2    20.4 2349091
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          7.6     0.1       0
                                                  <NA>               Commit          7.5     0.0    <NA>
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          7.4     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.3     9.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.0     7.1       0
                                Sales.Sales Line Label       TabularRefresh          6.1     5.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.3     1.5       0
        Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          2.8     0.1       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request b295bb8a-b41e-4502-a224-f6c3d8280e1a, 2026-11-17T12:43:49.9Z to 2026-11-17T12:44:44.003Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99m-baseline-pq on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T12:40:24Z run 20261117T123951Z-v99m-5113: variant=v99m-baseline-pq data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T12:40:58Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T12:41:01Z PPU: v99m-baseline-pq is 3394eba6-7666-49c7-99a1-cd99723178be, DataTag reads back data-1m-v1
2026-11-17T12:41:01Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T12:41:02Z Pro: v99m-baseline-pq is 5a069a77-4a12-426b-9c17-c69217c2a77f, DataTag reads back data-1m-v1
2026-11-17T12:41:19Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T12:41:22Z PPU: trace started (full)
2026-11-17T12:41:23Z PPU: refresh started, request 4af567b3-6fa9-4ca1-b17d-ce1bc48f0ccb
2026-11-17T12:43:03Z PPU: refresh refreshed (Completed) 
2026-11-17T12:43:34Z PPU: trace captured 433 events: ProgressReportEnd 388, ExecutionMetrics 34, CommandEnd 11
2026-11-17T12:43:35Z PPU: model size in memory right after the refresh: 136.1 MB
2026-11-17T12:43:49Z Pro: model size in memory before the refresh: None MB
2026-11-17T12:43:49Z Pro: standard refresh started
2026-11-17T12:44:50Z Pro: refresh refreshed (Completed) 
2026-11-17T12:44:50Z Pro: model size in memory right after the refresh: None MB
```
