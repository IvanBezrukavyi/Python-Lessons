users = [
    {"id": 1, "name": "Ivan", "age": 39, "city": "Dnipro"},
    {"id": 2, "name": "Olena", "age": 25, "city": "Kyiv"},
    {"id": 3, "name": "Oleh", "age": 17, "city": "Dnipro"},
    {"id": 4, "name": "Anna", "age": 30, "city": "Lviv"},
    {"id": 5, "name": "Max", "age": 15, "city": "Kyiv"},
]

# Task 1. Print users in such format as example:
# Ivan (39) from Dnipro, Olena (25) from Kyiv


def print_users(users):
    for user in users:
        username = user["name"]
        user_age = user["age"]
        user_city = user["city"]
        print(f"{username} ({user_age}) from {user_city}")


print_users(users)

# Task 2. Print all adult users (age more 18)


def print_users(users):
    for user in users:
        username = user["name"]
        user_age = user["age"]
        user_city = user["city"]

        if user_age >= 18:
            print(f"{username} ({user_age}) from {user_city}")
        else:
            print(f"{username} is too young")


print_users(users)

# Task 3. Count all adult users (age more 18)


def count_adult(users):
    count = 0

    for user in users:
        user_age = user["age"]

        if user_age >= 18:
            count += 1
    return count


result = count_adult(users)
print(result)

# Task 4. Create filter by city


def filter_users_by_city(users, city):
    filtered_users = []
    target_city = city.strip().lower()

    for user in users:
        if user.get("city", "").lower() == target_city:
            filtered_users.append(user)
    return filtered_users


dnipro_users = filter_users_by_city(users, "dNiPrO")
print(dnipro_users)


# Task 5. Count users by city


def count_users_by_city(users):
    stat = {}

    for user in users:
        city = user["city"]

        if city not in stat:
            stat[city] = 0
        stat[city] += 1
    return stat


result = count_users_by_city(users)
print(result)


# Count the average age by city


def average_age_by_city(users):
    stat = {}
    age_sums = {}

    for user in users:
        city = user["city"]
        age = user["age"]

        if city not in stat:
            stat[city] = 0
            age_sums[city] = 0

        stat[city] += 1
        age_sums[city] += age
    # Count the average
    average_result = {}

    for city in stat:
        average_result[city] = age_sums[city] / stat[city]
    return average_result


result = average_age_by_city(users)
print(result)
