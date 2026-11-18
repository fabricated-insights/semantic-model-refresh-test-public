# Harness run 20261117T060843Z-v24b-8c56

- Task: refresh
- Variant: v24b-second-fact-bidirectional
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: f1c1e742-07ac-4e00-9da1-4174a5d7413a
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 1,432 MB, Power Query 1,402 MB, duration 1 min, CPU 142 s, rows 3,541,806, model 103 MB (Backup step in XMLA trace)
- Refresh request 041088ca-e1a1-41c9-933e-720ab525e956, 2026-11-17T06:11:17.363 to 2026-11-17T06:12:40.363, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v24b-second-fact-bidirectional on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 1,432 MB vs 550 MB (+882 MB), Power Query 1,402 MB vs 270 MB, model 103 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (47%); F16 5,120 MB: fits (28%); F32 10,240 MB: fits (14%); F64 25,600 MB: fits (6%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  2b9c7b82-fae8-4534-8106-25e802c59a13 TabularSequencePoint         72.5     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         71.7    21.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         70.1    21.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         69.4    20.9 2349091
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa       TabularRefresh         19.0     7.0       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa              Process         18.1     7.0       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa             ReadData         14.4     6.9  980666
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         12.3    13.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         12.1    11.9       0
                                                  <NA>               Commit          7.7     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.6     1.9       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa    AnalyzeEncodeData          3.6     3.8       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 6f63e2ba-1ad5-44a2-bf0f-9a95b3aa6220, 2026-11-17T06:13:46.013Z to 2026-11-17T06:14:44.22Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v24b-second-fact-bidirectional on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T06:10:44Z run 20261117T060843Z-v24b-8c56: variant=v24b-second-fact-bidirectional data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T06:10:51Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T06:10:53Z PPU: v24b-second-fact-bidirectional is 2b9c7b82-fae8-4534-8106-25e802c59a13, DataTag reads back data-1m-v1
2026-11-17T06:10:53Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T06:10:54Z Pro: v24b-second-fact-bidirectional is e87d1e39-81ef-459e-b57b-0271412bfa91, DataTag reads back data-1m-v1
2026-11-17T06:11:13Z PPU: model size in memory before the refresh: 0.0 MB
2026-11-17T06:11:17Z PPU: trace started (full)
2026-11-17T06:11:17Z PPU: refresh started, request 041088ca-e1a1-41c9-933e-720ab525e956
2026-11-17T06:12:58Z PPU: refresh refreshed (Completed) 
2026-11-17T06:13:28Z PPU: trace captured 305 events: ProgressReportEnd 260, ExecutionMetrics 34, CommandEnd 11
2026-11-17T06:13:29Z PPU: model size in memory right after the refresh: 110.0 MB
2026-11-17T06:13:45Z Pro: model size in memory before the refresh: None MB
2026-11-17T06:13:46Z Pro: standard refresh started
2026-11-17T06:14:46Z Pro: refresh refreshed (Completed) 
2026-11-17T06:14:46Z Pro: model size in memory right after the refresh: None MB
```
