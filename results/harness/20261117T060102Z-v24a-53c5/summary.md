# Harness run 20261117T060102Z-v24a-53c5

- Task: refresh
- Variant: v24a-second-fact
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 5263f36a-080b-486b-b220-95c29932fb75
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 857 MB, Power Query 765 MB, duration 2 min, CPU 179 s, rows 3,541,806, model 103 MB (Backup step in XMLA trace)
- Refresh request bd7b40e7-2237-4439-96b6-d8ff8e4e9a10, 2026-11-17T06:03:52.443 to 2026-11-17T06:05:35.007, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v24a-second-fact on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 857 MB vs 550 MB (+307 MB), Power Query 765 MB vs 270 MB, model 103 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (28%); F16 5,120 MB: fits (17%); F32 10,240 MB: fits (8%); F64 25,600 MB: fits (3%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  b0358b26-6f81-4c1b-a470-0f781c76b094 TabularSequencePoint         94.0     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         93.3    28.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         88.9    28.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         88.5    28.2 2349091
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa       TabularRefresh         28.0     9.5       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa              Process         23.9     9.4       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa             ReadData         19.6     9.3  980666
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.4    12.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.2    11.1       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          9.5     3.2       0
                                                  <NA>               Commit          7.2     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          5.4     3.1       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 408958b7-6990-4c01-9a5d-cd570c172fc8, 2026-11-17T06:06:49.973Z to 2026-11-17T06:07:43.07Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v24a-second-fact on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T06:03:17Z run 20261117T060102Z-v24a-53c5: variant=v24a-second-fact data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T06:03:24Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T06:03:26Z PPU: v24a-second-fact is b0358b26-6f81-4c1b-a470-0f781c76b094, DataTag reads back data-1m-v1
2026-11-17T06:03:26Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T06:03:27Z Pro: v24a-second-fact is 1010796b-d670-4f9d-a35e-9823ea1138f1, DataTag reads back data-1m-v1
2026-11-17T06:03:48Z PPU: model size in memory before the refresh: 0.0 MB
2026-11-17T06:03:52Z PPU: trace started (full)
2026-11-17T06:03:52Z PPU: refresh started, request bd7b40e7-2237-4439-96b6-d8ff8e4e9a10
2026-11-17T06:06:03Z PPU: refresh refreshed (Completed) 
2026-11-17T06:06:34Z PPU: trace captured 305 events: ProgressReportEnd 260, ExecutionMetrics 34, CommandEnd 11
2026-11-17T06:06:34Z PPU: model size in memory right after the refresh: 110.0 MB
2026-11-17T06:06:49Z Pro: model size in memory before the refresh: None MB
2026-11-17T06:06:49Z Pro: standard refresh started
2026-11-17T06:07:50Z Pro: refresh refreshed (Completed) 
2026-11-17T06:07:50Z Pro: model size in memory right after the refresh: None MB
```
