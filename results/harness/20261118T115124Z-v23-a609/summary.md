# Harness run 20261118T115124Z-v23-a609

- Task: refresh
- Variant: v23-dax-calc-tables
- Data tag: data-10m-v1
- Targets: PPU, Pro
- Expected commit: 24e21d39b1452e2460142744f8aa9c637656719a
- Notebook run: 82552196-22d1-4393-ac30-c7b9452786d1
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 13,315 MB, Power Query 1,699 MB, duration 14 min, CPU 1,531 s, rows 75,922,895, model 1,833 MB (Backup step in XMLA trace)
- Refresh request cbe17bff-3daa-459d-8a98-5da1ab7c1564, 2026-11-18T11:54:21.793 to 2026-11-18T12:08:35.137, workspace at 24e21d3, DataTag read back data-10m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v23-dax-calc-tables on PPU data-10m-v1.
- Against v00-baseline on PPU data-10m-v1 (2026-11-18T11:14:13Z): peak 13,315 MB vs 1,834 MB (+11,481 MB), Power Query 1,699 MB vs 1,713 MB, model 1,833 MB vs 778 MB.
- Model size in memory when the full refresh started: 156 MB. The refresh may use the SKU maximum minus this: 102,244 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,910 MB: OVER (458%); F16 4,964 MB: OVER (268%); F32 10,084 MB: OVER (132%); F64 25,444 MB: fits (52%); PPU 102,244 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec     Rows
                  316478cf-dbf2-484e-9234-3f1cb86faffd TabularSequencePoint        810.0     2.1        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        629.6   196.2        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        623.2   196.2        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        618.8   196.2 23719935
                                 Sales Copy.Sales Copy       TabularRefresh        162.1   125.5        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData        160.3   171.6        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq        158.4   157.3        0
                                 Sales Copy.Sales Copy              Process        104.2   101.4        0
                           Sales Summary.Sales Summary       TabularRefresh        102.7    66.8        0
                                 Sales Copy.Sales Copy             ReadData        101.7   101.3 23719935
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         51.6    26.0        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process         48.7    26.0        0
```

## Pro

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 10 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 5fb54aa1-9602-498c-93c4-e23939e3b879, 2026-11-18T12:09:54.973Z to 2026-11-18T12:20:10.9Z, workspace at ?, DataTag read back data-10m-v1
- Numbers from: refresh API
- No earlier harness run of v23-dax-calc-tables on Pro data-10m-v1.
- No v00-baseline harness run with a measured peak on Pro data-10m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Unable to save the changes since the new dataset of size 1094 MB exceeds the limit of 1024 MB. If the dataset is hosted on a PowerBI Premium capacity, you may also reach out to your capacity administrator to see if the limit can be adjusted.
```

**Screenshot: the refresh error of v23-dax-calc-tables on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v23-dax-calc-tables-refresh-error.png**

## Log

```
2026-11-18T11:53:47Z run 20261118T115124Z-v23-a609: variant=v23-dax-calc-tables data_tag=data-10m-v1 targets=['PPU', 'Pro'] expected_commit=24e21d39b1452e2460142744f8aa9c637656719a
2026-11-18T11:53:56Z PPU: workspace already at 24e21d39b1452e2460142744f8aa9c637656719a
2026-11-18T11:53:58Z PPU: v23-dax-calc-tables is 316478cf-dbf2-484e-9234-3f1cb86faffd, DataTag reads back data-10m-v1
2026-11-18T11:53:58Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-18T11:53:59Z Pro: v23-dax-calc-tables is bba19b1a-80c0-4e0d-9deb-14134f1a4c29, DataTag reads back data-10m-v1
2026-11-18T11:54:18Z PPU: model size in memory before the refresh: 156.4 MB
2026-11-18T11:54:21Z PPU: trace started (full)
2026-11-18T11:54:21Z PPU: refresh started, request cbe17bff-3daa-459d-8a98-5da1ab7c1564
2026-11-18T12:09:05Z PPU: refresh refreshed (Completed) 
2026-11-18T12:09:36Z PPU: trace captured 1367 events: ProgressReportEnd 1333, ExecutionMetrics 23, CommandEnd 11
2026-11-18T12:09:38Z PPU: model size in memory right after the refresh: 1382.4 MB
2026-11-18T12:09:54Z Pro: model size in memory before the refresh: None MB
2026-11-18T12:09:54Z Pro: standard refresh started
2026-11-18T12:20:26Z Pro: refresh failed (Failed) other
```
