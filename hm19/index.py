import json
import csv
import random
import os

def generate_phone_number():
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])

json_file_path = os.path.join('..', 'hm18', 'дані.json')

csv_file_path = os.path.join('..', 'hm19', 'дані.csv')

with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['ID', 'Ім\'я', 'Вік', 'Телефон']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for id_, record in data.items():
        name, age = record
        phone = generate_phone_number()
        writer.writerow({'ID': id_, 'Ім\'я': name, 'Вік': age, 'Телефон': phone})

print("Дані були успішно записані у файл", csv_file_path)
