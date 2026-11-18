# Harness run 20261117T063521Z-v28-7a20

- Task: refresh
- Variant: v28-types-all-text
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: cfbb2646-b528-4f6c-a5b3-3621cc98d8df
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 687 MB, Power Query 583 MB, duration 1 min, CPU 160 s, rows 2,561,140, model 69 MB (Backup step in XMLA trace)
- Refresh request e89da547-ff32-46e6-94f9-7148e343ce04, 2026-11-17T06:36:40.273 to 2026-11-17T06:38:17.117, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v28-types-all-text on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 687 MB vs 550 MB (+137 MB), Power Query 583 MB vs 270 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (22%); F16 5,120 MB: fits (13%); F32 10,240 MB: fits (7%); F64 25,600 MB: fits (3%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    c247c1bb-bfef-4c45-b306-7b5ea0d8fe26 TabularSequencePoint         88.0     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         84.2    47.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         81.2    47.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         80.8    47.8 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.8    10.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.6     2.9       0
                                                                    <NA>               Commit          5.2     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.7     2.9       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.7     1.2       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          3.6     2.9  104990
                                                      Sales.Order Number       TabularRefresh          3.5     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.9     0.0       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 53dc6487-5e6e-4100-82b4-b01af4ec8040, 2026-11-17T06:39:04.347Z to 2026-11-17T06:39:47.337Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v28-types-all-text on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T06:36:12Z run 20261117T063521Z-v28-7a20: variant=v28-types-all-text data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T06:36:18Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T06:36:21Z PPU: v28-types-all-text is c247c1bb-bfef-4c45-b306-7b5ea0d8fe26, DataTag reads back data-1m-v1
2026-11-17T06:36:21Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T06:36:22Z Pro: v28-types-all-text is 6391583e-bd04-41bb-9d15-92bd6c0a4db7, DataTag reads back data-1m-v1
2026-11-17T06:36:36Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T06:36:40Z PPU: trace started (full)
2026-11-17T06:36:40Z PPU: refresh started, request e89da547-ff32-46e6-94f9-7148e343ce04
2026-11-17T06:38:20Z PPU: refresh refreshed (Completed) 
2026-11-17T06:38:51Z PPU: trace captured 282 events: ProgressReportEnd 237, ExecutionMetrics 34, CommandEnd 11
2026-11-17T06:38:52Z PPU: model size in memory right after the refresh: 171.5 MB
2026-11-17T06:39:04Z Pro: model size in memory before the refresh: None MB
2026-11-17T06:39:04Z Pro: standard refresh started
2026-11-17T06:40:04Z Pro: refresh refreshed (Completed) 
2026-11-17T06:40:04Z Pro: model size in memory right after the refresh: None MB
```
