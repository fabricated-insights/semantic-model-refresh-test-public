# Harness run 20261117T205356Z-v99g-13db

- Task: refresh
- Variant: v99g-sales-copy
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 5aee5b2f-6a4d-48a0-8cdb-a2ae722e9900
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 22,919 MB, Power Query 22,778 MB, duration 14 min, CPU 2,550 s, rows 38,422,496, model 536 MB (Backup step in XMLA trace)
- Refresh request a65b1ba9-a4a6-40b2-8f99-6dc488fc14c0, 2026-11-17T20:54:46.837 to 2026-11-17T21:08:36.937, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99g-sales-copy on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 22,919 MB vs 550 MB (+22,369 MB), Power Query 22,778 MB vs 270 MB, model 536 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (748%); F16 5,120 MB: OVER (448%); F32 10,240 MB: OVER (224%); F64 25,600 MB: fits (90%); PPU 102,400 MB: fits (22%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            0fc043ea-05ca-437e-b339-49dc7a786423 TabularSequencePoint        816.5     0.4       0
                           Sales Flat.Sales Flat       TabularRefresh        773.7    75.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        749.8    23.9       0
                           Sales Flat.Sales Flat           ExecuteSql        486.3     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        415.2    23.9       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        414.9    23.9 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        334.6     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        312.1     2.5       0
                           Sales Flat.Sales Flat              Process        287.3    75.7       0
                           Sales Flat.Sales Flat             ReadData        286.7    75.7 2349091
                   Customer Stats.Customer Stats           ExecuteSql        192.5     0.0       0
                   Customer Stats.Customer Stats              Process        119.6     2.5       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 17 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 527103ad-d00d-46f4-bff3-49605b3cc415, 2026-11-17T21:09:44.067Z to 2026-11-17T21:26:41.383Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99g-sales-copy on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T20:54:18Z run 20261117T205356Z-v99g-13db: variant=v99g-sales-copy data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T20:54:28Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T20:54:30Z PPU: v99g-sales-copy is 0fc043ea-05ca-437e-b339-49dc7a786423, DataTag reads back data-1m-v1
2026-11-17T20:54:30Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T20:54:32Z Pro: v99g-sales-copy is 365c91bc-922d-40fa-af7b-6ca43099dddb, DataTag reads back data-1m-v1
2026-11-17T20:54:43Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T20:54:46Z PPU: trace started (full)
2026-11-17T20:54:47Z PPU: refresh started, request a65b1ba9-a4a6-40b2-8f99-6dc488fc14c0
2026-11-17T21:08:59Z PPU: refresh refreshed (Completed) 
2026-11-17T21:09:30Z PPU: trace captured 844 events: ProgressReportEnd 799, ExecutionMetrics 34, CommandEnd 11
2026-11-17T21:09:31Z PPU: model size in memory right after the refresh: 662.8 MB
2026-11-17T21:09:43Z Pro: model size in memory before the refresh: None MB
2026-11-17T21:09:44Z Pro: standard refresh started
2026-11-17T21:26:46Z Pro: refresh refreshed (Completed) 
2026-11-17T21:26:46Z Pro: model size in memory right after the refresh: None MB
```
