# Harness run 20261117T092158Z-v18-b144

- Task: refresh
- Variant: v18-pq-10m-summary
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 7600ae2e-65d8-4089-a6f1-fd5556a683cc
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 1,519 MB, Power Query 1,380 MB, duration 2 min, CPU 235 s, rows 2,561,730, model 73 MB (Backup step in XMLA trace)
- Refresh request 74096730-9000-4348-8e32-2fcb8362dacf, 2026-11-17T09:24:40.193 to 2026-11-17T09:26:46.12, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v18-pq-10m-summary on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 1,519 MB vs 550 MB (+969 MB), Power Query 1,380 MB vs 270 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (50%); F16 5,120 MB: fits (30%); F32 10,240 MB: fits (15%); F64 25,600 MB: fits (6%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    5f501e01-52ef-4e24-81c1-aa3cafd4c095 TabularSequencePoint        118.3     0.1       0
                                   Store Year Summary.Store Year Summary       TabularRefresh        118.0     0.1       0
                                   Store Year Summary.Store Year Summary           ExecuteSql        117.9     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         85.3    20.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         80.6    20.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         80.1    20.2 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.2    12.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.0    11.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          8.1     1.9       0
                                                                    <NA>               Commit          5.7     0.0    <NA>
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          5.2     0.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          4.6     0.0       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 2 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 59cad79d-2c46-4db5-a99d-e0ebdd7836bd, 2026-11-17T09:27:47.623Z to 2026-11-17T09:29:22.947Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v18-pq-10m-summary on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T09:24:03Z run 20261117T092158Z-v18-b144: variant=v18-pq-10m-summary data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T09:24:11Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T09:24:14Z PPU: v18-pq-10m-summary is 5f501e01-52ef-4e24-81c1-aa3cafd4c095, DataTag reads back data-1m-v1
2026-11-17T09:24:14Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T09:24:15Z Pro: v18-pq-10m-summary is 45da3519-8fe1-4fbc-8ef6-9489829c8bb0, DataTag reads back data-1m-v1
2026-11-17T09:24:36Z PPU: model size in memory before the refresh: 0.0 MB
2026-11-17T09:24:40Z PPU: trace started (full)
2026-11-17T09:24:40Z PPU: refresh started, request 74096730-9000-4348-8e32-2fcb8362dacf
2026-11-17T09:26:51Z PPU: refresh refreshed (Completed) 
2026-11-17T09:27:21Z PPU: trace captured 300 events: ProgressReportEnd 255, ExecutionMetrics 34, CommandEnd 11
2026-11-17T09:27:22Z PPU: model size in memory right after the refresh: 92.7 MB
2026-11-17T09:27:47Z Pro: model size in memory before the refresh: None MB
2026-11-17T09:27:47Z Pro: standard refresh started
2026-11-17T09:29:48Z Pro: refresh refreshed (Completed) 
2026-11-17T09:29:48Z Pro: model size in memory right after the refresh: None MB
```
