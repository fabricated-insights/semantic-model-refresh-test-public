# Harness run 20261118T132207Z-v30-7c49

- Task: refresh
- Variant: v30-double-instead-of-fixed
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: 54c10e65cedad3a4c9272b3a30d1cffba84949e7
- Notebook run: fd0f2b78-2171-49d0-97da-4ed5f1f1335c
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 93 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request ef61ee7b-7204-47b0-b6f3-9628be1f7bb0, 2026-11-18T13:25:17.99 to 2026-11-18T13:26:16.783, workspace at 54c10e6, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v30-double-instead-of-fixed on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-18T13:24:42Z run 20261118T132207Z-v30-7c49: variant=v30-double-instead-of-fixed data_tag=data-1m-v1 targets=['F2'] expected_commit=54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:24:52Z F2: workspace already at 54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:24:54Z F2: v30-double-instead-of-fixed is e71e9c1f-9d96-4a79-af3c-f3d7d43f5d66, DataTag reads back data-1m-v1
2026-11-18T13:25:17Z F2: model size in memory before the refresh: 0.0 MB
2026-11-18T13:25:18Z F2: refresh started, request ef61ee7b-7204-47b0-b6f3-9628be1f7bb0
2026-11-18T13:26:28Z F2: refresh refreshed (Completed) 
2026-11-18T13:26:29Z F2: model size in memory right after the refresh: 92.9 MB
```
