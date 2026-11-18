# Harness run 20261116T224902Z-v00-c9d5

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: d0923d0a-46d3-411f-a002-10c5de883fa1
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 550 MB, Power Query 270 MB, duration 1 min, CPU 97 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request 147be3e3-735f-4222-aac1-a3249bea825a, 2026-11-16T22:51:53.077 to 2026-11-16T22:52:57.833, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v00-baseline on PPU data-1m-v1.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (18%); F16 5,120 MB: fits (11%); F32 10,240 MB: fits (5%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    0eee6936-1906-41cc-ae01-289b0589e4e1 TabularSequencePoint         56.4     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         55.7    17.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         52.7    17.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         51.6    17.8 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.8    11.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.7    10.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.0     1.7       0
                                                                    <NA>               Commit          4.6     0.0    <NA>
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.2     0.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          3.0     0.0       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          2.8     0.1       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          2.6     0.1       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 8a80d744-3fd7-4f48-aedd-9f56104dc0c7, 2026-11-16T22:53:39.957Z to 2026-11-16T22:54:27.51Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v00-baseline on Pro data-1m-v1: refreshed, peak n/a (2026-11-16T20:38:17Z).
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-16T22:51:17Z run 20261116T224902Z-v00-c9d5: variant=v00-baseline data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-16T22:51:23Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-16T22:51:25Z PPU: v00-baseline is 0eee6936-1906-41cc-ae01-289b0589e4e1, DataTag reads back data-1m-v1
2026-11-16T22:51:25Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-16T22:51:29Z Pro: v00-baseline is d617fd07-8a52-4fda-ab69-2b58d0426997, DataTag reads back data-1m-v1
2026-11-16T22:51:49Z PPU: model size in memory before the refresh: 0.0 MB
2026-11-16T22:51:53Z PPU: trace started (full)
2026-11-16T22:51:53Z PPU: refresh started, request 147be3e3-735f-4222-aac1-a3249bea825a
2026-11-16T22:53:03Z PPU: refresh refreshed (Completed) 
2026-11-16T22:53:34Z PPU: trace captured 271 events: ProgressReportEnd 237, ExecutionMetrics 23, CommandEnd 11
2026-11-16T22:53:34Z PPU: model size in memory right after the refresh: 92.7 MB
2026-11-16T22:53:39Z Pro: model size in memory before the refresh: None MB
2026-11-16T22:53:39Z Pro: standard refresh started
2026-11-16T22:54:40Z Pro: refresh refreshed (Completed) 
2026-11-16T22:54:40Z Pro: model size in memory right after the refresh: None MB
```
