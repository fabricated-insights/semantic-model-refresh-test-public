# Harness run 20261117T093046Z-v35-f6d2

- Task: refresh
- Variant: v35-calc-tables-four-copies
- Data tag: data-10m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 0be30294-18d9-4474-b596-b5bd2a91b912
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 9,737 MB, Power Query 1,754 MB, duration 28 min, CPU 2,642 s, rows 147,082,700, model 3,281 MB (Backup step in XMLA trace)
- Refresh request 37b4eb1c-4d4d-4475-8e5b-62b6c97c1a84, 2026-11-17T09:33:26.533 to 2026-11-17T10:03:47.643, workspace at 082095c, DataTag read back data-10m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v35-calc-tables-four-copies on PPU data-10m-v1.
- No v00-baseline harness run with a measured peak on PPU data-10m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (318%); F16 5,120 MB: OVER (190%); F32 10,240 MB: fits (95%); F64 25,600 MB: fits (38%); PPU 102,400 MB: fits (10%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec     Rows
            90c2816c-fbb9-4514-ac64-d4da369fe384 TabularSequencePoint       1701.5     0.3        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        841.3   261.4        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        826.0   261.3        0
                           Sales Copy.Sales Copy       TabularRefresh        821.2   710.4        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        821.2   261.3 23719935
                           Sales Copy.Sales Copy              Process        741.6   677.3        0
                           Sales Copy.Sales Copy             ReadData        725.0   677.1 94879740
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData        160.4   169.2        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq        158.0   153.7        0
                     Sales Summary.Sales Summary       TabularRefresh        156.3   101.2        0
                                            <NA>               Commit        116.3     0.0     <NA>
                           Sales Copy.Sales Copy    AnalyzeEncodeData        112.3   169.9        0
```

## Pro

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 14 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 81a14f08-9f77-4b51-b13e-1f07e305eba5, 2026-11-17T10:05:06.093Z to 2026-11-17T10:19:00.947Z, workspace at ?, DataTag read back data-10m-v1
- Numbers from: refresh API
- No earlier harness run of v35-calc-tables-four-copies on Pro data-10m-v1.
- No v00-baseline harness run with a measured peak on Pro data-10m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Unable to save the changes since the new dataset of size 2192 MB exceeds the limit of 1024 MB. If the dataset is hosted on a PowerBI Premium capacity, you may also reach out to your capacity administrator to see if the limit can be adjusted.
```

**Screenshot: the refresh error of v35-calc-tables-four-copies on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v35-calc-tables-four-copies-refresh-error.png**

## Log

```
2026-11-17T09:32:51Z run 20261117T093046Z-v35-f6d2: variant=v35-calc-tables-four-copies data_tag=data-10m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T09:33:00Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T09:33:03Z PPU: v35-calc-tables-four-copies is 90c2816c-fbb9-4514-ac64-d4da369fe384, DataTag reads back data-10m-v1
2026-11-17T09:33:03Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T09:33:04Z Pro: v35-calc-tables-four-copies is efd608fe-a1a6-4cac-9fa4-0d7057cd6624, DataTag reads back data-10m-v1
2026-11-17T09:33:22Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T09:33:26Z PPU: trace started (full)
2026-11-17T09:33:26Z PPU: refresh started, request 37b4eb1c-4d4d-4475-8e5b-62b6c97c1a84
2026-11-17T10:04:12Z PPU: refresh refreshed (Completed) 
2026-11-17T10:04:44Z PPU: trace captured 2944 events: ProgressReportEnd 2897, ExecutionMetrics 36, CommandEnd 11
2026-11-17T10:04:46Z PPU: model size in memory right after the refresh: 2829.4 MB
2026-11-17T10:05:05Z Pro: model size in memory before the refresh: None MB
2026-11-17T10:05:06Z Pro: standard refresh started
2026-11-17T10:19:09Z Pro: refresh failed (Failed) other
```
