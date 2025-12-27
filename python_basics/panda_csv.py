from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).parent.resolve()
CSV_PATH = BASE_DIR / "data" / "bugs.csv"

df = pd.read_csv(
    CSV_PATH,
    dtype={
        "title": "string",
        "severity": "string",
        "status": "string",
        "component": "string",
    },
)


df["id"] = pd.to_numeric(df["id"], errors="coerce").isna()
bad_rows = df["id"]

df["status"] = (
    df["status"]
    .astype("string")
    .str.strip()
    .str.lower()
    .replace({"": "open", "in-progres": "in_progress", "in progress": "in_progress"})
)


df["severity"] = df["severity"].replace({"p1": "critical", "blocker": "critical"})

df = df[df["title"] != ""]
df = df[df["severity"] != ""]


print(df.head(5))
print(bad_rows)

open_count = (df["status"] == "open").sum()
print("total open bugs:", open_count)

# Open + “payment” у title

open_payment_bugs = df[
    (df["status"] == "open")
    & (df["title"].str.contains("payment", case=False, na=False))
]
print("total open payment bug:", len(open_payment_bugs))

# Group by severity + status

by_severity_status = df.groupby(["severity", "status"]).size().reset_index(name="count")
print(by_severity_status.sort_values("count", ascending=False))


# Open + critical and sorted by component

open_critical = df[(df["status"] == "open") & (df["severity"] == "critical")]

top_components = (
    open_critical.groupby("component")
    .size()
    .reset_index(name="count")
    .sort_values("count", ascending=False)
)
print(top_components.head(10))
