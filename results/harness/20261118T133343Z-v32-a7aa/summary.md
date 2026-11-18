# Harness run 20261118T133343Z-v32-a7aa

- Task: refresh
- Variant: v32-calc-columns-aggregate
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: 54c10e65cedad3a4c9272b3a30d1cffba84949e7
- Notebook run: c32365ef-78bf-49f5-bb31-d21ebc40fd36
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 2 min, CPU n/a, rows n/a, model 368 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 18488ae7-bbe4-4dfc-bef4-ed61b4aef5f5, 2026-11-18T13:36:44.663 to 2026-11-18T13:38:17.517, workspace at 54c10e6, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v32-calc-columns-aggregate on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-18T13:36:09Z run 20261118T133343Z-v32-a7aa: variant=v32-calc-columns-aggregate data_tag=data-1m-v1 targets=['F2'] expected_commit=54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:36:20Z F2: workspace already at 54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:36:22Z F2: v32-calc-columns-aggregate is 775d81dc-8a41-4f8d-aa5e-a88a0f85de57, DataTag reads back data-1m-v1
2026-11-18T13:36:44Z F2: model size in memory before the refresh: 0.1 MB
2026-11-18T13:36:44Z F2: refresh started, request 18488ae7-bbe4-4dfc-bef4-ed61b4aef5f5
2026-11-18T13:38:25Z F2: refresh refreshed (Completed) 
2026-11-18T13:38:26Z F2: model size in memory right after the refresh: 367.9 MB
```
