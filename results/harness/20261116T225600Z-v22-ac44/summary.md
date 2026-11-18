# Harness run 20261116T225600Z-v22-ac44

- Task: refresh
- Variant: v22-dax-calc-columns
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: bd0cda2d-10f5-4eb4-9187-ddba3a4d0e74
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 621 MB, Power Query 271 MB, duration 1 min, CPU 108 s, rows 21,353,868, model 101 MB (Backup step in XMLA trace)
- Refresh request 8be0f184-c517-469c-9d05-e948dedc01f5, 2026-11-16T22:59:00.56 to 2026-11-16T23:00:08.77, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v22-dax-calc-columns on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 621 MB vs 550 MB (+71 MB), Power Query 271 MB vs 270 MB, model 101 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (20%); F16 5,120 MB: fits (12%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    f04681eb-fd6e-44c2-902a-dad6c2273007 TabularSequencePoint         60.8     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         53.4    18.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         50.5    18.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         50.2    18.8 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.2     7.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.0     6.1       0
                                                                    <NA>               Commit          5.5     0.0    <NA>
                                                  Sales.Sales Line Label       TabularRefresh          5.4     5.2       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.0     1.7       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.1     0.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.8     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.6     1.7       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 06d1da3b-7a55-4820-9787-606a3c5f935e, 2026-11-16T23:01:13.633Z to 2026-11-16T23:02:09.747Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v22-dax-calc-columns on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-16T22:58:24Z run 20261116T225600Z-v22-ac44: variant=v22-dax-calc-columns data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-16T22:58:33Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-16T22:58:35Z PPU: v22-dax-calc-columns is f04681eb-fd6e-44c2-902a-dad6c2273007, DataTag reads back data-1m-v1
2026-11-16T22:58:35Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-16T22:58:38Z Pro: v22-dax-calc-columns is 1c294d69-ca0d-4f75-8938-a00dc5a173ae, DataTag reads back data-1m-v1
2026-11-16T22:58:57Z PPU: model size in memory before the refresh: 0.0 MB
2026-11-16T22:59:00Z PPU: trace started (full)
2026-11-16T22:59:00Z PPU: refresh started, request 8be0f184-c517-469c-9d05-e948dedc01f5
2026-11-16T23:00:11Z PPU: refresh refreshed (Completed) 
2026-11-16T23:00:41Z PPU: trace captured 311 events: ProgressReportEnd 277, ExecutionMetrics 23, CommandEnd 11
2026-11-16T23:00:42Z PPU: model size in memory right after the refresh: 132.6 MB
2026-11-16T23:01:13Z Pro: model size in memory before the refresh: None MB
2026-11-16T23:01:13Z Pro: standard refresh started
2026-11-16T23:02:13Z Pro: refresh refreshed (Completed) 
2026-11-16T23:02:13Z Pro: model size in memory right after the refresh: None MB
```
