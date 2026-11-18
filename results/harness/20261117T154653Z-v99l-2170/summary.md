# Harness run 20261117T154653Z-v99l-2170

- Task: refresh
- Variant: v99l-no-calc-columns
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 1944796d-f519-4aa6-9117-01bcf6c40ffc
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 12,878 MB, Power Query 12,811 MB, duration 8 min, CPU 766 s, rows 3,292,315, model 158 MB (Backup step in XMLA trace)
- Refresh request 395d2dae-7227-47a4-a10f-4145703a9549, 2026-11-17T15:50:21.85 to 2026-11-17T15:58:25.477, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99l-no-calc-columns on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 12,878 MB vs 550 MB (+12,328 MB), Power Query 12,811 MB vs 270 MB, model 158 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (420%); F16 5,120 MB: OVER (252%); F32 10,240 MB: OVER (126%); F64 25,600 MB: fits (50%); PPU 102,400 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  bd05e14c-0c16-4a5f-9ea0-0eac63361a0c TabularSequencePoint        469.6     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        457.7    22.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        247.4    22.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        247.0    22.5 2349091
                         Customer Stats.Customer Stats       TabularRefresh        210.1     2.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        210.1     0.0       0
                         Customer Stats.Customer Stats           ExecuteSql        153.4     0.0       0
                         Customer Stats.Customer Stats              Process         56.5     2.4       0
                         Customer Stats.Customer Stats             ReadData         56.0     2.0  471482
                                                  <NA>               Commit         10.1     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.8     1.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.3     7.6       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 17 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 45df4ba6-2c38-4fd6-8c66-26a6f8a4ece0, 2026-11-17T15:59:19.853Z to 2026-11-17T16:16:33.693Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99l-no-calc-columns on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T15:49:35Z run 20261117T154653Z-v99l-2170: variant=v99l-no-calc-columns data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T15:49:48Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T15:49:51Z PPU: v99l-no-calc-columns is bd05e14c-0c16-4a5f-9ea0-0eac63361a0c, DataTag reads back data-1m-v1
2026-11-17T15:49:51Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T15:49:52Z Pro: v99l-no-calc-columns is 0f6c29d2-64ea-4290-8edb-60429d55affa, DataTag reads back data-1m-v1
2026-11-17T15:50:18Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T15:50:21Z PPU: trace started (full)
2026-11-17T15:50:22Z PPU: refresh started, request 395d2dae-7227-47a4-a10f-4145703a9549
2026-11-17T15:58:33Z PPU: refresh refreshed (Completed) 
2026-11-17T15:59:04Z PPU: trace captured 448 events: ProgressReportEnd 403, ExecutionMetrics 34, CommandEnd 11
2026-11-17T15:59:05Z PPU: model size in memory right after the refresh: 194.2 MB
2026-11-17T15:59:19Z Pro: model size in memory before the refresh: None MB
2026-11-17T15:59:19Z Pro: standard refresh started
2026-11-17T16:16:52Z Pro: refresh refreshed (Completed) 
2026-11-17T16:16:52Z Pro: model size in memory right after the refresh: None MB
```
