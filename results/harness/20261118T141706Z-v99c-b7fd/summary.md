# Harness run 20261118T141706Z-v99c-b7fd

- Task: refresh
- Variant: v99c-crossjoin-only
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 54c10e65cedad3a4c9272b3a30d1cffba84949e7
- Notebook run: 79f51e43-8c48-4b1b-9867-cd5975b0c9a3
- Refresh parallelism requested: 6

## F64

- Result: **failed** (resource governance)
- Peak 25,592 MB, Power Query 25,518 MB, duration 3 min, CPU 529 s, rows 10,591,518, model 0 MB (Backup step in SemanticModelLogs)
- Refresh request dbb14d74-98dc-4e05-b742-b2f8b62d2377, 2026-11-18T14:18:05.937 to 2026-11-18T14:20:55.283, workspace at 54c10e6, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99c-crossjoin-only on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-13T20:33:20Z): peak 25,592 MB vs 602 MB (+24,990 MB), Power Query 25,518 MB vs 527 MB, model 0 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (835%); F16 5,120 MB: OVER (500%); F32 10,240 MB: OVER (250%); F64 25,600 MB: fits (100%); PPU 102,400 MB: fits (25%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25603 MB, memory limit 25592 MB, database size before command execution 7 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25603 MB, memory limit 25592 MB, database size before command execution 7 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25593 MB, memory limit 25592 MB, database size before command execution 7 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25603 MB, memory limit 25592 MB, database size before command execution 7 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory  MB, memory limit  MB, database size before command execution  MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
```

Steps running or failed when it stopped:

```
                                          Object      OperationDetailName                        Began Ended EndStatus
                   Customer Stats.Customer Stats           TabularRefresh 2026-11-18T14:18:09.3559928Z  None          
                           Sales Flat.Sales Flat           TabularRefresh 2026-11-18T14:18:09.3665892Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-18T14:18:09.3973966Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba               ExecuteSql 2026-11-18T14:18:09.5298482Z  None          
                           Sales Flat.Sales Flat               ExecuteSql 2026-11-18T14:18:09.5328842Z  None          
      Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-18T14:18:10.6995519Z  None          
                   Customer Stats.Customer Stats                  Process 2026-11-18T14:20:30.4828478Z  None          
                   Customer Stats.Customer Stats                 ReadData 2026-11-18T14:20:30.4832933Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec     Rows
                                           Customer Stats.Customer Stats          ExecuteSql        141.0     0.0        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh          8.2     1.0        0
                                     Product Date Grid.Product Date Grid            VertiPaq          5.8     5.8        0
                                     Product Date Grid.Product Date Grid             Process          4.7     4.3        0
                                     Product Date Grid.Product Date Grid      TabularRefresh          4.7     4.3        0
                                     Product Date Grid.Product Date Grid            ReadData          4.3     4.3 10113306
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          4.2     0.9        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          4.1     0.9   104990
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          3.9     0.0        0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          1.2     0.0        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.2     0.3        0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          1.0     0.0        0
```

**Screenshot: the refresh error of v99c-crossjoin-only on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99c-crossjoin-only-resource-governance.png**

## Log

```
2026-11-18T14:17:40Z run 20261118T141706Z-v99c-b7fd: variant=v99c-crossjoin-only data_tag=data-1m-v1 targets=['F64'] expected_commit=54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T14:17:47Z F64: workspace already at 54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T14:17:50Z F64: v99c-crossjoin-only is daa7e567-713a-45fb-9a38-cd372ab42dd8, DataTag reads back data-1m-v1
2026-11-18T14:18:05Z F64: model size in memory before the refresh: 0.1 MB
2026-11-18T14:18:06Z F64: refresh started, request dbb14d74-98dc-4e05-b742-b2f8b62d2377
2026-11-18T14:21:17Z F64: refresh failed (Failed) resource governance
2026-11-18T14:21:17Z F64: monitoring database Monitoring KQL database
2026-11-18T14:23:54Z F64: ExecutionMetrics event found
```
