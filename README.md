# Semantic model refresh and query lab

How the design of a Power BI semantic model affects refresh memory, query cost and what fits on a Fabric capacity. Every number in this repo comes from a measured run on Fabric F2, F64 or Premium Per User in November 2026; nothing is estimated.

## Start here

| File | What it covers |
|---|---|
| [docs/lab-findings.md](docs/lab-findings.md) | Refresh memory: what costs memory during a refresh, what fails on F2 and F64, Power Query against the model, the limits and what the error messages mean. Includes a table of every model with its peak, model size and result. |
| [docs/lab-findings-queries.md](docs/lab-findings-queries.md) | Report queries: time, CPU and memory per query, the 1 GB per-query limit on F2, bad DAX, relationships, high-cardinality visuals, capacity load and throttling. |
| `models/<model>/README.md` | One per model: what changed, why, and its measured results. |
| [Compare two models](https://fabricated-insights.github.io/semantic-model-refresh-test-public/) | Pick two models and compare refresh memory, sizes, which capacities they fit on, and query cost. Built from this repo by [site/](site/). |

## How the lab works

- **Data**: Contoso, a synthetic retail dataset, as Parquet files. `data-1m-v1` has 2.35M sales rows, `data-10m-v1` 23.7M. The models load them from the GitHub releases of [vlpatkosdani/semantic-model-refresh-test](https://github.com/vlpatkosdani/semantic-model-refresh-test) with `Web.Contents`; the `DataTag` parameter picks the release. A profile of the 1M data is in [docs/data-1m-profile.md](docs/data-1m-profile.md).
- **Models**: `v00-baseline` is a clean star schema (Sales, Customer, Product, Store, Date, Currency Exchange). Every other model is the baseline plus one change, so each result can be read against the baseline: Power Query steps (v18 to v21), calculated columns and tables (v22, v23, v31, v32, v35, v36), relationships (v24, v25), bad DAX (v26), high-cardinality visuals (v27), data types (v28 to v30) and Auto date/time (v33, v34). `v99-kitchen-sink` combines many antipatterns; v99a to v99q take it apart to find what makes it fail.
- **Format**: Power BI projects (PBIP) with TMDL models and PBIR reports, deployed to the workspaces through Fabric Git integration.
- **Workload**: [reports/spec.yaml](reports/spec.yaml) defines 20 visuals and pages of 1, 5, 10 and 20 visuals. [reports/generate.py](reports/generate.py) builds a report and the matching DAX queries for each model; the DAX was checked against Performance Analyzer captures in [reports/validation/](reports/validation/).
- **Harness**: a Fabric notebook ([harness/](harness/)) refreshes a model or runs its query workload, and reads the engine's own numbers from workspace monitoring (`SemanticModelLogs`) or from an XMLA trace where there is no monitoring. A local driver, [harness/run_variant.py](harness/run_variant.py), starts it and appends the results to [results/](results/). See [docs/harness.md](docs/harness.md).

## Repo layout

| Path | Contents |
|---|---|
| `models/` | One folder per model: the semantic model, its own report, a generated workload report, and a README with results |
| `reports/` | Workload spec, report and query generator, generated queries, validation captures |
| `harness/` | Fabric notebook, Lakehouse definition and the local driver |
| `results/` | `harness-runs.csv` (one row per refresh), `query-*.csv` (query runs), `results/harness/<run>/` (summary and log extracts of every run) |
| `analysis/` | KQL queries for workspace monitoring |
| `docs/` | Findings, harness documentation, data profile, screenshots of error messages and capacity metrics |
| `site/` | The compare page, published with GitHub Pages; `site/models.yaml` holds its display text |

## Running it yourself

You need Fabric workspaces on the capacities you want to test, connected to a fork of this repo through Git integration, with workspace monitoring turned on where you want server-side numbers. The workspace IDs in the harness are placeholders (`<F64-workspace-id>`, `<F2-workspace-id>`, `<PPU-workspace-id>`); replace them in [harness/run_variant.py](harness/run_variant.py) and [harness/refresh-harness.Notebook/notebook-content.py](harness/refresh-harness.Notebook/notebook-content.py). The result files keep the same placeholders where the original runs recorded a workspace ID.

The driver authenticates with your own Azure CLI sign-in (`az login`); no service principal and no secrets are stored anywhere in the repo. Refreshing on 10M data and running query workloads uses capacity units; on a small capacity it can overload the capacity for a while (see finding 8 in the query findings).

## Caveats

- Most results are single runs or a few runs. Refresh peaks of the same model vary by a few hundred MB between runs, and query times on F64 vary up to two times (query finding 7). The findings say where a result is confirmed and where it is not.
- The data is synthetic and the Parquet source cannot fold. With a source that folds (SQL), Power Query steps that fold cost no refresh memory.
- F64 was a trial capacity. Limits and behavior are those of November 2026.
