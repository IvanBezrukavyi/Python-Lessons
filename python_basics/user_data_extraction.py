import csv
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "data" / "users.csv"


def load_users_from_csv(filepath: Path) -> list[dict[str, Any]]:
    users = []

    with filepath.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            users.append(
                {
                    "id": int(row["id"].strip()),
                    "name": row["name"].strip(),
                    "age": int(row["age"].strip()),
                    "city": row["city"].strip(),
                }
            )

    return users


users = load_users_from_csv(CSV_PATH)
print(users)

# Count adult


def count_adults(users):
    return sum(1 for u in users if u["age"] >= 18)


print("Adults:", count_adults(users))

# Count by city


def count_users_by_city(users):
    stats = {}
    for u in users:
        city = u["city"]
        stats[city] = stats.get(city, 0) + 1
    return stats


print("Users by city:", count_users_by_city(users))

# Count the average age by city


def average_age_by_city(users):
    sums = {}
    counts = {}

    for u in users:
        city = u["city"]
        sums[city] = sums.get(city, 0) + u["age"]
        counts[city] = counts.get(city, 0) + 1

    return {city: round(sums[city] / counts[city], 2) for city in counts}


print("Avg age by city:", average_age_by_city(users))
