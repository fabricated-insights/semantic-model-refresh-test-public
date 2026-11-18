# Harness run 20261117T152826Z-v99p-8e19

- Task: refresh
- Variant: v99p-high-cardinality
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 44b14e08-f295-462f-813f-9c6810daafd2
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 1,284 MB, Power Query 1,254 MB, duration 1 min, CPU 136 s, rows 21,609,543, model 175 MB (Backup step in XMLA trace)
- Refresh request 25d79ce9-6d05-4468-9f33-87d2408d52ab, 2026-11-17T15:29:36.863 to 2026-11-17T15:31:11.833, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99p-high-cardinality on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 1,284 MB vs 550 MB (+734 MB), Power Query 1,254 MB vs 270 MB, model 175 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (42%); F16 5,120 MB: fits (25%); F32 10,240 MB: fits (13%); F64 25,600 MB: fits (5%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  7bc682e3-1008-458e-bb4b-0c0ce9e874f9 TabularSequencePoint         81.0     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         72.5    24.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         71.0    24.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         70.7    24.8 2349091
                                                  <NA>               Commit         10.5     0.0    <NA>
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.3     9.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.9     7.0       0
                                Sales.Sales Line Label       TabularRefresh          5.7     5.4       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.2     1.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.9     1.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.8     1.7  104990
        Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          2.6     0.1       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request bc7d22d7-c193-4674-9df1-241a7f78408a, 2026-11-17T15:32:02.907Z to 2026-11-17T15:33:05.16Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99p-high-cardinality on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T15:29:03Z run 20261117T152826Z-v99p-8e19: variant=v99p-high-cardinality data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T15:29:13Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T15:29:15Z PPU: v99p-high-cardinality is 7bc682e3-1008-458e-bb4b-0c0ce9e874f9, DataTag reads back data-1m-v1
2026-11-17T15:29:15Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T15:29:16Z Pro: v99p-high-cardinality is 5489ea18-9291-4d57-a7b5-c8ad13e93441, DataTag reads back data-1m-v1
2026-11-17T15:29:33Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T15:29:36Z PPU: trace started (full)
2026-11-17T15:29:37Z PPU: refresh started, request 25d79ce9-6d05-4468-9f33-87d2408d52ab
2026-11-17T15:31:17Z PPU: refresh refreshed (Completed) 
2026-11-17T15:31:48Z PPU: trace captured 463 events: ProgressReportEnd 424, ExecutionMetrics 30, CommandEnd 9
2026-11-17T15:31:49Z PPU: model size in memory right after the refresh: 209.0 MB
2026-11-17T15:32:02Z Pro: model size in memory before the refresh: None MB
2026-11-17T15:32:02Z Pro: standard refresh started
2026-11-17T15:33:33Z Pro: refresh refreshed (Completed) 
2026-11-17T15:33:33Z Pro: model size in memory right after the refresh: None MB
```
