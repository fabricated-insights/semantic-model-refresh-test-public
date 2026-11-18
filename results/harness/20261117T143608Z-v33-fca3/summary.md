# Harness run 20261117T143608Z-v33-fca3

- Task: refresh
- Variant: v33-auto-date-time
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 403ad56f-f6df-44d3-9a5b-851f06fc1776
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 1,952 MB, Power Query 1,913 MB, duration 2 min, CPU 135 s, rows 2,791,244, model 74 MB (Backup step in XMLA trace)
- Refresh request 13416ec7-7067-42c5-b66b-e05943f156f3, 2026-11-17T14:37:09.637 to 2026-11-17T14:39:12.95, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v33-auto-date-time on PPU data-1m-v1: refreshed, peak 708 MB (2026-11-17T08:10:06Z).
  - Peak change: +1,244 MB (+175.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 1,952 MB vs 550 MB (+1,402 MB), Power Query 1,913 MB vs 270 MB, model 74 MB vs 73 MB.
- Model size in memory when the full refresh started: 70 MB. The refresh may use the SKU maximum minus this: 102,330 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,996 MB: fits (65%); F16 5,050 MB: fits (39%); F32 10,170 MB: fits (19%); F64 25,530 MB: fits (8%); PPU 102,330 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  fbb53e0d-05a8-434a-9ad9-ec2dac2730d7 TabularSequencePoint        105.5     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        104.4    25.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        102.9    25.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        102.0    25.5 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         14.7    13.9       0
                                                  <NA>               Commit         14.2     0.0    <NA>
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         13.5    12.5       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.6     1.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.3     1.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          3.2     1.8  104990
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          2.4     0.1       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          2.3     0.0       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 432edb86-c284-4575-a0df-35c4f1e9d9a9, 2026-11-17T14:40:05.56Z to 2026-11-17T14:40:53.673Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v33-auto-date-time on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T08:11:22Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T14:36:40Z run 20261117T143608Z-v33-fca3: variant=v33-auto-date-time data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T14:36:46Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T14:36:50Z PPU: v33-auto-date-time is fbb53e0d-05a8-434a-9ad9-ec2dac2730d7, DataTag reads back data-1m-v1
2026-11-17T14:36:50Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T14:36:51Z Pro: v33-auto-date-time is 19dc9ffc-6b26-46b1-b855-4c4f620ad74b, DataTag reads back data-1m-v1
2026-11-17T14:37:06Z PPU: model size in memory before the refresh: 69.7 MB
2026-11-17T14:37:09Z PPU: trace started (full)
2026-11-17T14:37:09Z PPU: refresh started, request 13416ec7-7067-42c5-b66b-e05943f156f3
2026-11-17T14:39:20Z PPU: refresh refreshed (Completed) 
2026-11-17T14:39:51Z PPU: trace captured 367 events: ProgressReportEnd 347, ExecutionMetrics 10, CommandEnd 10
2026-11-17T14:39:51Z PPU: model size in memory right after the refresh: 96.2 MB
2026-11-17T14:40:05Z Pro: model size in memory before the refresh: None MB
2026-11-17T14:40:05Z Pro: standard refresh started
2026-11-17T14:41:05Z Pro: refresh refreshed (Completed) 
2026-11-17T14:41:05Z Pro: model size in memory right after the refresh: None MB
```
