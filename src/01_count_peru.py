"""Download CRyPTIC open tables and count Peruvian isolates, lineages and phenotypes.

Usage: python src/01_count_peru.py   (writes data/peru_summary.csv)
"""
from pathlib import Path
import urllib.request
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
BASE = "https://ftp.ebi.ac.uk/pub/databases/cryptic/release_june2022"
FILES = {
    "reuse.csv": f"{BASE}/reuse/CRyPTIC_reuse_table_20240917.csv",
    "SAMPLES.csv.gz": f"{BASE}/reproducibility/data_tables/cryptic-analysis-group/SAMPLES.csv.gz",
    "SITES.csv": f"{BASE}/reproducibility/data_tables/cryptic-analysis-group/SITES.csv",
    "MYKROBE_LINEAGE.csv.gz": f"{BASE}/reproducibility/data_tables/cryptic-analysis-group/MYKROBE_LINEAGE.csv.gz",
}
DRUGS = ["AMI", "BDQ", "CFZ", "DLM", "EMB", "ETH", "INH", "KAN", "LEV", "LZD", "MXF", "RIF", "RFB"]


def fetch():
    RAW.mkdir(parents=True, exist_ok=True)
    for name, url in FILES.items():
        dest = RAW / name
        if not dest.exists():
            print("downloading", url)
            urllib.request.urlretrieve(url, dest)


def main():
    fetch()
    r = pd.read_csv(RAW / "reuse.csv")
    s = pd.read_csv(RAW / "SAMPLES.csv.gz", dtype=str)
    lin = pd.read_csv(RAW / "MYKROBE_LINEAGE.csv.gz")
    parts = r.UNIQUEID.str.split(".")
    r["SITEID"] = parts.str[1]
    r["SUBJID"] = parts.str[3]
    r["LABID"] = r.UNIQUEID.str.split(".lab.").str[1].str.split(".iso").str[0]
    m = r.merge(s[["SITEID", "SUBJID", "LABID", "COUNTRY_WHERE_SAMPLE_TAKEN"]],
                on=["SITEID", "SUBJID", "LABID"], how="left")
    print("reuse table rows:", len(r))
    per = m[m.COUNTRY_WHERE_SAMPLE_TAKEN == "PER"].merge(lin, on="UNIQUEID", how="left")
    print("Peruvian isolates (COUNTRY_WHERE_SAMPLE_TAKEN == PER):", len(per))
    print(per.MYKROBE_LINEAGE_NAME_1.value_counts(dropna=False).to_string())
    rows = []
    for d in DRUGS:
        vc = per[f"{d}_BINARY_PHENOTYPE"].value_counts()
        rows.append({"drug": d, "R": int(vc.get("R", 0)), "I": int(vc.get("I", 0)),
                     "S": int(vc.get("S", 0)), "NA": int(per[f"{d}_BINARY_PHENOTYPE"].isna().sum())})
    out = pd.DataFrame(rows)
    print(out.to_string(index=False))
    out.to_csv(ROOT / "data" / "peru_summary.csv", index=False)
    per[["UNIQUEID", "ENA_RUN", "MYKROBE_LINEAGE_NAME_1", "MYKROBE_LINEAGE_NAME_2"]].to_csv(
        ROOT / "data" / "peru_isolates.csv", index=False)


if __name__ == "__main__":
    main()
