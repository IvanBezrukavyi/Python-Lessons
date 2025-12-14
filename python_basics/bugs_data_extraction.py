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

            severity = row["severity"].strip().lower()
            if severity == "":
                print("Skip row (empty severity):", row)
                continue

            bugs.append(
                {
                    "id": bug_id,
                    "title": title,
                    "severity": severity,
                    "status": status,
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
        key = b["severity"] + "_" + b["status"]  # наприклад: "high_open"
        stats[key] = stats.get(key, 0) + 1

    return stats


print("By severity+status:", count_bugs_by_severity_status(bugs))

print("Statuses:", sorted(set(b["status"] for b in bugs)))
print("Severities:", sorted(set(b["severity"] for b in bugs)))
