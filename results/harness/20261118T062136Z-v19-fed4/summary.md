# Harness run 20261118T062136Z-v19-fed4

- Task: refresh
- Variant: v19-pq-heavy-10m
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 13b51688-ea33-483c-a537-e85f0f938f40
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (M evaluation memory limit)
- Peak 24,123 MB, Power Query 24,005 MB, duration 23 min, CPU 6,717 s, rows 2,563,048, model 0 MB (Backup step in XMLA trace)
- Refresh request ea33bc44-7b7a-4909-a2f5-18a82b65babd, 2026-11-18T06:22:53.563 to 2026-11-18T06:45:48.773, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v19-pq-heavy-10m on PPU data-1m-v1: failed, peak 22,186 MB (2026-11-13T10:48:06Z).
  - Peak change: +1,937 MB (+8.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 24,123 MB vs 550 MB (+23,573 MB), Power Query 24,005 MB vs 270 MB, model 0 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (787%); F16 5,120 MB: OVER (471%); F32 10,240 MB: OVER (236%); F64 25,600 MB: fits (94%); PPU 102,400 MB: fits (24%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
The M evaluation exceeded the memory limit. To address the issue consider optimizing the M expressions, reducing the concurrency of operations that are memory intensive or upgrading to increase the available memory. Container exited unexpectedly with code 0x0000DEAD. PID: 17816.
Used features: (none).;Container exited unexpectedly with code 0x0000DEAD. PID: 17816.
Used features: (none).
Container exited unexpectedly with code 0x0000DEAD. PID: 17816.
Used features: (none).
Container exited unexpectedly with code 0x0000DEAD. PID: 17816..
The operation was canceled.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec    Rows
                                         PQ Basket Pairs.PQ Basket Pairs      TabularRefresh       1314.9     0.0       0
                                         PQ Basket Pairs.PQ Basket Pairs          ExecuteSql       1314.8     0.0       0
                               PQ Customer Segments.PQ Customer Segments      TabularRefresh        939.6     0.1       0
                               PQ Customer Segments.PQ Customer Segments          ExecuteSql        939.4     0.0       0
                         PQ Top Products by Year.PQ Top Products by Year      TabularRefresh        168.6     0.0       0
                         PQ Top Products by Year.PQ Top Products by Year          ExecuteSql        168.5     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba      TabularRefresh         98.3    23.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             Process         97.3    23.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba            ReadData         96.8    23.5 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba   AnalyzeEncodeData         13.8    15.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba            VertiPaq         13.5    13.5       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          4.2     0.6       0
```

**Screenshot: the refresh error of v19-pq-heavy-10m on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v19-pq-heavy-10m-m-evaluation-memory.png**

## Pro

- Result: **failed** (M evaluation memory limit), after 202 min. The harness stopped polling at 2 h and recorded polltimeout; the outcome was read from the refresh history afterwards: status Failed, 06:46:50 to 10:09:19 UTC, "The M evaluation exceeded the memory limit ... Container exited unexpectedly with code 0x0000DEAD."
- Peak n/a, Power Query n/a, duration n/a, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 9c80c852-fd87-4758-a8c3-892ca20d4730, 2026-11-18T06:46:50.627Z to , workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v19-pq-heavy-10m on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

**Screenshot: the refresh error of v19-pq-heavy-10m on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v19-pq-heavy-10m-refresh-error.png**

## Log

```
2026-11-18T06:22:16Z run 20261118T062136Z-v19-fed4: variant=v19-pq-heavy-10m data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-18T06:22:27Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-18T06:22:32Z PPU: v19-pq-heavy-10m is 393784af-1418-40f1-a51d-7c01c12a2326, DataTag reads back data-1m-v1
2026-11-18T06:22:32Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-18T06:22:33Z Pro: v19-pq-heavy-10m is 453cdf86-f54d-4cb6-b14d-ac68bf7cf1ba, DataTag reads back data-1m-v1
2026-11-18T06:22:50Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-18T06:22:53Z PPU: trace started (full)
2026-11-18T06:22:53Z PPU: refresh started, request ea33bc44-7b7a-4909-a2f5-18a82b65babd
2026-11-18T06:46:07Z PPU: refresh failed (Failed) M evaluation memory limit
2026-11-18T06:46:38Z PPU: trace captured 346 events: ProgressReportEnd 290, ExecutionMetrics 40, CommandEnd 11, Error 5
2026-11-18T06:46:50Z Pro: model size in memory before the refresh: None MB
2026-11-18T06:46:50Z Pro: standard refresh started
2026-11-18T08:47:13Z Pro: refresh polltimeout (PollTimeout) other
```
