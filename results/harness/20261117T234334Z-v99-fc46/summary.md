# Harness run 20261117T234334Z-v99-fc46

- Task: refresh
- Variant: v99-kitchen-sink
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: f3bd52d5-ee56-4200-acfd-8d009813057d
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 25,882 MB, Power Query 25,777 MB, duration 15 min, CPU 3,144 s, rows 40,515,912, model 619 MB (Backup step in XMLA trace)
- Refresh request 83baf927-032b-4f37-9abb-832fd2038550, 2026-11-17T23:44:42.887 to 2026-11-18T00:00:01.453, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99-kitchen-sink on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 25,882 MB vs 550 MB (+25,332 MB), Power Query 25,777 MB vs 270 MB, model 619 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (844%); F16 5,120 MB: OVER (506%); F32 10,240 MB: OVER (253%); F64 25,600 MB: OVER (101%); PPU 102,400 MB: fits (25%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            67527e72-ce42-4278-b95a-711034a934b6 TabularSequencePoint        903.4     0.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        846.4    22.5       0
                           Sales Flat.Sales Flat       TabularRefresh        822.8    66.9       0
                           Sales Flat.Sales Flat           ExecuteSql        652.3     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        606.9     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        595.5     2.4       0
                   Customer Stats.Customer Stats           ExecuteSql        365.9     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        239.3    22.4       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        239.1    22.4 2349091
                   Customer Stats.Customer Stats              Process        229.5     2.4       0
                   Customer Stats.Customer Stats             ReadData        229.0     2.0  471482
                           Sales Flat.Sales Flat              Process        170.3    66.8       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 31 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 0b0d5d08-8fec-4b45-bcb9-4d022d3d2a26, 2026-11-18T00:01:11.48Z to 2026-11-18T00:31:58.29Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99-kitchen-sink on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T23:44:09Z run 20261117T234334Z-v99-fc46: variant=v99-kitchen-sink data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T23:44:19Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T23:44:24Z PPU: v99-kitchen-sink is 67527e72-ce42-4278-b95a-711034a934b6, DataTag reads back data-1m-v1
2026-11-17T23:44:24Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T23:44:25Z Pro: v99-kitchen-sink is 4af1fdd1-397f-427c-be5d-3ea9bc11943d, DataTag reads back data-1m-v1
2026-11-17T23:44:39Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T23:44:42Z PPU: trace started (full)
2026-11-17T23:44:43Z PPU: refresh started, request 83baf927-032b-4f37-9abb-832fd2038550
2026-11-18T00:00:25Z PPU: refresh refreshed (Completed) 
2026-11-18T00:00:56Z PPU: trace captured 771 events: ProgressReportEnd 726, ExecutionMetrics 34, CommandEnd 11
2026-11-18T00:00:58Z PPU: model size in memory right after the refresh: 744.1 MB
2026-11-18T00:01:11Z Pro: model size in memory before the refresh: None MB
2026-11-18T00:01:11Z Pro: standard refresh started
2026-11-18T00:32:16Z Pro: refresh refreshed (Completed) 
2026-11-18T00:32:16Z Pro: model size in memory right after the refresh: None MB
```
