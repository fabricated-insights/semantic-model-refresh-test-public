# Harness run 20261118T130813Z-v27-85ba

- Task: refresh
- Variant: v27-high-cardinality-visuals
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: 54c10e65cedad3a4c9272b3a30d1cffba84949e7
- Notebook run: b16f4b46-bc4f-416d-8b40-625d870540a0
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 93 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 63ed0d51-6b23-4f09-9d95-3ebfc24fa175, 2026-11-18T13:11:18.28 to 2026-11-18T13:12:43.34, workspace at 54c10e6, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v27-high-cardinality-visuals on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-18T13:10:47Z run 20261118T130813Z-v27-85ba: variant=v27-high-cardinality-visuals data_tag=data-1m-v1 targets=['F2'] expected_commit=54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:10:53Z F2: workspace already at 54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:10:56Z F2: v27-high-cardinality-visuals is d131c50b-c0d3-4117-869e-232e7514754a, DataTag reads back data-1m-v1
2026-11-18T13:11:18Z F2: model size in memory before the refresh: 0.0 MB
2026-11-18T13:11:18Z F2: refresh started, request 63ed0d51-6b23-4f09-9d95-3ebfc24fa175
2026-11-18T13:12:59Z F2: refresh refreshed (Completed) 
2026-11-18T13:13:00Z F2: model size in memory right after the refresh: 92.7 MB
```
