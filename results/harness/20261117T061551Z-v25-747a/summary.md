# Harness run 20261117T061551Z-v25-747a

- Task: refresh
- Variant: v25-many-to-many
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 393081ae-ffe2-4283-bf56-053bc1c3f25c
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 695 MB, Power Query 578 MB, duration 1 min, CPU 133 s, rows 3,611,040, model 79 MB (Backup step in XMLA trace)
- Refresh request 0b9624ed-8394-4121-b9d3-237d12170902, 2026-11-17T06:18:51.517 to 2026-11-17T06:20:17.347, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v25-many-to-many on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 695 MB vs 550 MB (+145 MB), Power Query 578 MB vs 270 MB, model 79 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (23%); F16 5,120 MB: fits (14%); F32 10,240 MB: fits (7%); F64 25,600 MB: fits (3%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    8e5f1fe2-bf93-4150-9f31-c99850c8b58c TabularSequencePoint         77.0     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         76.2    22.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         71.8    21.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         70.6    21.8 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         13.1    14.5       0
  Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637       TabularRefresh         13.0     5.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         12.9    12.9       0
  Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637              Process          9.8     5.1       0
  Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637             ReadData          9.5     4.9 1049900
                                                                    <NA>               Commit          6.1     0.0    <NA>
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          4.3     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          4.2     0.8       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 7aa3cd90-4a0a-4ef9-961e-776153328e45, 2026-11-17T06:21:17.103Z to 2026-11-17T06:22:19.013Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v25-many-to-many on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T06:18:18Z run 20261117T061551Z-v25-747a: variant=v25-many-to-many data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T06:18:25Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T06:18:27Z PPU: v25-many-to-many is 8e5f1fe2-bf93-4150-9f31-c99850c8b58c, DataTag reads back data-1m-v1
2026-11-17T06:18:27Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T06:18:29Z Pro: v25-many-to-many is 61112feb-5659-4f15-b98d-a38763ac31b2, DataTag reads back data-1m-v1
2026-11-17T06:18:47Z PPU: model size in memory before the refresh: 0.0 MB
2026-11-17T06:18:51Z PPU: trace started (full)
2026-11-17T06:18:51Z PPU: refresh started, request 0b9624ed-8394-4121-b9d3-237d12170902
2026-11-17T06:20:32Z PPU: refresh refreshed (Completed) 
2026-11-17T06:21:03Z PPU: trace captured 296 events: ProgressReportEnd 251, ExecutionMetrics 34, CommandEnd 11
2026-11-17T06:21:03Z PPU: model size in memory right after the refresh: 98.1 MB
2026-11-17T06:21:16Z Pro: model size in memory before the refresh: None MB
2026-11-17T06:21:17Z Pro: standard refresh started
2026-11-17T06:22:47Z Pro: refresh refreshed (Completed) 
2026-11-17T06:22:47Z Pro: model size in memory right after the refresh: None MB
```
