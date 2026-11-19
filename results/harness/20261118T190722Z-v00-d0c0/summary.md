# Harness run 20261118T190722Z-v00-d0c0

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: 1a8dec43b5609c2396f109700e19df1e138cfac1
- Notebook run: 90244de1-301b-4a8a-adaf-07ce58d7ac31
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 93 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 64e90050-1a16-49e5-b649-6afd63c86a4c, 2026-11-18T19:10:06.773 to 2026-11-18T19:11:18.127, workspace at 1a8dec4, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v00-baseline on F2 data-1m-v1: refreshed, peak n/a (2026-11-13T10:00:30Z).
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 3,000 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-18T19:09:36Z run 20261118T190722Z-v00-d0c0: variant=v00-baseline data_tag=data-1m-v1 targets=['F2'] expected_commit=1a8dec43b5609c2396f109700e19df1e138cfac1
2026-11-18T19:09:42Z F2: workspace already at 1a8dec43b5609c2396f109700e19df1e138cfac1
2026-11-18T19:09:45Z F2: v00-baseline is d5bd2831-6c52-4bdd-a667-69f292f70ca4, DataTag reads back data-1m-v1
2026-11-18T19:10:06Z F2: model size in memory before the refresh: 66.2 MB
2026-11-18T19:10:07Z F2: refresh started, request 64e90050-1a16-49e5-b649-6afd63c86a4c
2026-11-18T19:11:47Z F2: refresh refreshed (Completed) 
2026-11-18T19:11:48Z F2: model size in memory right after the refresh: 92.7 MB
```
