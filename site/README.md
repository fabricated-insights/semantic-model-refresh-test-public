# Compare two semantic models

A static page that compares two models from the lab: refresh memory, Power Query part, duration, CPU, the four sizes, which capacities they fit on, and report query time and memory. Published with GitHub Pages by `.github/workflows/pages.yml` on every push to `main` that touches `site/`, `results/`, `models/*/README.md` or `docs/lab-findings*.md`.

| File | What it is |
|---|---|
| `index.html`, `app.js`, `style.css` | The page. No framework, no build step. Charts are inline SVG. |
| `models.yaml` | Display metadata per model: name, category, description, data sizes, notes. Also the preset chips, the caveats and the article links. The only hand-written file. |
| `build_data.py` | Reads `results/*.csv` and `docs/lab-findings.md` and writes `data.json`, plus an inline copy of it in `index.html`. |
| `data.json` | Generated. Never edit it by hand. |

## Run it locally

```
pip install pyyaml
python site/build_data.py
```

Then open `site/index.html` in a browser. Opened from the file system it reads the inline copy of the data; served over HTTP it reads `data.json`:

```
python -m http.server -d site 8000
```

and go to http://localhost:8000/?a=v00@1M&b=v20@1M.

The build prints a `note:` line for anything worth checking: a peak in `lab-findings.md` that is not in the CSVs, a model in `lab-findings.md` that is not on the site, a result text that disagrees with the runs. The output only changes when the data does, so commit `data.json` and `index.html` together after a rebuild.

## Add a model

1. Run it with the harness, so its refreshes are in `results/harness-runs.csv` (and its query runs in `results/query-*.csv`).
2. Add its row to the "All runs" table in `docs/lab-findings.md`, with the sizes and the F2 result.
3. Add an entry under `models:` in `site/models.yaml`:

   ```yaml
   - id: v37
     folder: v37-my-change          # folder under models/
     name: My change
     category: Model design         # one of the categories at the top
     desc: Baseline plus one thing. One or two short sentences.
     sizes: [1M]                    # 1M and/or 10M orders
     qnote: Optional note under the query charts.
   ```

4. Run `python site/build_data.py` and check the `note:` lines.

## Where the numbers come from

- **Refresh peak, Power Query part, duration, CPU:** F64 runs from `harness-runs.csv` and `monitoring-refreshes.csv`. Every completed run counts; the page shows the highest, the median and the range. Power Query part, duration and CPU are from the latest run. A failed refresh has no peak; the page shows its result text.
- **Premium Per User:** harness runs with capacity `PPU`. Shown separately, never mixed into F64 numbers.
- **10M runs in `monitoring-refreshes.csv`:** that file has no data tag. A completed refresh that loaded at least 4 times the rows of the same model's smallest completed refresh counts as 10M (v00 and v23 on 2026-11-06).
- **Sizes:** service size from the `Backup` step of the latest completed run, in memory from the harness DAX query (`INFO.STORAGETABLECOLUMNSEGMENTS`), both falling back to `lab-findings.md`. The downloaded .pbix size is only in `lab-findings.md`.
- **F2 and F64 result texts:** `lab-findings.md`.
- **Queries:** `query-summary.csv`, F64, page p20, cold cache, all visuals at once. Runs where at least half of the queries failed (a model without data) are left out. Heaviest single query is the highest peak per query in that mode on any page, plus the XMLA runs. F2 failures are counted from `query-runs.csv`; the two matrices always fail over the REST API and are not counted.
- **Limits:** F2 to F8 3,066 MB, F16 5,120 MB, F32 10,240 MB, F64 25,600 MB, Premium Per User 102,400 MB per model; F2 1,024 MB per query. All MB are 1,048,576 bytes.
