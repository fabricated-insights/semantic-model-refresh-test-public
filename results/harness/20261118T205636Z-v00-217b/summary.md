# Harness run 20261118T205636Z-v00-217b

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: f223dfef873d39cf48b77eda7b75a0a8e5a91f74
- Notebook run: 5cc19af5-77e3-443d-9926-b6e5cf45012d
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 93 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 76a541f6-1e20-4c40-a12a-014290fc404c, 2026-11-18T21:03:43.473 to 2026-11-18T21:04:44.53, workspace at f223dfe, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v00-baseline on F2 data-1m-v1: refreshed, peak n/a (2026-11-18T19:11:47Z).
- Model size in memory when the full refresh started: 93 MB. The refresh may use the SKU maximum minus this: 2,973 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-18T20:56:59Z run 20261118T205636Z-v00-217b: variant=v00-baseline data_tag=data-1m-v1 targets=['F2'] expected_commit=f223dfef873d39cf48b77eda7b75a0a8e5a91f74
2026-11-18T20:57:04Z F2: update from Git 1a8dec43b5609c2396f109700e19df1e138cfac1 -> f223dfef873d39cf48b77eda7b75a0a8e5a91f74
2026-11-18T21:03:24Z F2: v00-baseline is d5bd2831-6c52-4bdd-a667-69f292f70ca4, DataTag reads back data-1m-v1
2026-11-18T21:03:43Z F2: model size in memory before the refresh: 92.7 MB
2026-11-18T21:03:43Z F2: refresh started, request 76a541f6-1e20-4c40-a12a-014290fc404c
2026-11-18T21:04:53Z F2: refresh refreshed (Completed) 
2026-11-18T21:04:55Z F2: model size in memory right after the refresh: 92.7 MB
```
