# Harness run 20261118T131615Z-v29-6b36

- Task: refresh
- Variant: v29-keys-as-text
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: 54c10e65cedad3a4c9272b3a30d1cffba84949e7
- Notebook run: 940dac20-439f-4eec-89bb-b7a7a416f993
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 142 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request ee464d57-b8bc-49de-9004-6887b76d95c5, 2026-11-18T13:19:24.763 to 2026-11-18T13:20:43.913, workspace at 54c10e6, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v29-keys-as-text on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-18T13:18:51Z run 20261118T131615Z-v29-6b36: variant=v29-keys-as-text data_tag=data-1m-v1 targets=['F2'] expected_commit=54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:18:57Z F2: workspace already at 54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:19:00Z F2: v29-keys-as-text is eb86148d-c52d-4cf3-9274-8cadec698b9f, DataTag reads back data-1m-v1
2026-11-18T13:19:24Z F2: model size in memory before the refresh: 0.0 MB
2026-11-18T13:19:24Z F2: refresh started, request ee464d57-b8bc-49de-9004-6887b76d95c5
2026-11-18T13:21:05Z F2: refresh refreshed (Completed) 
2026-11-18T13:21:06Z F2: model size in memory right after the refresh: 141.9 MB
```
