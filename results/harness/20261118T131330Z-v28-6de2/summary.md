# Harness run 20261118T131330Z-v28-6de2

- Task: refresh
- Variant: v28-types-all-text
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: 54c10e65cedad3a4c9272b3a30d1cffba84949e7
- Notebook run: 6af13c26-7b66-4c9a-8547-7d6fbc646ce1
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 172 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 027ce358-1b96-4b9e-b059-3f3bfb3d0587, 2026-11-18T13:14:20.037 to 2026-11-18T13:15:28.103, workspace at 54c10e6, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v28-types-all-text on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-18T13:13:55Z run 20261118T131330Z-v28-6de2: variant=v28-types-all-text data_tag=data-1m-v1 targets=['F2'] expected_commit=54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:14:03Z F2: workspace already at 54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T13:14:06Z F2: v28-types-all-text is 527da1e4-4584-4e41-aae4-fc3fd0387f67, DataTag reads back data-1m-v1
2026-11-18T13:14:19Z F2: model size in memory before the refresh: 0.1 MB
2026-11-18T13:14:20Z F2: refresh started, request 027ce358-1b96-4b9e-b059-3f3bfb3d0587
2026-11-18T13:15:30Z F2: refresh refreshed (Completed) 
2026-11-18T13:15:31Z F2: model size in memory right after the refresh: 171.5 MB
```
