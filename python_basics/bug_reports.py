# Count the total bug reports contain 'payment' word
bug_titles = [
    "Login error",
    "PAYMENT failed",
    "Page not found",
    "payment timeout",
    "CRASH on load"
]

total = 0

for p in bug_titles:
    if "payment" in p.lower():
        total += 1
print(f"Payment-related bugs: {total}")