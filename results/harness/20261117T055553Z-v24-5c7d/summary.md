# Harness run 20261117T055553Z-v24-5c7d

- Task: refresh
- Variant: v24-bidirectional
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: b8a9cbdb-5fc1-4012-ab3b-57732759cb80
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 551 MB, Power Query 460 MB, duration 1 min, CPU 96 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request 70754945-ade9-440f-abfa-3afa93eeb853, 2026-11-17T05:56:54.953 to 2026-11-17T05:57:58.397, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v24-bidirectional on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 551 MB vs 550 MB (+1 MB), Power Query 460 MB vs 270 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (18%); F16 5,120 MB: fits (11%); F32 10,240 MB: fits (5%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    396b5678-cec7-4bcd-98dc-b22a8c270567 TabularSequencePoint         55.2     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         54.5    18.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         51.7    18.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         51.3    18.2 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          9.1    10.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.9     9.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.1     1.8       0
                                                                    <NA>               Commit          4.4     0.0    <NA>
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          4.0     0.1       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.7     0.6       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b           ExecuteSql          3.7     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          2.9     0.0       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 4fd25c3c-8bbb-4c84-a641-00381b274129, 2026-11-17T05:58:40.777Z to 2026-11-17T05:59:27.46Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v24-bidirectional on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T05:56:29Z run 20261117T055553Z-v24-5c7d: variant=v24-bidirectional data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T05:56:34Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T05:56:37Z PPU: v24-bidirectional is 396b5678-cec7-4bcd-98dc-b22a8c270567, DataTag reads back data-1m-v1
2026-11-17T05:56:37Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T05:56:39Z Pro: v24-bidirectional is 2ffad2da-054f-4e22-a193-a672b0711d93, DataTag reads back data-1m-v1
2026-11-17T05:56:51Z PPU: model size in memory before the refresh: 0.0 MB
2026-11-17T05:56:54Z PPU: trace started (full)
2026-11-17T05:56:55Z PPU: refresh started, request 70754945-ade9-440f-abfa-3afa93eeb853
2026-11-17T05:58:05Z PPU: refresh refreshed (Completed) 
2026-11-17T05:58:36Z PPU: trace captured 286 events: ProgressReportEnd 237, ExecutionMetrics 37, CommandEnd 12
2026-11-17T05:58:36Z PPU: model size in memory right after the refresh: 92.7 MB
2026-11-17T05:58:40Z Pro: model size in memory before the refresh: None MB
2026-11-17T05:58:40Z Pro: standard refresh started
2026-11-17T05:59:40Z Pro: refresh refreshed (Completed) 
2026-11-17T05:59:40Z Pro: model size in memory right after the refresh: None MB
```
