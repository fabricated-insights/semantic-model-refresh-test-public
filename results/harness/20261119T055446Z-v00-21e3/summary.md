# Harness run 20261119T055446Z-v00-21e3

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: 331791b5ff71d5ca6193d149c439b53eaa125c11
- Notebook run: 6e0b91cb-d110-4aa2-bab6-8e732bcad5d2
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 550 MB, Power Query 456 MB, duration 1 min, CPU 108 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request 1580f17e-8c3e-410d-899e-4c0bd69602af, 2026-11-19T05:55:57.407 to 2026-11-19T05:57:09.597, workspace at 331791b, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v00-baseline on PPU data-1m-v1: refreshed, peak 550 MB (2026-11-16T22:53:34Z).
  - Peak change: +0 MB (+0.0%).
- Model size in memory when the full refresh started: 626 MB. The refresh may use the SKU maximum minus this: 101,774 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,440 MB: fits (23%); F16 4,494 MB: fits (12%); F32 9,614 MB: fits (6%); F64 24,974 MB: fits (2%); PPU 101,774 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    0eee6936-1906-41cc-ae01-289b0589e4e1 TabularSequencePoint         62.9     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         62.2    18.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         59.5    18.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         55.3    18.5 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         15.9    17.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         15.7    15.7       0
                                                                    <NA>               Commit          6.2     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.2     2.1       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.1     0.6       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.8     2.1       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.7     2.0  104990
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.6     0.0       0
```

## Log

```
2026-11-19T05:55:31Z run 20261119T055446Z-v00-21e3: variant=v00-baseline data_tag=data-1m-v1 targets=['PPU'] expected_commit=331791b5ff71d5ca6193d149c439b53eaa125c11
2026-11-19T05:55:37Z PPU: workspace already at 331791b5ff71d5ca6193d149c439b53eaa125c11
2026-11-19T05:55:39Z PPU: v00-baseline is 0eee6936-1906-41cc-ae01-289b0589e4e1, DataTag reads back data-1m-v1
2026-11-19T05:55:53Z PPU: model size in memory before the refresh: 625.7 MB
2026-11-19T05:55:57Z PPU: trace started (full)
2026-11-19T05:55:57Z PPU: refresh started, request 1580f17e-8c3e-410d-899e-4c0bd69602af
2026-11-19T05:57:37Z PPU: refresh refreshed (Completed) 
2026-11-19T05:58:08Z PPU: trace captured 281 events: ProgressReportEnd 237, ExecutionMetrics 33, CommandEnd 11
2026-11-19T05:58:09Z PPU: model size in memory right after the refresh: 92.7 MB
```
