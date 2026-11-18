# Harness run 20261117T062400Z-v26-f152

- Task: refresh
- Variant: v26-bad-dax
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: efa3a571-8911-4cb1-9753-b3fec8228a24
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 614 MB, Power Query 402 MB, duration 1 min, CPU 106 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request 4d220974-064e-442c-b8a6-4c12d98e3abb, 2026-11-17T06:24:46.237 to 2026-11-17T06:25:54.927, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v26-bad-dax on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 614 MB vs 550 MB (+64 MB), Power Query 402 MB vs 270 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (20%); F16 5,120 MB: fits (12%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    2ee61d67-d165-40e2-b3c1-d06e2a600c8e TabularSequencePoint         62.7     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         62.0    20.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         59.5    20.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         58.8    19.9 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.6    12.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.4    11.3       0
                                                                    <NA>               Commit          4.9     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.8     2.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.7     2.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.6     1.9  104990
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.3     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.3     0.6       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 0412b4b5-f351-4b60-96ef-8a72b057eb65, 2026-11-17T06:26:32.03Z to 2026-11-17T06:27:18.783Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v26-bad-dax on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T06:24:22Z run 20261117T062400Z-v26-f152: variant=v26-bad-dax data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T06:24:28Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T06:24:30Z PPU: v26-bad-dax is 2ee61d67-d165-40e2-b3c1-d06e2a600c8e, DataTag reads back data-1m-v1
2026-11-17T06:24:30Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T06:24:31Z Pro: v26-bad-dax is fd7a0114-741d-460c-8d6e-3c5c90d18558, DataTag reads back data-1m-v1
2026-11-17T06:24:42Z PPU: model size in memory before the refresh: 0.0 MB
2026-11-17T06:24:46Z PPU: trace started (full)
2026-11-17T06:24:46Z PPU: refresh started, request 4d220974-064e-442c-b8a6-4c12d98e3abb
2026-11-17T06:25:56Z PPU: refresh refreshed (Completed) 
2026-11-17T06:26:27Z PPU: trace captured 282 events: ProgressReportEnd 237, ExecutionMetrics 34, CommandEnd 11
2026-11-17T06:26:28Z PPU: model size in memory right after the refresh: 92.7 MB
2026-11-17T06:26:31Z Pro: model size in memory before the refresh: None MB
2026-11-17T06:26:31Z Pro: standard refresh started
2026-11-17T06:27:32Z Pro: refresh refreshed (Completed) 
2026-11-17T06:27:32Z Pro: model size in memory right after the refresh: None MB
```
