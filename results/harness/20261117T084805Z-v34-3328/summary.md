# Harness run 20261117T084805Z-v34-3328

- Task: refresh
- Variant: v34-auto-date-time-no-date-table
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: a3390fc6-92b8-4696-92a4-898fe5636ce4
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 620 MB, Power Query 523 MB, duration 1 min, CPU 109 s, rows 2,847,496, model 74 MB (Backup step in XMLA trace)
- Refresh request b91858c9-a039-44be-bf2f-ac8cbf3c5709, 2026-11-17T08:50:58.307 to 2026-11-17T08:52:10.56, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v34-auto-date-time-no-date-table on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 620 MB vs 550 MB (+70 MB), Power Query 523 MB vs 270 MB, model 74 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (20%); F16 5,120 MB: fits (12%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  7023f118-b5f8-4a7b-9811-b16c34d32708 TabularSequencePoint         63.5     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         62.7    19.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         60.1    19.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         59.1    19.6 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.2    12.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.0    11.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.4     2.2       0
                                                  <NA>               Commit          5.3     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.2     2.2       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          3.1     2.1  104990
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.4     0.0       0
        Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          2.3     0.1       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 95ba6b74-3d75-4609-a1a0-325e7eef06f2, 2026-11-17T08:53:16.613Z to 2026-11-17T08:54:15.74Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v34-auto-date-time-no-date-table on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T08:50:21Z run 20261117T084805Z-v34-3328: variant=v34-auto-date-time-no-date-table data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T08:50:27Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T08:50:30Z PPU: v34-auto-date-time-no-date-table is 7023f118-b5f8-4a7b-9811-b16c34d32708, DataTag reads back data-1m-v1
2026-11-17T08:50:30Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T08:50:31Z Pro: v34-auto-date-time-no-date-table is e7b5d152-c532-43e2-9408-761272f88a1c, DataTag reads back data-1m-v1
2026-11-17T08:50:54Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T08:50:58Z PPU: trace started (full)
2026-11-17T08:50:58Z PPU: refresh started, request b91858c9-a039-44be-bf2f-ac8cbf3c5709
2026-11-17T08:52:38Z PPU: refresh refreshed (Completed) 
2026-11-17T08:53:09Z PPU: trace captured 449 events: ProgressReportEnd 404, ExecutionMetrics 34, CommandEnd 11
2026-11-17T08:53:10Z PPU: model size in memory right after the refresh: 96.9 MB
2026-11-17T08:53:16Z Pro: model size in memory before the refresh: None MB
2026-11-17T08:53:16Z Pro: standard refresh started
2026-11-17T08:54:16Z Pro: refresh refreshed (Completed) 
2026-11-17T08:54:16Z Pro: model size in memory right after the refresh: None MB
```
