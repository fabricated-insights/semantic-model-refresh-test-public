"""Build site/data.json from the lab repo.

Run from anywhere:  python site/build_data.py
It writes site/data.json and refreshes the inline copy in site/index.html
(between the LAB-DATA markers), so the page also works from file://.

Sources, in order of trust:
  1. results/harness-runs.csv          every harness refresh
  2. results/monitoring-refreshes.csv  manual F64 refreshes from before the harness
  3. results/query-summary.csv, query-runs.csv, query-xmla.csv
  4. docs/lab-findings.md ("All runs")  sizes, F2 results, result texts not in the CSVs
  5. site/models.yaml                    display metadata (the only hand-written file)

MB means 1,048,576 bytes everywhere. Never hand-edit data.json.
"""

import csv
import difflib
import json
import re
import statistics
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
RESULTS = ROOT / "results"

warnings = []


def warn(msg):
    warnings.append(msg)


def num(text):
    """First number in a text like '1,833 MB on PPU'. None if there is none."""
    if text is None:
        return None
    m = re.search(r"-?\d[\d,]*(?:\.\d+)?", str(text))
    if not m:
        return None
    return float(m.group(0).replace(",", ""))


def fnum(text):
    """A plain CSV number ('', '<NA>' and 'nan' are None)."""
    if text is None:
        return None
    t = str(text).strip().replace(",", "")
    if t in ("", "<NA>", "nan", "None"):
        return None
    try:
        return float(t)
    except ValueError:
        return None


def size_of(data_tag):
    return {"data-1m-v1": "1M", "data-10m-v1": "10M"}.get(data_tag)


def read_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def md_table(path, heading):
    """Rows of the first markdown table after a heading, as dicts."""
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == heading)
    except StopIteration:
        sys.exit(f"{path.name}: heading {heading!r} not found")
    rows, header = [], None
    for line in lines[start + 1:]:
        if line.startswith("#"):
            break
        if not line.startswith("|"):
            if header:
                break
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            header = cells
        elif set(line.replace("|", "").strip()) <= set("-: "):
            continue
        else:
            rows.append(dict(zip(header, cells)))
    return rows


def r1(x, nd=1):
    return None if x is None else round(x, nd)


# ---------------------------------------------------------------- metadata

meta = yaml.safe_load((SITE / "models.yaml").read_text(encoding="utf-8"))
models = meta["models"]
by_folder = {m["folder"]: m for m in models}
by_id = {m["id"]: m for m in models}
for m in models:
    if m["category"] not in meta["categories"]:
        sys.exit(f"models.yaml: {m['id']} has unknown category {m['category']!r}")
    if not (ROOT / "models" / m["folder"]).is_dir():
        sys.exit(f"models.yaml: folder models/{m['folder']} does not exist")

keys = [f"{m['id']}@{s}" for m in models for s in m["sizes"]]


def key_for(folder, size):
    m = by_folder.get(folder)
    return f"{m['id']}@{size}" if m and size else None


# ---------------------------------------------------------------- refreshes

refreshes = {k: [] for k in keys}  # every refresh, any capacity


def failure_text(r):
    """The harness failure kind, with Pro's model size error spelled out instead of "other"."""
    m = re.search(r"dataset of size (\d+) MB exceeds the limit of (\d+) MB", r.get("error_text") or "")
    if m:
        return f"model size {int(m[1]):,} MB over the {int(m[2]):,} MB limit"
    return r["failure_kind"]


def minsec(minutes):
    """Duration as seconds below two minutes, else as minutes."""
    return f"{minutes * 60:,.0f} s" if minutes < 2 else f"{minutes:,.0f} min"


for r in read_csv(RESULTS / "harness-runs.csv"):
    k = key_for(r["variant"], size_of(r["data_tag"]))
    if k not in refreshes:
        continue
    when = (r["refresh_end_utc"] or r["timestamp_utc"]).replace("T", " ").rstrip("Z")
    refreshes[k].append({
        "src": "harness",
        "run": r["harness_run_id"],
        "when": when,
        "cap": r["capacity"],
        "ok": r["result"] == "refreshed",
        "failure": failure_text(r),
        "peak": fnum(r["peak_mb"]),
        "pq": fnum(r["pq_peak_mb"]),
        "dur": fnum(r["duration_min"]),
        "cpu": fnum(r["total_cpu_sec"]),
        "size": fnum(r["model_size_mb"]),
        "size_src": r["model_size_source"],
        "after": fnum(r.get("size_after_mb")),
    })

