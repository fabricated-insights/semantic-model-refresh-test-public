# Harness run 20261117T123951Z-v99f-bc92

- Task: refresh
- Variant: v99f-calc-tables
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: e93b7068-8b97-40db-9eb5-6bc8792484b3
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 22,870 MB, Power Query 22,756 MB, duration 23 min, CPU 4,628 s, rows 36,073,405, model 361 MB (Backup step in XMLA trace)
- Refresh request f65a146a-7ae7-4eb7-b70c-5fd14f62c9df, 2026-11-17T12:43:02.017 to 2026-11-17T13:06:41.003, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99f-calc-tables on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 22,870 MB vs 550 MB (+22,320 MB), Power Query 22,756 MB vs 270 MB, model 361 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (746%); F16 5,120 MB: OVER (447%); F32 10,240 MB: OVER (223%); F64 25,600 MB: fits (89%); PPU 102,400 MB: fits (22%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            78a00a5c-5123-48ef-a449-f334f1e5852f TabularSequencePoint       1390.7     0.4       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1304.9    27.8       0
                           Sales Flat.Sales Flat       TabularRefresh       1280.6    88.5       0
                           Sales Flat.Sales Flat           ExecuteSql        963.5     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        751.7     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        717.5     3.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        553.1    27.7       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        552.5    27.7 2349091
                   Customer Stats.Customer Stats           ExecuteSql        480.6     0.0       0
                           Sales Flat.Sales Flat              Process        316.9    88.4       0
                           Sales Flat.Sales Flat             ReadData        316.0    88.4 2349091
                   Customer Stats.Customer Stats              Process        236.8     3.2       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 27 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 80625f27-90ce-4279-b807-a8a23bca9c18, 2026-11-17T13:07:33.48Z to 2026-11-17T13:35:01.5Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99f-calc-tables on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T12:42:24Z run 20261117T123951Z-v99f-bc92: variant=v99f-calc-tables data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T12:42:30Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T12:42:34Z PPU: v99f-calc-tables is 78a00a5c-5123-48ef-a449-f334f1e5852f, DataTag reads back data-1m-v1
2026-11-17T12:42:34Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T12:42:35Z Pro: v99f-calc-tables is 0ab28c16-fec1-459d-9a1d-545cd285070a, DataTag reads back data-1m-v1
2026-11-17T12:42:58Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T12:43:01Z PPU: trace started (full)
2026-11-17T12:43:02Z PPU: refresh started, request f65a146a-7ae7-4eb7-b70c-5fd14f62c9df
2026-11-17T13:06:46Z PPU: refresh refreshed (Completed) 
2026-11-17T13:07:17Z PPU: trace captured 713 events: ProgressReportEnd 666, ExecutionMetrics 36, CommandEnd 11
2026-11-17T13:07:19Z PPU: model size in memory right after the refresh: 491.7 MB
2026-11-17T13:07:32Z Pro: model size in memory before the refresh: None MB
2026-11-17T13:07:33Z Pro: standard refresh started
2026-11-17T13:35:08Z Pro: refresh refreshed (Completed) 
2026-11-17T13:35:08Z Pro: model size in memory right after the refresh: None MB
```
