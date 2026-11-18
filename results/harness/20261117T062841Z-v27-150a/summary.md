# Harness run 20261117T062841Z-v27-150a

- Task: refresh
- Variant: v27-high-cardinality-visuals
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 8d1b63ba-18b6-447a-ae42-6cbd82e66229
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 747 MB, Power Query 677 MB, duration 2 min, CPU 157 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request 5a28cf93-9ade-488f-a2a3-448ee3e4bc25, 2026-11-17T06:29:38.857 to 2026-11-17T06:31:58.333, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v27-high-cardinality-visuals on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 747 MB vs 550 MB (+197 MB), Power Query 677 MB vs 270 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (24%); F16 5,120 MB: fits (15%); F32 10,240 MB: fits (7%); F64 25,600 MB: fits (3%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    c613573e-80fa-4597-8fae-8cbf73e69fa6 TabularSequencePoint        127.6     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        126.7    30.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        123.7    30.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        123.0    30.5 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         13.7    12.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         13.3    11.2       0
                                                                    <NA>               Commit          9.6     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.8     2.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          4.9     2.6       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          4.4     2.5  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.3     1.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          3.0     0.0       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 9b911546-bec3-4860-b3b6-4a830b14582f, 2026-11-17T06:33:04.98Z to 2026-11-17T06:33:55.753Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v27-high-cardinality-visuals on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T06:29:13Z run 20261117T062841Z-v27-150a: variant=v27-high-cardinality-visuals data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T06:29:18Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T06:29:22Z PPU: v27-high-cardinality-visuals is c613573e-80fa-4597-8fae-8cbf73e69fa6, DataTag reads back data-1m-v1
2026-11-17T06:29:22Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T06:29:23Z Pro: v27-high-cardinality-visuals is 747cf1df-8e4c-4923-80cf-8a35631068a1, DataTag reads back data-1m-v1
2026-11-17T06:29:35Z PPU: model size in memory before the refresh: 0.0 MB
2026-11-17T06:29:38Z PPU: trace started (full)
2026-11-17T06:29:39Z PPU: refresh started, request 5a28cf93-9ade-488f-a2a3-448ee3e4bc25
2026-11-17T06:32:19Z PPU: refresh refreshed (Completed) 
2026-11-17T06:32:50Z PPU: trace captured 282 events: ProgressReportEnd 237, ExecutionMetrics 34, CommandEnd 11
2026-11-17T06:32:51Z PPU: model size in memory right after the refresh: 92.7 MB
2026-11-17T06:33:04Z Pro: model size in memory before the refresh: None MB
2026-11-17T06:33:04Z Pro: standard refresh started
2026-11-17T06:34:05Z Pro: refresh refreshed (Completed) 
2026-11-17T06:34:05Z Pro: model size in memory right after the refresh: None MB
```
