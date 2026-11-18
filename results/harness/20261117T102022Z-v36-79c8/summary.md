# Harness run 20261117T102022Z-v36-79c8

- Task: refresh
- Variant: v36-calc-summary-month-grain
- Data tag: data-10m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: c070472a-7221-4dc1-b7b8-9d18ceeadcdc
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 14,929 MB, Power Query 1,723 MB, duration 16 min, CPU 1,759 s, rows 78,870,826, model 1,827 MB (Backup step in XMLA trace)
- Refresh request 60248e3c-2e4d-487d-9522-b4b1c83117bb, 2026-11-17T10:23:23.503 to 2026-11-17T10:40:30.15, workspace at 082095c, DataTag read back data-10m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v36-calc-summary-month-grain on PPU data-10m-v1.
- No v00-baseline harness run with a measured peak on PPU data-10m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (487%); F16 5,120 MB: OVER (292%); F32 10,240 MB: OVER (146%); F64 25,600 MB: fits (58%); PPU 102,400 MB: fits (15%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec     Rows
                  12b658b6-453c-4047-85fa-3e02aebcdc2e TabularSequencePoint        969.3     2.4        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        720.8   239.8        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        712.3   239.8        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        708.5   239.8 23719935
                                 Sales Copy.Sales Copy       TabularRefresh        229.2   152.7        0
                           Sales Summary.Sales Summary       TabularRefresh        167.8   105.3        0
                                 Sales Copy.Sales Copy              Process        155.7   124.6        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData        154.7   165.9        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq        152.4   150.2        0
                                 Sales Copy.Sales Copy             ReadData        126.7   124.5 23719935
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         58.7    34.2        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process         54.7    34.1        0
```

## Pro

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 11 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request c833e3ba-caff-4671-a7f2-97248f779583, 2026-11-17T10:41:25.1Z to 2026-11-17T10:52:27.017Z, workspace at ?, DataTag read back data-10m-v1
- Numbers from: refresh API
- No earlier harness run of v36-calc-summary-month-grain on Pro data-10m-v1.
- No v00-baseline harness run with a measured peak on Pro data-10m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Unable to save the changes since the new dataset of size 1099 MB exceeds the limit of 1024 MB. If the dataset is hosted on a PowerBI Premium capacity, you may also reach out to your capacity administrator to see if the limit can be adjusted.
```

**Screenshot: the refresh error of v36-calc-summary-month-grain on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v36-calc-summary-month-grain-refresh-error.png**

## Log

```
2026-11-17T10:22:46Z run 20261117T102022Z-v36-79c8: variant=v36-calc-summary-month-grain data_tag=data-10m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T10:22:54Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T10:22:57Z PPU: v36-calc-summary-month-grain is 12b658b6-453c-4047-85fa-3e02aebcdc2e, DataTag reads back data-10m-v1
2026-11-17T10:22:57Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T10:22:58Z Pro: v36-calc-summary-month-grain is a8869fbf-57b2-47cc-b053-c1fc95363f49, DataTag reads back data-10m-v1
2026-11-17T10:23:19Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T10:23:23Z PPU: trace started (full)
2026-11-17T10:23:23Z PPU: refresh started, request 60248e3c-2e4d-487d-9522-b4b1c83117bb
2026-11-17T10:40:37Z PPU: refresh refreshed (Completed) 
2026-11-17T10:41:08Z PPU: trace captured 1405 events: ProgressReportEnd 1360, ExecutionMetrics 34, CommandEnd 11
2026-11-17T10:41:11Z PPU: model size in memory right after the refresh: 1408.2 MB
2026-11-17T10:41:24Z Pro: model size in memory before the refresh: None MB
2026-11-17T10:41:25Z Pro: standard refresh started
2026-11-17T10:52:27Z Pro: refresh failed (Failed) other
```
