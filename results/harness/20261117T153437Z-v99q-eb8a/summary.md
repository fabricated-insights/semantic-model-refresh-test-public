# Harness run 20261117T153437Z-v99q-eb8a

- Task: refresh
- Variant: v99q-customer-stats
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 81036a31-30c1-440e-a7c1-e51b2bedb70e
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 3,700 MB, Power Query 3,535 MB, duration 7 min, CPU 437 s, rows 22,055,454, model 114 MB (Backup step in XMLA trace)
- Refresh request de2bb310-e76c-48dd-b10e-ae3857c9a9f7, 2026-11-17T15:35:50.22 to 2026-11-17T15:42:37.157, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99q-customer-stats on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 3,700 MB vs 550 MB (+3,150 MB), Power Query 3,535 MB vs 270 MB, model 114 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (121%); F16 5,120 MB: fits (72%); F32 10,240 MB: fits (36%); F64 25,600 MB: fits (14%); PPU 102,400 MB: fits (4%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    a0c7fd43-3720-419e-a1cf-b0e193d83052 TabularSequencePoint        394.7     0.4       0
                                           Customer Stats.Customer Stats       TabularRefresh        381.2     4.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        318.7    34.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        301.8    34.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        301.0    34.5 2349091
                                           Customer Stats.Customer Stats           ExecuteSql        294.8     0.0       0
                                           Customer Stats.Customer Stats              Process         86.3     3.9       0
                                           Customer Stats.Customer Stats             ReadData         85.8     3.5  471482
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         26.2     2.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql         16.7     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh         16.2     0.9       0
                                                  Sales.Sales Line Label       TabularRefresh         14.6    13.0       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 2 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 549dbebf-bcbf-4294-87cb-ba5e848b4906, 2026-11-17T15:43:47.427Z to 2026-11-17T15:45:17.767Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99q-customer-stats on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T15:35:22Z run 20261117T153437Z-v99q-eb8a: variant=v99q-customer-stats data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T15:35:28Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T15:35:32Z PPU: v99q-customer-stats is a0c7fd43-3720-419e-a1cf-b0e193d83052, DataTag reads back data-1m-v1
2026-11-17T15:35:32Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T15:35:33Z Pro: v99q-customer-stats is cb418f0d-011c-4722-8b2d-68fc739e28d9, DataTag reads back data-1m-v1
2026-11-17T15:35:46Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T15:35:50Z PPU: trace started (full)
2026-11-17T15:35:50Z PPU: refresh started, request de2bb310-e76c-48dd-b10e-ae3857c9a9f7
2026-11-17T15:43:01Z PPU: refresh refreshed (Completed) 
2026-11-17T15:43:32Z PPU: trace captured 451 events: ProgressReportEnd 406, ExecutionMetrics 34, CommandEnd 11
2026-11-17T15:43:34Z PPU: model size in memory right after the refresh: 162.1 MB
2026-11-17T15:43:47Z Pro: model size in memory before the refresh: None MB
2026-11-17T15:43:47Z Pro: standard refresh started
2026-11-17T15:45:47Z Pro: refresh refreshed (Completed) 
2026-11-17T15:45:47Z Pro: model size in memory right after the refresh: None MB
```
