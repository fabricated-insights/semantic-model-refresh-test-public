# Harness run 20261117T150225Z-v99o-c4ef

- Task: refresh
- Variant: v99o-sorts
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 8832b983-60a9-41b5-acdc-155a6b5c523e
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 5,182 MB, Power Query 4,917 MB, duration 12 min, CPU 1,135 s, rows 21,583,972, model 99 MB (Backup step in XMLA trace)
- Refresh request bce35c97-38bd-4668-a478-d5a7a2bd8e16, 2026-11-17T15:06:41.207 to 2026-11-17T15:19:18.307, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99o-sorts on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 5,182 MB vs 550 MB (+4,632 MB), Power Query 4,917 MB vs 270 MB, model 99 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (169%); F16 5,120 MB: OVER (101%); F32 10,240 MB: fits (51%); F64 25,600 MB: fits (20%); PPU 102,400 MB: fits (5%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  c2000c74-e8cf-4893-9b5e-8f96d7ccd23a TabularSequencePoint        747.6     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        727.9    21.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        538.3    21.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        537.9    20.9 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        189.5     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.8     8.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.4     6.5       0
                                Sales.Sales Line Label       TabularRefresh          7.1     6.8       0
                                                  <NA>               Commit          6.5     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.1     2.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.0     2.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.8     1.9  104990
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 7 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request a1453c8f-a542-4930-897f-ec3010451a2c, 2026-11-17T15:20:09.573Z to 2026-11-17T15:26:58.49Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99o-sorts on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T15:05:56Z run 20261117T150225Z-v99o-c4ef: variant=v99o-sorts data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T15:06:08Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T15:06:11Z PPU: v99o-sorts is c2000c74-e8cf-4893-9b5e-8f96d7ccd23a, DataTag reads back data-1m-v1
2026-11-17T15:06:11Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T15:06:12Z Pro: v99o-sorts is e2e544a9-720c-4719-97eb-0294c6aec895, DataTag reads back data-1m-v1
2026-11-17T15:06:37Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T15:06:41Z PPU: trace started (full)
2026-11-17T15:06:41Z PPU: refresh started, request bce35c97-38bd-4668-a478-d5a7a2bd8e16
2026-11-17T15:19:23Z PPU: refresh refreshed (Completed) 
2026-11-17T15:19:54Z PPU: trace captured 433 events: ProgressReportEnd 388, ExecutionMetrics 34, CommandEnd 11
2026-11-17T15:19:56Z PPU: model size in memory right after the refresh: 133.8 MB
2026-11-17T15:20:09Z Pro: model size in memory before the refresh: None MB
2026-11-17T15:20:09Z Pro: standard refresh started
2026-11-17T15:27:10Z Pro: refresh refreshed (Completed) 
2026-11-17T15:27:10Z Pro: model size in memory right after the refresh: None MB
```
