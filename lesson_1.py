# Порахувати квадрат числа
# Порахувати квадрат кожного числа зі списку
square_list = [1, 2, 3, 4, 5]


def square(x):
    return x * x


print([square(x) for x in square_list])

# Як перевірити тип змінної name?
def greet (name):
    return (type(name))
print (greet("Anna"))

# ✍️ ЗАДАЧА 1:
# Напиши функцію get_age_category(age), яка повертає:
# - "child", якщо < 14
# - "teen", якщо 14-18
# - "adult", якщо 19-65
# - "senior", якщо > 65


def get_age_category(age):
    if age < 14:
        return "child"
    elif 14 <= age <= 18:
        return "teen"
    elif 19 <= age <= 65:
        return "adult"
    else:
        return "senior"


def calculate():
    a = 2
    b = 3
    c = 4
    return a + b * c


print(calculate())

# ✍️ ЗАДАЧА 2:
# Є список температур в градусах Цельсія: [23.5, 25.1, 19.8, 30.0]
# Напиши функцію, яка переведе їх у Фаренгейти (формула: F = C * 9/5 + 32)

cels_temp = [23.5, 25.1, 19.8, 30.0]

def to_fahrenheit(celsius_list):
    return [(c * 9)/5 + 32 for c in celsius_list]

far_temp = to_fahrenheit(cels_temp)
print(far_temp)