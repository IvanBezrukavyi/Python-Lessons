ages = [25, 30, 29, 35, 41, 38]
total = 0

for a in ages:
    total_age = a + total
average = round(total_age / len(ages), 2)
print(f"Average age is {average}")

max_age = ages[0]

for a in ages:
    if a > max_age:
        max_age = a  
print(f"Max age is {max_age}") 