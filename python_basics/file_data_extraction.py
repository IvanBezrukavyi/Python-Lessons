import csv

def load_users_from_csv(filepath):
        users = []

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    header = lines[0]      # "id,name,age,city\n"
    data_lines = lines[1:] # всі рядки з даними