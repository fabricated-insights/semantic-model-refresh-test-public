# Harness run 20261117T174715Z-v99b-b75f

- Task: refresh
- Variant: v99b-one-sales-copy
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: f1b178ca-0102-45a3-b77d-8e45d6ad1e46
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 25,684 MB, Power Query 25,591 MB, duration 23 min, CPU 4,887 s, rows 28,053,515, model 517 MB (Backup step in XMLA trace)
- Refresh request 7990ac49-1dda-4745-8d6f-185cec815041, 2026-11-17T17:48:50.663 to 2026-11-17T18:12:32.15, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99b-one-sales-copy on PPU data-1m-v1: refreshed, peak 25,991 MB (2026-11-17T07:26:14Z).
  - Peak change: -307 MB (-1.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 25,684 MB vs 550 MB (+25,134 MB), Power Query 25,591 MB vs 270 MB, model 517 MB vs 73 MB.
- Model size in memory when the full refresh started: 524 MB. The refresh may use the SKU maximum minus this: 101,876 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,542 MB: OVER (1010%); F16 4,596 MB: OVER (559%); F32 9,716 MB: OVER (264%); F64 25,076 MB: OVER (102%); PPU 101,876 MB: fits (25%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            03d0c1da-34b0-4aba-85d6-ed2d23257e66 TabularSequencePoint       1404.1     0.3       0
                           Sales Flat.Sales Flat       TabularRefresh       1386.4    78.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1341.7    24.2       0
                           Sales Flat.Sales Flat           ExecuteSql       1042.6     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        698.1     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        643.5    24.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        643.3    24.2 2349091
                   Customer Stats.Customer Stats       TabularRefresh        629.4     2.5       0
                   Customer Stats.Customer Stats           ExecuteSql        399.4     0.0       0
                           Sales Flat.Sales Flat              Process        343.6    77.9       0
                           Sales Flat.Sales Flat             ReadData        342.9    77.8 2349091
                   Customer Stats.Customer Stats              Process        229.9     2.5       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 16 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 27b706de-12a3-4c4b-ba9c-728de8510ae5, 2026-11-17T18:13:20.73Z to 2026-11-17T18:29:42.07Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99b-one-sales-copy on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T07:56:37Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T17:48:00Z run 20261117T174715Z-v99b-b75f: variant=v99b-one-sales-copy data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T17:48:16Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T17:48:25Z PPU: v99b-one-sales-copy is 03d0c1da-34b0-4aba-85d6-ed2d23257e66, DataTag reads back data-1m-v1
2026-11-17T17:48:25Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T17:48:27Z Pro: v99b-one-sales-copy is 1c2a3fcf-c1d3-4055-9c06-ead16a7c0f62, DataTag reads back data-1m-v1
2026-11-17T17:48:47Z PPU: model size in memory before the refresh: 523.5 MB
2026-11-17T17:48:50Z PPU: trace started (full)
2026-11-17T17:48:50Z PPU: refresh started, request 7990ac49-1dda-4745-8d6f-185cec815041
2026-11-17T18:12:35Z PPU: refresh refreshed (Completed) 
2026-11-17T18:13:06Z PPU: trace captured 635 events: ProgressReportEnd 614, ExecutionMetrics 11, CommandEnd 10
2026-11-17T18:13:08Z PPU: model size in memory right after the refresh: 640.6 MB
2026-11-17T18:13:20Z Pro: model size in memory before the refresh: None MB
2026-11-17T18:13:20Z Pro: standard refresh started
2026-11-17T18:29:53Z Pro: refresh refreshed (Completed) 
2026-11-17T18:29:53Z Pro: model size in memory right after the refresh: None MB
```
