
# Програма запитує в користувача:
# ім’я
# вік
# місто
# Потім виводить щось типу:
# Привіт, Іван!
# Тобі 39 років і ти живеш у місті Дніпро.
# Через рік тобі буде 40.

name = input("What's your name? ")
age = int(input("How old are you? "))
city = input("Where're you from? ")

age_next_year = age + 1

print(f"Hi, {name}!")
print(f"You are {age} years old and you live in {city}.")
print(f"Next year you will be {age_next_year}.")