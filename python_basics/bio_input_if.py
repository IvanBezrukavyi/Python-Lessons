name = input("What's your name? ")
age = int(input("How old are you? "))
city = input("Where are you from? ")

age_next_year = age + 1

print(f"Hi, {name}!")
print(f"You are {age} years old and you live in {city}.")
print(f"Next year you will be {age_next_year}.")

if age >= 18:
    print("You are adult!")
else:
    print("You are underage")

if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior")

city = city.strip().lower()

if age >= 18 and city == "dnipro":
    print("You are an adualt from Dnipro")
