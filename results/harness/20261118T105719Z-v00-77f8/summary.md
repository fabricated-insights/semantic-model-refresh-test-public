# Harness run 20261118T105719Z-v00-77f8

- Task: refresh
- Variant: v00-baseline
- Data tag: data-10m-v1
- Targets: PPU, Pro
- Expected commit: 24e21d39b1452e2460142744f8aa9c637656719a
- Notebook run: 771b352c-d05f-4b1f-9b2a-31dfd90f453b
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 1,834 MB, Power Query 1,713 MB, duration 14 min, CPU 1,311 s, rows 25,506,840, model 778 MB (Backup step in XMLA trace)
- Refresh request 38feeb69-bace-4e90-94ea-1243e2a55fa9, 2026-11-18T10:59:27.86 to 2026-11-18T11:13:33.777, workspace at 24e21d3, DataTag read back data-10m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v00-baseline on PPU data-10m-v1.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (61%); F16 5,054 MB: fits (36%); F32 10,174 MB: fits (18%); F64 25,534 MB: fits (7%); PPU 102,334 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec     Rows
                  0eee6936-1906-41cc-ae01-289b0589e4e1 TabularSequencePoint        822.5     0.1        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        813.1   248.8        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        803.1   248.7        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        799.9   248.7 23719935
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData        151.8   162.4        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq        149.3   147.4        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         60.6    32.8        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process         55.5    32.8        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData         50.3    32.2  1679846
                                                  <NA>               Commit         20.8     0.0     <NA>
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba      CompressSegment         11.9    19.7        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          9.9     0.0        0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 8 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 03a799a0-a5d5-4286-82c6-e0160ab467df, 2026-11-18T11:14:29.147Z to 2026-11-18T11:22:52.53Z, workspace at ?, DataTag read back data-10m-v1
- Numbers from: refresh API
- No earlier harness run of v00-baseline on Pro data-10m-v1.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-18T10:57:57Z run 20261118T105719Z-v00-77f8: variant=v00-baseline data_tag=data-10m-v1 targets=['PPU', 'Pro'] expected_commit=24e21d39b1452e2460142744f8aa9c637656719a
2026-11-18T10:58:07Z PPU: update from Git 082095c0494b089e8303c0f6733826318c965814 -> 24e21d39b1452e2460142744f8aa9c637656719a
2026-11-18T10:59:07Z PPU: v00-baseline is 0eee6936-1906-41cc-ae01-289b0589e4e1, DataTag reads back data-10m-v1
2026-11-18T10:59:07Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-18T10:59:09Z Pro: v00-baseline is d617fd07-8a52-4fda-ab69-2b58d0426997, DataTag reads back data-10m-v1
2026-11-18T10:59:24Z PPU: model size in memory before the refresh: 66.2 MB
2026-11-18T10:59:27Z PPU: trace started (full)
2026-11-18T10:59:28Z PPU: refresh started, request 38feeb69-bace-4e90-94ea-1243e2a55fa9
2026-11-18T11:13:42Z PPU: refresh refreshed (Completed) 
2026-11-18T11:14:13Z PPU: trace captured 589 events: ProgressReportEnd 556, ExecutionMetrics 22, CommandEnd 11
2026-11-18T11:14:15Z PPU: model size in memory right after the refresh: 700.0 MB
2026-11-18T11:14:28Z Pro: model size in memory before the refresh: None MB
2026-11-18T11:14:29Z Pro: standard refresh started
2026-11-18T11:23:00Z Pro: refresh refreshed (Completed) 
2026-11-18T11:23:00Z Pro: model size in memory right after the refresh: None MB
```
