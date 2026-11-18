# Harness run 20261117T144201Z-v99n-50ff

- Task: refresh
- Variant: v99n-text-staging
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 61ebb070-c93d-4665-9853-04abd28c7052
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 905 MB, Power Query 841 MB, duration 10 min, CPU 657 s, rows 21,587,990, model 92 MB (Backup step in XMLA trace)
- Refresh request 2c75dccb-ac30-41bd-8055-8e1d94620708, 2026-11-17T14:44:39.587 to 2026-11-17T14:54:43.897, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99n-text-staging on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 905 MB vs 550 MB (+355 MB), Power Query 841 MB vs 270 MB, model 92 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (30%); F16 5,120 MB: fits (18%); F32 10,240 MB: fits (9%); F64 25,600 MB: fits (4%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    b50ca483-f3ad-48d4-bf77-74585e534ddb TabularSequencePoint        596.3     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        590.5    31.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        588.5    31.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        588.2    31.0 2349091
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          8.3     0.6       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          7.3     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.2     8.1       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.1     1.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.9     5.9       0
                                                                    <NA>               Commit          5.3     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          4.8     1.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          4.7     1.8  104990
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 5 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 44914c55-9812-4631-be03-b2b33f9a0902, 2026-11-17T14:55:37.527Z to 2026-11-17T15:00:50.493Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99n-text-staging on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T14:44:04Z run 20261117T144201Z-v99n-50ff: variant=v99n-text-staging data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T14:44:11Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T14:44:14Z PPU: v99n-text-staging is b50ca483-f3ad-48d4-bf77-74585e534ddb, DataTag reads back data-1m-v1
2026-11-17T14:44:14Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T14:44:15Z Pro: v99n-text-staging is 7a89f3dd-ca6e-4836-b3b2-383ccd224876, DataTag reads back data-1m-v1
2026-11-17T14:44:35Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T14:44:39Z PPU: trace started (full)
2026-11-17T14:44:39Z PPU: refresh started, request 2c75dccb-ac30-41bd-8055-8e1d94620708
2026-11-17T14:54:51Z PPU: refresh refreshed (Completed) 
2026-11-17T14:55:22Z PPU: trace captured 434 events: ProgressReportEnd 389, ExecutionMetrics 34, CommandEnd 11
2026-11-17T14:55:23Z PPU: model size in memory right after the refresh: 124.3 MB
2026-11-17T14:55:37Z Pro: model size in memory before the refresh: None MB
2026-11-17T14:55:37Z Pro: standard refresh started
2026-11-17T15:01:08Z Pro: refresh refreshed (Completed) 
2026-11-17T15:01:08Z Pro: model size in memory right after the refresh: None MB
```
