# Harness run 20261116T225204Z-v99k-aeca

- Task: refresh
- Variant: v99k-no-buffers
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 73564ddc-59c7-4ae4-9ae3-245b66031979
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 13,038 MB, Power Query 12,936 MB, duration 31 min, CPU 3,111 s, rows 22,085,043, model 185 MB (Backup step in XMLA trace)
- Refresh request 60e48466-555e-4810-afde-9d43dce7318d, 2026-11-16T22:54:53.07 to 2026-11-16T23:26:09.987, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99k-no-buffers on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 13,038 MB vs 550 MB (+12,488 MB), Power Query 12,936 MB vs 270 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (425%); F16 5,120 MB: OVER (255%); F32 10,240 MB: OVER (127%); F64 25,600 MB: fits (51%); PPU 102,400 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  036d4881-e715-4a7c-9782-be79275ef5ac TabularSequencePoint       1862.6     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1851.0    27.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process       1499.8    27.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData       1499.5    27.3 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        351.1     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        296.2     2.5       0
                         Customer Stats.Customer Stats           ExecuteSql        162.3     0.0       0
                         Customer Stats.Customer Stats              Process        133.8     2.5       0
                         Customer Stats.Customer Stats             ReadData        133.2     2.0  471482
                                                  <NA>               Commit         13.0     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.5     1.8       0
                                Sales.Sales Line Label       TabularRefresh          6.6     6.4       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 16 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 78ac8a50-224a-4d18-a6fc-9494dd84a33a, 2026-11-16T23:27:25.967Z to 2026-11-16T23:43:30.487Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99k-no-buffers on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-16T22:54:18Z run 20261116T225204Z-v99k-aeca: variant=v99k-no-buffers data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-16T22:54:25Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-16T22:54:28Z PPU: v99k-no-buffers is 036d4881-e715-4a7c-9782-be79275ef5ac, DataTag reads back data-1m-v1
2026-11-16T22:54:28Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-16T22:54:29Z Pro: v99k-no-buffers is 6d087e69-54e7-429e-93c1-4264a5d3b2e7, DataTag reads back data-1m-v1
2026-11-16T22:54:49Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-16T22:54:52Z PPU: trace started (full)
2026-11-16T22:54:53Z PPU: refresh started, request 60e48466-555e-4810-afde-9d43dce7318d
2026-11-16T23:26:38Z PPU: refresh refreshed (Completed) 
2026-11-16T23:27:08Z PPU: trace captured 478 events: ProgressReportEnd 443, ExecutionMetrics 24, CommandEnd 11
2026-11-16T23:27:10Z PPU: model size in memory right after the refresh: 232.6 MB
2026-11-16T23:27:25Z Pro: model size in memory before the refresh: None MB
2026-11-16T23:27:25Z Pro: standard refresh started
2026-11-16T23:43:58Z Pro: refresh refreshed (Completed) 
2026-11-16T23:43:58Z Pro: model size in memory right after the refresh: None MB
```
