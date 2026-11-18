# Harness run 20261118T092223Z-v99i-b094

- Task: refresh
- Variant: v99i-buffer-stg-sales
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 45750ced-df3e-4d75-8611-e95a32d9ab83
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 25,651 MB, Power Query 25,492 MB, duration 34 min, CPU 6,764 s, rows 38,422,496, model 536 MB (Backup step in XMLA trace)
- Refresh request 9369c2ef-f316-459e-a3f3-445db302153e, 2026-11-18T09:25:34.147 to 2026-11-18T09:59:35.517, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99i-buffer-stg-sales on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 25,651 MB vs 550 MB (+25,101 MB), Power Query 25,492 MB vs 270 MB, model 536 MB vs 73 MB.
- Model size in memory when the full refresh started: 543 MB. The refresh may use the SKU maximum minus this: 101,857 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,523 MB: OVER (1017%); F16 4,577 MB: OVER (560%); F32 9,697 MB: OVER (265%); F64 25,057 MB: OVER (102%); PPU 101,857 MB: fits (25%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            c22581d6-175d-489e-b120-eb36a486ebd1 TabularSequencePoint       2026.4     0.7       0
                           Sales Flat.Sales Flat       TabularRefresh       1950.6    82.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1671.1    28.5       0
                           Sales Flat.Sales Flat           ExecuteSql       1064.1     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        943.0    28.4       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        942.7    28.4 2349091
                           Sales Flat.Sales Flat              Process        886.4    82.8       0
                           Sales Flat.Sales Flat             ReadData        885.9    82.7 2349091
                   Customer Stats.Customer Stats       TabularRefresh        764.2     3.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        728.0     0.0       0
                   Customer Stats.Customer Stats           ExecuteSql        469.7     0.0       0
                   Customer Stats.Customer Stats              Process        294.3     3.1       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 29 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 5ecf66b9-17b7-4375-8a80-464512113250, 2026-11-18T10:00:42.333Z to 2026-11-18T10:29:40.89Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99i-buffer-stg-sales on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-18T09:24:40Z run 20261118T092223Z-v99i-b094: variant=v99i-buffer-stg-sales data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-18T09:24:54Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-18T09:25:03Z PPU: v99i-buffer-stg-sales is c22581d6-175d-489e-b120-eb36a486ebd1, DataTag reads back data-1m-v1
2026-11-18T09:25:03Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-18T09:25:05Z Pro: v99i-buffer-stg-sales is 8b00d85b-e78a-4019-865c-26c24933f52c, DataTag reads back data-1m-v1
2026-11-18T09:25:30Z PPU: model size in memory before the refresh: 542.7 MB
2026-11-18T09:25:34Z PPU: trace started (full)
2026-11-18T09:25:36Z PPU: refresh started, request 9369c2ef-f316-459e-a3f3-445db302153e
2026-11-18T09:59:52Z PPU: refresh refreshed (Completed) 
2026-11-18T10:00:23Z PPU: trace captured 831 events: ProgressReportEnd 798, ExecutionMetrics 23, CommandEnd 10
2026-11-18T10:00:25Z PPU: model size in memory right after the refresh: 662.8 MB
2026-11-18T10:00:41Z Pro: model size in memory before the refresh: None MB
2026-11-18T10:00:42Z Pro: standard refresh started
2026-11-18T10:29:47Z Pro: refresh refreshed (Completed) 
2026-11-18T10:29:47Z Pro: model size in memory right after the refresh: None MB
```
