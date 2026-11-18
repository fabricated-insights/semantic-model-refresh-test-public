# Harness run 20261117T091313Z-v21-add0

- Task: refresh
- Variant: v21-pq-group-by
- Data tag: data-1m-v1
- Targets: PPU, Pro
- Expected commit: a62fd5ad7f13dc668a8ef240bbc1320736b13b05
- Notebook run: 591bb934-71cc-452d-882e-952abe81e0f9
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 3,582 MB, Power Query 3,338 MB, duration 2 min, CPU 216 s, rows 3,032,622, model 84 MB (Backup step in XMLA trace)
- Refresh request ee6cd53d-2109-4c5a-93fe-89ec1aef9a08, 2026-11-17T09:16:06.75 to 2026-11-17T09:17:53.583, workspace at 082095c, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v21-pq-group-by on PPU data-1m-v1.
- Against v00-baseline on PPU data-1m-v1 (2026-11-16T22:53:34Z): peak 3,582 MB vs 550 MB (+3,032 MB), Power Query 3,338 MB vs 270 MB, model 84 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (117%); F16 5,120 MB: fits (70%); F32 10,240 MB: fits (35%); F64 25,600 MB: fits (14%); PPU 102,400 MB: fits (3%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            b551b92f-7694-4efc-9e6f-4c13eaec6dcf TabularSequencePoint         98.3     0.1       0
                   Customer Stats.Customer Stats       TabularRefresh         95.1     2.6       0
                   Customer Stats.Customer Stats           ExecuteSql         83.9     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         70.9    20.9       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         63.0    20.9       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         62.4    20.7 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         12.3    13.7       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         12.2    12.1       0
                   Customer Stats.Customer Stats              Process         11.2     2.5       0
                   Customer Stats.Customer Stats             ReadData         10.5     2.0  471482
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          7.8     0.0       0
                                            <NA>               Commit          5.7     0.0    <NA>
```

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 2 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 08ee05ba-8744-4f37-9f0d-d71166ccfd52, 2026-11-17T09:19:01.463Z to 2026-11-17T09:20:42.153Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v21-pq-group-by on Pro data-1m-v1.
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-17T09:15:28Z run 20261117T091313Z-v21-add0: variant=v21-pq-group-by data_tag=data-1m-v1 targets=['PPU', 'Pro'] expected_commit=a62fd5ad7f13dc668a8ef240bbc1320736b13b05
2026-11-17T09:15:37Z PPU: workspace at 082095c0494b089e8303c0f6733826318c965814, remote a62fd5ad7f13dc668a8ef240bbc1320736b13b05 has no changes for its items; no update needed
2026-11-17T09:15:41Z PPU: v21-pq-group-by is b551b92f-7694-4efc-9e6f-4c13eaec6dcf, DataTag reads back data-1m-v1
2026-11-17T09:15:41Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-17T09:15:42Z Pro: v21-pq-group-by is 70ddbd03-fc62-414e-86c4-ca217ba22a7c, DataTag reads back data-1m-v1
2026-11-17T09:16:03Z PPU: model size in memory before the refresh: 0.0 MB
2026-11-17T09:16:06Z PPU: trace started (full)
2026-11-17T09:16:06Z PPU: refresh started, request ee6cd53d-2109-4c5a-93fe-89ec1aef9a08
2026-11-17T09:18:17Z PPU: refresh refreshed (Completed) 
2026-11-17T09:18:48Z PPU: trace captured 300 events: ProgressReportEnd 255, ExecutionMetrics 34, CommandEnd 11
2026-11-17T09:18:49Z PPU: model size in memory right after the refresh: 118.6 MB
2026-11-17T09:19:01Z Pro: model size in memory before the refresh: None MB
2026-11-17T09:19:01Z Pro: standard refresh started
2026-11-17T09:21:01Z Pro: refresh refreshed (Completed) 
2026-11-17T09:21:01Z Pro: model size in memory right after the refresh: None MB
```
