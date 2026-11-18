# Harness run 20261117T225836Z-v99h-0bf5

- Task: refresh
- Variant: v99h-staging-buffers
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: bded471b-2087-4155-bfae-9e891e23682e
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 25,939 MB, Power Query 25,818 MB, duration 18 min, CPU 3,900 s, rows 38,422,496, model 534 MB (Backup step in XMLA trace)
- Refresh request bfaf9adc-af17-41be-965d-a00e31345cc2, 2026-11-17T22:59:33.187 to 2026-11-17T23:18:13.11, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99h-staging-buffers on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 25,939 MB vs 550 MB (+25,389 MB), Power Query 25,818 MB vs 270 MB, model 534 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (846%); F16 5,120 MB: OVER (507%); F32 10,240 MB: OVER (253%); F64 25,600 MB: OVER (101%); PPU 102,400 MB: fits (25%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            fceac6f8-d619-41bc-83ea-24304ed40142 TabularSequencePoint       1105.9     0.4       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1062.8    25.2       0
                           Sales Flat.Sales Flat       TabularRefresh       1041.8    79.2       0
                           Sales Flat.Sales Flat           ExecuteSql        850.5     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        767.0     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        679.4     2.6       0
                   Customer Stats.Customer Stats           ExecuteSql        441.8     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        295.7    25.1       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        295.5    25.1 2349091
                   Customer Stats.Customer Stats              Process        237.4     2.6       0
                   Customer Stats.Customer Stats             ReadData        236.8     2.1  471482
                           Sales Flat.Sales Flat              Process        191.3    79.1       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 22 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 7697b66e-8400-4f77-8f37-1565dbcabb35, 2026-11-17T23:19:00.477Z to 2026-11-17T23:41:10.227Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99h-staging-buffers on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T22:59:00Z run 20261117T225836Z-v99h-0bf5: variant=v99h-staging-buffers data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T22:59:10Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T22:59:13Z PPU: v99h-staging-buffers is fceac6f8-d619-41bc-83ea-24304ed40142, DataTag reads back data-1m-v1
2026-11-17T22:59:13Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T22:59:16Z Pro: v99h-staging-buffers is f80e532f-84c0-4fd5-95ad-f4fcbae06174, DataTag reads back data-1m-v1
2026-11-17T22:59:29Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T22:59:33Z PPU: trace started (full)
2026-11-17T22:59:33Z PPU: refresh started, request bfaf9adc-af17-41be-965d-a00e31345cc2
2026-11-17T23:18:16Z PPU: refresh refreshed (Completed) 
2026-11-17T23:18:47Z PPU: trace captured 844 events: ProgressReportEnd 799, ExecutionMetrics 34, CommandEnd 11
2026-11-17T23:18:48Z PPU: model size in memory right after the refresh: 660.7 MB
2026-11-17T23:19:00Z Pro: model size in memory before the refresh: None MB
2026-11-17T23:19:00Z Pro: standard refresh started
2026-11-17T23:41:34Z Pro: refresh refreshed (Completed) 
2026-11-17T23:41:34Z Pro: model size in memory right after the refresh: None MB
```
