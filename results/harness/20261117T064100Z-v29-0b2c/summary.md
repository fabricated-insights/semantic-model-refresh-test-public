# Harness run 20261117T064100Z-v29-0b2c

- Task: refresh
- Variant: v29-keys-as-text
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: b72f9776-afc5-4d10-a36f-19f9b4f246a4
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 642 MB, Power Query 459 MB, duration 1 min, CPU 138 s, rows 2,561,140, model 69 MB (Backup step in XMLA trace)
- Refresh request 025de7ad-77c8-486a-a0f6-2be8e48b1b61, 2026-11-17T06:44:22.893 to 2026-11-17T06:45:56.577, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v29-keys-as-text on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 642 MB vs 550 MB (+92 MB), Power Query 459 MB vs 270 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (21%); F16 5,120 MB: fits (13%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (3%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  b73c5270-73fd-4a15-abcd-c363c7d08602 TabularSequencePoint         86.1     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         81.8    29.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         76.8    29.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         76.4    29.0 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          9.3     9.2       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.1     2.4       0
                                                  <NA>               Commit          5.3     0.0    <NA>
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          4.9     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          4.8     2.4       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          4.7     2.3  104990
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          4.1     0.1       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          3.8     0.0       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 8dc67e5c-477c-4e71-9968-e53c7e383e2b, 2026-11-17T06:46:49.017Z to 2026-11-17T06:47:31.393Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v29-keys-as-text on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T06:43:46Z run 20261117T064100Z-v29-0b2c: variant=v29-keys-as-text data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T06:43:52Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T06:43:55Z PPU: v29-keys-as-text is b73c5270-73fd-4a15-abcd-c363c7d08602, DataTag reads back data-1m-v1
2026-11-17T06:43:55Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T06:43:56Z Pro: v29-keys-as-text is ac88cedc-9084-411b-8388-2fd68c96a7ee, DataTag reads back data-1m-v1
2026-11-17T06:44:19Z PPU: model size in memory before the refresh: 0.0 MB
2026-11-17T06:44:22Z PPU: trace started (full)
2026-11-17T06:44:23Z PPU: refresh started, request 025de7ad-77c8-486a-a0f6-2be8e48b1b61
2026-11-17T06:46:03Z PPU: refresh refreshed (Completed) 
2026-11-17T06:46:34Z PPU: trace captured 279 events: ProgressReportEnd 234, ExecutionMetrics 34, CommandEnd 11
2026-11-17T06:46:34Z PPU: model size in memory right after the refresh: 141.9 MB
2026-11-17T06:46:48Z Pro: model size in memory before the refresh: None MB
2026-11-17T06:46:48Z Pro: standard refresh started
2026-11-17T06:47:49Z Pro: refresh refreshed (Completed) 
2026-11-17T06:47:49Z Pro: model size in memory right after the refresh: None MB
```