# monitoring-refreshes.csv has no data tag. All of it is 1M except the two
# 10M runs of v00 and v23 on 2026-11-06, which loaded about 10 and 4.6 times
# the rows of that model's 1M run. A completed refresh that loaded at least
# 4 times the rows of the same model's smallest completed refresh is 10M.
mon = read_csv(RESULTS / "monitoring-refreshes.csv")
min_rows = {}
for r in mon:
    if r["Result"] == "refreshed":
        rows = fnum(r["RowsLoaded"])
        min_rows[r["Model"]] = min(rows, min_rows.get(r["Model"], rows))
for r in mon:
    ok = r["Result"] == "refreshed"
    rows = fnum(r["RowsLoaded"])
    size = "10M" if ok and rows >= 4 * min_rows[r["Model"]] else "1M"
    k = key_for(r["Model"], size)
    if k not in refreshes:
        continue
    refreshes[k].append({
        "src": "monitoring",
        "run": None,
        "when": r["Timestamp"][:19],
        "cap": "F64",
        "ok": ok,
        "failure": "" if ok else "failed",
        "peak": fnum(r["PeakMemMB"]),
        "pq": fnum(r["MEnginePeakMB"]),
        "dur": fnum(r["DurationMin"]),
        "cpu": fnum(r["TotalCpuSec"]),
        "size": None, "size_src": "", "after": None,
    })

# ---------------------------------------------------------------- doc table

doc_rows = {}
for row in md_table(ROOT / "docs" / "lab-findings.md", "## All runs"):
    mid = row["Model"].split("-")[0]
    what = row["What it is"]
    size = "10M" if re.search(r",\s*10M$", what) else "1M"
    doc_rows[f"{mid}@{size}"] = row


def split_ppu(text):
    """'failed at 25.6 GB (PPU: refreshed, peak 26,115)' -> ('failed at 25.6 GB', 'refreshed, peak 26,115')."""
    m = re.match(r"^(.*?)\s*\(PPU:\s*(.*)\)\s*$", text or "")
    return (m.group(1), m.group(2)) if m else (text or "", "")


def mb_after_failed_at(text):
    """'failed at 3,242' -> 'failed at 3,242 MB'."""
    return re.sub(r"(failed at [\d,]+)(?![\d,.]*\s*(?:MB|GB))", r"\1 MB", text)


# ---------------------------------------------------------------- queries

summ = read_csv(RESULTS / "query-summary.csv")
runs = read_csv(RESULTS / "query-runs.csv")
xmla = read_csv(RESULTS / "query-xmla.csv")

QUERY_LIMIT_F2 = 1024


