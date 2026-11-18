# Harness run 20261117T075519Z-v32-2d5f

- Task: refresh
- Variant: v32-calc-columns-aggregate
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 0df5ae98-8273-4b9f-ab7e-48fa1e9884a9
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 928 MB, Power Query 895 MB, duration 1 min, CPU 141 s, rows 24,570,331, model 221 MB (Backup step in XMLA trace)
- Refresh request aaf8251c-5b40-4cef-9b7d-dceb5364679e, 2026-11-17T07:58:35.363 to 2026-11-17T08:00:12.703, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v32-calc-columns-aggregate on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 928 MB vs 550 MB (+378 MB), Power Query 895 MB vs 270 MB, model 221 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (30%); F16 5,120 MB: fits (18%); F32 10,240 MB: fits (9%); F64 25,600 MB: fits (4%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  6873b8a8-fea6-4828-b1a1-ee4b78ed0d69 TabularSequencePoint         78.6     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         70.5    24.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         67.2    23.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         66.8    23.9 2349091
                                                  <NA>               Commit         15.2     0.0    <NA>
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          8.4    10.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.1     8.1       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          7.5     0.1       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          7.4     0.0       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          7.3     0.0       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          7.3     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.7     2.2       0
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request d80b125d-bd40-4f8f-a28e-4f705ed704c8, 2026-11-17T08:01:02.31Z to 2026-11-17T08:02:18.83Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v32-calc-columns-aggregate on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T07:57:56Z run 20261117T075519Z-v32-2d5f: variant=v32-calc-columns-aggregate data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T07:58:02Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T07:58:05Z PPU: v32-calc-columns-aggregate is 6873b8a8-fea6-4828-b1a1-ee4b78ed0d69, DataTag reads back data-1m-v1
2026-11-17T07:58:05Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T07:58:06Z Pro: v32-calc-columns-aggregate is 2d29c913-d071-455f-bc94-f8955108bb1b, DataTag reads back data-1m-v1
2026-11-17T07:58:31Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-17T07:58:35Z PPU: trace started (full)
2026-11-17T07:58:35Z PPU: refresh started, request aaf8251c-5b40-4cef-9b7d-dceb5364679e
2026-11-17T08:00:16Z PPU: refresh refreshed (Completed) 
2026-11-17T08:00:46Z PPU: trace captured 390 events: ProgressReportEnd 345, ExecutionMetrics 34, CommandEnd 11
2026-11-17T08:00:47Z PPU: model size in memory right after the refresh: 367.9 MB
2026-11-17T08:01:01Z Pro: model size in memory before the refresh: None MB
2026-11-17T08:01:02Z Pro: standard refresh started
2026-11-17T08:02:32Z Pro: refresh refreshed (Completed) 
2026-11-17T08:02:32Z Pro: model size in memory right after the refresh: None MB
```
