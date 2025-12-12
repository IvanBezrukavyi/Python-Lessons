# Task 1
def get_age_category(age: int) -> str:
    if age < 13:
        return "child"
    elif age < 18:
        return "teenager"
    elif age < 65:
        return "adult"
    else:
        return "senior"


name = input("What's your name? ")
age = int(input("How old are you? "))
raw_city = input("Where are you from? ")

city = raw_city.strip().lower()
category = get_age_category(age)

print(f"Hi, {name}!")
print(f"You are {age} years old and you live in {raw_city.strip()}.")
print(f"Your age category is: {category}.")


# Task 2
ages = [25, 30, 29, 35, 41, 38]


def get_age_stats(ages: list[int]) -> tuple[float, int, int, int]:
    average = round(sum(ages) / len(ages), 2)
    max_age = max(ages)
    min_age = min(ages)
    count_30_plus = len([a for a in ages if a >= 30])
    return average, max_age, min_age, count_30_plus


average, max_age, min_age, count_30_plus = get_age_stats(ages)
print("Average:", average)
print("Max:", max_age)
print("Min:", min_age)
print("30+:", count_30_plus)

# Task 4
bug_titles = [
    "Login error",
    "PAYMENT failed",
    "Page not found",
    "payment timeout",
    "CRASH on load",
]


def count_payment_bugs(bug_titles: list[str]) -> int:
    return len([p for p in bug_titles if "payment" in p.lower()])


payment_count = count_payment_bugs(bug_titles)
print("Payment-related bugs:", payment_count)