def queries(folder, size):
    tag = {"1M": "data-1m-v1", "10M": "data-10m-v1"}[size]
    mine = [r for r in summ if r["variant"] == folder and r["data_tag"] == tag]
    p20, cpu = [], []
    for r in mine:
        if (r["capacity"], r["page"], r["mode"], r["conc"]) != ("F64", "p20", "cold", "page"):
            continue
        n = (fnum(r["visuals"]) or 0) * (fnum(r["repeats"]) or 0)
        # A run where most queries failed (no data in the model) is not a measurement.
        if n and (fnum(r["errors"]) or 0) / n >= 0.5:
            continue
        if fnum(r["server_max_median_ms"]) is not None:
            p20.append(fnum(r["server_max_median_ms"]))
            cpu.append(fnum(r["cpu_sum_median_ms"]))
    # Heaviest single query: cold cache, all visuals at once (as in the doc), plus XMLA runs.
    peaks = [(fnum(r["peak_mem_max_kb"]), r["page"]) for r in mine
             if (r["capacity"], r["mode"], r["conc"]) == ("F64", "cold", "page")
             and fnum(r["peak_mem_max_kb"]) is not None]
    peaks += [(fnum(r["peak_mem_kb"]), r["page"]) for r in xmla
              if r["variant"] == folder and r["data_tag"] == tag and r["capacity"] == "F64"
              and fnum(r["peak_mem_kb"]) is not None]
    if not p20 and not peaks:
        return None
    q = {"runs": len(p20)}
    if p20:
        q["p20"] = [min(p20), max(p20)]
        q["cpu"] = [min(cpu), max(cpu)]
    if peaks:
        kb, page = max(peaks)
        q["qpeak"] = r1(kb / 1024)
        q["qpeakPage"] = page

    # F2: REST runs, p20. The two matrices (v01, v20) always fail over REST with
    # DaxResultsetCountNotSupported, which says nothing about the capacity.
    f2 = [r for r in runs if r["variant"] == folder and r["data_tag"] == tag
          and r["capacity"] == "F2" and r["page"] == "p20"]
    parts = []
    if f2:
        visuals = {r["visual"] for r in f2}
        api = {r["visual"] for r in f2 if "DaxResultsetCountNotSupported" in (r["server_error"] + r["client_error"])}
        bad = [r for r in f2 if r["failed"] == "True" and r["visual"] not in api]
        failed = {r["visual"] for r in bad}
        if failed:
            why = ""
            if all("Resource Governance" in r["client_error"] + r["server_error"] for r in bad):
                why = f": query memory over the {QUERY_LIMIT_F2:,} MB limit"
            parts.append(f"{len(failed)} of {len(visuals)} visuals fail on F2{why}")
        else:
            parts.append(f"no memory errors ({len(visuals) - len(api)} of {len(visuals)} visuals checked; "
                         f"the {len(api)} matrices can't run over the REST API)")
    fx = [fnum(r["peak_mem_kb"]) for r in xmla if r["variant"] == folder and r["data_tag"] == tag
          and r["capacity"] == "F2" and r["failed"] == "False" and fnum(r["peak_mem_kb"]) is not None]
    if fx:
        top = max(fx) / 1024
        parts.append(f"over XMLA the heaviest query ran at {top:,.0f} MB, "
                     f"{top / QUERY_LIMIT_F2 * 100:.0f}% of F2's {QUERY_LIMIT_F2:,} MB per-query limit")
    if parts:
        q["f2q"] = "; ".join(parts) + "."
    return q


# ---------------------------------------------------------------- model diffs

BASE_FOLDER = "v00-baseline"
DIFF_MAX_LINES = 160  # per file; the rest is a link to the file on GitHub
# Tables Power BI generates for Auto date/time: summarised, not listed line by line.
GENERATED = re.compile(r"^tables/(LocalDateTable|DateTableTemplate)_")


def tmdl_files(folder):
    """The model definition as {path: lines}, without the noise a save adds:
    line endings, trailing spaces and lineageTag lines, which Power BI
    regenerates and which differ between any two copies of the same table."""
    root = ROOT / "models" / folder / f"{folder}.SemanticModel" / "definition"
    out = {}
    for p in sorted(root.rglob("*.tmdl")):
        rel = p.relative_to(root).as_posix()
        if rel.startswith("cultures/"):  # linguistic metadata, not the model
            continue
        lines = [l.rstrip() for l in p.read_text(encoding="utf-8-sig").splitlines()]
        out[rel] = [l for l in lines if not re.match(r"\s*(source)?[lL]ineageTag:", l)]
    return out


def unified(a, b, n=3):
    """Unified diff lines (hunk headers and ' ', '-', '+' lines). Like
    difflib.unified_diff, but with autojunk off: otherwise lines that repeat a
    lot in a long file (blank lines, formatString) count as junk, never match,
    and unchanged lines show up as removed and added again."""
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for group in sm.get_grouped_opcodes(n):
        i1, i2, j1, j2 = group[0][1], group[-1][2], group[0][3], group[-1][4]
        yield f"@@ -{i1 + 1},{i2 - i1} +{j1 + 1},{j2 - j1} @@"
        for tag, a1, a2, b1, b2 in group:
            if tag == "equal":
                yield from (" " + l for l in a[a1:a2])
                continue
            yield from ("-" + l for l in a[a1:a2])
            yield from ("+" + l for l in b[b1:b2])


