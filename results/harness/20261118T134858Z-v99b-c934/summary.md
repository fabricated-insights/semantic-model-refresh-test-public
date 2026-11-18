# Harness run 20261118T134858Z-v99b-c934

- Task: refresh
- Variant: v99b-one-sales-copy
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 54c10e65cedad3a4c9272b3a30d1cffba84949e7
- Notebook run: 1b541bf5-25b8-410a-ab85-7a5b8e52c91b
- Refresh parallelism requested: 6

## F64

- Result: **failed** (resource governance)
- Peak 25,592 MB, Power Query 25,524 MB, duration 5 min, CPU 1,110 s, rows 478,212, model 0 MB (Backup step in SemanticModelLogs)
- Refresh request aa9dd464-ddbc-4292-b044-60f8886b4aa4, 2026-11-18T13:52:37.7 to 2026-11-18T13:57:58.46, workspace at 54c10e6, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99b-one-sales-copy on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-13T20:33:20Z): peak 25,592 MB vs 602 MB (+24,990 MB), Power Query 25,524 MB vs 527 MB, model 0 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (835%); F16 5,120 MB: OVER (500%); F32 10,240 MB: OVER (250%); F64 25,600 MB: fits (100%); PPU 102,400 MB: fits (25%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25594 MB, memory limit 25592 MB, database size before command execution 7 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
The operation was canceled.. The exception was raised by the IDbCommand interface.
```

Steps running or failed when it stopped:

```
                                          Object      OperationDetailName                        Began Ended EndStatus
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-18T13:52:40.3775491Z  None          
                           Sales Flat.Sales Flat           TabularRefresh  2026-11-18T13:52:40.391705Z  None          
                   Customer Stats.Customer Stats           TabularRefresh 2026-11-18T13:52:40.4054805Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba               ExecuteSql 2026-11-18T13:52:40.5077899Z  None          
                           Sales Flat.Sales Flat               ExecuteSql 2026-11-18T13:52:40.5171562Z  None          
      Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-18T13:52:44.0084227Z  None          
                   Customer Stats.Customer Stats                  Process 2026-11-18T13:56:51.7739182Z  None          
                   Customer Stats.Customer Stats                 ReadData 2026-11-18T13:56:51.7748546Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec   Rows
                                           Customer Stats.Customer Stats          ExecuteSql        251.3     0.0      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh         14.1     1.7      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          7.1     0.0      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          6.8     1.6      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          6.7     1.6 104990
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          2.7     0.1      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          2.5     0.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          1.5     0.2      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.4     0.6      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          1.0     0.0      0
                                                                                      Commit          1.0     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          0.9     0.6      0
```

**Screenshot: the refresh error of v99b-one-sales-copy on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99b-one-sales-copy-resource-governance.png**

## Log

```
2026-11-18T13:51:58Z run 20261118T134858Z-v99b-c934: variant=v99b-one-sales-copy data_tag=data-1m-v1 targets=['F64'] expected_commit=54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:52:07Z F64: workspace already at 54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:52:12Z F64: v99b-one-sales-copy is 1fe6d06d-415b-469f-9bfa-d9105a1aa0a2, DataTag reads back data-1m-v1
2026-11-18T13:52:37Z F64: model size in memory before the refresh: 0.1 MB
2026-11-18T13:52:37Z F64: refresh started, request aa9dd464-ddbc-4292-b044-60f8886b4aa4
2026-11-18T13:58:19Z F64: refresh failed (Failed) resource governance
2026-11-18T13:58:19Z F64: monitoring database Monitoring KQL database
2026-11-18T14:00:56Z F64: ExecutionMetrics event found
```
