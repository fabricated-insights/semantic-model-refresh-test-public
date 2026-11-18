# Harness run 20261118T134245Z-v34-4404

- Task: refresh
- Variant: v34-auto-date-time-no-date-table
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: 54c10e65cedad3a4c9272b3a30d1cffba84949e7
- Notebook run: 1dd84e56-6840-41b3-964a-3134b96ccaf8
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 97 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 864d9814-3bad-4b95-b595-d6b1af43771d, 2026-11-18T13:45:33.36 to 2026-11-18T13:46:52.84, workspace at 54c10e6, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v34-auto-date-time-no-date-table on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-18T13:45:01Z run 20261118T134245Z-v34-4404: variant=v34-auto-date-time-no-date-table data_tag=data-1m-v1 targets=['F2'] expected_commit=54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:45:09Z F2: workspace already at 54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:45:11Z F2: v34-auto-date-time-no-date-table is 3a018001-17d2-4978-b22c-79cf3b55216c, DataTag reads back data-1m-v1
2026-11-18T13:45:32Z F2: model size in memory before the refresh: 0.1 MB
2026-11-18T13:45:33Z F2: refresh started, request 864d9814-3bad-4b95-b595-d6b1af43771d
2026-11-18T13:47:14Z F2: refresh refreshed (Completed) 
2026-11-18T13:47:15Z F2: model size in memory right after the refresh: 96.9 MB
```
