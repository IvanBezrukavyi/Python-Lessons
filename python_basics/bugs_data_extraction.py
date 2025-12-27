import csv
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).parent.resolve()
CSV_PATH = BASE_DIR / "data" / "bugs.csv"


def load_bugs_from_csv(filepath: Path) -> list[dict[str, Any]]:
    bugs = []

    with filepath.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            component = row["component"].strip().lower()

            if component == "":
                component = "unknown"

            row_id = row["id"].strip()
            try:
                bug_id = int(row_id)
            except ValueError:
                print("Skip row (bad id):", row)
                continue

            title = row["title"].strip()
            if title == "":
                print("Skip row (empty title):", row)
                continue

            status = row["status"].strip().lower()

            if status == "":
                status = "open"

            if status in ("in progress", "in-progress"):
                status = "in_progress"

            if status == "in_progresss":
                status = "in_progress"

            severity = row["severity"].strip().lower()
            if severity == "":
                continue

            if severity in ("p1", "blocker"):
                severity = "critical"
            bugs.append(
                {
                    "id": bug_id,
                    "title": title,
                    "severity": severity,
                    "status": status,
                    "component": component,
                }
            )
    return bugs


bugs = load_bugs_from_csv(CSV_PATH)
print(bugs)


# Count open bugs
def count_open_bugs(bugs: list[dict]) -> int:
    count = 0
    for b in bugs:
        if b["status"] == "open":
            count += 1
    return count


# Count payment bugs
def count_open_payment_bugs(bugs: list[dict]) -> int:
    count = 0

    for p in bugs:
        if p["status"] == "open" and "payment" in p["title"].lower():
            count += 1
    return count


print("Total open bugs:", count_open_bugs(bugs))
print("Total payment bugs:", count_open_payment_bugs(bugs))


# Group by severity + status
def count_bugs_by_severity_status(bugs: list[dict]) -> dict[str, int]:
    stats = {}

    for b in bugs:
        key = b["severity"] + "_" + b["status"]
        stats[key] = stats.get(key, 0) + 1

    return stats


print("By severity+status:", count_bugs_by_severity_status(bugs))

print("Statuses:", sorted({b["status"] for b in bugs}))
print("Severities:", sorted({b["severity"] for b in bugs}))


def normalize_status(raw: str) -> str:

    status = raw.strip().lower()

    if status == "":
        return "open"

    if status in ("in progress", "in-progress"):
        return "in_progress"

    if status == "in_progresss":
        return "in_progress"


print(normalize_status(" Open "))


def normalize_severity(raw: str) -> str:
    severity = raw.strip().lower()

    if severity == "":
        return ""

    if severity in ("p1", "blocker"):
        severity = "critical"
    return severity


print(normalize_severity("P1"))


def open_critical_by_component(bugs):
    stats = {}
    for b in bugs:
        if b["status"] == "open" and b["severity"] == "critical":
            print(b["id"], b["component"], b["title"])
            comp = b["component"]
            stats[comp] = stats.get(comp, 0) + 1
    return stats


stats = open_critical_by_component(bugs)
items = list(stats.items())
items.sort(key=lambda x: x[1], reverse=True)
print(items[:3])


def list_open_critical(bugs):
    result = []
    for b in bugs:
        if b["status"] == "open" and b["severity"] == "critical":
            result.append(b)
    return result


critical_open = list_open_critical(bugs)
print("Count:", len(critical_open))
print("First:", critical_open[0])