def model_diff(folder, base):
    """Unified diff against the baseline, per file, for the git-diff view."""
    mine = tmdl_files(folder)
    files, generated = [], {"files": 0, "lines": 0}
    for path in sorted(set(base) | set(mine)):
        a, b = base.get(path, []), mine.get(path, [])
        if a == b:
            continue
        status = "added" if path not in base else "removed" if path not in mine else "modified"
        if GENERATED.match(path):
            generated["files"] += 1
            generated["lines"] += len(b) or len(a)
            continue
        hunks, cur, shown, cut, add, rem = [], None, 0, 0, 0, 0
        for line in unified(a, b):
            add += line.startswith("+")
            rem += line.startswith("-")
            if line.startswith("@@"):
                cur = [line, []]
                hunks.append(cur)
                continue
            if shown >= DIFF_MAX_LINES:
                cut += 1
                continue
            cur[1].append(line)
            shown += 1
        hunks = [h for h in hunks if h[1]]
        f = {"path": path, "status": status, "add": add, "del": rem, "hunks": hunks}
        if cut:
            f["cut"] = cut
        files.append(f)
    d = {"files": files}
    if generated["files"]:
        d["generated"] = generated
    return d


base_files = tmdl_files(BASE_FOLDER)
diffs = {}

# ---------------------------------------------------------------- records

