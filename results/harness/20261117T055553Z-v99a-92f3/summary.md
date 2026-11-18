# Harness run 20261117T055553Z-v99a-92f3

- Task: refresh
- Variant: v99a-no-big-calc-tables
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 2bad6523-1448-4ff4-ac18-2c754e4945ff
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 16,045 MB, Power Query 15,926 MB, duration 21 min, CPU 2,410 s, rows 22,085,043, model 185 MB (Backup step in XMLA trace)
- Refresh request b8a3b7ff-6bff-4409-b5a9-a24948a0d4ee, 2026-11-17T05:58:49.303 to 2026-11-17T06:20:08.903, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99a-no-big-calc-tables on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 16,045 MB vs 550 MB (+15,495 MB), Power Query 15,926 MB vs 270 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (523%); F16 5,120 MB: OVER (313%); F32 10,240 MB: OVER (157%); F64 25,600 MB: fits (63%); PPU 102,400 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  948a9aac-0241-4366-b5de-ce4224c7bc48 TabularSequencePoint       1264.7     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1251.7    26.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        773.3    26.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        773.1    26.3 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        478.3     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        354.5     2.7       0
                         Customer Stats.Customer Stats           ExecuteSql        180.3     0.0       0
                         Customer Stats.Customer Stats              Process        174.1     2.6       0
                         Customer Stats.Customer Stats             ReadData        173.5     2.2  471482
                                                  <NA>               Commit         12.4     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.7     1.9       0
                                Sales.Sales Line Label       TabularRefresh          6.1     5.8       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 29 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request f6058aec-9589-4e76-9f65-594c6363958b, 2026-11-17T06:21:30.393Z to 2026-11-17T06:50:33.707Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99a-no-big-calc-tables on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T05:58:11Z run 20261117T055553Z-v99a-92f3: variant=v99a-no-big-calc-tables data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T05:58:20Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T05:58:22Z PPU: v99a-no-big-calc-tables is 948a9aac-0241-4366-b5de-ce4224c7bc48, DataTag reads back data-1m-v1
2026-11-17T05:58:22Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T05:58:23Z Pro: v99a-no-big-calc-tables is dd227607-351c-4da2-9567-c2fd3fd51c22, DataTag reads back data-1m-v1
2026-11-17T05:58:45Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T05:58:49Z PPU: trace started (full)
2026-11-17T05:58:49Z PPU: refresh started, request b8a3b7ff-6bff-4409-b5a9-a24948a0d4ee
2026-11-17T06:20:33Z PPU: refresh refreshed (Completed) 
2026-11-17T06:21:03Z PPU: trace captured 490 events: ProgressReportEnd 443, ExecutionMetrics 36, CommandEnd 11
2026-11-17T06:21:05Z PPU: model size in memory right after the refresh: 232.6 MB
2026-11-17T06:21:30Z Pro: model size in memory before the refresh: None MB
2026-11-17T06:21:30Z Pro: standard refresh started
2026-11-17T06:50:35Z Pro: refresh refreshed (Completed) 
2026-11-17T06:50:35Z Pro: model size in memory right after the refresh: None MB
```
