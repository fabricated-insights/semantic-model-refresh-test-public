# Harness run 20261117T142951Z-v31-a73e

- Task: refresh
- Variant: v31-calc-columns-row
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 66fa875f-5456-4562-a5d0-2f8287073c85
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 849 MB, Power Query 528 MB, duration 1 min, CPU 160 s, rows 77,732,052, model 223 MB (Backup step in XMLA trace)
- Refresh request 2508f55a-246b-4ab6-8696-6299d4207a51, 2026-11-17T14:31:04.433 to 2026-11-17T14:32:37.497, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v31-calc-columns-row on PPU data-1m-v1: refreshed, peak 977 MB (2026-11-17T07:01:08Z).
  - Peak change: -128 MB (-13.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 849 MB vs 550 MB (+299 MB), Power Query 528 MB vs 270 MB, model 223 MB vs 73 MB.
- Model size in memory when the full refresh started: 234 MB. The refresh may use the SKU maximum minus this: 102,166 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,832 MB: fits (30%); F16 4,886 MB: fits (17%); F32 10,006 MB: fits (8%); F64 25,366 MB: fits (3%); PPU 102,166 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    ac3ebe29-9abb-4067-9007-e7d601187a3c TabularSequencePoint         79.1     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         58.5    24.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         55.5    24.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         54.8    23.9 2349091
                                                    Sales.Order Line Key       TabularRefresh         14.2     4.3       0
                                                                    <NA>               Commit         12.3     0.0    <NA>
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.2    14.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          9.9     9.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.2     1.8       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          4.6     0.5       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          3.8     0.0       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          3.2     0.1       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 23a1efa6-f852-4588-a759-355ac771c7b9, 2026-11-17T14:33:29.683Z to 2026-11-17T14:34:39.737Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v31-calc-columns-row on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T07:02:55Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T14:30:19Z run 20261117T142951Z-v31-a73e: variant=v31-calc-columns-row data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T14:30:39Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T14:30:45Z PPU: v31-calc-columns-row is ac3ebe29-9abb-4067-9007-e7d601187a3c, DataTag reads back data-1m-v1
2026-11-17T14:30:45Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T14:30:46Z Pro: v31-calc-columns-row is 9294e5ca-efe7-40c2-be3f-9ea4bb8bf562, DataTag reads back data-1m-v1
2026-11-17T14:31:00Z PPU: model size in memory before the refresh: 233.5 MB
2026-11-17T14:31:04Z PPU: trace started (full)
2026-11-17T14:31:04Z PPU: refresh started, request 2508f55a-246b-4ab6-8696-6299d4207a51
2026-11-17T14:32:45Z PPU: refresh refreshed (Completed) 
2026-11-17T14:33:15Z PPU: trace captured 416 events: ProgressReportEnd 396, ExecutionMetrics 10, CommandEnd 10
2026-11-17T14:33:16Z PPU: model size in memory right after the refresh: 316.8 MB
2026-11-17T14:33:29Z Pro: model size in memory before the refresh: None MB
2026-11-17T14:33:29Z Pro: standard refresh started
2026-11-17T14:34:59Z Pro: refresh refreshed (Completed) 
2026-11-17T14:34:59Z Pro: model size in memory right after the refresh: None MB
```