out = []
for m in models:
    for size in m["sizes"]:
        k = f"{m['id']}@{size}"
        rs = sorted(refreshes[k], key=lambda r: r["when"])
        if m.get("ignore_before"):
            # Runs of an earlier version of the model, before it was changed.
            rs = [r for r in rs if r["when"] >= m["ignore_before"]]
        doc = doc_rows.get(k, {})
        if not rs and not doc:
            warn(f"{k}: no refresh in the CSVs and no row in lab-findings.md, left out")
            continue

        f64 = [r for r in rs if r["cap"] == "F64"]
        f64_ok = [r for r in f64 if r["ok"] and r["peak"] is not None]
        ppu = [r for r in rs if r["cap"] == "PPU"]
        f2 = [r for r in rs if r["cap"] == "F2"]

        rec = {
            "key": k, "id": m["id"], "folder": m["folder"], "size": size,
            "name": m["name"], "category": m["category"], "desc": m["desc"],
            # A failed refresh has no peak: only completed F64 runs go in.
            "peaks": [r1(r["peak"], 0) for r in f64_ok],
            # Power Query peak of the same runs, in the same order as peaks
            "pqs": [r1(r["pq"], 0) for r in f64_ok],
        }
        if f64_ok:
            last = f64_ok[-1]
            rec.update(pq=r1(last["pq"], 0), dur=r1(last["dur"], 2), cpu=r1(last["cpu"], 0))
        rec["runs"] = len(f64)
        # Every refresh, any capacity, for the "All runs" table. A failed run keeps the
        # value where the engine stopped, marked as such, never as a peak.
        rec["runlist"] = [{
            "date": r["when"][:10], "cap": r["cap"], "ok": r["ok"],
            "peak": r1(r["peak"], 0) if r["ok"] else None,
            "stopped": r1(r["peak"], 0) if not r["ok"] else None,
            "failure": r["failure"] or None,
            "pq": r1(r["pq"], 0) if r["ok"] else None,
            "dur": r1(r["dur"], 2), "cpu": r1(r["cpu"], 0),
            "run": r.get("run"), "src": r["src"],
        } for r in rs]
        rec["fails"] = len([r for r in f64 if not r["ok"]])

        doc_f64, doc_ppu = split_ppu(doc.get("F64 result", ""))
        rec["f64"] = doc_f64 or ("refreshed" if f64_ok else ("failed" if f64 else "not run"))
        if f64_ok and not rec["f64"].startswith("refreshed"):
            warn(f"{k}: completed F64 runs in the CSVs but lab-findings says {rec['f64']!r}")

        doc_f2 = doc.get("F2 result", "")
        if doc_f2:
            rec["f2"] = mb_after_failed_at(doc_f2)
        elif f2:
            rec["f2"] = "refreshed" if f2[-1]["ok"] else "failed"
        else:
            rec["f2"] = "not run"

        if ppu:
            p = ppu[-1]
            if p["ok"]:
                rec["ppu"] = f"refreshed, peak {p['peak']:,.0f} MB"
                rec.update(ppuPeak=r1(p["peak"], 0), ppuPq=r1(p["pq"], 0),
                           ppuDur=r1(p["dur"], 2), ppuCpu=r1(p["cpu"], 0))
            else:
                at = f" at {p['peak']:,.0f} MB" if p["peak"] is not None else ""
                rec["ppu"] = f"failed{at}, {p['failure'] or 'error'}"
        else:
            rec["ppu"] = doc_ppu or "not run"

        # Sizes, in the order the findings use: F64 from the CSVs (latest completed run),
        # then the doc table (F64 unless it says "on PPU"), then PPU from the CSVs,
        # labelled. Older F64 sizes are only in the doc, so the doc comes before PPU.
        def size_pick(runs, value, doc_text, field):
            f64_runs = [r for r in runs if r["cap"] != "PPU"]
            if f64_runs:
                rec[field] = r1(value(f64_runs[-1]))
            elif num(doc_text) is not None:
                rec[field] = r1(num(doc_text))
                if "on PPU" in doc_text:
                    rec[field + "On"] = "PPU"
            elif runs:
                rec[field] = r1(value(runs[-1]))
                rec[field + "On"] = "PPU"
            else:
                rec[field] = None

        svc = [r for r in rs if r["ok"] and r["size"] is not None and r["size_src"].startswith("Backup step")]
        size_pick(svc, lambda r: r["size"], doc.get("Service size", ""), "service")
        mem = [r for r in rs if r["ok"] and (r["after"] is not None or
               (r["size"] is not None and r["size_src"].startswith("INFO.STORAGE")))]
        size_pick(mem, lambda r: r["after"] if r["after"] is not None else r["size"],
                  doc.get("In memory after refresh", ""), "memory")
        rec["pbix"] = r1(num(doc.get("Downloaded .pbix")))
        if "on PPU" in doc.get("Downloaded .pbix", ""):
            rec["pbixOn"] = "PPU"

        # Cross-check the doc's F64 peak against the CSV runs.
        doc_peak = doc.get("F64 peak MB", "")
        if doc_peak and rec["peaks"]:
            nums = [float(x.replace(",", "")) for x in re.findall(r"\d[\d,]*", doc_peak)
                    if len(x.replace(",", "")) >= 3]
            for n in nums:
                if n not in rec["peaks"]:
                    warn(f"{k}: lab-findings peak {n:,.0f} is not among the CSV peaks {rec['peaks']}")
        elif doc_peak and not rec["peaks"] and num(doc_peak) and rec["f64"].startswith("refreshed"):
            rec["peaks"] = [num(doc_peak)]
            warn(f"{k}: peak {doc_peak} from lab-findings.md only")

        q = queries(m["folder"], size)
        if q:
            if m.get("qnote"):
                q["note"] = m["qnote"]
            rec["q"] = q
        if m.get("refnote"):
            rec["refnote"] = m["refnote"]
        if m["folder"] not in diffs:
            diffs[m["folder"]] = model_diff(m["folder"], base_files)
        # Pro: harness runs first; models.yaml holds the one manual run from before the harness (v99).
        pro = [r for r in rs if r["cap"] == "Pro"]
        if pro:
            last = pro[-1]
            if last["ok"]:
                rec["pro"] = "refreshed" + (f", {minsec(last['dur'])}" if last["dur"] is not None else "")
            else:
                rec["pro"] = "failed" + (f", {last['failure']}" if last["failure"] else "")
        elif m.get("pro"):
            rec["pro"] = m["pro"]
        for k in ("why", "fix"):
            if m.get(k):
                rec[k] = m[k]
        if m.get("diffnote"):
            rec["diffnote"] = m["diffnote"]
        out.append(rec)

