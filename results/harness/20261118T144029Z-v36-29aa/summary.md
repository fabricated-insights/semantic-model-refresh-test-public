# Harness run 20261118T144029Z-v36-29aa

- Task: refresh
- Variant: v36-calc-summary-month-grain
- Data tag: data-10m-v1
- Targets: F2
- Expected commit: 54c10e65cedad3a4c9272b3a30d1cffba84949e7
- Notebook run: 6afbdd2a-d63a-4764-a003-ee384d06ff8d
- Refresh parallelism requested: 6

## F2

- Result: **failed** (resource governance)
- Peak n/a, Power Query n/a, duration 11 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 358623b3-47f5-4429-b313-8eb8aa9b6655, 2026-11-18T14:43:34.65 to 2026-11-18T14:54:59.48, workspace at 54c10e6, DataTag read back data-10m-v1
- Numbers from: refresh API
- No earlier harness run of v36-calc-summary-month-grain on F2 data-10m-v1.
- No v00-baseline harness run with a measured peak on F2 data-10m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- Engine cancelled at 3,066 MB against a limit of 3,066 MB (database size before the command 5 MB).

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3066 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3066 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3066 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3066 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3122 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3068 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3067 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3066 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3066 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3066 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3066 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3122 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3068 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3066 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3068 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3066 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3066 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The current operation was cancelled because another operation in the transaction failed.
```

**Screenshot: the refresh error of v36-calc-summary-month-grain on F2 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f2-v36-calc-summary-month-grain-resource-governance.png**

## Log

```
2026-11-18T14:42:58Z run 20261118T144029Z-v36-29aa: variant=v36-calc-summary-month-grain data_tag=data-10m-v1 targets=['F2'] expected_commit=54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T14:43:08Z F2: workspace already at 54c10e65cedad3a4c9272b3a30d1cffba84949e7
2026-11-18T14:43:11Z F2: v36-calc-summary-month-grain is a4311446-46ea-4497-80a1-7a0e4a156699, DataTag reads back data-10m-v1
2026-11-18T14:43:34Z F2: model size in memory before the refresh: 0.1 MB
2026-11-18T14:43:34Z F2: refresh started, request 358623b3-47f5-4429-b313-8eb8aa9b6655
2026-11-18T14:55:17Z F2: refresh failed (Failed) resource governance
```
