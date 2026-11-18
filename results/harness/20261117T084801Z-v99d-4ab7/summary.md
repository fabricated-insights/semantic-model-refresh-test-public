# Harness run 20261117T084801Z-v99d-4ab7

- Task: refresh
- Variant: v99d-power-query
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: eee855e8-319f-451e-b289-67e63ca3ef27
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 16,132 MB, Power Query 16,018 MB, duration 23 min, CPU 2,462 s, rows 22,085,043, model 185 MB (Backup step in XMLA trace)
- Refresh request 1d55f5c1-059c-4781-b3c1-93fc5e5f140b, 2026-11-17T08:50:51.727 to 2026-11-17T09:13:52.707, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99d-power-query on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 16,132 MB vs 550 MB (+15,582 MB), Power Query 16,018 MB vs 270 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (526%); F16 5,120 MB: OVER (315%); F32 10,240 MB: OVER (158%); F64 25,600 MB: fits (63%); PPU 102,400 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  2fb3d992-aae5-40d4-ac2d-710eb2f49931 TabularSequencePoint       1364.8     0.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1318.1    25.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        971.1    25.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        970.8    25.4 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        346.9     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        339.9     2.7       0
                         Customer Stats.Customer Stats           ExecuteSql        210.0     0.0       0
                         Customer Stats.Customer Stats              Process        129.9     2.6       0
                         Customer Stats.Customer Stats             ReadData        129.1     2.1  471482
                                                  <NA>               Commit         13.5     0.0    <NA>
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.8     9.1       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.5     1.8       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 50 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request b9c12564-6193-4254-bbc2-5556aad47f03, 2026-11-17T09:14:56.213Z to 2026-11-17T10:05:02.393Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99d-power-query on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T08:50:14Z run 20261117T084801Z-v99d-4ab7: variant=v99d-power-query data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T08:50:22Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T08:50:25Z PPU: v99d-power-query is 2fb3d992-aae5-40d4-ac2d-710eb2f49931, DataTag reads back data-1m-v1
2026-11-17T08:50:25Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T08:50:27Z Pro: v99d-power-query is 553edd0b-c792-40ee-876c-a6ffab6df3eb, DataTag reads back data-1m-v1
2026-11-17T08:50:48Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T08:50:51Z PPU: trace started (full)
2026-11-17T08:50:51Z PPU: refresh started, request 1d55f5c1-059c-4781-b3c1-93fc5e5f140b
2026-11-17T09:14:06Z PPU: refresh refreshed (Completed) 
2026-11-17T09:14:37Z PPU: trace captured 490 events: ProgressReportEnd 443, ExecutionMetrics 36, CommandEnd 11
2026-11-17T09:14:39Z PPU: model size in memory right after the refresh: 232.6 MB
2026-11-17T09:14:55Z Pro: model size in memory before the refresh: None MB
2026-11-17T09:14:56Z Pro: standard refresh started
2026-11-17T10:05:05Z Pro: refresh refreshed (Completed) 
2026-11-17T10:05:05Z Pro: model size in memory right after the refresh: None MB
```