missing_docs = [k for k in doc_rows if k not in {r["key"] for r in out}]
if missing_docs:
    warn("in lab-findings.md but not on the site: " + ", ".join(missing_docs))

site = meta["site"]
data = {
    # The date of the newest run in the data, not the build time, so the output only
    # changes when the data does.
    "latest": max([r["when"][:10] for rs in refreshes.values() for r in rs] +
                  [r["client_start_utc"][:10] for r in runs if r["client_start_utc"]]),
    "title": site.get("title", ""),
    "subtitle": site.get("subtitle", ""),
    "intro": site.get("intro", ""),
    "repo": site["repo"],
    "branch": site.get("branch", "main"),
    "articles": site.get("articles", []),
    "default": site["default"],
    "categories": meta["categories"],
    "presets": meta.get("presets", []),
    "caveats": meta.get("caveats", []),
    "models": out,
    "base": BASE_FOLDER,
    "diffs": diffs,
}
for p in data["presets"]:
    for side in ("a", "b"):
        if p[side] not in {r["key"] for r in out}:
            sys.exit(f"models.yaml: preset {p['label']!r} uses unknown key {p[side]}")

# Each model's cleaned definition, for the A-vs-B diff the page computes on demand.
# One small file per model folder; the page fetches only the two it compares.
tmdl_dir = SITE / "tmdl"
tmdl_dir.mkdir(exist_ok=True)
wanted = {f"{f}.json" for f in diffs}
for old in tmdl_dir.glob("*.json"):
    if old.name not in wanted:
        old.unlink()
for folder in diffs:
    (tmdl_dir / f"{folder}.json").write_text(
        json.dumps(tmdl_files(folder), ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")

text = json.dumps(data, ensure_ascii=False, indent=1)
(SITE / "data.json").write_text(text + "\n", encoding="utf-8")

# Inline copy for file://, between the markers in index.html.
index = SITE / "index.html"
if index.exists():
    html = index.read_text(encoding="utf-8")
    inline = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    new, n = re.subn(r"(<!-- LAB-DATA -->).*?(<!-- /LAB-DATA -->)",
                     lambda mt: f'{mt.group(1)}<script id="lab-data" type="application/json">{inline}</script>{mt.group(2)}',
                     html, flags=re.S)
    if n != 1:
        sys.exit("index.html: LAB-DATA markers not found")

    # Link preview (Open Graph, Twitter) and favicon, from models.yaml.
    def attr(t):
        return t.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")
    url = site.get("url", "").rstrip("/") + "/"
    title, desc = site.get("title", ""), site.get("description", "")
    icon = ("data:image/svg+xml,"
            "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
            "%3Crect x='1' y='4' width='14' height='24' rx='4' fill='%23175E85'/%3E"
            "%3Crect x='17' y='4' width='14' height='24' rx='4' fill='%23E8792E'/%3E%3C/svg%3E")
    meta = "\n".join([
        f'<meta name="description" content="{attr(desc)}">',
        f'<meta property="og:type" content="website">',
        f'<meta property="og:title" content="{attr(title)}">',
        f'<meta property="og:description" content="{attr(desc)}">',
        f'<meta property="og:url" content="{attr(url)}">',
        f'<meta property="og:image" content="{attr(url)}og.png">',
        f'<meta property="og:image:width" content="1200">',
        f'<meta property="og:image:height" content="630">',
        f'<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{attr(title)}">',
        f'<meta name="twitter:description" content="{attr(desc)}">',
        f'<meta name="twitter:image" content="{attr(url)}og.png">',
        f'<link rel="icon" href="{icon}">',
    ])
    new, n = re.subn(r"(<!-- LAB-META -->).*?(<!-- /LAB-META -->)",
                     lambda mt: f"{mt.group(1)}\n{meta}\n{mt.group(2)}", new, flags=re.S)
    if n != 1:
        sys.exit("index.html: LAB-META markers not found")
    index.write_text(new, encoding="utf-8")

print(f"data.json: {len(out)} records")
for w in warnings:
    print("note:", w)
