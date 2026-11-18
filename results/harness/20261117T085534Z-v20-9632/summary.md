# Harness run 20261117T085534Z-v20-9632

- Task: refresh
- Variant: v20-pq-sort
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 7c88fdb6-1589-414f-859d-581eb7234e2f
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 5,219 MB, Power Query 5,008 MB, duration 6 min, CPU 477 s, rows 2,561,140, model 72 MB (Backup step in XMLA trace)
- Refresh request 0182d809-cf2a-4d89-95da-f0bd25d553f7, 2026-11-17T08:56:39.5 to 2026-11-17T09:02:53.903, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v20-pq-sort on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 5,219 MB vs 550 MB (+4,669 MB), Power Query 5,008 MB vs 270 MB, model 72 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (170%); F16 5,120 MB: OVER (102%); F32 10,240 MB: fits (51%); F64 25,600 MB: fits (20%); PPU 102,400 MB: fits (5%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    6507a4e8-9e64-476c-92dd-186299e9d72f TabularSequencePoint        368.4     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        326.8    18.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        223.9    18.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        223.5    18.5 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        102.8     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          8.7     9.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.5     8.5       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.2     1.6       0
                                                                    <NA>               Commit          4.7     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.0     1.6       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.9     1.5  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.8     0.6       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 8 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 3ab2aaab-bea8-4f24-b243-033536568869, 2026-11-17T09:04:06.633Z to 2026-11-17T09:12:05.66Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v20-pq-sort on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T08:56:12Z run 20261117T085534Z-v20-9632: variant=v20-pq-sort data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T08:56:17Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T08:56:20Z PPU: v20-pq-sort is 6507a4e8-9e64-476c-92dd-186299e9d72f, DataTag reads back data-1m-v1
2026-11-17T08:56:20Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T08:56:21Z Pro: v20-pq-sort is 9ba227b5-b6d9-4408-802d-1748ad2c3722, DataTag reads back data-1m-v1
2026-11-17T08:56:35Z PPU: model size in memory before the refresh: 0.0 MB
2026-11-17T08:56:39Z PPU: trace started (full)
2026-11-17T08:56:39Z PPU: refresh started, request 0182d809-cf2a-4d89-95da-f0bd25d553f7
2026-11-17T09:03:21Z PPU: refresh refreshed (Completed) 
2026-11-17T09:03:52Z PPU: trace captured 282 events: ProgressReportEnd 237, ExecutionMetrics 34, CommandEnd 11
2026-11-17T09:03:53Z PPU: model size in memory right after the refresh: 91.9 MB
2026-11-17T09:04:06Z Pro: model size in memory before the refresh: None MB
2026-11-17T09:04:06Z Pro: standard refresh started
2026-11-17T09:12:08Z Pro: refresh refreshed (Completed) 
2026-11-17T09:12:08Z Pro: model size in memory right after the refresh: None MB
```
