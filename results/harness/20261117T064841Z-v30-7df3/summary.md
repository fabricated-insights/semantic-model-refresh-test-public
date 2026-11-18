# Harness run 20261117T064841Z-v30-7df3

- Task: refresh
- Variant: v30-double-instead-of-fixed
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 48084eb9-5fca-443c-a03c-b504f03219a6
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 607 MB, Power Query 529 MB, duration 1 min, CPU 96 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request 0288d19b-b5d5-4113-984d-20c97d5a27f7, 2026-11-17T06:51:25.51 to 2026-11-17T06:52:27.777, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v30-double-instead-of-fixed on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 607 MB vs 550 MB (+57 MB), Power Query 529 MB vs 270 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (20%); F16 5,120 MB: fits (12%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  9e47cacd-824d-4e24-8998-6f639088fddf TabularSequencePoint         53.3     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         52.6    19.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         49.4    19.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         49.0    18.9 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          9.1    10.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.9     8.9       0
                                                  <NA>               Commit          6.1     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.9     1.8       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          4.0     0.1       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          3.9     0.0       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          3.9     0.0       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          3.8     0.0       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 7ee2ee46-e404-48a4-bed1-f0dadf2fc1c2, 2026-11-17T06:53:11.957Z to 2026-11-17T06:53:53.253Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v30-double-instead-of-fixed on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T06:50:52Z run 20261117T064841Z-v30-7df3: variant=v30-double-instead-of-fixed data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T06:51:00Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T06:51:02Z PPU: v30-double-instead-of-fixed is 9e47cacd-824d-4e24-8998-6f639088fddf, DataTag reads back data-1m-v1
2026-11-17T06:51:02Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T06:51:03Z Pro: v30-double-instead-of-fixed is f5ade11e-0d70-4124-9864-769370fc626d, DataTag reads back data-1m-v1
2026-11-17T06:51:21Z PPU: model size in memory before the refresh: 0.0 MB
2026-11-17T06:51:25Z PPU: trace started (full)
2026-11-17T06:51:25Z PPU: refresh started, request 0288d19b-b5d5-4113-984d-20c97d5a27f7
2026-11-17T06:52:35Z PPU: refresh refreshed (Completed) 
2026-11-17T06:53:06Z PPU: trace captured 282 events: ProgressReportEnd 237, ExecutionMetrics 34, CommandEnd 11
2026-11-17T06:53:07Z PPU: model size in memory right after the refresh: 92.9 MB
2026-11-17T06:53:11Z Pro: model size in memory before the refresh: None MB
2026-11-17T06:53:11Z Pro: standard refresh started
2026-11-17T06:54:12Z Pro: refresh refreshed (Completed) 
2026-11-17T06:54:12Z Pro: model size in memory right after the refresh: None MB
```
