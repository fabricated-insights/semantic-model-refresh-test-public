# Harness run 20261118T133930Z-v33-dd29

- Task: refresh
- Variant: v33-auto-date-time
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: 54c10e65cedad3a4c9272b3a30d1cffba84949e7
- Notebook run: 84d2502a-420d-4def-a54c-27ca595203aa
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 96 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request dedc5101-9d15-4b8f-a3d7-c8b79d481077, 2026-11-18T13:40:27.713 to 2026-11-18T13:41:56.167, workspace at 54c10e6, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v33-auto-date-time on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-18T13:40:03Z run 20261118T133930Z-v33-dd29: variant=v33-auto-date-time data_tag=data-1m-v1 targets=['F2'] expected_commit=54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:40:10Z F2: workspace already at 54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:40:12Z F2: v33-auto-date-time is 30e0e36a-643f-49ab-82af-1f8214be1ba6, DataTag reads back data-1m-v1
2026-11-18T13:40:27Z F2: model size in memory before the refresh: 0.1 MB
2026-11-18T13:40:27Z F2: refresh started, request dedc5101-9d15-4b8f-a3d7-c8b79d481077
2026-11-18T13:42:08Z F2: refresh refreshed (Completed) 
2026-11-18T13:42:09Z F2: model size in memory right after the refresh: 96.2 MB
```
