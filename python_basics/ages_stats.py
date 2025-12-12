ages = [25, 30, 29, 35, 41, 38]
total = 0

# Task 1
for a in ages:
    total += a
average = round(total / len(ages), 2)
print(f"Average age is {average}")

# Task 2
max_age = ages[0]

for a in ages:
    if a > max_age:
        max_age = a
print(f"Max age is {max_age}")

# Task 3
count_30_plus = 0
for age in ages:
    if age >= 30:
        count_30_plus += 1
print(f"People aged 30+ : {count_30_plus}")

# Task 4
min_age = ages[0]

for age in ages:
    if age < min_age:
        min_age = age
print(f"Min age is {min_age}")
# or
min_age = min(ages)
print(f"Min age is {min_age}")
