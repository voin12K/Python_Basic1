import json

data = {
    123456: ('Іван', 30),
    234567: ('Марія', 25),
    345678: ('Петро', 35),
    456789: ('Олена', 28),
    567890: ('Андрій', 40),
    678901: ('Катерина', 22)
}

with open('дані.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
