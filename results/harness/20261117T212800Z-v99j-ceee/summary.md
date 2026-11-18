# Harness run 20261117T212800Z-v99j-ceee

- Task: refresh
- Variant: v99j-buffer-stg-customer
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 62bbc881-614b-433e-a3f7-b51ea9f480c7
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 22,919 MB, Power Query 22,812 MB, duration 19 min, CPU 3,789 s, rows 38,422,496, model 536 MB (Backup step in XMLA trace)
- Refresh request 2381b1f5-c74c-4385-a4cf-fca962d0afdd, 2026-11-17T21:29:36.443 to 2026-11-17T21:48:45.33, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99j-buffer-stg-customer on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 22,919 MB vs 550 MB (+22,369 MB), Power Query 22,812 MB vs 270 MB, model 536 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (748%); F16 5,120 MB: OVER (448%); F32 10,240 MB: OVER (224%); F64 25,600 MB: fits (90%); PPU 102,400 MB: fits (22%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            69bc2532-0803-4ff1-841a-d6893208f449 TabularSequencePoint       1134.5     0.4       0
                           Sales Flat.Sales Flat       TabularRefresh       1101.0    74.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1052.4    25.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        579.0    24.9       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        578.7    24.9 2349091
                           Sales Flat.Sales Flat              Process        559.8    74.2       0
                           Sales Flat.Sales Flat             ReadData        559.0    74.2 2349091
                           Sales Flat.Sales Flat           ExecuteSql        541.1     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        473.3     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        381.2     2.7       0
                   Customer Stats.Customer Stats           ExecuteSql        270.8     0.0       0
                   Customer Stats.Customer Stats              Process        110.3     2.7       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 15 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 35de8c84-8382-4d11-abbd-a63049e2a5be, 2026-11-17T21:49:37.34Z to 2026-11-17T22:05:04.983Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99j-buffer-stg-customer on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T21:28:47Z run 20261117T212800Z-v99j-ceee: variant=v99j-buffer-stg-customer data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T21:28:56Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T21:29:10Z PPU: v99j-buffer-stg-customer is 69bc2532-0803-4ff1-841a-d6893208f449, DataTag reads back data-1m-v1
2026-11-17T21:29:10Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T21:29:15Z Pro: v99j-buffer-stg-customer is cbaa387f-25ff-4493-a117-b7450fd39e13, DataTag reads back data-1m-v1
2026-11-17T21:29:32Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T21:29:36Z PPU: trace started (full)
2026-11-17T21:29:36Z PPU: refresh started, request 2381b1f5-c74c-4385-a4cf-fca962d0afdd
2026-11-17T21:48:49Z PPU: refresh refreshed (Completed) 
2026-11-17T21:49:20Z PPU: trace captured 844 events: ProgressReportEnd 799, ExecutionMetrics 34, CommandEnd 11
2026-11-17T21:49:22Z PPU: model size in memory right after the refresh: 662.8 MB
2026-11-17T21:49:36Z Pro: model size in memory before the refresh: None MB
2026-11-17T21:49:37Z Pro: standard refresh started
2026-11-17T22:05:09Z Pro: refresh refreshed (Completed) 
2026-11-17T22:05:09Z Pro: model size in memory right after the refresh: None MB
```
