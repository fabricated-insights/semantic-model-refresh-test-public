# Harness run 20261118T125350Z-v24b-9767

- Task: refresh
- Variant: v24b-second-fact-bidirectional
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: 54c10e65cedad3a4c9272b3a30d1cffba84949e7
- Notebook run: 560de254-ffdd-4f09-89a0-a5f7330ea780
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 110 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 41f60a76-30e4-468e-bfa5-6a2393ec2486, 2026-11-18T12:56:47.337 to 2026-11-18T12:58:09.34, workspace at 54c10e6, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v24b-second-fact-bidirectional on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-18T12:56:15Z run 20261118T125350Z-v24b-9767: variant=v24b-second-fact-bidirectional data_tag=data-1m-v1 targets=['F2'] expected_commit=54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T12:56:24Z F2: workspace already at 54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T12:56:27Z F2: v24b-second-fact-bidirectional is 256381b6-5aae-4faa-bb41-efc1cb01273a, DataTag reads back data-1m-v1
2026-11-18T12:56:47Z F2: model size in memory before the refresh: 0.0 MB
2026-11-18T12:56:47Z F2: refresh started, request 41f60a76-30e4-468e-bfa5-6a2393ec2486
2026-11-18T12:58:28Z F2: refresh refreshed (Completed) 
2026-11-18T12:58:29Z F2: model size in memory right after the refresh: 110.0 MB
```
