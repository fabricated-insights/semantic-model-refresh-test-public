# Harness run 20261118T125940Z-v25-47af

- Task: refresh
- Variant: v25-many-to-many
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: 54c10e65cedad3a4c9272b3a30d1cffba84949e7
- Notebook run: 9666a227-3e17-480b-b7b3-c56dd9e26f2e
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 2 min, CPU n/a, rows n/a, model 98 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 50644f18-a860-4f4e-bd1f-57bf7203aa4b, 2026-11-18T13:02:48.897 to 2026-11-18T13:04:39.08, workspace at 54c10e6, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v25-many-to-many on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-18T13:02:11Z run 20261118T125940Z-v25-47af: variant=v25-many-to-many data_tag=data-1m-v1 targets=['F2'] expected_commit=54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:02:22Z F2: workspace already at 54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:02:26Z F2: v25-many-to-many is 482ccae8-be74-482a-9196-84137a9ecb4a, DataTag reads back data-1m-v1
2026-11-18T13:02:48Z F2: model size in memory before the refresh: 0.0 MB
2026-11-18T13:02:49Z F2: refresh started, request 50644f18-a860-4f4e-bd1f-57bf7203aa4b
2026-11-18T13:04:59Z F2: refresh refreshed (Completed) 
2026-11-18T13:05:01Z F2: model size in memory right after the refresh: 98.1 MB
```
