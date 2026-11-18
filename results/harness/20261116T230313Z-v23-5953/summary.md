# Harness run 20261116T230313Z-v23-5953

- Task: refresh
- Variant: v23-dax-calc-tables
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: fb62f688-4563-430f-9fc0-f87c605e6b8b
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 1,405 MB, Power Query 666 MB, duration 1 min, CPU 141 s, rows 16,549,502, model 184 MB (Backup step in XMLA trace)
- Refresh request 324dd94a-b8ce-4fef-995a-97a2c0c0fff4, 2026-11-16T23:04:12.69 to 2026-11-16T23:05:41.947, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v23-dax-calc-tables on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 1,405 MB vs 550 MB (+855 MB), Power Query 666 MB vs 270 MB, model 184 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (46%); F16 5,120 MB: fits (27%); F32 10,240 MB: fits (14%); F64 25,600 MB: fits (5%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  316478cf-dbf2-484e-9234-3f1cb86faffd TabularSequencePoint         72.6     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         58.0    17.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         56.1    17.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         55.1    17.6 2349091
                                                  <NA>               Commit         13.4     0.0    <NA>
                                 Sales Copy.Sales Copy       TabularRefresh         13.3    11.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.0    12.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.8    10.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         10.1     1.7       0
                                 Sales Copy.Sales Copy              Process          9.5     9.4       0
                                 Sales Copy.Sales Copy             ReadData          9.2     9.2 2349091
                   Product Date Grid.Product Date Grid             VertiPaq          9.1     9.1       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request c977d8c5-271d-4d4b-81b3-dd7fdd8b6b01, 2026-11-16T23:06:37.817Z to 2026-11-16T23:07:40.62Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v23-dax-calc-tables on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-16T23:03:48Z run 20261116T230313Z-v23-5953: variant=v23-dax-calc-tables data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-16T23:03:53Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-16T23:03:55Z PPU: v23-dax-calc-tables is 316478cf-dbf2-484e-9234-3f1cb86faffd, DataTag reads back data-1m-v1
2026-11-16T23:03:55Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-16T23:03:56Z Pro: v23-dax-calc-tables is bba19b1a-80c0-4e0d-9deb-14134f1a4c29, DataTag reads back data-1m-v1
2026-11-16T23:04:09Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-16T23:04:12Z PPU: trace started (full)
2026-11-16T23:04:12Z PPU: refresh started, request 324dd94a-b8ce-4fef-995a-97a2c0c0fff4
2026-11-16T23:05:53Z PPU: refresh refreshed (Completed) 
2026-11-16T23:06:24Z PPU: trace captured 453 events: ProgressReportEnd 419, ExecutionMetrics 23, CommandEnd 11
2026-11-16T23:06:25Z PPU: model size in memory right after the refresh: 185.3 MB
2026-11-16T23:06:37Z Pro: model size in memory before the refresh: None MB
2026-11-16T23:06:37Z Pro: standard refresh started
2026-11-16T23:08:08Z Pro: refresh refreshed (Completed) 
2026-11-16T23:08:08Z Pro: model size in memory right after the refresh: None MB
```
