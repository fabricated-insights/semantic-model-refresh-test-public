# Harness run 20261118T124806Z-v24a-90b5

- Task: refresh
- Variant: v24a-second-fact
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: 54c10e65cedad3a4c9272b3a30d1cffba84949e7
- Notebook run: 0c820051-f7a7-4fe0-aca5-7a300461ad38
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 110 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 333ea6aa-da1a-4e07-8ad5-20e0c7287669, 2026-11-18T12:51:28.793 to 2026-11-18T12:52:42.367, workspace at 54c10e6, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v24a-second-fact on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-18T12:50:52Z run 20261118T124806Z-v24a-90b5: variant=v24a-second-fact data_tag=data-1m-v1 targets=['F2'] expected_commit=54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T12:51:02Z F2: workspace already at 54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T12:51:04Z F2: v24a-second-fact is 00e9cd53-9bde-4c52-b82c-ef14e342e946, DataTag reads back data-1m-v1
2026-11-18T12:51:28Z F2: model size in memory before the refresh: 0.0 MB
2026-11-18T12:51:28Z F2: refresh started, request 333ea6aa-da1a-4e07-8ad5-20e0c7287669
2026-11-18T12:53:09Z F2: refresh refreshed (Completed) 
2026-11-18T12:53:10Z F2: model size in memory right after the refresh: 110.0 MB
```
