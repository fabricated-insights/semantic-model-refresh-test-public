# Harness run 20261117T100637Z-v99e-a6d6

- Task: refresh
- Variant: v99e-sales-flat
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: fed53685-ce77-4269-8f4c-48bb1cdefd26
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 23,382 MB, Power Query 23,276 MB, duration 22 min, CPU 4,256 s, rows 24,459,705, model 323 MB (Backup step in XMLA trace)
- Refresh request ec226530-f90e-4b80-b486-6a08345c3884, 2026-11-17T10:10:01.467 to 2026-11-17T10:32:04.843, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99e-sales-flat on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 23,382 MB vs 550 MB (+22,832 MB), Power Query 23,276 MB vs 270 MB, model 323 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (763%); F16 5,120 MB: OVER (457%); F32 10,240 MB: OVER (228%); F64 25,600 MB: fits (91%); PPU 102,400 MB: fits (23%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            a580ec47-fa81-43a8-98d8-f79d00b354d1 TabularSequencePoint       1300.8     0.2       0
                           Sales Flat.Sales Flat       TabularRefresh       1285.9    65.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1221.1    21.7       0
                           Sales Flat.Sales Flat           ExecuteSql        776.3     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        675.5    21.7       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        675.2    21.6 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        545.4     0.0       0
                           Sales Flat.Sales Flat              Process        509.3    65.3       0
                           Sales Flat.Sales Flat             ReadData        508.6    65.2 2349091
                   Customer Stats.Customer Stats       TabularRefresh        504.7     2.2       0
                   Customer Stats.Customer Stats           ExecuteSql        309.1     0.0       0
                   Customer Stats.Customer Stats              Process        195.4     2.2       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 57 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request c746e23f-c092-4f2e-b168-6b5bd3794bee, 2026-11-17T10:33:05.577Z to 2026-11-17T11:29:49.207Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99e-sales-flat on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T10:09:19Z run 20261117T100637Z-v99e-a6d6: variant=v99e-sales-flat data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T10:09:26Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T10:09:29Z PPU: v99e-sales-flat is a580ec47-fa81-43a8-98d8-f79d00b354d1, DataTag reads back data-1m-v1
2026-11-17T10:09:29Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T10:09:30Z Pro: v99e-sales-flat is 501ed679-2c3e-4eb5-9103-ebd582eec18f, DataTag reads back data-1m-v1
2026-11-17T10:09:57Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T10:10:01Z PPU: trace started (full)
2026-11-17T10:10:01Z PPU: refresh started, request ec226530-f90e-4b80-b486-6a08345c3884
2026-11-17T10:32:18Z PPU: refresh refreshed (Completed) 
2026-11-17T10:32:48Z PPU: trace captured 652 events: ProgressReportEnd 605, ExecutionMetrics 36, CommandEnd 11
2026-11-17T10:32:50Z PPU: model size in memory right after the refresh: 459.7 MB
2026-11-17T10:33:05Z Pro: model size in memory before the refresh: None MB
2026-11-17T10:33:05Z Pro: standard refresh started
2026-11-17T11:30:15Z Pro: refresh refreshed (Completed) 
2026-11-17T11:30:15Z Pro: model size in memory right after the refresh: None MB
```
