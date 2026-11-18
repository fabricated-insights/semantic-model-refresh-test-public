# Harness run 20261118T132724Z-v31-549c

- Task: refresh
- Variant: v31-calc-columns-row
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: 54c10e65cedad3a4c9272b3a30d1cffba84949e7
- Notebook run: d01bcf36-2874-4c15-a929-0f8104a8af3c
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 2 min, CPU n/a, rows n/a, model 317 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 2b8343e3-0a41-4f56-bbbf-2fe7143a7861, 2026-11-18T13:30:35.943 to 2026-11-18T13:32:44.693, workspace at 54c10e6, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v31-calc-columns-row on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-18T13:29:59Z run 20261118T132724Z-v31-549c: variant=v31-calc-columns-row data_tag=data-1m-v1 targets=['F2'] expected_commit=54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:30:08Z F2: workspace already at 54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:30:12Z F2: v31-calc-columns-row is a58404cc-fc6f-49b8-acb7-d6337e669dd6, DataTag reads back data-1m-v1
2026-11-18T13:30:35Z F2: model size in memory before the refresh: 0.1 MB
2026-11-18T13:30:36Z F2: refresh started, request 2b8343e3-0a41-4f56-bbbf-2fe7143a7861
2026-11-18T13:32:46Z F2: refresh refreshed (Completed) 
2026-11-18T13:32:48Z F2: model size in memory right after the refresh: 316.8 MB
```
