# Harness run 20261118T123936Z-v24-800c

- Task: refresh
- Variant: v24-bidirectional
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: 54c10e65cedad3a4c9272b3a30d1cffba84949e7
- Notebook run: 0986fe03-d463-40c7-8db9-fd1d4e8d2999
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 2 min, CPU n/a, rows n/a, model 93 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 3a14899b-f8c5-4807-8c18-30f614d9b39a, 2026-11-18T12:43:06.477 to 2026-11-18T12:45:04.603, workspace at 54c10e6, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v24-bidirectional on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-18T12:41:50Z run 20261118T123936Z-v24-800c: variant=v24-bidirectional data_tag=data-1m-v1 targets=['F2'] expected_commit=54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T12:41:59Z F2: update from Git 11b19b5ae786173223c42ae0ed7f0e2cc4488bfb -> 54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T12:42:42Z F2: v24-bidirectional is cdbee253-9936-4702-b957-38fbad3272fa, DataTag reads back data-1m-v1
2026-11-18T12:43:06Z F2: model size in memory before the refresh: 0.0 MB
2026-11-18T12:43:06Z F2: refresh started, request 3a14899b-f8c5-4807-8c18-30f614d9b39a
2026-11-18T12:45:17Z F2: refresh refreshed (Completed) 
2026-11-18T12:45:18Z F2: model size in memory right after the refresh: 92.7 MB
```
